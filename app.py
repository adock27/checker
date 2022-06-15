
# Importo la libreria de flask


from flask import Flask, render_template, json, request
# import numpy as np
import urllib.request
import validators
from urllib.parse import urlparse

app = Flask(__name__)

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

# verificar url
def url_check(url):

    try:
        # print(urllib.request.urlopen("http://"+url).getcode()
        return urllib.request.urlopen(url).getcode()
    except urllib.error.URLError as e:
        # print(e.reason)
        return "No fue posible establecer conexion con el host " + str(e.reason)


# verificar arrray de urls 
def data_check(datos):

    resultado = []
    for url in datos:
        # print(uri_validator(url))
        if len(url.strip()) > 1 and uri_validator(url) == True:
            resultado.append(url+" = "+str(url_check(url.strip())))
        elif len(url.strip()) > 1:
            resultado.append(url+" = "+"Url no valido")
    return resultado




# defino una ruta de mi app
@app.route("/")
def main():
    return render_template('index.html')

# ruta para recibir post 
@app.route('/verificar', methods=['POST'])
def signUp():

    #  obtengo los datos de mi formulario, campo urls
    _datosCampo = request.form['urls']

    # creo un array por los url recibidos
    datos = _datosCampo.split("\n")

    # verifico lo datos 
    resultados = data_check(datos)


    if _datosCampo:
        return json.dumps(resultados)
    else:
        return "error"





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run()
