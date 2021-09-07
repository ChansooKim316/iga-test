import sys


# 케이스 수
case = None
# # 최고층
# N = 0
# # 탑승가능 인원
# M = 0
# # 탑승가능횟수
# T = 0
# # 인원초과 지표
# occupancy_exceed = False

# 엘리베이터 딕셔너리
elevator = {
    'top_floor': 0,
    'curr_floor': 0,
    'max_occupancy': 0,
    'curr_occupancy': 0,
    'greatest_occupancy': 0,
    'occupancy_exceed': False,
    'max_boarding': 0,
    'people': {}
}


def recieve_input():
    line1 = input('케이스의 갯수를 입력하세요. (예: 3) : ')
    line2 = input('이동가능한 층수, 탑승가능 인원, 탑승횟수를 입력하세요. (예: 5 4 4) : ').rstrip('\n').split(' ')
    # 케이스 갯수 (c)
    global case
    case = int(line1)
    # 최고층 (N)
    # N = int(line2[0])
    elevator['top_floor'] = int(line2[0])
    # 탑승가능 인원 (M)
    # M = int(line2[1])
    elevator['max_occupancy'] = int(line2[1])
    # 탑승가능횟수 (T)
    # T = int(line2[2])
    elevator['max_boarding'] = int(line2[2])
   

def on_board(count):
    line3 = input('승객의 탑승대기층과 목적지층을 입력하세요. (예: 2 5) : ').rstrip('\n').split(' ')
    # print('count :', count)
    # print('line3 : ', line3)

    # 대기중인 층 == 목적지 일 경우, 탑승자가 없을경우 탑승시키지 않음
    if (int(line3[0]) == int(line3[1])) or line3 != ['']:
        return
    # 탑승인원 추가
    else :
        elevator['people'][count] = {'on-boarding floor': int(line3[0]), 'destination': int(line3[1])}
        elevator['curr_occupancy'] = elevator['curr_occupancy'] + 1
        # print('입력후 엘베 :', elevator)
    return
    

def one_floor_up():
    # 층수 증가
    elevator['curr_floor'] = elevator['curr_floor'] + 1
    print('현재층 :', elevator['curr_floor'])
    off_boarding()
    return


def off_boarding():
    # 하차하기
    # 사람 i 루핑하면서 destination == curr_floor 이면 obj 에서 obj['ppl'][i] 제거
    for i in range(1, len(elevator['people'].keys())):
        print('i', i)
        print('사람들 :', elevator['people'])
        # 탑승자들중 목적지 == 현재층 인경우 해당 탑승자 지우기
        if elevator['people'][i]['destination'] == elevator['curr_floor']:
            print('내릴사람 :', elevator['people'][i])
            del elevator['people'][i]
            print('내리기 후 :', elevator['people'])
        # 변경사항 : 현재인원 감소
        elevator['curr_occupancy'] = elevator['curr_occupancy'] - 1

    # 인원초과 조건
    if elevator['curr_occupancy'] >= elevator['max_occupancy']:
        elevator['occupancy_exceed'] = True

    # 변경사항 : 현재층, 탑승인원최고기록 갱신
    if elevator['curr_occupancy'] > elevator['greatest_occupancy']:
        elevator['greatest_occupancy'] = elevator['curr_occupancy']
    
    return


def run_functions():
    global case
    recieve_input()
    for c in range(1, case + 1):
        # 엘리베이터 초기화
        print('\n--- {}번째 케이스 ---\n'.format(c))
        for time in range(1, elevator['max_boarding'] + 1):
            one_floor_up()
            # 인원초과시 정지
            if elevator['occupancy_exceed']:
                return '인원초과. 발생시각 : {}'.format(time)
            # print('time : ', time)
            on_board(time)
    
    return


run_functions()

print('\n--- 케이스가 모두 종료되었습니다. ---\n')
