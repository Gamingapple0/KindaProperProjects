# Completion time 10 mins

from operator import lt, gt


class BubbleSort:
    def __init__(self, array, ascending=True):
        self.array = array
        self.asc = ascending
        self.sort()

    def sort(self):
        length = len(self.array)
        swapped = False
        op = gt
        if self.asc:
            op = lt
        for i in range(1, length + 1):
            for j in range(length - i):
                curr = self.array[j]
                next = self.array[j + 1]
                if op(next,curr):
                    swapped = True
                    self.array[j + 1], self.array[j] = curr, next
            if not swapped:
                break
        print(self.array)


if __name__ == '__main__':
    arr = [2, 4, 5, 25, 7, 8, 16, 3, 1, 9, 23, 65, 7, 55, 65, 42, 64, 5, 25, 11, 234, 22, 34, 56, 75, 4, 22]
    a = BubbleSort(arr, ascending=True)
