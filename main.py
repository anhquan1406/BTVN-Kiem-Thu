import math

# ================== BÀI 1: CHU VI HCN ==================
def chu_vi_hcn(a, b):
    if a <= 0 or b <= 0:
        return "Invalid input"
    return 2 * (a + b)


# ================== BÀI 2: DIỆN TÍCH HCN ==================
def dien_tich_hcn(a, b):
    if a <= 0 or b <= 0:
        return "Invalid input"
    return a * b


# ================== BÀI 3: PT BẬC 2 ==================
def giai_pt_bac2(a, b, c):
    if a == 0:
        if b == 0:
            return "Vo nghiem" if c != 0 else "Vo so nghiem"
        return f"PT bac 1: x = {-c / b}"

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Vo nghiem"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiem kep: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"2 nghiem: x1 = {x1}, x2 = {x2}"


# ================== BÀI 4: SỐ NGÀY TRONG THÁNG ==================
def so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        return "Invalid input"

    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        return 28


# ================== BÀI 5: SỐ NGUYÊN TỐ ==================
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# ================== BÀI 6: TỔNG XEN KẼ ==================
def tong_xen_ke(n):
    if n <= 0:
        return "Invalid input"

    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s -= i
        else:
            s += i
    return s


# ================== BÀI 7: UCLN ==================
def ucln(a, b):
    if a == 0 and b == 0:
        return "Invalid input"
    while b != 0:
        a, b = b, a % b
    return abs(a)


# ================== BÀI 8: TỔNG GIAI THỪA ==================
def giai_thua(n):
    if n < 0:
        return "Invalid"
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def tong_giai_thua(n):
    if n < 0:
        return "Invalid input"

    s = 0
    for i in range(1, n + 1):
        s += giai_thua(i)
    return s


# ================== MENU TEST ==================
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Chu vi HCN")
        print("2. Dien tich HCN")
        print("3. Giai PT bac 2")
        print("4. So ngay trong thang")
        print("5. Kiem tra so nguyen to")
        print("6. Tong xen ke")
        print("7. UCLN")
        print("8. Tong giai thua")
        print("0. Thoat")

        choice = input("Chon: ")

        try:
            if choice == "1":
                a = float(input("a = "))
                b = float(input("b = "))
                print("KQ:", chu_vi_hcn(a, b))

            elif choice == "2":
                a = float(input("a = "))
                b = float(input("b = "))
                print("KQ:", dien_tich_hcn(a, b))

            elif choice == "3":
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                print("KQ:", giai_pt_bac2(a, b, c))

            elif choice == "4":
                thang = int(input("Thang = "))
                nam = int(input("Nam = "))
                print("KQ:", so_ngay_trong_thang(thang, nam))

            elif choice == "5":
                n = int(input("n = "))
                print("So nguyen to?" , is_prime(n))

            elif choice == "6":
                n = int(input("n = "))
                print("KQ:", tong_xen_ke(n))

            elif choice == "7":
                a = int(input("a = "))
                b = int(input("b = "))
                print("UCLN:", ucln(a, b))

            elif choice == "8":
                n = int(input("n = "))
                print("KQ:", tong_giai_thua(n))

            elif choice == "0":
                break

            else:
                print("Lua chon khong hop le!")

        except:
            print("Loi: Du lieu khong hop le!")


# ================== RUN ==================
if __name__ == "__main__":
    menu()
