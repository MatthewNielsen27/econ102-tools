#!/usr/bin/env python3

import numpy as np


class Group:
    def __init__(self, num: int, duration: int):
        self.num = num
        self.duration = duration


class LabourDynamics:
    """
    This class is used to determine the steady-state characteristics of
    the labour market.

    note:   All work is done in the __repr__ function, since we don't
            often need to use the results of the computation for
            anything else.

            This is obviously bad practice, but I didn't really care
            at the time of writing the code.
    """
    def __init__(self, lf:int, groups: list):
        """
        :lf          labour force size
        :groups      (num, duration)
        """
        self.lf = lf
        self.groups = sorted(groups, key=lambda x: x.duration)

    def __repr__(self) -> str:
        # step 1, compute each row until steady state
        rows = []

        done = False
        while not done:
            month = len(rows)
            row = rows[-1].copy() if len(rows) else np.zeros(len(self.groups))

            for i, group in enumerate(self.groups):
                # Keep adding until this column is in steady state
                if month < group.duration:
                    row[i] += group.num
            
            if len(rows) and np.array_equal(row, rows[-1]):
                done = True
            
            rows.append(row)

        incidence = (sum(list(rows[0])) / self.lf) * 100

        def format_row(row, k):
            u = sum(list(row))
            ur = (u / self.lf) * 100
            return f"{k:03} | {row} | ur: {ur:4.01f}% | i: {incidence:4.01f}%"

        return "\n".join(format_row(r, i + 1) for i, r in enumerate(rows))


def main():
    print(
        LabourDynamics(
            lf=1000,
            groups=[
                Group(duration=1, num=52),
                Group(duration=2, num=55),
                Group(duration=3, num=17),
                Group(duration=4, num=15),
            ]
        )
    )


if __name__ == "__main__":
    main()
