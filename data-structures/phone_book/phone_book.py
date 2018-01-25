# python3


class PhoneBook:
    def __init__(self):
        self._index = {}

    def add(self, number, name):
        self._index[number] = name

    def find(self, number):
        return self._index.get(number, 'not found')

    def delete(self, number):
        if self._index.get(number):
            del self._index[number]


def write_responses(result):
    print('\n'.join(result))


if __name__ == '__main__':
    n = int(input())
    pb = PhoneBook()
    result = []
    for i in range(n):
        op = input().split()
        if op[0] == "add":
            pb.add(op[1], op[2])
        elif op[0] == "find":
            result.append(pb.find(op[1]))
        elif op[0] == "del":
            pb.delete(op[1])
    write_responses(result)
