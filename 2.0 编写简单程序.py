def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit=9/5*celsius+32
    print("The temperature is ", fahrenheit, "degree Fahrenheit.")

main()


#1. 输出语句
#构建单行输出，默认是/n
print("Then answer is",end=" ")
print(3+4)

#2. 赋值语句
name=input("Enter your name: ")
name
#2.1赋值输入
#把文本改成求值但是很容易被攻击
ans=eval(input("Enter an expression: "))
print(ans)

#2.2同时赋值
x,y=1,2
sum,diff=x+y,x-y

x,y=y,x

# A simple program to average two exam scores
# Illustrates use of multiple input
def main():
    print("This program computes the average of two exam scores.")
    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2
    print("The average of the scores is:", average)
main()
#不适合用在字符串输入

#2.3确定循环
for i in range(10):
    x=3.9*x*(1-x)
    print(x)

for i in [10,1,2,3]:
    print(i)

for odd in [1,3,5,7,9]:
    print(odd*odd)

# A program to compute the value of an investment
# carried 10 years into the future
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(10):
        principal = principal * (1 + apr)
        print("The value in 10 years is:", principal)

main()




