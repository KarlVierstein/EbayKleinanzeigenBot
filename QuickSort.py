class QuickSort:
    def __init__(self, unsorted_list):
        self.unsorted_list = unsorted_list

    def quick_sort(self):
        self.quick_sort_helper(self.unsorted_list, 0, len(self.unsorted_list) - 1)

        return self.get_unsorted_list()

    def quick_sort_helper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)

            self.quick_sort_helper(alist, first, splitpoint - 1)
            self.quick_sort_helper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    def get_unsorted_list(self):
        return self.unsorted_list