import streamlit as st
import pandas as pd
import json
from scripts.access_checker import check_access
from scripts.privilege_audit import audit_users

# Page setup
st.set_page_config(page_title="IAM Dashboard", layout="wide")
st.title("🔐 IAM Analyst Dashboard")

# --- Load data ---
audit_df = audit_users()
users_df = pd.read_csv("data/users.csv")
roles_df = pd.read_csv("data/roles.csv")

# --- Section 1: Entitlement Overview ---
st.header("📋 User Access Summary")
st.dataframe(audit_df[['UserID', 'Username', 'Role', 'Entitlements', 'Excessive_Access']])

# --- Section 2: Toxic Combination Violations ---
st.header("🚩 Toxic Access Violations")
toxic_violations = audit_df[audit_df['Toxic_Combinations'] != ""]
st.dataframe(toxic_violations[['Username', 'Role', 'Toxic_Combinations']])

# --- Section 3: Role Overview ---
st.header("🧩 Role-to-Entitlement Mapping")
roles_df[['Role', 'Entitlements']] = roles_df[['Role', 'Entitlements']]
st.dataframe(roles_df)

# --- Section 4: Access Request Tester ---
st.header("🔍 Access Request Tester")
user_options = users_df['UserID'].tolist()
entitlements_list = sorted(set(sum([e.split(';') for e in roles_df['Entitlements']], [])))

col1, col2 = st.columns(2)
with col1:
    selected_user = st.selectbox("Select User", user_options)
with col2:
    selected_entitlement = st.selectbox("Select Entitlement", entitlements_list)

if st.button("Test Access"):
    result = check_access(selected_user, selected_entitlement)
    st.success(result) if result.startswith("✅") else st.error(result)

# Footer
st.markdown("---")
st.caption("Simulated IAM Audit Project by Kiran Regmi – Identity & Access Management Portfolio")
