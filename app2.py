import streamlit as st
import pandas as pd

# Sample DataFrame
df = pd.read_csv('NVD.csv')

# Function to display the home page
def show_home():
    st.title("Home Page")
    st.write("Click the button to view the selected columns.")

    if st.button("Show Data"):
        st.session_state.page = "output"

# Function to display the output page
def show_output(selected_columns):
    st.title("Output Page")
    
    if not selected_columns:
        st.write("No columns selected.")
    else:
        st.write("First 5 rows of the selected columns of the DataFrame:")
        st.dataframe(df[selected_columns].head())

    if st.button("Show More Details"):
        st.session_state.page = "output2"
    if st.button("Back"):
        st.session_state.page = "home"

# Function to display the second output page with more details
def show_output2(selected_columns):
    st.title("Output Page 2")
    
    if not selected_columns:
        st.write("No columns selected.")
    else:
         
        st.write(cve/descriptions/0/value' ,'cve/metrics/cvssMetricV2/0/cvssData/vectorString,	
        'cve/metrics/cvssMetricV2/0/cvssData/accessVector',	
        'cve/metrics/cvssMetricV2/0/cvssData/accessComplexity',	
        'cve/metrics/cvssMetricV2/0/cvssData/authentication',	
        'cve/metrics/cvssMetricV2/0/cvssData/confidentialityImpact',	
        'cve/metrics/cvssMetricV2/0/cvssData/integrityImpact',	
        'cve/metrics/cvssMetricV2/0/cvssData/availabilityImpact',	
        'cve/metrics/cvssMetricV2/0/cvssData/baseScore',	
        'cve/metrics/cvssMetricV2/0/baseSeverity',	
        'cve/metrics/cvssMetricV2/0/exploitabilityScore',	
        'cve/metrics/cvssMetricV2/0/impactScore',
        'cve/configurations/0/nodes/0/cpeMatch/0/vulnerable',	
        'cve/configurations/0/nodes/0/cpeMatch/0/criteria',	
        'cve/configurations/0/nodes/0/cpeMatch/0/matchCriteriaId',
        'cve/configurations/0/nodes/0/cpeMatch/1/vulnerable',	
        'cve/configurations/0/nodes/0/cpeMatch/1/criteria',	
        'cve/configurations/0/nodes/0/cpeMatch/1/matchCriteriaId',
        'cve/configurations/0/nodes/0/cpeMatch/2/vulnerable',	
        'cve/configurations/0/nodes/0/cpeMatch/2/criteria',	
        'cve/configurations/0/nodes/0/cpeMatch/2/matchCriteriaId')

                 
    if st.button("Back"):
        st.session_state.page = "output"

# Main function to control the navigation
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_columns" not in st.session_state:
        st.session_state.selected_columns = df.columns.tolist()

    with st.sidebar:
        st.header("Column Selection")
        selected_columns = st.multiselect("Select columns to display", options=df.columns.tolist(), default=st.session_state.selected_columns)
        st.session_state.selected_columns = selected_columns

    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "output":
        show_output(selected_columns)
    elif st.session_state.page == "output2":
        show_output2(selected_columns)

if __name__ == "__main__":
    main()
