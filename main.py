from partida import Partida

print('MOLINO 9\n')

numero = int(input('seleccione el número de piezas [3 o 9]:'))
p = Partida(numero)
p.jugar_partida()

