import urllib.request
import json
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


def url_cleaner(url):
    # limpiar espacios iniciales y finales
    new_url = url.strip()
   
    # contiene http o https
    if  "https://" in new_url or "http://" in new_url:
        return new_url
    else:
        return "http://"+new_url


   

    



# verificar arrray de urls
def urls_data_check(urls):

    resultado = []
    for url in urls:
       
        url = url_cleaner(url)

        if uri_validator(url) == True:
            resultado.append([url,str(url_check(url)),"Ok"])
        elif len(url.strip()) > 1:
            resultado.append([url,str(url_check(url)),"Error"])

    

    print(resultado)
    return resultado
