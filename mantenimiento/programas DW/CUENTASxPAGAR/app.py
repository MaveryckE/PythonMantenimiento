from flask import Flask
from flask import render_template, request, redirect, url_for, session
import requests
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'maverick' 





@app.route('/')
def iniciar():
    return render_template('login.html')

@app.route('/conectarse', methods=["post"])
def prueba():
    extraerUsuario = request.form['usuario']
    extraerClave = request.form['clave']
    
    URL = "http://127.0.0.1:8000/api/conectarse/<user><pasw>"
 
    PARAMS = {'user':extraerUsuario, 'pasw': extraerClave}
    
    r = requests.get(url = URL, params = PARAMS)
    
    if r.status_code == 200:
          data = r.json()
          menu = data["menu"]
          return render_template("inicio.html", men = menu)
    else:
        redirect("/")  
        
@app.route('/adentromenu')
def adentromenu():
   
    return render_template('inicio.html')

@app.route('/tabla')
def vistab():
    
    return render_template('proveedores.html')

@app.route('/proveedores')
def provs():
    url = "http://127.0.0.1:8000/api/verProveedores"
    visualizar = requests.get(url)
    data =""
    if visualizar.status_code ==200:
        data = visualizar.json()
    
    return render_template('proveedores.html', tabla = data)

@app.route("/AgregarProveedor", methods=["POST"])
def AgregarProveedor():
        llega = request.form["llega"]
        dpiproveedor = request.form["dpi"]
        nombreproveedor = request.form["nombres"]
        apellidoproveedor = request.form["apellidos"]
        correoproveedor = request.form["correo"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        id1 = request.form["id1"]
        url = "http://127.0.0.1:8000/api/AgregarProveedor"
        url2 = "http://127.0.0.1:8000/api/ModificarProveedor"
        datos ={
         "codigoproveedor":int(id1),   
        "dpiproveedor":int(dpiproveedor),
        "nombreproveedor":  nombreproveedor,
        "apellidoproveedor":  apellidoproveedor,
        "correoproveedor": correoproveedor,
        "direccion":  direccion,
        "telefono": int(telefono)
        }
        if llega == "aceptar":
            crear = requests.post(url, json.dumps(datos))
            return redirect("/proveedores")
        if llega == "actualizar":
            requests.put(url2, json.dumps(datos))
            return redirect("/proveedores")
    
    
@app.route("/eliminarProv", methods=["POST"])
def eliminarProveedor():
    idproducto = request.form["idproducto"]    
    url = "http://127.0.0.1:8000/api/EliminarProveedor"
    datos ={
         "codigoproveedor":int(idproducto),   
        "dpiproveedor":0,
        "nombreproveedor":  "",
        "apellidoproveedor":  "",
        "correoproveedor":  "",
        "direccion": "",
        "telefono": 0
        }
    crear = requests.delete(url, data = json.dumps(datos))
    return redirect("/proveedores")

#PRODUCTOS MANTENIMIENTO

@app.route('/productos')
def verProductos():
    url = "http://127.0.0.1:8000/api/verProductos"
    visualizar = requests.get(url)
    data =""
    if visualizar.status_code ==200:
        data = visualizar.json()
    
    return render_template('productos.html', tabla = data)


@app.route("/AgregarProductos", methods=["POST"])
def AgregarProductos():
    llega = request.form["llega"]
    codigo_producto= request.form["id1"]
    nombre_producto= request.form["producto"]
    descripcion= request.form["descripcion"] 
    precio= request.form["precio"]
    tipoproducto= request.form["tipoproducto"]
    datos ={
    "codigo_producto":codigo_producto,
    "nombre_producto":nombre_producto,
    "descripcion":descripcion, 
    "precio":precio,
    "tipoproducto":tipoproducto,
    }
    tabla = ""
    
    url = "http://127.0.0.1:8000/api/CreaProducto"
    url2 = "http://127.0.0.1:8000/api/modificarProducto"
    if llega == "aceptar":
        requests.post(url,json.dumps(datos))
        return redirect("/productos")
    if llega == "actualizar":
        requests.put(url2, data = json.dumps(datos))
        return redirect("/productos")
        
@app.route("/eliminarProducto", methods=["POST"])
def Eliminarproductos():
    idproducto = request.form["idproducto"]
    
    url = "http://127.0.0.1:8000/api/EliminarProducto"
    datos ={
         "codigo_producto":int(idproducto),   
        "nombre_producto":"",
        "descripcion":"", 
        "precio":0,
        "tipoproducto":"",
        }
    crear = requests.delete(url, data = json.dumps(datos))
    return redirect("/productos")

# @app.route("/excelpro", methods=["POST"])
# def excelProo():
#     url="http://127.0.0.1:8000/api/excelProveedores"
    
#     crear = requests.get(url)
    
#     return redirect("/proveedores")

        
@app.route('/Salir')
def libros():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
