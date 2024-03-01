# 1. Program to find the sum and calculate the average of ‘n’ numbers in a list.
n = int(input("Enter the number of elements: "))
list_num = []
for i in range(0, n):
    list_num.append(int(input("Enter the number: ")))

SumOfNumbers = sum(list_num)
Average = SumOfNumbers/n
print("The sum of numbers:", SumOfNumbers)
print("The average of numbers:", Average)
print("---------------------------")

# 2. Print both the list before multiplying and the list after multiplied by the number ‘m’.
num = int(input("Enter the number of elements: "))
numbers = []
for i in range(0, num):
    numbers.append(int(input("Enter the number: ")))
print("Original list:", numbers)
m = int(input("Enter the number for multiplication: "))
for i in range(0, num):
    numbers[i] = numbers[i]*m
print("Modified list:", numbers)
print("---------------------------")
