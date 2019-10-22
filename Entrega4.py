# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:30:29 2019

@author: Ignacio Mayer
"""
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
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
    
#https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py  
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        rect.axes.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')    

#https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


#funcion sacada de la pagina https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html
#esta funcion me ayuda a saber si es una fecha correcta 
        
def main(i,f):
 # Establecer formato de las fechas a introducir: dd/mm/aaaa
 
 formato = "%Y-%m-%d"
 
 # Bucle 'sin fin' 
 
 while True:
  try:
   # Introducir fecha inicial utilizando el formato definido
   
   fecha_desde = i
   
   # Si no se introduce ningún valor se fuerza el final del bucle 
   
   if fecha_desde == "":
    break
   
   # Introducir fecha final utilizando el formato definido   
   
   fecha_hasta = f 

   # Si no se introduce ningún valor se fuerza el final del bucle 
   
   if fecha_hasta == "":
    break
   
   # Se evaluan las fechas según el formato dd/mm/aaaa
   # En caso de introducirse fechas incorrectas se capturará
   # la excepción o error
   
   fecha_desde = datetime.strptime(fecha_desde, formato)
   fecha_hasta = datetime.strptime(fecha_hasta, formato)
   
   # Se comprueba que fecha_hasta sea mayor o igual que fecha_desde
   
   if fecha_hasta >= fecha_desde:
    
    # Se cálcula diferencia en día y se muestra el resultado
    
    return True
    
   else:
    return ("La fecha fecha final debe ser mayor o igual que la inicial")
   
  except:
   return('Error en la/s fecha/s. ¡Inténtalo de nuevo!')

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
                  [8] Estadísticas
                  [9] Salir de CrossNot 
                  
                  Ingrese una opcion [1-8]:   ''')
          if (Is_int(mp)):
              mp = int(mp)
              if mp == 1:
                  o1 = True 
                  while (o1):
                      query = 'SELECT id_llamada FROM llamada;'
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close()
                      llamadas = []
                      i = 0
                      while i < len(a):
                          llamadas.append(a[i][0])
                          i+=1
                      
                      #mostrar todas las llamadas
                      query= "SELECT l.id_llamada, l.ubicacion_archivo, l.fecha, l.duracion, l.transcripcion, l.aprobacion, l.entrada_salida, l.rut_cliente, l.id_agente, l.id_supervisor FROM llamada l NATURAL JOIN agente a WHERE a.id_tennant = {} ORDER BY l.id_llamada;".format(tennant)
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close()
                      l_clasificadas = [] #id de llamadas ya clasificadas
                      print ()
                      print("Lista de llamadas")
                      print('id_llamada | ubicacion | fecha | duracion | transcripcion | aprovacion | entrada(0) salida(1) | rut_cliente | id_agente | id_supervisor')
                  
                      i = 0
                      while i < len(a):
                          print('   {}   |    {}   |    {}   |    {}   |    {}   |    {}   |    {}    |    {}   |    {}    |    {}   '.format(a[i][0],a[i][1], a[i][2],a[i][3],a[i][4], a[i][5],a[i][6],a[i][7], a[i][8],a[i][9]))
                          l_clasificadas.append(a[i][0])
                          i+=1

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
                          #Mostrar la llamada elegida        
                          if llamada == 1:
                              comprobar = True
                              while(comprobar):
                                  idllamada = input('Ingrese su Id de la llamada: ')
                                  if (Is_int(idllamada)):
                                      idllamada = int(idllamada)
                                      if idllamada in llamadas:
                                          query = 'SELECT l.id_llamada, l.ubicacion_archivo, l.fecha, l.duracion, l.transcripcion, l.aprobacion, l.entrada_salida, l.rut_cliente, l.id_agente, l.id_supervisor FROM llamada l ORDER BY l.id_llamada;'
                                          loc = conn.cursor()
                                          loc.execute(query)
                                          a = loc.fetchall()
                                          loc.close()
                                          print ()
                                          print("Lista de llamadas {}".format(llamada))
                                          print('id_llamada | ubicacion | fecha | duracion | transcripcion | aprovacion | entrada(0) salida(1) | rut_cliente | id_agente | id_supervisor')
                                      
                                          i = idllamada-1
                                          for i in a:
                                              if int(i[0]) == int(idllamada):
                                                comprobar = False
                                                print('     {}     |      {}     |      {}     |      {}     |      {}     |      {}     |      {}      |      {}     |      {}      |      {}     '.format(i[0],i[1], i[2],i[3],i[4], i[5],i[6],i[7], i[8],i[9]))
                                      else:    
                                          print('''
                                                ERROR: Este id de supervisor no pertenece a las llamada {}
                                          '''.format(tennant))
                          if llamada == 2:
                            cur2 = conn.cursor()
                            cur2.execute("SELECT id_agente FROM agente WHERE id_tennant = {}".format(tennant))
                            agentes2 = cur2.fetchall()
                            cur2 = conn.cursor()
                            cur2.execute("SELECT id_supervisor FROM supervisor WHERE id_tennant = {}".format(tennant))
                            supervisor2 = cur2.fetchall()
                            
                            cur2 = conn.cursor()
                            cur2.execute("SELECT rut FROM cliente")
                            clientes2 = cur2.fetchall()
                            cur2.close()
                            
                            id_agent  = []
                            id_super = []
                            id_clientes = []
                            
                            print ("Lista ID Agentes del tennant {} :".format(tennant))
                            for i in agentes2:
                              print(i[0])
                              id_agent.append(i[0])
                            print ("Lista Rut clientes:")
                            for j in clientes2:
                              print(j[0])
                              id_clientes.append(j[0])
                            for i in supervisor2:
                                id_super.append(i[0])
                                
                            i1 = input("ID Agente: ")
                            if (Is_int(i1)):
                                i1 = int(i1)
                                if i1 in id_agent:
                                    i2 = input("Rut Cliente: ")
                                    if (Is_int(i2)):
                                        if i2 in id_clientes:
                                            print("Debe ingresar la fecha de la forma 2019-11-26)")
                                            i3 = input("Fecha: ")
                                            if (validate(i3)):
                                                i3 = datetime.strptime(i3, '%Y-%m-%d')
                                                print("Debe ingresar duración en el formato hora:minutos:segudos")
                                                print("ejemplo: 01:23:08")
                                                i4 = input("Duracion: ")
                                                i5 = input("Ingrese (1) para aprobar (0): ")
                                                if (Is_int(i5)):
                                                    i5 = int(i5)
                                                    if i5 == 1 or i5 == 0:
                                                        i6 = input("Entrada[0]/Salida[1]: ")
                                                        if (Is_int(i6)):
                                                            i6 = int(i6)
                                                            if i6 == 1 or i6 == 0:
                                                                i7 = input("Ubicacion Archivo")
                                                                i8 = input("Transcripcion:")
                                                                i9 = input("ID Supervisor")
                                                                if (Is_int(i9)):
                                                                    i9 = int(i9)
                                                                    if i9 in id_super:
                                                                        cur2 = conn.cursor()
                                                                        cur2.execute("INSERT INTO llamada(ubicacion_archivo,fecha,duracion,transcripcion,aprobacion,entrada_salida,rut_cliente,id_agente,id_supervisor) VALUES('{}',{},'{}','{}',{},{},{},{},{});".format(i7, i3, i4, i8, i5, i6, i2, i1, i9))
                                                                        conn.commit()
                                                                        cur2.close()
                                                                    else:
                                                                        print("Este id supervisor no pertenece al tennant.")
                                                                else:
                                                                    print("Ingrese numeros válidos.")
                                                            else:
                                                                print("Ingrese 0 o 1 !!!")
                                                        else:
                                                                    print("Ingrese numeros válidos.")
                                                    else:
                                                                print("Ingrese 0 o 1 !!!")
                                                else:
                                                                    print("Ingrese numeros válidos.")
                                            else:
                                                                    print("Ingrese fecha válida.")
                                                                
                                        else:
                                            print ("Error: El id {} no pertence a ningun cliente registrado en Crossnot  {}.".format(i2,tennant))
                                else:
                                    print ("Error: El id {} no pertence a ningun agente del Tennant {}.".format(i1,tennant))
                            else:
                                print ("Error:  Los id de los agentes son de tipo numéricos!!!")


                          if llamada == 3:
                              l = input('Ingrese el id de la llamada para la cual quiere editar sus datos: ')
                              if Is_int(l):
                                id1 = int(l)
                                cat7 = input('''
                                  ---== Que campo desea modificar  ==---
                                  [1] Ubicacion de archivo
                                  [2] Fecha
                                  [3] Duracion
                                  [4] Transcripcion
                                  [5] Aprobacion
                                  [6] Entrada/Salida
                                  [7] Rut cliente
                                  [8] ID agente
                                  [9] ID supervisor
                                      
                                  Ingrese una opcion [1-9]:   ''')
                                cur1 = conn.cursor()
                                if cat7 == '1':
                                  x = input("Nueva ubicacion de archivo: ")
                                  cur1.execute("UPDATE supervisor s SET ubicacion_archivo = '{}' WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '2':
                                  x = input("Nueva fecha: ")
                                  cur1.execute("UPDATE supervisor SET fecha = '{}' WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '3':
                                  x = input("Nueva duracion: ")
                                  cur1.execute("UPDATE supervisor s SET duracion = '{}' WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '4':
                                  x = input("Nueva transcripcion: ")
                                  cur1.execute("UPDATE supervisor SET transcripcion = '{}' WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '5':
                                  x = input("Nuevo aprobacion[Si/No]: ")
                                  if(Is_int(x)):
                                      x = int(x)
                                      cur1.execute("UPDATE supervisor s SET aprobacion = {} WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '6':
                                  x = input("Si es Entrada[0] o Salida[1]: ")
                                  if(Is_int(x)):
                                      x = int(x)
                                      cur1.execute("UPDATE supervisor SET entrada_salida = {} WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '7':
                                  x = input("Nuevo rut cliente: ")
                                  if(Is_int(x)):
                                      x = int(x)
                                      cur1.execute("UPDATE supervisor s SET rut_cliente = {} WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '8':
                                  x = input("Nuevo ID agente: ")
                                  if(Is_int(x)):
                                      x = int(x)
                                      cur1.execute("UPDATE supervisor SET id_agente = {} WHERE id_llamada = {};".format(x, id1))
                                if cat7 == '9':
                                  x = input("Nuevo ID del supervisor: ")
                                  if(Is_int(x)):
                                      x = int(x)
                                      cur1.execute("UPDATE supervisor SET id_supervisor = {} WHERE id_llamada = {};".format(x, id1))
                                conn.commit()
                                cur1.close()

                          if llamada == 4:
                            l1 = input("Indique ID de llamada que quere eliminar: ")
                            if(Is_int(l1)):
                                    l1 = int(l1)
                                    cur7 = conn.cursor()
                                    cur7.execute("SELECT * FROM llamada WHERE id_llamada = {}".format(l1))
                                    ten7 = cur7.fetchall()
                                    print("Estas seguro que quieres eliminar la siguiente llamada?\n", ten7[0], )
                                    sure = input("[1: Si]\n[2: No]\n---> ")
                                    if sure == '1':
                                      cur7.execute("DELETE FROM llamada WHERE id_llamada = {};".format(ten7[0][0]))
                                      conn.commit()
                                    cur7.close()
                              
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
                                  o=True
                                  while (o):
                                      fecha_desde = input('Introducir fecha inicial (aaaa-mm-dd): ')
                                      fecha_hasta = input('Introducir fecha final   (aaaa-mm-dd): ') 
                                        
                                      fechas = main(fecha_desde,fecha_hasta)
                                      if (fechas):
                                            cur5 = conn.cursor()
                                            cur5.execute("INSERT INTO campagna(inicio,fin,id_tennant) VALUES('{}','{}',{});".format(fecha_desde,fecha_hasta,tennant))
                                            conn.commit()
                                            cur5.close()
                                            o=False 
                                            intresar = False
                                            o3 = False
                                            break
                                      else: 
                                          print(fechas)
                                      
                                        
                              #eliminar campaña
                              if campagna == 2:
                                  ingresar = True 
                                  while (ingresar):
                                      c1 = input("Ingrese id_campaña que quiere editar o eliminar:  ")
                                      if (Is_int(c1)):
                                          c1 = int(c1)
                                          if c1 in campagnas[0]:
                                              o = True
                                              while (o):
                                                  eliminar1 = input('''Esta seguro que desea eliminar la calificacion?
                                                                   
                                                                      si (1)                       no (2)          
                                                  ''')
                                                  if (eliminar1 == '1'):
                                                        cur5 = conn.cursor()
                                                        cur5.execute("DELETE FROM campagna WHERE id_campagna = {};".format(c1))
                                                        conn.commit()
                                                        cur5.close()
                                                        break
                                                        o = False
                                                        intresar = False
                                                        o3 = False
                                                        break
                                                  elif (eliminar1 == '2'):
                                                      break 
                                                  else:
                                                      print ('Ingrese una opcion válida.')
                                                      o=False 
                                          else: 
                                                 print('Ingrese una Campaña del Tennant {}'.format(tennant))
                                      else: 
                                          print('Ingrese un numero valido')
                                         
                               
                              #editar campaña
                              elif campagna == 3:
                                  ingresar = True 
                                  while (ingresar):
                                      c1 = input("Ingrese id_campaña que quiere editar:  ")
                                      if (Is_int(c1)):
                                          c1 = int(c1)
                                          if c1 in campagnas[0]:
                                              o = True
                                              while (o):
                                                  fecha_desde = input('Introducir fecha inicial (aaaa-mm-dd): ')
                                                  fecha_hasta = input('Introducir fecha final   (aaaa-mm-dd): ') 
                                                    
                                                  fechas = main(fecha_desde,fecha_hasta)
                                                  if (fechas):
                                                       cur5 = conn.cursor()
                                                       cur5.execute("UPDATE campagna SET inicio = '{}' WHERE id_campagna = {};".format(fecha_desde,c1))
                                                       conn.commit()
                                                       cur5.close()
                                                       
                                                       cur = conn.cursor()
                                                       cur.execute("UPDATE campagna SET fin = '{}' WHERE id_campagna = {};".format(fecha_hasta,c1))
                                                       conn.commit()
                                                       cur.close()
                                                      
                                                       o = False
                                                       ingresar = False
                                                       break
                                                  else:
                                                       print(fechas)
                                                
                                          else: 
                                                 print('Ingrese una Campaña del Tennant {}'.format(tennant))
                                      else: 
                                          print('Ingrese un numero valido')
                                                  
                                          
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
                      else: 
                          print('Ingrese numero valido')
                                
                
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
                      
                  ids_campagnas=[]
                  q = 0
                  while q < len(a):
                      ids_campagnas.append((a[q][0]))
                      q+=1
               
                  o4 = True 
                  while (o4):
                       select_campagna = input('Seleccione Id_Campaña:    ')
                       if (Is_int(select_campagna)):
                          select_campagna = int(select_campagna) 
                          if select_campagna in ids_campagnas:
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
                                                 
                                                  edit_aso = True 
                                                  while (edit_aso):
                                                      
                                                      elegir_tipi = input('Ingrese id_tipificacion que desea editar:   ')
                                                      if (Is_int(elegir_tipi)):
                                                          elegir_tipi = int(elegir_tipi)
                                                          if elegir_tipi in id_tipi_campa:
                                                              query1 = '''SELECT l.id_llamada, t.id 
                                                                        FROM llamada l LEFT JOIN tipificacion_dato d ON l.id_llamada = d.id_llamada JOIN agente a on a.id_agente = l.id_agente JOIN tennant t on a.id_tennant=t.id
                                                                        where d.id_llamada IS NULL AND t.id={} '''.format(tennant)
                                                              loc2 = conn.cursor()
                                                              loc2.execute(query1)
                                                              a2 = loc2.fetchall()
                                                              loc2.close()
                                                              llamadas_tennant = []
                                                              print ()
                                                              print("Lista de Llamadas sin Campañas del Tennant {} en CrossNot".format(tennant))
                                                              print()
                                                              print ('Id_llamada')
                
                                                              g = 0
                                                              while g < len(a2):
                                                                  print('{}'.format(a2[g][0]))
                                                                  llamadas_tennant.append(a2[g][0])
                                                                  g+=1 
                  
                                                              sel = True
                                                              while (sel): 
                                                                  
                                                                  select_llamada = input('Ingrese id_llamada que quiere editar:   ')
                                                                  if (Is_int(select_llamada)):
                                                                      select_llamada = int(select_llamada)
                                                                      
                                                                      if select_llamada in llamadas_tennant:
                                                                          query1 = '''select dato 
                                                                                    from tipificacion 
                                                                                    where id_tipificacion = {}'''.format(elegir_tipi)
                                                                          loc2 = conn.cursor()
                                                                          loc2.execute(query1)
                                                                          a2 = loc2.fetchall()
                                                                          loc2.close()
                                                                          datoo = []
                                                                
                                                                          g = 0
                                                                          while g < len(a2):
                                                                              datoo.append(a2[g][0])
                                                                              g+=1 
                                                                              
                                                                        
                                                                          val = input('Ingrese valor de la tipificacion ({}) que desea agregar:   '.format(datoo[0]))
                                                                          
                                                                          cur2= conn.cursor()
                                                                          cur2.execute("INSERT INTO tipificacion_dato(id_llamada,id_tipificacion,valor) VALUES({},{},'{}');".format(select_campagna,elegir_tipi,val))
                                                                          conn.commit()
                                                                          cur2.close()
                                                                          
                                                                          cur5 = conn.cursor()
                                                                          cur5.execute("UPDATE llamada SET entrada_salida = 1 WHERE id_llamada = {};".format(select_llamada))
                                                                          conn.commit()
                                                                          cur5.close()
                                                                          
                                                                          query1 = '''select inicio
                                                                                    from campagna
                                                                                    where id_campagna = {}'''.format(select_campagna)
                                                                          loc2 = conn.cursor()
                                                                          loc2.execute(query1)
                                                                          a2 = loc2.fetchall()
                                                                          loc2.close()
                                                                          fechai = []
                                                                
                                                                          g = 0
                                                                          while g < len(a2):
                                                                              fechai.append(a2[g][0])
                                                                              g+=1 
                                                                         
                                                                          cur = conn.cursor()
                                                                          cur.execute("UPDATE llamada SET fecha = '{}' WHERE id_llamada = {};".format(fechai[0],select_llamada))
                                                                          conn.commit()
                                                                          cur.close()
                                                                          
                                                                          sel =False 
                                                                          edit_aso=False
                                                                          ct = False
                                                                          o4 = False
                                                                          conn.close()
                                                                          break 
         
                                                                          
                                                                      else: 
                                                                        print('Ingrese llamada sin asociacion')
                                                                  else:
                                                                      print('Ingrese numero valido')
                                                          else: 
                                                              print('Ingrese una tipificacion de la campaña {}'.format(select_campagna))
                                                      else: 
                                                          print('Ingrese numero valido')
                                                          
                                                  
                                                      
                                                      
                                                     
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
                                                     
                                          elif tip == 4:
                                              edit_aso = True 
                                              while (edit_aso):
                                                  elegir_tipi = input('Ingrese id_tipificacion que desea editar:   ')
                                                  if (Is_int(elegir_tipi)):
                                                      elegir_tipi = int(elegir_tipi)
                                                      if elegir_tipi in id_tipi_campa:
                                                          o = True 
                                                          while (o): 
                                                              edit_valor = input("Ingrese nuevo dato de la tipificacion {}:   ".format(elegir_tipi))
                                                              if (Is_str(edit_valor)):
                                                                  edit_valor=str(edit_valor)
                                                                  
                                                                  cur5 = conn.cursor()
                                                                  cur5.execute("UPDATE tipificacion SET dato = '{}' WHERE id_tipificacion = {};".format(edit_valor,elegir_tipi))
                                                                  conn.commit()
                                                                  cur5.close()
                                                              
                                                                  query1 = '''SELECT d.id_tipificaciondato, d.valor, t.dato 
                                                                            FROM tipificacion_dato d JOIN  tipificacion t on t.id_tipificacion = d.id_tipificacion
                                                                            WHERE d.id_tipificacion = {}
                                                                            order by id_tipificaciondato'''.format(elegir_tipi)
                                                                  loc2 = conn.cursor()
                                                                  loc2.execute(query1)
                                                                  a2 = loc2.fetchall()
                                                                  loc2.close()
                                                                  datos_camp_tipi = []
                                
                                                                  print ("Tabla valores a editar")
                                                                  print ('Id_tipificaciondato   |   Valor')
                                                                  
                                                                  i = 0
                                                                  while i < len(a2):
                                                                      b = []
                                                                      b.append(a2[i][0])
                                                                      b.append(a2[i][1])
                                                                      b.append(a2[i][2])
                                                                      print ('{}    |   {}'.format(a2[i][0],a2[i][2]))
                                                                      datos_camp_tipi.append(b)
                                                                      i+=1  
                                                                      
                                                                  id_dato_camp =[]
                                                                  g = 0
                                                                  while g < len(a2):
                                                                      id_dato_camp.append(a2[g][0])
                                                                      g+=1 
                                                                      
                                                                  j=0
                                                                  for i in id_dato_camp:
                                                                      val = datos_camp_tipi[1][2]
                                                                      valor = input("Ingrese nuevo valor de {} para la tipificacion_dato {}:   ".format(val,i))
                                                                      cur5 = conn.cursor()
                                                                      cur5.execute("UPDATE tipificacion_dato SET valor = '{}' WHERE id_tipificaciondato = {};".format(valor,i))
                                                                      conn.commit()
                                                                      cur5.close()

                                                                      if j == len(id_dato_camp)-1:
                                                                            
                                                                            o= False
                                                                            edit_aso=False
                                                                            ct = False
                                                                            o4 = False 
                                                                            break
                                                                      j+=1
                                                                      
                                                              else:
                                                                 print('Ingrese un numero porfavor') 
                                                      else: 
                                                          print('Ingrese una tipificacion de la campaña {}'.format(select_campagna))
                                                  else: 
                                                      print('Ingrese un numero porfavor')
                                              
                                          elif tip == 5:
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
                                            ct = False
                                            o4 = False
                                          #Salir de CrossNot
                                          elif tip == 7:
                                            print()
                                            print("Gracias por utilizar CrossNot")
                                            ct = False
                                            o4 = False
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
                      query= 'SELECT * FROM tennant'
                      loc = conn.cursor()
                      loc.execute(query)
                      a = loc.fetchall()
                      loc.close() 
                      info_tennant = []
                      print('ID |  telefono')
                      
                      i = 0
                      while i < len(a):
                          b=[]
                          b.append(a[i][0])
                          b.append(a[i][1])
                          print(' {} | {} '.format(a[i][0],a[i][1]))
                          info_tennant.append(b)
                          i+=1
                      
                      tens = []
                      r = 0
                      while r < len(a):
                          tens.append(a[r][0])
                          r+=1
                          
                      cant_tele = []
                      r = 0
                      while r < len(a):
                          cant_tele.append(a[r][1])
                          r+=1
                      
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
                        if 0<tennant1<6: 
                            # Agrega tennant
                            if tennant1 == 1:
                                tel = input("Indique el número de telefono: ")
                                cur7 = conn.cursor()
                                cur7.execute("INSERT INTO tennant(telefono) VALUES({});".format(tel))
                                conn.commit()
                                cur7.close()
                                agr = False 
                                break 
                                        
                            # Modifica tennant
                           
                            elif tennant1 == 2:
                                 mod = True
                                 while (mod):
                                    tenn = input("Indique ID del tennant: ")
                                    if (Is_int(tenn)):
                                      tenn = int(tenn)
                                      
                                      if tenn in tens:
                                            query1 = "SELECT s.id_supervisor, s.nombre, s.apellido FROM supervisor s JOIN tennant t on t.id = s.id_tennant where t.id={}".format(tenn)
                                            loc = conn.cursor()
                                            loc.execute(query1)
                                            a = loc.fetchall()
                                            loc.close() 
                                            info_super= []
                                            print('ID supervisor |  nombre   | apellido  ')
                                              
                                            i = 0
                                            while i < len(a):
                                                  b=[]
                                                  b.append(a[i][0])
                                                  b.append(a[i][1])
                                                  print(' {} | {} | {} '.format(a[i][0],a[i][1],a[i][2]))
                                                  info_tennant.append(b)
                                                  i+=1
                                                  
                                            cant_super = []
                                            r = 0
                                            while r < len(a):
                                                  cant_super.append(a[r][0])
                                                  r+=1
                                            
                                            corr = True 
                                            while (corr):
                                                id7 = input("Indique el ID del supervisor que quiere modificar: ")
                                                if (Is_int(id7)):
                                                    id7 = int(id7)
                                                    if id7 in cant_super:
                                                        o = True
                                                        while (o):
                                                            cat7 = int(input('''
                                                              ---== Que campo desea modificar  ==---
                                                              [1] Nombre
                                                              [2] Apellido
                                                                  
                                                              Ingrese una opcion [1-2]:   '''))
                                                            cur7 = conn.cursor()
                                                            if cat7 == 1:
                                                              name7 = input("Nuevo nombre: ")
                                                              cur7.execute("UPDATE supervisor s SET nombre = '{}' WHERE id_supervisor = '{}';".format(name7, id7))
                                                            elif cat7 == 2:
                                                              name7 = input("Nuevo apellido: ")
                                                              cur7.execute("UPDATE supervisor SET apellido = '{}' WHERE id_supervisor = '{}';".format(name7, id7))
                                                            else:
                                                                print ('Ingrese opcion valida')
                                                                
                                                            conn.commit()
                                                            cur7.close()
                                                            o = False 
                                                            corr = False
                                                            mod = False 
                                                            o7 = False
                                                    else:
                                                         print('Ingrese supervisor que sea del tennant {}'.format(tenn))
                                                else:
                                                      print('Ingrese numero valido')
                                                        
                                      else:
                                          print('Ingrese tennant de la lista')
                                    else:
                                       print('Ingrese numero valido')
                    
                            # Elimina tennant
                            
                            elif tennant1 == 3:
                                eliminar = True 
                                while (eliminar):
                                    tenn = int(input("Indique ID del tennant que quere eliminar: "))
                                    if (Is_int(tenn)):
                                        if tenn in tens:
                                            print("Estas seguro que quieres eliminar el tennant {}".format(tenn))
                                            sure = input("[1: Si]\n[2: No]\n---> ")
                                            
                                            if sure == '1':
                                              cur7 = conn.cursor()
                                              cur7.execute("DELETE FROM tennant WHERE id = {};".format(tenn))
                                              conn.commit()
                                              cur7.close()
                                              eliminar = False
                                              o7= False
                                              
                                            else: 
                                                print('Opcion invalida')
                                        else: 
                                            print('Ingrese tennant de la lista')
                                    else:
                                        print('Ingrese numero valido' )
                                                
                            # Volver Menu Opciones
                            elif tennant1 == 4:  
                                o7 = False
                              #Salir de CrossNot
                            elif tennant1 == 5:
                                print()
                                print("Gracias por utilizar CrossNot")
                                eliminar = False
                                menu = False
                                login = False
                                conn.close()  
                                break 
                                
                        else: 
                              print('Ingrese opcion valido')  
                      else:
                          print('Ingrese numero valido')
               
                
                
              elif mp == 8:
                  t = True 
                  while (t):
                      e = input('''
                         ---== Estadísticas ==---
                         [1] Llamadas por tennant
                         [2] Evaluaciones por tennant
                         [3] Agentes
                         [4] Supervisores
                         [5] Volver Menu Opciones
                         [6] Salir de CrossNot
                            
                         Ingrese una opcion [1-6]:   ''')
                      
                      
                      if e == '1':
                            cur2 = conn.cursor()
                            cur2.execute("SELECT a.id_tennant, COUNT(*) FROM agente a NATURAL JOIN llamada l WHERE l.entrada_salida = 0 GROUP BY a.id_tennant ORDER BY a.id_tennant;")
                            l_entrada = cur2.fetchall()
                            cur2.execute("SELECT a.id_tennant, COUNT(*) FROM agente a NATURAL JOIN llamada l WHERE l.entrada_salida = 1 GROUP BY a.id_tennant ORDER BY a.id_tennant;")
                            l_salida = cur2.fetchall()
                            cur2.close()
                           
                            tennants = []
                            quantity_s = []
                            quantity_e = []
                            for i in l_salida:
                                tennants.append(i[0])
                            for i in l_salida:
                                quantity_s.append(i[1])
                            for i in l_entrada:
                                quantity_e.append(i[1])
                            # Esto lo saqué de    https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py 
                            x = np.arange(len(tennants))  # the label locations
                            width = 0.35  # the width of the bars
                            
                            fig, ax = plt.subplots()
                            rects1 = ax.bar(x - width/2, quantity_s, width, label='Entrantes')
                            rects2 = ax.bar(x + width/2, quantity_e, width, label='Salientes')
                            
                            # Add some text for labels, title and custom x-axis tick labels, etc.
                            ax.set_ylabel('Cantidad de llamadas')
                            ax.set_title('ID del Tennant')
                            ax.set_xticks(x)
                            ax.set_xticklabels(tennants)
                            ax.legend()
                            autolabel(rects1)
                            autolabel(rects2)
                            
                            fig.tight_layout()
                            
                            plt.show()
                      
                      elif e == '2':
                            cur2 = conn.cursor()
                            cur2.execute("SELECT a.id_tennant, COUNT(*) FROM agente a NATURAL JOIN llamada l WHERE l.aprobacion = 1 GROUP BY a.id_tennant ORDER BY a.id_tennant;")
                            l_aprobadas = cur2.fetchall()
                            cur2.execute("SELECT a.id_tennant, COUNT(*) FROM agente a NATURAL JOIN llamada l WHERE l.aprobacion = 0 GROUP BY a.id_tennant ORDER BY a.id_tennant;")
                            l_desaprobadas = cur2.fetchall()
                            cur2.close()
                            tennants = []
                            quantity_a = []
                            quantity_d = []
                            for i in l_aprobadas:
                                tennants.append(i[0])
                            for i in l_aprobadas:
                                quantity_a.append(i[1])
                            for i in l_desaprobadas:
                                quantity_d.append(i[1])
                            # Esto lo saqué de    https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py 
                            x = np.arange(len(tennants))  # the label locations
                            width = 0.35  # the width of the bars
                            
                            fig, ax = plt.subplots()
                            rects1 = ax.bar(x - width/2, quantity_a, width, label='Aprobadas')
                            rects2 = ax.bar(x + width/2, quantity_d, width, label='Desaprobadas')
                            
                            # Add some text for labels, title and custom x-axis tick labels, etc.
                            ax.set_ylabel('Cantidad de llamadas')
                            ax.set_title('ID del Tennant')
                            ax.set_xticks(x)
                            ax.set_xticklabels(tennants)
                            ax.legend()
                            autolabel(rects1)
                            autolabel(rects2)
                            
                            fig.tight_layout()
                            
                            plt.show()  
                      elif e == '5':  
                            t = False
                          #Salir de CrossNot
                      elif e == '6':
                            print()
                            print("Gracias por utilizar CrossNot")
                            menu = False
                            login = False
                            conn.close()  
                            break 
                      
              elif mp == 9:
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
     

    