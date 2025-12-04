# Proyecto de Prácticas en Python + Proyecto ESP32 Car Robot

Este repositorio contiene una serie de ejercicios de Python ampliados y mejorados, junto con un proyecto extra que incluye el control de un **carro robótico con ESP32** usando MicroPython.  
El objetivo es practicar programación estructurada, manejo de errores, procesamiento de texto, ciclos, validaciones y control de hardware con microcontroladores.

---

## 📂 Contenido del Repositorio

### 🐍 **1. Ejercicios de Python Mejorados**
Incluye programas enfocados en:

- Validación de entradas y manejo de excepciones.
- Uso de ciclos `for` y `while`.
- Procesamiento avanzado de cadenas.
- Generación de reportes y estadísticas simples.
- Menús interactivos.
- Manipulación de listas.
- Cálculos matemáticos.
- Programas de seguridad (evaluación de contraseñas).
- Formateo de nombres y textos.

Cada ejercicio está expandido y estructurado para facilitar lectura y reutilización.

---

## 🚗 **2. Proyecto: Carro Robótico con ESP32 (MicroPython)**

Este proyecto consiste en controlar un pequeño vehículo robótico con un ESP32 utilizando MicroPython.  
Incluye:

### 🔧 **Hardware necesario**
- ESP32 DevKit
- Driver de motores L298N o L9110S
- 2 motores DC
- Batería Li-ion o pack AA
- Protoboard y cables dupont

### 💻 **Archivos incluidos**
- `main.py` – Lógica principal del vehículo
- `motor.py` – Controlador de motores en MicroPython
- `config.py` – Pines configurables del ESP32

### 🧠 **Funciones que implementa**
- Avanzar, retroceder, girar izquierda/derecha
- Parar de emergencia
- Control por comandos seriales
- Modo automático básico (patrón de movimiento)

---

## 🚀 **Ejecución del Proyecto ESP32**

### 1. Instalar MicroPython en el ESP32
Puedes usar:
- **esptool**
- **Thonny IDE**
- **uPyCraft**

### 2. Subir los archivos
Con Thonny:


---

## 🧪 Requisitos

### Para Python:
- Python 3.8+
- No se requieren librerías externas

### Para ESP32:
- MicroPython firmware 1.19 o superior

---

## 📝 Notas
Este repositorio puede crecer conforme agregues más prácticas o expandas el proyecto del ESP32.

Si deseas agregar control vía WiFi (webserver), Bluetooth clásico o BLE, también puedo ayudarte a extenderlo.

---

## 🧑‍💻 Autor
Proyecto estructurado con apoyo de ChatGPT (OpenAI).  
Ejercicios desarrollados por **Ruben Reyes**.

"""
# 🚗 Proyecto: Carro Robótico con ESP32 + L293D  
Control de un vehículo de dos motores mediante una ESP32, usando el driver L293D y una app móvil para enviar comandos remotos.

---

## 🧩 ¿Cómo funciona el sistema?

Un carro diferencial utiliza **dos motores DC independientes**:
- **Motor izquierdo (M1)**
- **Motor derecho (M2)**

Dependiendo de cómo giren, el carro puede avanzar, retroceder o girar:

- ▶️ **Avanzar**: ambos motores hacia adelante  
- ◀️ **Retroceder**: ambos motores hacia atrás  
- ↱ **Giro izquierda**: motor derecho avanza, izquierdo se detiene  
- ↰ **Giro derecha**: motor izquierdo avanza, derecho se detiene  
- ⏹️ **Detener**: ambos motores apagados  

---

## 🔌 Conexión ESP32 → L293D → Motores

El L293D permite controlar dos motores DC usando un puente H.  
Conexiones típicas:

| ESP32 | L293D |
|-------|--------|
| GPIO18 | IN1 |
| GPIO19 | IN2 |
| GPIO21 | IN3 |
| GPIO22 | IN4 |
| 5V     | Vcc1 (lógica) |
| Batería 6–12V | Vcc2 (motores) |
| GND (común) | GND |

---

## 📡 Control desde el celular

El ESP32 puede recibir comandos vía **Bluetooth** o **WiFi**.  
Comandos típicos enviados desde una app:

| Comando | Acción |
|---------|---------|
| F | Forward |
| B | Backward |
| L | Left |
| R | Right |
| S | Stop |

El ESP32 interpreta estos comandos y activa los pines correspondientes del L293D.

---

## 🧠 Código de ejemplo (MicroPython)

Este código controla la dirección del carro:

```python
from machine import Pin
import time

IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(21, Pin.OUT)
IN4 = Pin(22, Pin.OUT)

def stop():
    IN1.value(0); IN2.value(0)
    IN3.value(0); IN4.value(0)

def forward():
    IN1.value(1); IN2.value(0)
    IN3.value(1); IN4.value(0)

def backward():
    IN1.value(0); IN2.value(1)
    IN3.value(0); IN4.value(1)

def left():
    IN1.value(0); IN2.value(0)
    IN3.value(1); IN4.value(0)

def right():
    IN1.value(1); IN2.value(0)
    IN3.value(0); IN4.value(0)


## 💡 Ejemplo de Uso

```bash
# Clonar el repositorio
git clone https://github.com/usuario/casa_domotica.git
cd casa_domotica

# Ejecutar el programa
python main.py
