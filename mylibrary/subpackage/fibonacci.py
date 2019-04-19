import numpy as np


class Fibonacci:

    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2

    def calc_sequence(self, length):

        return list(self.next_number() for i in range(length))

    def next_number(self):
        nth = self.n1 + self.n2
        # update values
        self.n1 = self.n2
        self.n2 = nth
        return nth

    def __next__(self):
        return self.next_number()