# 📸 Aplicación CLI para Procesamiento de Fotografías

Aplicación de línea de comandos para procesar fotos desde la API de JSONPlaceholder, comparando rendimiento en tres modos de ejecución: secuencial, multihilos y multiprocesos.

## 🚀 Características principales
- **Tres modos de procesamiento**:
  - `secuencial`: Procesamiento lineal tradicional
  - `multihilos`: Paralelización con hilos (threading)
  - `multiprocesos`: Distribución en núcleos de CPU (multiprocessing)
- **Benchmark integrado** para comparación de tiempos
- Integración con API externa de [JSONPlaceholder](https://jsonplaceholder.typicode.com)
- Sistema de pruebas funcionales
- Interfaz CLI intuitiva con Typer

## 📦 Requisitos técnicos
- Python 3.9+
- Dependencias:
- requests typer


## ⚙️ Instalación
1. Clonar repositorio:

git clone https://github.com/tu-repositorio/photo-processor-cli.git
cd prueba-pandora-fms

2. Instalar dependencias:
pip install -r requirements.txt


## 🖥 Uso básico
python main.py --mode [MODO] --photos [CANTIDAD]


**Parámetros**:
- `--mode`: Modo de ejecución (`secuencial`, `multihilos`, `multiprocesos`)
- `--photos`: Número de fotos a procesar (opcional)

**Ejemplo**:
python main.py --mode multiprocesos --photos 50



## ⏱ Benchmark de rendimiento
Ejecutar comparativa completa:
python benchmark.py

**Salida típica**:

🔎 Resultados de rendimiento:
Modo | Tiempo (s)
secuencial | 15.200
multihilos | 8.350
multiprocesos | 4.600


## 🧠 Arquitectura

prueba-pandora-fms/
├── main.py # Interfaz CLI principal
├── api_service.py # Cliente de la API
│ ├── sequential.py
│ ├── multithreading.py
│ └── multiprocessing.py
├── benchmark.py # Script de comparativa
└── test_api.py # Pruebas de conexión


## 🔍 Pruebas de API
Verificar conectividad:
python test_api.py

**Salida esperada**:

✅ Conexión exitosa con la API
📸 Foto ID: 1 | Título: accusamus beatae ad facilis cum similique...


## 📚 Integración con API
Flujo de datos:
1. Obtener fotos de `/photos`
2. Recuperar metadatos de álbumes desde `/albums`
3. Combinar datos relacionados
4. Procesar según modo seleccionado

## 📄 Licencia
MIT License - Libre para uso y modificación
