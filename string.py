
# print('Hello') # stringler hem "" hem '' hem  """ hem de ''' arasinda yazila biler
# print("Hello")
# a='simvol'
# b="Leman"
# c="""hello"""
# d='''Happy'''
# print(a)
# print(b)
# print(c)
# print(d)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[-1])
# print(a[-2])
# print(len(a))
# a='Salam dunya'
# print(a[3:])
# print(a[:3])
# print(a[2:])
# print(a[1:4])
# print(a[2:-2])
# print(a[2:5])
# print(a[:5])
# for x in "banana":
#     print(x)
# text="The best things in life are free!"
# print("free" in text)
# print("lmn" in text)
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# a="Nermin"
# print(a.upper())
# print(a.lower())
# print(*reversed(a))
# a="Leman, Nermini, cox, isteyir"
# adlar="Aylin asim seher"
# print(a.split(",", 1))
# print(a.rsplit(",", 2))
# print(a.rsplit(",", 1))
# print(a.isupper())
# print(a.lower())
# print(a.upper())
# print(a.capitalize())
# print(a.endswith("r"))
# print(a.startswith("l"))
# print(a.startswith("L"))
# print(a.title())
# print(a.swapcase())
# print(a.casefold())
# print(a.strip())
# print(a.strip('k'))
# c="salam"
# d="a"
# print(c+d)
# print(c*2)
# print(a.count('a'))
# print(a.index('a', 2))
# print(a.rindex('a', 3))
# a="python"
# print(a.center(10))
# print(a.center(10,'*'))
# x='12'
# y='lmn'
# z='lmn27'
# print(x.zfill(5))
# print(x.isdigit())
# print(y.isnumeric())
# print(x.isalpha())
# print(y.isalpha())
# print(x.isalnum())
# print(z.isalnum())
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
      






