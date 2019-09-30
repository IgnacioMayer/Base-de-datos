# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:30:29 2019

@author: Ignacio Mayer
"""

import psycopg2
# Importamos la Base de Datos
conn = psycopg2.connect(host="201.238.213.114",database="grupo18", user="grupo18", password="BQtmLl", port ="54321")


print ("--------------------------------------------------------")
print ("               ---== CrossNot ==---                     ")
print ("--------------------------------------------------------")
print ("")
print ("")


login = True
while (login):
    op = input('''
          ---== MENU PRINCIPAL ==---
          [1] LOGIN
          [2] Salir de CrossNot
          
          Ingrese una opcion [1-2]:   ''')
    
    if op == '1':
      query = 'SELECT * FROM tennant'
      loc = conn.cursor()
      loc.execute(query)
      a = loc.fetchall()
      loc.close()
      tennants = []
      print ()
      print("Lista de Tennants en CrossNot")
      print()
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
                    Ingrese ID Tennant para  
                    Iniciar Sesion: ''' ))
          
          for i in tennants:
              if i[0] == tennant:
                  inicio_sesion = False
                  
      menu = True 
      while (menu):
          mp = int(input('''
                       ---== OPCIONES ==---
                  [1] Ver Llamadas
                  [2] Evaluar Llamadas
                  [3] Manejar Campañas
                  [4] Manejar Tipificaciones
                  [5] Manejar Agentes
                  [6] Manejar Supervisores
                  [7] Manejar Tennants 
                  [8] Salir de CrossNot 
                  
                  Ingrese una opcion [1-8]:   '''))
            
          if mp == 3:
                campagna = int(input('''
                                    [1] Agregar Campaña
                                    [2] Eliminar Campaña
                                    [3] Editar Campaña
                                        
                                    Ingrese una opcion [1-3]:   '''))
                if campagna == 1:
                    c1 = int(input("Ingrese id_campaña:  "))
                    c2 = input("Ingrese fecha inicio campaña (ej: '2019-09-30'):   ")
                    c3 = input("Ingrese fecha fin campaña (ej: '2019-10-12'):   ")
                    c4 = input("Ingrese id_tennant:   ")
                    cur5 = conn.cursor()
                    cur5.execute("INSERT INTO campagna(id_campagna,inicio,fin,id_tennant) VALUES({},{},{},{});".format('c1','c2','c3','c4'))
                    conn.commit()
                    cur5.close()
                elif campagna == 2:
                    c1 = int(input("Ingrese id_campaña:  "))
                    cur5 = conn.cursor()
                    cur5.execute("DELETE FROM campagna WHERE id_campagna = c1 .......;")
                    conn.commit()
                    cur5.close()
                elif campagna == 3:
                        c1 = int(input("Ingrese id_campaña:  "))
                        print()
                        ed5 = int(input('''
                                    [1] Editar id_campaña
                                    [2] Editar fecha inicio campaña
                                    [3] Editar fecha fin campaña
                                    [4] Editar id_tennant
                                        
                                    Ingrese una opcion [1-4]:   '''))
                        if ed5 == 1:
                            ed5n = int(input("Ingrese nuevo id_campaña:  "))
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET id_campagna = ed5n WHERE id_campagna = c1 .......;")
                            conn.commit()
                            cur5.close()
                        elif ed5 == 2:
                            ed5n = input("Ingrese nueva fecha inicio(ej: '2019-09-30'):  ")
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET inicio = ed5n WHERE id_campagna = c1 .......;")
                            conn.commit()
                            cur5.close()
                        elif ed5 == 3:
                            ed5n = input("Ingrese nueva fecha fin (ej: '2019-10-12'):  ")
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET fin = ed5n WHERE id_campagna = c1 .......;")
                            conn.commit()
                            cur5.close()
                        elif ed5 == 4:
                            ed5n = int(input("Ingrese nuevo id_tennant:  "))
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET id_tennant = ed5n WHERE id_campagna = c1 .......;")
                            conn.commit()
                            cur5.close()
                    
                else:
                    print('Opcion invalida, ingrese opcion nuevamente')
                    campagna = int(input('''
                                    [1] Agregar Campaña
                                    [2] Eliminar Campaña
                                    [3] Editar Campaña)
                                        
                                    Ingrese una opcion [1-3]:   '''))
      
        
    elif op == '2':
          login = False


      
    
      

conn.close()      