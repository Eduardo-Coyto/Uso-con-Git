def sum_list (lst: list) -> float:
    assert type(lst) == list, 'Parametro lst debe ser de tipo lista'
    assert len(lst), 'Lista vacía'
    total = 0

    for item in lst:
        total += item
    return total

lst_sum = sum_list(lst=[1,2,3.5])

print(lst_sum)
