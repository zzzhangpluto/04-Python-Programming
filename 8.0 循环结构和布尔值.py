# 8.1 常见循环模式
# 8.1.1交互式循环
def main():
    total = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        total = total + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", total / count)
main()

# 8.2.2 哨兵循环
def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", total / count)
main()

def main():
    total = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        total = total + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit) >> ")
    print("\nThe average of the numbers is", total / count)
main()

# 8.1.3 文件循环
def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
    print("\nThe average of the numbers is", total / count)
main()

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", total / count)
main()

# 8.1.4 嵌套循环
def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        # update total and count for values in line
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
            line = infile.readline()
    print("\nThe average of the numbers is", total / count)
main()

# 8.2 布尔值计算
# 优先级：(a or ((not b) and c))

# 8.3 其他常见结构
number = -1 # Start with an illegal value to get into the loop.
while number < 0:
    number = float(input("Enter a positive number: "))

while True:
    number = float(input("Enter a positive number: "))
    if number >= 0: break # Exit loop if number is valid.

number = -1 # Start with an illegal value to get into the loop.
while number < 0:
    number = float(input("Enter a positive number: "))
    if number < 0:
        print("The number you entered was not positive")

while True:
    number = float(input("Enter a positive number: "))
    if number >= 0:
        break # Exit loop if number is valid.
    else:
        print("The number you entered was not positive")


