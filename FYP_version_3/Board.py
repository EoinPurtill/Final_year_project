import unicodedata


class Board:

    def __init__(self, board=None, size=8):

        assert size >= 4 and size % 2 == 0
        self.size = size
        # Check for the different types of input.

        if board is None:
            self.generate_initial_board()

        elif isinstance(board, str):
            self.board = list(map(list, self.convert_board(self.size, board)))

        elif all(isinstance(elem, str) for elem in board):
            self.board = list(map(list, board))

        elif all(isinstance(elem, str) for elem in board):
            def uni_to_str(u):
                return unicodedata.normalize('NFKD', u).encode('ascii', 'ignore')
            self.board = list([list(uni_to_str(u)) for u in board])

        elif all(isinstance(elem, list) for elem in board):
            self.board = board

    def __getitem__(self, item):
        i, j = item
        return self.board[i][j]

    def __setitem__(self, key, value):
        k1, k2 = key
        self.board[k1][k2] = value

    @staticmethod
    def board_tolist(size, board):
        board = board.replace('\n', '')
        board = board.replace(' ', '')
        return [board[i:i + size] for i in range(0, len(board), size)]

    def generate_board(self):
        self.board = self.board_tolist(self.size,
                                        """_x_x_x_x
                                        x_x_x_x_
                                        ___x_x_x
                                        x_______
                                        ________
                                        y_y_y_y_
                                        _y_y_y_y
                                        y_y_y_y_""")

    def is_inbound(self, position):
        if position[0] < 0 or position[0] >= len(self.board):
            return False
        if position[1] < 0 or position[1] >= len(self.board[0]):
            return False
        return True

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board
