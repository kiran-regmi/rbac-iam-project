import pandas as pd
import json
from itertools import combinations

# Load data
users_df = pd.read_csv("data/users.csv")
roles_df = pd.read_csv("data/roles.csv")
toxic_data = json.load(open("data/toxic_combinations.json"))

# Build entitlement mapping
role_map = roles_df.set_index("Role")["Entitlements"].str.split(";").to_dict()

# Load toxic combinations
toxic_pairs = [set(pair) for pair in toxic_data["toxic_pairs"]]

# Audit function
def audit_users():
    audit_results = []

    for _, user in users_df.iterrows():
        user_id = user["UserID"]
        username = user["Username"]
        role = user["Role"]
        entitlements = set(role_map.get(role, []))

        # Check for toxic combinations
        toxic_found = []
        for pair in toxic_pairs:
            if pair.issubset(entitlements):
                toxic_found.append(tuple(pair))

        # Mark excessive access (arbitrary threshold = 3+ entitlements)
        excessive = len(entitlements) >= 3

        audit_results.append({
            "UserID": user_id,
            "Username": username,
            "Role": role,
            "Entitlements": ", ".join(entitlements),
            "Toxic_Combinations": "; ".join([" + ".join(pair) for pair in toxic_found]),
            "Excessive_Access": excessive
        })

    return pd.DataFrame(audit_results)

# Run audit and export to CSV
if __name__ == "__main__":
    audit_df = audit_users()
    audit_df.to_csv("data/access_audit_report.csv", index=False)
    print("✅ Audit complete. Output saved to 'access_audit_report.csv'.")
