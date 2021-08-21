import streamlit as st
import pandas as pd
import numpy as np
import base64

st.image("trginslogo.png")

st.title("Rate Analysis")

# df = pd.read_excel('Concrete Itms - Foundation, Column, Slab & Beam, Walls Works (1).xls')

# df = df.astype(str)

# st.markdown("""
# <embed src="CivilDAR_2019_Vol_1.pdf" width="400" height="400">
# """, unsafe_allow_html=True)

# pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

with st.expander("Expand Rate Data"):
    st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0"> <iframe src="http://127.0.0.1:8887/output%20(1).html" width="700" height="1000" type="application/pdf"></iframe>', unsafe_allow_html=True)

# displayPDF("http://127.0.0.1:8887/CivilDAR_2019_Vol_1.pdf")

# # df.drop(df.columns[0],axis=1,inplace=True)

# # df = df.iloc[1:]


# # df.columns = [i for i in range(5)]

# # # df.fillna(0)

# # df[2] = df[2].astype(str)

# # df[1] = df[1].fillna('')
# # df[2] = df[2].replace({'nan':''})
# # df[3] = df[3].fillna('')
# # df[4] = df[4].fillna('')
# # df[4] = df[4].replace({'-':''})

# df.columns.values[1:] = [i for i in range(1,13)]

# df[:] = df[:].replace(np.nan,'')

# # df.columns.values[2] = 2
# # df.columns.values[3] = 3
# # df.columns.values[4] = 4

# # df.dropna(inplace = True)

# df = df[60:]

# df = df.replace('nan','')

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))