# Program to chek if a number is palindrome or not
# Enter a number
num=int(input("Enter any number: "))
if num==int(str(num)[::-1]):
    print("The number is palindrome")
else:    
    print("The number is not palindrome")
