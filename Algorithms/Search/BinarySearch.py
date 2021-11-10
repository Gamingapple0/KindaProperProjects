# Completion time 2 hrs
class BinarySearch:
    def __init__(self, array, sel, recursion=False):
        self.array = array
        self.sel = sel
        self.lowest_index = 0
        self.highest_index = len(array) - 1  # -1 since indexing starts at 0 and the last val's index would be 11,
        self.res = None  # whereas len would provide 12 which would cause an 'out of index' error
        if recursion:
            self.recursive(array, sel, self.lowest_index, self.highest_index)
        else:
            self.iteration()

    def __str__(self):
        return 'Index: ' + str(self.res)

    def recursive(self, arr, sel, lowest_index, highest_index):

        # Low and high are required to traverse through the list
        # while keeping track of their indexes without having to create a new list after each recursion

        # To check if the number is even in the list,
        # as -1 being gt 0 would mean even after going through the entire list the could not be found
        if highest_index < lowest_index:
            self.res = -1
            return
        mid = (highest_index + lowest_index) // 2
        if arr[mid] == sel:
            self.res = mid
            return
        if sel > arr[mid]:
            return self.recursive(arr, sel, mid + 1, highest_index)
        return self.recursive(arr, sel, lowest_index, mid - 1)

    def iteration(self):
        while self.highest_index >= self.lowest_index:
            mid = (self.lowest_index + self.highest_index) // 2
            if self.array[mid] == self.sel:
                self.res = mid
                return
            elif self.array[mid] > self.sel:
                self.highest_index = mid - 1
            else:
                self.lowest_index = mid + 1
        self.res = -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    a = BinarySearch(arr, 8, recursion=True)
    b = BinarySearch(arr, 7)
    print(a, b)
