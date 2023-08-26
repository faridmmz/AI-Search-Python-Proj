import copy

from Board import Board
from Cell import Cell

class Find:

    def __init__(self, board: Board):
        self.board = board
        self.source = self.__find_source()
        self.goal = self.__find_goal()
        self.explored = []
        self.ida_cutoff = self.__get_number(self.goal[0], self.goal[1]) - self.__get_number(self.source[0], self.source[1])
        self.ids_max_cutoff = self.board.m * self.board.n

    def __find_source(self):
        for row in range(self.board.m):
            for col in range(self.board.n):
                if self.__get_opt(row, col).lower() == 's':
                    return [row, col]

    def __find_goal(self):
        for row in range(self.board.m):
            for col in range(self.board.n):
                if self.__get_opt(row, col).lower() == 'g':
                    return [row, col]

    def __get_opt(self, row: int, col: int) -> str:
        return self.board.cells[row][col][0].lower()

    def __get_number(self, row: int, col: int) -> int:
        return int(self.board.cells[row][col][1:])

    def __successor(self, cell: Cell) -> list:
        cells = []
        if cell.row > 0:
            if self.__get_opt(cell.row - 1, cell.col) != 'w':
                c = Cell(cell.row - 1, cell.col, copy.deepcopy(cell.table), 0, 0, cell.path.copy())
                c.path.append(c)
                c.path_value, c.goal_value = self.__cal_opt(cell.path_value, cell.goal_value, c.row, c.col)
                if not self.explored.__contains__(c.__hash__()):
                    cells.append(c)

        if cell.col > 0:
            if self.__get_opt(cell.row, cell.col - 1) != 'w':
                c = Cell(cell.row, cell.col - 1, copy.deepcopy(cell.table), 0, 0, cell.path.copy())
                c.path.append(c)
                c.path_value, c.goal_value = self.__cal_opt(cell.path_value, cell.goal_value, c.row, c.col)
                if not self.explored.__contains__(c.__hash__()):
                    cells.append(c)

        if cell.row < self.board.m - 1:
            if self.__get_opt(cell.row + 1, cell.col) != 'w':
                c = Cell(cell.row + 1, cell.col, copy.deepcopy(cell.table), 0, 0, cell.path.copy())
                c.path.append(c)
                c.path_value, c.goal_value = self.__cal_opt(cell.path_value, cell.goal_value, c.row, c.col)
                if not self.explored.__contains__(c.__hash__()):
                    cells.append(c)

        if cell.col < self.board.n - 1:
            if self.__get_opt(cell.row, cell.col + 1) != 'w':
                c = Cell(cell.row, cell.col + 1, copy.deepcopy(cell.table), 0, 0, cell.path.copy())
                c.path.append(c)
                c.path_value, c.goal_value = self.__cal_opt(cell.path_value, cell.goal_value, c.row, c.col)
                if not self.explored.__contains__(c.__hash__()):
                    cells.append(c)
        return cells

    def __cal_opt(self, path_sum, goal_value, row, col):
        opt = self.__get_opt(row, col)

        if opt == '+':
            path_sum += self.__get_number(row, col)
        elif opt == '-':
            path_sum -= self.__get_number(row, col)
        elif opt == '*':
            path_sum *= self.__get_number(row, col)
        elif opt == '^':
            path_sum **= self.__get_number(row, col)
        elif opt == 'a':
            goal_value += self.__get_number(row, col)
        elif opt == 'b':
            goal_value -= self.__get_number(row, col)

        return path_sum, goal_value

    def __check_goal(self, cell: Cell) -> bool:
        if cell.path_value > cell.goal_value:
            self.__print_solution(cell)

            return True
        return False

    def bfs_search(self):
        queue = []

        queue.append(
            Cell(self.source[0], self.source[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                 self.__get_number(self.source[0], self.source[1]),
                 self.__get_number(self.goal[0], self.goal[1]), []))

        queue[0].path.append(queue[0])

        while len(queue) > 0:
            cell = queue.pop(0)
            self.explored.append(cell.__hash__())
            neighbors = self.__successor(cell)

            for c in neighbors:
                if c.row == self.goal[0] and c.col == self.goal[1]:
                    if self.__check_goal(cell):
                        return
                else:
                    if not cell.table[c.row][c.col]:
                        queue.append(c)

        print('no solution!!!')

    def ids_search(self):
        for i in range(1, self.ids_max_cutoff):
            self.dfs_search(i)
            self.explored = []

    def dfs_search(self, max_cutoff):
        stack = [
            Cell(self.source[0], self.source[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                 self.__get_number(self.source[0], self.source[1]),
                 self.__get_number(self.goal[0], self.goal[1]), [])]
        stack[0].path.append(stack[0])

        while stack:
            cell = stack.pop(len(stack) - 1)
            if len(cell.path) >= max_cutoff:
                continue

            self.explored.append(cell.__hash__())
            successors = self.__successor(cell)

            if cell.row == self.goal[0] and cell.col == self.goal[1]:
                if self.__check_goal(cell):
                    exit()
                    return

            for successor in successors:
                if not cell.table[successor.row][successor.col]:
                    stack.append(successor)

    def bds_search(self):
        s_queue = [
            Cell(self.source[0], self.source[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                 self.__get_number(self.source[0], self.source[1]),
                 self.__get_number(self.goal[0], self.goal[1]), [])]

        g_queue = [Cell(self.goal[0], self.goal[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                        self.__get_number(self.source[0], self.source[1]),
                        self.__get_number(self.goal[0], self.goal[1]), [])]

        s_queue[0].path.append(s_queue[0])
        g_queue[0].path.append(g_queue[0])

        while s_queue and g_queue:
            s_count = len(s_queue)
            for i in range(0, s_count):
                s_cell = s_queue.pop(0)
                self.explored.append(s_cell.__hash__())
                s_successors = self.__successor(s_cell)

                for successor in s_successors:
                    if not s_cell.table[successor.row][successor.col]:
                        for g_cell in g_queue:
                            if successor.row == g_cell.row and successor.col == g_cell.col:
                                potential_answer = []
                                for path in successor.path:
                                    potential_answer.append([path.row, path.col])
                                for path in range(len(g_cell.path) - 2, -1, -1):
                                    potential_answer.append([g_cell.path[path].row, g_cell.path[path].col])

                                finished = self.cal_potential(potential_answer)
                                if finished:
                                    print(potential_answer)
                                    exit()

                        if successor.row == self.goal[0] and successor.col == self.goal[1]:
                            potential_answer = []
                            for path in range(len(successor.path) - 1, -1, -1):
                                potential_answer.append([successor.path[path].row, successor.path[path].col])

                            finished = self.cal_potential(potential_answer)
                            if finished:
                                print(potential_answer)
                                exit()

                        s_queue.append(successor)

            g_count = len(g_queue)
            for i in range(0, g_count):
                g_cell = g_queue.pop(0)
                self.explored.append(g_cell.__hash__())
                g_successors = self.__successor(g_cell)

                for successor in g_successors:
                    if not g_cell.table[successor.row][successor.col]:
                        for s_cell in s_queue:
                            if successor.row == s_cell.row and successor.col == s_cell.col:
                                potential_answer = []
                                for path in s_cell.path:
                                    potential_answer.append([path.row, path.col])
                                for path in range(len(successor.path) - 2, -1, -1):
                                    potential_answer.append([successor.path[path].row, successor.path[path].col])

                                finished = self.cal_potential(potential_answer)
                                if finished:
                                    print(potential_answer)
                                    exit()

                        if successor.row == self.goal[0] and successor.col == self.goal[1]:
                            potential_answer = []
                            for path in range(len(successor.path) - 1, -1, -1):
                                potential_answer.append([successor.path[path].row, successor.path[path].col])

                            finished = self.cal_potential(potential_answer)
                            if finished:
                                print(potential_answer)
                                exit()

                        g_queue.append(successor)

    def cal_potential(self, answer):
        if answer[0][0] != self.source[0] or answer[0][1] != self.source[1]:
            return False
        for i in range(0, len(answer)-1):
            for j in range(i + 1, len(answer)):
                if answer[i] == answer[j]:
                    return False

        sum_path = self.__get_number(self.source[0], self.source[1])
        g_value = self.__get_number(self.goal[0], self.goal[1])

        for unit in answer:
            op = self.__get_opt(unit[0], unit[1])
            num = self.__get_number(unit[0], unit[1])

            if op == '^':
                sum_path **= num
            elif op == '*':
                sum_path *= num
            elif op == '+':
                sum_path += num
            elif op == 'b':
                g_value -= num
            elif op == '-':
                sum_path -= num
            elif op == 'a':
                g_value += num

        if sum_path > g_value:
            print("this is the answer")
            return True

        return False

    def a_star_search(self):
        a_list = []

        a_list.append(
            Cell(self.source[0], self.source[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                 self.__get_number(self.source[0], self.source[1]),
                 self.__get_number(self.goal[0], self.goal[1]), []))

        a_list[0].path.append(a_list[0])

        while a_list:
            cell = a_list.pop(0)
            self.explored.append(cell.__hash__())
            successors = self.__successor(cell)

            a_list_succs = []
            for successor in successors:
                if successor.row == self.goal[0] and successor.col == self.goal[1]:
                    if self.__check_goal(cell):
                        return
                else:
                    if not cell.table[successor.row][successor.col]:
                        a_list_succs.append(successor)

            temp_list = a_list + a_list_succs
            min_function_f = self.hueristic_cal(temp_list[0])
            if len(temp_list) >= 2:
                for i in range(1, len(temp_list)):
                    if self.hueristic_cal(temp_list[i]) < min_function_f:
                        min_function_f = self.hueristic_cal(temp_list[i])
                        temp_list[0], temp_list[i] = temp_list[i], temp_list[0]

            a_list = temp_list

    def hueristic_cal(self, cell: Cell):
        hueristic = 0
        for row in range(0, self.board.m):
            for col in range(0, self.board.n):
                if cell.table[row][col]:
                    op = self.__get_opt(row, col)
                    if op == '^':
                        hueristic += 11
                    elif op == '*':
                        hueristic += 5
                    elif op == '+':
                        hueristic += 2
                    elif op == 'b':
                        hueristic += 2
                    elif op == '-':
                        hueristic += 1
                    elif op == 'a':
                        hueristic += 1
                    elif op == 'g':
                        hueristic += 1

        function_f = (cell.goal_value - cell.path_value) + hueristic
        return function_f

    def ida_star_search(self):
        round1 = True

        while True:
            if not round1:
                cut_off_num = self.ida_cutoff
                for function_f in new_cut_offs:
                    if self.ida_cutoff < function_f:
                        self.ida_cutoff = function_f
                if self.ida_cutoff == cut_off_num:
                    print("no solution")
                    exit()

            new_cut_offs = []
            round1 = False

            ida_stack = [
                Cell(self.source[0], self.source[1], [[False for x in range(self.board.n)] for y in range(self.board.m)],
                     self.__get_number(self.source[0], self.source[1]),
                     self.__get_number(self.goal[0], self.goal[1]), [])]
            ida_stack[0].path.append(ida_stack[0])

            while ida_stack:
                cell = ida_stack.pop(len(ida_stack) - 1)

                self.explored.append(cell.__hash__())
                successors = self.__successor(cell)

                if cell.row == self.goal[0] and cell.col == self.goal[1]:
                    if self.__check_goal(cell):
                        exit()
                        return

                for successor in successors:
                    if not cell.table[successor.row][successor.col]:
                        new_cut_offs.append(self.hueristic_cal(successor))
                        if self.ida_cutoff >= self.hueristic_cal(successor):
                            ida_stack.append(successor)

    def __print_solution(self, cell: Cell):
        print(len(cell.path))

        for p in cell.path:
            print(str(p.row + 1) + ' ' + str(p.col + 1))


