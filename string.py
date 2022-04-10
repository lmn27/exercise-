
# stringler hem "" hem '' hem  """ hem de ''' arasinda yazila biler

print('Hello') 
print("Hello")

a="Leman"
b='Python'
c="""Hello"""
d='''Happy'''
print(a)
print(b)
print(c)
print(d)

a='string'
print(a)
print(a[0],a[1])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[-1])
print(a[-2])
print("lenght=",len(a))
print("s" in a)
print('s' not in a)
for x in "Leman":
     print(x)

a="Hello World"
print(a)
print(a[2:])
print(a[5:])
print(a[6:])
print(a[:2])
print(a[-2:])
print(a[:-3])
print(a[1:4])
print(a[2:-2])
print(a[::-1])
print(a[0:7:2])

print(*enumerate(a))  # index ve simvol (0, 'H')
print(*enumerate(a,2))  # index nomrelemini 2den basla (2, 'H') 
print(*reversed(a))  # tersine yazilis
print(sorted(a))    # herfleri artan sira ile duzur
a = (1, 11, 2)
print(sorted(a))  # artan sira
print(sorted(a,reverse=True))  # azalan sira

ad='leman'
print(ad.replace('l','L')) # evezetme
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three",2) # 1 yazsaq ilk 1 sozu evez edecek
print(x)

uni="Dovlet Idarecilik Akademiyasi"
print(uni.split()) # bosluga gore boldu
ad="Aylin, Asim, Anar, Aytac"
print(ad.split(',')) # vergule esasen bolur
print(ad.split(" ",1)) # 1 defe bolur
print(ad.split(" ",2)) # iki defe bolur
print(ad.rsplit(" ",1)) # sagdan bolecek 1 defe

txt = "Thank you for the music\nWelcome to the jungle"
print( txt.splitlines())
print( txt.splitlines(True))

print(ad.lower()) # butun simvollar kicik
print(ad.upper()) # butun simvollar boyuk
print(ad.capitalize()) # yalniz ilk simvol boyuk
a='mother'
print(a.islower())  # butun herflerin kicik olub olmadigini yoxlayir
a="FATHER"
print(a.isupper()) #butun herflerin boyuk olub olmadigini yoxlayir
print(a.endswith("m")) # string sonu ne ile bitir
b="Hello world"
print(b.endswith("d")) # son herfi yoxlayir
print(b.startswith("H")) # ilk herfi yoxlayir

universitet = "doVlet idArecilik akadEmiyaSi"
print(universitet.title()) # setirdeki sozlerin ilk herfi boyuk
print(universitet.swapcase()) # kicik -> boyuk, boyuk -> kicik
print(universitet.casefold()) # =lower()

a="  Hello world   "
print(a.strip())  # sondan ve evelden bosluqlari silir
a="kLemankk"
print(a.strip('k'))


universitet="Dovlet idarecilik akademiyasi"
a=universitet.split()
print(" ".join(a))  # birlesdirir
print(universitet.count("a")) # a simvolunu sayir
print(universitet.count("a", 12)) # 12ci index sonra sayir
print(universitet.index("a")) # ilk a-nin index verir
print(universitet.index("a",14)) # 14den sonra ilk a-nin index
print(universitet.index("a",19,26)) 
print(universitet.rindex("a")) # sagdan yoxlayr 


a="python"
print(a.center(19,'-'))

a="Lmn"
print(a.zfill(4))

a="27"
b="27L"
c="lmn"
d="l mn*"
e="12.4"
print(a.isdigit()) # only number
print(a.isnumeric()) #only number
print(b.isdigit())  
print(b.isalpha())  # only herf
print(c.isalpha())
print(d.isalnum()) # hem herf hem reqem
print(a.isalnum())
print(b.isalnum())
print(a.isdecimal())  # natural olsa true verir
print(e.isdecimal()) 

# Format...
ad="Leman"
a=17
print("{} 11-ci sinifde oxuyur".format(ad))
print("{} 11-ci sinifde oxuyur ve onun {} yasi var ".format(ad, a))
print("|{:^15}|".format("salam"))

print('{:c}'.format(65)) # chr 
print("{:d}".format(65))  # reqem tipinde
print("{:o}".format(65)) # 8lik -> 10luq
print("{:x}".format(65)) # 16liq -> 10luq
print("{:.2f}".format(50)) # floata çeviri
print("{:,}".format(1234567890)) # mərtəbələrinə ayırır

a="Leman"
b="good"
print(a+b)
print(a+ " " +b)
print(a*2)




# ad=input("Adinizi daxil edin: ")
# soyad=input("Soyadinizi daxil edin: ")
# print("xos gelmisen {} {} ".format(ad,soyad))
# a="Leman"
# print(a[:2])
# b=len(a)
# c=a[b-2:]
# print(c)
# a='Leman'
# b='Nermin'
# c=a
# d=b
# a=a[:-1]+b[-1:]
# b=d[:-1]+c[-1:]
# print(a)
# print(b)
# for i in range(10):
#      print(i)
     
# import random
# print(random.randint(0,100))

# try:
#     a=int(input("1-ci eded daxil edin: "))
#     b=int(input("2-ci eded daxil edin:"))
#     print("a/b=",a/b)
# except ValueError:
#      print( "sadece reqem yazin"  )

# try:
#     a=int(input("1-ci eded daxil edin: "))
#     b=int(input("2-ci eded daxil edin:"))
#     print("a/b=",a/b)
# except ZeroDivisionError:
#      print( "ededi 0-a bolmek olmaz"  )

# try:
#     a=int(input("1-ci eded daxil edin: "))
#     b=int(input("2-ci eded daxil edin:"))
#     print("a/b=",a/b)
# except ZeroDivisionError:
#      print( "ededi 0-a bolmek olmaz"  )
# except ValueError:
#      print( "sadece reqem yazin"  )

try:
    a=int(input("1-ci eded daxil edin: "))
    b=int(input("2-ci eded daxil edin:"))
    print("a/b=",a/b)
except ValueError as xeta:
     print( "orginal xeta",xeta  )
      






