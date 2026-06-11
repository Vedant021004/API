import pandas as pd
from pathlib import Path
import os 
# age  = int(input("Please enter your age: "))
f = open("ridvedk.txt",'r')
# f.write(str(age)) 
# print(f.read())
path = Path("ridvedk.txt")
print(os.path.isfile("ridvedk.txt"))

f.close()
