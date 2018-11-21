def movimiento_posible(x, y, area_posible):
	print("punto a adjuntar", x, y)
	for idx, punto_inicial in enumerate(area_posible):
		if(x >= punto_inicial[0] and y >=punto_inicial[1] and x <= punto_inicial[0]+50 and y <=punto_inicial[1]+50):
			print("posicion ", idx+1)
			return True
	return False
