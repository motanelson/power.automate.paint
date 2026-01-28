x=200
y=200
c=0
outs="bitmap.dat"
print( "\n\033c\033[40;37m\ngive the x value of the table ? ")
x=int(input())
print( "\n\033[40;37m\ngive the y value of the table ? ")
y=int(input())
print( "\n\033[40;37m\ngive the color fro 0 to 15 ? ")
c=int(input())
c=chr(c)
f1=open(outs,"wb")
for yy in range(y):
    
    for xx in range(x):
        f1.write(c.encode())
    f1.write(chr(32).encode())
f1.close()