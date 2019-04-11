# …or push an existing repository from the command line
# git remote add origin https://github.com/nvetrov/MSSQL.git
# git push -u origin master
import pyodbc
server = 'tcp:prs043'
database = 'OST'
username = 'OSTUser'
password = 'OSTUser'

connection = pyodbc.connect('driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor()
# cursor.execute("select TOP 10 * FROM [OST].[dbo].[Scenter]")
# row = cursor.fetchone()
# if row:
#     print(row)

# while True:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row.LM_CODE, row.CAPTION)
# Rayon = 1 Это переменная ОТДЕЛ
cursor.execute('''
SELECT TOP (1000) [BAR_CODE]
      ,[LM_CODE]
      ,[CAPTION]
      ,[FACING]
      ,[PRICE]
      ,[STATUS]
      ,[IF_MAIN_BC]
      ,[VPN]
      ,[Rayon]
      ,[val]
      ,[Weight]
      ,[Length]
      ,[Width]
      ,[Height]
      ,[VAT]
      ,[Origin_Country]
      ,[Otdel]
      ,[supplier]
      ,[Top]
FROM [OST].[dbo].[Scenter]
where Otdel = ? 
''', Rayon)
for row in cursor:
    print(row.LM_CODE, row.CAPTION, row.Top)

# cursor.execute("select TOP 1 * FROM [OST].[dbo].[Scenter]")

# for c in cursor:
#     print(int(c.BAR_CODE), int(c.LM_CODE), c.CAPTION, c.Otdel, c.Top)
cursor.close()
connection.close()



