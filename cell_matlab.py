def cell(a, b):
    outer = []
    for i in range(1,a+1):
        for j in range(1,b+1):
            inside = []
            inside.append(i)
            inside.append(j)
            outer.append(inside)
    for i in outer:
        i.clear()
    return outer

if __name__ == "__main__":
    A = cell(1,10)
    print(A)
