#ex1
result = []
for i in range(2000, 3000+1):
    if (i % 7 == 0) and (i %5 != 0):
        result.append(str(i))

print(','.join(result))

#ex2:
