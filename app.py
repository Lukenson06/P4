import streamlit as st
import pandas as pd
import plotly.express as px


# Load the dataset
df = pd.read_csv('vehicles_us.csv')

st.dataframe(df, hide_index=True)


# Add header
st.header("Vehicle Data Dashboard")

# Display data
st.write("This dashboard shows some exploratory data analysis of the vehicles in the dataset.")




# Add histogram
fig_histogram = px.histogram(df, x='price', title= "Vehicle value") 
st.plotly_chart(fig_histogram)

# Add scatter plot
fig_scatter = px.scatter(df, x='odometer', y='price', title='Odometer vs. Vehicle Price')
st.plotly_chart(fig_scatter)

# Add checkbox
show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

if show_expensive_cars:
    filtered_df = df[df['price'] > 20000]
else:
    filtered_df = df

st.write(filtered_df)
