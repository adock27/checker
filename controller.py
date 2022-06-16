import urllib.request

from urllib.parse import urlparse
# validar url 
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
def urls_data_check(urls):

    resultado = []
    for url in urls:
        # print(uri_validator(url))
        if len(url.strip()) > 1 and uri_validator(url) == True:
            resultado.append(url+" = "+str(url_check(url.strip())))
        elif len(url.strip()) > 1:
            resultado.append(url+" = "+"Url no valido")
    return resultado
