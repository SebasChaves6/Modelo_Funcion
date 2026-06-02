import time
import tracemalloc
import random
import string
import sys
import os

from lista_arreglos import lista_arreglos
from lista_punteros import lista_punteros
from tabla_hash import tabla_hash
from trie_punteros import trie_punteros
from trie_arreglos import trie_arreglos
from abb_punteros import ModeloFuncionABBPunteros
from abb_heap import ModeloFuncionABBHeap

# Sube el limite de recursion por si alguna estructura lo necesita
sys.setrecursionlimit(50000)

def generar_valor_aleatorio(longitud=20):
    """Genera valores válidos (20 letras minúsculas)."""
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(longitud))

def generar_datos(N, tipo):
    """Genera llaves y valores según el tipo solicitado (Aleatorio u Ordenado)."""
    valores = [generar_valor_aleatorio() for _ in range(N)]
    
    if tipo == "Ordenado":
        # Hace llaves seguidas en orden alfabético
        llaves = [f"llave{str(i).zfill(10)}" for i in range(N)]
    else:
        # Saca llaves al azar con letras y números
        caracteres = string.ascii_lowercase + string.digits
        llaves = [''.join(random.choice(caracteres) for _ in range(15)) for _ in range(N)]
        
    return llaves, valores

def analizar_estructura(clase_est, nombre_est, rangos_N):
    print(f"\n" + "="*105)
    print(f" EVALUANDO: {nombre_est} (PROMEDIO DE 10 CORRIDAS)")
    print("="*105)
    print(f"{'N':<6} | {'Tipo':<9} | {'Assign(s)':<9} | {'Lookup(s)':<9} | {'Print(s)':<9} | {'Unassign(s)':<11} | {'Done(s)':<8} | {'Mem(MB)':<8}")
    print("-" * 105)

    tipos_prueba = ["Aleatorio", "Ordenado"]
    REPETICIONES = 10

    for N in rangos_N:
        for tipo in tipos_prueba:
            
            # Va juntando los tiempos de las 10 corridas
            sum_assign = 0.0
            sum_lookup = 0.0
            sum_print = 0.0
            sum_unassign = 0.0
            sum_done = 0.0
            sum_memoria = 0.0
            
            colapso = False
            mensaje_colapso = ""
            consola_original = sys.stdout

            for corrida in range(REPETICIONES):
                # Genera datos nuevos en cada una de las 10 corridas
                llaves, valores = generar_datos(N, tipo)
                
                try:
                    # Arranca con una estructura limpia
                    est = clase_est()

                    # 1. ASSIGN & MEMORIA
                    tracemalloc.start()
                    t_inicio = time.perf_counter()
                    for i in range(N):
                        est.assign(llaves[i], valores[i])
                    t_fin = time.perf_counter()
                    _, pico_memoria = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    
                    sum_assign += (t_fin - t_inicio)
                    # Guarda el pico mas alto de memoria
                    sum_memoria = max(sum_memoria, pico_memoria / (1024 * 1024))

                    # 2. LOOKUP
                    t_inicio = time.perf_counter()
                    for llave in llaves:
                        est.lookup(llave)
                    t_fin = time.perf_counter()
                    sum_lookup += (t_fin - t_inicio)

                    # 3. PRINT (Lo manda al agujero negro del sistema)
                    sys.stdout = open(os.devnull, 'w') if hasattr(os, 'devnull') else open('NUL', 'w') if sys.platform == 'win32' else open('/dev/null', 'w')
                    
                    t_inicio = time.perf_counter()
                    est.print()
                    t_fin = time.perf_counter()
                    sum_print += (t_fin - t_inicio)
                    
                    sys.stdout.close()
                    sys.stdout = consola_original

                    # 4. UNASSIGN
                    t_inicio = time.perf_counter()
                    for llave in llaves:
                        est.unassign(llave)
                    t_fin = time.perf_counter()
                    sum_unassign += (t_fin - t_inicio)

                    # 5. DONE
                    t_inicio = time.perf_counter()
                    est.done()
                    t_fin = time.perf_counter()
                    sum_done += (t_fin - t_inicio)

                except MemoryError:
                    tracemalloc.stop()
                    sys.stdout = consola_original
                    colapso = True
                    mensaje_colapso = "¡COLAPSO! MemoryError (RAM insuficiente)"
                    break # Corta las 10 corridas si se queda sin RAM
                except RecursionError:
                    tracemalloc.stop()
                    sys.stdout = consola_original
                    colapso = True
                    mensaje_colapso = "¡COLAPSO! RecursionError (Límite excedido)"
                    break
                except Exception as e:
                    tracemalloc.stop()
                    sys.stdout = consola_original
                    colapso = True
                    mensaje_colapso = f"Error: {str(e)}"
                    break

            # Si salen bien las 10 corridas, calcula e imprime los promedios
            if not colapso:
                prom_assign = sum_assign / REPETICIONES
                prom_lookup = sum_lookup / REPETICIONES
                prom_print = sum_print / REPETICIONES
                prom_unassign = sum_unassign / REPETICIONES
                prom_done = sum_done / REPETICIONES
                
                print(f"{N:<6} | {tipo:<9} | {prom_assign:<9.4f} | {prom_lookup:<9.4f} | {prom_print:<9.4f} | {prom_unassign:<11.4f} | {prom_done:<8.4f} | {sum_memoria:<8.2f}")
            else:
                print(f"{N:<6} | {tipo:<9} | {mensaje_colapso:<70}")

if __name__ == "__main__":
    print("=================================================================================")
    print("      PROGRAMA DE ANÁLISIS ESTADÍSTICO (10 CORRIDAS) - MODELO FUNCIÓN (ETAPA 3)")
    print("=================================================================================")
    
    # Rangos de N a evaluar
    rangos_N = [1000, 5000, 10000, 20000]

    estructuras = [
        (lista_arreglos, "Lista Ordenada por Arreglos"),
        (lista_punteros, "Lista Ordenada por Punteros"),
        (tabla_hash, "Tabla Hash Abierta"),
        (trie_punteros, "Trie por Punteros"),
        (trie_arreglos, "Trie por Arreglos"),
        (ModeloFuncionABBPunteros, "ABB por Punteros"),
        (ModeloFuncionABBHeap, "ABB por Arreglos (Vector Heap)")
    ]

    for clase, nombre in estructuras:
        analizar_estructura(clase, nombre, rangos_N)
        
    print("\nAnálisis completo finalizado. Los promedios estadísticos están listos.")