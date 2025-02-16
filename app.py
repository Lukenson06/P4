import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\Users\luken\Downloads\vehicles_us.csv")
print(df.head())


# Header
st.header("Car Sales Dashboard")

# Plotly Histogram
hist_fig = px.histogram(df, x='condition', title='Distribution of Car Condition')
st.plotly_chart(hist_fig)

# Plotly Scatter Plot
scatter_fig = px.scatter(df, x='price', y='model_year', color='condition', title='Price vs Model Year')
st.plotly_chart(scatter_fig)

# Checkbox to filter data
if st.checkbox('Show only cars newer than 2018'):
    filtered_df = df[df['model_year'] > 2018]
else:
    filtered_df = df

# Display filtered scatter plot
scatter_fig_filtered = px.scatter(filtered_df, x='price', y='model_year', color='condition', title='Filtered Price vs Model Year')
st.plotly_chart(scatter_fig_filtered)
