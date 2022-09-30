n= int(input("Введите число: "))
numbers = []
work=0

for i in range (-n,n):
    new_arg=i+1
    numbers.append(new_arg)
    data = open('file.txt', 'r')
    ind= data.readlines()
ind_string = '' 
for line in ind:
        ind_string += line.strip()
        if numbers[i]==ind_string:
         work*=i
        print(numbers)

        print(work)

data.close()
