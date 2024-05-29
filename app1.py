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
    st.dataframe(data)

 
    selected_index = st.selectbox('Select a row index to see details', data.index)
    if selected_index is not None:
        # Get the details of the selected row
        selected_row = data.iloc[selected_index]
        st.write('## Additional Details')

        data = {
    "ID": [1, 2, 3],
    "Names": [["Alice", "Bob"], ["Charlie", "David"], ["Eve", "Frank"]]
      }

# Configure the list column
    list_column_config = st.column_config.ListColumn(
        label="Names",
        help="List of names associated with each ID"
     )

# Display the dataframe with the configured list column
    st.dataframe(data, column_config={"Names": list_column_config})  
 
       
         

if __name__=='__main__':
        main()