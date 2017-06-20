import argparse


if __name__ == '__main__':

	parser= argparse.ArgumentParser('valor')
	parser.add_argument('nombre')
	parser.add_argument('edad')
	parser.add_argument('clase')

	
	args = parser.parse_args()
	
	datos = {
	'nombre': args.nombre,
	'edad': args.edad,
	'clase':args.clase
	}

	for llave,valor in datos.iteritems():
		print llave,valor