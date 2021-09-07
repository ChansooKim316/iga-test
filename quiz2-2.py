
conf = {
    'top_floor': 0,
    'max_occupancy': 0,
    'max_onboard_count': 0,
    'elevator': [],
    'wait_list': [],
    'curr_floor': 1,
    'time': 1
}

# top_floor = 0
# max_occupancy = 0
# max_onboard_count = 0
# elevator = []
# wait_list = []
# curr_floor = 1


def recieve_inputs():
    # N, M, T 입력 받기
    line2 = input('이동가능한 층수, 탑승가능 인원, 탑승횟수를 입력하세요. (예: 5 4 4) : ').rstrip('\n').split(' ')
    conf['top_floor'] = int(line2[0])
    conf['max_occupancy'] = int(line2[1])
    conf['max_onboard_count'] = int(line2[2])
    # 초기화
    conf['elevator'] = []
    conf['wait_list'] = []
    conf['curr_floor'] = 1
    

    for num in range(conf['max_occupancy']):
        # 대기자 입력받기
        person = input('승객의 탑승대기층과 목적지층을 입력하세요 (예: 2 5) : ')
        conf['wait_list'].append(person)

    print('입력값 conf :', conf)
    return


def move_elevator():
    # 층수 계산
    t = conf['time'] 
    current_flr = conf['curr_floor']
    top_flr = conf['top_floor']

    while t < 10:
        print('starting time :', t)
        # 층수 증가
        for flr in range(1, top_flr + 1):
            print('curr flr :', flr)
            # 탑승 하차 대기
            t = t + 1
        # 층수 감소
        for i in range(1, top_flr):
            current_flr = top_flr - i
            print('curr flr :', current_flr)
            # 탑승 하차 대기
            t = t + 1
        print('finishing time :', t)
        

    return


def on_board():

    return


def off_board():

    return

def initiate():
    try:
        case = input('케이스의 갯수를 입력하세요. : ')
        for c in range(1, int(case) + 1):
            print('\n---- {}번째 케이스 ----\n'.format(c))
            recieve_inputs()
            move_elevator()
    except Exception as e:
        print('오류가 발생했습니다. 처음부터 다시 시작해주세요.')
        initiate()
    return


initiate()
print('\n---- 모든 케이스가 종료되었습니다 ----\n')