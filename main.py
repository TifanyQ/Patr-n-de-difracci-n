import math
import statistics
from scipy.constants import hbar, m_e, pi   #hbar en J.s


# Ingreso de datos (ángulos)
onda = float(input("Ingresa la longitud de onda (Angstrom): "))
lista = [float(input("Ingresa los 8 ángulos: ")) for _ in range(1, 9)]

# Cálculos intermedios
listadostheta = [x / 2 for x in lista]
listaseno = [math.sin(math.radians(x)) for x in listadostheta]
distinterplanar = [onda / (2 * x) for x in listaseno]
listaseno2 = [x**2 for x in listaseno]
listadiv = [x / listaseno2[0] for x in listaseno2]

# Resultados parciales
print("Ángulo (theta): {}".format(listadostheta))
print("Seno del ángulo: {}".format(listaseno))
print("Seno^2 del ángulo: {}".format(listaseno2))
print("División: {}".format(listadiv))
print("Distancia interplanar: {}".format(distinterplanar))

# Obtención de los sigma
listasumatoria = []

for n in range(1, 5):
    m = n * listadiv[1]
    if abs(round(m) - m) < 0.1:
        primernumero = n
        listasumatoria.extend([primernumero] + [round(primernumero * x) for x in listadiv[1:]])
        listadea = [math.sqrt((onda ** 2 * x) / (4 * y)) for x, y in zip(listasumatoria[1:], listaseno2[1:])]

# Resultados finales
print("Los valores sigma son: {}".format(listasumatoria))
print("Constante de red: {}".format(listadea))

# Cálculo del promedio y desviación estándar
promedio = statistics.mean(listadea)
desviacion_estandar = statistics.stdev(listadea)
print("El valor promedio de a es: {}".format(promedio))
print("La desviación estándar es: {}".format(desviacion_estandar))