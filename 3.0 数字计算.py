#3.1 数值数据类型
type(3)
type(3.14)
type(3.0)
myInt=-32
type(myInt)
myFloat=32.0
type(myFloat)

#3.2 类型转换和舍入
round(3.14)
pi=2.1415926
round(pi,2)
round(pi,3)

int("32")
float("32")
float("9.8")

# A program to calculate the value of some change in dollars
def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = .25*quarters + .10*dimes + .05*nickels + .01*pennies
    print()
    print("The total value of your change is", total)


main()
#在input中使用Int而不是eval刻意确保用户只输入有效的整数，但但不支持同时输入

#3.3 使用math库
# A program that computes the real roots of a quadratic equation.
# Illustrates use of the math library.
# Note: This program crashes if the equation has no real roots.
import math # Makes the math library available.
def main():
    print("This program finds the real solutions to a quadratic")
    print()
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print()
    print("The solutions are:", root1, root2 )


main()

#3.4 累计结果：阶乘
list(range(10))
list(range(5,10))
list(range(5, 10, 3))

# Program to compute the factorial of a number
# Illustrates for loop with an accumulator
def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()


