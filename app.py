import pandas as pd
import streamlit as st

def combine_sheets(input_file):
    # Load the Excel file
    excel_file = pd.ExcelFile(input_file)

    # Create an empty DataFrame to store the combined data
    combined_df = pd.DataFrame()

    # Iterate through each sheet in the Excel file
    for sheet_name in excel_file.sheet_names:
        # Read the sheet into a DataFrame, ignoring additional header rows
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=0)
        
        # Append the data to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

# Streamlit app
def main():
    st.title("Excel Sheets Combiner")

    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    if uploaded_file is not None:
        combined_df = combine_sheets(uploaded_file)

        st.write("Combined Data")
        st.write(combined_df)

        # Save the combined data to a new Excel file in memory
        output_file = "combined_output.xlsx"
        combined_df.to_excel(output_file, index=False)

        # Create a download button
        with open(output_file, "rb") as f:
            btn = st.download_button(
                label="Download combined Excel file",
                data=f,
                file_name="combined_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()
