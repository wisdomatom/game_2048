from gamefunc2048 import *


list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

init_list(list1)

while 1:

    view(list1)
    num = input('请输入您要的操作(t退出)：')

    if num == 'w':
        lt1, lt2, lt3, lt4 = ud_list(list1)
        left_add_list(lt1, lt2, lt3, lt4)
        list1 = revert(lt1, lt2, lt3, lt4)
        if lose(list1):
            print('抱歉，你输了')
            break
        if win(list1):
            print('恭喜你获得胜利')
            break
        add24(list1)

    elif num == 's':
        lt1, lt2, lt3, lt4 = ud_list(list1)
        right_add_list(lt1, lt2, lt3, lt4)
        list1 = revert(lt1, lt2, lt3, lt4)
        if lose(list1):
            print('抱歉，你输了')
            break
        if win(list1):
            print('恭喜你获得胜利')
            break
        add24(list1)

    elif num == 'a':
        lt1, lt2, lt3, lt4 = lr_list(list1)
        left_add_list(lt1, lt2, lt3, lt4)
        list1 = lt1 + lt2 + lt3 + lt4
        if lose(list1):
            print('抱歉，你输了')
            break
        if win(list1):
            print('恭喜你获得胜利')
            break
        add24(list1)

    elif num == 'd':
        lt1, lt2, lt3, lt4 = lr_list(list1)
        right_add_list(lt1, lt2, lt3, lt4)
        list1 = lt1 + lt2 + lt3 + lt4
        if lose(list1):
            print('抱歉，你输了')
            break
        if win(list1):
            print('恭喜你获得胜利')
            break
        add24(list1)

    elif num == 't':
        break
    else:
        print('尚未定义此操作')