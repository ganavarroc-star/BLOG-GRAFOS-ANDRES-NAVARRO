"""
Implementaciones de Estructura de Datos: Grafos
Incluye: Grafo con Lista de Adyacencia, Matriz de Adyacencia, BFS y DFS
"""

from collections import deque, defaultdict
from typing import List, Dict, Set, Tuple


# ==================== LISTA DE ADYACENCIA ====================

class GrafoListaAdyacencia:
    """
    Implementación de un Grafo usando Lista de Adyacencia.
    Eficiente para grafos dispersos (pocas aristas).
    
    Complejidad espacial: O(V + E)
    """
    
    def __init__(self, dirigido=False):
        """
        Args:
            dirigido: True si es grafo dirigido, False si no dirigido
        """
        self.grafo = defaultdict(list)
        self.dirigido = dirigido
    
    def agregar_arista(self, u, v, peso=1):
        """
        Añade una arista entre los nodos u y v.
        
        Args:
            u: Nodo origen
            v: Nodo destino
            peso: Peso de la arista (default: 1)
        """
        self.grafo[u].append((v, peso))
        
        # Para grafos no dirigidos, añadir también la arista inversa
        if not self.dirigido:
            self.grafo[v].append((u, peso))
    
    def obtener_vecinos(self, nodo):
        """Retorna los vecinos de un nodo"""
        return self.grafo.get(nodo, [])
    
    def existe_arista(self, u, v):
        """Verifica si existe una arista entre u y v"""
        for vecino, _ in self.grafo[u]:
            if vecino == v:
                return True
        return False
    
    def mostrar(self):
        """Muestra la lista de adyacencia"""
        print("\nLista de Adyacencia:")
        for nodo in sorted(self.grafo.keys()):
            vecinos = ", ".join([f"{v}({p})" for v, p in self.grafo[nodo]])
            print(f"  {nodo}: [{vecinos}]")
    
    def bfs(self, inicio):
        """
        Búsqueda en Amplitud (BFS) - Breadth-First Search
        
        Complejidad: O(V + E)
        
        Args:
            inicio: Nodo de inicio
            
        Returns:
            Lista de nodos visitados en orden BFS
        """
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        resultado = []
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)
            
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return resultado
    
    def dfs_iterativo(self, inicio):
        """
        Búsqueda en Profundidad Iterativa (DFS)
        
        Complejidad: O(V + E)
        
        Args:
            inicio: Nodo de inicio
            
        Returns:
            Lista de nodos visitados en orden DFS
        """
        visitados = set()
        pila = [inicio]
        resultado = []
        
        while pila:
            nodo = pila.pop()
            
            if nodo not in visitados:
                visitados.add(nodo)
                resultado.append(nodo)
                
                # Agregar vecinos a la pila (en orden inverso)
                for vecino, _ in reversed(self.grafo[nodo]):
                    if vecino not in visitados:
                        pila.append(vecino)
        
        return resultado
    
    def dfs_recursivo(self, inicio, visitados=None, resultado=None):
        """
        Búsqueda en Profundidad Recursiva (DFS)
        
        Args:
            inicio: Nodo de inicio
            visitados: Conjunto de nodos visitados
            resultado: Lista de nodos visitados
            
        Returns:
            Lista de nodos visitados en orden DFS
        """
        if visitados is None:
            visitados = set()
        if resultado is None:
            resultado = []
        
        visitados.add(inicio)
        resultado.append(inicio)
        
        for vecino, _ in self.grafo[inicio]:
            if vecino not in visitados:
                self.dfs_recursivo(vecino, visitados, resultado)
        
        return resultado
    
    def tiene_ciclo(self):
        """
        Detecta si el grafo tiene ciclos (solo para grafos no dirigidos)
        """
        visitados = set()
        
        def dfs(nodo, padre=None):
            visitados.add(nodo)
            
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    if dfs(vecino, nodo):
                        return True
                elif vecino != padre:
                    return True
            
            return False
        
        for nodo in self.grafo:
            if nodo not in visitados:
                if dfs(nodo):
                    return True
        
        return False
    
    def componentes_conexas(self):
        """
        Encuentra todas las componentes conexas del grafo
        
        Returns:
            Lista de listas, cada una conteniendo nodos de una componente
        """
        visitados = set()
        componentes = []
        
        for nodo in self.grafo:
            if nodo not in visitados:
                componente = self.bfs(nodo)
                for n in componente:
                    visitados.add(n)
                componentes.append(componente)
        
        return componentes


# ==================== MATRIZ DE ADYACENCIA ====================

class GrafoMatrizAdyacencia:
    """
    Implementación de un Grafo usando Matriz de Adyacencia.
    Eficiente para grafos densos (muchas aristas).
    
    Complejidad espacial: O(V²)
    """
    
    def __init__(self, vertices, dirigido=False, ponderado=False):
        """
        Args:
            vertices: Número de vértices
            dirigido: True si es grafo dirigido
            ponderado: True si es grafo ponderado
        """
        self.V = vertices
        self.dirigido = dirigido
        self.ponderado = ponderado
        
        # Inicializar matriz
        if ponderado:
            self.grafo = [[float('inf')] * vertices for _ in range(vertices)]
            # Diagonal con 0
            for i in range(vertices):
                self.grafo[i][i] = 0
        else:
            self.grafo = [[0] * vertices for _ in range(vertices)]
    
    def agregar_arista(self, u, v, peso=1):
        """
        Añade una arista entre u y v
        
        Args:
            u: Índice del nodo origen
            v: Índice del nodo destino
            peso: Peso de la arista
        """
        if self.ponderado:
            self.grafo[u][v] = peso
            if not self.dirigido:
                self.grafo[v][u] = peso
        else:
            self.grafo[u][v] = 1
            if not self.dirigido:
                self.grafo[v][u] = 1
    
    def existe_arista(self, u, v):
        """Verifica si existe una arista entre u y v - O(1)"""
        if self.ponderado:
            return self.grafo[u][v] != float('inf')
        else:
            return self.grafo[u][v] == 1
    
    def obtener_peso(self, u, v):
        """Obtiene el peso de la arista entre u y v"""
        return self.grafo[u][v]
    
    def mostrar(self):
        """Muestra la matriz de adyacencia"""
        print("\nMatriz de Adyacencia:")
        print("   ", end="")
        for i in range(self.V):
            print(f"{i:4}", end="")
        print()
        
        for i in range(self.V):
            print(f"{i}  ", end="")
            for j in range(self.V):
                val = self.grafo[i][j]
                if self.ponderado and val == float('inf'):
                    print("  ∞ ", end="")
                else:
                    print(f"{int(val):4}", end="")
            print()
    
    def bfs(self, inicio):
        """Búsqueda en Amplitud"""
        visitados = [False] * self.V
        cola = deque([inicio])
        visitados[inicio] = True
        resultado = []
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)
            
            for vecino in range(self.V):
                if self.existe_arista(nodo, vecino) and not visitados[vecino]:
                    visitados[vecino] = True
                    cola.append(vecino)
        
        return resultado
    
    def dfs(self, inicio):
        """Búsqueda en Profundidad"""
        visitados = [False] * self.V
        pila = [inicio]
        resultado = []
        
        while pila:
            nodo = pila.pop()
            
            if not visitados[nodo]:
                visitados[nodo] = True
                resultado.append(nodo)
                
                for vecino in range(self.V - 1, -1, -1):
                    if self.existe_arista(nodo, vecino) and not visitados[vecino]:
                        pila.append(vecino)
        
        return resultado


# ==================== EJEMPLOS DE USO ====================

def ejemplo_lista_adyacencia():
    """Ejemplo de uso: Lista de Adyacencia"""
    print("=" * 60)
    print("EJEMPLO 1: Lista de Adyacencia")
    print("=" * 60)
    
    # Crear grafo no dirigido
    g = GrafoListaAdyacencia(dirigido=False)
    
    # Agregar aristas
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'D')
    g.agregar_arista('B', 'C')
    g.agregar_arista('B', 'D')
    g.agregar_arista('C', 'D')
    g.agregar_arista('C', 'E')
    
    # Mostrar
    g.mostrar()
    
    # BFS
    print("\nBFS desde A:", g.bfs('A'))
    
    # DFS
    print("DFS desde A (iterativo):", g.dfs_iterativo('A'))
    print("DFS desde A (recursivo):", g.dfs_recursivo('A'))
    
    # Detectar ciclo
    print(f"¿Tiene ciclo?: {g.tiene_ciclo()}")
    
    # Componentes conexas
    print("Componentes conexas:", g.componentes_conexas())
    print()


def ejemplo_matriz_adyacencia():
    """Ejemplo de uso: Matriz de Adyacencia"""
    print("=" * 60)
    print("EJEMPLO 2: Matriz de Adyacencia")
    print("=" * 60)
    
    # Crear grafo no dirigido
    g = GrafoMatrizAdyacencia(5, dirigido=False)
    
    # Agregar aristas (usando índices 0-4)
    g.agregar_arista(0, 1)  # A-B
    g.agregar_arista(0, 3)  # A-D
    g.agregar_arista(1, 2)  # B-C
    g.agregar_arista(1, 3)  # B-D
    g.agregar_arista(2, 3)  # C-D
    g.agregar_arista(2, 4)  # C-E
    
    # Mostrar
    g.mostrar()
    
    # Verificar aristas
    print(f"\n¿Existe arista 0-1? {g.existe_arista(0, 1)}")
    print(f"¿Existe arista 0-4? {g.existe_arista(0, 4)}")
    
    # BFS
    print("\nBFS desde 0:", g.bfs(0))
    
    # DFS
    print("DFS desde 0:", g.dfs(0))
    print()


def ejemplo_grafo_ponderado():
    """Ejemplo de uso: Grafo Ponderado"""
    print("=" * 60)
    print("EJEMPLO 3: Grafo Ponderado (Matriz)")
    print("=" * 60)
    
    # Crear grafo ponderado
    g = GrafoMatrizAdyacencia(5, dirigido=False, ponderado=True)
    
    # Agregar aristas con pesos
    g.agregar_arista(0, 1, 5)   # A-B: 5
    g.agregar_arista(0, 3, 3)   # A-D: 3
    g.agregar_arista(1, 2, 8)   # B-C: 8
    g.agregar_arista(1, 3, 2)   # B-D: 2
    g.agregar_arista(2, 3, 1)   # C-D: 1
    g.agregar_arista(2, 4, 4)   # C-E: 4
    
    # Mostrar
    g.mostrar()
    
    # Obtener pesos
    print(f"\nPeso de arista 0-1: {g.obtener_peso(0, 1)}")
    print(f"Peso de arista 0-2: {g.obtener_peso(0, 2)}")
    print()


def ejemplo_grafo_dirigido():
    """Ejemplo de uso: Grafo Dirigido"""
    print("=" * 60)
    print("EJEMPLO 4: Grafo Dirigido (Lista Adyacencia)")
    print("=" * 60)
    
    # Crear grafo dirigido
    g = GrafoListaAdyacencia(dirigido=True)
    
    # Agregar aristas dirigidas
    g.agregar_arista('A', 'B')
    g.agregar_arista('A', 'C')
    g.agregar_arista('B', 'C')
    g.agregar_arista('B', 'D')
    g.agregar_arista('C', 'D')
    g.agregar_arista('D', 'E')
    
    # Mostrar
    g.mostrar()
    
    # BFS
    print("\nBFS desde A:", g.bfs('A'))
    
    # DFS
    print("DFS desde A:", g.dfs_iterativo('A'))
    print()


if __name__ == "__main__":
    # Ejecutar ejemplos
    ejemplo_lista_adyacencia()
    ejemplo_matriz_adyacencia()
    ejemplo_grafo_ponderado()
    ejemplo_grafo_dirigido()
    
    print("=" * 60)
    print("Ejemplos completados exitosamente")
    print("=" * 60)
