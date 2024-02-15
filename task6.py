a = "1 0 2 0 3 0 4 0 5".split(" ")
b = [i for i in a if i != "0"]
c = len(a) - len(b)
b += ["0" for _ in range(c)]
print(" ".join(b))














