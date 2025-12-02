"""
Ejercicio: Estructura de Datos Cola (Queue)
Implementación de una cola FIFO (First In, First Out)
"""

class Cola:
    """
    Clase que implementa una Cola (Queue) con estructura FIFO.
    El primer elemento en entrar es el primero en salir.
    """
    
    def __init__(self):
        """Inicializa una cola vacía."""
        self.elementos = []
    
    def enqueue(self, elemento):
        """
        Añade un elemento al final de la cola.
        
        Args:
            elemento: El elemento a añadir
        """
        self.elementos.append(elemento)
        print(f"✓ {elemento} añadido a la cola")
    
    def dequeue(self):
        """
        Elimina y devuelve el primer elemento de la cola.
        
        Returns:
            El primer elemento de la cola
            
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            print("❌ Error: La cola está vacía")
            return None
        
        elemento = self.elementos.pop(0)
        print(f"✓ {elemento} removido de la cola")
        return elemento
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            True si la cola está vacía, False en caso contrario
        """
        return len(self.elementos) == 0
    
    def tamaño(self):
        """
        Devuelve el número de elementos en la cola.
        
        Returns:
            Número de elementos en la cola
        """
        return len(self.elementos)
    
    def frente(self):
        """
        Devuelve el primer elemento sin eliminarlo.
        
        Returns:
            El primer elemento de la cola o None si está vacía
        """
        if self.esta_vacia():
            return None
        return self.elementos[0]
    
    def mostrar(self):
        """Muestra todos los elementos de la cola."""
        if self.esta_vacia():
            print("Cola vacía: []")
        else:
            print(f"Cola: {self.elementos}")
    
    def limpiar(self):
        """Vacía la cola completamente."""
        self.elementos.clear()
        print("✓ Cola limpiada")


class ColaConPrioridad:
    """
    Extensión de Cola: Cola con Prioridad.
    Los elementos se ordenan por prioridad (menor número = mayor prioridad).
    """
    
    def __init__(self):
        """Inicializa una cola con prioridad vacía."""
        self.elementos = []
    
    def enqueue(self, elemento, prioridad=0):
        """
        Añade un elemento con su prioridad.
        
        Args:
            elemento: El elemento a añadir
            prioridad: Nivel de prioridad (0 = máxima prioridad)
        """
        self.elementos.append((elemento, prioridad))
        self.elementos.sort(key=lambda x: x[1])  # Ordenar por prioridad
        print(f"✓ {elemento} (prioridad: {prioridad}) añadido")
    
    def dequeue(self):
        """
        Elimina el elemento con mayor prioridad.
        
        Returns:
            Tupla (elemento, prioridad)
        """
        if self.esta_vacia():
            print("❌ Error: La cola está vacía")
            return None
        
        elemento, prioridad = self.elementos.pop(0)
        print(f"✓ {elemento} (prioridad: {prioridad}) removido")
        return elemento, prioridad
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0
    
    def mostrar(self):
        """Muestra todos los elementos con sus prioridades."""
        if self.esta_vacia():
            print("Cola vacía: []")
        else:
            print("Cola con Prioridad:")
            for elemento, prioridad in self.elementos:
                print(f"  - {elemento} (prioridad: {prioridad})")


# ==================== EJEMPLOS DE USO ====================

def ejemplo_cola_basica():
    """Ejemplo 1: Operaciones básicas de una cola."""
    print("=" * 50)
    print("EJEMPLO 1: Cola Básica FIFO")
    print("=" * 50)
    
    cola = Cola()
    
    # Enqueue (insertar elementos)
    cola.enqueue("Cliente 1")
    cola.enqueue("Cliente 2")
    cola.enqueue("Cliente 3")
    cola.enqueue("Cliente 4")
    
    cola.mostrar()
    print(f"\nTamaño de la cola: {cola.tamaño()}")
    
    # Dequeue (extraer elementos)
    print("\nAtendiendo clientes:")
    cola.dequeue()
    cola.dequeue()
    
    cola.mostrar()
    print()


def ejemplo_banco():
    """Ejemplo 2: Simulación de un banco."""
    print("=" * 50)
    print("EJEMPLO 2: Cola en un Banco")
    print("=" * 50)
    
    banco = Cola()
    
    # Clientes llegando
    clientes = ["Juan", "María", "Pedro", "Ana", "Carlos"]
    
    print("Clientes llegando al banco:")
    for cliente in clientes:
        banco.enqueue(cliente)
    
    banco.mostrar()
    
    print("\nAtendimiento en cajas (FIFO):")
    while not banco.esta_vacia():
        cliente = banco.dequeue()
        print(f"  Caja 1 atendiendo a {cliente}")
    
    print()


def ejemplo_impresora():
    """Ejemplo 3: Cola de impresión."""
    print("=" * 50)
    print("EJEMPLO 3: Cola de Impresora")
    print("=" * 50)
    
    cola_impresion = Cola()
    
    documentos = ["documento1.pdf", "documento2.pdf", "documento3.pdf", "documento4.pdf"]
    
    print("Documentos enviados a imprimir:")
    for doc in documentos:
        cola_impresion.enqueue(doc)
    
    cola_impresion.mostrar()
    
    print("\nImprimiendo documentos:")
    contador = 1
    while not cola_impresion.esta_vacia():
        doc = cola_impresion.dequeue()
        print(f"  Impresora procesando: {doc}")
    
    print()


def ejemplo_cola_prioridad():
    """Ejemplo 4: Cola con prioridad (Urgencias en un hospital)."""
    print("=" * 50)
    print("EJEMPLO 4: Cola con Prioridad (Hospital)")
    print("=" * 50)
    
    urgencias = ColaConPrioridad()
    
    # Pacientes con sus niveles de urgencia (0=crítico, 1=grave, 2=moderado, 3=leve)
    pacientes = [
        ("Juan Pérez", 2),      # Moderado
        ("María García", 1),    # Grave
        ("Carlos López", 0),    # Crítico
        ("Ana Martínez", 3),    # Leve
        ("Pedro Sánchez", 1),   # Grave
    ]
    
    print("Pacientes llegando a urgencias:")
    for paciente, urgencia in pacientes:
        urgencias.enqueue(paciente, urgencia)
    
    urgencias.mostrar()
    
    print("\nAtendimiento por prioridad:")
    while not urgencias.esta_vacia():
        paciente, prioridad = urgencias.dequeue()
    
    print()


def ejercicio_interactivo():
    """Ejercicio interactivo: Crea tu propia cola."""
    print("=" * 50)
    print("EJERCICIO INTERACTIVO: Tu Cola")
    print("=" * 50)
    
    mi_cola = Cola()
    
    # Menú interactivo
    while True:
        print("\nOpciones:")
        print("1. Enqueue (insertar)")
        print("2. Dequeue (extraer)")
        print("3. Ver cola")
        print("4. Tamaño")
        print("5. Frente")
        print("6. Limpiar")
        print("7. Salir")
        
        opcion = input("\nElige una opción (1-7): ").strip()
        
        if opcion == "1":
            elemento = input("¿Qué elemento deseas insertar? ")
            mi_cola.enqueue(elemento)
        
        elif opcion == "2":
            mi_cola.dequeue()
        
        elif opcion == "3":
            mi_cola.mostrar()
        
        elif opcion == "4":
            print(f"Tamaño de la cola: {mi_cola.tamaño()}")
        
        elif opcion == "5":
            frente = mi_cola.frente()
            if frente:
                print(f"Elemento al frente: {frente}")
        
        elif opcion == "6":
            mi_cola.limpiar()
        
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    # Ejecutar ejemplos
    ejemplo_cola_basica()
    ejemplo_banco()
    ejemplo_impresora()
    ejemplo_cola_prioridad()
    
    # Descomenta la siguiente línea para el ejercicio interactivo
    # ejercicio_interactivo()
