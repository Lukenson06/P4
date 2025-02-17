import streamlit as st
import pandas as pd
import plotly.express as px


# Header
st.header("Car Sales Dashboard")
st.write("This project is a simple web application dashboard, It's dedicated to helping  find and purchase car.")

df = pd.read_csv('vehicles_us.csv', sep=',')
print(df.head())

#fill the missing values base on grouping, specific columns and calculate median for model_year, median for odemeter and cylinders
df['model_year'] = df.groupby('model')['model_year'].transform('median')
df['odometer'] = df.groupby('model')['odometer'].transform('median')
df['cylinders'] = df.groupby('model')['cylinders'].transform('median')

# since we have missing values on odometer we can replace the missing values with 0 because we no need to drop the rows.
df['odometer'] = df['odometer'].fillna(0)

# convert the year and odonometer to int
df['model_year'] = df['model_year'].astype(int)
df['odometer'] = df['odometer'].astype(int)


#Correct the date_posted to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'])


# Plotly Histogram
hist_fig = px.histogram(df, x='condition', title='Distribution of Car Condition')
st.plotly_chart(hist_fig)
st.write("This fig show vehicle's car condition distribution, About 24.7k vehicles are in excelent condition")


fig = px.histogram(df, x='odometer', title='Odometer Reading Distribution')
st.plotly_chart(fig)
st.write("This fig show vehicle's ondometer distribution. About 4000 vehicles have ondometer reading 120k miles.")

# Plotly Scatter Plot

scatter_fig = px.scatter(df, x='price', y='model_year', color='condition', title='Price vs Model Year')
st.plotly_chart(scatter_fig)
st.write("This fig show vehicle's condition, its price and model year")


fig = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Vehicle Condition')
st.plotly_chart(fig)
st.write("This fig show vehicle's condition, its mileage, and its price. Its normal to assume that vehicles with 0 miles should cost more than the others, but from the plot we see that vehicle have odometer 105252 mile and cost $375K")


# Checkbox to filter data
if st.checkbox('Show only cars newer than 2018'):
    filtered_df = df[df['model_year'] > 2018]
else:
    filtered_df = df

# Display filtered scatter plot
scatter_fig_filtered = px.scatter(filtered_df, x='price', y='model_year', color='condition', title='Filtered Price vs Model Year')
st.plotly_chart(scatter_fig_filtered)
st.write("The scatter plot below visualizes vehicle models based on selected characteristics, with color coding indicating different condition.")
