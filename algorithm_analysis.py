from tic_tac_toe_with_minimax import findBestMove
from random import randint

# board = [
#     ['o', 'x', 'o'],
#     ['x', 'x', 'o'],
#     ['o', 'o', 'x']
# ]

# board = [
#     ['o', 'x', 'o'],
#     ['x', 'x', 'o'],
#     ['_', 'x', '_']
# ]

# board = [
#     ['o', 'x', '_'],
#     ['o', 'x', '_'],
#     ['o', '_', '_']
# ]

# board = [
#     ['x', 'o', '_'],
#     ['x', '_', '_'],
#     ['_', '_', '_']
# ]

# board = [
#     ['_', '_', '_'],
#     ['_', 'x', '_'],
#     ['o', '_', '_']
# ]

# board = [
#     ['_', 'x', '_'],
#     ['o', '_', '_'],
#     ['o', '_', '_']
# ]

# board = [
#     ['x', 'x', 'o'],
#     ['o', '_', '_'],
#     ['o', '_', '_']
# ]

# board = [
#     ['_', 'x', 'o'],
#     ['_', 'x', '_'],
#     ['o', '_', '_']
# ]


board = [
    ['x', 'o', '_'],
    ['_', 'o', '_'],
    ['_', '_', '_']
]


findBestMove(board)

# for test in range(20):
#     print("\n\n==================================")
#     board = [
#         ['_', '_', '_'],
#         ['_', '_', '_'],
#         ['_', '_', '_']
#     ]
#     num_of_x = 0;
#     num_of_o = 0;
#     for i in range(3):
#         for j in range(3):
#             x = randint(0, 1)
#             if (x == 1 and num_of_x<num_of_o):
#                 board[i][j] = 'x'
#                 num_of_x += 1
#             if (x == 0 and num_of_o<num_of_x+1):
#                 board[i][j] = 'o'
#                 num_of_o += 1
#     findBestMove(board)
#     print("==================================\n\n")
