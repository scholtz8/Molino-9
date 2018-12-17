import partida
import random


def evaluar_posicionamiento(par,color,posicion):
    tablero = par.tablero
    ptj = 0
    molinos = tablero.ver_molinos(posicion)

    count = 0
    #contar molinos que se hace con ficha en esa posicion
    for m in molinos:
        ct = 0
        for n in m:
            if tablero.ver_estado(n) == color:
                ct += 1
        if ct == 3:
            count += 1   
    
    ptj += 25*count

    # contar si bloquea algun posibilidad de que el rival hiciera un molino
    count = 0
    for m in molinos:
        ct = 0
        for n in m:
            est = tablero.ver_estado(n)
            if est != color and est != 'V':
                ct += 1
        if ct == 2:
            count += 1   
    
    ptj += 15*count

    # contar si deja la posibilidad de hacer un molino al siguiente turno (si el oponente no lo bloquea)
    count = 0
    for m in molinos:
        ct1 = 0
        ct2 = 0
        for n in m:
            est = tablero.ver_estado(n)
            if est == color:
                ct1 += 1
            elif est == 'V':
                ct2 += 1
        if ct1+ct2 == 3:
            count += 1
    
    ptj += 7*count

    ady = tablero.adyacentes(posicion)
    count = 0
    for a in ady:
        if tablero.ver_estado(a) != 'V':
            count +=1
    ptj += count*1

    for a in ady:
        if tablero.ver_estado(a) != color:
            count +=1
    ptj += count*2

    for a in ady:
        if tablero.ver_estado(a) != par.rival(color).ver_color():
            count +=1
    ptj -= count*2

    return ptj

def posicionar(partida,color):
    par = partida
    posibles = partida.vacios()

    listmax = list()
    max = 1
    for p in posibles:
        par.tablero.grafo.node[p]['estado'] = color
        e =  evaluar_posicionamiento(par,color,p)
        par.tablero.grafo.node[p]['estado'] = 'V'
        if max < e:
            listmax.clear()
            max = e
            listmax.append(p)
        elif max == e:
            listmax.append(p)
    
    return random.choice(listmax)

def evaluar_movimiento(partida,fase,color,posicion):
    par = partida
    if fase == 2:
        posibles = partida.movimientos_posibles(posicion)
    elif fase == 3:
        posibles = partida.vacios()
    bonus = list()
    listmax = list()
    max = 0
    for p in posibles:
        par.tablero.grafo.node[posicion]['estado'] = 'V'
        par.tablero.grafo.node[p]['estado'] = color
        e = evaluar_posicionamiento(partida,color,p)
        par.tablero.grafo.node[p]['estado'] = 'V'
        par.tablero.grafo.node[posicion]['estado'] = color
        bonus.append((posicion,p,e))
        if max < e:
            listmax.clear()
            max = e
            listmax.append((posicion,p,e))
        elif max == e:
            listmax.append((posicion,p,e))

    if listmax.__len__() == 0:
        listmax = bonus

    return random.choice(listmax)

def mover(partida,fase,color):
    if fase == 2:
        posibles = partida.movibles(color)
    elif fase == 3:
        posibles =partida.en_juego(color)

    bonus = list()
    listmax = list()
    max = 0
    for p in posibles:
        (pos1,pos2,e) = evaluar_movimiento(partida,fase,color,p)
        bonus.append((pos1,pos2))
        if max < e:
            listmax.clear()
            max = e
            listmax.append((pos1,pos2))
        elif max == e:
            listmax.append((pos1,pos2))
    
    if listmax.__len__() == 0:
        listmax = bonus
    
    return random.choice(listmax)


def evaluar_eliminacion(par,color,posicion):
    tablero = par.tablero
    ptj = 0
    molinos = tablero.ver_molinos(posicion)

    count = 0
    #contar molinos que estan hechos con ficha en esa posicion
    for m in molinos:
        ct = 0
        for n in m:
            if tablero.ver_estado(n) == color:
                ct += 1
        if ct == 3:
            count += 1   
    
    ptj += 10*count

    # contar si esa ficha esta en un casi molino 
    count = 0
    for m in molinos:
        ct1 = 0
        ct2 = 0
        for n in m:
            est = tablero.ver_estado(n)
            if est == color:
                ct1 += 1
            if est == 'V':
                ct2 += 1
        if ct1+ct2 == 3 and ct1<3:
            count += 1
    
    ptj += 25*count

    ady = tablero.adyacentes(posicion)
    count = 0
    for a in ady:
        if tablero.ver_estado(a) == 'V':
            count +=1
    ptj -= count*1

    return ptj

def eliminar(partida,color):
    eliminables = partida.eliminables(partida.rival(color).ver_color())

    listmax = list()
    max = 1
    for p in eliminables:
        e =  evaluar_eliminacion(partida,color,p)
        if max < e:
            listmax.clear()
            max = e
            listmax.append(p)
        elif max == e:
            listmax.append(p)
    
    if listmax.__len__() == 0:
        listmax = eliminables

    return random.choice(listmax)
