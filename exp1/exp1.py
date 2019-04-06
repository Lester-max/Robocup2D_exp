# Author:   王子�?
# Class:    计算机�?��?�与技�?17-1�?
# ID:       2017217713

# coding:utf-8

def hear_msg(str):
    loc_begin = str.find('hear', 0, len(str))
    loc_end = str.find('))', 0, len(str))
    loc_time = str.find(' ', loc_begin + 5, loc_begin + 10)
    time = str[loc_begin + 5 : loc_time] 
    print('�?', time, '周期hear', end = ' ')
    loc_pos = str.find(' ', loc_begin + 10, loc_begin + 15)
    pos = str[loc_time : loc_pos]
    print('�?', pos, '方向', end = ' ')
    loc_past = str.find(' ', loc_begin + 15, loc_begin + 25)
    past = str[loc_past : loc_end]
    print('�?到了', past)

def see_msg(str):
    loc_begin = str.find('see', 0, len(str))
    loc_time = str.find(' ', loc_begin, loc_begin + 5)
    time = str[loc_begin + 5 : loc_time]
    print('�?', time, '周期see')
    loc_ball = str.find('(ball)', loc_begin, loc_begin + 20)
    distance = str[loc_ball + 5 : loc_ball + 6]
    print('Ball距�?�我的Distance�?', distance, end = ' ')
    direction = str[loc_ball + 7 : loc_ball + 9]
    print('Derection�?', direction, end = ' ')
    distChng = str[loc_ball + 10 : loc_ball + 13]
    print('DirChng�?', distChng, end = ' ')

def player_msg(str):
    loc_player = str.find('player', 0, len(str))
    player = str[loc_player + 5 : loc_player + 10]
    print('player', player, end = ' ')
    loc_distance = str.find(')', loc_player, loc_player + 10)
    distance = str[loc_distance + 1 : loc_distance + 4]
    print('距�?�我的Distance�?', distance, end = ' ')
    loc_derection = str.find(' ', loc_distance + 1, loc_distance + 4)
    derection = str[loc_derection : loc_derection + 3]
    print('Direction�?', derection, end = ' ')
    loc_distChng = str.find(' ', loc_distance + 4, loc_distance + 7)
    distChng = str[loc_distChng : loc_distChng + 3]
    print('DistChng�?', distChng, end = ' ')
    loc_dirChng = str.find(' ', loc_distance + 7, loc_distance + 10)
    dirChng = str[loc_dirChng : loc_dirChng + 3]
    print('DirChng�?', dirChng, end = ' ')
    loc_bodyDir = str.find(' ', loc_distance + 10, loc_distance + 13)
    bodydir = str[loc_bodyDir : loc_bodyDir + 3]
    print('bodyDir�?', bodydir, end = ' ')
    loc_headDir = str.find(' ', loc_distance + 13, loc_distance + 17)
    headdir = str[loc_headDir : loc_headDir + 3]
    print('bodyDir�?', headdir, end = ' ')


def goal_msg(str):
    loc_goal = str.find('goal', 0, len(str))
    loc_start = str.find(')', loc_goal, len(str))
    distance = str[loc_start : loc_start + 3]
    print('goal r距�?�我的Distance�?', distance, end = ' ')
    loc_direction = str.find(' ', loc_start, loc_start + 4)
    direction = str[loc_direction : loc_direction + 3]
    print('Direction�?', direction)



def main():
    str = '(hear 1022 -30 passto(23,24))(see 1022 ((ball) 20 -20 1 -2) ((player hfut1  2) 23 45 0.5 1 22 40 ) ((goal r) 12 20)))'
    hear_msg(str)
    see_msg(str)
    player_msg(str)
    goal_msg(str)

if __name__ == '__main__':
    main()
