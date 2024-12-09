def primenumber(lst):
    nonprime = []
    prime = []
    for number in lst:
        mid = int(number/2) + 1
        for i in range(2,mid):
            if number % i == 0:
                nonprime.append(number)
                break
        else:
            prime.append(number)
                

    return ('non prime number: ', nonprime, 'prime number: ', prime)
    #return prime

lst = [2,3,4,5,6,7,8,9,10,11]
print(primenumber(lst)) #('non prime number: ', [4, 6, 8, 9, 10], 'prime number: ', [2, 3, 5, 7, 11])
#print(max(primenumber(lst)))