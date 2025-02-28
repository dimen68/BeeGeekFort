n = int(input())
k = int(input())-1
d = []
for i in range( n ):
    d.append(i+1)
nach=0
while len(d) > 1:
    for j in range(nach, len(d), k):
        if j+k<len(d):
            d.pop(j+k)
            if len(d)==1:
                break
        else:
            nach=(j+k)-len(d)
            if nach>len(d):
                nach-=len(d)
            d.pop(nach)
            break
print(d[0])



