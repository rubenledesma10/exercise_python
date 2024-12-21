import datetime as dt
def validarPersona():
    cuenta = {
    "saldo": 0,
    "listaMovimientos": [],
    "personasAutorizadas": {"Ruben": "1234", "Lucas": "abcd", "Pablo": "9876"}
}
 #creo un diccionario que tenga como clave unica (saldo inicializado en 0), listaMovimientos que tenga una lista vacia para guardar las transacciones, personasAutorizadas que tenga las personas autorizadas para operar en la cuenta
    validarIdentidad(cuenta)

def validarIdentidad(cuenta):  #esta funcion es para evaluar si la persona esta autorizada, si lo esta accede al menu principal, si no, el programa termina
    nombreValidacion = input("Ingrese su nombre: ").title()
    if nombreValidacion not in cuenta["personasAutorizadas"]:
        print("Usted no está autorizado a operar sobre la cuenta!")
    else:
        contrasena = input("Ingrese su contraseña: ")
        if cuenta["personasAutorizadas"][nombreValidacion] == contrasena:
            print(f"Bienvenido nuevamente {nombreValidacion}.")
            menuPrincipal(cuenta)
        else:
            print("Contraseña incorrecta. Acceso denegado.")


def menuPrincipal(cuenta):
    
    while True:
        print("--- MENÚ PRINCIPAL ---")
        print("¿Qué operación desea realizar hoy?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Movimientos realizados")
        print("4. Ver Saldo")
        print("5. Menú Personas Autorizadas en mi cuenta")
        print("6. Salir")
        try:
            opcion=int(input("Ingrese lo que usted desee hacer: "))
            if opcion==1:
                depositar(cuenta)
            elif opcion==2:
                retirar(cuenta)
            elif opcion==3:
                movimientos(cuenta)
            elif opcion==4:
                verSaldo(cuenta)
            elif opcion==5:
                menuPersonas(cuenta)
            elif opcion==6:
                salir = validarSalida()
                if salir == True:
                    print("Gracias, vuelva pronto.")
                    break
            else:
                print("Opción incorrecta, intente nuevamente...")
                input("Presione ENTER para CONTINUAR....")
        except ValueError:
            print("Por favor, ingrese un numero... ")
            input("Presione ENTER para CONTINUAR....")
        
def depositar(cuenta):
    while True:
        try:
            deposito = int(input("¿Cuanto va a depositar? Si usted desea salir de esta sección aprieta cualquier caracter que no sea un número "))
            if deposito>0: 
                cuenta["saldo"] = cuenta["saldo"] + deposito
                cuenta["listaMovimientos"].append({"Operación":"Déposito","Importe":deposito, "Fecha":fecha(),"Hora":hora()}) #agrego a la lista de movimientos el tipo de operacion que se hizo, importe fecha y hora
                print(f"Depósito realizado correctamente. Su saldo actual es de {cuenta['saldo']}")
                input("Presione ENTER para CONTINUAR....")
                break
            else:
                print(f"El deposito tiene que ser mayor a 1 (inclusive), usted no puede depositar {deposito} pesos")
                input("Presione ENTER para CONTINUAR....")
        except ValueError:
            volverAtras()
            break

def retirar(cuenta):
    while True:
        try:
            retiro = int(input("¿Cuanto va a retirar? Si usted desea salir de esta sección aprieta cualquier caracter que no sea un número "))
            if retiro < 1:
                print(f"No puede retirar ${retiro}. El monto a retirar tiene que ser igual o mayor a 1")
            else:
                if retiro <= cuenta["saldo"]:  #agrego a la lista de movimientos el tipo de operacion que se hizo, importe fecha y hora
                    cuenta["saldo"]= cuenta["saldo"] - retiro
                    cuenta["listaMovimientos"].append({"Operación":"Retiro","Importe":retiro, "Fecha":fecha(),"Hora":hora()})
                    print(f"Retiro realizado correctamente. Su saldo actual es de {cuenta['saldo']}")
                    input("Presione ENTER para CONTINUAR....")
                    break
                else:
                    print(f"Usted quiere retirar más dinero de lo que tiene en su cuenta, su saldo actual es de {cuenta['saldo']} y usted quiere retirar {retiro}")
                    input("Presione ENTER para CONTINUAR....")
        except ValueError:
            volverAtras()
            break

def movimientos(cuenta): #mostrar los movimientos que se hicieron
    acumulador=1 #lo uso para mostrar en orden numerico el orden de las operaciones que se hicieron
    if not cuenta["listaMovimientos"]:
        print(f"No hay movimientos realizados")
    else:
        for movimientos in cuenta["listaMovimientos"]:
            print(f"{acumulador}. Operación: {movimientos['Operación']}     Importe: {movimientos['Importe']}     Fecha: {movimientos['Fecha']}     Hora: {movimientos['Hora']}")
            acumulador=acumulador+1
        print(f"Saldo al día de hoy {fecha()} es de ${cuenta['saldo']}")
    volverAtras()

def verSaldo(cuenta):
    print(f"Su saldo actual es de {cuenta['saldo']}")
    input("Presione ENTER para CONTINUAR....")

def validarSalida():
    
    while True:
        salida=input("Desea salir? Ingrese S en caso de que SI, y una N en caso de que NO ").upper()
        if salida=="S":
            return True
        elif salida=="N":
            volverAtras()
            break
        else:
            print("Opción incorrecta, ingrese S por SI o N por NO")  

def menuPersonas(cuenta):
    while True:
        print("Que desea hacer con las personas autorizadas? ")
        print("1. Agregar Personas nueva ")
        print("2. Modificar nombre de una persona")
        print("3. Eliminar persona autorizada")  
        print("4. Ver Personas autorizadas")
        print("5. Volver al menu principal ")
        try:
            opcionPersonas=int(input("Elija una opción: "))
            if opcionPersonas==1:
                agregarPersona(cuenta)  
            elif opcionPersonas==2:
                modificarPersona(cuenta)  
            elif opcionPersonas==3:
                eliminarPersona(cuenta)
            elif opcionPersonas==4:
                verPersonas(cuenta)
            elif opcionPersonas==5:
                salir = validarSalida()
                if salir == True:
                    break
            else:
                print("Opción incorrecta, vuelva a ingresar una opción, pero que esta vez sea correcta por favor")
                input("Presione ENTER para CONTINUAR....")
        except ValueError:
            print("No se permiten digitos, tiene que ser un caracter...")
            input("Presione ENTER para CONTINUAR....")

def agregarPersona(cuenta):
    nombre = input("Ingrese el nombre de la persona autorizada: ").title()
    contrasena = input("Ingrese una contraseña para esta persona: ")
    cuenta["personasAutorizadas"][nombre] = contrasena
    print(f"El nombre {nombre} ha sido agregado exitosamente.")
    volverAtras()


def modificarPersona(cuenta):
    nombreAModificar = input("Ingrese el nombre de la persona a modificar: ").title()
    if nombreAModificar not in cuenta["personasAutorizadas"]:
        print(f"{nombreAModificar} no está en la lista.")
    else:
        nuevoNombre = input("Ingrese el nuevo nombre: ").title()
        nuevaContrasena = input("Ingrese la nueva contraseña: ")
        cuenta["personasAutorizadas"][nuevoNombre] = nuevaContrasena
        if nuevoNombre != nombreAModificar:
            del cuenta["personasAutorizadas"][nombreAModificar]
        print(f"{nombreAModificar} ha sido actualizado correctamente.")
        volverAtras()

        
def eliminarPersona(cuenta):
    nombreAEliminar = input("Ingrese el nombre que desea eliminar de la lista de personas autorizadas ").title()
    if nombreAEliminar not in cuenta["personasAutorizadas"]:
        print(f"El nombre {nombreAEliminar} no existe en la lista de personas autorizadas. ")
        volverAtras()
    else:
        cuenta["personasAutorizadas"].remove(nombreAEliminar)
        print(f"El nombre {nombreAEliminar} ha sido eliminado exitosamente")
        volverAtras()
        
def verPersonas(cuenta):
    print("Personas autorizadas:")
    for persona in cuenta["personasAutorizadas"]:
        print(persona)
    volverAtras()
    
def volverAtras():
    print("Volviendo al menú anterior...")
    input("Presione ENTER para CONTINUAR....")

def fecha():
    hoy=dt.datetime.today()
    fecha_actual=hoy.strftime('%d/%m/%Y')
    return fecha_actual

def hora():
    hora=dt.datetime.today()
    hora_actual=hora.strftime('%H:%M')
    return hora_actual

def anio():
    hoy = dt.datetime.today()
    anio_actual=hoy.strftime('%Y')
    return anio_actual

#PROGRAMA PRINCIPAL

print("--- Bienvenido a nuestro cajero Automatico ---")

validarPersona()
