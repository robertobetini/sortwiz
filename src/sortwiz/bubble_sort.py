from datetime import datetime

from .base_sort import BaseSort, SortResult
from .errors import InvalidOrderError

class BubbleSort(BaseSort):
    @classmethod
    def sort_asc(self, items: list, in_place: bool = False) -> SortResult:
        f'''
        Applies a bubble sort in ascending order to the given list.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.

        Returns
        -------
            The `SortResult` with the list of items in ascending order.
        '''

        return self.sort(items, in_place, 1)
    
    @classmethod
    def sort_desc(self, items: list, in_place: bool = False) -> SortResult:
        '''
        Applies a bubble sort in descending order to the given list.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.

        Returns
        -------
            The `SortResult` with the list of items in descending order.
        '''

        return self.sort(items, in_place, -1)
    
    @classmethod
    def sort(self, items: list, in_place: bool = False, order: int = 1) -> SortResult:
        '''
        Applies a bubble sort to the given list.

        Parameters
        ----------
            `items` - A list with items to sort.
            `in_place` - Whether to apply the sort into the given list or not. If True, modifies the given list, if False, not.
            `order` - 1 (ascending) or -1 (descending)

        Returns
        -------
            The `SortResult` with the list of items.
        '''
        self.validate(items)

        start_time = datetime.now()

        swapped = True
        sorted_list = items if in_place else list(items)
        sort_result = SortResult(sorted_list, 0, 0, 0)

        while swapped:
            swapped = False

            for i in range(len(sorted_list) - 1):
                if self.__apply_order_rule(sorted_list, i, order):
                    self.swap(sorted_list, i, i + 1, sort_result)
                    swapped = True

        end_time = datetime.now()

        sort_result.time = end_time - start_time

        return sort_result
    
    @classmethod
    def __apply_order_rule(self, items: list, i: int, order: int):
        if order == 1:
            return items[i] > items[i + 1]
        elif order == -1:
            return items[i] < items[i + 1]
        else:
            raise InvalidOrderError(order)
