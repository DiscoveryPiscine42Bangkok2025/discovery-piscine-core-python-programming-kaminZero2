def checkmate(board):
    lines = board.strip().split('\n')
    size = len(lines)
    grid = [list(line) for line in lines]
# หาตำแหน่งของคิง (K)
    kx, ky = -1, -1
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                kx, ky = r, c
                break
# หากไม่พบคิงในกระดาน พิมพ์ "Fail" และออกจากฟังก์ชัน
    if kx == -1:
        return
    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        'P': [(-1, -1), (-1, 1)]
    }
# ตรวจสอบการเคลื่อนที่ของเรือ (R), บิชอป (B), และควีน (Q) ที่สามารถโจมตีคิงได้ (หมากรุกเหล่านี้สามารถเคลื่อนที่ได้ในหลายช่อง)
    for piece_type, move_dirs in directions.items():
        for dr, dc in move_dirs:
            r, c = kx + dr, ky + dc
            while 0 <= r < size and 0 <= c < size:
                char = grid[r][c]
                if char != '.':
                    if char == piece_type or char == 'Q':
                        print("Check mate")
                        return
                    break
                r += dr
                c += dc
# ตรวจสอบการเคลื่อนที่ของเบี้ย (P) ที่สามารถโจมตีคิงได้ (เบี้ยสามารถโจมตีได้เฉพาะในทิศทางทแยงมุมไปข้างหน้า)
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = kx + dr, ky + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == 'P':
                print("Not check mate")
                return
# หากไม่มีหมากรุกใดสามารถโจมตีคิงได้ พิมพ์ "Fail"
    print("Fail")

# r = row, c = column, dr = delta row, dc = delta column
# piece_type = 'R', 'B', 'Q' , 'P' for rook, bishop, queen, pawn
# kx, ky = ตำแหน่งของคิงในกระดาน (king x, king y)
# directions = dictionary ที่เก็บทิศทางการเคลื่อนที่ของหมากรุกแต่ละประเภท