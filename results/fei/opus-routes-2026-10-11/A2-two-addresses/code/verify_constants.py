"""Interval re-evaluation of the numeric constants used in the analytic parts of Theorems A and S, plus the
rho in {2,3} certificates with a finer subdivision (K = 20000)."""
from mpmath import iv, mp
import verify_rho23 as V
iv.dps = 40
L2 = lambda x: iv.log(x) / iv.log(2)
h = lambda t: -(t * L2(t) + (1 - t) * L2(1 - t))
c, k, d = V.C, V.KAP, V.DEL
GA, GB, SA, psi = V.GA, V.GB, V.SA, V.PSI
HI = V.HI; LO = V.LO
out = {}
# Lemma E (Theorem A): beta, case u=1 f0=0, case u=1 f0>=1, coefficient 1.2344
beta = L2(iv.mpf(17) / 16)
out["beta=log2(17/16) < 0.0875"] = HI(beta) < 0.0875
caseA = iv.mpf(5) / 8 * (4 + 1 + h(iv.mpf(1) / 10) - iv.mpf(4) / 10 - L2(iv.mpf(5)))
out["LemmaE u=1,f0=0 value < 1.72"] = HI(caseA) < 1.72
xs = 1 + beta - 1 / iv.log(2)
caseB = iv.mpf(2) ** xs / iv.log(2)
out["LemmaE u=1,f0>=1 max < 1.13 (x* <= 0)"] = HI(caseB) < 1.13 and HI(xs) <= 0
coef = L2(iv.mpf(5)) - 1 - beta
out["LemmaE coefficient log2 5 - 1 - beta >= 1.2344"] = LO(coef) >= 1.2344
# 5.2 scenario A
K = -d * L2(iv.mpf(2) ** (1 - c / d) + iv.mpf(2) ** (-2 * c / d))
out["5.2 K >= 2.4264"] = LO(K) >= 2.4264
gmax = d * L2(1 + iv.mpf(2) ** (-K / d))
rhs = iv.mpf("0.4569") * iv.mpf("0.55") * (1 + L2(iv.mpf("0.55")))
out["5.2 max(delta h - K eps) < 0.4569*0.55*(1+log2 0.55)"] = HI(gmax) < LO(rhs)
out["5.2 delta - 0.45 K < 0"] = HI(d - iv.mpf("0.45") * K) < 0
Pmin = k * (L2(iv.mpf(10)) - 2) - psi
out["5.2 kappa(log2 10 - 2) - psi >= 0.4569"] = LO(Pmin) >= 0.4569
out["5.2 kappa + G(2,1) >= 0.4569"] = LO(k + V.Gpair(2, 1)) >= 0.4569
# 5.4 / 5.5 tail
a = d + GB
jcoef = 2 * GB - 2 * k + 2 * (GB - GA) * SA
out["5.4 j-coefficient < 0"] = HI(jcoef) < 0
even_const = 2 * k + jcoef - 2 * GB
K0 = 2 * k - 2 * GB
out["5.4 even constant <= K0"] = HI(even_const) <= LO(K0)
gibbs = 2 * a * L2(1 + iv.mpf(2) ** (-c / a))
tail4 = gibbs + K0 - 4 * GB
out["5.5 tail bound at rho=4 < 0"] = HI(tail4) < 0
print("tail bound value at rho=4:", tail4)
# 5.7 rho = 1
odd_fair = 3 * d + 2 * k
out["5.7 3 delta + 2 kappa < 2.5221"] = HI(odd_fair) < 2.5221
caseEmptyOdd = odd_fair / 8 - (c - 3 * d) * iv.mpf(5) / 8
out["5.7(ii) empty odd: bound < 0"] = HI(caseEmptyOdd) < 0
wlog = d / (iv.e * iv.log(2))
neg = (odd_fair - c) / 4 + (odd_fair - 2 * c) / 8
out["5.7(ii) empty even: delta/(e ln2) + [(2.522-c)/4 + (2.522-2c)/8] < 0"] = HI(wlog + neg) < 0
out["5.7(ii) even rows worse per unit weight than odd fair rows"] = HI(3 * d - c) < LO(odd_fair - c)
# AND_3 identity: H - c I = 0
H = iv.mpf(4) - iv.mpf(9) / 8 * L2(iv.mpf(3)); I = iv.mpf(3) / 4
out["AND_3: |H - c* I| < 1e-35"] = HI(abs(H - c * I)) < mp.mpf("1e-35")
for kk, vv in out.items():
    print(("PASS " if vv else "FAIL ") + kk)
for rho, e_odd, mu in [(2, True, "-1.7668"), (3, True, "-1.4779"), (2, False, "-1.7058"), (3, False, "-1.4921")]:
    tot, M = V.certificate(rho, e_odd, mu, 20000)
    print(f"K=20000 rho={rho} e {'odd ' if e_odd else 'even'}: certified bound {float(tot):+.6f}", "PASS" if tot < 0 else "FAIL", flush=True)
