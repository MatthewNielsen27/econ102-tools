#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt


class IncomeBuckets:
    """
    Groups incomes into buckets, computes their avg and their share of total income.
    """
    def __init__(self, incomes: list = None, n: int = 0, income_avg: list = None, income_share:list = None):

        if income_share:
            self.bucket_share = income_share
            self.bucket_avg = None
            self.bucket_sum = None
            return
        elif income_avg:
            self.bucket_avg = income_avg
            self.bucket_sum = None
            
            # note: this value will be an approximation because we are
            #       projecting from the average.
            total_income = sum(self.bucket_avg)
            self.bucket_share = [(s / total_income) * 100 for s in self.bucket_avg]
            return
        else:
            self.bucket_avg = []
            self.bucket_sum = []

            # Compute the n buckets
            incomes = sorted(incomes)
            chunk_size = len(incomes) // n
            buckets = [ incomes[i:i+chunk_size] for i in range(0, len(incomes), chunk_size) ]

            # Get the avg and total income in each bucket
            for b in buckets:
                q_total = sum(b)
                self.bucket_sum.append(q_total)
                self.bucket_avg.append(q_total / len(b))

            total_income = sum(self.bucket_avg)
            self.bucket_share = [(s / total_income) * 100 for s in self.bucket_avg]


    def series(self) -> tuple:
        ys = self.cumulative()
        xs = np.linspace(0, 100, num=len(ys))
        return (xs, ys)


    def cumulative(self) -> list:
        xs = [0]
        for x in self.bucket_share:
            xs.append(xs[-1] + x)
        return xs


def gini(shares: list) -> float:
    """
    note:   shares[0]  should be 0
            shares[-1] should be 100
    """
    xs = shares.copy()
    if any([x > 1 for x in xs]):
        xs = [x / 100 for x in xs]

    n = len(xs) - 1
    return ((n - 1) / n) - (2/n) * sum(xs[0:n])


def main():
    qd = IncomeBuckets(
        income_avg=[
            114,
            288,
            605,
            621,
            1012,
            1023,
            1101,
            1434,
            1925,
            1934
        ]
    )

    # Now let's plot the lorenz curve
    plt.figure()

    xs, ys = qd.series()

    plt.plot(xs, xs, '-o', label="equality line")
    plt.plot(xs, ys, '-o', label="series")

    plt.title("Lorenz Curve")
    plt.xlabel("Cumulative households (percent)")
    plt.ylabel("Cumulative income share (percent)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
