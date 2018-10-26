class Sorting_algs():
    @staticmethod
    def binary_search(lst, targ, sort = None):
        """
        @param list[int] lst: ordered list
        @param int targ: element to find
        @param sort: optional ordering comparison
        @return int: index of target
        Finds index of target element by recursively halving the list
        """
        def helper(lh, rh):
            if rh >= lh:
                pivot = lh + (rh - lh) // 2
                if lst[pivot] == targ:
                    return pivot
                elif lst[pivot] < targ:
                    return helper(pivot + 1, rh)
                else:
                    return helper(lh, pivot - 1)
            else:
                return -1
        return helper(0, len(lst) - 1)

    @staticmethod
    def bubble_sort(lst, sort = None):
        """
        @param list[int] lst: unordered list
        @return list[int]: ordered list according to sort
        Repeatedly iterates through the list, swapping adjacent elements
            according to sort
        """
        while True:
            numChanges = 0
            for i in range(len(lst) - 1):
                if lst[i + 1] < lst[i]:
                    lst[i + 1], lst[i] = lst[i], lst[i + 1]
                    numChanges += 1
            if numChanges == 0: # list is sorted
                return lst

    @staticmethod
    def insertion_sort(lst, sort = None):
        """
        @param list[int] lst: unordered list
        @return list[int]: ordered list according to sort
        Sorts list by moving through list and inserting elements
            and creating an ordered sublist
        """
        for i in range(len(lst)):
            index = i
            while index > 0: # insert elem at correct index in sorted sublist
                if lst[index] < lst[index - 1]:
                    lst[index], lst[index - 1] = lst[index - 1], lst[index]
                    index -= 1
                else:
                    break
        return lst

    @staticmethod
    def selection_sort(lst, sort = None):
        """
        @param list[int] lst: unordered list
        @return list[int]: ordered list according to sort
        Sorts the list by iterating through the list and 
            swapping to create an ordered sublist
        """
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)): # find the smallest elem remaining
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    @staticmethod
    def merge_sort(lst, sort = None):
        """
        @param list[int] lst: unordered list
        @return list[int]: ordered list
        Recursively splits the job in half in order to divide
            and conquer
        """
        # base case: only 1 element
        if len(lst) == 1:
            return lst

        # divide in half
        i = len(lst) // 2
        left = Sorting_algs.merge_sort(lst[:i])
        right = Sorting_algs.merge_sort(lst[i:])

        # merge
        merged = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        while l < len(left):
            merged.append(left[l])
            l += 1
        while r < len(right):
            merged.append(right[r])
            r += 1
        
        return merged