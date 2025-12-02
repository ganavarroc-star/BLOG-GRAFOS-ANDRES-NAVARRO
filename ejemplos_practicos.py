"""
Ejemplos Prácticos Adicionales: Grafos y Colas en Aplicaciones Reales
Estos son ejemplos que complementan el blog técnico
"""

from collections import deque
from grafos import GrafoListaAdyacencia
from cola import Cola


# ==================== EJEMPLO 1: REDES SOCIALES ====================

def ejemplo_red_social():
    """
    Aplicación: Analizar conexiones en una red social como Facebook
    Problema: Encontrar amigos de amigos (sugerencias de amistad)
    """
    print("\n" + "="*60)
    print("EJEMPLO 1: Red Social - Sugerencias de Amistad")
    print("="*60)
    
    # Crear grafo de amistades
    red_social = GrafoListaAdyacencia(dirigido=False)
    
    # Agregar conexiones
    amistades = [
        ("Juan", "María"),
        ("Juan", "Pedro"),
        ("María", "Ana"),
        ("María", "Luis"),
        ("Pedro", "Carlos"),
        ("Pedro", "Luis"),
        ("Ana", "Sofia"),
    ]
    
    for persona1, persona2 in amistades:
        red_social.agregar_arista(persona1, persona2)
    
    print("\nRed social:")
    red_social.mostrar()
    
    # Buscar amigos de un usuario
    usuario = "Juan"
    print(f"\n✓ Amigos de {usuario}:")
    for amigo, _ in red_social.grafo[usuario]:
        print(f"  - {amigo}")
    
    # Buscar amigos de amigos (BFS)
    sugerencias = set()
    for amigo, _ in red_social.grafo[usuario]:
        for amigo_de_amigo, _ in red_social.grafo[amigo]:
            if amigo_de_amigo != usuario and amigo_de_amigo not in \
               [a for a, _ in red_social.grafo[usuario]]:
                sugerencias.add(amigo_de_amigo)
    
    print(f"\n✓ Sugerencias de amistad para {usuario}:")
    for sugerencia in sugerencias:
        print(f"  - {sugerencia} (amigo de amigos)")


# ==================== EJEMPLO 2: CIUDADES Y CARRETERAS ====================

def ejemplo_mapa_ciudades():
    """
    Aplicación: Sistema de navegación GPS
    Problema: Encontrar la ruta más corta entre ciudades
    """
    print("\n" + "="*60)
    print("EJEMPLO 2: Mapa de Ciudades - BFS para Ruta Más Corta")
    print("="*60)
    
    # Crear grafo de ciudades
    mapa = GrafoListaAdyacencia(dirigido=False)
    
    # Ciudades conectadas
    rutas = [
        ("Madrid", "Barcelona"),
        ("Madrid", "Valencia"),
        ("Barcelona", "Tarragona"),
        ("Valencia", "Murcia"),
        ("Tarragona", "Lleida"),
        ("Lleida", "Huesca"),
        ("Huesca", "Zaragoza"),
    ]
    
    for ciudad1, ciudad2 in rutas:
        mapa.agregar_arista(ciudad1, ciudad2)
    
    print("\nMapa de conexiones:")
    mapa.mostrar()
    
    # BFS para encontrar ruta más corta
    inicio = "Madrid"
    fin = "Huesca"
    
    visitados = set()
    cola = deque([(inicio, [inicio])])
    visitados.add(inicio)
    
    ruta = None
    while cola and not ruta:
        ciudad_actual, camino = cola.popleft()
        
        if ciudad_actual == fin:
            ruta = camino
            break
        
        for vecino, _ in mapa.grafo[ciudad_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
    
    if ruta:
        print(f"\n✓ Ruta más corta de {inicio} a {fin}:")
        print(f"  {' → '.join(ruta)}")
        print(f"  Distancia: {len(ruta) - 1} saltos")


# ==================== EJEMPLO 3: SISTEMA DE ATENCIÓN AL CLIENTE ====================

def ejemplo_cola_atencion():
    """
    Aplicación: Centro de atención al cliente (banco, supermercado)
    Problema: Gestionar colas de espera con prioridades
    """
    print("\n" + "="*60)
    print("EJEMPLO 3: Centro de Atención - Cola con Prioridades")
    print("="*60)
    
    import heapq
    
    class ColaAtencion:
        def __init__(self):
            self.cola = []
            self.contador = 0
        
        def agregar_cliente(self, nombre, tipo):
            """
            Tipos: 0=jubilado, 1=embarazada/discapacitado, 2=normal
            """
            prioridades = {"jubilado": 0, "embarazada": 0, "normal": 2}
            prioridad = prioridades.get(tipo, 2)
            heapq.heappush(self.cola, (prioridad, self.contador, nombre, tipo))
            self.contador += 1
        
        def atender_cliente(self):
            if self.cola:
                _, _, nombre, tipo = heapq.heappop(self.cola)
                return nombre, tipo
            return None, None
        
        def numero_en_espera(self):
            return len(self.cola)
    
    # Crear cola de atención
    cola_banco = ColaAtencion()
    
    # Clientes llegando
    clientes = [
        ("Carlos", "normal"),
        ("Abuela Rosa", "jubilado"),
        ("María", "embarazada"),
        ("Pedro", "normal"),
        ("Don José", "jubilado"),
        ("Ana", "normal"),
    ]
    
    print("\nClientes llegando al banco:")
    for nombre, tipo in clientes:
        cola_banco.agregar_cliente(nombre, tipo)
        print(f"  {nombre} ({tipo})")
    
    print(f"\nTotal en espera: {cola_banco.numero_en_espera()}")
    
    print("\nAtendiendo clientes (por prioridad):")
    while cola_banco.numero_en_espera() > 0:
        nombre, tipo = cola_banco.atender_cliente()
        print(f"  Caja 1: {nombre} ({tipo}) ✓")


# ==================== EJEMPLO 4: COMPONENTES EN CIRCUITO ELECTRÓNICO ====================

def ejemplo_componentes_conectados():
    """
    Aplicación: Análisis de circuitos electrónicos
    Problema: Encontrar componentes desconectados
    """
    print("\n" + "="*60)
    print("EJEMPLO 4: Circuito Electrónico - Componentes Conectados")
    print("="*60)
    
    # Crear grafo del circuito
    circuito = GrafoListaAdyacencia(dirigido=False)
    
    # Componentes conectados
    conexiones = [
        ("R1", "C1"),   # Resistor a Capacitor
        ("C1", "D1"),   # Capacitor a Diodo
        ("D1", "L1"),   # Diodo a Bobina
        ("R2", "C2"),   # Resistor 2 a Capacitor 2
        ("C2", "D2"),   # Capacitor 2 a Diodo 2
        # Nota: R2-D2 están desconectados de R1-C1-D1-L1
    ]
    
    for comp1, comp2 in conexiones:
        circuito.agregar_arista(comp1, comp2)
    
    print("\nCircuito:")
    circuito.mostrar()
    
    # Encontrar grupos de componentes conectados
    componentes_conectados = circuito.componentes_conexas()
    
    print(f"\nGrupos de componentes conectados: {len(componentes_conectados)}")
    for i, grupo in enumerate(componentes_conectados, 1):
        print(f"  Grupo {i}: {' ← → '.join(grupo)}")
    
    if len(componentes_conectados) > 1:
        print("\n⚠ Advertencia: Circuito con componentes desconectados")
    else:
        print("\n✓ Circuito completamente conectado")


# ==================== EJEMPLO 5: ANÁLISIS DE TRÁFICO ====================

def ejemplo_trafico_ciudades():
    """
    Aplicación: Sistema de análisis de tráfico
    Problema: Encontrar todas las rutas posibles
    """
    print("\n" + "="*60)
    print("EJEMPLO 5: Análisis de Tráfico - Todas las Rutas")
    print("="*60)
    
    # Grafo dirigido de tráfico
    trafico = GrafoListaAdyacencia(dirigido=True)
    
    # Rutas con sentidos únicos (avenidas de una sola dirección)
    rutas = [
        ("Av. Norte", "Centro"),
        ("Centro", "Av. Este"),
        ("Centro", "Av. Oeste"),
        ("Av. Este", "Zona Industrial"),
        ("Av. Oeste", "Zona Residencial"),
        ("Zona Industrial", "Autopista"),
        ("Zona Residencial", "Autopista"),
    ]
    
    for origen, destino in rutas:
        trafico.agregar_arista(origen, destino)
    
    print("\nRed de tráfico (direccional):")
    trafico.mostrar()
    
    # DFS desde el punto de entrada
    entrada = "Av. Norte"
    print(f"\n✓ Lugares accesibles desde {entrada}:")
    accesibles = trafico.dfs_iterativo(entrada)
    for lugar in accesibles:
        print(f"  - {lugar}")


# ==================== EJEMPLO 6: TAREAS CON DEPENDENCIAS ====================

def ejemplo_tareas_dependencias():
    """
    Aplicación: Gestor de proyectos (Pert/CPM)
    Problema: Detectar orden correcto de tareas
    """
    print("\n" + "="*60)
    print("EJEMPLO 6: Gestor de Proyecto - Orden de Tareas")
    print("="*60)
    
    # Grafo dirigido de dependencias
    proyecto = GrafoListaAdyacencia(dirigido=True)
    
    # Tareas y sus dependencias
    tareas = [
        ("Diseño", "Desarrollo"),      # Primero diseño, luego desarrollo
        ("Desarrollo", "Testing"),     # Después de desarrollo, testing
        ("Testing", "Deploy"),         # Después testing, deploy
        ("Documentación", "Deploy"),   # La documentación también debe estar antes de deploy
        ("Diseño", "Documentación"),   # Diseño viene antes de documentación
    ]
    
    for tarea1, tarea2 in tareas:
        proyecto.agregar_arista(tarea1, tarea2)
    
    print("\nDependencias del proyecto:")
    proyecto.mostrar()
    
    # Orden correcto (DFS inverso simularía ordenamiento topológico)
    print("\n✓ Orden sugerido de ejecución:")
    tareas_ordenadas = proyecto.dfs_iterativo("Diseño")
    for i, tarea in enumerate(tareas_ordenadas, 1):
        print(f"  {i}. {tarea}")


# ==================== MAIN ====================

if __name__ == "__main__":
    print("\n" + "█"*60)
    print("█ EJEMPLOS PRÁCTICOS: GRAFOS Y COLAS EN APLICACIONES REALES")
    print("█"*60)
    
    try:
        ejemplo_red_social()
        ejemplo_mapa_ciudades()
        ejemplo_cola_atencion()
        ejemplo_componentes_conectados()
        ejemplo_trafico_ciudades()
        ejemplo_tareas_dependencias()
        
        print("\n" + "█"*60)
        print("█ TODOS LOS EJEMPLOS COMPLETADOS EXITOSAMENTE")
        print("█"*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
