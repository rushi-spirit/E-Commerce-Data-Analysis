import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.set_page_config(page_title="E-commerce Sales Dashboard", layout="wide")

st.title("E-commerce Sales Data Analysis Dashboard")
st.write("Analyze sales trends, revenue, and customer behavior from your dataset.")

# Upload CSV file
###uploaded_file = st.file_uploader("📂 Upload your E-commerce Sales Data (CSV)", type=["csv"])
uploaded_file = 'EDA_Report.csv'


if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")
    
    # Ensure correct data types
   
   
    

category_selection = st.sidebar.multiselect("Select Category", df['title'].unique())
platform_selection = st.sidebar.multiselect("Select Platform", df['platform'].unique())
gender_selection = st.sidebar.radio("Select Gender", df['maincateg'].dropna().unique(), index=0)


    # Sidebar Filters
    # Category Filter
if 'Category' in df.columns:
    if st.sidebar.button("Filter by Category"):
        category_selection = True

# Platform Filter
if 'Platform' in df.columns:
    if st.sidebar.button("Filter by Platform"):
        apply_platform = True

# Gender Filter
if 'Gender' in df.columns:
    if st.sidebar.button("Filter by Gender"):
        apply_gender = True

# Submit button to apply all selected filters
if st.sidebar.button("Submit"):
    filtered_df = df.copy()  # Start with the original dataframe

    # Apply filters only if the respective button was clicked
    if category_selection:
        filtered_df = filtered_df[filtered_df['title'].isin(category_selection)]
    
    if platform_selection:
        filtered_df = filtered_df[filtered_df['platform'].isin(platform_selection)]
    
    if gender_selection:
        filtered_df = filtered_df[filtered_df['maincateg'] == gender_selection]

    # Show the final filtered dataset
    st.write("**Filtered Data:**")
    st.write(filtered_df)

    st.write(f"**Total Count Of Filtered Data:{len(filtered_df)}**")

    if not filtered_df.empty:
        st.write("**Bar Chart: Product Counts by Category**")

        # Count occurrences of each selected product title
        product_counts = filtered_df['title'].value_counts()

        # Plot bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(product_counts.index, product_counts.values, color='purple')
        plt.title("Product Counts by Category")
        plt.xlabel("Product Title")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Display in Streamlit
        st.pyplot(plt)

    else:
        st.write("No data available for the selected filters.")
