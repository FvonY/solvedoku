from cell import Cell


class Sudoku():
    def __init__(self, riddle=None):
        if riddle is None:
            self.board = [[Cell() for i in range(9)] for j in range(9)]
        else:
            self.board = []
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(Cell(riddle[i][j]))
                self.board.append(row)
        pass

    def as_list(self):
        i = 0
        list_representation = []
        for row in self.board:
            cur_row = []
            for cell in row:
                cur_row.append(i)
                i += 1
            list_representation.append(cur_row)
        return list_representation

    def print_sudoku(self):
        print("=" * 27)
        for i in range(len(self.board)):
            self._print_row(i)
            if i == 2 or i == 5 or i == 8:
                print("=" * 27)

    def _print_row(self, row):
        r = [cell.getValueAsString() for cell in self.board[row]]
        print("|| %s %s %s | %s %s %s | %s %s %s ||" % (*r,))

    def solve(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.check_cell(self.board[i][j], i, j)

        for row in self.board:
            for cell in row:
                cell.checkSolved()

    def check_cell(self, cur_cell: Cell, i, j):
        # check: row, column, block

        possible = cur_cell.possible
        # row -> same i, all j
        for other_cell in self.board[i]:
            if other_cell.value is None:
                continue
            else:
                if other_cell.value in possible:
                    possible.remove(other_cell.value)
                # print(f"Removed {other_cell.value} from ({i}, {j})")

        # column -> same j, all i
        for ii in range(9):
            other_cell = self.board[ii][j]
            if other_cell.value is None:
                continue
            else:
                if other_cell.value in possible:
                    possible.remove(other_cell.value)

        # block -> i, j in mod 3 range thingy
        i_mod = i % 3
        i_div = int(i / 3)
        i_min = i - i_mod
        i_max = i_div*3 + 2

        j_mod = j % 3
        j_div = int(j / 3)
        j_min = j - j_mod
        j_max = j_div*3 + 2
        for ii in range(i_min, i_max+1):
            for jj in range(j_min, j_max+1):
                other_cell = self.board[ii][jj]
                if other_cell.value is None:
                    continue
                else:
                    if other_cell.value in possible:
                        possible.remove(other_cell.value)
        pass

    def check_row(self, cur_cell, i, j):
        possible = cur_cell.possible
        # row -> same i, all j
        for other_cell in self.board[i]:
            if other_cell.value is None:
                continue
            else:
                if other_cell.value in possible:
                    possible.remove(other_cell.value)
