from partida import Partida

print('MOLINO 9\n')

piezas_posibles = [3,5,6,7,9]
numero = int(input('seleccione el número de piezas [3, 5, 6, 7 ó 9]:'))
if numero not in piezas_posibles:
    print('numero invalido')
else:    
    p = Partida(numero)
    p.jugar_partida()

