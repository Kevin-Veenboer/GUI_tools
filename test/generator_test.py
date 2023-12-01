import time

data_1 = range(0, 17)
data_2 = list(range(0, 10))

print(data_1)
print(data_2)


def generator_test(iterable):
    data = list(iterable)
    total = len(data)
    count = 0
    print(f"at {(count/total)*100}% of total")

    for element in data:
        # simulating work
        time.sleep(0.3)
        count += 1
        print(f"at {(count/total)*100}% of total")
        yield element


for val in generator_test(data_1):
    print(val)
