# This program is used to find the Fibonacci sequence up to a certain number of terms
# Enter the number of terms you want in the Fibonacci sequence
n=int(input("Enter any number: "))
# First two terms of the Fibonacci sequence
first_num=0
second_num=1
# Loop to generate the Fibonacci sequence
for i in range(n):
    print(first_num)
    # Update the values of first_num and second_num
    first_num=first_num+second_num
    second_num=first_num-second_num

