log=eval(input("Ведите искомое: "))
print (log)

with open("res.txt","a+") as file:
        file.write(str(log))
