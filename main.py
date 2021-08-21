import streamlit as st
import pandas as pd
import numpy as np
import base64
from gsheetsdb import connect

# Create a connection object.
con = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = con.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
upd_test = run_query(f'UPDATE {sheet_url} 
SET Quantity = 0.90
WHERE Code = 0295;')

# Print results.
for row in rows:
    cols = st.columns(6)
    cols[0].write(f"{row.Code}")
    cols[1].write(f"{row.Description}")
    cols[2].write(f"{row.Unit}")
    cols[3].write(f"{row.Quantity}")
    cols[4].write(f"{row.Rate}")
    cols[5].write(f"{row.Amount}")
