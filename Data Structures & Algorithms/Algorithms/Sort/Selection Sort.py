# Completion time 45 mins

from operator import lt, gt


class SelectionSort:
    def __init__(self, array, ascending=True):
        self.array = array
        self.asc = ascending
        self.sort()

    def sort(self):
        length = len(self.array)
        lowest = self.array[0]
        op = lt
        if self.asc:
            op = gt
        loc = 0  # Index of the lowest number, initialized as a formality to avoid PEP annoying me
        for i in range(length):
            for j in range(i, length):
                curr = self.array[j]

                # Index of the number that will be swapped,since the lowest will always be in this index after each iter
                # [3,2,4,1] i = 0, a.k.a 3; swap_index = 1, a.k.a 2

                if j == i:  # Pick lowest val from arr
                    lowest = self.array[i]
                    loc = j

                if op(lowest,curr):  # Chooses to order it in either descending or ascending format
                    lowest = curr
                    loc = j
            self.swap(i, self.array[i], loc, lowest)    # Swaps 2 values in the array
        print(self.array)

    def swap(self, pos1, val1, pos2, val2):  # Could've used a,b = b,c but, I forgor lol
        temp = val1
        self.array[pos1] = val2
        self.array[pos2] = temp


if __name__ == '__main__':
    arr = [2, 4, 5, 25, 7, 8, 16, 3, 1,23,65,7,55,65,42,64,5,25, 11, 234, 22, 34, 56, 75, 4, 22]
    a = SelectionSort(arr,False)
