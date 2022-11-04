import datetime
dt_now = datetime.datetime.now()
log=eval(input("Ведите искомое: "))
print (log)
print (dt_now)
with open("res.txt","a+") as file:
        file.write(str(dt_now) + '      ')
        file.write(str(log) + '\n')
