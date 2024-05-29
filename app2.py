import streamlit as st
import pandas as pd

# Sample DataFrame
data =  pd.read_csv('NVD.csv')

df = pd.DataFrame(data)

# Function to display the home page
def show_home():
    st.title("Home Page")
    st.write("Click the button to view the first 5 rows and columns.")

    if st.button("Show Data"):
        st.session_state.page = "output"

# Function to display the output page
def show_output():
    st.title("Output Page")
    
    st.write("First 5 rows and first 5 columns of the DataFrame:")
    st.dataframe(df.iloc[:5, :5])

    if st.button("Back"):
        st.session_state.page = "home"
    

# Main function to control the navigation
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "output":
        show_output()

if __name__ == "__main__":
    main()
