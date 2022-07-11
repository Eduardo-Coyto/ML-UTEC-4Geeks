import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

database =  os.getenv("DATABASE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv('HOST')
port = os.getenv('PORT')

conn = psycopg2.connect(
                        database= database, 
                        user= user, 
                        password= password,  
                        host= host, 
                        port= port
                        )
conectar = conn.cursor()

name_Table = "publishers"
sqlCreateTable = "create table if not exists "+name_Table+" (publisher_id INT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY(publisher_id));"

conectar.execute(sqlCreateTable)

conn.commit()

sqlGetTableList =   """
                    INSERT INTO publishers (publisher_id, name) values (1,'O Reilly Media');
                    INSERT INTO publishers(publisher_id,name) values (2,'A Book Apart');
                    INSERT INTO publishers(publisher_id,name) values (3,'A K PETERS');
                    INSERT INTO publishers(publisher_id,name) values (4,'Academic Press');
                    INSERT INTO publishers(publisher_id,name) values (5,'Addison Wesley');
                    INSERT INTO publishers(publisher_id,name) values (6,'Albert&Sweigart');
                    INSERT INTO publishers(publisher_id,name) values (7,'Alfred A. Knopf');
                    """

conectar.execute(sqlGetTableList)

conn.commit()
conn.close()
conectar.close()

df= pd.read_sql('SELECT * FROM publishers', conn)
df
conn.close()

df