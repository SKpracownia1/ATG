#-*- coding: utf-8 -*-

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

print("Podaj wierzchołki początkowe i końcowe krawędzi(oddzielone spacją):")

for j in range (int(m)):
	a,b=input().split(' ')
	matrix[int(a)][int(b)]=1
	matrix[int(b)][int(a)]=1

stopnie(matrix)
	
	

