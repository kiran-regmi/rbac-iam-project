# 🔐 RBAC “Identity & Access Management - Access Control""
**In this project,** we will:
* Manages User Identites
* Defines Roles and Entitlements
* Enforces Access Policies (RBAC/ABAC)
* Detects Privilege Escalation
* Logs Access Events

## 🧱 Tech Stack:
* Python & Pandas
* YAML or JSON for policies
* Streamlit (Dashborad)
* SQLite or CSV (user directory)

## ✅ Phase 1: Setup & Identity Directory  
### 🔹 Step 1: Project Structure
![Screen Shot 2025-06-16 at 12 28 38 PM](https://github.com/user-attachments/assets/35544925-d786-4eb3-9741-2a13fac55164)

### 🔹 Step 2: Identity Directory (users.csv)
      - Path: data/users.csv

![Screen Shot 2025-06-16 at 1 42 59 PM](https://github.com/user-attachments/assets/5260a6ba-b8fd-4a78-bbc8-d409b3928762)


### 🔹 Step 3: Role-to-Entitlement Mapping (roles.csv)
       - Path: data/roles.csv
![Screen Shot 2025-06-16 at 1 36 22 PM](https://github.com/user-attachments/assets/0f7aafd5-1797-44be-8e2f-2fbe4e15eefa)

### 🔹 Step 4: Access Policy Definitions (policies.json)
      - Path: data/policies.json
      
![Screen Shot 2025-06-16 at 1 50 36 PM](https://github.com/user-attachments/assets/5212d1fd-222f-4ff6-9d91-f381d8d30d32)

## ✅ Phase 2: Access Control Logic
### 🎯 Goal:
In this phase, we will:
* Load user and role data
* Maps users -> roles -> entitlements
* Evaluates requests using policy rules
* Returs Allow or Deny

### 🔹 Step 1: Create the Script
      - Path: scripts/access_checker.py

View Script(
      
  



