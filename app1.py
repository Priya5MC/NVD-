import streamlit as st
import pandas as pd

def main():
    st.title('Field Value Details')

    # Sample data
    data = {
        'Name': ['John', 'Jane', 'Alice'],
        'Age': [30, 25, 35],
        'Occupation': ['Engineer', 'Designer', 'Doctor']
    }

    df = pd.DataFrame(data)

    st.write('## Data Table')
    st.dataframe(df)

    # Create a selectbox to choose a name
    selected_name = st.selectbox('Select a Name to see details', df['Name'])

    if selected_name:
        # Get the details of the selected name
        selected_row = df[df['Name'] == selected_name].iloc[0]
        st.write('## Additional Details')
        st.write(f'**Name:** {selected_row["Name"]}')
        st.write(f'**Age:** {selected_row["Age"]}')
        st.write(f'**Occupation:** {selected_row["Occupation"]}')

if __name__ == '__main__':
    main()
