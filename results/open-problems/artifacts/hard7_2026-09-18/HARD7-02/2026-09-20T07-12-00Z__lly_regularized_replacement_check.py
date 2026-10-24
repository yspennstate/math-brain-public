#!/usr/bin/env python3
"""
HARD7-02 exact self-check for the regularized hybrid-volume route.

This is only a finite/symbolic check of:
  (1) the ridge Schur-complement determinant identity in the smallest
      nontrivial 2-row/2-column symbolic case;
  (2) Q = eta^2 (B^*B+eta^2 I)^{-1};
  (3) the exponent identities used for the choice
      a=(2+eps)/(2(1+eps)).

It is NOT an independent validation of the asymptotic theorem.
"""
import sympy as sp

b1,b2,a1,a2,eta = sp.symbols("b1 b2 a1 a2 eta", positive=True, real=True)
B = sp.Matrix([[b1,b2]])
a = sp.Matrix([[a1,a2]])
H = sp.Matrix.vstack(B,a)

S = B*B.T + eta**2*sp.eye(1)
Q = sp.eye(2) - B.T*S.inv()*B

lhs = sp.factor((H*H.T + eta**2*sp.eye(2)).det())
rhs = sp.factor(S.det() * (eta**2 + (a*Q*a.T)[0]))
assert sp.simplify(lhs-rhs) == 0

Q2 = eta**2*(B.T*B + eta**2*sp.eye(2)).inv()
assert Q.applyfunc(sp.simplify) == Q2.applyfunc(sp.simplify)

# In this rank-one 1x2 case, Q has one eigenvalue exactly 1,
# hence tr Q >= 1 = n-m+1.
assert sp.simplify(sp.trace(Q)-1) == eta**2/(b1**2+b2**2+eta**2)

eps = sp.symbols("eps", positive=True)
alpha = (2+eps)/(2*(1+eps))
assert sp.simplify(1-alpha - eps/(2*(1+eps))) == 0
assert sp.simplify((1+eps)*alpha - (1+eps/2)) == 0

print("schur_identity = PASS")
print("ridge_resolvent_identity = PASS")
print("trace_gap_identity = PASS")
print("1-alpha =", sp.simplify(1-alpha))
print("(1+eps)*alpha =", sp.simplify((1+eps)*alpha))
print("ALL_EXACT_CHECKS_PASS = True")
