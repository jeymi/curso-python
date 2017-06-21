

if __name__ == '__main__':

    person = input('ingresar el nombre de la persona:')
    edad = int(input('ingresar edad actual:'))
    fecha = int(input('ingresar año de nacimiento:'))
    resta = 100
    suma = resta + fecha
    mensaje = 'En {suma} {person} llegara a cumplir 100 años'

    print(mensaje.format(suma=suma, person=person))
