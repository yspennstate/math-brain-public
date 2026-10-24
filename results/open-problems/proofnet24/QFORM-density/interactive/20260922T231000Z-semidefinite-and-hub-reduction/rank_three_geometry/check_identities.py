try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import sympy as sp
# discriminant identity with an outside linear term (Lemma X' heavy case)
Stt, Stz, Szz, w, bp, uj, tau, Z2, z0, Z4, s, kap, x = sp.symbols('Stt Stz Szz w bp uj tau Z2 z0 Z4 s kap x', real=True)
T = w*x + tau
g = Stt*T**2 + 2*Stz*T*(Z2-z0) + Szz*(Z2-z0)**2 + kap + bp*(uj*x + Z4)
P = sp.Poly(sp.expand(g), x)
a = P.coeff_monomial(x**2); M = P.coeff_monomial(x)/2; C = P.coeff_monomial(1)
D = sp.expand(M**2 - a*(C - s))
detS = Stt*Szz - Stz**2
claim = sp.expand(w**2*(-detS)*(Z2-z0)**2 + w*bp*uj*Stz*(Z2-z0) + Stt*w*bp*(uj*tau - w*Z4) + bp**2*uj**2/4 - Stt*w**2*(kap - s))
print('Lemma X-prime discriminant identity holds:', sp.simplify(D - claim) == 0, flush=True)
# rank-3 discriminant: D = l*(L11*s - W^T N W), N = L11*Lperp - b b^T  (pivot bound in discriminant form)
l, L11, b1, b2, p11, p12, p22, Z0, V, U, e = sp.symbols('l L11 b1 b2 p11 p12 p22 Z0 V U e', real=True)
Tt = sp.sqrt(l)*x + e*Z0
Q = L11*Tt**2 + 2*Tt*(b1*V + b2*U) + p11*V**2 + 2*p12*V*U + p22*U**2
P = sp.Poly(sp.expand(Q), x)
a = P.coeff_monomial(x**2); M = P.coeff_monomial(x)/2; C = P.coeff_monomial(1)
D = sp.expand(M**2 - a*(C - s))
Wv = sp.Matrix([V, U]); bb = sp.Matrix([b1, b2]); Lp = sp.Matrix([[p11, p12], [p12, p22]])
N = L11*Lp - bb*bb.T
claim = sp.expand(l*(L11*s - (Wv.T*N*Wv)[0]))
print('rank-3 discriminant depends on W only (Z0 cancels):', sp.simplify(D - claim) == 0, flush=True)
# Sylvester: det N = L11 * det(Lambda-tilde)
Lt = sp.Matrix([[L11, b1, b2], [b1, p11, p12], [b2, p12, p22]])
print('det N == L11 det Lt:', sp.simplify(N.det() - L11*Lt.det()) == 0, flush=True)
