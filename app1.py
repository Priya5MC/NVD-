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
    
  
# Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

# Navigation function
    def navigate_to(page):
        st.session_state.page = page

# Main Page content
    def main_page():
        st.title("Main Page")
    
    # Example data
    data = {
        "Item 1": "Detail of Item 1",
        "Item 2": "Detail of Item 2",
        "Item 3": "Detail of Item 3",
    }
    
    # Display clickable items
    for item, detail in data.items():
        if st.button(item):
            st.session_state.selected_item = item
            st.session_state.detail = detail
            navigate_to('detail')
            st.experimental_rerun()

# Detail Page content
def detail_page():
    st.title("Detail Page")
    
    # Display details
    st.write(f"Details of {st.session_state.selected_item}:")
    st.write(st.session_state.detail)
    
    # Button to go back to the main page
    if st.button("Go Back"):
        navigate_to('main')
        st.experimental_rerun()

# Page routing
    if st.session_state.page == 'main':
        main_page()
    elif st.session_state.page == 'detail':
        detail_page()


if __name__=='__main__':
        main()