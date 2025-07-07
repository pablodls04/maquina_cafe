from maquina_cafe import MaquinaCafe

def mostrar_opciones():
    print("=== Máquina de Café ☕ ===")
    print("1. Seleccionar vaso (pequeño / mediano / grande)")
    print("2. Seleccionar azúcar (número de cucharadas)")
    print("3. Preparar café")
    print("4. Salir")

def main():
    maquina = MaquinaCafe()
    while True:
        mostrar_opciones()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            tipo = input("Tamaño del vaso: ").strip().lower()
            print(maquina.seleccionar_vaso(tipo))
        elif opcion == "2":
            try:
                cantidad = int(input("Cantidad de azúcar: "))
                print(maquina.seleccionar_azucar(cantidad))
            except ValueError:
                print("Número inválido.")
        elif opcion == "3":
            print(maquina.preparar_cafe())
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
