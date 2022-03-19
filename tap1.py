#tapsiriq 1: kalkulyator proqrami qurmaq

a=input("1-ci eded: ")
b=input("2-ci eded: ")
print("1-toplama;\n2-cixma;\n3-vurma;\n4-bolme.")
print(" emeliyyatin nomresini secin:")
x=input()
if x==1:
    print(a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a*b)
elif x==4:
    print(a/b)
else:
    print("Qeyd olunan emeliyyatlari secin!!!") 
