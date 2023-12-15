from config_reader import Config


class ScrabbleBoard:
    def __init__(self):
        board_size = Config.board_size()
        init_state = [["#" for j in range(board_size)] for i in range(board_size)]
        self.board_states = [init_state]

    def get(self, age=0):
        saved_states_count = len(self.board_states)
        if saved_states_count > age:
            return self.board_states[saved_states_count - age - 1]
        raise "A board state this old does not exist."

    def print(self, age=0):
        board = self.get(age)

        print("   | ", end="")
        for i, row in enumerate(board):
            print(f"{i + 1:02}", end=" ")
        print("\n----------------------------------------------------")

        for i, row in enumerate(board):
            print(f"{i + 1:02}", end=" | ")
            for j, col in enumerate(row):
                print(col, end="  ")
            print(" |")
