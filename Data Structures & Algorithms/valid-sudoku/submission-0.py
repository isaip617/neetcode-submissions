class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        sub_boxes = {}
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] != ".":
                    sub_box = 0
                    if row in rows:
                        if board[row][column] in rows[row]:
                            return False
                        else:
                            rows[row].add(board[row][column])
                    else:
                        rows[row] = set()
                        rows[row].add(board[row][column])
                    
                    if column in columns:
                        if board[row][column] in columns[column]:
                            return False
                        else:
                            columns[column].add(board[row][column])
                    else:
                        columns[column] = set()
                        columns[column].add(board[row][column])
                    
                    
                    if row < 3 and column < 3:
                        sub_box = 0
                    elif row < 3 and column > 2 and column < 6:
                        sub_box = 1
                    elif row < 3 and column > 5 and column < 9:
                        sub_box = 2
                    elif row < 6 and row > 2 and column < 3:
                        sub_box = 3
                    elif row < 6 and row > 2 and column > 2 and column < 6:
                        sub_box = 4
                    elif row < 6 and row > 2 and column > 5 and column < 9:
                        sub_box = 5
                    elif row < 9 and row > 5 and column < 3:
                        sub_box = 6
                    elif row < 9 and row > 5 and column > 2 and column < 6:
                        sub_box = 7
                    elif row < 9 and row > 5 and column > 5 and column < 9:
                        sub_box = 8
                    
                    if sub_box in sub_boxes:
                        if board[row][column] in sub_boxes[sub_box]:
                            return False
                        else:
                            sub_boxes[sub_box].add(board[row][column])
                    else:
                        sub_boxes[sub_box] = set()
                        sub_boxes[sub_box].add(board[row][column])

        return True



