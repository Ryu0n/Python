import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

if __name__ == '__main__':
    print('Hello\nWorld')