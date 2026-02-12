# pylint: disable=missing-docstring

def is_valid_unit(unit):
    """Satır, sütun veya 3x3 karedeki sayıları 1-9 arası kontrol eder."""
    # 1'den 9'a kadar olan sayıların her biri tam olarak bir kez bulunmalıdır
    return sorted(unit) == list(range(1, 10))

def sudoku_validator(grid):
    """
    9x9 Sudoku grid'inin satır, sütun ve kare kurallarına göre doğruluğunu kontrol eder.
    """
    # 1. Satırların Kontrolü
    # Grid zaten satır listelerinden oluştuğu için doğrudan döngüye alıyoruz
    for row in grid:
        if not is_valid_unit(row):
            return False

    # 2. Sütunların Kontrolü
    # Her bir sütun indeksine (0-8) göre dikeydeki sayıları bir listeye topluyoruz
    for col_idx in range(9):
        column = [grid[row_idx][col_idx] for row_idx in range(9)]
        if not is_valid_unit(column):
            return False

    # 3. 3x3 Alt Karelerin Kontrolü
    # Grid'i 3'erli bloklar halinde geziyoruz
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(grid[r + i][c + j])
            if not is_valid_unit(square):
                return False

    # Tüm kontrollerden geçtiyse Sudoku geçerlidir
    return True
