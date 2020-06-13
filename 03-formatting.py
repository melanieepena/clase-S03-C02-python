for i in range(1, 13):
    print("{0:2} -> {1:^3} -> {2:4}".format(i, i ** 2, i ** 3))

print()
print("-" * 50)
print()

pi = 22 / 7
print("pi is {0}".format(pi))
print("pi is {0:<12f}|".format(pi))
print("pi is {0:<12.50f}|".format(pi))
print("pi is {0:<12.2f}|".format(pi))
print("pi is {0:52.50f}|".format(pi))
print("pi is {0:62.50f}|".format(pi))
print("pi is {0:72.50f}|".format(pi))
# para rellenar con ceros los espacios
print("pi is {0:<72.72f}|".format(pi))
