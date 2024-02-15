a = [list(i) for i in input()]
for x in range(len(a)):
    for j in range(len(a)):
        if x != j and a[x] == a[j]:
            break
    else:
        print(a[x], end=" ")





