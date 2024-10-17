# Definición de la función (calcular bonificación)
# y uso de la funcion (lower()) para convertir a mayuscula la primera letra de una cadena
def calcular_bonificacion(salario_base, cargo_empleado, nivel_desempeno):
    cargo_empleado = cargo_empleado.lower()
    nivel_desempeno = nivel_desempeno.lower()
    bonificacion = 0

#Condisiones para directivos y operativos
    if cargo_empleado == "directivo":
        if nivel_desempeno == "alto":
            bonificacion = salario_base * 0.20
        elif nivel_desempeno == "medio":
            bonificacion = salario_base * 0.10
    elif cargo_empleado == "operativo":
        if nivel_desempeno == "alto":
            bonificacion = salario_base * 0.15
        elif nivel_desempeno == "medio":
            bonificacion = salario_base * 0.05

#si el desempeñp del empleado es bajo, nos retornara a bonificacion = 0
    return bonificacion

#Definición de la funcion (imprimir_resumen) para que nos muestre en pantalla los resultados
def imprimir_resumen(salario_base, cargo_empleado, nivel_desempeno):
    bonificacion = calcular_bonificacion(salario_base, cargo_empleado, nivel_desempeno)
    total_a_recibir = salario_base + bonificacion

#Datos a mostrar en pantalla usando f'string y \n para salto de linea
    print("-----Resumen del Pago-----")
    print(f"Cargo: {cargo_empleado.capitalize()}")
    print(f"Nivel de Desempeño: {nivel_desempeno.capitalize()}")
    print(f"Salario Base: ${salario_base}")
    print(f"Bonificación: ${bonificacion}")
    print(f"Total a Recibir: ${total_a_recibir}")
    print("------------------------------------\n")

#Datos solicitados por teclado
salario_base = float(input("Salario base mensual $: "))
cargo_empleado = input("Cargo empleado: ")
nivel_desempeno = input("Nivel de desempeño: ")

imprimir_resumen(salario_base, cargo_empleado, nivel_desempeno)