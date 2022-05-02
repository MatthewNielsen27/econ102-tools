#!/user/bin/env python3

import math


class Chart:
    def __init__(self, p: list, q: list):
        self.p = p
        self.q = q


def pp(src: Chart, ref: Chart) -> float:
    """
    :returns the paasche price index of 'src' at 'ref' (base 100)
    """
    top = sum([p*q for p, q in zip(src.p, src.q)])
    bot = sum([p*q for p, q in zip(ref.p, src.q)])
    return (top / bot) * 100


def lp(src: Chart, ref: Chart) -> float:
    """
    :returns the laspeyres price index of 'src' at 'ref' (base 100)
    """
    top = sum([p*q for p, q in zip(src.p, ref.q)])
    bot = sum([p*q for p, q in zip(ref.p, ref.q)])
    return (top / bot) * 100


def pq(src: Chart, ref: Chart) -> float:
    """
    :returns the paasche quantity index of 'src' at 'ref' (base 100)
    """
    top = sum([p*q for p, q in zip(src.p, src.q)])
    bot = sum([p*q for p, q in zip(src.p, ref.q)])
    return (top / bot) * 100


def lq(src: Chart, ref: Chart) -> float:
    """
    :returns the laspeyres quantity index of 'src' at 'ref' (base 100)
    """
    top = sum([p*q for p, q in zip(ref.p, src.q)])
    bot = sum([p*q for p, q in zip(ref.p, ref.q)])
    return (top / bot) * 100


def fq(src: Chart, ref: Chart) -> float:
    """
    :returns the fisher quantity index of 'src' at 'ref' (base 100)
    """
    return math.sqrt(lq(src, ref) * pq(src, ref))


def fp(src: Chart, ref: Chart) -> float:
    """
    :returns the fisher price index of 'src' at 'ref' (base 100)
    """
    return math.sqrt(lp(src, ref) * pp(src, ref))


def main():
    basket_1990 = Chart(
        p=[10,  39,  11],
        q=[80, 50, 58]
    )

    basket_1995 = Chart(
        p=[23,  45,  17],
        q=[95, 58,  63]
    )

    basket_2000 = Chart(
        p=[27, 43, 22],
        q=[127, 70,  90]
    )

    basket_2005 = Chart(
        p=[30, 55, 25],
        q=[140, 66, 109]
    )

    print(pp(basket_2005, basket_2000))

    # print(f'a. {lq(basket_1990, basket_2000)}')
    # print(f'b. {lp(basket_2005, basket_1995)}')
    # print(f'c. {pq(basket_1990, basket_2000)}')
    # print(f'd. {pp(basket_2005, basket_1995)}')
    # print(f'e. {fp(basket_1990, basket_2000)}')

    # chained = (fp(basket_1995, basket_1990) / 100) * (fp(basket_2000, basket_1995) / 100) * 100
    # print(f'f. {chained}')


if __name__=='__main__':
    main()
