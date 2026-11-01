#!/usr/bin/env python3
import sympy as sp

a,s = sp.symbols("a s", real=True)
Q = sp.Matrix([
    [-2, 2-a, a, 0],
    [ 2, -(2+a), 0, a],
    [ 0, 2*a, -(2+a), 2-a],
    [ 0, 0, 2, -2],
])
assert all(sp.simplify(sum(Q[i,j] for j in range(4))) == 0 for i in range(4))
assert all(sp.simplify(sum(Q[i,j] for i in range(4))) == 0 for j in range(4))

# Keilson-Kester generator inequalities, encoded with <=0 convention.
def mono_conditions(A):
    n=A.rows
    les=[]
    for i in range(n):
        for ip in range(i+1,n):
            for k in range(n):
                U=list(range(k,n))
                if i not in U and ip not in U:
                    les.append(sp.factor(sum(A[i,j] for j in U)-sum(A[ip,j] for j in U)))
                D=list(range(k+1))
                if i not in D and ip not in D:
                    # down-set criterion is row_i(D) >= row_ip(D), hence negate.
                    les.append(sp.factor(-(sum(A[i,j] for j in D)-sum(A[ip,j] for j in D))))
    return [x for x in les if x != 0]

cond_Q = mono_conditions(Q)
cond_Qt = mono_conditions(Q.T)
expected_Q = list(map(sp.factor, [-a, a-2, -2, 2*(a-1), -2, -2*a]))
expected_Qt = list(map(sp.factor, [-2*a, -2, 2*(a-1), -2, a-2, -a]))
assert sorted(map(str,cond_Q)) == sorted(map(str,expected_Q))
assert sorted(map(str,cond_Qt)) == sorted(map(str,expected_Qt))

R = sp.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
assert sp.simplify(Q.T - R*Q*R) == sp.zeros(4)

lam=sp.symbols("lam")
char = sp.factor(Q.charpoly(lam).as_expr())
expected_char = lam*(lam**3+(2*a+8)*lam**2+(a**2+16*a+16)*lam+32*a)
assert sp.expand(char-expected_char)==0

a0=sp.Rational(5,6)
char0=sp.factor((char/lam).subs(a,a0))
assert sp.expand(char0 - (2*lam+3)*(18*lam**2+147*lam+320)/36)==0
assert 147**2 - 4*18*320 == -1431
assert 1431 == 9*159

# Orthonormal reflection-parity basis: c,u,v,w as columns.
B=sp.Matrix([
 [sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2)],
 [sp.Rational(1,2),-sp.Rational(1,2), sp.Rational(1,2),-sp.Rational(1,2)],
 [sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2), sp.Rational(1,2)],
 [sp.Rational(1,2), sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2)],
])
assert B.T*B == sp.eye(4)
T=sp.simplify(B.T*Q*B)
expected_T=sp.Matrix([
 [0,0,0,0],
 [0,-4,-a,a],
 [0,a,-2*a,a],
 [0,-a,a,-4],
])
assert sp.simplify(T-expected_T)==sp.zeros(4)

M=expected_T[1:4,1:4].subs(a,a0)
res=sp.factor((s*sp.eye(3)-M).inv()[0,0])
expected_res=sp.factor((36*s**2+204*s+215)/((2*s+3)*(18*s**2+147*s+320)))
assert sp.simplify(res-expected_res)==0

alpha=sp.Rational(49,12)
beta=sp.sqrt(159)/12
# Laplace transform of the proposed Euclidean covariance kernel k(t).
proposed_LT = sp.Rational(1,28)*(
    -1/(s+sp.Rational(3,2))
    +29*(s+alpha)/((s+alpha)**2+beta**2)
    +(sp.Rational(59,1)/sp.sqrt(159))*beta/((s+alpha)**2+beta**2)
)
assert sp.simplify(proposed_LT-res)==0

print("Q_a_ROW_COLUMN_SUMS_PASS")
print("Q_a_FORWARD_MONOTONICITY_CONDITIONS:", cond_Q)
print("Q_a_REVERSE_MONOTONICITY_CONDITIONS:", cond_Qt)
print("Q_a_DOUBLE_MONOTONE_FOR_0_LE_a_LE_1_PASS")
print("REFLECTION_TIME_REVERSAL_IDENTITY_PASS")
print("CHARPOLY_PASS:", char)
print("a=5/6_CUBIC_FACTOR_PASS:", char0)
print("a=5/6_COMPLEX_PAIR: -49/12 +- i*sqrt(159)/12")
print("PARITY_BLOCK_PASS")
print("CENTERED_EVEN_RESOLVENT_PASS:", res)
print("EXACT_COVARIANCE_LAPLACE_MATCH_PASS")
print("ALL_EXACT_CHECKS_PASS")
