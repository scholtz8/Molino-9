from tablero import Tablero
from jugador import Jugador


print('Molino 9')

class Partida(object):

    def __init__(self,num_piezas):
        self.turno = 1
        self.piezas_juego = num_piezas
        self.jugador1 = Jugador(num_piezas,'B')
        self.jugador2 = Jugador(num_piezas,'N')
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

    # lista con las piezas en juego del jugador
    def piezas_jugadas(self,color):
        piezas = []
        for i in range(1,25):
            if self.tablero.ver_estado(i) == color:
                piezas.append(i)
        return piezas

    # lista con las piezas que el jugador puede mover
    def piezas_movibles(self,color):
        piezas_jugador = self.piezas_jugadas(color)
        for p in piezas_jugador:
            ady_v = self.tablero.adyacentes_vacios(p)
            if ady_v.__len__() == 0:
                piezas_jugador.remove(p)
        return piezas_jugador

    def movimientos_posibles(self,pieza):
        return self.tablero.adyacentes_vacios(pieza)

    def mover_pieza(self,origen,destino,color):
        self.tablero.cambiar_estado(origen,'V')
        self.tablero.cambiar_estado(destino,color)

    # ver si pieza pertenece a un molino
    def es_molino(self,pieza,jugador):
        molinos = self.tablero.ver_molinos(pieza)
        for m in molinos:
            i = 0
            for p in m:
                if self.tablero.ver_estado(p) == jugador.ver_color():
                    i += 1
                if i == 3:
                    return True
        return False

    # obtener el color del jugador oponente
    def ver_rival(self,color_jugador):
        if color_jugador == 'B':
            return self.jugador2
        else:
            return self.jugador1

    def piezas_eliminables(self,jugador):
        # cantidad de piezas que le quedan al jugador
        piezas_jugadas = self.piezas_jugadas(jugador.ver_color())
        piezas_no_molino = []
        contador_piezas_molino = 0

        for p in piezas_jugadas:
            if self.es_molino(p,jugador):
                contador_piezas_molino += 1
            else:
                piezas_no_molino.append(p)

        if contador_piezas_molino == piezas_jugadas.__len__():
            return piezas_jugadas
        else:
            return piezas_no_molino
        
    def eliminar_pieza(self,jugador):        
        while True:
            try:
                eliminada = int(input("("+jugador.ver_color()+") ELIJA LA PIEZA OPONENTE A ELIMINAR"))
            except ValueError:
                print('VALOR INVALIDO\n')
                continue
            if eliminada not in self.piezas_eliminables(self.ver_rival(jugador.ver_color())):
                print('VALOR INVALIDO\n')
                continue
            else:
                self.tablero.cambiar_estado(eliminada,'V')
                self.ver_rival(jugador.ver_color()).perder_pieza()
                break     
        
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
        return numero                    

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
        return destino
    

    def fase3(self,jugador):
        

        return
    

    def jugar_turno(self):

        if self.ver_turno().ver_piezas() > 0:
            pieza_jugada = self.fase1(self.ver_turno())
        else:
            if self.ver_turno().ver_perdidas() < self.piezas_juego - 3:
                pieza_jugada = self.fase2(self.ver_turno())
            else:
                pieza_jugada = self.fase3(self.ver_turno())

        
        if self.es_molino(pieza_jugada,self.ver_turno()):
            self.eliminar_pieza(self.ver_turno())
    
        self.cambiar_turno()


p = Partida(9)
for i in range(0,23):
    p.jugar_turno()


