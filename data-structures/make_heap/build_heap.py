# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        self.size = len(self._data)
        assert n == self.size

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def child_index(self, index, side='left'):
        if side == 'left':
            plus = 1
        elif side == 'right':
            plus = 2
        else:
            return -1
        child_index = 2 * index + plus
        if child_index >= self.size:
            return -1
        return child_index

    def sift_down(self, i):
        min_index = i
        l = self.child_index(i, side='left')
        r = self.child_index(i, side='right')

        if l != -1 and self._data[l] < self._data[min_index]:
            min_index = l

        if r != - 1 and self._data[r] < self._data[min_index]:
            min_index = r

        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = \
                self._data[min_index], self._data[i]
            self.sift_down(min_index)

    def generate_heap(self):
        size = len(self._data)
        for i in range(size // 2, -1, -1):
            self.sift_down(i)

    def generate_swaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
