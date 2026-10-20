#add multiples of 7 in a list from 1 to 100

multiples=[]

for i in range(1,101):
    if i % 7 ==0:
        multiples.append(i)

print(multiples)