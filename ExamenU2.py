#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear')
	print ("Examen Unidad 2 por Lilia")
	print ("Programacion asincrona")
	print ("\t1 - Multiprocessing")
	print ("\t2 - Threading")
	print ("\t3 - Coroutines")
	print ("\t4 - Count Async")
	print ("\t5 - Rand")
	print ("\t6 - Chained ")
	print ("Paralelismo")
	print ("\t7 - Función Pool.Appy")
	print ("\t8 - Función Pool Map")
	print ("\t9 - Función Pool Starmap")
	print ("\t0 - Salir")

while True:
	# Mostramos el menu
	menu()
	# solicituamos una opción al usuario
	opcionMenu = input("Seleccione una opcion >> ")
	if opcionMenu=="1":
		subprocess.call(["python", "E1multiprocessing.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="2":
		subprocess.call(["python", "E2threading.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="3":
		subprocess.call(["python3", "E3coroutines.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
#	elif opcionMenu=="4":
#		subprocess.call(["python3.7", "E4async.py"])
#		print ("")
#		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="4":
		subprocess.call(["python3.7", "E5countasync.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="5":
		subprocess.call(["python3", "E6rand.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="6":
		subprocess.call(["python3", "E7chained.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="7":
		subprocess.call(["python3", "E9poolApply.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="8":
		subprocess.call(["python3", "E10poolMap.py"])
		print ("")
		input("\nPulsa una tecla para continuar")
	elif opcionMenu=="9":
		subprocess.call(["python3", "E11poolStarmap.py"])
		print ("")
		input("\nPulsa una tecla para continuar")		
						
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")