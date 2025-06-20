# 🔐 RBAC + ABAC Access Control
**In this project,** we will:
* Manages User Identites
* Defines Roles and Entitlements
* Enforces Access Policies (RBAC/ABAC)
* Detects Privilege Escalation
* Logs Access Events

**🛡️ Skills Demonstrated**
* Identity & Access Management (IAM)
* Python scripting for policy enforcement
* Entitlement auditing & toxic pair detection
* Streamlit dashboard creation
* Access review simulation

## 📌 Project Features
- ✅ Role-Based & Attribute-Based Access Control (RBAC + ABAC)
- 🧩 Role-to-Entitlement Mapping
- 🚩 Toxic Combination Detection (Segregation of Duties)
- ⚠️ Excessive Privilege Audit
- 📊 Streamlit Dashboard for real-time simulation & visibility 

## 🧱 Tech Stack:
* Python & Pandas
* YAML or JSON for policies
* Streamlit (Dashborad)
* SQLite or CSV (user directory)

## ✅ Phase 1: Setup & Identity Directory  

### 🔹 Step 1: Project Folder Structure
![Screen Shot 2025-06-16 at 6 14 28 PM](https://github.com/user-attachments/assets/551bab56-4d71-486f-9767-64e6ada15bad)

- data/ -> User, Role, and Policy daga files
- scripts/ -> Python access logic & auditing tools
- dashboard/ -> Streamlit IAM vishual dashboard
- images/ -> dashboard screenshots (optional)

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

[View Script](https://github.com/kiran-regmi/rbac-iam-project/blob/main/access_checker.py)

![Screen Shot 2025-06-16 at 2 31 31 PM](https://github.com/user-attachments/assets/9f6d6737-fd11-4b30-b305-068c0b5aba9a)

### ✅ Sample Output:

![Screen Shot 2025-06-16 at 2 37 08 PM](https://github.com/user-attachments/assets/a1090e43-6a2c-41ba-b4aa-b2dea0b81ae7)

### 📌 Optional Enhancements
* Log every request and result to a CSV **(access_logs.csv)**
* Accept input via command-line or dashboard

## 🚀 Phase 3 Preview: Privilege Audit & Toxic Combinations
In the next phase, we will:
* Build a script to **identify users with high-risk combinations**
* Flag users with **excessive or unusual access**
* Create a compliance-ready **access audit report**
* Detects **toxic combinations** (eg. Create_Users + Modify_Access)

### 🔹 Step 1: Define Toxic Combinations (optional file or inline)
       - path: data/toxic_combinations.json
![Screen Shot 2025-06-16 at 5 44 39 PM](https://github.com/user-attachments/assets/9efb2bbf-0667-4aa7-8a20-89691799ca06)

**// these are examples of Segregation of Duties (SoD) violations.**

### 🔹 Step 2: Create the Script
       - path: scripts/privilege_audit.py
[View Script](https://github.com/kiran-regmi/rbac-iam-project/blob/main/privilege_audit.py)

### 📄 Audit Output (CSV)
![Screen Shot 2025-06-16 at 5 30 04 PM](https://github.com/user-attachments/assets/fe920abd-3940-4a63-a7f2-c8597b9056c7)

## ✅ Phase 4 - IAM Dashboard
* ✅ User Entitlements
* 🚩 Toxic Combinations
* ⚠️ Excessive Privilege Flags
* 🔍 Live Access Request Tester
        - path: dashboard/app.py

[View Script](https://github.com/kiran-regmi/rbac-iam-project/blob/main/app.py)

## ▶️ How to Run the Dashboard
From the terminal:
![Screen Shot 2025-06-16 at 6 10 53 PM](https://github.com/user-attachments/assets/b35808e8-4d12-46ba-a561-2660fbfeacff)




       
       

  
  



