import math
 
n, m, a = list(map(int, input().split()))
 
number_for_n = math.ceil(n/a)
number_for_m = math.ceil(m/a)
 
solution = number_for_m * number_for_n
 
print(solution)
