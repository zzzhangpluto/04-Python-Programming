# 11.1 应用列表
list(range(10))
"This is an ex-parrot".split()

lst=[1,2,3,4]
3 in lst
5 in lst
ans='Y'
ans in 'Yy'
lst[3]="Hello"
lst[1:3]=["Slice", "Assignment"]
lst

odds = [1, 3, 5,7, 9]
food = ["spam", "eggs", "back bacon"]
silly = [1, "spam", 4, "U"]
empty = []

def getNumbers():
    nums = [] # start with an empty list
    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x) # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos-1]) / 2
    else:
        med = nums[midPos]
    return med

from math import sqrt

def getNumbers():
    nums = [] # start with an empty list
    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x) # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num-xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        med = nums[midPos]
    return med

def main():
    print("This program computes mean, median, and standard deviation.")

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print("\nThe mean is", xbar)
    print("The standard deviation is", std)
    print("The median is", med)


if __name__ == '__main__': main()

# 11.2 记录的列表
# A program to sort student information into GPA order.

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".
                format(s.getName(), s.getHours(), s.getQPoints()),
            file=outfile)
    outfile.close()

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(key=Student.gpa)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)


if __name__ == '__main__': main()

# 11.3 用列表和类设计
from graphics import *
class DieView:
    """ DieView is a widget that displays a graphical representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
            d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0  # half of size
        offset = 0.6 * hsize  # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
        # Create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx - offset, cy - offset),
                     self.__makePip(cx - offset, cy),
                     self.__makePip(cx - offset, cy + offset),
                     self.__makePip(cx, cy),
                     self.__makePip(cx + offset, cy - offset),
                     self.__makePip(cx + offset, cy),
                     self.__makePip(cx + offset, cy + offset)]

        # Create a table for which pips are on for each value
        self.onTable = [[], [3], [2, 4], [2, 3, 4],
                        [0, 2, 4, 6], [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]
        self.setValue(1)

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)
        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

# 11.4 无顺序集合
passwd = {"guido":"superprogrammer", "turing":"genius", "bill":"monopoly"}
passwd["guido"]
passwd["bill"]
passwd["bill"] = "bluescreen"
passwd

passwd['newuser'] = 'ImANewbie'
passwd

list(passwd.keys())
list(passwd.items())
"bill" in passwd
passwd.get('bill','unknown')
passwd.get('john','unknown')
passwd.clear()

def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words.
    n = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))


if __name__ == '__main__': main()


