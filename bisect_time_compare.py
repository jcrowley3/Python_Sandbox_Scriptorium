import timeit
import random
import bisect
from bisect import bisect_left
from typing import List, Union
import tqdm

# Original function
# def bisect_search_rc(haystack, item, index_pos=None, return_type=None):
def bisect_search_rc_old(haystack: List, item: any, index_pos: int = None, return_type: type = int) -> any:

	if not return_type: return_type = int;

	def returnValue(value):
		if return_type is bool and value == -1:
			return False
		elif return_type is bool:
			return True
		elif value != -1:
			return value

	try:
		item_index = bisect.bisect_left(haystack, item)
		if item_index < len(haystack):
			if index_pos is not None and item[index_pos] == haystack[item_index][index_pos]:
				return returnValue(item_index)
			elif index_pos is None and item == haystack[item_index]:
				return returnValue(item_index)

	except Exception as inst:
		print('bisectSearchRC.ERROR', inst)

	return returnValue(-1)

# Optimized/refactored function
# def bisect_search_rc_new(haystack: List, item: any, index_pos: int = None, return_type: type = None) -> any:
# def bisect_search_rc_new(haystack: List, item: any, index_pos:int|None = None, return_type: type|None = None) -> bool|int|any:
def bisect_search_rc_new(haystack: List, item: any, index_pos: Union[int, None] = None, return_type: Union[type, None] = None) -> Union[bool, int, any]:
    if not return_type:
        return_type = int

    try:
        if index_pos is None:
            item_index = bisect_left(haystack, item)
            if item_index != len(haystack) and haystack[item_index] == item:
                return_value = item_index
            else:
                return_value = -1
        else:
            bisect_key = [x[index_pos] for x in haystack]
            item_key = item[index_pos]
            key_index = bisect_left(bisect_key, item_key)
            if key_index != len(bisect_key) and bisect_key[key_index] == item_key:
                item_index = key_index
                if haystack[item_index] == item:
                    return_value = item_index
                else:
                    return_value = -1
            else:
                return_value = -1

        if return_type is bool:
            return return_value != -1
        elif return_value != -1:
            return return_value

    except Exception as e:
        print(f'bisect_search_rc.ERROR: {e}')

    return -1


# Test function to measure time complexity
def test_bisect_search_rc():
    # Generate a list of random integers to search
    haystack = sorted([random.randint(0, 10000) for _ in range(1000)])

    # Generate some random items to search for
    items = [random.randint(0, 10000) for _ in range(10000)]

    # Measure time complexity of old function
    old_time = timeit.timeit(lambda: [bisect_search_rc_old(haystack, item) for item in items], number=1000)

    # Measure time complexity of new function
    new_time = timeit.timeit(lambda: [bisect_search_rc_new(haystack, item) for item in items], number=1000)

    print(f"Old function time: {old_time:.5f} seconds")
    print(f"New function time: {new_time:.5f} seconds")
    print(f"Ratio (new/old): {new_time/old_time:.2f}")

    ratio = new_time / old_time
    percentage = round(ratio * 100, 2)
    print(f"NEW took {percentage}% less time than OLD!")

    percent_increase = ((old_time - new_time) / old_time) * 100
    formatted_percent_increase = "{:.2f}%".format(percent_increase)
    print(f"NEW is {formatted_percent_increase} faster than OLD!")

# Run the test
test_bisect_search_rc()
