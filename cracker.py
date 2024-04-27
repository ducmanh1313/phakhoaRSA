from prime import find_factor
from powmod import power_modulo
from euklidian import inverse_modulo
from pollard import pollard


def main():
    
    n = int(input("Nhập n ( một phần của khóa công khai): "))
    e = int(input("Nhập e ( một phần của khóa công khai): "))
    #c = int(input("Nhập c (thông điệp đã được mã hóa để giải mã): "))
    b = int(input("Nhập b (số nguyên tố tối đa trong n, tùy chọn): ") or 1)
    
 

    if n < 2 or e < 2  or b > n or b <= 0:
        print("Đầu vào không hợp lệ")
        return
        
    p = None

    if b == 1:
        print("Đang phân tích n bằng thuật toán pollard......")
        p = find_factor(n)
    else:
        print("Đang phân tích n bằng thuật toán Pollard...")
        if b > n - 1:
            b = n - 1
        p = pollard(b, n)
    print("Phân tích hoàn tất.")
    print("p = %d" % p)

    q = n // p

    print("q = %d" % q)
    

    phi = (p - 1) * (q - 1) if p != q else p * p - p

    print("phi(n) = %d" % phi)

    print("Giải phương trình e * d = 1 mod phi(n) bằng thuật toán Euclid...")

    d = inverse_modulo(e, phi)

    print("d (khóa bí mật) = %d" % d)

    #m = power_modulo(c, d, n)

    #print("m (thông điệp giải mã) = %d" % m)


if __name__ == "__main__":
    main()
