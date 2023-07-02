
#a={1,2,3,4,5,9,5}
#b={}
#print(type(a))
#print(a)
#c={"adi",34,56,"er"}
#print(c)

#d={"adi",34,56,"er","adi"}
#print(d)
#d.remove("adi")
#print(d)
#print(a.count(5))
#print(a)
#a.add(34)
#print(a)
#b=a.copy()
#print(b)
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)