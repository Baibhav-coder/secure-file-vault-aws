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

## 🖥️ Demo Screenshots

---

### 🔐 Application UI

#### Login — AWS Cognito Authentication
![Login](screenshots/login.png)
> Secure login powered by AWS Cognito with HMAC-SHA256 secret hash authentication.

#### 👑 Admin Panel — Full Access
![Admin Panel](screenshots/Admin_Panel.png)
> Admin role has unrestricted access to all department folders: Engineering, Finance, HR, and Legal.

#### ✏️ Editor Panel — Partial Access
![Editor Panel](screenshots/Editor_Panel.png)
> Editor role is restricted to Engineering, Finance, and HR folders only.

#### 👁️ Viewer Panel — Read-Only Access
![Viewer Panel](screenshots/Viewer_Panel.png)
> Viewer role has read-only access to the Engineering folder only — enforced server-side via IAM.

---

### 🔑 AWS Cognito — Authentication

#### User Pool
![Cognito User Pool](screenshots/Cognito_UserPool.png)
> AWS Cognito User Pool managing all application users with secure authentication flows.

#### Users in Cognito
![Users in Cognito](screenshots/Users_In_Cognito.png)
> Registered users provisioned in the Cognito User Pool.

#### Groups (Roles) in Cognito
![Groups in Cognito](screenshots/Groups_In_Cognito.png)
> Admin, Editor, and Viewer groups defined in Cognito — mapped to IAM roles for access control.

#### App Client Configuration
![App Client](screenshots/App_Client.png)
> Cognito App Client configured with secret hash to prevent unauthorised API calls.

---

### 🗂️ Amazon S3 — Secure Storage

#### S3 Bucket Structure
![S3 Structure](screenshots/Securevault_S3_Structure.png)
> Department-level folder isolation: Engineering, Finance, HR, and Legal.

#### Encryption at Rest (SSE)
![S3 Encryption](screenshots/S3_Encryption.png)
> Server-side encryption (SSE-S3) enabled — all files encrypted at rest.

#### Versioning Enabled
![S3 Versioning](screenshots/S3_Versioning.png)
> S3 versioning active — full file version history and recovery capability.

#### Lifecycle Policy
![S3 Lifecycle](screenshots/S3_Lifecycle.png)
> Lifecycle rules configured for automated storage management.

#### S3 Buckets (Logs + Project)
![S3 Buckets](screenshots/S3_Bucket_For_logs_EB_and_Mycloudproject.png)
> Separate S3 buckets for application data and Elastic Beanstalk logs.

---

### 🔑 IAM — Authorisation

#### IAM Dashboard
![IAM Dashboard](screenshots/Iam_dashboard.png)
> IAM overview showing roles and policies configured for the project.

#### IAM Roles
![IAM Roles](screenshots/IAM_Roles.png)
> Dedicated IAM roles for Admin, Editor, and Viewer with least-privilege policies.

#### Cloud Admin IAM Role
![IAM Cloud Admin](screenshots/IAM_CLOUDADMIN.png)
> Fine-grained IAM policy for the Admin role — full S3 access across all folders.

#### S3 Admin Role Policy
![S3 Admin Role](screenshots/S3_ADMIN_ROLE.png)
> Admin IAM policy granting full S3 bucket access.

#### S3 Editor Role & Policy
![S3 Editor](screenshots/S3_EDITOR.png)
> Editor IAM role scoped to Engineering, Finance, and HR folders.

![S3 Editor Policy](screenshots/S3_EDITOR_POLICY.png)
> Explicit IAM policy denying Editor access to Legal folder.

#### S3 Viewer Role & Policy
![S3 Viewer Role](screenshots/S3_Viewer_Role.png)
> Viewer IAM role with read-only permissions on Engineering folder only.

![S3 Viewer Policy](screenshots/S3_Viewere_Policy.png)
> Explicit IAM policy enforcing Viewer read-only restrictions.

---

### 📊 Monitoring, Logging & Alerts

#### CloudTrail Dashboard
![CloudTrail](screenshots/Cloudtrail_Dashboards.png)
> AWS CloudTrail logging all API activity — including unauthorised access attempts.

#### CloudWatch Alarms
![CloudWatch Alarms](screenshots/Cloudwatch_Alarms.png)
> CloudWatch alarms configured to trigger on suspicious or denied access events.

#### CloudWatch Logs
![CloudWatch Logs](screenshots/Cloudwatch_Logs.png)
> Real-time log streams capturing all application and infrastructure events.

#### SNS Email Notification
![SNS Notification](screenshots/SNS_Notification_Via_Email.png)
> Live SNS email alert triggered on a security event — demonstrating real-time alerting.

---

### ☁️ Deployment — AWS Elastic Beanstalk

#### Elastic Beanstalk Environment
![Elastic Beanstalk](screenshots/ElasticBeanstalk.png)
> Application deployed and running on AWS Elastic Beanstalk.

![Elastic Beanstalk Health](screenshots/Elastic_BeanStalk.png)
> Environment health status showing successful deployment.

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


