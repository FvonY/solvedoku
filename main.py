from sudoku import Sudoku
from riddles import hard_1


def main():
    sudoku = Sudoku(hard_1)
    for i in range(7):
        sudoku.solve()
        print(sudoku.print_sudoku())


if __name__ == "__main__":
    main()
