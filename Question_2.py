def special_percentile(percent: int, numbers: list) -> float:
    '''
    receives a list and a percentile, return the number at that percentile
    :param percent: the user input percentage
    :param numbers: a list of user input numbers
    :return: percentile number
    '''
    numbers.sort()
    selected_number = int(((percent/100) * (len(numbers))) - 1)
    return numbers[int(selected_number + 1)]

print(special_percentile(25, [40, 10, 30 ,20]))
print(special_percentile(25, [50, 40, 10, 30 ,20]))
print(special_percentile(50, [9, 1, 7, 3]))
