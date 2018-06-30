import random

list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def lr_list(lt):
    lt1, lt2, lt3, lt4 = lt[0:4], lt[4:8], lt[8:12], lt[12:16]
    return lt1, lt2, lt3, lt4

def ud_list(lt):
    lt1, lt2, lt3, lt4 = [], [], [], []
    j = 0
    for i in range(4):
        lt1.append(lt[j])
        lt2.append(lt[j+1])
        lt3.append(lt[j+2])
        lt4.append(lt[j+3])
        j += 4
    return lt1, lt2, lt3, lt4

def revert(lt1, lt2, lt3, lt4):
    lt = []
    for i in range(4):
        lt.append(lt1[i])
        lt.append(lt2[i])
        lt.append(lt3[i])
        lt.append(lt4[i])
    return lt

def left_zero(lt):
    for l in range(3):
        for i in range(3):
            if lt[i] == 0:
                k = i
                for j in range(3-i):
                    lt[k], lt[k + 1] = lt[k + 1], lt[k]
                    k += 1

    # return lt

def reverse_list(lt):
    lt[0], lt[3] = lt[3], lt[0]
    lt[1], lt[2] = lt[2], lt[1]
    # return lt

def right_zero(lt):
    reverse_list(lt)
    for l in range(3):
        for i in range(3):
            if lt[i] == 0:
                k = i
                for j in range(3-i):
                    lt[k], lt[k + 1] = lt[k + 1], lt[k]
                    k += 1
    reverse_list(lt)
    # return lt


def left_add_list(lt1, lt2, lt3, lt4):
    for lt in [lt1, lt2, lt3, lt4]:
        left_zero(lt)
        for i in range(3):
            if lt[i] == lt[i + 1]:
                temp = lt[i] + lt[i + 1]
                lt[i] = temp
                lt[i + 1] = 0
                i += 1
        left_zero(lt)
    # return lt1, lt2, lt3, lt4

def right_add_list(lt1, lt2, lt3, lt4):
    # map(reverse_list, [lt1, lt2, lt3, lt4])
    reverse_list(lt1), reverse_list(lt2), reverse_list(lt3), reverse_list(lt4)
    left_add_list(lt1, lt2, lt3, lt4)
    # map(reverse_list, [lt1, lt2, lt3, lt4])
    reverse_list(lt1), reverse_list(lt2), reverse_list(lt3), reverse_list(lt4)

# lt1, lt2, lt3, lt4 = [8,0,0,0], [8,4,4,2], [2,2,0,8], [4,4,0,2]
# lt5 = lt1 + lt2 +lt3 +lt4
# print(lt5)
# # left_add_list(lt1,lt2,lt3,lt4)
# right_add_list(lt1, lt2, lt3, lt4)
# print(lt1, lt2, lt3, lt4)

def init_list(lt):
    index = [i for i in range(0, 16)]
    i = random.sample(index, 2)
    j = random.sample([2, 4], 1)
    k = random.sample([2, 4], 1)
    lt[i[0]] = j[0]
    lt[i[1]] = k[0]

def add24(lt):
    zero_index = []
    for i in range(0, 16):
        if lt[i] == 0:
            zero_index.append(i)
    j = random.sample(zero_index, 1)
    k = random.sample([2, 4], 1)
    lt[j[0]] = k[0]

def view(lt):
    i = 1
    for x in lt:
        if i%4 != 0:
            print('%4d' %x, end=' ')
        else:
            print('%4d' %x, end='')
            print()
        i += 1

def win(lt):
    for x in lt:
        if x == 2048:
            return 1
    else:
        return 0

def lose(lt):
    def lose_1(lt1, lt2, lt3, lt4):
        for lt in [lt1, lt2, lt3, lt4]:
            left_zero(lt)
            for i in range(3):
                if lt[i] == lt[i + 1]:
                    return 0
        return 1
    def lose_2(lt1, lt2, lt3, lt4):
        reverse_list(lt1), reverse_list(lt2), reverse_list(lt3), reverse_list(lt4)
        for lt in [lt1, lt2, lt3, lt4]:
            left_zero(lt)
            for i in range(3):
                if lt[i] == lt[i + 1]:
                    return 0
        return 1

    lt11, lt12, lt13, lt14 = lr_list(lt)
    lt21, lt22, lt23, lt24 = ud_list(lt)
    if lose_1(lt11, lt12, lt13, lt14) & lose_2(lt21, lt22, lt23, lt24):
        return 1
    else:
        return 0


