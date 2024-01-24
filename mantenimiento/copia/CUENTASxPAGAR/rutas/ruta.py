
from conf.conexion import conexion
from fastapi import FastAPI, Response, APIRouter
from pydantic import BaseModel
from starlette.status import HTTP_400_BAD_REQUEST

class retornar(BaseModel):
    menu: str 

user= APIRouter()

@user.get('/')
def root():
    return {"casa": "casa"}

@user.get('/api/conectarse/<user><pasw>', response_model=retornar )
def prueba(user: str, pasw:str ):
    conectar = conexion.cursor()
    resultado = conectar.execute ("select * from SCHEMA_cuentasXpagar.Usuario where Nombres ='"+user +"'and Password ='" + pasw + "';")
    respuesta = resultado.fetchone()
    retorna = []
    if respuesta is not None :
        j = {}
        contenido = conexion.cursor()
        contenido = conexion.execute("select * from SCHEMA_cuentasXpagar.Menus where SCHEMA_cuentasXpagar.Menus.[id.Roles]='"+str(respuesta[5])+"';")
        receptorDato = contenido.fetchall()
        print(receptorDato)
        menu =""
        menu += "<ul>"
        for t in receptorDato:
            menu +=  "<li><a href=\""+t[2] +"\" target=\"myFrame\">"+t[1]+"</a></li>"
            print(t[2])
        menu+="<li><a href=\"/Salir\">Salir</a></li>"    
        menu+= "</ul>"
        j["menu"] = menu
        return j
    else:
        
        return Response(status_code= HTTP_400_BAD_REQUEST)
  
        
 
    
