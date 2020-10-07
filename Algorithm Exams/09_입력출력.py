import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 정수 입력
if __name__ == '__main__':
    n = input()
    print(n)