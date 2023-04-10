from paquete_entrega.modulo_clientes import * #importo todo del módulo clientes

print(" *** Bienvenido al sistema de clientes *** ")
opcion = ""
while opcion != "3":
    opcion = input("Ingrese una opción:\n1. Crear un nuevo cliente\n2. Mostrar información de un cliente\n3. Salir\n")
    if opcion == "1": #Para crear nuevos usaurios
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            email = input("Ingrese el email del cliente: ")
            clave = input("Ingrese una clave: ")

            cliente = Cliente(nombre, apellido, email, clave)
            print(f"Los datos que usted ingresó son los siguientes:", "\n", cliente) #Muestro los datos seteados con el método str
            correcto = input("Ingrese SI/NO para guardarlos: ") 
            if correcto == "SI": #Si el usuario confirma los datos, se guardarán en la base
                b_datos = open("base_datos.txt", "a") #Guardo los datos la base de datos en txt
                b_datos.write(f"{cliente.nombre}, {cliente.apellido}, {cliente.email}, {cliente.clave}""\n")
                b_datos.close()
                
                print(f"Gracias por registrarte ", cliente.nombre_completo()) #Llamo el método que une nombre y apellido. 
                print("Recuerde que para ingresar al sitio, deberá ingresar con su email y clave: ")
                print(cliente.info_usario()) # con este método muestro cuál será su usuario y clave para ingresar
            
            else:
                print("No se guardaran los datos. ")
        
    elif opcion == "2": #Muestro los datos en la base de datos
        b_datos = open("base_datos.txt", "r")
        contenido = b_datos.read()
        print("Estos son los usuarios y claves de nuestra base de datos" + "\n" + contenido)
        b_datos.close()

    elif opcion == "3":
         print("*** EL PROGRAMA FINALIZO.")
