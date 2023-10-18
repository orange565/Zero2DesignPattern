import itertools

cycle = itertools.cycle([1,2,3])

for _ in range(10):
    print(next(cycle))

import functools

multiple_by_2 = functools.partial(lambda x, y: x * y, 3)
result = multiple_by_2(5)
print(result)