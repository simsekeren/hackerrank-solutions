if __name__ == '__main__':
    n = int(input())
    squares = []
    for i in range(n):
        squares.append(i ** 2)

    for square in squares:
        print(square)