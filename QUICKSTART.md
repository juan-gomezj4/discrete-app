# 🚀 Inicio Rápido

## Instalación en 3 pasos

### 1. Instalar UV (si no lo tienes)

**macOS/Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/discrete-app.git
cd discrete-app
```

### 3. Ejecutar la aplicación

**macOS/Linux**:
```bash
./run.sh
```

**Windows**:
```cmd
run.bat
```

**O manualmente**:
```bash
uv venv
uv sync
uv run streamlit run app/ui.py
```

## ¡Listo! 🎉

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## Uso Básico

1. **Modo Práctica**:
   - Selecciona un tema
   - Ajusta cantidad de preguntas (3-10)
   - Presiona "Iniciar"

2. **Modo Examen**:
   - Selecciona "Examen (1 de cada tema)"
   - Presiona "Iniciar"

3. **Navega** con los botones Anterior/Siguiente

4. **Revisa** tus resultados al finalizar

## Solución de Problemas

### Puerto ocupado
```bash
# Usar puerto alternativo
uv run streamlit run app/ui.py --server.port=8502
```

### Módulo no encontrado
```bash
# Asegúrate de estar en el directorio correcto
cd discrete-app
# Y que el entorno esté sincronizado
uv sync
```

### Error al cargar preguntas
- Verifica que `data/questions.json` exista
- Valida el JSON en [jsonlint.com](https://jsonlint.com)

## Más Información

- **README completo**: [README.md](README.md)
- **Documentación técnica**: [COMPONENTES.md](COMPONENTES.md)
- **Agregar preguntas**: Ver sección "Extender el Banco" en README

## Atajos de Teclado

- `Ctrl+C`: Detener servidor
- `R`: Recargar aplicación (en navegador)
- `C`: Limpiar cache (en navegador)

---

**¿Necesitas ayuda?** Abre un issue en GitHub

