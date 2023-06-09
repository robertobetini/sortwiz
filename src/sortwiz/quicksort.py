from datetime import datetime

from .base_sort import BaseSort, SortResult

class Quicksort(BaseSort):
    @classmethod
    def sort_asc(self, items: list, in_place: bool = False) -> SortResult:
        '''
        Applies a quicksort in ascending order to `items`.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.

        Returns
        -------
            The `SortResult` with the list of items in ascending order.
        '''

        return self.sort(items, in_place, False)
    
    @classmethod
    def sort_desc(self, items: list, in_place: bool = False) -> SortResult:
        '''
        Applies a quicksort in descending order to `items`.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.

        Returns
        -------
            The `SortResult` with the list of items in ascending order.
        '''

        return self.sort(items, in_place, True)
    
    @classmethod
    def sort(self, items: list, in_place: bool = False, reverse: bool = False) -> SortResult:
        '''
        Applies a quicksort to `items`.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.
            `reverse` - `True` for descending, `False` for ascending.

        Returns
        -------
            The `SortResult` with the list of items.
        '''

        self.validate(items)

        start_time = datetime.now()

        sorted_list = items if in_place else list(items)
        sort_result = SortResult(sorted_list, 0, 0, 0)

        start = 0
        end = len(sorted_list)
        self.__quicksort(sorted_list, start, end, reverse, sort_result)

        end_time = datetime.now()

        sort_result.time = end_time - start_time

        return sort_result
    
    @classmethod
    def __quicksort(self, items: list, start: int, end: int, reverse: bool, sort_result: SortResult) -> None:
        if start < end:
            partition = self.__partition(items, start, end, reverse, sort_result)
            self.__quicksort(items, start, partition, reverse, sort_result)
            self.__quicksort(items, partition + 1, end, reverse, sort_result)

    @classmethod
    def __partition(self, items: list, start: int, end: int, reverse: bool, sort_result: SortResult) -> int:
        pivot_index = end - 1
        pivot = items[pivot_index]

        for i in range(start, end):
            if self.__apply_order_rule(items, i, pivot, reverse):
                BaseSort.swap(items, start, i, sort_result)
                start += 1

        if self.__apply_order_rule_to_swap_pivot(items, start, pivot, reverse):
            BaseSort.swap(items, start, pivot_index, sort_result)

        return start

    def __apply_order_rule(items: list, i: int, pivot, reverse: bool) -> bool:
        if reverse:
            return items[i] > pivot
        
        return items[i] < pivot
    
    def __apply_order_rule_to_swap_pivot(items: list, start: int, pivot, reverse: bool) -> bool:
        if reverse:
            return items[start] < pivot
        
        return  items[start] > pivot
