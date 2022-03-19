# { } istifade olunmur onun evezine bosluq qoyulur
# sherh yazmaq ucun ya "#" ya da uc dirnaqdan istifade olunur
'''uc dirnaq arasinda uzun sherhler
  yazilir
'''
if 5>2:
   print(5)
b='Leman'
print(b)
a="salam" # string tipinde deyisenler ya bir dirnaq ya iki dirnaqda yazilir
print(a)   
x=5  
y=3  
print("x=",x)
print("y=",y)
print(x+y)
x=4  # x integer tipindedir
y="Leman" # y  string tipindedir
print("x=",x,type (x) )
x="salam"
print("x=",x,type (x) )
x=5
x,y,z="salam",5,True
print(x,y,z)
x=y=8
print("x=y=",x)
x=int(30) # normalda tipi bildirmeye ehtiyac yoxdur python ozu secir. tipi qeyd elemek istesek bu sekilde yaziriq
print(x)
x=-348763874
y=38739728678
print("x=",x,type (x) )
print("y=",y,type (y) )
x=10.8
y=-9.7
z=35e3
k=12E4
print("x=",x,type (x) )
print("y=",y,type (y) )
print("z=",z,type (z) )
print("k=",k,type (k) )
x=1+3j
y=1+7j
print("x=",x,type(x))
print("x+y=",x+y)
x=int(20.7)
print("x=",x,type(x))
y=complex(3)
print("y=",y,type(y))
x=-89
print(abs(x)) # modul tap
print(round(21/2,3)) # yuvarlaqlaşdırmaq
print(divmod(16,5))   # Tam və kəsr hissəni tap
print(pow(2,3))
print(max("ad","367832","leman",key=len))
print(min("ad","367832","leman",key=len))
a=[2,10,8,5]
x=sum(a)
print(x)
# y=bin(1)[2:]
# print(y)
x='4875'
y=int(x)
print("y=",type(y))
a=~10
print(a)
x=oct(18)
print(x)
x=int('7bc',16)   
print(x)
x='{:b}'.format(7148)   # 10-->2
print(x)
x='{:o}'.format(7148)   # 10-->8
print(x)
x='{:x}'.format(7148)   # 10-->16
print(x)
x=12
print(a.bit_length()	)
c=3+4j
print(c.imag)
print(c.real)
print(c.conjugate() )








    
