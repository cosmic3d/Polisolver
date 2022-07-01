import math
#EXEMPLES: 

#4X6 + 4X5 - 47X4 - 48X3 + 128X2 + 140X +35

#X2 + 2X + 1

#25X3 - 15X + 10

#X4 - 5X2 + 4

#FEM UNA FUNCIÓ PER LA FORMULETA
def formul(a,b,c):
	detpos = (-b + math.sqrt(b*b -4*(a*c)))/(2*a)
	detneg = (-b - math.sqrt(b*b -4*(a*c)))/(2*a)
	dets = [detpos, detneg]
	if dets[0] == dets[1]:
		return str(detpos) + ", multiplicitat: 2" 
	else:
		return [str(detpos) + ", multiplicitat: 1", str(detneg) + ", multiplicitat: 1"]
#FEM UNA FUNCIÓ PER CALCULAR SI UN DIVISOR ES SOLUCIÓ I QUINA MULTIPLICITAT TÉ
def ruffi(divi, valors):
	vals = len(valors)
	prox = []
	proxante = []
	multipli = 0
	numir = -2
	prox.append(valors[0])
	for i in range(1, vals - 1):
		prox.append((divi*prox[-1]) + valors[i])
	
	if (divi*prox[-1]) + valors[-1] == 0:
		multipli += 1
		for i in prox:
			proxante.append(i)
		while True:
			si = False
			for g in range(1, len(prox)):
				prox.pop(1)
			longi = len(proxante)
			for i in range(1, longi - 1):
				prox.append((divi*prox[-1]) + proxante[i])
			if (divi*prox[-1]) + proxante[-1] == 0:
				si = True
			proxante = []
			for i in prox:
				proxante.append(i)
			if si == True:
				multipli += 1
			elif si == False:
				ret = str(divi) + ", multiplicitat: " + str(multipli)
				return ret
	else:
		return 0
#PREGUNTEM PEL GRAU
while True:
	grau = int(input("DE QUIN GRAU ES EL TEU POLINOMI?"))
	if grau <= 1:
		print("AIXÒ HO POTS RESOLDRE TU :)")
		continue
	break
if grau > 2:
	#CREEM GRUPS PELS VALORS DE LES X I PELS DIVISORS DEL TI I ALTRES VARIABLES
	sumi = 0
	multi = 0
	sero = 0
	negati = False
	negaqp = False
	valorsx = []
	divisorsTI = []
	divisorsQP = []
	divisorstotals = []
	solucions = []
	#PREGUNTEM PEL VALOR DE LES X I ANYADIM AQUEST VALOR AL GRUP VALORSX
	while True:
		for i in range(0, grau + 1):
			if i == 0:
				ti = int(input("QUIN ES EL TERME INDEPENDENT?"))
				if ti == 0:
					solucions.append(0)
					print("Simplifica-ho :)")
					break
				valorsx.append(ti)
			elif i >= 1:
				valorsx.append(int(input("QUIN ES EL QUOFICIENT PRINCIPAL DE X A LA " + str(i) + "? ")))
		if ti != 0:
			if valorsx[-1] == 0:
				print("VAS DIR QUE ERA DE GRAU " + str(grau))
				continue
		if ti != 0: 
			break
	qp = valorsx[-1]
	#TROBEM ELS DIVISORS DEL TI I DEL QUOFICIENT PRINCIPAL I ELS GUARDEM A UN GRUP
	divisorsTI.append(1)
	divisorsQP.append(1)
	if ti < 0:
		ti = ti * -1
		negati = True
	if qp < 0:
		qp = qp * -1
		negaqp = True
	for i in range(0, ti):
		if i >= 2:
			if ti%i == 0:
				divisorsTI.append(i)
	for i in range(0, qp):
		if i >= 2:
			if qp%i == 0:
				divisorsQP.append(i)
	if ti != 1 and ti != -1:
		divisorsTI.append(ti)  #AQUI POSEM A UN GRUP ELS DIVISORS DEL TI
	if qp != 1 and qp != -1:
		divisorsQP.append(qp)  #AQUI POSEM A UN GRUP ELS DIVISORS DEL QP
	if negati:
		ti = ti * -1
	if negaqp:
		qp = qp * -1
	#BUSQUEM ELS CANDIDATS RACIONALS
	for quofi in divisorsQP:
		for termi in divisorsTI:
			if not (termi/quofi) in divisorstotals:
				divisorstotals.append(termi/quofi)
				divisorstotals.append((termi/quofi)*-1)
	print("ELS DIVISORS DEL TI SÓN: " + str(divisorstotals))
	#FEM ELS CÁLCULS
	var = len(valorsx)
	valorsx.reverse()
	resuls = []
	for d in divisorstotals:
		resul = ruffi(d, valorsx) #TRUQUEM A LA FUNCIÓ QUE FARÁ EL RUFFINI PER A CADASCÚN DELS DIVISORS
		if resul != 0:            #I RETORNARÁ EL DIVISOR SI ES ARREL DEL POLINOMI
			resuls.append(resul)
	for i in resuls:
		print(i)
		print(" ")
elif grau == 2:
	#FEM TAMBÉ UNA FORMULETA
	print("UTILITZANT LA FORMULETA...")
	a = int(input("Valor A?"))
	b = int(input("Valor B?"))
	c = int(input("Valor C?"))
	resul1 = formul (a,b,c) #TRUQUEM A LA FUNCIÓ QUE FARÁ LA FORMULETA I RETORNARÁ ELS RESULTATS
	print(resul1)






