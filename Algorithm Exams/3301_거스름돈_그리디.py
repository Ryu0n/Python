import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

'''
어떤 가게의 욕심쟁이 점원은 거스름돈을 나눠줄때 거스름돈의 개수를 적게해서 주고자 한다.
거스름돈을 입력 받아 점원이 줄 수 있는 최소 거스름돈의 개수를 출력하시오.

예를 들어 54520원인 경우,
거스름돈으로 50000원권 1장, 1000원권 4장, 500원 1개, 10원 2개 해서 총 8개이다.

(※ 현재 우리나라가 사용하고 있는 화폐를 사용한다. 10원 50원 100원 500원 1,000원 5,000원 10,000원 50,000원)
'''

if __name__ == '__main__':
    moneyList = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    extra = int(input())
    answer = 0

    for money in moneyList:
        moneyNum = int(extra / money)
        if moneyNum > 0:
            answer += moneyNum
            extra %= money

    print(answer)