from curses.ascii import TAB
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine, Table
from dotenv import load_dotenv
import os
load_dotenv()
MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

fakeDataset = pd.DataFrame({'colors' : ['blue', 'purple', 'pink']})
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
engine = create_engine(connection_string)
TABLENAME = MYSQL_USER + 'Tablehw'
fakeDataset.to_sql(TABLENAME, con=engine)
