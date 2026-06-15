
import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Finance Tracker")

st.title("💰 Smart Finance Tracker")

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    st.success("✅ Supabase Connected Successfully!")

except Exception as e:
    st.error(f"Connection Failed: {e}")
