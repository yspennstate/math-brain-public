from fractions import Fraction

# Exact self-check for P19-I0068-CONCAVIFICATION-BRIDGE-FAIL-03.
# We factor out the strictly positive scalar exp(-t) (or exp(-2t))
# from semigroup expressions, so every checked quantity is rational.


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def matvec(A, x):
    return [sum(A[i][k] * x[k] for k in range(2)) for i in range(2)]


I = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
N = [[Fraction(0), Fraction(-1)], [Fraction(0), Fraction(0)]]
A = [[I[i][j] + N[i][j] for j in range(2)] for i in range(2)]

# N^2=0, so (I+N)^(1/2)=I+N/2 and exp(-t(I+N))=exp(-t)(I-tN).
assert matmul(N, N) == [[Fraction(0), Fraction(0)],
                         [Fraction(0), Fraction(0)]]
Ahalf = [[I[i][j] + Fraction(1, 2) * N[i][j] for j in range(2)]
         for i in range(2)]
assert matmul(Ahalf, Ahalf) == A

t = Fraction(1, 4)
St = [[I[i][j] - t * N[i][j] for j in range(2)] for i in range(2)]
S2t = [[I[i][j] - 2 * t * N[i][j] for j in range(2)] for i in range(2)]
x = [Fraction(0), Fraction(1)]

u = matvec(Ahalf, matvec(St, x))
lhs = [v * v for v in u]
rhs = matvec(A, matvec(S2t, [v * v for v in x]))

print("A =", A)
print("Ahalf =", Ahalf)
print("t =", t)
print("exp(+t) S(t)x coefficient =", matvec(St, x))
print("exp(+t) A^(1/2)S(t)x coefficient =", u)
print("exp(+2t) |A^(1/2)S(t)x|^2 =", lhs)
print("exp(+2t) A S(2t)|x|^2 =", rhs)

assert lhs[0] == Fraction(1, 16)
assert rhs[0] == Fraction(-1, 2)
assert lhs[0] > 0 > rhs[0]

print("first-coordinate sign: lhs > 0, rhs < 0")
print("P19-I0068-CONCAVIFICATION-BRIDGE-FAIL-03 PASS")
