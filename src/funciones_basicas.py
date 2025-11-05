import csv
import os

def cargar_datos(RUTA_CSV):
    paises = []
    if not os.path.exists(RUTA_CSV):
        with open(RUTA_CSV, mode='r', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()
        return paises

    with open(RUTA_CSV, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila["nombre"].strip()
            poblacion = fila["poblacion"].strip()
            superficie = fila["superficie"].strip()
            continente = fila["continente"].strip() or "Desconocido"
            poblacion = int(poblacion) if poblacion.isdigit() and int(poblacion) >= 0 else 0
            superficie = int(superficie) if superficie.isdigit() and int(superficie) >= 0 else 0
            if nombre:
                paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
    return paises

def guardar_datos(RUTA_CSV, paises):
    
     campos = ["nombre","poblacion","superficie","continente"]
     with open(RUTA_CSV, mode='w', newline='', encoding='utf-8') as archivo:
          escritor = csv.DictWriter(archivo, fieldnames=campos)
          escritor.writeheader()
          for p in paises:
               escritor.writerow({
                    "nombre": p["nombre"],
                    "poblacion": int(p["poblacion"]),
                    "superficie": int(p["superficie"]),
                    "continente": p["continente"]
               })

def existe_pais(nombre, paises):
     nombre = nombre.strip().lower()
     for p in paises:
          if p["nombre"].strip().lower() == nombre:
               return True
     return False

def agregar_pais(RUTA_CSV):
     paises = cargar_datos(RUTA_CSV)
     nombre = input("Ingrese el nombre del país: ").strip()
     if not nombre:
          print("❌ El nombre no puede estar vacío.")
          return
     if existe_pais(nombre, paises):
          print("❌ El país ya existe.")
          return
     poblacion = input("Ingrese la población (número entero): ").strip()
     superficie = input("Ingrese la superficie en km² (número entero): ").strip()
     continente = input("Ingrese el continente: ").strip() or "Desconocido"
     poblacion = int(poblacion) if poblacion.isdigit() and int(poblacion) >= 0 else 0
     superficie = int(superficie) if superficie.isdigit() and int(superficie) >= 0 else 0
     paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
     guardar_datos(RUTA_CSV, paises)
     print(f"✅ País '{nombre}' agregado exitosamente.")

def actualizar_pais(RUTA_CSV):
    paises = cargar_datos(RUTA_CSV)
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    for p in paises:
        if p["nombre"].strip().lower() == nombre.strip().lower():
            poblacion = input(f"Ingrese la nueva población para '{nombre}' (actual: {p['poblacion']}): ").strip()
            superficie = input(f"Ingrese la nueva superficie para '{nombre}' (actual: {p['superficie']}): ").strip()
            if poblacion:
                p["poblacion"] = int(poblacion) if poblacion.isdigit() and int(poblacion) >= 0 else p["poblacion"]
            if superficie:
                    p["superficie"] = int(superficie) if superficie.isdigit() and int(superficie) >= 0 else p["superficie"]
            guardar_datos(RUTA_CSV, paises)
            print(f"✅ País '{nombre}' actualizado correctamente.")
            return
    print("❌ País no encontrado.")

def buscar_pais(RUTA_CSV):
     paises = cargar_datos(RUTA_CSV)
     nombre = input("Ingrese el nombre del país a buscar: ").strip().lower()
     if not nombre:
          print("❌ El nombre no puede estar vacío.")
          return
     encontrados = [p for p in paises if nombre in p["nombre"].strip().lower()]
     if not encontrados:
          print("❌ No se encontraron países que coincidan con la búsqueda.")
          return
     for p in encontrados:
          print(f"✅ País encontrado:")
          print(f"- Nombre: {p['nombre']}")
          print(f"- Población: {p['poblacion']}")
          print(f"- Superficie: {p['superficie']} km²")
          print(f"- Continente: {p['continente']}")

def mostrar_paises(RUTA_CSV):
     paises = cargar_datos(RUTA_CSV)
     if not paises:
          print("⚠️ No hay países registrados.")
          return
     print("---- Países ----")
     for p in paises:
          print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")
     print("-------------------------")
