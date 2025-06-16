import pandas as pd
import json

# Load data
users_df = pd.read_csv("data/users.csv")
roles_df = pd.read_csv("data/roles.csv")
with open("data/policies.json") as f:
    policies = json.load(f)

# Parse roles into a dictionary
role_map = roles_df.set_index("Role")["Entitlements"].str.split(";").to_dict()

# Build policy rule index
policy_rules = {}
for rule in policies["rules"]:
    policy_rules[rule["entitlement"]] = rule["allowed_departments"]

# Function to check access
def check_access(user_id, entitlement_requested):
    user = users_df[users_df["UserID"] == user_id].iloc[0]
    user_role = user["Role"]
    user_dept = user["Department"]

    entitlements = role_map.get(user_role, [])
    if entitlement_requested not in entitlements:
        return f"? Access Denied: Entitlement '{entitlement_requested}' not in user's role ({user_role})"

    allowed_departments = policy_rules.get(entitlement_requested, [])
    if user_dept not in allowed_departments:
        return f"? Access Denied: Department '{user_dept}' not authorized for '{entitlement_requested}'"

    return f"? Access Granted to '{entitlement_requested}' for user '{user['Username']}'"

# Sample test cases
if __name__ == "__main__":
    print(check_access("U001", "View_HR_Records"))       # Should Deny
    print(check_access("U002", "Create_Users"))               # Should Deny 
    print(check_access("U003", "Modify_Access"))            # Should Allow
    print(check_access("U004", "View_HR_Records"))       # Should Deny
    print(check_access("U005", "View_HR_Records"))       # Should Allow

