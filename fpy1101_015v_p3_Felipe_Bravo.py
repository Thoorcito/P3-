#librerias
import os 
os.system("cls")
import random
#lista
lista=[]

#funciones

def guardar () :
    while True:
        
        while True:
            try :
                Nombre=input ("ingrese nombre: ")
                
                if Nombre == '' or Nombre == " " or Nombre == "@" or Nombre =="*":
                    print("dato no valido intente nuevamente")
                else:
                    print ("dato ingresado correctamente") 
                    break                                   
            except:
                Nombre=0
                
        
        while True:                
            try:    
                Edad=int(input("ingrese edad debe ser igual o mayor que 0: "))
                 
                if Edad == '' or Edad == " " or Edad == "@" or Edad =="*":
                    print("dato no valido intente nuevamente")
                else:
                    print ("dato ingresado correctamente") 
                    break  
            except:
                Edad=-1
               
            
        while True :    
            try:    
                Nif=input("ingrese nif (debe tener 8 digitos,guion y 3 caracteres ej 99999999-RTX ): ")
            
                if Nif == '' or Nif == " " or Nif == "@" or Nif =="*":
                    print("dato no valido intente nuevamente")
                elif len (Nif)> 12 or len (Nif)<8:
                    print("dato no valido intente nuevamente")    
                else:
                    print ("dato ingresado correctamente") 
                    break  
            except:
                Nif=0
                   
        
        dic_datos = { 
            'nombre' : Nombre,'nif': Nif,'edad':Edad 
        }
        
        lista.append(dic_datos)
        break
    
    
def buscar () :
    print("buscar datos por nif")
    nif_buscado = input("ingrese nif buscado: ")
    for cosa in lista :
        if cosa ['nif'] == nif_buscado :
            print (cosa)
            return
        
        #no recordaba como buscar el caracter en la posicion 11 y 12 segun eso deberia discriminar si pertenece o no por eso dejo esta parte comentada :(
        #elif cosa ['nif'] == "sp" :
            #print ("pertenece a España") 
        #else:
            #print ("pertenece a europa")       
            
        
    print ("nif no encontrado intenta nuevamente :( ") 
    
def certificados ():
    nif_buscado = input("ingrese nif buscado: ")
    for cosa in lista :
        if cosa ['nif'] == nif_buscado :
            print (cosa)
            certificado = {'nacimiento' : random.randint (1500 , 5000),
                           'estado' :  random.randint (1500 , 5000),
                           'pertenece' : random.randint (1500 , 5000),
                
            }
            print (f"Certificado de nacimiento : {certificado['nacimiento']}")
            print (f"Certificado de estado conyugal : {certificado['estado']}")
            print (f"Certificado de pertenencia a la union europea : {certificado['pertenece']}")
            return    
    
    print ("nif no encontrado intenta nuevamente :( ")        
    
        
   

def salir ():
    print (" Programa Finalizado V1.0 Felipe Bravo")
    
#menu     
while True :
    
    print ("------------------------------")
    print ("Bienvenidooo ")
    print ('''
           1.-Grabar
           2.-Buscar
           3.-Imprimir certificado
           4.- Salir''')
    
    print ("------------------------------")
    try:
        op=int(input("ingrese opcion: "))
    except:
        op=0
    if op <1 or op >4 :
        print ("opcion no valida")
    else: 
        if op == 1:
            guardar ()
        elif op ==2 :
            buscar ()
        elif op == 3 :
         certificados () 
        else :
            salir () 
            break
                                   