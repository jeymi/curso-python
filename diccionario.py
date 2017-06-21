import random
mensaje= "el {0} de {1} de edad, es de la ciudad de {2} y cursa {3} en la universidad"
NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]
import random

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }
    return estudiantes

if __name__ == '__main__':
    diccio = generar_diccionario_estudiantes()
 
    for llave,valor in diccio.iteritems() :
        print llave,valor
if __name__ == '__main__':
    for llave,valor in diccio.iteritems():
        print mensaje.format(llave,valor['edad'],valor['ciudad'],valor['anio'])
if __name__ == '__main__':
    
    
