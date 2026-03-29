import random


def add(a: int, b: int) -> int:
    return a + b


def main():
    x, y = random.randint(1, 100), random.randint(1, 100)
    result = add(x, y)
    print(f"{x} + {y} = {result}")


if __name__ == "__main__":
    main()
