@echo off
REM Script de inicio rápido para Windows

echo 🧠 Iniciando Aplicación de Matemáticas Discretas...
echo.

REM Verificar si el entorno virtual existe
if not exist ".venv" (
    echo ⚠️  Entorno virtual no encontrado. Creando...
    uv venv
    echo ✅ Entorno virtual creado
)

REM Sincronizar dependencias
echo 📦 Sincronizando dependencias...
uv sync

REM Iniciar la aplicación
echo.
echo 🚀 Iniciando servidor Streamlit...
echo 📍 La aplicación se abrirá en http://localhost:8501
echo.
echo 💡 Presiona Ctrl+C para detener el servidor
echo.

uv run streamlit run app/ui.py

