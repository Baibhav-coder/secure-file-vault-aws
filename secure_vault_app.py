import os
import hmac
import hashlib
import base64
from datetime import datetime

import streamlit as st
import boto3

# ----------------------------
# AWS CONFIG
# ----------------------------

REGION = "us-east-1"
USER_POOL_ID = "us-east-1_kwfnGYzPj"
CLIENT_ID = "3tfkk9mtmavses3jkfhs3cd9jd"
CLIENT_SECRET = "n73iup1ve176lllfin784meto068lerd3nok0gr51m2aknvk076"

BUCKET_NAME = "mycloudprojcybersec"

# AWS clients
cognito = boto3.client("cognito-idp", region_name=REGION)
s3 = boto3.client("s3")

# ----------------------------
# ROLE MAPPING (LOCKED)
# ----------------------------

USER_ROLES = {
    "admin@test.com": "Admin",
    "editor@test.com": "Editor",
    "viewer@test.com": "Viewer"
}

ROLE_PERMISSIONS = {
    "Admin": {"engineering", "finance", "hr", "legal"},
    "Editor": {"engineering", "finance", "hr"},
    "Viewer": {"engineering"}  # viewer only sees engineering
}

# ----------------------------
# SECRET HASH
# ----------------------------

def get_secret_hash(username):
    message = username + CLIENT_ID
    dig = hmac.new(
        CLIENT_SECRET.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256,
    ).digest()

    return base64.b64encode(dig).decode()


# ----------------------------
# LOGIN FUNCTION
# ----------------------------

def cognito_login(username, password):
    try:
        cognito.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
                "SECRET_HASH": get_secret_hash(username),
            },
        )
        return True
    except:
        return False


# ----------------------------
# SESSION STATE
# ----------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ----------------------------
# LOGIN UI
# ----------------------------

if not st.session_state.authenticated:

    st.title("🔐 Secure File Vault Login")

    username = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if cognito_login(username, password):

            role = USER_ROLES.get(username)

            if role is None:
                st.error("User not authorized")
                st.stop()

            st.session_state.authenticated = True
            st.session_state.user = username
            st.session_state.role = role

            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Secure File Vault",
    page_icon="🔐",
    layout="wide",
)

st.title("🔐 Secure File Vault")

# ----------------------------
# USER INFO (NO DROPDOWN)
# ----------------------------

user = st.session_state.user
role = st.session_state.role

with st.sidebar:
    st.header("Session Info")
    st.write(f"User: {user}")
    st.write(f"Role: {role}")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# ----------------------------
# S3 FUNCTIONS
# ----------------------------

def upload_to_s3(file, folder):
    key = f"secure-vault/{folder}/{file.name}"
    s3.upload_fileobj(file, BUCKET_NAME, key)
    return key


def list_files(folder):
    prefix = f"secure-vault/{folder}/"

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=prefix,
    )

    files = []

    if "Contents" in response:
        for obj in response["Contents"]:
            files.append(obj)

    return files


# ----------------------------
# FOLDERS
# ----------------------------

FOLDERS = {
    "engineering": "Project documents and technical files",
    "finance": "Invoices, budgets, and confidential finance records",
    "hr": "Employee and internal HR documents",
    "legal": "Contracts and legal records",
}

allowed_folders = list(ROLE_PERMISSIONS[role])

# ----------------------------
# MAIN UI
# ----------------------------

col1, col2 = st.columns([2, 1], gap="large")

with col1:

    st.subheader("Vault Folders")

    folder_cols = st.columns(2)

    for idx, folder in enumerate(FOLDERS.keys()):

        with folder_cols[idx % 2]:

            allowed = folder in ROLE_PERMISSIONS[role]

            st.markdown(f"### {folder.capitalize()}")
            st.write(FOLDERS[folder])
            st.write(f"Access: {'✅ Allowed' if allowed else '❌ Not allowed'}")

    st.markdown("---")
    st.subheader("Upload Files")

    selected_folder = st.selectbox("Choose target folder", allowed_folders)

    if role == "Viewer":
        st.warning("Viewer cannot upload files")
    else:

        uploaded_files = st.file_uploader(
            "Drag and drop files here",
            accept_multiple_files=True,
        )

        if uploaded_files:

            if st.button("Upload to Vault"):

                for file in uploaded_files:
                    upload_to_s3(file, selected_folder)

                st.success("Files uploaded successfully")

# ----------------------------
# FILE LIST
# ----------------------------

with col2:

    st.subheader("Recent Files")

    recent_folder = st.selectbox(
        "View folder contents",
        allowed_folders,
        key="recent_folder",
    )

    files = list_files(recent_folder)

    if not files:
        st.write("No files uploaded yet.")
    else:

        for obj in files[:10]:

            file_key = obj["Key"]
            filename = file_key.split("/")[-1]

            modified = obj["LastModified"].strftime("%Y-%m-%d %H:%M")

            st.write(f"**{filename}**")
            st.caption(f"Modified: {modified}")

            url = s3.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": BUCKET_NAME,
                    "Key": file_key,
                },
                ExpiresIn=3600,
            )

            st.markdown(f"[Download]({url})")