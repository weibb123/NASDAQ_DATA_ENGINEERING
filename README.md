# NASDAQ_DATA_ENGINEERING
ETL pipeline on one year of NASDAQ stock data with SNOWFLAKE
FREE trial of Snowflake account.

Procedures to follow
1. create python virtual environment
2. 

```python
pip install streamlit pandas plotly snowflake-connector-python yfinance
```

3. Create Snowflake free trial and free credits
    1. Upload CSV to Snowflake, and populate tables with columns
    2. create database, schema, tables
    3. Install extension to snowflake in VSCODE
4. Utlized Streamlit connect to snowflake with snowflake credentials and load the data for fancy charts.
5. Deployed to Streamlit Community Cloud and share the app for free

## Extract data from yahoofinance
The script to extract data -> dataframe -> csv is in **stock.ipynb**


## Upload data to SnowFlake
![image](https://github.com/user-attachments/assets/5a3847e8-b7aa-4d16-971a-a64dd695eba2)
![image](https://github.com/user-attachments/assets/33f7040d-01dd-4f17-991c-bdbdfae841a5)
![image](https://github.com/user-attachments/assets/e075facc-7644-4f7f-9f6b-1cffb4937134)





You can find this information once you install snowflake in VSCode Extension

![image](https://github.com/user-attachments/assets/bec3e736-a3b6-4552-ad22-a1ca6835a15c)

## Improvements
Use Apache Airflow to build a airflow pipeline to automate this data ingestion process.

