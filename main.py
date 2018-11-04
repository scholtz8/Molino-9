from tablero import Tablero
from jugador import Jugador


print('Molino 9')

class Partida(object):

    def __init__(self,piezas):
        self.turno = 1
        self.piezas_juego = piezas
        self.jugador1 = Jugador(piezas,'B')
        self.jugador2 = Jugador(piezas,'N')
        self.tablero = Tablero()

    #cambiar a turno entre el jugador 1 y 2
    def cambiar_turno(self):
        if self.turno == 1:
            self.turno = 2
        else:
            self.turno = 1

    def posicionar_pieza(self,nodo,color):
        if self.tablero.ver_estado(nodo) == 'V':
            self.tablero.cambiar_estado(nodo,color)
            return True
        else:
            print(f'ESPACIO YA UTILIZADO\n')
            return False

    def pieza_movible(self,nodo,color):
        if self.tablero.ver_estado(nodo) == color:
            ady = self.tablero.adyacentes(nodo)
            mov_posibles = []
            for n in ady:
                if self.tablero.ver_estado(n) == 'V':
                    mov_posibles.append(n)
            if mov_posibles.__len__() > 0:
                return True
            else:
                return False
        else:
            return False

    def jugar_turno(self):
        if self.turno == 1:
            jugador = self.jugador1
        else:
            jugador = self.jugador2

        #fase de posicionar piezas
        if jugador.ver_piezas() > 0:
            i = False
            while not i:
                self.tablero.ver_tablero()
                while True:
                    try:
                        numero = int(input(jugador.color+"¿Donde va poner la pieza?:"))
                    except ValueError:
                        print(f'ESPACIO INVALIDO\n')
                        continue
                    if numero < 1 or numero > 24:
                        print(f'ESPACIO INVALIDO\n')
                        continue
                    else:
                        break
                i = self.posicionar_pieza(numero,jugador.ver_color())
            jugador.jugar_pieza()
        else:
            #fase de mover piezas
            if jugador.ver_muertas() < self.piezas_juego - 3:
                while True:
                    try:
                        numero = int(input(jugador.color+"¿Que pieza va a mover?:"))
                    except:
                        print(f'POSICION INVALIDA\n')
                    if self.pieza_movible(numero,jugador.ver_color()) == True:
                        print('se puede mover la pieza\n')
                        break
                    else:
                        print('no se puede mover la pieza')

                return
            #fase de vuelo
            else:
                print('wenu')
                return

        self.cambiar_turno()
        return

t = Tablero()
t.ver_tablero()
print(t.adyacentes(1),t.adyacentes_vacios(1))
t.cambiar_estado(2,'N')
print(t.adyacentes(1),t.adyacentes_vacios(1))

'''    
p = Partida(9)
for i in range(0,13):
    p.jugar_turno()
    p.jugar_turno()
'''