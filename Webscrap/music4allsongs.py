import pandas as pd
import sqlite3
Movies = pd.read_excel('Webscrap.xlsx', sheet_name='MovieLists', header=0)
#print(MovieLists)
print("Excel read completed")
db_conn = sqlite3.connect("music4all.db")
c = db_conn.cursor()
Movies.to_sql('Music4all',db_conn, if_exists='append', index=False)
print("SQLite Insert completed")
db_conn.close()