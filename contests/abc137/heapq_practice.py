# https://juppy.hatenablog.com/entry/2019/04/05/%E8%9F%BB%E6%9C%AC_Python_%E3%83%97%E3%83%A9%E3%82%A4%E3%82%AA%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AD%E3%83%A5%E3%83%BC_2_heapq_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3

import heapq

a = [1,7,3,5,4]

#heapify
# 配列 to heap
heapq.heapify(a)
print(a)

# heappop
# 最小値の取り出し
print(heapq.heappop(a))
print(a)

#heappush
#要素(2)の挿入
heapq.heappush(a,2)
print(a)

#最小値の取り出し
print(heapq.heappop(a))

# 最大値の場合
a = [1, 7, 3 ,5, 4]

heapq._heapify_max(a)
print(a)

# heappush
#  module 'heapq' has no attribute '_heappush_max'

# heappop
print(heapq._heappop_max(a))
print(a)

