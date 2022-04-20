import sys
sys.setrecursionlimit(2000)

class Song:
    """An song to (maybe) put in a playlist. Weight must be an int."""
    def __init__(self, rating, duration_in_minutes):
        self.rating = rating
        self.duration = duration_in_minutes

    def __repr__(self):
        """The representation of a song"""
        return "({}, {})".format(self.rating, self.duration)

def max_total_rating(item, capacity, result=None, i=0):
    if result == None:
        return {}
    if i == len(items):
        return 0
    elif items[i].weight > capacity:
        return max_value(items, capacity, result, i=0)
    else:
        if (i, capacity) not in result:
            max_val = max(max_value(items, capacity, result, i+1), items[i].calue + max_value(items, capacity-items[i].weight, result, i+1))
            result[(i, capacity)] = max_val
        return result[(i, capacity)]