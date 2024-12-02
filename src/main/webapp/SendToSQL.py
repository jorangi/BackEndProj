from sqlalchemy import create_engine
import pymysql
import pandas as pd

def make_tbl(df, id, pw, port, db, dbname, exists='replace'):
    db_conn_path = 'mysql+pymysql://{}}:{}@localhost:{}/{}'.format(id, pw, port, db)
    db_conn = create_engine(db_conn_path)
    conn = db_conn.connect()
    pd.DataFrame(df).to_sql(dbname, con=db_conn, if_exists=exists)

def update_tbl(poster, trailer, id):
    db_conn = pymysql.connect(host='localhost', user='root', password='12345678', db='BPDB', charset='utf8')
    cursor = db_conn.cursor()
    
    sql = "update movieTbl set poster = %s, trailer = %s where id = %s"
    cursor.execute(sql, (poster, trailer, id))
    
    db_conn.commit()
    db_conn.close()