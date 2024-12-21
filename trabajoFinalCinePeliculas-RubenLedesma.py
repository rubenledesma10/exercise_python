import datetime as dt

def menuPrincipal():
    funciones = crearFunciones()  # Crear múltiples funciones
    print("Bienvenido a nuestro gestor de asientos de cine")

    while True:
        print("Seleccione la función (película) que desea gestionar:")
        for clave, funcion in funciones.items():
            print(f"{clave}. {funcion['pelicula']}")
        print("4. Salir")
        
        opcion_funcion = input("Ingrese el número de la función: ")
        if opcion_funcion == "4":
            print("Gracias, vuelva pronto")
            break
        elif opcion_funcion in funciones:
            funcion_actual = funciones[opcion_funcion]
            gestionarFuncion(funcion_actual)
        else:
            print("Opción inválida, intente nuevamente.")

def gestionarFuncion(funcion):
    sala = funcion["sala"]
    reservas = funcion["reservas"]
    print(f"Entradas para la película: {funcion['pelicula']} ---")

    while True:
        print("\n¿Qué desea hacer en esta función?")
        print("1. Reservar asiento ")
        print("2. Eliminar asiento reservado ")
        print("3. Ver el mapa de asientos ")
        print("4. Lista de asientos reservados")
        print("5. Volver al menú principal")
        try:
            opcion = int(input("Ingrese el número de la opción que quiera: "))
            if opcion == 1:
                crearReserva(sala, reservas)
            elif opcion == 2:
                eliminarReserva(sala, reservas)
            elif opcion == 3:
                mostrarSala(sala)
            elif opcion == 4:
                listarReservas(reservas)
            elif opcion == 5:
                print("Regresando al menú principal...")
                break
            else:
                print("Eligió una opción incorrecta.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def crearFunciones():
    funciones = {
        "1": {"pelicula": "Batman", "sala": crearSala(), "reservas": []},
        "2": {"pelicula": "Superman", "sala": crearSala(), "reservas": []},
        "3": {"pelicula": "Spider-Man", "sala": crearSala(), "reservas": []},
    }
    return funciones

def crearSala():
    cine = {}
    filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in filas:
        fila = []
        for j in range(1, 23):
            if j == 10 or j == 11:
                fila.append("P")
            else:
                fila.append("D")
        cine[i] = fila
    return cine

def crearReserva(sala, reservas):
    mostrarSala(sala)
    lugarReserva = datosReserva(sala)
    if lugarReserva is None:
        print("No se pudo realizar la reserva")
        return
    fila, columna = lugarReserva
    nombre, precio, fechaReserva, horaReserva = datosClientes()
    reservas.append({
        "Ubicación": f"{fila}{columna}", "Nombre": f"{nombre}", "Precio": precio, "Fecha": f"{fechaReserva}", "Hora": f"{horaReserva}"
    })
    sala[fila][columna - 1] = "X"
    print(f"Reserva confirmada para {nombre.title()}, en el asiento {fila}{columna} a las {horaReserva} del día {fechaReserva}.")

def mostrarSala(sala):
    print("------------------ PANTALLA ------------------")
    for clave, valor in sala.items():
        print(f"{clave}: {' '.join(valor)}")
    print("Aclaración: D: Asiento Disponible, P: Pasillo, X:Asiento Ocupado")

def datosReserva(sala):
    fila = input("Ingrese una fila (A-J): ").upper()
    try:
        columna = int(input("Ingrese el número de asiento (1-22): "))
        if fila not in sala or columna < 1 or columna > 22:
            print("Error: La fila o el asiento ingresado no son válidos.")
            return None
        if not verificarAsiento(sala, fila, columna):
            return None
        return fila, columna
    except ValueError:
        print("Error: El número del asiento debe ser válido.")
        return None

def verificarAsiento(sala, fila, columna):
    indice_columna = columna - 1
    if sala[fila][indice_columna] != "D":
        print("Ese asiento ya está ocupado.")
        return False
    elif sala[fila][indice_columna] == "P":
        print("No puede sentarse en el pasillo por cuestiones de seguridad.")
        return False
    return True

def datosClientes():
    nombre = input("Ingrese su nombre y apellido: ")
    precio = 2700
    fechaReserva = fecha()
    horaReserva = hora()
    return nombre, precio, fechaReserva, horaReserva

def eliminarReserva(sala, reservas):
    if not reservas:
        print("No hay reservas para eliminar.")
        return
    listarReservas(reservas)
    ubicacion = input("Ingrese el asiento a eliminar (Ej. A1, B5): ").upper()
    reservaEliminar = None
    for reserva in reservas:
        if reserva["Ubicación"] == ubicacion:
            reservaEliminar = reserva
            break
    if reservaEliminar is None:
        print(f"No se encontró ninguna reserva en el asiento {ubicacion}.")
        return
    reservas.remove(reservaEliminar)
    fila = ubicacion[0]
    columna = int(ubicacion[1:])
    sala[fila][columna - 1] = "D"
    print(f"Reserva en el asiento {ubicacion} eliminada exitosamente.")

def listarReservas(reserva):
    if not reserva:
        print("No hay reservas realizadas por el momento.")
        return
    print("RESERVAS")
    total = 0
    for reservas in reserva:
        ubicacion = reservas["Ubicación"]
        nombre = reservas["Nombre"]
        precio = reservas["Precio"]
        fecha = reservas["Fecha"]
        hora = reservas["Hora"]
        total += precio
        print(f"Asiento: {ubicacion} | Nombre: {nombre.title()} | Precio: ${precio} | Fecha: {fecha} | Hora: {hora}")
    print(f"El importe total de la reserva es de ${total}")

def fecha():
    hoy = dt.datetime.today()
    fecha_actual = hoy.strftime('%d/%m/%Y')
    return fecha_actual

def hora():
    hoy = dt.datetime.today()
    hora_actual = hoy.strftime('%H:%M')
    return hora_actual

# PROGRAMA PRINCIPAL
menuPrincipal()
