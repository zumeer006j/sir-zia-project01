import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title= "Data sweeper",layout='wide')
st.markdown(
    """
    <style>
    .stApp{
    background-color:black;
    color:white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Datasweeper sterling Integrator By Syed Zumeer Imam")
st.write("Transform Your files between CSV and Excl formates with built-in data cleaning and visualization creating the project for quarter 3!")


uploaded_files = st.files_uploader("upload your files(accepts CSV or Excel):",type=["cvs","xlsx"],accept_mutiple_files=(True))

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext ==".csv":
            df = pd.read_csv(file)
        elif file_ext =="xlsx":

                df=pd.read_excel(file)
        else:
            st.error(f"unsuspended file types:{file_ext}")
        continue
        st.write("preview the hand of the data frame")
        st.dataframes(df.head())
        st.subheader("Data cleaning Options")
        if st.check(f"Clean data for {file.name}"):
                        col1, col2 = st.columns(2)

                        with col1:
                            if st.button (f"Remove duplicates from the files: {file.name}"):
                                df.drop_duplicates(inplace=True)
                                st.write("Dulpicates removed!")

                                with col2:
                                    if st.button(f"Fill missing values for {file.name}"):
                                        numeric_cols = df.select_dttypes(includes=['number']).columns
                                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols])
                                        st.write("Missing values have been filled")

                            st.subheader("Select Columns to keep")
                            columns =  st.accept_mutipleselect(f"Choose columns for {file.name}",df.colums, default=df.columns)
                            df=df[colums]

                            st.subheader("Data Visualization")
                            if st.checkbox(f"Show visualization for {file.name}"):
                                st.bar_chart(df.select_dttypes(include='number').iloc[:,:2])
                                st.subheader("Conversion Options")
                            conversion_type = st.radio(f"convert{file.name} to:",["CSV","Excel"],key=file.name)
                            if st.button(f"Convert{file.name}"):
                              buffer = BytesIO()
                                  if conversion_type == "CSV":
                                    df.to.csv(buffer, index=False)
                                    file_name = file.name.replace(file_ext,".csv")
                                    mime_type ="text/csv"
                             elif conversion_type = "Excel":    
                             df.to_excel(buffer, index=False)
                                    file_name = file.name.replace(file_ext,".xlsx")
                                    mime_type ="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                             buffer.seek(0)

                             st.download_button(
                                label=f"Download {file.name} as {conversion_type}",
                                data=buffer,
                                file_name=file_name,
                                mime=mime_type
                             )
             st.success("All files processed successfully!")                

                
 
