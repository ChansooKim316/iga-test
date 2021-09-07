
# 문제 1

'''

- 주석달기
- 풀이 
 - 표 PDF
- 다양한 테스트케이스
 - 백준

'''


import sys


def get_number_of_cases():
    number_of_cases = int(input('\n케이스의 갯수를 입력하세요 : '))
    return number_of_cases


def run_functions():
    number_of_cases = get_number_of_cases()
    if number_of_cases == 1:
        calculate_minimum_time()  # -------->>>
        return
    for n in range(0, number_of_cases):
        print('\n---- {}번째 캐이스 ----\n'.format(n+1))
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

        # 입력값 조건 확인
        # if ppl_total < num_of_rides:
        #     print('\n잘못된 입력 : 아이들의 수는 놀이기구의 수보다 같거나 많아야 합니다.\n')
        #     calculate_minimum_time()

        # print()
        # print('총 인원수 :', ppl_total)
        # print('놀이기구 수 :', num_of_rides)
        # print('각 놀이기구의 탑승시간', rides_list)

        
        for time_count in range(1, 10**10):
            ppl_finished = 0
            for i in range(0, len(rides_list)):
                ppl_finished = ppl_finished + int(time_count/rides_list[i])        
            if ppl_finished >= ppl_total:
                time_total = time_count
                break

        print()
        print('최소 소요시간 :', time_total)

    except Exception as e:
        print(e)
        print('\n---- 오류가 발생하여 프로그램을 다시 시작합니다. ----')
        run_functions()

    return


run_functions()
# get num of case 로 시작?
print('\n---- 모든 케이스가 종료되었습니다. ----')
