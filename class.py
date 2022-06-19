f=open("sample1.txt")
f.read()
filelines=f.readlines()
for line in filelines:
    print(line)


introstring="My name is harshini.I am in 9th standard."
words=introstring.split(".")
print(words)

def greet(name):
    print("hello " + name + "   How are you?")

greet("harshini")