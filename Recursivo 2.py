vec = []


def in_data(number):
    vec.append(input())
    if number < 20:
        number += 1
        in_data(number)


def main():
    in_data(1)
    print(vec)


main()
