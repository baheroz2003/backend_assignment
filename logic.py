from typing import List, Tuple
from collections import defaultdict

def largest_rectangle(a: List[List[int]]) -> Tuple[int, int]:
    n = len(a)
    segs = defaultdict(list)
    for i in range(n):
        j = 0
        while j < len(a[i]):
            v = a[i][j]
            l = j
            while j < len(a[i]) and a[i][j] == v:
                j += 1
            segs[v].append((i, l, j - 1))

    ans, val = 0, a[0][0]

    for x, lst in segs.items():
        mp = {}
        prev_row = -1

        for r, l, rr in lst:
            if r != prev_row + 1:
                mp.clear()

            key = (l, rr)
            mp[key] = mp.get(key, 0) + 1

            area = (rr - l + 1) * mp[key]
            if area > ans:
                ans, val = area, x

            prev_row = r

    return val, ans
