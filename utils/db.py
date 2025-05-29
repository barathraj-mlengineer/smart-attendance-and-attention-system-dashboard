import pandas as pd
from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:root@localhost/smart_classroom"
engine = create_engine(DB_URL)

def get_attendance_data():
    query = "SELECT name, timestamp FROM attendance"
    return pd.read_sql(query, engine)

def get_attention_data():
    query = "SELECT name, timestamp, attentive FROM attention"
    return pd.read_sql(query, engine)
