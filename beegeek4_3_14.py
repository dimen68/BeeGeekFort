raw = input().split()
l_f = [[]]
for i in range(1, len(raw)):
    for j in range(len(raw)):
        if j + i <= len(raw):
            l_l = raw[j:j + i:]
        else:
            break
        l_f.append(l_l)
l_f.append(raw)
print(l_f)