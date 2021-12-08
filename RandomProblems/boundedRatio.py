def boundedRatio(a, l, r):
    b = []
    i = 0#index
    x = a[i]#the element

    while l < x < r and a[i] is (i + 1) * x:
        i += 1
        b.append(True)
    else:
        i += 1
        b.append(False)
        if len(a) == len(b):
            print(b)

    return b 
print(boundedRatio([2,1,5,7], 1, 3))
