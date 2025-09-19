def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def tao_khoa(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    return (e, n), (d, n)

def ma_hoa(message, pub):
    e, n = pub
    c = []
    for ch in message:
        c.append(pow(ord(ch), e, n))
    return c

def giai_ma(cipher, pri):
    d, n = pri
    text = ""
    for num in cipher:
        text += chr(pow(num, d, n))
    return text

p = 17
q = 23
e = 5
P = "NguyenThiMyNhi"

pub, pri = tao_khoa(p, q, e)

print("Khoa cong khai:", pub)
print("Khoa bi mat:", pri)

cipher = ma_hoa(P, pub)
print("Ban ma hoa:", cipher)

plain = giai_ma(cipher, pri)
print("Giai ma lai:", plain)

