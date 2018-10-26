import time
from random import randint
from sorting_algs import Sorting_algs

class Test():
    NUM_ITER = 1000
    LIST_LENGTH = 500
    MAX_VAL = 10000

    def __init__(self):
        self.sorter = Sorting_algs()
        self.incorrect = 0

    def print_incorrect(self):
        if self.incorrect == 0:
            print ('All tests passed without errors.')
        else:
            print (self.incorrect, 'tests passed with errors.')

    @staticmethod
    def print_nicely(alg_def):
        return alg_def.replace('.', ' ').split()[2]

    def binary_test(self):
        self.test_sorted_search(self.sorter.binary_search)

    def bubble_test(self):
        self.test_sorter(self.sorter.bubble_sort)

    def insertion_test(self):
        self.test_sorter(self.sorter.insertion_sort)

    def selection_test(self):
        self.test_sorter(self.sorter.selection_sort)

    def merge_test(self):
        self.test_sorter(self.sorter.merge_sort)

    def test_sorted_search(self, search_alg):
        print(self.print_nicely(str(search_alg)), 'performance:')
        num_incorrect = 0
        start = time.time()
        for _ in range(self.NUM_ITER):
            temp = sorted(list(set([randint(0, self.MAX_VAL) for _ in range(self.LIST_LENGTH)])))
            index = randint(0, len(temp) - 1)
            if search_alg(temp, temp[index]) != index:
                print(search_alg(temp, temp[index]))
                num_incorrect += 1
        print ('\t Time elapsed: ', time.time() - start)
        print('\tPercent correct:', 100 * (self.NUM_ITER - num_incorrect) / self.NUM_ITER)
        if num_incorrect != 0:
            self.incorrect += 1

    def test_sorter(self, sort_alg):
        print(self.print_nicely(str(sort_alg)), 'performance:')
        num_incorrect = 0
        start = time.time()
        for _ in range(self.NUM_ITER):
            temp = [randint(0, self.MAX_VAL) for _ in range(self.LIST_LENGTH)]
            if sort_alg(temp) != sorted(temp):
                num_incorrect += 1
        print ('\t Time elapsed: ', time.time() - start)
        print('\tPercent correct:', 100 * (self.NUM_ITER - num_incorrect) / self.NUM_ITER)
        if num_incorrect != 0:
            self.incorrect += 1

t = Test()
t.binary_test()
t.bubble_test()
t.insertion_test()
t.selection_test()
t.merge_test()
t.print_incorrect()