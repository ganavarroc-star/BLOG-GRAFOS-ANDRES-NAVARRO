# Blog Técnico: Estructura de Datos - Grafos

## 📚 Descripción

Blog técnico interactivo dedicado a la **Estructura de Datos Grafos** y temas relacionados. Este proyecto combina contenido educativo de alta calidad con implementaciones prácticas en Python, diseño web responsivo y best practices de desarrollo.

## 🎯 Objetivo de la Actividad

Crear un blog técnico que cubra los fundamentos de la estructura de datos de **Grafos**, incluyendo:
- Conceptos fundamentales
- Representación en memoria
- Algoritmos de recorrido
- Aplicaciones prácticas

## 📑 Artículos Principales

### 1. 🎯 [Introducción a los Grafos](posts/introduccion-grafos.html)
Aprende los conceptos esenciales sobre grafos:
- **Definición de Grafo**: Estructura no lineal compuesta por nodos y aristas
- **Conceptos Clave**: Vértices, aristas, peso, grado, camino y ciclo
- **Tipos de Grafos**: 
  - Grafos no dirigidos
  - Grafos dirigidos
  - Grafos ponderados
  - Grafos cíclicos vs acíclicos
  - Grafos conectados vs desconectados
- **Aplicaciones Prácticas**: Redes sociales, mapas, biología, sistemas operativos

### 2. 🔧 [Representación de Grafos](posts/representacion-grafos.html)
Explora cómo representar grafos en memoria:
- **Lista de Adyacencia**
  - Estructura: O(V + E)
  - Ideal para grafos dispersos
  - Fácil recorrido de vecinos
  - Implementación en Python
- **Matriz de Adyacencia**
  - Estructura: O(V²)
  - Ideal para grafos densos
  - Búsqueda rápida de aristas O(1)
  - Implementación con arrays
- **Comparativa detallada** de ventajas y desventajas

### 3. ⚡ [Algoritmos de Recorrido: BFS y DFS](posts/algoritmos-recorrido.html)
Domina los algoritmos fundamentales de búsqueda:
- **Búsqueda en Amplitud (BFS - Breadth-First Search)**
  - Recorrido nivel por nivel
  - Utiliza cola (FIFO)
  - Encuentra camino más corto (grafos no ponderados)
  - O(V + E) tiempo
  - Aplicaciones: conexidad, análisis de redes
  
- **Búsqueda en Profundidad (DFS - Depth-First Search)**
  - Recorrido profundo antes de retroceder
  - Utiliza pila o recursión
  - Detecta ciclos eficientemente
  - O(V + E) tiempo
  - Aplicaciones: componentes conexas, ordenamiento topológico

### 4. 📋 [Cola (Queue) - FIFO](posts/cola.html)
Estructura complementaria esencial:
- **Definición**: First In, First Out (FIFO)
- **Operaciones**: enqueue, dequeue, front, rear, isEmpty, size
- **Implementación**: Lista vs deque optimizado
- **Aplicaciones**: BFS, sistemas de atención, procesamiento de tareas
- **Cola con Prioridad**: Variante avanzada

## 🏗️ Estructura del Proyecto

```
blog_grafos/
├── index.html                 # Página principal
├── README.md                  # Este archivo
├── cola.py                    # Implementación Python de Cola
├── css/
│   └── style.css             # Estilos CSS (diseño responsivo y moderno)
└── posts/
    ├── introduccion-grafos.html
    ├── representacion-grafos.html
    ├── algoritmos-recorrido.html
    └── cola.html
```

## 🔧 Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3 (con variables CSS y flexbox/grid)
- **Backend**: Python 3.x (implementaciones de algoritmos)
- **Control de Versiones**: Git / GitHub
- **Hosting**: GitHub Pages

## 🎨 Características del Diseño

- ✅ **Responsivo**: Adaptable a todos los tamaños de pantalla
- ✅ **Tema oscuro profesional**: Colores azul cian (#00d4ff) y verde (#00ff99)
- ✅ **Tipografía clara**: Legibilidad optimizada
- ✅ **Navegación intuitiva**: Enlaces entre artículos
- ✅ **Código resaltado**: Bloques de código bien formateados
- ✅ **Diagramas visuales**: Representaciones ASCII claras

## 💻 Ejemplos de Código

### Implementación de Cola en Python

```python
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def enqueue(self, elemento):
        """Añade un elemento al final"""
        self.elementos.append(elemento)
    
    def dequeue(self):
        """Extrae el primer elemento"""
        if not self.esta_vacia():
            return self.elementos.popleft()
        return None
    
    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return len(self.elementos) == 0

# Uso
cola = Cola()
cola.enqueue("A")
cola.enqueue("B")
print(cola.dequeue())  # "A"
```

### Búsqueda en Amplitud (BFS)

```python
from collections import deque

def bfs(grafo, inicio):
    """BFS - Búsqueda en Amplitud"""
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        nodo = cola.popleft()
        print(f"Visitando: {nodo}")
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
```

## 🚀 Cómo Usar Este Blog

1. **Abrir en navegador**: Descarga el proyecto y abre `index.html`
2. **Navegar por artículos**: Haz click en los enlaces de los posts
3. **Estudiar código**: Revisa los ejemplos de Python
4. **Practicar**: Implementa los algoritmos por tu cuenta

## 📊 Complejidad de Algoritmos

| Algoritmo | Tiempo | Espacio | Caso de Uso |
|-----------|--------|---------|------------|
| BFS | O(V + E) | O(V) | Camino más corto (no ponderado) |
| DFS | O(V + E) | O(V) | Detectar ciclos |
| Cola Enqueue | O(1) | - | Inserción FIFO |
| Cola Dequeue | O(1)* | - | Extracción FIFO |

*O(1) con deque, O(n) con listas estándar

## 📋 Checklist de Requisitos (Actividad)

- ✅ **Artículos Mínimos**: 3 posts requeridos
  - ✅ Post 1: Introducción a los Grafos
  - ✅ Post 2: Representación de Grafos
  - ✅ Post 3: Algoritmos de Recorrido (BFS y DFS)
  - ✅ Post 4: Bonus - Cola (Queue)

- ✅ **Contenido Técnico**:
  - ✅ Definiciones claras
  - ✅ Diagramas visuales
  - ✅ Ejemplos de código
  - ✅ Casos de uso reales
  - ✅ Análisis de complejidad

- ✅ **Tecnología Web**:
  - ✅ HTML5 semántico
  - ✅ CSS3 responsive
  - ✅ Navegación consistente
  - ✅ Diseño profesional

- ✅ **Control de Versiones**:
  - ✅ Repositorio Git
  - ✅ Commits significativos
  - ✅ README documentado
  - ✅ Publicado en GitHub Pages

## 🌐 GitHub Pages

**URL del Blog**: `https://[tu-usuario].github.io/blog_grafos`

Para publicar en GitHub Pages:
1. Sube tu repositorio a GitHub
2. Ve a Settings → Pages
3. Selecciona Branch: main (o master)
4. Guarda
5. Tu blog será accesible en la URL anterior

## 📚 Referencias y Recursos

- [GeeksforGeeks - Graphs](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Programiz - Data Structures](https://www.programiz.com/dsa)
- [Python Collections - deque](https://docs.python.org/3/library/collections.html#collections.deque)
- [Algorithms MIT](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

## ✍️ Autor

[Tu nombre]  
Estudiante de Estructura de Datos II  
Diciembre 2024

## 📄 Licencia

Este proyecto está disponible bajo licencia educativa. Úsalo libremente para aprender y enseñar.

## 🤝 Contribuciones

Las sugerencias y mejoras son bienvenidas. Si encuentras errores o tienes recomendaciones, abre un issue o pull request.

---

**Nota**: Este blog fue creado como parte de una actividad académica sobre estructura de datos. El objetivo es proporcionar una guía clara y completa sobre grafos y estructuras de datos relacionadas.

**Última actualización**: Diciembre 2024
