from collections import deque


# ball = [1, 2, 3, 4, 5, 6]
# order = [6, 2, 5, 1, 4, 3]

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]





def solution(ball, order):
    answer = []
    wait = []

    left = 0
    right = len(ball) - 1

    for exitBall in order:

        # print(ball, left, right)

        while len(wait) != 0:
            if ball[left] in wait: # 가장 왼쪽이 대기목록에 있으면
                exit = ball.pop(left)
                answer.append(exit)
                wait.remove(exit)
                left = 0
                right = len(ball) - 1
            elif ball[right] in wait:
                exit = ball.pop(right)
                answer.append(exit)
                wait.remove(exit)
                left = 0
                right = len(ball) - 1
            else:
                break

        if exitBall == ball[left]:
            answer.append(ball.pop(left))
            left = 0
            right = len(ball) - 1

        elif exitBall == ball[right]:
            answer.append(ball.pop(right))
            left = 0
            right = len(ball) - 1

        else:
            wait.append(exitBall)

        print(answer)


solution(ball, order)