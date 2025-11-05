from funciones_basicas import(
     mostrar_paises,
     agregar_pais,
     actualizar_pais,
     buscar_pais,
)
from pathlib import Path
""" from funciones_avanzadas import(
     filtrar_paises,
     ordenar_paises,
     mostrar_estadisticas,
)
 """
DIR_SCRIPTS = Path(__file__).resolve().parent
DIR_RAIZ = DIR_SCRIPTS.parent
RUTA_CSV = DIR_RAIZ / "data" / "data_paises.csv"

def mostrar_menu():
     while True:

          print("*" * 30)
          print(" SISTEMA DE GESTIÓN DE PAÍSES 🌍 ")
          print("*" * 30)
          print("1. Mostrar todos los países")
          print("2. Agregar un nuevo país")
          print("3. Actualizar información de un país")
          print("4. Buscar un país por nombre")
          print("5. Filtrar paises")
          print("6. Ordenar paises")
          print("7. Mostrar estadísticas")
          print("8. Salir")
          print("*" * 30)

          opcion = input("Seleccione una opción: ").strip()

          match opcion:
               case "1":
                    mostrar_paises(RUTA_CSV)
               case "2":
                    agregar_pais(RUTA_CSV)
               case "3":
                    actualizar_pais(RUTA_CSV)
               case "4":
                    buscar_pais(RUTA_CSV)
               case "5":
                    """ filtrar_paises(RUTA_CSV) """
               case "6":
                    """ ordenar_paises(RUTA_CSV) """
               case "7":
                    """ mostrar_estadisticas(RUTA_CSV) """
               case "8":
                    print("Saliendo del programa...")
                    break
               case _:
                    print("Opción inválida. Por favor, intente de nuevo.")

mostrar_menu()