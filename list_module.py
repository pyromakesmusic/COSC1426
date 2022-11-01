def sort_descending(list):
    list.sort(reverse=True)
    return

def get_list_average(list):
    y = sum(list) / len(list)
    return y

def get_list_minus_evens(list):
    z = [x for x in list if x % 2 != 0]
    return z

def remove_extremes(list):
    w = list[:]
    w.remove(min(w))
    w.remove(max(w))
    return w

def pretty_print_list(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    return