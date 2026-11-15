# score.py
def is_valid_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Diem phai la kieu so")
    return 0 < score <= 10
