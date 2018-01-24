class SetUnionRank:

    def __init__(self, arr):
        self.parents = arr
        self.ranks = [0] * self.size

    @property
    def size(self):
        return len(self.parents)

    def find(self, i):
        while i != self.parents[i - 1]:
            i = self.parents[i - 1]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.ranks[i_id - 1] > self.ranks[j_id - 1]:
            self.parents[j_id - 1] = i_id
        else:
            self.parents[i_id - 1] = j_id
            if self.ranks[i_id - 1] == self.ranks[j_id - 1]:
                self.ranks[j_id - 1] += 1


class SetUnionRankPathCompression:

    def __init__(self, arr):
        self.parents = arr
        self.ranks = [0] * self.size

    @property
    def size(self):
        return len(self.parents)

    def find(self, i):
        if i != self.parents[i - 1]:
            self.parents[i - 1] = self.find(self.parents[i - 1])
        return self.parents[i - 1]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.ranks[i_id - 1] > self.ranks[j_id - 1]:
            self.parents[j_id - 1] = i_id
        else:
            self.parents[i_id - 1] = j_id
            if self.ranks[i_id - 1] == self.ranks[j_id - 1]:
                self.ranks[j_id - 1] += 1
