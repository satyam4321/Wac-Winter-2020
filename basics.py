# print(True and True)
'''comparision operators
'''
# n = int(input("enter a number: "))
# if n%2 == 0:
#     print("even")
# else:
#     print("odd")

# n = 9

# if n > 10 :
#     print("larger")
# else :
#     print("smaller")

# n = int(input("enter a number: "))

# if n%3 == 0 :
#     print("remainder: 0")
# elif n%3 == 1 :
#     print("remainder: 1")    
# else:
#     print("remainder: 2")    


# n = int(input("Enter a number: "))

# if n%3 == 0 and n%5 == 0 :
#     print("FizzBuzz")
# elif n%5 == 0 :
#     print("Buzz")
# elif n%3 == 0 :
#     print("Fizz") 
# else:
#     print(n)           


# calculator

# n = int(input("Enter first Number : "))
# m = int(input("Enter second Number : "))

# op = input("Enter operator : ")

# if op == '+' :
#     print(n+m)
# elif op == '-' :
#     print(n-m)
# elif op == '/' :
#     print(n/m)
# elif op == '*' 
#     print("wrong operator")        


# Leap Year

# y = int(input("year: "))
# if y%100 == 0 and y%400 != 0 :
#     print("not a leap year")
# elif y%400 == 0 :
#     print("leap year")
# elif y%4 == 0 :
#     print("leap year")
# else :
#     print("not a leap year")        


# n = int(input("enter a year : "))

# if n % 400 == 0 :
#     print("leap year")
# else:
#     if n % 100 == 0 :
#         print("not a leap year")
#     elif n % 4 == 0 :
#         print("leap year")
#     else:
#         print("not a leap year")



# print('hello \n' * 10)


# count = 1
# limit = 10

# while count <= limit :
#     count += 1
#     print("Hello")


# number = int(input("Enter a number : "))

# for item in range(1, 11) :
#     print(item * number)

# n = int(input())

# sum = 0
# for i in range(1, n+1) :
#     sum += i
# print("sum is:", sum)

# n = int(input())
# fact = 1
# for i in range(1, n+1) :
#     fact = fact*i 
# print("factorial is : ",fact)

# nested loops

# for i in range(5) :
#     for j in range(5) :
#         print(i ,sep ='')
#     print()    
# n = int(input())
# for i in range(n) :
#     for j in range(n):
#         print('*', end = '')
#     print()  


# n = int(input())

# for i in range(n) :
#     print('* ' * (i+1))

# for i in range(n):
#     for j in range(i+1):
#         print('*', end = '')
#     print()

# n = int(input("Enter a number : "))

# is_prime = True

# for i in range(2, n) :
#     if n%i == 0 :
#         is_prime = False
#         break
# if is_prime :
#     print("it is a prime number")
# else :
#     print("not a prime number")       
#     # nCr 

n = int(input())

for i in range(n) :
    for j in range(i + 1) :
        print(i+1, end = '' )
    print()    