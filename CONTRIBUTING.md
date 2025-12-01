# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Esta guía te ayudará a empezar.

## Formas de Contribuir

- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 📝 Mejorar documentación
- ✨ Agregar preguntas al banco
- 🔧 Enviar código

## Reportar Bugs

Abre un issue en GitHub incluyendo:

1. **Descripción clara** del problema
2. **Pasos para reproducir**:
   - Paso 1
   - Paso 2
   - ...
3. **Comportamiento esperado**
4. **Comportamiento actual**
5. **Información del sistema**:
   - SO y versión
   - Versión de Python
   - Versión de Streamlit

## Sugerir Características

Abre un issue con:

1. **Descripción** de la característica
2. **Motivación**: ¿Por qué es útil?
3. **Ejemplos** de uso
4. **Alternativas** consideradas (opcional)

## Agregar Preguntas

La forma más fácil de contribuir es agregar preguntas al banco.

### Proceso

1. **Fork** el repositorio
2. **Edita** `data/questions.json`
3. **Sigue el formato**:

```json
{
  "type": "single|multiple|tf|input",
  "question": "Texto claro y conciso",
  "options": ["A", "B", "C"],  // Solo para single/multiple
  "answer": 0  // Índice, lista, booleano o string
}
```

4. **Valida** el JSON en [jsonlint.com](https://jsonlint.com)
5. **Prueba** localmente:
   ```bash
   uv run streamlit run app/ui.py
   ```
6. **Commit** con mensaje descriptivo:
   ```bash
   git commit -m "Agregar preguntas de conjuntos"
   ```
7. **Abre Pull Request**

### Criterios de Calidad

- ✅ Pregunta clara y sin ambigüedades
- ✅ Respuesta correcta verificada
- ✅ Opciones plausibles (para multiple choice)
- ✅ Ortografía y gramática correctas
- ✅ Símbolos matemáticos apropiados (∧, ∨, ¬, etc.)

## Contribuir Código

### Configuración del Entorno

1. **Fork y clonar**:
   ```bash
   git clone https://github.com/tu-usuario/discrete-app.git
   cd discrete-app
   ```

2. **Crear rama**:
   ```bash
   git checkout -b feature/mi-caracteristica
   ```

3. **Instalar dependencias**:
   ```bash
   uv venv
   uv sync
   ```

### Estándares de Código

#### Python

- **Estilo**: PEP 8
- **Tipado**: Usar type hints donde sea útil
- **Docstrings**: Formato Google/NumPy
- **Nombres**: Descriptivos en español para UI, inglés para código

#### Estructura

```python
def funcion_ejemplo(parametro: str) -> bool:
    """Descripción breve de la función.
    
    Args:
        parametro: Descripción del parámetro
        
    Returns:
        Descripción del valor de retorno
    """
    # Implementación
    return True
```

#### Comentarios

- Comentarios en español para lógica de negocio
- Comentarios en inglés para código técnico (opcional)
- Explicar el "por qué", no el "qué"

### Testing

Antes de enviar tu PR:

1. **Prueba manual**:
   ```bash
   uv run streamlit run app/ui.py
   ```

2. **Verifica todos los modos**:
   - Práctica por tema
   - Modo examen
   - Navegación (anterior/siguiente)
   - Resultados finales

3. **Prueba tipos de pregunta**:
   - Opción única
   - Opción múltiple
   - Verdadero/Falso
   - Respuesta libre

### Proceso de Pull Request

1. **Actualiza tu fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Commit con mensajes claros**:
   ```bash
   git commit -m "Agregar: Modo de práctica cronometrado"
   ```

   Prefijos recomendados:
   - `Agregar:` Nueva característica
   - `Corregir:` Bug fix
   - `Mejorar:` Mejora de código existente
   - `Documentar:` Cambios en documentación
   - `Refactorizar:` Cambios sin afectar funcionalidad

3. **Push a tu fork**:
   ```bash
   git push origin feature/mi-caracteristica
   ```

4. **Abre Pull Request** en GitHub:
   - Título descriptivo
   - Descripción detallada de cambios
   - Referencias a issues relacionados
   - Screenshots si aplica

### Revisión de Código

Tu PR será revisado considerando:

- ✅ Funcionalidad correcta
- ✅ Código limpio y mantenible
- ✅ Documentación actualizada
- ✅ Sin errores de linting
- ✅ Compatible con Python 3.11+

## Estructura del Proyecto

```
discrete-app/
├── app/
│   ├── ui.py          # Interfaz Streamlit (modifica aquí para UI)
│   ├── logic.py       # Evaluación (modifica para nueva lógica)
│   └── utils.py       # Utilidades (modifica para I/O)
├── data/
│   └── questions.json # Banco de preguntas (agrega preguntas aquí)
├── .streamlit/
│   └── config.toml    # Configuración de Streamlit
└── docs/              # Documentación adicional
```

### Dónde Modificar

- **Nueva característica UI**: `app/ui.py`
- **Nueva lógica de evaluación**: `app/logic.py`
- **Nuevo formato de pregunta**: `app/utils.py` + `app/logic.py`
- **Nuevas preguntas**: `data/questions.json`
- **Documentación**: `*.md`

## Estilo de Commits

### Formato

```
Tipo: Descripción breve (máx 50 caracteres)

Descripción detallada opcional (máx 72 caracteres por línea).
Explica el "por qué" de los cambios, no el "qué".

Refs: #123
```

### Ejemplos

```bash
# Bueno
git commit -m "Agregar: Soporte para preguntas de emparejamiento"

# Mejor
git commit -m "Agregar: Soporte para preguntas de emparejamiento

Implementa nuevo tipo 'matching' que permite emparejar conceptos
con definiciones. Útil para evaluar comprensión de vocabulario.

Refs: #45"
```

## Licencia

Al contribuir, aceptas que tus contribuciones se licencien bajo la misma licencia del proyecto (MIT).

## Código de Conducta

### Nuestro Compromiso

- Ser respetuoso y profesional
- Aceptar críticas constructivas
- Enfocarse en lo mejor para la comunidad
- Mostrar empatía hacia otros

### Comportamiento Inaceptable

- Lenguaje ofensivo o discriminatorio
- Ataques personales
- Trolling o comentarios despectivos
- Acoso de cualquier tipo

## Preguntas

¿Tienes preguntas? Abre un issue con la etiqueta `question`.

## Reconocimientos

Todos los contribuidores serán reconocidos en el README.

---

**¡Gracias por contribuir! 🎉**

