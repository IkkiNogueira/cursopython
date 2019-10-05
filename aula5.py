##### Bibliotecas #####
import bs4
import requests
import sys
import mysql


from aula5_2 import media

cnx = mysql.connector.connect(
    user='teste', 
    password='teste', 
    host='127.0.0.1', 
    database='teste')

l = [23,54,51,77,14,34]

print(media(l))

statuscode = requests.get('https://adrenaline.uol.com.br/')

print(statuscode)

try:
    numero = int(input("Entre com um numero entre 1 - 10: "))
except ValueError:
    print("Digite apenas números")
    sys.exit()
finally:
    cnx.close()