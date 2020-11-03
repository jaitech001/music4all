import pandas as pd
import sqlite3
MovieLists = pd.read_excel(
    'C:/Users/sures/Desktop/music4all/Webscrap/Webscrap.xlsx', 
    sheet_name='MovieLists',
    header=0)
#print(MovieLists)
print("Excel read completed")
db_conn = sqlite3.connect("C://sqlite/gui/SQLiteStudio/demodb")
c = db_conn.cursor()
MovieLists.to_sql('Music4all',db_conn, if_exists='append', index=False)
print("SQLite Insert completed")
db_conn.close()