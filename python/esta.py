
import sys
import io

from string import Template

filein = open('estadistica.html')

src = Template(filein.read())

#codificacion_actual = sys.stdout.encoding

#print(codificacion_actual)

#nueva_codificacion = 'latin-1'
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding=nueva_codificacion)
#codificacion_actual = sys.stdout.encoding
#print(codificacion_actual)

from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'


import RAKE as rake
import operator
import os
import io
import PyPDF2
import textract
import pandas as pd
import pytrends
#from pytrends.request import TrendReq


import sys
import io

from string import Template
from django.shortcuts import render

#filein = open("C:/Users/USUARIO/Code/proymaestria/python/estadistica.html")

#src = Template(filein.read())


# 1. initialize RAKE by providing a path to a stopwords file
stoppath = 'C:/Users/USUARIO/Code/proymaestria/python/SmartStoplist.txt'
#rake_object = rake.Rake(stoppath, 5, 3, 4)
rake_object = rake.Rake(stoppath)
 
# 2. run on RAKE on a given text
#filename = 'C:/Users/USUARIO/Code/proymaestria/python/documents/securityart.pdf'
#file_pdf = io.open(filename, 'r', encoding="iso-8859-1")

#sample_file = io.open("data/docs/spanish/text.txt", 'r')
#text = file_pdf.read()

#pdfFileObj = open(filename,'rb')
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#num_pages = pdfReader.numPages
#count = 0
#text = ""
#recorrer las paginas del PDF y extraer el texto
#while count < num_pages:
#  pageObj = pdfReader.getPage(count)
#  count +=1
#  text += pageObj.extractText()

#if text != "":
#  text = text
#else:
#  text = textract.process(fileurl, method='tesseract', language='eng')
#print("-----------\n",text[0:1000])

def sort_keyword(tup):
  tup.sort(reverse=True)
  return tup

#keywords = sort_keyword(rake_object.run(text))
# 3. print results
#print("Keywords:", keywords)
#print("----------")

#keywords[0:10]
#result = keywords[0:10]
#print(result)

# Folder Path
path = "C:/Users/USUARIO/Code/proymaestria/python/documents/"
os.chdir(path)
#file_pdf = io.open(filename, 'r', encoding="iso-8859-1")
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
      pdfFileObj = open(file_path,'rb')             #Abrimos archivo de PDF
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  #leemos el PDF
      num_pages = pdfReader.numPages                #contamos la paginas del PDF
      print(num_pages)
      count = 0
      text = ""
      #recorrer las paginas del PDF y extraer el texto
      while count < num_pages: 
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
        text = text.encode('utf-8').decode('ascii', 'ignore')

      if text != "":
        text = text
      else:
        text = textract.process(fileurl, method='tesseract', language= "eng")  # extraemos unicamente el TEXTO en idioma INGLES
      return text
#leemos todos los PDF que estan en una carpeta
for file in os.listdir():
    print(file)
    if file.endswith(".pdf"):
        file_path = f"{path}{file}"
        print("_______________________________\n archivo: ",file_path)
        text=read_text_file(file_path)
        #print(text)
        keywords = sort_keyword(rake_object.run(text))
        result = keywords[0:10]
        print("keywords=======>\n",result)
        
list_of = dict((l,v) for l, v in result)
print (type(list_of))
print (list_of)

values= list_of.values()
print (values)

keys= list_of.keys()
print(keys)

groupkeywords = list(zip(*[iter(keys)]*1))
groupkeywords = [list(x) for x in groupkeywords]

#result = src.substitute(groupkeywords)
#try: 
#   os.mkdir("analisis")
#   filein2 = open('analisis/'+'.html','w')
#   filein2.writelines(result)
#   print("creando carpeta...")
#   print ("guardando archivo")
#except OSError:
#     if os.path.exists("analisis"):
#          filein2 = open('analisis/'+str(202245)+'.html','w')
#          filein2.writelines(result)
#          print("guardando archivo")
#while True:
#    pregunta = input("presione N si quiere continuar y S si quiere salir")
#    if pregunta == "N":
#      os.system(r"esta.py")
#    elif  pregunta == "S":
#      sys.exit()


def ini(request):
    dic = groupkeywords
    print(dic)
    return render(request, 'estadis.html', context={"dic": dic})
  




  

## Se crea la conexion, se indica que el lenguaje es español de Mexico
pytrend = TrendReq(hl='es-MX')
 
## Se construye el payload a enviar
pytrend.build_payload(kw_list=["programacion"], cat=0, timeframe='today 1-m', geo='MX', gprop='')
 
## Envia el payload para obtener la serie temporal e imprime la informacion
print(pytrend.interest_over_time())


dicti = {}
i = 1
for trending in groupkeywords:
        #pytrend.build_payload (trend, delay = & 39; today 3 m &  39;, geo = &  39; GB &  39)
        pytrend.build_payload(trending, timeframe = 'today 3-m', geo = 'GB')
        #pytrends.build_payload(trending, timeframe = 'today 3-m', geo = 'GB')
        dicti[i] = pytrend.interest_over_time ()
        i+=1

result = pd.concat(dicti, axis=1)
result.columns = result.columns.droplevel(0)
result = result.drop('isPartial', axis = 1)

result



import sys 
codificacion_actual = sys.stdout.encoding
print(codificacion_actual)
