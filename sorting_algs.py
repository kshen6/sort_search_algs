import random

class Sorting_algs():
    @staticmethod
    def binary_search_recursive(lst, targ, sort = None):
        """
        Finds index of target element by *recursively* halving the list
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
    def binary_search_iterative(lst, targ, sort = None):
        """
        Finds index of target element by *iteratively* halving the list
        """

        lh, rh = 0, len(lst) - 1
        while lh <= rh:
            piv = lh + (rh - lh) // 2
            if lst[piv] == targ:
                return piv
            elif lst[piv] < targ:
                lh = piv + 1
            else:
                rh = piv - 1
        return -1
    
    @staticmethod
    def binary_search_adding(lst, targ, sort = None):
        """
        Finds index of target element by repeatedly adding intervals of
        decreasing size
        """
        n = len(lst)
        curr_index = 0
        step = n // 2
        while step >= 1:
            while curr_index + step < n and lst[curr_index + step] <= targ:
                curr_index += step
            step //= 2
        return curr_index if lst[curr_index] == targ else -1

    @staticmethod
    def bubble_sort(lst, sort = None):
        """
        Sorts a list by repeatedly iterates through the list, swapping 
        adjacent elements according to sort
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
    def insertion_sort_swapping(lst, sort = None):
        """
        Sorts list by moving through list and swapping elements
        until the sublist is again ordered.
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
    def insertion_sort_moving(lst, sort = None):
        """
        Sorts list by moving through list and moving elements over
        until the sublist is again ordered.
        """
        for i in range(len(lst)):
            key = lst[i]
            j = i - 1
            # move over elements one at a time, circumventing swapping
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
        return lst

    @staticmethod
    def selection_sort(lst, sort = None):
        """
        Sorts the list by iterating through the list and swapping
        the current element with the minimum remaining element
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
        l = r = 0
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

    @staticmethod
    def merge_sort_2(lst, sort = None):
        """
        @param list[int] lst: unordered list
        @return list[int]: ordered list
        Recursively splits the job in half in order to divide
            and conquer, with performance optimization
        """
        # base case: only 1 element
        if len(lst) == 1:
            return lst

        # divide in half
        i = len(lst) // 2
        left = Sorting_algs.merge_sort_2(lst[:i])
        right = Sorting_algs.merge_sort_2(lst[i:])

        # merge
        merged = []
        l = r = 0
        try:
            while True:
                if left[l] < right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
        except:
            return merged + left[l:] + right[r:]
    
    @staticmethod
    def quicksort(lst, sort = None):
        """
        Recursively partitions the list using a divide and conquer
        approach
        """
        def partition(lh, rh, pivot):
            while lh <= rh:
                # skip unswapped elements
                while lst[lh] < pivot:
                    lh += 1
                while lst[rh] > pivot:
                    rh -= 1
                # swap
                if lh <= rh:
                    lst[lh], lst[rh] = lst[rh], lst[lh]
                    lh += 1
                    rh -= 1
            return lh

        # main driver function
        def helper(start, end):
            # base case
            if start >= end: return
            # randomly choose middle element
            pivot = random.choice(lst[start:end + 1])
            half = partition(start, end, pivot)
            helper(start, half - 1)
            helper(half, end)
        
        helper(0, len(lst) - 1)
        return lst
    
    @staticmethod
    def order_stats(lst, k):
        """
        Finds the kth largest element
        """
        def partition(lh, rh, pivot):
            while lh <= rh:
                while lst[lh] < pivot:
                    lh += 1
                while lst[rh] > pivot:
                    rh -= 1
                if lh <= rh:
                    lst[lh], lst[rh] = lst[rh], lst[lh]
                    lh += 1
                    rh -=1
            return lh

        def helper(lh, rh):
            if lh >= rh: # length to be sorted is 1
                return lst[lh]
            pivot = random.choice(lst[lh:rh + 1])
            ind = partition(lh, rh, pivot) # find the index of our pivot element
            # if it is in the second half:
            if len(lst) - ind >= k:
                return helper(ind, rh)
            else:
                return helper(lh, ind - 1)

        return helper(0, len(lst) - 1)

# s = Sorting_algs()
# while True:
#     arr = [int(x) for x in input('Array? ').split()]
#     if len(arr) == 0: break
#     k = int(input('k? '))
#     print(s.order_stats(arr, k))