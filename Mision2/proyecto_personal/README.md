# Procesador Excel con IA

> Herramienta de automatización de Excel mediante instrucciones en lenguaje natural, permitiendo limpieza de datos y unión de columnas de forma intuitiva.

---

## 📌 Tabla de Contenidos
- [Procesador Excel con IA](#procesador-excel-con-ia)
  - [📌 Tabla de Contenidos](#-tabla-de-contenidos)
  - [📖 Descripción General](#-descripción-general)
  - [🏗️ Arquitectura](#️-arquitectura)
  - [🛠️ Tecnologías](#️-tecnologías)
  - [⚙️ Instalación](#️-instalación)
  - [▶️ Uso](#️-uso)
  - [🧩 Estructura del Proyecto](#-estructura-del-proyecto)
  - [✅ Buenas Prácticas](#-buenas-prácticas)
  - [🔐 Seguridad](#-seguridad)
  - [🤝 Contribución](#-contribución)
  - [📄 Licencia](#-licencia)
  - [👨‍💻 Autor](#-autor)

---

## 📖 Descripción General
Este proyecto facilita la manipulación de archivos Excel para usuarios no técnicos. Utiliza una interfaz gráfica simple y un motor de procesamiento de lenguaje natural básico para interpretar comandos como "Limpia la columna A" o "Une columna A y B".
Soluciona problemas comunes de formateo de datos y concatenación sin necesidad de fórmulas complejas.

## 🏗️ Arquitectura
El sistema sigue el patrón Modelo-Vista-Controlador (MVC) simplificado:
- **Vista (UI)**: Interfaz Tkinter para entrada de usuario y selección de archivos.
- **Controlador**: Gestiona la comunicación entre la UI, el intérprete de comandos y el procesador de datos.
- **Servicios**:
    - `ia_service`: Interpreta texto a comandos estructurados.
    - `processor`: Ejecuta la lógica sobre el archivo Excel usando OpenPyXL.

```text
📦 proyecto_personal
 ┣ 📂 src/
 ┃ ┣ 📄 controller.py
 ┃ ┣ 📄 ia_service.py
 ┃ ┣ 📄 processor.py
 ┃ ┗ 📄 ui.py
 ┣ 📂 docs/
 ┃ ┗ 📄 ejemplo.xlsx
 ┣ 📂 tests/
 ┣ 📄 main.py
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

## 🛠️ Tecnologías
- **Python 3.10+**
- **Tkinter**: Interfaz gráfica nativa.
- **OpenPyXL**: Manipulación de archivos Excel.
- **Regex**: Procesamiento de lenguaje natural basado en reglas.

## ⚙️ Instalación
1. Asegúrese de estar en el entorno virtual activo (carpeta raíz Mision2).
2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

## ▶️ Uso
1. Ejecute la aplicación:
```bash
python main.py
```
2. En la interfaz:
    - Seleccione un archivo Excel (`.xlsx`) usando el botón "Seleccionar Archivo".
    - Escriba una instrucción, por ejemplo:
        - `Limpia columna A` (Deja solo números).
        - `Une columna A y columna B` (Une en una nueva columna).
        - `Une columna A y columna B en columna D`.
    - Haga clic en "**EJECUTAR**".

## 🧩 Estructura del Proyecto
- `src/`: Código fuente de la aplicación.
- `docs/`: Documentación y archivos de ejemplo.
- `main.py`: Punto de entrada.

## ✅ Buenas Prácticas
- Clean Code y nomenclatura descriptiva.
- Separación de lógica de negocio y presentación.
- Manejo de excepciones en operaciones de archivo.

## 🔐 Seguridad
- Validación de rutas de archivo antes de la ejecución.
- Ejecución local sin envío de datos a servidores externos.

## 🤝 Contribución
Las contribuciones son bienvenidas.

## 📄 Licencia
Propiedad del usuario.

## 👨‍💻 Autor
**Cristian Camilo Londoño Ospina**  
Estudiante desarrollo software | Desarrollador 
📧 cristianclondonoo@gmail.com  
📱 310 597 8216

---
_Este proyecto sigue estándares profesionales de documentación y desarrollo de software._
