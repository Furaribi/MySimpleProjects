prime_numbers=[]
#just in case to see how many prime numbers there
validinput=True
try:
    d = int(input('inter the total numbers you want to check here: '))
except ValueError:
    print('pls inter a valid number!')
    validinput = False
if validinput:
    for n in range(2, d+1):
        prime=True
#you can use -> int(n**0.5)+1
#but i didn't cuz easier to understand...
        for i in range(2 , n):
            x=n%i
            if x==0:
                prime=False
                break
        if prime==True:
            prime_numbers.append(n)

print('there is output:', prime_numbers)
print(f'there was {len(prime_numbers)} prime number.')