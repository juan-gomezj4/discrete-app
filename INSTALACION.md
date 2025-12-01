# 📦 Guía de Instalación - Matemáticas Discretas

## 🚀 Instalación Rápida

### Requisitos Previos

- **Python 3.11 o superior**
- **UV** (gestor de paquetes moderno) o **pip** (tradicional)

---

## Opción 1: Con UV (Recomendado) ⭐

### 1. Instalar UV

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Descomprimir el archivo

Extrae el archivo `discrete-app.zip` en tu ubicación preferida.

### 3. Ejecutar la aplicación

**macOS/Linux:**
```bash
cd discrete-app
./run.sh
```

**Windows:**
```cmd
cd discrete-app
run.bat
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## Opción 2: Con pip (Tradicional)

### 1. Verificar Python

```bash
python --version
# o
python3 --version
```

Debe ser 3.11 o superior.

### 2. Descomprimir el archivo

Extrae el archivo `discrete-app.zip` en tu ubicación preferida.

### 3. Crear entorno virtual

**macOS/Linux:**
```bash
cd discrete-app
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```cmd
cd discrete-app
python -m venv .venv
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
streamlit run app/ui.py
```

La aplicación se abrirá en `http://localhost:8501`

---

## 📖 Uso de la Aplicación

### Modo Práctica por Tema

1. En la barra lateral, selecciona **"Práctica por tema"**
2. Elige un tema del menú desplegable
3. Ajusta el número de preguntas (3-10) con el slider
4. Presiona **"Iniciar"**
5. Responde cada pregunta
6. Al finalizar, revisa tus resultados en la tabla interactiva

### Modo Examen

1. En la barra lateral, selecciona **"Examen (1 de cada tema)"**
2. Presiona **"Iniciar"**
3. Responde las preguntas (una de cada tema)
4. Al finalizar, revisa tu desempeño general

---

## 🐛 Solución de Problemas

### Error: "Puerto 8501 ocupado"

El puerto ya está en uso. Usa uno alternativo:

```bash
streamlit run app/ui.py --server.port=8502
```

### Error: "Módulo no encontrado"

Asegúrate de haber activado el entorno virtual:

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```cmd
.venv\Scripts\activate
```

### Error al cargar preguntas

Verifica que el archivo `data/questions.json` exista y sea válido.

---

## 📚 Temas Disponibles

1. **Proposiciones**
2. **Operadores Lógicos**
3. **Tautologías y Contradicciones**
4. **Implicaciones Lógicas**
5. **Cuantificadores**
6. **Interpretación de Cuantificadores**

---

## 📂 Estructura del Proyecto

```
discrete-app/
├── app/
│   ├── ui.py              # Interfaz de usuario
│   ├── logic.py           # Lógica de evaluación
│   └── utils.py           # Utilidades
├── data/
│   └── questions.json     # Banco de preguntas
├── .streamlit/
│   └── config.toml        # Configuración
├── README.md              # Documentación completa
├── QUICKSTART.md          # Inicio rápido
├── COMPONENTES.md         # Documentación técnica
├── requirements.txt       # Dependencias
├── run.sh                 # Script Linux/macOS
└── run.bat                # Script Windows
```

---

## 🔗 Recursos Adicionales

- **README completo**: Ver `README.md` para documentación exhaustiva
- **Documentación técnica**: Ver `COMPONENTES.md`
- **Guía de contribución**: Ver `CONTRIBUTING.md`
- **Repositorio GitHub**: https://github.com/juan-gomezj4/discrete-app

---

## 💡 Consejos

- **Detener el servidor**: Presiona `Ctrl+C` en la terminal
- **Recargar la app**: Presiona `R` en el navegador
- **Limpiar caché**: Presiona `C` en el navegador

---

## 📧 Soporte

Si encuentras problemas:

1. Revisa la sección de "Solución de Problemas"
2. Consulta el README completo
3. Abre un issue en GitHub

---

**¡Disfruta practicando Matemáticas Discretas! 🎓**

