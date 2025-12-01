# 🧠 Juego Interactivo de Matemáticas Discretas

Aplicación web interactiva desarrollada con Streamlit para practicar y evaluar conocimientos en Matemáticas Discretas.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Inicio Rápido](#inicio-rápido)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso de la Aplicación](#uso-de-la-aplicación)
- [Formato de Preguntas](#formato-de-preguntas)
- [Cómo se Construyó](#cómo-se-construyó)
- [Extender el Banco de Preguntas](#extender-el-banco-de-preguntas)
- [Documentación Adicional](#documentación-adicional)

## 🚀 Inicio Rápido

¿Quieres empezar inmediatamente? Consulta la [Guía de Inicio Rápido](QUICKSTART.md).

**TL;DR**:
```bash
# Instalar UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clonar y ejecutar
git clone https://github.com/tu-usuario/discrete-app.git
cd discrete-app
./run.sh  # Linux/macOS
# o run.bat en Windows
```

## ✨ Características

### Modos de Práctica

1. **Modo Práctica por Tema**
   - Selección de tema específico
   - Configuración de cantidad de preguntas (3-10)
   - Sorteo aleatorio de preguntas
   - Ideal para enfocarse en un área específica

2. **Modo Examen**
   - Evaluación integral de todos los temas
   - Una pregunta aleatoria por tema
   - Orden aleatorio de presentación
   - Perfecto para autoevaluación general

### Funcionalidades

- ✅ **Navegación flexible**: Avanza y retrocede entre preguntas
- 📊 **Resultados detallados**: Tabla interactiva con resumen de respuestas
- 🎯 **Retroalimentación inmediata**: Conoce tu resultado al responder
- 📈 **Métricas de desempeño**: Visualización de correctas, incorrectas y porcentaje
- 🔄 **Reintentar**: Practica cuantas veces quieras
- 📚 **Temas cubiertos**:
  - Proposiciones
  - Operadores Lógicos
  - Tautologías y Contradicciones
  - Implicaciones Lógicas
  - Cuantificadores
  - Interpretación de Cuantificadores

## 💻 Requisitos del Sistema

### Software Necesario

- **Python**: Versión 3.11 o superior
- **uv**: Gestor de paquetes y entornos virtuales de Python (recomendado)
  - Alternativa: pip y venv tradicional

### Dependencias de Python

Las siguientes librerías se instalan automáticamente:

- `streamlit>=1.35,<2`: Framework web para la interfaz
- `pandas>=2.0,<3`: Manejo de datos tabulares
- `pandas-stubs>=2.0`: Type hints para pandas (desarrollo)

## 🚀 Instalación

### Opción 1: Usando UV (Recomendado)

UV es un gestor de paquetes moderno y rápido para Python.

1. **Instalar UV** (si no lo tienes):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Clonar el repositorio**:

```bash
git clone https://github.com/tu-usuario/discrete-app.git
cd discrete-app
```

3. **Crear entorno virtual e instalar dependencias**:

```bash
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
uv sync
```

### Opción 2: Usando pip tradicional

1. **Clonar el repositorio**:

```bash
git clone https://github.com/tu-usuario/discrete-app.git
cd discrete-app
```

2. **Crear entorno virtual**:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instalar dependencias**:

```bash
pip install streamlit pandas pandas-stubs
```

## ▶️ Ejecución

### Con UV

```bash
# Asegúrate de estar en el directorio del proyecto
cd discrete-app

# Activa el entorno virtual (si no está activado)
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Ejecuta la aplicación
uv run streamlit run app/ui.py
```

### Con pip tradicional

```bash
# Asegúrate de estar en el directorio del proyecto
cd discrete-app

# Activa el entorno virtual (si no está activado)
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Ejecuta la aplicación
streamlit run app/ui.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
discrete-app/
├── app/
│   ├── __init__.py          # Marca el directorio como paquete Python
│   ├── ui.py                # Interfaz de usuario con Streamlit
│   ├── logic.py             # Lógica de evaluación de respuestas
│   └── utils.py             # Utilidades (carga de datos, formateo)
├── data/
│   └── questions.json       # Banco de preguntas por tema
├── .venv/                   # Entorno virtual (generado)
├── main.py                  # Script principal alternativo
├── pyproject.toml           # Configuración del proyecto y dependencias
├── uv.lock                  # Lock file de dependencias (UV)
├── .gitignore               # Archivos ignorados por Git
├── .python-version          # Versión de Python del proyecto
└── README.md                # Este archivo
```

### Descripción de Componentes

#### `app/ui.py`
- Punto de entrada de la aplicación Streamlit
- Maneja la interfaz de usuario y navegación
- Gestiona el estado de la sesión
- Implementa los modos de práctica y examen
- Renderiza preguntas y resultados

#### `app/logic.py`
- Funciones de evaluación por tipo de pregunta:
  - `evaluate_single_choice()`: Opción única
  - `evaluate_multiple_choice()`: Opción múltiple
  - `evaluate_true_false()`: Verdadero/Falso
  - `evaluate_free_input()`: Respuesta libre
- `compute_score()`: Calcula puntaje total y detalle

#### `app/utils.py`
- `load_questions()`: Carga y valida el JSON de preguntas
- `get_topics()`: Obtiene lista de temas disponibles
- `get_questions_for_topic()`: Filtra preguntas por tema con opciones de sorteo
- `get_exam_questions()`: Genera examen con una pregunta por tema
- `format_correct_answer_display()`: Formatea respuestas para mostrar
- `_validate_question_schema()`: Validación de estructura de preguntas

#### `data/questions.json`
- Banco de preguntas estructurado por temas
- Formato JSON con validación automática
- Fácilmente extensible sin modificar código

## 📖 Uso de la Aplicación

### Modo Práctica por Tema

1. En la barra lateral, selecciona **"Práctica por tema"**
2. Elige un tema del menú desplegable
3. Ajusta el número de preguntas (3-10) con el slider
4. Presiona **"Iniciar"**
5. Responde cada pregunta y navega con los botones
6. Al finalizar, revisa tus resultados en la tabla interactiva

### Modo Examen

1. En la barra lateral, selecciona **"Examen (1 de cada tema)"**
2. Presiona **"Iniciar"**
3. Responde las preguntas (una de cada tema disponible)
4. Al finalizar, revisa tu desempeño general

### Navegación

- **Anterior**: Vuelve a la pregunta previa
- **Siguiente**: Avanza a la siguiente pregunta
- **Finalizar**: Completa el cuestionario (última pregunta)
- **Reintentar**: Comienza de nuevo (en barra lateral)

### Resultados

Después de finalizar, verás:

- **Métricas**: Correctas, incorrectas y porcentaje
- **Tabla resumen**: Vista rápida de todas las respuestas
- **Detalle expandible**: Información completa de cada pregunta
- **Retroalimentación**: Mensaje según tu desempeño

## 📝 Formato de Preguntas

El archivo `data/questions.json` sigue esta estructura:

```json
{
  "topics": {
    "Nombre del Tema": [
      {
        "type": "single",
        "question": "¿Texto de la pregunta?",
        "options": ["Opción A", "Opción B", "Opción C"],
        "answer": 0
      }
    ]
  }
}
```

### Tipos de Preguntas Soportados

#### 1. Opción Única (`single`)

```json
{
  "type": "single",
  "question": "¿Es una proposición? 'Hoy es lunes'",
  "options": ["Sí, es proposición", "No, no es proposición"],
  "answer": 0
}
```

- `answer`: Índice de la opción correcta (base 0)

#### 2. Opción Múltiple (`multiple`)

```json
{
  "type": "multiple",
  "question": "Selecciona los operadores lógicos:",
  "options": ["∧", "∨", "+", "¬"],
  "answer": [0, 1, 3]
}
```

- `answer`: Lista de índices de opciones correctas

#### 3. Verdadero/Falso (`tf`)

```json
{
  "type": "tf",
  "question": "p ∨ ¬p es una tautología",
  "answer": true
}
```

- `answer`: Booleano (`true` o `false`)

#### 4. Respuesta Libre (`input`)

```json
{
  "type": "input",
  "question": "¿Cuál es la negación de ∀x P(x)?",
  "answer": "∃x ¬P(x)"
}
```

- `answer`: String (comparación case-insensitive)

## 🔧 Cómo se Construyó

### Arquitectura

La aplicación sigue una arquitectura modular de tres capas:

1. **Capa de Presentación** (`ui.py`):
   - Framework: Streamlit
   - Gestión de estado con `st.session_state`
   - Renderizado dinámico de componentes
   - Estilos CSS personalizados

2. **Capa de Lógica** (`logic.py`):
   - Evaluación independiente por tipo de pregunta
   - Funciones puras sin efectos secundarios
   - Cálculo de puntajes y estadísticas

3. **Capa de Datos** (`utils.py`):
   - Carga y validación de JSON
   - Transformación de datos
   - Funciones de utilidad reutilizables

### Decisiones de Diseño

#### ¿Por qué Streamlit?

- **Rapidez de desarrollo**: Interfaz web sin HTML/CSS/JS
- **Interactividad nativa**: Componentes reactivos integrados
- **Python puro**: Sin cambio de lenguaje
- **Despliegue sencillo**: Compatible con Streamlit Cloud

#### ¿Por qué UV?

- **Velocidad**: 10-100x más rápido que pip
- **Gestión unificada**: Entornos y paquetes en una herramienta
- **Lock file**: Reproducibilidad garantizada
- **Moderno**: Escrito en Rust, compatible con estándares Python

#### Gestión de Estado

Streamlit re-ejecuta el script completo en cada interacción. Usamos `st.session_state` para persistir:

- Tema seleccionado
- Índice de pregunta actual
- Respuestas del usuario
- Estado de finalización
- Modo de práctica (tema/examen)

#### Validación de Datos

El módulo `utils.py` valida automáticamente:

- Existencia de archivo JSON
- Estructura de temas y preguntas
- Tipos de pregunta válidos
- Coherencia de opciones y respuestas
- Índices dentro de rango

### Flujo de Ejecución

```
1. Usuario inicia app → ui.py carga
2. init_state() → Inicializa session_state
3. load_questions() → Carga y valida JSON
4. Usuario selecciona modo/tema → Actualiza estado
5. get_questions_for_topic() → Filtra y sortea preguntas
6. render_question() → Muestra pregunta actual
7. Usuario responde → Guarda en responses[]
8. evaluate_question() → Valida respuesta
9. Usuario finaliza → compute_score()
10. Muestra resultados → Tabla + detalle
```

### Tecnologías Utilizadas

- **Python 3.11+**: Lenguaje base
- **Streamlit 1.35+**: Framework web
- **Pandas 2.0+**: Tablas de resultados
- **JSON**: Almacenamiento de preguntas
- **UV**: Gestión de dependencias
- **Git**: Control de versiones

## 🔄 Extender el Banco de Preguntas

### Agregar un Nuevo Tema

Edita `data/questions.json`:

```json
{
  "topics": {
    "Tema Existente": [...],
    "Nuevo Tema": [
      {
        "type": "single",
        "question": "¿Primera pregunta del nuevo tema?",
        "options": ["A", "B", "C"],
        "answer": 0
      }
    ]
  }
}
```

### Agregar Preguntas a Tema Existente

Simplemente añade objetos al array del tema:

```json
{
  "topics": {
    "Proposiciones": [
      {...},
      {...},
      {
        "type": "tf",
        "question": "Nueva pregunta",
        "answer": true
      }
    ]
  }
}
```

### Validación Automática

La aplicación validará automáticamente:

- ✅ Estructura JSON correcta
- ✅ Tipos de pregunta válidos
- ✅ Campos requeridos presentes
- ✅ Índices de respuestas válidos

Si hay errores, se mostrará un mensaje claro en la interfaz.

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado como proyecto educativo para la práctica de Matemáticas Discretas.

## 📚 Documentación Adicional

- **[QUICKSTART.md](QUICKSTART.md)**: Guía de inicio rápido en 3 pasos
- **[COMPONENTES.md](COMPONENTES.md)**: Documentación técnica detallada de componentes y requerimientos
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Guía para contribuir al proyecto

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee nuestra [Guía de Contribución](CONTRIBUTING.md) para más detalles.

Formas de contribuir:
- 🐛 Reportar bugs
- 💡 Sugerir características
- 📝 Mejorar documentación
- ✨ Agregar preguntas
- 🔧 Enviar código

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor abre un issue en el repositorio de GitHub.

## 📜 Changelog

### v0.1.0 (Diciembre 2024)

**Características iniciales**:
- ✨ Modo práctica por tema con selección de cantidad (3-10 preguntas)
- ✨ Modo examen (1 pregunta por tema)
- ✨ Sorteo aleatorio de preguntas
- 📊 Tabla interactiva de resultados con pandas
- 🎯 Retroalimentación inmediata
- 📈 Métricas de desempeño
- 🔄 Navegación flexible entre preguntas
- 📚 6 temas cubiertos con múltiples preguntas

## 🙏 Agradecimientos

Desarrollado como proyecto educativo para facilitar el aprendizaje de Matemáticas Discretas.

---

**¡Disfruta practicando Matemáticas Discretas! 🎓**
