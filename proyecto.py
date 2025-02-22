
estudiantes = [] 

def agregar_estudiante(nombre):
   
    estudiantes.append({"nombre": nombre, "notas": []})  
    print(f"Estudiante '{nombre}' agregado.")

def registrar_notas(nombre):
  
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():  
            notas_input = input("Ingrese las notas separadas por espacio: ") 
            try:
                notas = list(map(float, notas_input.split()))
                estudiante["notas"].extend(notas) 
                print(f"Notas {notas} registradas para {nombre}.")
                return
            except ValueError:
                print("Por favor, ingrese solo números válidos.")
            break
    print("Estudiante no encontrado.")

def calcular_promedio(notas):
    
    if len(notas) == 0:
        return 0  # 
    return sum(notas) / len(notas)  
def ver_estudiantes():
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\nLista de Estudiantes:")
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])  
        estado = "Aprobado" if promedio >= 6 else "Reprobado"  
        print(f"{estudiante['nombre']} - Notas: {estudiante['notas']} - Promedio: {promedio:.2f} - Estado: {estado}")

def menu():
   
    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar estudiante")
        print("2. Registrar notas")
        print("3. Ver lista de estudiantes")
        print("4. Salir")

        opcion = input("Selecciona la opción que quieres: ")  
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")  
            agregar_estudiante(nombre)  
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante: ") 
            registrar_notas(nombre)  
        elif opcion == "3":
            ver_estudiantes()
        elif opcion == "4":
            print(" Hasta luego") 
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.") 


if __name__ == "__main__":
    menu()  



   




