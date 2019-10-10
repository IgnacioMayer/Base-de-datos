# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:30:29 2019

@author: Ignacio Mayer
"""

#funcion IS_INT me ayda a determinar si es o no un valor numerico. me inspiro en la funcion de c#

def Is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def Is_str(x):
    try:
        int(x)
        return False
    except:
        return True

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
      print('ID |  Telefono')
      
      i = 0
      while i < len(a):
          b = []
          b.append(a[i][0])
          b.append(a[i][1])
          print(' {} | {}'.format(a[i][0],a[i][1]))
          tennants.append(b)
          i+=1
     
      inicio_sesion = True
      while (inicio_sesion):
          tennant = input('''
                    Ingrese ID Tennant para  
                    Iniciar Sesion: ''' )
          
          if(Is_int(tennant)):
              tennant = int(tennant)
              for i in tennants:
                  if tennant in i:
                      inicio_sesion = False
          
          else:
              print("Ingrese opcion valida.")
          
      menu = True 
      while (menu):
          mp = input('''
                       ---== MENU OPCIONES ==---
                  [1] Ver Llamadas
                  [2] Evaluar Llamadas
                  [3] Manejar Campañas
                  [4] Manejar Tipificaciones
                  [5] Manejar Agentes
                  [6] Manejar Supervisores
                  [7] Manejar Tennants 
                  [8] Salir de CrossNot 
                  
                  Ingrese una opcion [1-8]:   ''')
          if (Is_int(mp)):
              mp = int(mp)
              if mp == 1:
                  o1 = True 
                  while (o1):
                      llamada = input('''
                         ---== Ver Llamadas ==---
                         [1] Ver Llamada
                         [2] Agregar Llamada
                         [3] Editar Campaña
                         [4] Eliminar Llamada
                         [5] Volver Menu Opciones
                         [6] Salir de CrossNot
                            
                         Ingrese una opcion [1-6]:   ''')
                      if (Is_int(llamada)):
                          llamada = int(llamada)
                          #Volver Menu Opciones
                          if llamada == 5:  
                            o1 = False
                          #Salir de CrossNot
                          elif llamada == 6:
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break    
                     
                      
                    
              elif mp == 2:
                  o2 = True 
                  while (o2):
                      query = 'SELECT id_supervisor FROM supervisor WHERE id_tennant = {};'.format(tennant)
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close()
                      supervisores = []
                      i = 0
                      while i < len(a):
                          supervisores.append(a[i][0])
                          i+=1
                      llamada2 = input('''
                         ---== Evaluar Llamadas ==---
                         [1] Agregar calificación
                         [2] Editar calificación
                         [3] Eliminar calificación
                         [4] Volver Menu Opciones
                         [5] Salir de CrossNot
                            
                         Ingrese una opcion [1-5]:   ''')
                      if (Is_int(llamada2)):
                          llamada2 = int(llamada2)
                          if 0<llamada2<4:
                              #mostramos todas las llamdas ya clasificadas
                              query = 'SELECT l.id_llamada, l.id_supervisor, l.aprobacion FROM llamada l, supervisor s WHERE l.id_supervisor = s.id_supervisor AND s.id_tennant = {} ORDER BY l.id_supervisor;'.format(tennant)
                              loc = conn.cursor()
                              loc.execute(query)
                              a = loc.fetchall()
                              loc.close()
                              l_clasificadas = [] #id de llamadas ya clasificadas
                              print ()
                              print("Lista de llamadas clasificadas del Tennant {}".format(tennant))
                              print('id_llamada | id_supervisor | aprobacion')
                          
                              i = 0
                              while i < len(a):
                                  print('    {}     |        {}     |    {}     '.format(a[i][0],a[i][1], a[i][2]))
                                  l_clasificadas.append(a[i][0])
                                  i+=1
                                  
                          if llamada2 == 1:
                              comprobar = True
                              while(comprobar):
                                  
                                  supervisor = input('Ingrese su Id de supervisor: ')
                                  if (Is_int(supervisor)):
                                      supervisor = int(supervisor)
                                      if supervisor in supervisores:
                                          query = 'SELECT id_llamada FROM llamada l NATURAL JOIN agente a WHERE  l.aprobacion IS NULL AND a.id_tennant = {};'.format(tennant)
                                          loc = conn.cursor()
                                          loc.execute(query)
                                          a = loc.fetchall()
                                          loc.close()
                                          llamada = []
                                          print('ids llamadas sin supervisar')
                                          print('-------------------------')
                                          i = 0
                                          while i < len(a):
                                              llamada.append(a[i][0])
                                              print(a[i][0])
                                              i+=1
                                          i = True
                                          while (i):
                                              aprobar = input('Ingrese id de la llamada que desea supervisar: ')
                                              if (Is_int(aprobar)):
                                                  aprobar = int(aprobar)
                                                  if aprobar in llamada:
                                                      x = input('Ingrese (1) si desea aprobar la llamada, (0) para desaprobar: ')
                                                      if (Is_int(x)):
                                                           x = int(x)
                                                           if x == 1:
                                                               
                                                                cur = conn.cursor()
                                                                cur.execute("UPDATE llamada SET aprobacion = 1, id_supervisor = {} WHERE id_llamada = {};".format(supervisor, aprobar))
                                                                conn.commit()
                                                                cur.close()
                                                                i = False
                                                                comprobar = False
                                                           elif x == 0:
                                                                cur = conn.cursor()
                                                                cur.execute("UPDATE llamada SET aprobacion = 1, id_supervisor = {} WHERE id_llamada = {};".format(supervisor, aprobar))
                                                                conn.commit()
                                                                cur.close()
                                                                i = False
                                                                comprobar = False
                                                           else:
                                                               print ("Ingrese número válido...")
                                                      else:
                                                           print("Ingrese un número...")
                                      else:    
                                          print('''
                                                ERROR: Este id de supervisor no pertenece al Tennant {}
                                          '''.format(tennant))
                          
                          elif llamada2 == 2:
                              l = input('Ingrese el id de la llamada para la cual quiere editar su calificación: ')
                              if (Is_int(l)):
                                  l = int(l)
                                  if l in l_clasificadas:
                                      s = input('Ingrese su id de supervisor: ')
                                      if (Is_int(s)):
                                           s = int(s)
                                           if s in supervisores:
                                              x = input('Ingrese (1) si desea aprobar la llamada, (0) para desaprobar: ')
                                              if (Is_int(x)):
                                                   x = int(x)
                                                   if x == 1:      
                                                        cur = conn.cursor()
                                                        cur.execute("UPDATE llamada SET aprobacion = 1, id_supervisor = {} WHERE id_llamada = {};".format(s, aprobar))
                                                        conn.commit()
                                                        cur.close()
                                                        i = False
                                                        comprobar = False
                                                   elif x == 0:
                                                        cur = conn.cursor()
                                                        cur.execute("UPDATE llamada SET aprobacion = 1, id_supervisor = {} WHERE id_llamada = {};".format(s, aprobar))
                                                        conn.commit()
                                                        cur.close()
                                                        i = False
                                                        comprobar = False
                                                   else:
                                                       print ("Ingrese número válido...")
                                              else:
                                                   print("Ingrese un número...")
                                           else:    
                                              print('''
                                                        ERROR: Este id de supervisor no pertenece al Tennant {}
                                                  '''.format(tennant))
                                      
                                        
                                  else:
                                      print ('Esta llamada no puede ser editada.')
                              else:
                                  print ('Ingrese números')
                                     
                          elif llamada2 == 3:
                              i = input('Ingrese el id de la llamada a la cual usted quiere eliminar la calificación: ')
                              if (Is_int(i)):
                                  i = int(i)
                                  o = True
                                  while (o):
                                      eliminar = input('''Esta seguro que desea eliminar la calificacion?
                                                       
                                                          si (1)                       no (2)          
                                      ''')
                                      if (eliminar == '1'):
                                            cur = conn.cursor()
                                            cur.execute("UPDATE llamada SET aprobacion = NULL, id_supervisor = NULL WHERE id_llamada = {};".format(i))
                                            conn.commit()
                                            cur.close()
                                            o = False
                                      elif (eliminar == '2'):
                                          o = False
                                      else:
                                          print ('Ingrese una opcion válida.')
                          #Volver Menu Opciones
                          elif llamada2 == 4:  
                            o2 = False
                          #Salir de CrossNot
                          elif llamada2 == 5:
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break
                    
              elif mp == 3:
                  query = '''SELECT c.id_campagna, c.inicio, c.fin
                            FROM campagna c, tennant t 
                            WHERE c.id_tennant = t.id AND c.id_tennant = {}
                            ORDER BY c.id_campagna'''.format(tennant)
                  loc = conn.cursor()
                  loc.execute(query)
                  a = loc.fetchall()
                  loc.close()
                  campagnas = []
                  print ()
                  print("Lista de Campañas del Tennant {} en CrossNot".format(tennant))
                  print()
                  print ('Id_campaña | Fecha inicio campaña | Fecha fin campaña')
                  
                  i = 0
                  while i < len(a):
                      b = []
                      b.append(a[i][0])
                      b.append(a[i][1])
                      b.append(a[i][2])
                      print ('{}     | {}     | {}    '.format(a[i][0], a[i][1], a[i][2]))
                      campagnas.append(b)
                      i+=1
                      
                  o3 = True 
                  while (o3):
                      campagna = input('''
                         ---== Manejar Campañas ==---
                         [1] Agregar Campaña
                         [2] Eliminar Campaña
                         [3] Editar Campaña
                         [4] Volver Menu Opciones
                         [5] Salir de CrossNot
                            
                         Ingrese una opcion [1-5]:   ''')
                      if (Is_int(campagna)):
                          campagna = int(campagna)  
                          if 0<campagna<6: 
                              
                              #agregar campaña
                              if campagna == 1: 
                                c2 = input("Ingrese fecha inicio campaña (ej: '2019-09-30'):   ")
                                c3 = input("Ingrese fecha fin campaña (ej: '2019-10-12'):   ")
                                cur5 = conn.cursor()
                                cur5.execute("INSERT INTO campagna(inicio,fin,id_tennant) VALUES('{}','{}',{});".format(c2,c3,tennant))
                                conn.commit()
                                cur5.close()
                                break 
                              
                              ingresar = True 
                              while (ingresar):
                                  c1 = input("Ingrese id_campaña que quiere editar o eliminar:  ")
                                  if (Is_int(c1)):
                                      c1 = int(c1)
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
                                cur5.execute("DELETE FROM campagna WHERE id_campagna = {};".format(c1))
                                conn.commit()
                                cur5.close()
                                break
                              #editar campaña
                              elif campagna == 3:
                                    print()
                                    ed5 = input('''
                                        ---== Editor de Campañas ==---
                                        [1] Editar id_campaña
                                        [2] Editar fecha inicio campaña
                                        [3] Editar fecha fin campaña
                                        [4] Editar id_tennant
                                        [5] Volver Menu Opciones
                                        [6] Salir de CrossNot
                                        
                                            
                                        Ingrese una opcion [1-6]:   ''')
                                    if (Is_int(ed5)):
                                        llamada = int(ed5)
                                        #Editar id_campaña
                                        if ed5 == 1:
                                            ed5n = int(input("Ingrese nuevo id_campaña:  "))
                                            cur5 = conn.cursor()
                                            cur5.execute("UPDATE campagna SET id_campagna = {} WHERE id_campagna = {};".format(ed5n,c1))
                                            conn.commit()
                                            cur5.close()
                                            break
                                        #Editar fecha inicio campaña
                                        elif ed5 == 2:
                                            ed5n = input("Ingrese nueva fecha inicio(ej: '2019-09-30'):  ")
                                            cur5 = conn.cursor()
                                            cur5.execute("UPDATE campagna SET inicio = {} WHERE id_campagna = {};".format(ed5n,c1))
                                            conn.commit()
                                            cur5.close()
                                            break
                                        #Editar fecha fin campaña
                                        elif ed5 == 3:
                                            ed5n = input("Ingrese nueva fecha fin (ej: '2019-10-12'):  ")
                                            cur5 = conn.cursor()
                                            cur5.execute("UPDATE campagna SET fin = {} WHERE id_campagna = {};".format(ed5n,c1))
                                            conn.commit()
                                            cur5.close()
                                            break
                                        #Editar id_tennant
                                        elif ed5 == 4:
                                            ed5n = int(input("Ingrese nuevo id_tennant:  "))
                                            cur5 = conn.cursor()
                                            cur5.execute("UPDATE campagna SET id_tennant = {} WHERE id_campagna = {};".format(ed5n,c1))
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
                                            conn.close()  
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
                                conn.close()  
                                break 
                          else: 
                              print('Ingrese opcion valida')
                                
                
              elif mp == 4: 
                  query = '''SELECT c.id_campagna,c.inicio, c.fin
                            FROM campagna c, tennant t 
                            WHERE c.id_tennant = t.id AND c.id_tennant = {}
                            ORDER BY c.id_campagna'''.format(tennant)
                  loc = conn.cursor()
                  loc.execute(query)
                  a = loc.fetchall()
                  loc.close()
                  campagnas4 = []
                  print ()
                  print("Lista de Campañas del Tennant {} en CrossNot".format(tennant))
                  print()
                  print ('Id_campaña')
                  
                  i = 0
                  while i < len(a):
                      b=[]
                      b.append(a[i][0])
                      b.append(a[i][1])
                      b.append(a[i][2])
                      print ('{}     '.format(a[i][0]))
                      campagnas4.append(b)
                      i+=1

                  o4 = True 
                  while (o4):
                       select_campagna = input('Seleccione Id_Campaña:    ')
                       if (Is_int(select_campagna)):
                          select_campagna = int(select_campagna) 
                          if select_campagna in campagnas4[0]:
                              ct = True
                              while (ct):
                                  query = '''SELECT c.id_campagna, c.id_tipificacion, t.dato
                                            FROM tipificacion_campagna c, tipificacion t
                                            WHERE c.id_tipificacion = t.id_tipificacion AND c.id_campagna = {} 
                                            Order By c.id_tipificacion;'''.format(select_campagna)
                                  loc = conn.cursor()
                                  loc.execute(query)
                                  a = loc.fetchall()
                                  loc.close()
                                  tipificaciones = []
                                  print ()
                                  print("Lista de Tipificaciones de la Campaña {}".format(select_campagna))
                                  print()
                                  print ('Id_Tipificacion   |  Tipificacion (Dato)')
                                  
                                  i = 0
                                  while i < len(a):
                                      b = []
                                      b.append(a[i][0])
                                      b.append(a[i][1])
                                      b.append(a[i][2])
                                      print ('{}               |  {}   '.format(a[i][1],a[i][2]))
                                      tipificaciones.append(b)
                                      i+=1     
                                      
                                  e =0
                                  id_tipi_campa = []
                                  while e < len(a):
                                      id_tipi_campa.append((a[e][1]))
                                      e+=1
                             
                                  tip = input('''
                     ---== Manejar Tipificaciones ==---
                     [1] Agregar tipificación
                     [2] Asociar tipificación
                     [3] Eliminar tipificación
                     [4] Editar tipificación
                     [5] Editar asociación 
                     [6] Volver Menu Opciones
                     [7] Salir de CrossNot
                        
                     Ingrese una opcion [1-7]:   ''')
                                   
                                  if (Is_int(tip)):
                                      tip = int(tip) 
                                      if 0<tip<8:
                                          if tip == 1: 
                                              agregar = True
                                              while(agregar):
                                                  nuevo_dato = input('Ingrese la tipificacion nueva (tipo de dato):   ').upper()
                                                  if (Is_str(nuevo_dato)):                                                
                                                      nuevo_dato = str(nuevo_dato)
                                                      cur1= conn.cursor()
                                                      cur1.execute("INSERT INTO tipificacion(Dato) VALUES('{}');".format(nuevo_dato))
                                                      conn.commit()
                                                      cur1.close()
                                                      
                                                      query1 = 'select t.id_tipificacion from tipificacion t;'
                                                      loc2 = conn.cursor()
                                                      loc2.execute(query1)
                                                      a2 = loc2.fetchall()
                                                      loc2.close()
                                                      id_tipificaciones_totales = []
                                                      
                                                      g = 0
                                                      while g < len(a2):
                                                          id_tipificaciones_totales.append(a2[g][0])
                                                          g+=1 
                                                          
                                                      nuevo_id_tipi= id_tipificaciones_totales[len(id_tipificaciones_totales)-1]
                                                  
                                                      cur2= conn.cursor()
                                                      cur2.execute("INSERT INTO tipificacion_campagna(id_campagna,id_tipificacion) VALUES({},{});".format(select_campagna,nuevo_id_tipi))
                                                      conn.commit()
                                                      cur2.close()
                                                      
                                                      agregar = False
                                                      ct = False
                                                      o4 = False
                                                      break
                                                  else:
                                                      print('Ingrese opcion valida')
                                          elif tip ==2:
                                              acociar = True
                                              while(acociar):
                                                  query1 = '''SELECT l.id_llamada
                                                            FROM llamada l JOIN agente a on l.id_agente = a.id_agente JOIN tennant t on t.id=a.id_tennant
                                                            WHERE t.id = {}
                                                            GROUP BY l.id_llamada
                                                            ORDER BY l.id_llamada'''.format(tennant)
                                                  loc2 = conn.cursor()
                                                  loc2.execute(query1)
                                                  a2 = loc2.fetchall()
                                                  loc2.close()
                                                  llamadas_tennant = []
                                                  print ()
                                                  print("Lista de Llamadas del Tennant {} en CrossNot".format(tennant))
                                                  print()
                                                  print ('Id_llamada')
    
                                                  g = 0
                                                  while g < len(a2):
                                                      print('{}'.format(a2[g][0]))
                                                      llamadas_tennant.append(a2[g][0])
                                                      g+=1 
                                                     
                                          elif tip == 3: 
                                              eliminar = True
                                              while (eliminar): 
                                                  elegir_tipi = input('Ingrese id_tipificacion que desea eliminar:   ')
                                                  if (Is_int(elegir_tipi)):
                                                      elegir_tipi = int(elegir_tipi)
                                                      
                                                      if elegir_tipi in id_tipi_campa:
                                                          o = True
                                                          while (o):
                                                              eliminar1 = input('''Esta seguro que desea eliminar la calificacion?
                                                                               
                                                                                  si (1)                       no (2)          
                                                              ''')
                                                              if (eliminar1 == '1'):
                                                                    cur = conn.cursor()
                                                                    cur.execute("DELETE FROM tipificacion WHERE id_tipificacion = {};".format(elegir_tipi))
                                                                    conn.commit()
                                                                    cur.close()
                                                                    o = False
                                                                    eliminar = False
                                                                    break
                                                              elif (eliminar1 == '2'):
                                                                  break 
                                                              else:
                                                                  print ('Ingrese una opcion válida.')
                                                                  o=False 
                                                      else: 
                                                          print('Ingrese una tipificacion de la campaña {}'.format(select_campagna))
                                                  else: 
                                                      print('Ingrese un numero porfavor')
                                                     
                                                  
                                          if tip == 5:
                                              edit_aso = True 
                                              while (edit_aso):
                                                  elegir_tipi = input('Ingrese id_tipificacion que desea editar:   ')
                                                  if (Is_int(elegir_tipi)):
                                                      elegir_tipi = int(elegir_tipi)
                                                      if elegir_tipi in id_tipi_campa:
                                                      
                                                          query1 = '''Select d.id_llamada, p.dato
                                                                        From campagna c JOIN tennant t on c.id_tennant = t.id JOIN tipificacion_campagna e on e.id_campagna = c.id_campagna JOIN tipificacion p on e.id_tipificacion = p.id_tipificacion JOIN tipificacion_dato d on d.id_tipificacion = p.id_tipificacion 
                                                                        where c.id_campagna = {} AND p.id_tipificacion = {}
                                                                        group by d.id_llamada, p.dato
                                                                        order by d.id_llamada'''.format(select_campagna,elegir_tipi) 
                                                          loc2 = conn.cursor()
                                                          loc2.execute(query1)
                                                          a2 = loc2.fetchall()
                                                          loc2.close()
                                                          llamadas_camp_tipi = []
                                                          print ()
                                                          print("Lista de Llamadas de la Campaña {} en CrossNot".format(select_campagna))
                                                          print()
                                                          print ('Id_llamada')
                                                          
                                                          i = 0
                                                          while i < len(a2):
                                                              b = []
                                                              b.append(a2[i][0])
                                                              b.append(a2[i][1])
                                                              
                                                              print ('{}   '.format(a2[i][0]))
                                                              llamadas_camp_tipi.append(b)
                                                              i+=1  
                                                              
                                                          id_llamada_camp =[]
                                                          g = 0
                                                          while g < len(a2):
                                                              id_llamada_camp.append(a2[g][0])
                                                              g+=1 
                                                          elige_llamada = input('Ingrese id_llamada que desea editar:   ')
                                                          if (Is_int(elige_llamada)):
                                                              elige_llamada = int(elige_llamada)
                                                              if elige_llamada in id_llamada_camp:
                                                                    val = llamadas_camp_tipi[0][1]
                                                                    edit_valor = input("Ingrese nuevo valor de {} para la llamada {}:   ".format(val,elige_llamada))
                                                                    cur5 = conn.cursor()
                                                                    cur5.execute("UPDATE tipificacion_dato SET valor = '{}' WHERE id_llamada = {} AND id_tipificacion = {};".format(edit_valor,elige_llamada,elegir_tipi))
                                                                    conn.commit()
                                                                    cur5.close()
                                                                    edit_aso = False
                                                                    ct = False
                                                                    o4 = False 
                                                                    break
                                                                    
                                                              else: 
                                                                  print('Ingrese una llamada de la tipificacion {}'.format(elegir_tipi))
                                                          else:
                                                             print('Ingrese un numero porfavor') 
                                                      else: 
                                                          print('Ingrese una tipificacion de la campaña {}'.format(select_campagna))
                                                  else: 
                                                      print('Ingrese un numero porfavor')
                                                      
                                                  
                                                                
                                              
                                          #Volver Menu Opciones
                                          if tip == 6:  
                                            o4 = False
                                          #Salir de CrossNot
                                          elif tip == 7:
                                            print()
                                            print("Gracias por utilizar CrossNot")
                                            menu = False
                                            login = False
                                            conn.close()  
                                            break  
                                      else:
                                          print('Ingrese opcion valida')
                          else: 
                                  print('ERROR: Este id de campaña no pertenece al Tennant {}'.format(tennant))
                                    
                      
              elif mp == 5:
                  o5 = True 
                  while (o5):
                      id_tennants = []
                      for i in tennants:
                          id_tennants.append(i[0])
                      print (''' 
                                   --== Agentes actuales del Tennant {} ==--
                                   '''.format(tennant))
                      query = 'SELECT * FROM agente WHERE id_tennant = {}'.format(tennant)
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close()
                      id_agentes = []
                      print('ID |  nombre  |  apellido  |  ID tennant')
                      
                      i = 0
                      while i < len(a):
                          print(' {} | {} | {} | {}'.format(a[i][0],a[i][1], a[i][2], a[i][3]))
                          id_agentes.append(a[i][0])
                          i+=1
                      
                      agente = input('''
                         ---== Manejar Agentes ==---
                         [1] Agregar agente
                         [2] Editar información
                         [3] Eliminar agente
                         [4] Volver Menu Opciones
                         [5] Salir de CrossNot
                            
                         Ingrese una opcion [1-5]:   ''')
                      if (Is_int(agente)):
                          agente = int(agente)
                          #Volver Menu Opciones
                          if agente == 1:
                              nombre = input("Ingrese Nombre: ").upper()
                              apellido = input("Ingrese Apellido: ").upper()
                              
                              cur5 = conn.cursor()
                              cur5.execute("INSERT INTO agente(nombre, apellido ,id_tennant) VALUES({},{},{});".format(nombre,apellido,tennant))
                              conn.commit()
                              cur5.close()
                        
                          elif agente == 2:
                                print('''
                                    ---== Editor de Agentes ==---
                                    ''')
                                edit = input("Ingrese el id del agente al cual desea editar: ")
                                if (Is_int(edit)):
                                    edit = int(edit)
                                    if (edit in id_agentes):
                                        query = 'SELECT * FROM agente WHERE id_agente = {}'.format(edit)
                                        loc = conn.cursor()
                                        loc.execute(query)
                                        a = loc.fetchall()
                                        loc.close()
                                        id_agentes = []
                                        print('ID |  nombre  |  apellido  |  ID tennant')
                                      
                                        i = 0
                                        while i < len(a):
                                            print(' {} | {} | {} | {}'.format(a[i][0],a[i][1], a[i][2], a[i][3]))
                                            i+=1
                                    
                                        ed5 = input('''
                                            [1] Editar nombre
                                            [2] Editar apellido
                                            [3] Editar id tennant 
                                            [3] Volver Menu Opciones
                                            [4] Salir de CrossNot
                                            
                                                
                                            Ingrese una opcion [1-5]:   ''')
                                        if (Is_int(ed5)):
                                            ed5 = int(ed5)
                                            #Editar id_campaña
                                            if ed5 == 1:
                                                nombre = input("Ingrese nuevo nombre:  ").upper()
                                                cur5 = conn.cursor()
                                                cur5.execute("UPDATE agente SET nombre = {} WHERE id_agente = {};".format(nombre, edit))
                                                conn.commit()
                                                cur5.close() 
                                                break
                                            elif ed5 == 2:
                                                apellido = input("Ingrese nuevo apellido:  ").upper()
                                                cur5 = conn.cursor()
                                                cur5.execute("UPDATE agente SET apellido = {} WHERE id_agente = {};".format(apellido, edit))
                                                conn.commit()
                                                cur5.close() 
                                                break
                                            elif ed5 == 3:
                                                  tennant1 = input("Ingrese id_tennant donde trabajará: ")
                                                  if (Is_int(tennant1)):
                                                      tennant1 = int(tennant1)
                                                      if tennant1 in id_tennants:
                                                            cur5 = conn.cursor()
                                                            cur5.execute("UPDATE agente SET id_tennant = {} WHERE id_agente = {};".format(tennant1, edit))
                                                            conn.commit()
                                                            cur5.close()
                                                      else:
                                                          print("El id Tennant ingresado no existe en nuestros registros...")
                                                  else:
                                                      print ("Error:   Ingrese un número")
                                            #Volver Menu Opciones
                                            elif ed5 == 4:
                                                break 
                                            #Salir de CrossNot
                                            elif ed5 == 5 :
                                                print()
                                                print("Gracias por utilizar CrossNot")
                                                menu = False
                                                login = False
                                                conn.close()  
                                                break 
                                            else:
                                                print("Ingrese opción válida.")
                                        else:
                                                print("Ingrese opción válida.")
                          elif agente == 3:
                                errase = input("Ingrese el id del agente al cual desea eliminar: ")
                                if (Is_int(errase)):
                                    errase = int(errase)
                                    if errase in id_agentes:
                                        cur5 = conn.cursor()
                                        cur5.execute('DELETE FROM agente WHERE id_agente = {} AND id_tennant = {};'.format(errase, tennant))
                                        conn.commit()
                                        cur5.close()
                                    else:
                                        print ('Este id agente no pertenece al Tennant {}'.format(tennant))
                                else:
                                    print('Ingrese números.')
                          elif agente == 4:  
                            o5 = False
                          #Salir de CrossNot
                          elif agente == 5:
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break      
                    
              elif mp == 6:
                  o6 = True 
                  while (o6):
                      id_tennants = []
                      for i in tennants:
                          id_tennants.append(i[0])
                      print (''' 
                                   --== Supervisores actuales del Tennant {} ==--
                                   '''.format(tennant))
                      query = 'SELECT * FROM supervisor WHERE id_tennant = {}'.format(tennant)
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close()
                      id_supervisores = []
                      print('ID |  nombre  |  apellido  |  ID tennant')
                      
                      i = 0
                      while i < len(a):
                          print(' {} | {} | {} | {}'.format(a[i][0],a[i][1], a[i][2], a[i][3]))
                          id_supervisores.append(a[i][0])
                          i+=1
                      supervisor = input('''
                         ---== Manejar supervisores  ==---
                         [1] Agregar supervisor
                         [2] Editar información
                         [3] Eliminar supervisor
                         [4] Volver Menu Opciones
                         [5] Salir de CrossNot
                            
                         Ingrese una opcion [1-5]:   ''')
                      if (Is_int(supervisor)):
                          supervisor = int(supervisor)        
                          if supervisor == 1:
                              nombre = input("Ingrese Nombre: ").upper()
                              apellido = input("Ingrese Apellido: ").upper()
                              cur5 = conn.cursor()
                              cur5.execute("INSERT INTO supervisor(nombre, apellido ,id_tennant) VALUES('{}','{}',{});".format(nombre,apellido,tennant))
                              conn.commit()
                              cur5.close()
                          elif supervisor == 2:
                                print('''
                                    ---== Editor de Supervisores ==---
                                    ''')
                                edit = input("Ingrese el id del supervisor al cual desea editar: ")
                                if (Is_int(edit)):
                                    edit = int(edit)
                                    if (edit in id_agentes):
                                        query = 'SELECT * FROM supervisor WHERE id_supervisor = {}'.format(edit)
                                        loc = conn.cursor()
                                        loc.execute(query)
                                        a = loc.fetchall()
                                        loc.close()
                                        id_agentes = []
                                        print('ID |  nombre  |  apellido  |  ID tennant')
                                      
                                        i = 0
                                        while i < len(a):
                                            print(' {} | {} | {} | {}'.format(a[i][0],a[i][1], a[i][2], a[i][3]))
                                            i+=1
                                    
                                        ed5 = input('''
                                            [1] Editar nombre
                                            [2] Editar apellido
                                            [3] Editar id tennant
                                            [4] Volver Menu Opciones
                                            [5] Salir de CrossNot
                                            
                                                
                                            Ingrese una opcion [1-5]:   ''')
                                        if (Is_int(ed5)):
                                            ed5 = int(ed5)
                                            #Editar id_campaña
                                            if ed5 == 1:
                                                nombre = input("Ingrese nuevo nombre:  ").upper()
                                                cur5 = conn.cursor()
                                                cur5.execute("UPDATE supervisor SET nombre = {} WHERE id_supervisor = {};".format(nombre, edit))
                                                conn.commit()
                                                cur5.close() 
                                                break
                                            elif ed5 == 2:
                                                apellido = input("Ingrese nuevo apellido:  ").upper()
                                                cur5 = conn.cursor()
                                                cur5.execute("UPDATE supervisor SET apellido = {} WHERE id_supervisor = {};".format(apellido, edit))
                                                conn.commit()
                                                cur5.close() 
                                                break
                                            elif ed5 == 3:
                                                  tennant1 = input("Ingrese id_tennant donde trabajará: ")
                                                  if (Is_int(tennant1)):
                                                      tennant1 = int(tennant1)
                                                      if tennant1 in id_tennants:
                                                            cur5 = conn.cursor()
                                                            cur5.execute("UPDATE supervisor SET id_tennant = {} WHERE id_supervisor = {};".format(tennant1, edit))
                                                            conn.commit()
                                                            cur5.close()
                                                      else:
                                                          print("El id Tennant ingresado no existe en nuestros registros...")
                                                  else:
                                                      print ("Error:   Ingrese un número")
                                            #Volver Menu Opciones
                                            elif ed5 == 4:
                                                break 
                                            #Salir de CrossNot
                                            elif ed5 == 5 :
                                                print()
                                                print("Gracias por utilizar CrossNot")
                                                menu = False
                                                login = False
                                                conn.close()  
                                                break 
                                            else:
                                                print("Ingrese opción válida.")
                                        else:
                                                print("Ingrese opción válida.")
                          elif supervisor == 3:
                                errase = input("Ingrese el id del supervisor al cual desea eliminar: ")
                                if (Is_int(errase)):
                                    errase = int(errase)
                                    if errase in id_supervisores:
                                        cur5 = conn.cursor()
                                        cur5.execute('DELETE FROM supervisor WHERE id_supervisor = {} AND id_tennant = {};'.format(errase, tennant))
                                        conn.commit()
                                        cur5.close()
                                    else:
                                        print ('Este id supervisor no pertenece al Tennant {}'.format(tennant))
                                else:
                                    print('Ingrese números.')
                          #Volver Menu Opciones
                          if supervisor == 4:  
                            o6 = False
                          #Salir de CrossNot
                          elif supervisor == 5:
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break 
                    
              elif mp == 7:
                  o7 = True 
                  while (o7):
                      tennant1 = input('''
                         ---== Manejar tennants   ==---
                         [1] Agregar tennant
                         [2] Editar información
                         [3] Eliminar tennant
                         [4] Volver Menu Opciones
                         [5] Salir de CrossNot
                            
                         Ingrese una opcion [1-5]:   ''')
                      if (Is_int(tennant1)):
                          tennant1 = int(tennant1)        
                          #Volver Menu Opciones
                          if tennant1 == 4:  
                            o7 = False
                          #Salir de CrossNot
                          elif tennant1 == 5:
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break      
              elif mp == 8:
                  print()
                  print("Gracias por utilizar CrossNot")
                  menu = False
                  login = False
                  conn.close()  
                  break 
              
                
  
        
    
    elif op == '2':
          login = False
          conn.close()  


      
conn.close()     
     

    