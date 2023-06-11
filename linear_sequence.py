# Linear Sequence - Ismail AlAdl

# Input sequence and nth term
seq = input("Input a linear sequence: ").split()
nth = int(input("input the nth term of the sequence: "))

# Converting sequence from string to int
seq =[int(i) for i in seq] 

# Operation
dif = seq[1] - seq[0]  
seq_dif = seq[0] - dif
nth_output = ((dif * nth) + seq_dif)

# Output
print ("Your sequence is ", seq)
print ("The ", str(nth),"th number is",str(nth_output))