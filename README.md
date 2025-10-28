# 🏠 Proyecto de Casa Domótica en Python

Bienvenido al proyecto **Casa Domótica**, un sistema inteligente desarrollado en **Python** para automatizar y controlar diferentes dispositivos del hogar, brindando **comodidad, eficiencia y seguridad**.

---

## 🚀 Descripción del Proyecto

Este proyecto simula (o implementa) un sistema de **automatización del hogar**, permitiendo gestionar de forma centralizada funciones como:

- Encendido y apagado de luces 💡  
- Control de temperatura y ventilación 🌡️  
- Seguridad mediante sensores de movimiento y puertas 🔒  
- Monitoreo y registro de eventos 📋  
- Interfaz de usuario sencilla y configurable 🖥️  

El objetivo principal es **demostrar la integración de sensores, actuadores y lógica de control** usando Python como núcleo del sistema.

---

## 🧩 Tecnologías Utilizadas

- **Python 3.10+**
- **GPIO / Simulación de sensores** (según el entorno)
- **Tkinter** o **Flask** (para interfaz gráfica o web)
- **JSON / SQLite** (para almacenamiento de datos)
- **Threading** y **time** (para procesos concurrentes)

---

## ⚙️ Estructura del Proyecto

📂 casa_domotica/
┣ 📜 main.py # Programa principal del sistema
┣ 📜 sensores.py # Módulo para simular o leer sensores
┣ 📜 actuadores.py # Control de luces, puertas, ventiladores, etc.
┣ 📜 interfaz.py # Interfaz gráfica o web
┣ 📜 config.json # Archivo de configuración
┗ 📁 logs/ # Registros de actividad del sistema

---

## 🧠 Funcionamiento General

1. **Inicio del sistema:** se cargan las configuraciones y se inicializan los dispositivos.  
2. **Lectura de sensores:** el programa monitorea constantemente el estado del entorno.  
3. **Procesamiento de datos:** se aplican reglas lógicas (por ejemplo, si hay movimiento y es de noche → encender luces).  
4. **Acción automática:** se activan los actuadores necesarios.  
5. **Registro y visualización:** se muestran los resultados en la interfaz y se guardan los eventos.

---

## 💡 Ejemplo de Uso

```bash
# Clonar el repositorio
git clone https://github.com/usuario/casa_domotica.git
cd casa_domotica

# Ejecutar el programa
python main.py
