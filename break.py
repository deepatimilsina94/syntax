
i=1
while i <=1000:
    i = i + 1 #update rokcha infinite loop lai
    if i == 100:
        break
    print(i)

    if i%2==0:
        continue # continue bhetne bitikai tala jadaina so always use break up
    if i == 100:
        break
    print(i)
    i = i + 1 #update rokcha infinite loop lai

def add(*args):
    total = 0
    for i in args:
        total +=i
    print (total)

add(1,2,3,4,5)

