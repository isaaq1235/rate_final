import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache to only run once.
# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})

conn = mysql.connector.connect(host = "localhost", user = 'root',password = 'isaaq2021',database='rate_analysis')

# conn.execute("select * from rate_data;")

cur = conn.cursor()

cur.execute("select * from rate_data")

for i in cur:
    st.write(i)
