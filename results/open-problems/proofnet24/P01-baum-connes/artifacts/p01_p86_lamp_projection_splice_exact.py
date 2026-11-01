from fractions import Fraction

# Exact self-check in Q[C2] for the finite-support lamp-projection splice.
# Elements are represented as a + b h with h^2 = 1.
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c)

zero = (Fraction(0), Fraction(0))
one = (Fraction(1), Fraction(0))
h = (Fraction(0), Fraction(1))
p = (Fraction(1, 2), Fraction(1, 2))   # (1+h)/2
q = (Fraction(1, 2), Fraction(-1, 2))  # (1-h)/2

assert mul(h, h) == one
assert mul(p, p) == p
assert mul(q, q) == q
assert mul(p, q) == zero
assert mul(q, p) == zero
assert add(p, q) == one

def matmul(A, B):
    out = [[zero, zero], [zero, zero]]
    for i in range(2):
        for j in range(2):
            s = zero
            for k in range(2):
                s = add(s, mul(A[i][k], B[k][j]))
            out[i][j] = s
    return out

S = [[p, q], [q, p]]
I = [[one, zero], [zero, one]]
assert matmul(S, S) == I

# w = s1 s2^{-2} s1^3 s2^{-5}
word = [(1, 1), (2, -1), (2, -1), (1, 1), (1, 1), (1, 1),
        (2, -1), (2, -1), (2, -1), (2, -1), (2, -1)]
e1 = sum(sign for gen, sign in word if gen == 1)
e2 = sum(sign for gen, sign in word if gen == 2)
assert (e1, e2) == (4, -7)

print("p^2=p:", mul(p, p) == p)
print("q^2=q:", mul(q, q) == q)
print("pq=qp=0:", mul(p, q) == zero and mul(q, p) == zero)
print("p+q=1:", add(p, q) == one)
print("S_h^2=I_2:", matmul(S, S) == I)
print("word exponent sums:", (e1, e2))
print("explicit splice support rows:")
print("  2 U[1,1] = u_w + u_{w h}")
print("  2 U[1,2] = u_w - u_{w h}")
print("  2 U[2,1] = 1 - u_h")
print("  2 U[2,2] = 1 + u_h")
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
