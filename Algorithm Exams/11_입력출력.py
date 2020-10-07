import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 실수 입력
if __name__ == '__main__':
    n = float(input())
    print(n)