import pyodbc
server = 'tcp:prs043'
database = 'OST'
username = 'sa'
password = 'russi@'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()
cursor.execute("select TOP 10 * FROM [OST].[dbo].[Scenter]")
for c in cursor:
    print(int(c.BAR_CODE), int(c.LM_CODE),c.CAPTION,c.Otdel,c.Top)

cursor.close()
connection.close()


