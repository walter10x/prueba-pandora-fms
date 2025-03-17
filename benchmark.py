# benchmark.py
import subprocess
import time

def run_benchmark(photos: int = 100):
    modes = ["secuencial", "multihilos", "multiprocesos"]
    results = {}
    
    print("🚀 Ejecutando prueba de rendimiento...\n")
    
    for mode in modes:
        command = f"python main.py --mode {mode} --photos {photos}"
        start_time = time.perf_counter()
        
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error en modo {mode}: {str(e)}")
            continue
        
        elapsed = time.perf_counter() - start_time
        results[mode] = elapsed
    
    # Mostrar resultados
    print("\n🔎 Resultados:")
    print("{:<12} {:<10}".format("Modo", "Tiempo (s)"))
    print("-" * 25)
    for mode, time_spent in results.items():
        print("{:<12} {:.3f}".format(mode, time_spent))

if __name__ == "__main__":
    run_benchmark(photos=100)
