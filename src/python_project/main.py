import random

from python_project.operations import add, mul


def main():
    x, y = random.randint(1, 100), random.randint(1, 100)
    result = add(x, y)
    print(f"{x} + {y} = {result}")
    result = mul(x, y)
    print(f"{x} * {y} = {result}")


if __name__ == "__main__":
    main()
