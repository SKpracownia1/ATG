#-*- coding: utf-8 -*-
# cyfry w macierzy powinny być rozdzielone przecinkami.

def stopnie(m):
	licznik=0
	st_grafu=0
	for i in m:
		print("Stopień wierzchołka ",licznik,"=",sum(i))
		if (sum(i)>=st_grafu):
			st_grafu=sum(i)
		licznik+=1
	print("Stopień grafu= ",st_grafu)
	

n=input("Podaj liczbę wierzchołków:")
m=input("Podaj liczbę krawędzi:")

matrix = [[0]*int(n) for i in range(int(n))]

print("Wpisz macierz sąsiedztwa:")

for j in range (int(n)):
	wiersz=input()
	matrix.append(wiersz.split(','))

stopnie(matrix)
	
	

