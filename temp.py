n=6
xs = []
for i in range(n//2):
    xs.append(int(str(10**i)*(n//(i+1)))/(10**i))
print(xs)