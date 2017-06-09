from itertools import permutations
from math import sqrt

arr = [169, 715, 144, 136, 112]
arr_perfsq = {}
for arr_num in arr:
    arr_perfsq[arr_num] = 0

for number_original in arr:
    perfsq = []
    combinations = list(permutations(str(number_original)))
    for combination in combinations:
        number = int("".join(combination))
        if sqrt(number).is_integer() and number not in perfsq:
            perfsq.append(number)
            if number_original:
                arr_perfsq[number_original] += 1

arr_perfsq_list = sorted(arr_perfsq.items(), key=lambda arr_perfsq_number: arr_perfsq_number[1], reverse=True)
arr_perfsq_final = []
for arr_perfsq_entry in arr_perfsq_list:
    arr_perfsq_final.append(arr_perfsq_entry[0])
return arr_perfsq_final
