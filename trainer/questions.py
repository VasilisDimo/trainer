import math
import random

LOW, HIGH = 0, 10


def random_float():
    x = random.randint(LOW, HIGH) + random.randint(1, 9) / 10 
    return random.choice([x, -x])


def q_floor():
    x = random_float()
    return f"math.floor({x})", math.floor(x)


def q_ceil():
    x = random_float()
    return f"math.ceil({x})", math.ceil(x)


def q_trunc():
    x = random_float()
    return f"math.trunc({x})", math.trunc(x)


def q_hypot():
    k = random.randint(1, 9)
    return f"math.hypot(3 * {k}, 4 * {k})", int(math.hypot(3 * k, 4 * k))


def q_sqrt():
    n = random.randint(2, 30)
    return f"math.sqrt({n * n})", int(math.sqrt(n * n))


def q_factorial():
    n = random.randint(3, 6)
    return f"math.factorial({n})", math.factorial(n)


KINDS = [q_floor, q_ceil, q_trunc, q_hypot, q_sqrt, q_factorial]


def make_question():
    text, answer = random.choice(KINDS)()
    assert isinstance(answer, int)
    #assert LOW >= answer or answer>= HIGH
    return text, answer


if __name__ == "__main__":
    random.seed(2026)
    for i in range(6):
        text, answer = make_question()
        print(f"{text} = {answer}")