from checkmate import checkmate
# กำหนดโครงสร้างกระดานในรูปแบบ String (หลายบรรทัด)

def main():
    board = """\
R...
...K
..P.
...."""
    checkmate(board)
if __name__ == "__main__":
    main()
