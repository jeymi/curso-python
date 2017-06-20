import argparse


if __name__ == '__main__':
	parser= argparse.ArgumentParser('valor')
	parser.add_argument('nombre')

	args = parser.parse_args()

	datos = {'ama':{'ana','jose'}}
    #args.nombre

    # si ana esta en datos
    #if args.nombre in datos:

        #print('la llave',args.nombre,'no existe en el diccionario')
	#else
        #print('la llave',args.nombre,'si existe en el diccionario')	
			
		

	for llave,valor in datos.iteritems():
		if args.nombre == llave :
			print('la llave',args.nombre,'no existe en el diccionario')
		else:
		    print('la llave',args.nombre,'si existe en el diccionario')	
			
		