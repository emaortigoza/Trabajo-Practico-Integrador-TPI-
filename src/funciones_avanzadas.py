from funciones_basicas import cargar_datos

def filtrar_paises(RUTA_CSV):
    paises = cargar_datos(RUTA_CSV)
    if not paises:
        print("⚠️ No hay países registrados.")
        return
    
    print("Opciones de filtro:")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Elija una opción (1-3): ").strip()

    if opcion == "1":
        continente = input("Ingrese el continente: ").strip().lower()
        filtrados = [p for p in paises if p["continente"].strip().lower() == continente]
    elif opcion == "2":
        min_p = input("Ingrese población mínima: ").strip()
        max_p = input("Ingrese población máxima: ").strip()
        min_p = int(min_p) if min_p.isdigit() else 0
        max_p = int(max_p) if max_p.isdigit() else 9999999999
        filtrados = [p for p in paises if min_p <= p["poblacion"] <= max_p]
    elif opcion == "3":
        min_s = input("Ingrese superficie mínima: ").strip()
        max_s = input("Ingrese superficie máxima: ").strip()
        min_s = int(min_s) if min_s.isdigit() else 0
        max_s = int(max_s) if max_s.isdigit() else 9999999999
        filtrados = [p for p in paises if min_s <= p["superficie"] <= max_s]
    else:
        print("❌ Opción inválida.")
        return

    if not filtrados:
        print("❌ No se encontraron países con ese criterio.")
        return

    print("---- Resultados del filtro ----")
    for p in filtrados:
        print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} | Cont: {p['continente']}")
    print("--------------------------------")


def ordenar_paises(RUTA_CSV):
    paises = cargar_datos(RUTA_CSV)
    if not paises:
        print("⚠️ No hay países registrados.")
        return

    print("Campos disponibles: nombre, poblacion, superficie")
    campo = input("Ordenar por: ").strip().lower()
    if campo not in ["nombre", "poblacion", "superficie"]:
        print("❌ Campo inválido.")
        return

    orden = input("Orden ascendente (a) o descendente (d)? [a/d]: ").strip().lower()
    reverso = True if orden == "d" else False

    paises_ordenados = sorted(paises, key=lambda p: p[campo], reverse=reverso)

    print("---- Países ordenados ----")
    for p in paises_ordenados:
        print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} | Cont: {p['continente']}")
    print("---------------------------")


def mostrar_estadisticas(RUTA_CSV):
    paises = cargar_datos(RUTA_CSV)
    if not paises:
        print("⚠️ No hay países registrados.")
        return

    # País con mayor y menor población
    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])

    # Promedios
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    # Cantidad por continente
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1

    print("---- Estadísticas ----")
    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Promedio de población: {prom_pob:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f} km²")
    print("Cantidad de países por continente:")
    for c, cant in continentes.items():
        print(f"- {c}: {cant}")
    print("-----------------------")
    
    