import math
n = 2022
x = math.pi   # save with 5 digits after a dot (import 'math' first!)
word = "Python"
polish = "książka"   # 'book' in English

with open('vars.txt', 'w') as outfile:   
    outfile.write(f"{n}\n{x:.5f}\n{word}\n{polish}\n")

with open('vars.txt', 'r') as infile:
    L = infile.readlines()

for i in L:
    print(i)