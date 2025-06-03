# file: calculator.py
def tinh_gia_tri_bieu_thuc(expr):
    try:
        return eval(expr)
    except:
        return "Lỗi cú pháp"
