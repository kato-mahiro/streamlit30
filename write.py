import streamlit as st
import pandas as pd

st.header('st.write')

st.write(1234)

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write(df)


