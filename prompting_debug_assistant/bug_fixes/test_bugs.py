from bug1_fixed import calculate_total
from bug3_fixed import calculate_average

assert abs(calculate_total([12.50, 8.00, 4.25], 0.10) - 27.225) < 1e-9
assert round(calculate_average([85, 90, 78]), 2) == 84.33
assert round(calculate_average([92, 88, 95]), 2) == 91.67
assert calculate_average([]) is None
print("All Python assertions passed")
