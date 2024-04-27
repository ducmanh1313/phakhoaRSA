import sys
from prime import next_prime
from powmod import power_modulo
from euklidian import gcd, next_coprime


def compute_k(b: int) -> int:

    k = 1

    cur_prime = 2

    while cur_prime <= b:

        cur_expo = 1

        while cur_prime ** cur_expo <= b:
            k *= cur_prime
            cur_expo += 1

        cur_prime = next_prime(cur_prime)

    return k


def pollard(b: int, n: int) -> int:

    k = compute_k(b)

    sys.set_int_max_str_digits(10000)  # Tăng giới hạn cho phép chuyển đổi số nguyên sang chuỗi

    print("k có %d chữ số" % len(str(k)))

    p = 1
    # a là một phần tử tùy ý trong nhóm nhân của các ước số của 1 modulo n
    a = next_coprime(1, n)

    while p == 1 or p >= n:

        print("Thử với p = %d" % a)

        a_pow_k_mod_n_minus1 = power_modulo(a, k, n) - 1

        print("không chia hết" )

        p = gcd(a_pow_k_mod_n_minus1, n)

        a = next_coprime(a, n)
  
    return p
    
