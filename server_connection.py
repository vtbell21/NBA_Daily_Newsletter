import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-ADUDDFK\SQLEXPRESS10;'
    'DATABASE=NBA_Emails;'
    'Trusted_Connection=yes;'
)

cursor = cnxn.cursor()
cursor.execute('SELECT email_address FROM emails')
all_emails = cursor.fetchall()
for row in all_emails:
    print(row)

cursor.close()
cnxn.close()
