#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BLOG TÉCNICO: ESTRUCTURA DE DATOS GRAFOS
✨ Guía de Inicio Rápido ✨

Este script te ayuda a explorar el proyecto desde la línea de comandos.
"""

import os
import sys
from pathlib import Path


def mostrar_banner():
    """Mostrar banner principal"""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║   📊 BLOG TÉCNICO: ESTRUCTURA DE DATOS GRAFOS             ║
    ║                                                            ║
    ║   Conceptos, Implementaciones y Aplicaciones Reales       ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)


def listar_archivos():
    """Listar archivos principales del proyecto"""
    print("\n📁 ARCHIVOS DEL PROYECTO")
    print("─" * 60)
    
    archivos = {
        "📄 Documentación": [
            ("README.md", "Documentación completa del proyecto"),
            ("GITHUB_PAGES.md", "Guía para publicar en GitHub Pages"),
            ("PROYECTO_COMPLETADO.txt", "Resumen de lo completado"),
        ],
        "🌐 Sitio Web": [
            ("index.html", "Página principal del blog"),
            ("css/style.css", "Estilos CSS modernos"),
            ("posts/introduccion-grafos.html", "Post 1: Introducción"),
            ("posts/representacion-grafos.html", "Post 2: Representación"),
            ("posts/algoritmos-recorrido.html", "Post 3: Algoritmos BFS/DFS"),
            ("posts/cola.html", "Post 4: Estructura Cola"),
        ],
        "🐍 Python": [
            ("cola.py", "Implementación de Cola FIFO"),
            ("grafos.py", "Implementación de Grafos"),
            ("ejemplos_practicos.py", "Ejemplos de aplicaciones reales"),
        ],
        "⚙️ Configuración": [
            (".gitignore", "Archivos ignorados por Git"),
            ("requirements.txt", "Dependencias del proyecto"),
        ],
    }
    
    for seccion, items in archivos.items():
        print(f"\n{seccion}")
        for archivo, descripcion in items:
            print(f"  ✓ {archivo:40s} - {descripcion}")


def mostrar_menu():
    """Mostrar menú de opciones"""
    print("\n\n🎯 ACCIONES DISPONIBLES")
    print("─" * 60)
    
    opciones = [
        ("1", "Ejecutar ejemplos de Cola", "python cola.py"),
        ("2", "Ejecutar ejemplos de Grafos", "python grafos.py"),
        ("3", "Ejecutar ejemplos prácticos", "python ejemplos_practicos.py"),
        ("4", "Abrir página principal (navegador)", "start index.html"),
        ("5", "Ver documentación", "cat README.md"),
        ("6", "Ver guía GitHub Pages", "cat GITHUB_PAGES.md"),
        ("7", "Listar archivos Python", "dir *.py"),
        ("8", "Listar posts HTML", "dir posts/*.html"),
        ("9", "Mostrar este menú", ""),
        ("0", "Salir", ""),
    ]
    
    for num, descripcion, comando in opciones:
        print(f"  {num} - {descripcion}")


def ejecutar_comando(opcion):
    """Ejecutar comando según opción seleccionada"""
    comandos = {
        "1": lambda: os.system("python cola.py"),
        "2": lambda: os.system("python grafos.py"),
        "3": lambda: os.system("python ejemplos_practicos.py"),
        "4": lambda: os.system("start index.html"),
        "5": lambda: os.system("type README.md | more"),
        "6": lambda: os.system("type GITHUB_PAGES.md | more"),
        "7": lambda: os.system("dir *.py"),
        "8": lambda: os.system("dir posts\\*.html"),
        "9": lambda: mostrar_menu(),
        "0": lambda: (print("\n👋 ¡Hasta luego!"), exit(0)),
    }
    
    if opcion in comandos:
        comandos[opcion]()
    else:
        print("❌ Opción inválida")


def mostrar_estadisticas():
    """Mostrar estadísticas del proyecto"""
    print("\n📊 ESTADÍSTICAS DEL PROYECTO")
    print("─" * 60)
    
    stats = {
        "Artículos HTML": 4,
        "Archivos Python": 3,
        "Líneas de código Python": "~500",
        "Líneas de HTML/CSS": "~1500",
        "Ejemplos de código": "15+",
        "Diagramas visuales": "10+",
        "Tablas comparativas": "5+",
        "Aplicaciones demostradas": 6,
    }
    
    for metrica, valor in stats.items():
        print(f"  • {metrica:.<40s} {str(valor):>15s}")


def mostrar_contenido():
    """Mostrar contenido del blog"""
    print("\n📚 CONTENIDO DEL BLOG")
    print("─" * 60)
    
    posts = [
        ("1. Introducción a los Grafos", [
            "Definición de grafo",
            "Conceptos clave (nodos, aristas, etc.)",
            "Tipos de grafos",
            "Aplicaciones prácticas",
        ]),
        ("2. Representación de Grafos", [
            "Lista de Adyacencia",
            "Matriz de Adyacencia",
            "Comparativa y análisis",
            "Código Python",
        ]),
        ("3. Algoritmos de Recorrido", [
            "BFS (Breadth-First Search)",
            "DFS (Depth-First Search)",
            "Análisis de complejidad",
            "Implementaciones",
        ]),
        ("4. Cola (Queue) - FIFO", [
            "Definición y operaciones",
            "Implementación en Python",
            "Cola con Prioridad",
            "Aplicaciones en BFS",
        ]),
    ]
    
    for titulo, temas in posts:
        print(f"\n{titulo}")
        for tema in temas:
            print(f"  → {tema}")


def main():
    """Función principal"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    mostrar_banner()
    listar_archivos()
    mostrar_estadisticas()
    mostrar_contenido()
    
    print("\n\n🚀 PRÓXIMOS PASOS")
    print("─" * 60)
    print("""
  1. Explora el código:
     - Lee la documentación en README.md
     - Ejecuta los ejemplos de Python
     - Abre el blog en tu navegador

  2. Publica en GitHub Pages:
     - Lee GITHUB_PAGES.md
     - Crea un repositorio en GitHub
     - Sube el código
     - ¡Tu blog estará online!

  3. Aprende:
     - Estudia los conceptos en el blog
     - Lee el código Python
     - Modifica y experimenta
     - Crea tus propios ejemplos
    """)
    
    mostrar_menu()
    
    print("\n\n" + "─" * 60)
    print("Ingresa el número de la opción que deseas:")
    
    while True:
        try:
            opcion = input("\n➜ ").strip()
            if opcion:
                ejecutar_comando(opcion)
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        sys.exit(0)
