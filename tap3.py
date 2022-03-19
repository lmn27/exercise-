password=input("Parolunuzu teyin edin: ") 
a=input("Parol qeyd edin: ")
i=0
if password==a:
    print("True...")
else:
   while i<3:
       print("Wrong")
       b=input("Parol daxil edin: ")
       i+=1
       if b==password:
           print("True")
           break
if i==3:
        print("Yeniden parol daxil etmek sansiniz yoxdur")
           
  