import streamlit as st
import pandas as pd

st.title("📊 CSV Data Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Preview of Data")
    st.dataframe(df)

    st.subheader("🧮 Basic Info")
    st.write("Shape of data:", df.shape)
    st.write("Columns:", list(df.columns))

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    st.subheader("📈 Plot a Column")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Choose a numeric column to plot:", numeric_cols)
        st.line_chart(df[selected_col])
    else:
        st.warning("No numeric columns found to plot.")

    numeric_col = st.selectbox("Choose a column for custom stats", numeric_cols)
    if numeric_col:
        st.write("Mean:", df[numeric_col].mean())
        st.write("Median:", df[numeric_col].median())
        st.write("Mode:", df[numeric_col].mode()[0])
        st.write("Standard Deviation:", df[numeric_col].std())


    st.subheader("🔎 Filter Data")
    column_to_filter = st.selectbox("Select a column to filter by:", df.columns)

    if df[column_to_filter].dtype == 'object':
        unique_vals = df[column_to_filter].unique().tolist()
        selected_val = st.selectbox("Select a value:", unique_vals)
        filtered_df = df[df[column_to_filter] == selected_val]
        st.dataframe(filtered_df)
    else:
        st.info("Filtering works best with text/categorical columns.")
