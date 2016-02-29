import matplotlib.pyplot as plt
import math

M = 5
maxLen = 10000
K = 10.0
arr_for_xi = []

def frac(num):
    return math.modf(num)[0]


def random_new(previous):
    return frac(previous*M)


def get_new_arr(num):
    result = []
    while num not in result and len(result) < maxLen:
        result.append(num)
        num = random_new(num)
    return result


def make_arr_to_draw_digital_dem(full_arr):
    result = []
    for num in full_arr:
        i = math.trunc(num*10)
        result.append(i)
    # print(result)
    return result


def dig_dem(arr):
    osx = make_arr_to_draw_digital_dem(arr)
    plt.hist(osx)
    plt.show()


def count_m(arr):
    return sum(arr) / len(arr)


def count_disp(arr):
    m = count_m(arr)
    sum_quad = 0
    for i in range (0, len(arr)):
        sum_quad += (arr[i] - m)**2
    return sum_quad / len(arr)


def draw_hist(full_arr):
    min_of_arr = min(full_arr)
    max_of_arr = max(full_arr)
    interval = (max_of_arr-min_of_arr)/K
    # print min_of_arr
    # print max_of_arr
    # print interval
    result = []
    for num in full_arr:
        # print num
        for i in range(1, 11):
            if (num >= (min_of_arr+interval*(i-1))) and (num <= (min_of_arr+interval*(i))):
                result.append(i-1)
                # print i-1
    plt.hist(result)
    plt.show()
    return result


def xi_quad(arr):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    xi = 0
    for i in arr:
        result[i] += 1
    for col in result:
        xi += K/maxLen * (col - maxLen/K)**2
    print(xi)



R0 = 0.123415123
randArr = get_new_arr(R0)

xi_quad(draw_hist(randArr))

# digDem(randArr)
