
# Importo la libreria de flask


from flask import Flask, render_template, json, request

from controller import *

app = Flask(__name__)


# raiz app
@app.route("/")
def main():
    return render_template('index.html')

# ruta para recibir post 
@app.route('/verificar', methods=['POST'])
def validar():

    #  obtengo los datos de mi formulario, campo urls
    _field_data = request.form['urls']

    # creo un array por los url recibidos
    urls = _field_data.split("\n")

    # verifico lo datos 
    resultados = urls_data_check(urls)


    if _field_data:
        return json.dumps(resultados)
    else:
        return "error"





if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run()
