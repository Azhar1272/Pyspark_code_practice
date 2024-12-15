def findfactorial(num):
    if num == 0 or num == 1:
        return 1
    return num * findfactorial(num -1)

num = 5
result = findfactorial(num)
print("factorial of given number is :", result)
