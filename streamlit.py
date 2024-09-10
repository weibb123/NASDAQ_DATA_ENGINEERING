import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from snowflake.connector import connect
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from NASDAQ_YEAR;")

# Streamlit app
st.title('Snowflake Data Visualization')

# Create a 2x2 grid for charts
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Candlestick chart
with col1:
    st.subheader('Candlestick Chart')
    fig = go.Figure(data=[go.Candlestick(x=df['DATE'],
                    open=df['OPEN'],
                    high=df['HIGH'],
                    low=df['LOW'],
                    close=df['CLOSE'])])
    fig.update_layout(xaxis_rangeslider_visible=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

# Line chart of closing prices
with col2:
    st.subheader('Closing Price Over Time')
    fig = px.line(df, x='DATE', y='CLOSE', title='Closing Price')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Volume bar chart
with col3:
    st.subheader('Trading Volume Over Time')
    fig = px.bar(df, x='DATE', y='VOLUME', title='Trading Volume')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Scatter plot of Open vs Close prices
with col4:
    st.subheader('Open vs Close Price')
    fig = px.scatter(df, x='OPEN', y='CLOSE', title='Open vs Close Price')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Additional analysis or metrics can be added here
st.subheader('Summary Statistics')
col5, col6, col7 = st.columns(3)
col5.metric("Average Closing Price", f"${df['CLOSE'].mean():.2f}")
col6.metric("Highest Price", f"${df['HIGH'].max():.2f}")
col7.metric("Lowest Price", f"${df['LOW'].min():.2f}")