a,b = input().split(' '),{}
for ha in a:
    if len(ha) in b:
        b[len(ha)] += 1
    else:
        b[len(ha)] = 1
print (b)