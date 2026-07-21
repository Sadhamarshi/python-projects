import math


class PrimeChecker:

    def __init__(self, number):
        self.number = number

    def is_prime(self):

        if self.number <= 1:
            return False

        if self.number == 2:
            return True

        if self.number % 2 == 0:
            return False

        limit = int(math.sqrt(self.number)) + 1

        for i in range(3, limit, 2):
            if self.number % i == 0:
                return False

        return True