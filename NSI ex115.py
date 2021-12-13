def nb_triplet(x):
    n = 0
    for c in range(x + 1):
        for b in  range(c):
            for a in range(b):
                if a**2 + b**2 == c**2:
                    n += 1
    return n

print(nb_triplet(100))