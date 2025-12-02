# 🚀 Instrucciones para GitHub Pages

Este documento explica cómo publicar tu blog en GitHub Pages.

## Requisitos Previos

- Cuenta de GitHub
- Git instalado en tu computadora
- Acceso a línea de comandos (Terminal/PowerShell)

## Pasos para Publicar

### 1. Crear un repositorio en GitHub

1. Abre https://github.com/new
2. Completa los datos:
   - **Repository name**: `blog_grafos` o el nombre que desees
   - **Description**: "Blog técnico sobre estructura de datos: Grafos"
   - **Visibility**: Public (para que sea visible)
3. Haz clic en "Create repository"

### 2. Inicializar Git en tu proyecto local

```powershell
cd "c:\Users\nandr\OneDrive\Escritorio\UNIVERSIDAD\ESTRUCTURA DE DATOS II\blog_grafos"
git init
git add .
git commit -m "Commit inicial: Blog sobre Grafos"
```

### 3. Conectar con GitHub

Copia el comando de GitHub (aparece después de crear el repo) y ejecuta:

```powershell
git branch -M main
git remote add origin https://github.com/[tu-usuario]/blog_grafos.git
git push -u origin main
```

Reemplaza `[tu-usuario]` con tu nombre de usuario de GitHub.

### 4. Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Haz clic en "Settings" → "Pages"
3. Bajo "Source" selecciona:
   - Branch: `main`
   - Folder: `/ (root)`
4. Haz clic en "Save"

### 5. Esperar a que se construya

GitHub tardará 1-2 minutos en procesar. Verás un mensaje de éxito.

## Tu URL será:

```
https://[tu-usuario].github.io/blog_grafos
```

## Actualizar el Blog

Cada vez que hagas cambios:

```powershell
git add .
git commit -m "Descripción del cambio"
git push
```

Los cambios se publicarán automáticamente.

## Configuración Adicional (Opcional)

### Custom Domain

Si tienes un dominio propio, puedes configurarlo en Settings → Pages.

### HTTPS

GitHub Pages habilita HTTPS automáticamente. ✓

### Tema (Opcional)

GitHub Pages puede aplicar temas Jekyll, pero este blog usa CSS personalizado.
Para mantener tu CSS personalizado, asegúrate de que la carpeta está en root.

## Estructura Esperada

```
blog_grafos/
├── .git/                    # (creado por git)
├── .gitignore
├── index.html              # ← Página principal
├── README.md
├── requirements.txt
├── cola.py
├── grafos.py
├── css/
│   └── style.css
├── posts/
│   ├── introduccion-grafos.html
│   ├── representacion-grafos.html
│   ├── algoritmos-recorrido.html
│   └── cola.html
└── GITHUB_PAGES.md        # Este archivo
```

## Solución de Problemas

### "Pushed but page hasn't deployed"

- Espera 2-3 minutos
- Refresca la página en tu navegador (Ctrl+Shift+R para limpiar cache)
- Verifica que `index.html` esté en la raíz

### "404 - Page not found"

- Asegúrate de que el repositorio es **público**
- Verifica que Pages esté habilitado
- Comprueba que el nombre del rama es `main` (no `master`)

### Links rotos

- Los links deben ser relativos: `posts/archivo.html` no `/posts/archivo.html`
- Verifica que no haya espacios en los nombres de archivos

## Verificar que Todo Funciona

1. **Localmente**: Abre `index.html` en tu navegador
   ```powershell
   start .\index.html
   ```

2. **En GitHub Pages**: Visita tu URL después de que se publique

## Recursos

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Configurar GitHub Pages](https://docs.github.com/es/pages/getting-started-with-github-pages)
- [Troubleshooting GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-common-issues-with-github-pages)

---

**Nota**: El proyecto es un sitio estático HTML/CSS. No necesita compilación ni servidor. GitHub Pages lo sirve directamente.

**¡Tu blog estará disponible para el mundo entero!** 🌍
