def main(int1, int2):
    try:
        return int1 + int2
    except Exception as e:
        print(e)
        return 0

if __name__=="main":
    main()  # pragma: no cover