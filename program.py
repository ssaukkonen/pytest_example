def main():
    result = add(1, 1)

def add(int1, int2):
    try:
        return int1 + int2
    except Exception as e:
        print(e)
        return 0

if __name__=="__main__":
    main()  # pragma: no cover