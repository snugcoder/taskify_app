import requests
import pymysql
import pandas as pd
import sqlalchemy as db

response = requests.get("https://jsonplaceholder.typicode.com/todos")
jsonData = response.json()


df = pd.DataFrame()




'''
db_data = pd.DataFrame.from_dict(jsonData)

engine = db.create_engine('sqlite://todo.db')
db_data.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
    print(pd.DataFrame(query_result))
    '''