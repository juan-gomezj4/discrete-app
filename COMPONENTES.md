# 📦 Documentación de Componentes y Requerimientos

## Componentes del Sistema

### 1. Frontend - Interfaz de Usuario

#### Streamlit (`app/ui.py`)

**Propósito**: Proporcionar la interfaz web interactiva para la aplicación.

**Componentes principales**:

- **Configuración de página**:
  ```python
  st.set_page_config(page_title=APP_TITLE, page_icon="🧠", layout="centered")
  ```
  - Define título, icono y diseño de la página

- **Gestión de estado** (`st.session_state`):
  - `topic`: Tema seleccionado o "Examen"
  - `current_idx`: Índice de pregunta actual
  - `responses`: Lista de respuestas del usuario
  - `finished`: Booleano de finalización
  - `data`: Datos cargados del JSON
  - `mode`: Modo de práctica ("practice" o "exam")
  - `questions_count`: Cantidad de preguntas configuradas

- **Componentes UI utilizados**:
  - `st.sidebar`: Panel lateral de control
  - `st.radio()`: Selector de modo y opciones
  - `st.selectbox()`: Selector de tema
  - `st.slider()`: Selector de cantidad de preguntas
  - `st.button()`: Botones de acción
  - `st.checkbox()`: Preguntas de opción múltiple
  - `st.text_input()`: Preguntas de respuesta libre
  - `st.dataframe()`: Tabla interactiva de resultados
  - `st.metric()`: Métricas de desempeño
  - `st.progress()`: Barra de progreso
  - `st.expander()`: Secciones expandibles

- **Estilos CSS personalizados**:
  - Paleta de colores consistente
  - Badges para etiquetas
  - Cards para preguntas
  - Estilos para botones primarios

### 2. Backend - Lógica de Negocio

#### Módulo de Evaluación (`app/logic.py`)

**Propósito**: Evaluar respuestas del usuario y calcular puntajes.

**Funciones principales**:

1. **`evaluate_single_choice(user_answer, correct_index)`**
   - Evalúa preguntas de opción única
   - Compara índice seleccionado con índice correcto
   - Retorna: `bool`

2. **`evaluate_multiple_choice(user_answers, correct_indices)`**
   - Evalúa preguntas de opción múltiple
   - Compara conjuntos de índices
   - Retorna: `bool`

3. **`evaluate_true_false(user_answer, correct_value)`**
   - Evalúa preguntas de verdadero/falso
   - Compara booleanos
   - Retorna: `bool`

4. **`evaluate_free_input(user_answer, correct_text)`**
   - Evalúa respuestas libres
   - Comparación case-insensitive y sin espacios externos
   - Retorna: `bool`

5. **`evaluate_question(q, user_response)`**
   - Función genérica que delega según tipo
   - Soporta: "single", "multiple", "tf", "input"
   - Retorna: `bool`

6. **`compute_score(questions, responses)`**
   - Calcula puntaje total
   - Genera detalle por pregunta
   - Retorna: `Dict` con "total", "correct", "detail"

#### Módulo de Utilidades (`app/utils.py`)

**Propósito**: Carga de datos, validación y transformaciones.

**Funciones principales**:

1. **`load_questions(json_path)`**
   - Carga archivo JSON de preguntas
   - Valida estructura básica
   - Llama a `_validate_question_schema()`
   - Retorna: `Dict` con estructura de temas
   - Lanza: `FileNotFoundError`, `ValueError`

2. **`get_topics(data)`**
   - Extrae lista de temas disponibles
   - Retorna: `List[str]`

3. **`get_questions_for_topic(data, topic, max_questions, shuffle)`**
   - Filtra preguntas por tema
   - Sortea aleatoriamente si `shuffle=True`
   - Limita cantidad si `max_questions > 0`
   - Retorna: `List[Dict]`

4. **`get_exam_questions(data)`**
   - Selecciona una pregunta aleatoria por tema
   - Agrega metadato `_topic` a cada pregunta
   - Sortea orden de presentación
   - Retorna: `List[Dict]`

5. **`format_correct_answer_display(q)`**
   - Formatea respuesta correcta para mostrar
   - Convierte índices a textos legibles
   - Retorna: `str`

6. **`_validate_question_schema(data)`**
   - Valida estructura completa del JSON
   - Verifica tipos de pregunta válidos
   - Valida coherencia de opciones y respuestas
   - Lanza: `ValueError` con mensaje descriptivo

### 3. Datos - Almacenamiento

#### Banco de Preguntas (`data/questions.json`)

**Estructura**:

```json
{
  "topics": {
    "Tema1": [
      {
        "type": "single|multiple|tf|input",
        "question": "Texto de la pregunta",
        "options": ["A", "B", "C"],  // Solo para single/multiple
        "answer": 0 | [0,1] | true | "texto"
      }
    ]
  }
}
```

**Validaciones automáticas**:

- ✅ Archivo existe y es JSON válido
- ✅ Clave "topics" presente y es objeto
- ✅ Cada tema contiene lista de preguntas
- ✅ Cada pregunta es objeto con campos requeridos
- ✅ Tipo de pregunta es válido
- ✅ Campo "question" no está vacío
- ✅ Preguntas single/multiple tienen "options" no vacío
- ✅ Respuestas son del tipo correcto
- ✅ Índices están dentro de rango

## Requerimientos de Ejecución

### Requerimientos de Hardware

**Mínimos**:
- CPU: 1 core, 1 GHz
- RAM: 512 MB disponibles
- Disco: 100 MB libres
- Red: No requerida (app local)

**Recomendados**:
- CPU: 2+ cores
- RAM: 2 GB disponibles
- Disco: 500 MB libres

### Requerimientos de Software

#### Sistema Operativo

- **Linux**: Ubuntu 20.04+, Debian 10+, Fedora 35+, o equivalente
- **macOS**: 10.15 (Catalina) o superior
- **Windows**: 10 o 11 (64-bit)

#### Python

**Versión requerida**: 3.11 o superior

**Verificar instalación**:
```bash
python --version
# o
python3 --version
```

**Instalar Python** (si no está instalado):

- **Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install python3.11 python3.11-venv python3-pip
  ```

- **macOS** (con Homebrew):
  ```bash
  brew install python@3.11
  ```

- **Windows**:
  - Descargar desde [python.org](https://www.python.org/downloads/)
  - Marcar "Add Python to PATH" durante instalación

#### Gestor de Paquetes

**Opción 1: UV (Recomendado)**

**Instalación**:

- **Linux/macOS**:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- **Windows**:
  ```powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

**Verificar**:
```bash
uv --version
```

**Opción 2: pip (Incluido con Python)**

Viene preinstalado con Python 3.11+.

**Verificar**:
```bash
pip --version
```

### Dependencias de Python

Todas las dependencias se instalan automáticamente con `uv sync` o `pip install`:

#### Dependencias de Producción

1. **streamlit** (>=1.35, <2)
   - **Propósito**: Framework web para la interfaz
   - **Tamaño**: ~50 MB
   - **Dependencias transitivas**: 
     - altair (visualizaciones)
     - pandas (datos)
     - pillow (imágenes)
     - protobuf (serialización)
     - tornado (servidor web)
     - watchdog (recarga automática)

2. **pandas** (>=2.0, <3)
   - **Propósito**: Manejo de tablas de resultados
   - **Tamaño**: ~20 MB
   - **Dependencias transitivas**:
     - numpy (cálculos numéricos)
     - python-dateutil (fechas)
     - pytz (zonas horarias)

#### Dependencias de Desarrollo

3. **pandas-stubs** (>=2.0)
   - **Propósito**: Type hints para pandas (mejora autocompletado)
   - **Tamaño**: ~5 MB
   - **Opcional**: Solo para desarrollo con IDE

### Navegador Web

Cualquier navegador moderno:

- **Chrome/Chromium**: 90+
- **Firefox**: 88+
- **Safari**: 14+
- **Edge**: 90+

La aplicación se abre automáticamente en el navegador predeterminado.

## Arquitectura de Despliegue

### Despliegue Local (Desarrollo)

```
┌─────────────────┐
│   Navegador     │
│  localhost:8501 │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐
│  Streamlit      │
│  Server         │
│  (Python)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  app/ui.py      │
│  app/logic.py   │
│  app/utils.py   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ questions.json  │
└─────────────────┘
```

### Despliegue en Streamlit Cloud (Producción)

1. **Requisitos**:
   - Repositorio en GitHub
   - Cuenta en [share.streamlit.io](https://share.streamlit.io)

2. **Configuración**:
   - Archivo: `requirements.txt` o `pyproject.toml`
   - Python version: `.python-version`
   - Entry point: `app/ui.py`

3. **Pasos**:
   ```bash
   # 1. Crear requirements.txt desde pyproject.toml
   uv pip compile pyproject.toml -o requirements.txt
   
   # 2. Commit y push a GitHub
   git add .
   git commit -m "Preparar para despliegue"
   git push origin main
   
   # 3. En Streamlit Cloud:
   # - New app → From existing repo
   # - Seleccionar repo y rama
   # - Main file: app/ui.py
   # - Deploy!
   ```

## Variables de Entorno

La aplicación no requiere variables de entorno actualmente.

**Configurables** (opcional):

```bash
# Puerto personalizado (por defecto 8501)
export STREAMLIT_SERVER_PORT=8080

# Desactivar telemetría
export STREAMLIT_GATHER_USAGE_STATS=false

# Tema oscuro por defecto
export STREAMLIT_THEME_BASE="dark"
```

## Puertos de Red

- **8501**: Puerto por defecto de Streamlit
- **Alternativo**: Configurable con `--server.port`

**Verificar disponibilidad**:
```bash
# Linux/macOS
lsof -i :8501

# Windows
netstat -ano | findstr :8501
```

## Logs y Debugging

### Logs de Streamlit

**Ubicación**:
- Linux/macOS: `~/.streamlit/logs/`
- Windows: `%USERPROFILE%\.streamlit\logs\`

**Habilitar debug**:
```bash
streamlit run app/ui.py --logger.level=debug
```

### Errores Comunes

1. **Puerto ocupado**:
   ```
   Error: Port 8501 is already in use
   ```
   **Solución**: Usar puerto alternativo
   ```bash
   streamlit run app/ui.py --server.port=8502
   ```

2. **Módulo no encontrado**:
   ```
   ModuleNotFoundError: No module named 'streamlit'
   ```
   **Solución**: Activar entorno virtual
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **JSON inválido**:
   ```
   Error al cargar preguntas: ...
   ```
   **Solución**: Validar JSON en [jsonlint.com](https://jsonlint.com)

## Monitoreo de Rendimiento

### Métricas de Streamlit

Streamlit incluye métricas en la interfaz (esquina superior derecha):

- **Tiempo de ejecución**: Tiempo de re-ejecución del script
- **Uso de memoria**: RAM consumida
- **Conexiones activas**: Usuarios conectados

### Optimizaciones Implementadas

1. **Caching de datos**:
   - `st.session_state.data`: Carga JSON una sola vez

2. **Validación temprana**:
   - Validación de JSON al cargar, no en cada pregunta

3. **Renderizado condicional**:
   - Solo se renderiza la pregunta actual
   - Resultados solo al finalizar

## Seguridad

### Consideraciones

1. **No hay autenticación**: App pública local
2. **No hay persistencia**: Datos solo en sesión
3. **No hay backend**: Todo en cliente
4. **JSON local**: No se expone a internet

### Recomendaciones para Producción

Si se despliega públicamente:

- [ ] Agregar autenticación (Streamlit Auth)
- [ ] Implementar rate limiting
- [ ] Validar inputs del usuario
- [ ] Usar HTTPS
- [ ] Configurar CORS apropiadamente

## Mantenimiento

### Actualizar Dependencias

**Con UV**:
```bash
uv sync --upgrade
```

**Con pip**:
```bash
pip install --upgrade streamlit pandas
```

### Backup de Datos

Respaldar regularmente:
```bash
cp data/questions.json data/questions.backup.json
```

### Limpieza

Eliminar archivos temporales:
```bash
# Cache de Python
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Cache de Streamlit
rm -rf ~/.streamlit/cache/
```

## Soporte y Contacto

Para problemas técnicos:

1. Revisar logs de Streamlit
2. Verificar validación de JSON
3. Consultar documentación de Streamlit: [docs.streamlit.io](https://docs.streamlit.io)
4. Abrir issue en GitHub

---

**Última actualización**: Diciembre 2024

