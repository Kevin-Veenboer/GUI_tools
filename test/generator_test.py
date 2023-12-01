data_1 = range(0, 10)
data_2 = list(range(0, 10))

print(data_1)
print(data_2)


def generator_test(iterable):
    data = list(iterable)
    print("doing main work")
    for element in data:
        print("doing intermediate work")
        yield element


for val in generator_test(data_1):
    print(val)
