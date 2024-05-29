


import numpy as np
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def read_first_5_records(input_file):
    data = pd.read_csv(input_file)
    
    first_5_records = data.head(5)
    return first_5_records


def main():
    st.title('NVD')
    html_tmp = """
    <div style='background-color:red;'>
    <h2 style='color:white;text-align:center;'>CVE LIST</h2>
    </div>
    """
    data = pd.read_csv('NVD.csv')
    st.markdown(html_tmp, unsafe_allow_html=True)
    st.write("First five rows")
    st.dataframe(data.head(5))

if __name__ == '__main__':
    main()