# file: test_calculator.py
from calculator import tinh_gia_tri_bieu_thuc

def test_cong():
    assert tinh_gia_tri_bieu_thuc("2+3") == 5

def test_loi():
    assert tinh_gia_tri_bieu_thuc("2+") == "Lỗi cú pháp"



