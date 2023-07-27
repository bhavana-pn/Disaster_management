import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv ('forestfire21.csv')   
df = pd.DataFrame(data)


# Connect to SQL Server
conn = pyodbc.connect( 'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=forestfire;'
    'UID=root;'
    'PWD=My@220402;'
    'charset=utf8mb4;')

cursor = conn.cursor()


# Create Table
cursor.execute('''
		CREATE TABLE forestinfo01 (
			temp  float,
			RH float,
			wind float,
            rain float,
            area float
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO forestinfo01 (temp, RH, wind,rain,area)
                VALUES (?,?,?,?,?)
                ''',
                row.temp, 
                row.RH,
                row.wind,
                row.rain,
                row.area
                )
conn.commit()