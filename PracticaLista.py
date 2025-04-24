#Nombre, apellido, correo y edad.

usuarios =[]
continuar = True


print("---"*30)
print("BASE DE DATOS ")
print("---"*30)



while continuar:
    nombre = input("Ingresa por favor el nombre")

    apellido = input("Ingrese por favor el apellido: ")

    correo= input("ingrese por favor el correo: ")
    

    edad = input("ingrese la edad: ")

    usuarios.append([nombre,apellido,edad,correo])

    valor = input("deseas seguir creando usuarios: (si/no)")
    if (valor == "no"):
        continuar = False

continuar2 = True
while continuar2:
    print("---"*30)
    opcion =int(input( "Que desea hacer \n " \
    "1) Listar usuarios \n "
    "2) Editar usuarios \n "
    "3) crear nuevo usuario \n "
    "4) Eliminar usuario \n ")) 

    if opcion==3:
        nombre = input("Ingresa por favor el nombre")

        apellido = input("Ingrese por favor el apellido: ")

        correo= input("ingrese por favor el correo: ")
    

        edad = input("ingrese la edad: ")

        usuarios.append([nombre,apellido,edad,correo])

        devolver = int(input("1) para volver al menu principal \n2) para terminar "))

        if devolver == 2:
            continuar2 = False

    elif  opcion==1:
        contador = 0
        for cont in usuarios:
            print ("(",contador,")",cont[0], cont[1], cont[2], cont[3])
            contador = contador + 1

        devolver = int(input("1) para volver al menu principal \n 2) para terminar "))
        
        if devolver == 2:
            continuar2 = False

    elif opcion == 2:
        contador = 0
        for cont in usuarios:
            print ("(",contador,")",cont[0], cont[1], cont[2], cont[3])
            contador = contador + 1
        
        editar = int(input("que usuario desea editar? , indiquelo con los numeros del indice que aparece al principio \n" \
        "del usuario"))
        print("")
        print(usuarios[editar])
        print("")
        editar_pos = int(input("indique que posicion de la lista desea editar, teniendo en cuenta que \n" \
        "nombre = 0 \n" \
        "apellido = 1 \n" \
        "edad = 2 \n" \
        "correo = 3 \n "))
        print("")
        print(usuarios[editar][editar_pos])
        print("")
        del usuarios[editar][editar_pos]
        usuarios[editar][editar_pos] = input(" ingrese por lo que lo quiere reemplazar: ")
        print("asi quedó el usuario: \n \n" \
        , usuarios[editar] )
        print("")
        devolver = int(input("1) para volver al menu principal \n2) para terminar "))

        if devolver == 2:
            continuar2 = False

    elif opcion == 4:
        contador = 0
        for cont in usuarios:
            print ("(",contador,")",cont[0], cont[1], cont[2], cont[3])
            contador = contador + 1
        pa_eliminar = int(input("que usuario desea eliminar teniendo en cuenta el numero que aparece al principio del usuario: "))
        del usuarios[pa_eliminar]
        print("")
        print("usuario correctamente eliminado")
        print("")
        contador = 0
        for cont in usuarios:
            print ("(",contador,")",cont[0], cont[1], cont[2], cont[3])
            contador = contador + 1
        print("")
        devolver = int(input("1) para volver al menu principal \n2) para terminar "))

        if devolver == 2:
            continuar2 = False

        
    



   



        



    
    


    

   
        




   





