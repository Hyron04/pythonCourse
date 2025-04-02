message = 4.5
print(message)

#Ejemplo de listas
trabajadores = ["Jordi", "Pep", "Maria", "Anna"]
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método append para añadir un elemento
trabajadores.append("Josep")
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método remove para eliminar un elemento
trabajadores.remove("Pep")
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método insert para añadir un elemento en una posición concreta
trabajadores.insert(3, "Pep")
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método pop para eliminar un elemento
trabajadores.pop(2)
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método sort para ordenar los elementos
trabajadores.sort()
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método reverse para invertir el orden de los elementos
trabajadores.reverse()
print(trabajadores)
print(len(trabajadores))

#Lista donde aplicamos el método clear para eliminar todos los elementos
trabajadores.clear()
print(trabajadores)
print(len(trabajadores))

#Ejemplo de listas con rangos
trabajadores = ["Jordi", "Pep", "Maria", "Anna", "Josep", "Jolien", "Albert", "Iris"]
print(trabajadores)
print(len(trabajadores))
print(trabajadores[0:3]) #Imprime los elementos de la posición 0 a la 2
print(trabajadores[2:3]) #Imprime los elementos de la posición 2 a la 2
print(trabajadores[:4]) #Imprime los elementos de la posición 0 a la 3