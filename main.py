import streamlit as st
import numpy as np
import psycopg2

st.title('Rate Analysis')

@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

con = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=60)
def run_query(query):
    with con.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from rate_dat;")

# Print results.
for row in rows:
    st.write(f"{row[0]}")
