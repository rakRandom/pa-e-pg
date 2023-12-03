class PA:
    @staticmethod
    def progression(vi: float,
                    v2: float) -> float:

        return v2 - vi

    @staticmethod
    def nth_value(vi: float,
                  n: int,
                  r: float) -> float:

        return vi if n == 1 else vi + (n - 1) * r

    @staticmethod
    def value_sum(vi: float,
                  n: int,
                  r: float) -> float:

        return vi if n == 1 else (vi + PA.nth_value(vi, n, r)) * n / 2
