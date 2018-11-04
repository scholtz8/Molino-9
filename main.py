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
            
    def ver_turno(self):
        if self.turno == 1:
            return self.jugador1
        else:
            return self.jugador2

    def piezas_jugadas(self,color):
        piezas = []
        for i in range(1,25):
            if self.tablero.ver_estado(i) == color:
                piezas.append(i)
        return piezas

    def piezas_movibles(self,color):
        piezas_jugador = self.piezas_jugadas(color)
        for p in piezas_jugador:
            ady_v = self.tablero.adyacentes_vacios(p)
            if ady_v.__len__() == 0:
                piezas_jugador.remove(p)
        return piezas_jugador

    def movimientos_posibles(self,nodo):
        return self.tablero.adyacentes_vacios(nodo)

    def mover_pieza(self,origen,destino,color):
        self.tablero.cambiar_estado(origen,'V')
        self.tablero.cambiar_estado(destino,color)

    # fase de colocar piezas en el tablero
    def fase1(self,jugador):
        while True:
            try:
                self.tablero.ver_tablero()
                numero = int(input("("+jugador.ver_color()+") ELIJA UN ESPACIO EN EL TABLERO:"))
            except ValueError:
                print('ESPACIO INVALIDO\n')
                continue
            if numero < 1 or numero > 24:
                print('ESPACIO INVALIDO\n')
                continue
            else:
                if self.tablero.ver_estado(numero) != 'V':
                    print('ESPACIO OCUPADO\n')
                    continue
                else:
                    self.tablero.cambiar_estado(numero,jugador.ver_color())
                    jugador.restar_pieza()
                    break                    

    def fase2(self,jugador):
        while True:
            try:
                self.tablero.ver_tablero()
                origen, destino = [int(x) for x in input("("+jugador.ver_color()+") PIEZA A MOVER Y DONDE:").split()]
            except ValueError:
                print('VALOR O VALORES INVALIDOS\n')
                continue
            if origen not in self.piezas_movibles(jugador.ver_color()):
                print('PIEZA A MOVER INVALIDA\n')
                continue
            else:
                if destino not in self.movimientos_posibles(origen):
                    print('MOVIMIENTO DE '+str(origen)+' a '+str(destino)+' INVALIDO\n')
                    continue
                else:
                    self.mover_pieza(origen,destino,jugador.ver_color())
                    break
    

    def fase3(self,jugador):
        

        return
    

    def jugar_turno(self):

        if self.ver_turno().ver_piezas() > 0:
            self.fase1(self.ver_turno())
        else:
            if self.ver_turno().ver_perdidas() < self.piezas_juego - 3:
                self.fase2(self.ver_turno())
            else:
                self.fase3(self.ver_turno())

        self.cambiar_turno()


p = Partida(9)
for i in range(0,23):
    p.jugar_turno()


