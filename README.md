
---

## Estructura del Proyecto
| Archivo              | Descripción                                  |
|----------------------|----------------------------------------------|
| `app/cli.py`         | Interfaz CLI con validación de parámetros    |
| `app/api_service.py` | Cliente HTTP con retries y manejo de errores |
| `app/sequential.py`  | Procesamiento secuencial                     |
| `app/multithreading.py` | Procesamiento concurrente con hilos       |
| `app/multiprocessing.py` | Procesamiento paralelo con procesos      |

---


## 🚀 Uso
### Ejecución básica

Modo secuencial (todas las fotos)
python main.py --mode secuencial

Modo multihilos (50 fotos)
python main.py --mode multihilos --photos 50

Modo multiprocesos (sin límite)
python main.py --mode multiprocesos

## Resumen de la Experiencia

### Lógica de la Solución
1. **CLI con Typer**:  
   - Seleccioné Typer por su integración con type hints y autocompletado.  
   - Parámetros `--mode` y `--photos` validados estrictamente (`--photos` es opcional).

2. **Concurrencia**:  
   - **Multihilos**: Usé `ThreadPoolExecutor` para optimizar operaciones I/O (peticiones HTTP).  
   - **Multiprocesos**: Implementé `ProcessPoolExecutor` para paralelismo real en CPU.

3. **Manejo de Errores**:  
   - Retries automáticos (3 intentos) en peticiones HTTP.  
   - Logging en consola y archivo (`app.log`).

### Problemas y Soluciones
| Problema                          | Solución                                  |
|-----------------------------------|-------------------------------------------|
| **Orden en multihilos**           | Lista pre-inicializada con índices.       |
| **Errores HTTP 429**              | Límite de 20 hilos concurrentes.          |
| **Serialización en multiprocesos**| Funciones a nivel de módulo.              |

### ¿Cuándo Usar Cada Modo?
| Modo           | Caso de Uso Ideal                          |
|----------------|--------------------------------------------|
| **Secuencial** | Debugging o pruebas con pocos datos.       |
| **Multihilos** | Operaciones I/O (APIs, redes, archivos).   |
| **Multiprocesos** | Cálculos intensivos en CPU (procesamiento local). |

---

## Comparativa de Rendimiento
Ejecutando 100 fotos (resultados de referencia):




---

## Puntos Extra Implementados
1. **Manejo de Errores**:  
   - Retries automáticos en peticiones HTTP.  
   - Mensajes de error en rojo en la CLI.  

2. **Logging Dual**:  
   - Registro en consola y archivo `app.log`.  

3. **Benchmark Automático**:  
   - Script `benchmark.py` para comparar tiempos.  

---

## Criterios de Evaluación Cumplidos
✅ **CLI funcional** con parámetros validados.  
✅ **Tres modos de ejecución** implementados.  
✅ **Límite de fotos** opcional.  
✅ **Documentación completa** en README.md.  
✅ **Resumen técnico** con decisiones y problemas.  

---

**¡Listo para revisión técnica!** 🚀  

