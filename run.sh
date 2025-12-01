#!/bin/bash
# Script de inicio rápido para la aplicación

echo "🧠 Iniciando Aplicación de Matemáticas Discretas..."
echo ""

# Verificar si el entorno virtual existe
if [ ! -d ".venv" ]; then
    echo "⚠️  Entorno virtual no encontrado. Creando..."
    uv venv
    echo "✅ Entorno virtual creado"
fi

# Sincronizar dependencias
echo "📦 Sincronizando dependencias..."
uv sync

# Iniciar la aplicación
echo ""
echo "🚀 Iniciando servidor Streamlit..."
echo "📍 La aplicación se abrirá en http://localhost:8501"
echo ""
echo "💡 Presiona Ctrl+C para detener el servidor"
echo ""

uv run streamlit run app/ui.py

