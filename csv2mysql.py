import pandas as pd
from sqlalchemy import create_engine

#lee el achivo CSV
column_names = ['person','year', 'company']

df = pd.read_csv('C:\laragon\www\django\scripts\json2mysql\json2mysql.csv', header = None, names = column_names)
print(df)

#df = pd.read_csv('C:\laragon\www\django\scripts\json2mysql\json2mysql.csv', header = 0)
#print(df)


engine = create_engine('mysql://root:p4r4guaY@localhost/json2mysql')
with engine.connect() as conn, conn.begin():
    df.to_sql('csv', conn, if_exist='append', index=False)
