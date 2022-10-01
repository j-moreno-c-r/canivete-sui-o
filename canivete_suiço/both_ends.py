


def main():
    s = input("digite uma palavra:")
    if len(s)  > 2:
        print(s[:2] + s[-2:len(s)])
    if len(s) < 2 or len(s) == 2:
        print("")



main()
