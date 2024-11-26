from sqlalchemy import create_engine
import pymysql
import pandas as pd

def make_tbl(df, id, pw, port, db):
    db_conn_path = 'mysql+pymysql://{}:{}@localhost:{}/{}'.format(id, pw, port, db)
    db_conn = create_engine(db_conn_path)
    conn = db_conn.connect()
    
    pd.DataFrame(df).to_sql('testTbl', con=db_conn, if_exists='replace')