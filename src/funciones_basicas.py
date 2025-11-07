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
<<<<<<< Updated upstream
     print("*" * 10 + " Agregar País " + "*" * 10)

     # ---- Validación del nombre ----
     while True:
          nombre = input("Ingrese el nombre del país: ").strip()
          if not nombre:
               print("❌ El nombre no puede estar vacío.")
               continue
          if existe_pais(nombre, paises):
               print("⚠️ El país ya existe en la base de datos.")
               return
          break

     # ---- Validación de la población ----
     while True:
          poblacion = input("Ingrese la población: ").strip()
          if not poblacion:
               print("❌ La población no puede estar vacía.")
               continue
          if not poblacion.isdigit() or int(poblacion) <= 0:
               print("❌ La población debe ser un número entero positivo.")
               continue
          poblacion = int(poblacion)
          break

     # ---- Validación de la superficie ----
     while True:
          superficie = input("Ingrese la superficie (km²): ").strip()
          if not superficie:
               print("❌ La superficie no puede estar vacía.")
               continue
          if not superficie.isdigit() or int(superficie) <= 0:
               print("❌ La superficie debe ser un número entero positivo.")
               continue
          superficie = int(superficie)
          break

     # ---- Validación del continente ----
     continentes_validos = ["America", "Europa", "Asia", "África", "Oceanía", "Antártida"]
     while True:
          continente = input("Ingrese el continente: ").strip()
          if not continente:
               print("❌ El continente no puede estar vacío.")
               continue
          if continente not in continentes_validos:
               print(f"❌ Continente inválido. Opciones válidas: {', '.join(continentes_validos)}")
               continue
          break

     #---- Agregar el nuevo país ----
     nuevo_pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
     paises.append(nuevo_pais)

=======
     nombre = input("Ingrese el nombre del país: ").strip()
     if not nombre:
          print("❌ El nombre no puede estar vacío.")
          return
     if existe_pais(nombre, paises):
          print("❌ El país ya existe.")
          return
     poblacion = input("Ingrese la población (número entero): ").strip().lower()
     superficie = input("Ingrese la superficie en km² (número entero): ").strip().lower()
     continente = input("Ingrese el continente: ").strip().lower() or "Desconocido"
     poblacion = int(poblacion) if poblacion.isdigit() and int(poblacion) >= 0 else 0
     superficie = int(superficie) if superficie.isdigit() and int(superficie) >= 0 else 0
     paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
>>>>>>> Stashed changes
     guardar_datos(RUTA_CSV, paises)
     print(f"✅ País '{nombre}' agregado correctamente.")

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
