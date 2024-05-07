import streamlit as st
import sweetviz as sv
import pandas as pd
from tempfile import NamedTemporaryFile

def main():
    st.title('Auto EDA with Sweetviz')
    st.subheader('Upload a dataset and get a comprehensive EDA report instantly.')

    # File uploader allows user to add their own dataset
    uploaded_file = st.file_uploader("Choose a file (CSV format)", type=['csv'])

    if uploaded_file is not None:
        # Check if the uploaded file is valid
        try:
            # Using a context manager to read the file
            with NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_file.getvalue())
                df = pd.read_csv(tmp.name)

            # Display the dataset
            st.write("Data Sample:")
            st.write(df.head())

            # Generate the EDA report
            if st.button('Generate Sweetviz Report'):
                # Sweetviz analysis
                report = sv.analyze(df)
                report_html = report.show_html()
                st.markdown('Your Sweetviz report is ready!', unsafe_allow_html=True)
                st.components.v1.html(report_html, height=600, scrolling=True)

        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
