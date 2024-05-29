import numpy as np
import pandas as pd
import streamlit as st
 

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

 
    selected_index = st.selectbox('Select a row index to see details', data.index)
    if selected_index is not None:
        # Get the details of the selected row
        selected_row = data.iloc[selected_index]
        st.write('## Additional Details')
    
       
         

if __name__=='__main__':
        main()