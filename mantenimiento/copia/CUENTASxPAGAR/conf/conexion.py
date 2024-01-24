
import pyodbc

server='LAPTOP-P0NLEKGB\SQLEXPRESS'
db = 'CUENTAS_X_PAGAR'
user = 'USR_DUEÑOCRUDD'
password = '12345'


try:
    conexion = pyodbc.connect(
        'DRIVER={ODBC DRIVER 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+password
    )
    print('Conexion Exitosa')
except:
    print('Error')


 
