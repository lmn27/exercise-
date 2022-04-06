# { } istifade olunmur onun evezine bosluq qoyulur
# sherh yazmaq ucun ya "#" ya da uc dirnaqdan istifade olunur
'''uc dirnaq arasinda uzun sherhler
  yazilir
'''
"""bir nece setir serhler ucun"""


if 5>2:
   print(5)
   
'''if 5>2:
   print(5)    
   Error '''
   
"""if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!") 
 Error (Eyni kod blokunda eyni sayda boşluqdan istifadə etməlisiniz)"""
 
b='Leman'
print(b)
a="salam" # string tipinde deyisenler ya bir dirnaq ya iki dirnaqda yazilir
print(a)   
x=5  
y=3  
print("x=",x)
print("y=",y)
print(x+y)

#növü dəyişə bilərik
x = 4       # x is of type int
x = "Leman" # x is now of type str
print(x)

x="salam"
print("x=",x,type (x) )

x=5
print("x=",x,type (x) )

x,y,z="salam",5,True
print(x,y,z)

x=y=8
print("x=y=",x)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# normalda tipi bildirmeye ehtiyac yoxdur python ozu secir. tipi qeyd elemek istesek bu sekilde yaziriq
x = str(3)    # x - '3'
y = int(3)    # y - 3
z = float(3)  # z - 3.0
print(x,y,z)


#Python Data Types
x=-348763874
y=3873972867
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


#Type Conversion
x=int(20.9)
print("x=",x,type(x))

y=complex(3)
print("y=",y,type(y))

z=float(12)
print("z=",z,type(z))

#Python Operatorları
print(2+3)  
print(2.+3)
print(2-3)
print(3-2.)
print(2*3)
print(2*3.)
print(6/3)
print(7%2)
print(12%4.5)
print(2**3)
print(2.1**3)
print(12//5)  
print(8//5)
print(16**(1/2))
print(int(8**(1/3)))

x = ["apple", "banana"]
print("banana" in x)  # True

x = ["apple", "banana"]
print("pineapple" not in x) #True

print(3&5) # and
print(3|5) # or
print(3^5) # XOR
print(2<<3)  # 2*(2^3)
print(17>>3) # 17//(2^3)

a=~10  # inkar
print(a)

x=-89
print(abs(x)) # ededin modulunu tapir
# yuvarlaqlaşdırmaq
print(round(15.65) )  # 16
print(round(15.55) )  # 16
print(round(15.35) )  # 15
print(round(14.65) )  # 15
print(round(14.5) )   # 14
print(round(13.5) )   # 14
print(round(15.4575,2) )  # 15.46
print(round(21/2,3)) 

# Tam və kəsr hissəni tapir
print(divmod(16,5))  
 
#qüvvətə yüksəldir
print(pow(2,3))  # pow(x,y)=x**y

#max ve min
print(max(12,54,75,14))
print(min(12,7,5,3,98,34))
print(max("ad","367832","leman",key=len))
print(min("ad","367832","leman",key=len))


a=[2,10,8,5]
x=sum(a)
y=sum(a,6)
print(x)
print(y)

#say sistemləri 
print(bin(6))  # 10luq -> 2lik
print(bin(6)[2:]) 
x='{:b}'.format(7148)   
print(x)


print(oct(12))  # 10luq -> 8lik
print(oct(12)[2:]) 
x='{:o}'.format(7148)  
print(x)

print(hex(127))  # 10luq -> 16liq
print(hex(127)[2:])
x='{:x}'.format(7148)   
print(x)

print(int('1011',2))  # 2lik -> 10luq
print(int('116',8))   # 8lik -> 10luq
print(int('1ca',16))  # 16liq -> 10luq


print((12).bit_length())    # tam ededin yaddasda nece bit yer tutdugu
a=3.5
print(a.as_integer_ratio())   # hansi iki ededin bir birine bolunmesinden alindigini tapir

print((13.6).is_integer())     # false
print((13.0).is_integer())     # true


c=3-4j
print(c.imag)   # complex xeyali hissesini
print(c.real)  # complex real hissesini
print(c.conjugate() )  # qosmasi








    
