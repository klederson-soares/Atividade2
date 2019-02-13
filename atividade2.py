
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


print(a.union(b))  
print(a.intersection(b)) 
print(a.difference(b)) 
print(a.symmetric_difference(b)) 
print(1 in a)



c = {1, 2}
print(c.issubset(a))


c = {1, 2}
d = {3, 4}
print(c.isdisjoint(d))

lista = [1, 2, 3, 4, 5, 6]
conjunto = set(lista)
print(conjunto)


