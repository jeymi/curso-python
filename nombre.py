import argparse


if __name__ == '__main__':
	parser= argparse.ArgumentParser('valor')
	parser.add_argument('nombre')

	args = parser.parse_args()

	datos = {'nombre':{'ana','jose'}}
			
		
    if args.nombre in datos:


	for llave,valor in datos.iteritems():
		if args.nombre == llave :
			mensaje = 'la llave {0} si existe en el diccionarios'
			print mensaje.format(args.nombre)
		else:
			msj = 'la llave {0} no existe en el diccionario'
		    print msj.format(args.nombre)
			
		