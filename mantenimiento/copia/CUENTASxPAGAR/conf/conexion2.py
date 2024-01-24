import oracledb

try:
    params = oracledb.ConnectParams(host="LAPTOP-P0NLEKGB", port=1521, service_name="XE")
    conn = oracledb.connect(user="USR_PRUEBADMIN", password="UNO123", params=params)

    print("Successfully connected to Oracle Database")
except oracledb.Error as error:
    print("Error en la conexion", error)