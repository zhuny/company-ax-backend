import math


def solution_slow(N, n):
    doors = [0 for i in range(N)]
    for j in range(1, n+1):
        doors = [
            1-state if i % j == 0 else state
            for i, state in enumerate(doors, 1)
        ]
    return sum(doors)


def solution(N, n):
    assert N >= n

    if n == 1:
        return N

    lcm = 1
    for i in range(1, n+1):
        lcm = lcm*i//math.gcd(i, lcm)

    if N >= lcm:
        mult = solution_slow(lcm, n)
    else:
        mult = 0
    rest = solution_slow(N % lcm, n)

    return mult * (N // lcm) + rest


if __name__ == '__main__':
    print(solution_slow(50, 1))
    print(solution_slow(50, 2))
    print(solution(50, 1))
    print(solution(50, 2))


