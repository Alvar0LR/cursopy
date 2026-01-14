# 🐳 Mini Servidor Web PHP + Apache (Docker)

Este entorno levanta un servidor **Apache + PHP 7.0** en un contenedor Docker, usando el archivo `index.php` como punto de entrada.

---

## 🚀 Cómo levantar el servidor

Desde la carpeta `fs`:

```bash
# Construir la imagen (solo la primera vez o si modificas algo)
docker build . -t web_server

# Ejecutar el contenedor
docker run -dit -p 80:80 web_server
