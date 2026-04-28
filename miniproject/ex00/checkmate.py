
def checkmate(board):
    lines = board.strip().split('\n')
    size = len(lines)
    grid = [list(line) for line in lines]
# แปลงกระดานจากรูปแบบ String เป็น List of Lists เพื่อให้ง่ายต่อการเข้าถึงแต่ละช่อง

    kings = []
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                kings.append((r, c))
# ค้นหาตำแหน่งของคิง (K) ในกระดานทั้งหมด

    if not kings:
        print("No King found on the board.")
        return
# หากไม่พบคิงในกระดาน แสดงว่าไม่มีคิงอยู่เลย จึงไม่สามารถเป็น Check mate ได้(Error case)

    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    }
# ตรวจสอบการเคลื่อนที่ของเรือ (R), บิชอป (B) และควีน (Q) ที่สามารถโจมตีคิงได้

    knight_moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
# ตรวจสอบการเคลื่อนที่ของม้า (N) ที่สามารถโจมตีคิงได้ โดยตรวจสอบตำแหน่งที่ม้าสามารถเคลื่อนที่ไปได้จากตำแหน่งของคิง

    for kx, ky in kings:
        # ตรวจสอบสำหรับแต่ละคิง
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
        # ตรวจสอบเบี้ย (P) ที่โจมตีแบบทแยงมุมด้านหน้า (สมมติว่าคิงอยู่ด้านบน)

        for dc in [-1, 1]:
            r, c = kx + 1, ky + dc
            if 0 <= r < size and 0 <= c < size and grid[r][c] == 'P':
                print("Success")
                return
        # ตรวจสอบม้า (N)
        
        for dr, dc in knight_moves:
            r, c = kx + dr, ky + dc
            if 0 <= r < size and 0 <= c < size and grid[r][c] == 'N':
                print("Success")
                return
    print("Fail")
# หากไม่มีหมากรุกใดสามารถโจมตีคิงใดคิงหนึ่งได้ แสดงว่าไม่เป็น Check mate ดังนั้นผลลัพธ์จะเป็น "Fail"


# [ ตาราง และ พิกัด ]
# grid       : ตารางหมากรุกที่แปลงจาก String เป็น List 2 มิติ เพื่อให้ระบุตำแหน่งแบบ [แถว][คอลัมน์] ได้
# size       : ขนาดของกระดาน (N x N) ใช้สำหรับเช็คขอบเขตไม่ให้โปรแกรมทำงานเกินพื้นที่บอร์ด
# kx, ky     : พิกัดแกน X (แถว) และแกน Y (คอลัมน์) ของ King (K) ที่ใช้เป็นจุดศูนย์กลางในการตรวจจับ

# [ ระบบการเคลื่อนที่ ]
# r, c       : พิกัด แถว (row) และ คอลัมน์ (column) ปัจจุบันที่ "เรดาร์" กำลังตรวจสอบอยู่
# dr, dc     : ส่วนต่างการเคลื่อนที่ (Delta row, Delta column) ใช้กำหนดทิศทาง เช่น
#              - dr = -1 (ขึ้น), dr = 1 (ลง), dr = 0 (อยู่กับที่)
#              - dc = -1 (ซ้าย), dc = 1 (ขวา), dc = 0 (อยู่กับที่)

# [ ตัวหมากศัตรู ]
# piece_type : ประเภทของหมากที่โจมตีทางไกลได้ ได้แก่ 'R' (Rook), 'B' (Bishop), 'Q' (Queen)
# char       : ตัวอักษรที่พบในช่องนั้นๆ เพื่อเช็คว่าเป็นช่องว่าง ('.') หรือตัวหมากอันตราย
# 'P' (Pawn) : เบี้ย - โจมตีทแยงมุม 1 ช่อง
# 'N' (Knight): ม้า - โจมตีเป็นรูปตัว L (ข้ามหมากตัวอื่นได้)

# [ ทิศทาง (Directions) ]
# directions   : พจนานุกรม (Dictionary) เก็บกลุ่มทิศทางการเดินของหมากแต่ละประเภท
# knight_moves : รายการพิกัด 8 ตำแหน่งรอบตัว King ที่ม้าสามารถกระโดดมาโจมตีได้