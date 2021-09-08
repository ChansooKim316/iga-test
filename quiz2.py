# 문제 2

from queue import Queue


# elevator - 각층의 탑승인원
elevator = []
# all floors - 각 층의 대기자. 층마다 큐가 하나씩 존재
all_floors = []
# 현재까지 최고 탑승인원
greatest_occupancy = 0
# 이동가능 층수 (N)
top_floor = 0
# 탑승가능 인원 (M)
max_occupancy = 0
# 탑승 횟수(T)
onboard_limit = 0


def receive_cases():
    cases =  input('전체 케이스 수를 입력하세요 : ').rstrip()
    return cases


# N, M, T 입력 받기
def receive_input():
    global top_floor, max_occupancy, onboard_limit
    line2 = input('이동가능한 층수, 탑승가능 인원, 탑승횟수를 입력하세요. (예: 5 4 4) : ').rstrip().split(' ')
    top_floor = int(line2[0])
    max_occupancy = int(line2[1])
    onboard_limit = int(line2[2])
    return



# # 각 층의 대기인원이 들어갈 Queue 들을 층수만큼 생성
# for flr in range(0, top_floor):
#     all_floors.append(Queue())

# # 엘리베이터 배열의 길이를 층수만큼 
# for i in range(0, top_floor):
#     elevator.append(0)


# 대기자
def receive_wait_list():
    global max_occupancy, all_floors
    for num in range(0, max_occupancy):
        # 대기자 입력받기
        data = input('승객의 탑승대기층과 목적지층을 입력하세요 (예: 2 5) : ').rstrip()
        person = [int(data.split(' ')[0]), int(data.split(' ')[1])]

        # all_floors 배열의 각 인덱스(층)에 있는 큐에 대기자 추가하기
        # person 의 0번째 인덱스가 대기층
        wait_floor = person[0]
        # 대기자가 들어가야 할 큐가 all_floors[대기층-1] 에 위치하므로 해당 큐에 대기자를 추가 
        all_floors[wait_floor - 1].put(person)

    return


# # 층별 대기자 확인
# for i in range(0, len(all_floors)):
#     print('flr {} :'.format(i+1), list(all_floors[i].queue))


def on_board_going_up(index):
    # all_floor 순회하면서 현재층 == 대기층 이면 승차
    # print('index :', index)
    curr_floor = index + 1
    # for i in range(0, len(all_floors)):
    #     print('-- i --- :', i)
    # 해당층에 대기자가 있을경우만 if 문 통과
    if(all_floors[index].queue):
        departure = list(all_floors[index].queue)[0][0]
        destination = list(all_floors[index].queue)[0][1]
        # 목적지층 < 대기층 일경우 내려가는 승객이므로 탑승하지않음
        if(destination < departure):
            # print('not going up')
            return
        # 대기층 == 탑승층일 경우 탑승하지 않음
        if(departure == destination):
            all_floors[index].get()
        if(curr_floor == departure and departure != destination):
            # print('<< {} 층에서 탑승'.format(curr_floor))
            # 대기자 한명 dequeue
            all_floors[index].get()
            # 출발점 ~ 목적지 까지 탑승인원 1 증가
            for i in range(departure, destination):
                elevator[i-1] = elevator[i-1] + 1

    # print('탑승후 elev :', elevator)
    return


def on_board_going_down(index):
    curr_floor = index + 1
    # 해당층에 대기자가 있을경우만 조건문 통과
    if(all_floors[index].queue):
        departure = list(all_floors[index].queue)[0][0]
        destination = list(all_floors[index].queue)[0][1]
        # 대기층 < 목적지층 일경우 올라가는 승객이므로 탑승하지않음
        if(departure < destination):
            # print('not going down')
            return
        if(curr_floor == departure and departure != destination):
            # print('<< down - {} 층에서 탑승'.format(curr_floor))
            # 대기자 한명 dequeue
            all_floors[index].get()
             # 출발점 ~ 목적지 까지 탑승인원 1 증가
            for i in range(destination, departure):
                # print('down - idx :', i)
                # 인덱스 = 실제층 - 1
                elevator[i] = elevator[i] + 1
    return


def is_elevator_full():
    global elevator, max_occupancy
    if(max(elevator) > max_occupancy):
        return True
    return False


# 엘리베이터 구동
def move_elevator():
    try:
        global elevator, onboard_limit, greatest_occupancy
        time_count = 1
        current_flr = 0
        # 제약조건 : 1 <= t(시간) <= T(탑승횟수)
        while time_count < onboard_limit:
            # 엘리베이터 상승
            for flr in range(0, top_floor-1):
                current_flr = flr
                # print('up - curr flr :', current_flr)
                time_count = time_count + 1
                # 탑승
                on_board_going_up(current_flr)

                if(is_elevator_full()):
                    # 출력 : 정원초과 발생시각
                    print('정원초과')
                    print(time_count)
                    return
                
            # 탑승인원 최고치 갱신
            if greatest_occupancy < max(elevator):
                greatest_occupancy = max(elevator)

            # 최고층에서 엘리베이터 초기화
            for i in range(0, top_floor):
                elevator[i] = 0
            
            # print('\nelev reset :', elevator, '\n')

            # 엘리베이터 하강
            for flr in reversed(range(0, top_floor)):
                # current_flr = current_flr - 1
                current_flr = flr
                # print('down - curr flr :', current_flr)
                # print('down - curr elev :', elevator)
                time_count = time_count + 1
                # 탑승
                on_board_going_down(current_flr)

                if(is_elevator_full()):
                    # 출력 : 정원초과 발생시각
                    print('정원초과')
                    print(time_count)
                    return
            
            # 탑승인원 최고치 갱신
            if greatest_occupancy < max(elevator):
                greatest_occupancy = max(elevator)

        # 출력 : 탑승했던 최다인원수 - 탑승가능 인원수(M)
        # print('move elev - 결과')
        print(greatest_occupancy - max_occupancy)
    except Exception as e:
        print('오류가 발생하여 프로그램을 다시 시작합니다.')
        initiate()
    return



def initiate():
    global elevator, all_floors, greatest_occupancy
    cases = int(receive_cases())
    for case in range(0, cases):
        # 새 케이스 시작시 초기화
        elevator = []
        all_floors = []
        greatest_occupancy = 0
        receive_input()
        # 각 층에 대기인원이 들어갈 Queue 들을 생성
        for i in range(0, top_floor):
            all_floors.append(Queue())
        # 엘리베이터 배열의 길이를 층수만큼 설정
        for i in range(0, top_floor):
            elevator.append(0)
        receive_wait_list()
        move_elevator()
    return


initiate()