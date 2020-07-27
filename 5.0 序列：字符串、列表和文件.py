# 5.1 字符串数据类型
str1="Hello"
str2="spam"
print(str1,str2)
type(str1)

first_name=input("Please enter your name: ")
print("Hello",first_name)

greet="Hello Bob"
greet[0]
print(greet[0],greet[2],greet[4])
x=8
print(greet[x-2])
greet[-1]
greet[-3]

greet[0:3]
greet[5:9]
greet[:5]
greet[5:]
greet[:]

"spam" + "eggs"
3*"Spam"
len("Spam")
for ch in "Spam!":
    print(ch, end=" ")

# 5.2 简单字符串处理
def main():
    print("This program generates computer usernames.\n")

    # get user's first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    # output the username
    print("Your username is:", uname)


main()

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

# A program to print the abbreviation of a month, given its number
def main():
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # compute starting position of month n in months
    pos = (n-1) * 3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]

    # print the result
    print("The month abbreviation is", monthAbbrev + ".")


main()


# 5.3 列表作为序列
[1,2]+[3,4]

[1,2]*3

grades=['A','B','C','D','F']
grades[0]
grades[2:4]
len(grades)

def main():
    # months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("Enter a month number (1-12): "))
    print("The month abbreviation is", months[n-1] + ".")

main()

mylist=[34,26,15,10]
mylist[2]
mylist[2]=0
mylist
mystring="Hello World"
mystring[2]
mystring[2]='z'

# 5.4 字符串表示和消息编码
ord("a")
ord("A")
chr(97)
chr(90)

# A program to convert a textual message into a sequence of
# numbers, utilizing the underlying Unicode encoding.
def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")

    # Get the message to encode
    message = input("Please enter the message to encode: ")
    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print() # blank line before prompt

main()

# 5.5 字符串方法
mystring="Hello, string methods"
mystring.split()
"32,24,25,57".split(",")

coords = input("Enter the point coordinates (x,y): ").split(",")
coords
coords[0]
coords[1]

# A program to convert a sequence of Unicode numbers into
# a string of text.
def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message
        print("\nThe decoded message is:", message)


main()

s = "hello, I came here for an argument"
s.capitalize()
s.title()
s.lower()
s.upper()
s.replace("I","you")
s.center(30)
s.count('e')
s.find(',')
" ".join(["Number", "one,", "the", "Larch"])
"spam".join(["Number", "one,", "the", "Larch"])

# 5.6 列表方法
# A program to convert a sequence of Unicode numbers into
# a string of text. Efficient version using a list accumulator.
def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        chars.append(chr(codeNum)) # accumulate new character

    message = "".join(chars)
    print("\nThe decoded message is:", message)


main()

# 5.7 输入/输出作为字符串操作
# Converts a date in form "mm/dd/yyyy" to "month day, year"
def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)


main()

str(500)
value=3.14
str(value)

# A program to calculate the value of some change in dollars
# This version represents the total cash in cents.
def main():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))


main()

#5.8 多行字符串
# Program to create a file of usernames in batch mode.
def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0]+last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)


main()






