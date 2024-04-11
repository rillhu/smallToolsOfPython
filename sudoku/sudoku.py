# -*- coding: gb2312 -*-

def find_empty(board):
    '''
    �ҵ�board����һ����Ҫ����λ��
    :param board: ��������
    :return: ��һ����Ҫ����λ��,�����������,����None
    '''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def valid(board, num, pos):
    """
    ���num�Ƿ��������board[pos]
    :param board: ��������
    :param num: ����������
    :param pos: ������λ��
    :return: �Ƿ���Ч
    """
    # ���ͬһ���Ƿ��ظ�
    if num in board[pos[0]]:
        return False

    # ���ͬһ���Ƿ��ظ�
    if num in [board[i][pos[1]] for i in range(9)]:
        return False

    # ������ھŹ����Ƿ��ظ�
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    if num in [board[box_y*3 + i][box_x*3 + j] for i in range(3) for j in range(3)]:
        return False

    return True



def solve(board):
    """
    ʹ�û����㷨�����������
    :param board: ��������
    :return: �Ƿ����ɹ�
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