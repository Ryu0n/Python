n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2 # 절단기의 높이
    for x in array:
        if x > mid: # 떡들의 양 계산
            total += x - mid
    if total < m: # 떡의 양이 부족하면 더 많이 자르기
        end = mid - 1 # 절단기의 높이를 낮춰서 더 많이 자르기
    else: # 떡의 양이 충분하다면 최대한 더 적게 자르기
        result = mid
        start = mid + 1 # 절단기의 높이를 높여서 더 적게 자르기

print(result)