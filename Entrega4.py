# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:30:29 2019

@author: Ignacio Mayer
"""

import psycopg2
# Importamos la Base de Datos
conn = psycopg2.connect(host="201.238.213.114",database="grupo18", user="grupo18", password="BQtmLl", port ="54321")


menu = True
while (menu):
    op = input('''
          ---== MENU PRINCIPAL ==---
          1- LOGIN
          2- SALIR
          
          '''
            )
    if op == '1':
      query = 'SELECT * FROM tennant'
      loc = conn.cursor()
      loc.execute(query)
      a = loc.fetchall()
      loc.close()
      tennants = []
      print ('ID  | Telefono')
      
      i = 0
      while i < len(a):
          b = []
          b.append(a[i][0])
          b.append(a[i][1])
          print ('{}  | {}'.format(a[i][0], a[i][1]))
          tennants.append(b)
          i+=1
      inicio_sesion = True
      while (inicio_sesion):
          tennant = int(input('''
                    Ingrese ID 
                    Iniciar sesion Tennant: ''' ))
          j = 0
          for i in tennants:
              if i[0] == tennant:
                  inicio_sesion = False
        
              j+=1
      query = 'SELECT * FROM agente'
      loc = conn.cursor()
      loc.execute(query)
      a = loc.fetchall()
      loc.close()
      agentes = []
      
    elif op == '2':
      menu = False
      
print ('hola')
        