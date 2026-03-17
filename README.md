# 🔐 Cloud Secure File Vault

> A secure, cloud-native file storage system built with AWS — simulating real-world enterprise data protection using authentication, authorization, and cloud security best practices.

---

## 📌 Overview

This project is a secure, cloud-based file storage system that demonstrates how organisations can protect sensitive documents across departments — Engineering, Finance, HR, and Legal — using **Role-Based Access Control (RBAC)** and AWS-native security services.

It replicates real enterprise scenarios where:
- Sensitive files must be protected from unauthorised access
- Different roles require different access levels
- Manual access control is insecure and error-prone
- Centralised, auditable storage is essential

---

## 🏗️ Architecture

```
User
 │
 ▼
Streamlit App (AWS Elastic Beanstalk)
 │
 ├──► AWS Cognito          → Authentication + Secret Hash (HMAC-SHA256)
 │
 ├──► IAM Role/Policy      → Authorisation (RBAC enforcement)
 │
 ├──► Amazon S3            → Secure Storage (SSE, Versioning, HTTPS-only, Pre-signed URLs)
 │
 ├──► AWS CloudTrail       → Audit Logging (all access + denied attempts)
 │
 └──► CloudWatch + SNS     → Real-time Alerts on suspicious activity
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | Streamlit |
| **Backend** | Python |
| **Cloud Platform** | Amazon Web Services (AWS) |
| **Authentication** | AWS Cognito |
| **Authorisation** | IAM Roles & Policies |
| **Storage** | Amazon S3 (SSE + Versioning + HTTPS enforcement) |
| **Deployment** | AWS Elastic Beanstalk |
| **Audit Logging** | AWS CloudTrail |
| **Alerting** | AWS CloudWatch + SNS |

---

## 🚀 Enterprise Security Features Implemented

| # | Feature | Description |
|---|---|---|
| 🔐 | **Authentication via AWS Cognito** | Secure user login with secret hash (HMAC-SHA256) |
| 👥 | **Role-Based Access Control (RBAC)** | Enforced roles: Admin, Editor, Viewer — restricted in both UI and backend (no bypass possible) |
| 🗂️ | **Secure File Storage (Amazon S3)** | Structured storage with department-level folder isolation |
| 🔒 | **Encryption at Rest** | S3 server-side encryption (SSE) enabled across all stored files |
| 🔑 | **IAM Role-Based Authorisation** | Fine-grained IAM policies governing all S3 interactions |
| 📥 | **Pre-Signed URLs for Secure Downloads** | Time-limited, scoped access links — no permanent public exposure |
| 📊 | **Audit Logging with AWS CloudTrail** | Tracks all access attempts, including unauthorised actions |
| 🚨 | **Real-Time Alerts via CloudWatch + SNS** | Email alerts triggered on suspicious or denied access events |
| 📦 | **S3 Versioning Enabled** | File version tracking and recovery capability |
| 🔐 | **Secure Transport Enforcement (HTTPS only)** | Bucket policy enforces TLS — insecure access is blocked |
| 🔑 | **Environment-Based Secret Management** | No hardcoded credentials — all secrets handled via Beanstalk environment variables |

---

## 👥 Role-Based Access Control

| Role | Access Level |
|---|---|
| **Admin** | Full access to all folders (Engineering, Finance, HR, Legal) |
| **Editor** | Access to Engineering, Finance, and HR folders |
| **Viewer** | Read-only access to Engineering folder only |

> ⚠️ Access control is enforced **server-side via IAM policies** — frontend restrictions alone are not relied upon.

---

## 📁 Features

- 📤 Upload files securely to S3
- 📂 View files based on assigned role
- 🔗 Download files via pre-signed URLs (time-limited)
- 🚫 Role-restricted folder access (server-side enforcement)
- 🔑 Authentication via AWS Cognito
- ☁️ Fully cloud-native deployment on Elastic Beanstalk

---

## 🚀 Deployment

This project is deployed using **AWS Elastic Beanstalk**.

### Prerequisites

- AWS CLI configured (`aws configure`)
- EB CLI installed (`pip install awsebcli`)
- Python 3.x and pip

### Steps

```bash
# Clone the repository
git clone https://github.com/<your-username>/cloud-secure-file-vault.git
cd cloud-secure-file-vault

# Install dependencies
pip install -r requirements.txt

# Initialise Elastic Beanstalk
eb init

# Create the environment
eb create secure-vault-env

# Deploy
eb deploy
```

---

## 🔑 Environment Variables

Set the following environment variables in your **AWS Elastic Beanstalk** console under *Configuration → Software → Environment Properties*:

| Variable | Description |
|---|---|
| `CLIENT_ID` | AWS Cognito App Client ID |
| `CLIENT_SECRET` | AWS Cognito App Client Secret |
| `USER_POOL_ID` | AWS Cognito User Pool ID |

> 🔒 Never commit these values to version control.

---

## 📌 Key Learnings

- Implemented secure user authentication using **AWS Cognito** with secret hash support
- Enforced **RBAC at the IAM level** — bypassing the frontend is not possible
- Managed secrets securely using **environment variables** (no credentials in code)
- Debugged real-world AWS deployment issues on **Elastic Beanstalk**
- Designed and deployed a **production-like cloud security architecture**

---

## 👨‍💻 Author

**Baibhav Chowdhury**  
MSc Cyber Security

---


