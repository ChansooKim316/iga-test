# 문제 1

import sys


def get_number_of_cases():
    number_of_cases = int(input('\n케이스의 갯수를 입력하세요 : '))
    return number_of_cases


def run_functions():
    number_of_cases = get_number_of_cases()
    if number_of_cases == 1:
        calculate_minimum_time()
        return
    for n in range(0, number_of_cases):
        # print('\n---- {}번째 캐이스 ----\n'.format(n+1))
        calculate_minimum_time()


def calculate_minimum_time():
    try:
        # stdin 입력
        line2 = input('아이들의 수와 놀이기구의 수를 입력하세요 (예: 5 3): ').rstrip('\n').split(' ')
        line3 = input('각 놀이기구의 운행시간을 입력하세요 (예: 12 10 4): ').rstrip('\n').split(' ')

        # 총 소요시간 초기화
        time_total = 0

        # 총 인원수
        ppl_total = int(line2[0])

        # 놀이기구 수
        num_of_rides = int(line2[1])

        # 각 놀이기구의 탑승시간 (배열)
        rides_list = [int(element) for element in line3]
        
        for time_count in range(1, 10**10):
            ppl_finished = 0
            for i in range(0, len(rides_list)):
                ppl_finished = ppl_finished + int(time_count/rides_list[i])        
            if ppl_finished >= ppl_total:
                time_total = time_count
                break

        # print('최소 소요시간 :')
        print(time_total)

    except Exception as e:
        print(e)
        print('\n---- 오류가 발생하여 프로그램을 다시 시작합니다. ----')
        run_functions()

    return


run_functions()
print('\n---- 모든 케이스가 종료되었습니다. ----')
