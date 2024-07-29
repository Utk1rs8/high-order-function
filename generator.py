def gen_no(x,y):
    while x<=y:
        yield x
        x=x+1
var1=gen_no(1,10)
print(next(var1+1))
print(next(var1+2))
for i in var1:
    i=i+5
    print(i)