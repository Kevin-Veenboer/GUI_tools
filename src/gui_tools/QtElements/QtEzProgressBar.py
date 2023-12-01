import time


class some_module:
    def __init__(self) -> None:
        pass

    def some_func(self, start, stop):
        for element in range(start, stop):
            print("working...")
            time.sleep(0.2)


"""
Might be able to give it the progress bar as an fucntion input?

Model and View may be allowed to have two way communication
"""


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
