# -*- coding: gb2312 -*-

def find_empty(board):
    '''
    找到board中下一个需要填充的位置
    :param board: 数独棋盘
    :return: 下一个需要填充的位置,如果棋盘已满,返回None
    '''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def valid(board, num, pos):
    """
    检查num是否可以填入board[pos]
    :param board: 数独棋盘
    :param num: 待填充的数字
    :param pos: 待填充的位置
    :return: 是否有效
    """
    # 检查同一行是否重复
    if num in board[pos[0]]:
        return False

    # 检查同一列是否重复
    if num in [board[i][pos[1]] for i in range(9)]:
        return False

    # 检查所在九宫格是否重复
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    if num in [board[box_y*3 + i][box_x*3 + j] for i in range(3) for j in range(3)]:
        return False

    return True



def solve(board):
    """
    使用回溯算法解决数独问题
    :param board: 数独棋盘
    :return: 是否解决成功
    """
    find = find_empty(board)
    if find[0] is None:
        return True

    row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    
    return False


if __name__ == "__main__":
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


    # board = [
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 2, 0, 3, 0, 0, 0, 4],
    #     [0, 0, 0, 5, 0, 0, 6, 0, 7],
    #     [5, 0, 0, 1, 4, 0, 0, 0, 0],
    #     [0, 7, 0, 0, 0, 0, 0, 2, 0],
    #     [0, 0, 0, 0, 7, 8, 0, 0, 9],
    #     [8, 0, 7, 0, 0, 9, 0, 0, 0],
    #     [4, 0, 0, 0, 6, 0, 3, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 5, 0, 0]

    # ]

    print(solve(board))
    for row in board:
        print(row)