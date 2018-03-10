import copy

a=[1,2,3,['a','b','c'],4]

b= a

c = copy.copy(a)

d = copy.deepcopy(a)

print("a.id:",id(a))
print("a[3]:",a[3])
print("a[3].id",id(a[3]))
print("b.id:",id(b))
print("b[3].id",id(b[3]))
print("c.id:",id(c))
print("c[3].id",id(c[3]))
print("d.id:",id(d))
print("d[3].id",id(d[3]))

a.append(5)
print("---a.append(5)---")
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

a[3].append('e')
print("---a[3].append('e')---")
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
