def checkmate(board):
    lines = board.strip().split('\n')
    size = len(lines)
    grid = [list(line) for line in lines]
    
    kx, ky = -1, -1
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                kx, ky = r, c
                break
    
    if kx == -1:
        return

    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        'P': [(-1, -1), (-1, 1)]
    }

    for piece_type, move_dirs in directions.items():
        for dr, dc in move_dirs:
            r, c = kx + dr, ky + dc
            while 0 <= r < size and 0 <= c < size:
                char = grid[r][c]
                if char != '.':
                    if char == piece_type or char == 'Q':
                        print("Success")
                        return
                    break
                r += dr
                c += dc

    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = kx + dr, ky + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == 'P':
                print("Success")
                return

    print("Fail")
# r = row, c = column, dr = delta row, dc = delta column
# piece_type = 'R', 'B', 'Q' , 'P' for rook, bishop, queen, pawn
# kx, ky = position of the king
#directions = dictionary mapping piece types to their possible move directions
