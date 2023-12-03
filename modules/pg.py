class PG:
    @staticmethod
    def progression(vi: float,
                    v2: float) -> float:
        return vi / v2

    @staticmethod
    def nth_value(vi: float,
                  n: int,
                  q: float) -> float:
        return vi * (q ** (n - 1))

    @staticmethod
    def finite_value_sum(vi: float,
                         n: int,
                         q: float) -> float:
        return (vi * ((q ** n) - 1)) / (q - 1)

    @staticmethod
    def infinite_value_sum(vi: float,
                           q: float) -> float:
        return vi / (1 - q)
