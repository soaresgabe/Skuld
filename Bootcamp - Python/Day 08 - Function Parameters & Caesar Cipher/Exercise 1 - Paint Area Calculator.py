# number of cans = (wall height โ๏ธ wall width) รท coverage per can.
#Write your code below this line ๐
from math import ceil

def paint_calc(height, width, cover):
    print(f"You'll need {ceil(height * width / cover)} cans of paint.")
#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)