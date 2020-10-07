import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

from itertools import combinations

if __name__ == '__main__':
    # 토핑의 종류의 수
    toppingKind = int(input())

    # 도우와 토핑의 가격
    prices = input().split(' ')
    dowPrice = int(prices[0])
    toppingPrice = int(prices[1])

    # 도우의 칼로리
    dowCalorie = int(input())

    # 토핑의 칼로리
    toppingCalorieList = []
    for i in range(0, toppingKind):
        toppingCalorieList.append(int(input()))

    pizzaCalorie = dowCalorie
    pizzaPrice = dowPrice
    pizzaCaloriePerPrice = float(pizzaCalorie / pizzaPrice)

    toppingCalorieList.sort(reverse=True)

    for toppingCalorie in toppingCalorieList:
        if (pizzaCaloriePerPrice < float((pizzaCalorie + toppingCalorie) / (pizzaPrice + toppingPrice))):
            pizzaCalorie += toppingCalorie
            pizzaPrice += toppingPrice
            pizzaCaloriePerPrice = float(pizzaCalorie / pizzaPrice)

    print(int(pizzaCaloriePerPrice))