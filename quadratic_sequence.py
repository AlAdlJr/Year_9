# Quadratic sequence calculator -  Ismail AlAdl 

# Getting the sequence and the nth number
seq_0 = input("Input a Quadrtic sequence: ").split()
n = int(input("Input the nth number of a sequence to generate: " ))

# Converting sequence from string to int
seq_1 =[int(i) for i in seq_0] 
seq_2 = []

# Finding dif_1
for i in range (len(seq_1)-1):
    seq_2.append(seq_1[i+1] - seq_1[i])

dif_1 = seq_2 [1] - seq_2 [0]

seq_3 = []

# Finding the nth sequence
x = 0
n = 0
while x != 5:
    if dif_1 == 2:
        seq_3.append((n+1) ** dif_1 )
        n=n+1
        x = x+1

# Finding dif_2
dif_2 = seq_1 [0] - seq_3 [0]
nth = (n ** 2) + dif_2

# Printing the output 
print("This is your sequence: " + str(seq_1))
print("This is the difference of your first sequence: " + str(seq_2))
print("This is the difference of your second sequence: " + str(dif_1)) 
print("This is the nth sequence: " + str(seq_3))
print("This is you Linear nth term: " + str(dif_2))
print("This is your nth term: " + str(nth))

# Launching interface - I.Aladl - 1.0

from tkinter import *
window = Tk()
window.title( ' Lable Example')
label = Label( window , str = nth)
label.pack( padx = 200 , pady = 50)
window.mainloop()
