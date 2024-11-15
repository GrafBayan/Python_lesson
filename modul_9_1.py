def _min(i):
    j = min(i)
    return j


def _max(i):
    t = max(i)
    return t


def _sum(i):
    sum_ = 0
    for j in i:
        sum_ += j
    return sum_


def _len(i):
    l = len(i)
    return l


def _sorted(i):
    s = sorted(i)
    return s


my_functions = [_min, _sum, _len, _sorted]


def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        results[i.__name__] = i(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))