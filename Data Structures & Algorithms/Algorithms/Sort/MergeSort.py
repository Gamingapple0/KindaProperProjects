from operator import lt, gt


# Completion time 5 hrs
class MergeSort:
    def __init__(self, arr, ascending=True):
        self.res = []
        self.op = lt
        self.ascending = ascending
        if ascending:
            self.op = gt
        self.sort(arr)

    def __str__(self):
        return str(self.res)

    def sort(self, arr):
        len_arr = len(arr)
        if len_arr == 1:
            return arr
        mid = len_arr // 2
        arr1 = self.sort(arr[:mid])  # Sort left
        arr2 = self.sort(arr[mid:])  # Sort right
        len_arr1 = len(arr1)
        len_arr2 = len(arr2)
        arr3 = []
        tot_len = len_arr1 + len_arr2
        index1 = index2 = 0
        for i in range(tot_len):
            if len_arr1 <= index1:  # If arr1 is empty just append the rest of arr2
                arr3.append(arr2[index2])
                index2 += 1
                continue
            elif len_arr2 <= index2:  # If arr2 is empty just append the rest of arr1
                arr3.append(arr1[index1])
                index1 += 1
                continue
            if self.op(arr1[index1], arr2[index2]):  # Main operation
                arr3.append(arr2[index2])
                index2 += 1
            else:
                arr3.append(arr1[index1])
                index1 += 1
        self.res = arr3
        return arr3


if __name__ == '__main__':
    a = [2, 1, 4, 5, 6, 7, 1, 0, 4, 9, 3, 8, 11, 2, 10, 34, 6, 22, 34, 67, 86, 42]
    b = MergeSort(a)
    print(b)
