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
          m=0
          for i in tennants:
              if i[0] == tennant:
                  inicio_sesion = False
              else:
                  if m == len(tennants)-1:
                      print ()
                      print('Opcion invalida, ingrese opcion nuevamente')     
              m+= 1
                  
      menu = True 
      while (menu):
          mp = int(input('''
                       ---== MENU OPCIONES ==---
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
              query = 'SELECT * FROM campagna'
              loc = conn.cursor()
              loc.execute(query)
              a = loc.fetchall()
              loc.close()
              campagnas = []
              print ()
              print("Lista de Campañas en CrossNot")
              print()
              print ('Id_campaña | Fecha inicio campaña | Fecha fin campaña | Id_tennant')
              
              i = 0
              while i < len(a):
                  b = []
                  b.append(a[i][0])
                  b.append(a[i][1])
                  print ('{}     | {}     | {}    |     {}'.format(a[i][0], a[i][1], a[i][2], a[i][3]))
                  campagnas.append(b)
                  i+=1
                  
              o3 = True 
              while (o3):
                  campagna = int(input('''
                     ---== Manejar Campañas ==---
                     [1] Agregar Campaña
                     [2] Eliminar Campaña
                     [3] Editar Campaña
                     [4] Volver Menu Opciones
                     [5] Salir de CrossNot
                        
                     Ingrese una opcion [1-5]:   '''))
                          
                  #Opcion Invalida
                  while campagna <1 or campagna >=6:
                    print()
                    print('Opcion invalida, ingrese opcion nuevamente')
                    print()
                    campagna = int(input('''
                     ---== Manejar Campañas ==---
                     [1] Agregar Campaña
                     [2] Eliminar Campaña
                     [3] Editar Campaña
                     [4] Volver Menu Opciones
                     [5] Salir de CrossNot
                        
                     Ingrese una opcion [1-5]:   '''))
                    
                  #agregar campaña
                  if campagna == 1:
                    ingresar = True 
                    while (ingresar):
                      c1 = int(input("Ingrese id_campaña:  "))
                      j=0
                      for i in campagnas:
                          if i[0] == c1:
                              if j == len(campagnas)-1:
                                  print ()
                                  print('Este id_campaña ya existe, ingrese otra opcion nuevamente')                                                        
                          else:
                              ingresar = False 
                          j+= 1    
                    '''
                    c2 = input("Ingrese fecha inicio campaña (ej: '2019-09-30'):   ")
                    c3 = input("Ingrese fecha fin campaña (ej: '2019-10-12'):   ")
                    cur5 = conn.cursor()
                    cur5.execute("INSERT INTO campagna(id_campagna,inicio,fin,id_tennant) VALUES({},{},{},{});".format('c1','c2','c3','tennant'))
                    conn.commit()
                    cur5.close()'''
                    print('hola')
                    break 
                  
                  ingresar = True 
                  while (ingresar):
                      c1 = int(input("Ingrese id_campaña:  "))
                      j=0
                      for i in campagnas:
                          if i[0] == c1:
                              ingresar = False 
                          else:
                              if j == len(campagnas)-1:
                                  print ()
                                  print('Opcion invalida, ingrese opcion nuevamente')     
                          j+= 1
                            
                  #eliminar campaña
                  if campagna == 2:
                    cur5 = conn.cursor()
                    cur5.execute("DELETE FROM campagna WHERE id_campagna = {};".format('c1'))
                    conn.commit()
                    cur5.close()
                    break
                  #editar campaña
                  elif campagna == 3:
                        print()
                        ed5 = int(input('''
                            ---== Editor de Campañas ==---
                            [1] Editar id_campaña
                            [2] Editar fecha inicio campaña
                            [3] Editar fecha fin campaña
                            [4] Editar id_tennant
                            [5] Volver Menu Opciones
                            [6] Salir de CrossNot
                            
                                
                            Ingrese una opcion [1-6]:   '''))
                        
                        #Opcion invalida 
                        while ed5 < 1 or ed5 >= 7:
                            print()
                            print('Opcion invalida, ingrese opcion nuevamente')
                            print()
                            ed5 = int(input('''
                            ---== Editor de Campañas ==---
                            [1] Editar id_campaña
                            [2] Editar fecha inicio campaña
                            [3] Editar fecha fin campaña
                            [4] Editar id_tennant
                            [5] Volver Menu Opciones
                            [6] Salir de CrossNot
                                
                            Ingrese una opcion [1-6]:   '''))
                        #Editar id_campaña
                        if ed5 == 1:
                            ed5n = int(input("Ingrese nuevo id_campaña:  "))
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET id_campagna = {} WHERE id_campagna = {};".format('ed5n','c1'))
                            conn.commit()
                            cur5.close()
                        #Editar fecha inicio campaña
                        elif ed5 == 2:
                            ed5n = input("Ingrese nueva fecha inicio(ej: '2019-09-30'):  ")
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET inicio = {} WHERE id_campagna = {};".format('ed5n','c1'))
                            conn.commit()
                            cur5.close()
                        #Editar fecha fin campaña
                        elif ed5 == 3:
                            ed5n = input("Ingrese nueva fecha fin (ej: '2019-10-12'):  ")
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET fin = {} WHERE id_campagna = {};".format('ed5n','c1'))
                            conn.commit()
                            cur5.close()
                        #Editar id_tennant
                        elif ed5 == 4:
                            ed5n = int(input("Ingrese nuevo id_tennant:  "))
                            cur5 = conn.cursor()
                            cur5.execute("UPDATE campagna SET id_tennant = {} WHERE id_campagna = {};".format('ed5n','c1'))
                            conn.commit()
                            cur5.close() 
                        #Volver Menu Opciones
                        elif ed5 == 5:
                            break 
                        #Salir de CrossNot
                        elif ed5 == 6 :
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            break 
                        
                  #Volver Menu Opciones
                  elif campagna == 4:  
                    o3 = False
                  #Salir de CrossNot
                  elif campagna == 5:
                    print()
                    print("Gracias por utilizar CrossNot")
                    menu = False
                    login = False
                    break 
            
            
          elif mp == 8:
              print()
              print("Gracias por utilizar CrossNot")
              login = False
              break 
              
                
  
        
    
    elif op == '2':
          login = False


      
conn.close()     
     

    