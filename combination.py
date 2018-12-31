
def combine2(a_arr, b_arr):
    arr = []

    for i in a_arr:
        for j in b_arr:
            arr.append(i + '-' + j)

    return arr

def combine3(a_arr, b_arr, c_arr):
    arr = []

    for i in a_arr:
        for j in b_arr:
            for k in c_arr:
                arr.append(i + '-' + j + '-' + k)

    return arr
