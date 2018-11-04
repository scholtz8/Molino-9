class Jugador(object):

    def __init__(self,num_piezas,color):
        self.color = color
        self.piezas = num_piezas
        self.perdidas = 0

    def ver_piezas(self):
        return self.piezas

    def ver_muertas(self):
        return self.perdidas

    def ver_color(self):
        return self.color

    def jugar_pieza(self):
        self.piezas -= 1

    def matar_pieza(self):
        self.perdidas += 1
