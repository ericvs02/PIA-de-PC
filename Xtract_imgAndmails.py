from bs4 import BeautifulSoup as bs
import os
import requests
import time
import re

def obtenerDatos(query):
    
    print("Script para obtener imagenes y direcciones de correo de un sitio")
    os.system("mkdir imagenes")
    #query = input("ingrese url a analizar:")
    res=requests.get("http://"+ query) #peticion a la url
    soup=bs(res.text,"lxml")
    print("obtniendo imagenes...")
    time.sleep(3)
    for imagen in soup.find_all("img"):
        if imagen["src"].startswith("http") == False:
            download = "http://" + query + imagen["src"]
        else:
            download = imagen["src"]
        print (download)

        r = requests.get(download)
        f = open("imagenes/%s" % download.split("/")[-1],"wb")
        f.write(r.content)
        f.close()
        print("Hecho.")
    time.sleep(2)
    print("Obteniendo direcciones de correo disponibles...")

    try:
        pag = requests.get("http://"+query)
        html = bs(pag.content,"html.parser")
        
        exp=re.compile(r"\w+\d?@\w+\W\w+")  
        mo=exp.search(str(pag.content))
        print(mo.group())
    except AttributeError:
        print("No se encontraron resultados")
    
        
    
  

