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
    
  

# Sample data
    data = {
        "ID": [1, 2, 3],
        "Name": ["Alice", "Bob", "Charlie"]
    }
    df = pd.DataFrame(data)

# Display the dataframe
    st.write("Click on a row to navigate to the details page:")

# Use st.dataframe or st.table to display the table
    st.table(df)

# JavaScript to capture row click and navigate to a new page with the ID as a query parameter
    st.markdown("""
        <script>
        const table = window.parent.document.querySelector('table');
        table.addEventListener('click', (event) => {
            const cell = event.target;
            const row = cell.parentElement;
            const id = row.children[0].innerText;
            window.location.href = `?page=details&id=${id}`;
        });
        </script>
    """, unsafe_allow_html=True)


if __name__=='__main__':
        main()