"""Hod's slack function and the read-once inequality.

For a seed formula with (p, I, H), Hod's limit-of-limits construction F_{m+1} = (F_m AND F_{m+1})^dual has
(Prop 4.1) q_{m+1} = 1/(1+q_m), I+_{m+1} = I+_m / q_{m+1}, H+_{m+1} = (H+_m + h(q_m)/(1-q_m)) / q_{m+1}, so its
limit ratio is  R(p, I, H) = (H - h(V_p) + V_p S(p)) / I  with

    S(z) = sum_{j>=0} h(q_j) q_1 ... q_j / (1 - q_j),  q_0 = z, q_{j+1} = 1/(1+q_j),   i.e.  S(z) = h(z)/(1-z) + S(1/(1+z))/(1+z).

beta(1/2) = S(1/2) = 6.4547837 (seed = one variable). Every read-once f gives the lower bound R(f) <= C_RO, so if
C_RO = beta(1/2) then H(f) <= beta(1/2) I(f) - Gamma_H(p_f) with Gamma_H(p) = V_p S(p) - h(V_p). This script tests
whether Gamma_H is admissible for the functional inequality (A) (then the theorem follows) and where it is tight.
"""
import sys, math
import numpy as np
sys.path.insert(0, r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei")
from fei_readonce_gamma import Ht_and, h2

def S(z, terms=120):
    z = np.asarray(z, dtype=float)
    q = z.copy(); prod = np.ones_like(z); tot = np.zeros_like(z)
    for j in range(terms):
        tot += h2(q) * prod / (1 - q)
        qn = 1 / (1 + q)
        prod = prod * qn
        q = qn
    return tot

def gamma_H(p):
    p = np.asarray(p, dtype=float)
    V = 4 * p * (1 - p)
    return V * S(p) - h2(V)

def check(n=600, lo=0.002, hi=0.998):
    g = np.linspace(lo, hi, n)
    P, Q = np.meshgrid(g, g, indexing="ij")
    P = P.ravel(); Q = Q.ravel()
    lhs = gamma_H(P * Q)
    rhs = Q * (gamma_H(P) + h2(4 * P * (1 - P))) + P * (gamma_H(Q) + h2(4 * Q * (1 - Q))) - Ht_and(P, Q)
    D = rhs - lhs
    j = int(np.argmin(D))
    return float(D[j]), (float(P[j]), float(Q[j])), D, P, Q

if __name__ == "__main__":
    Phi = (math.sqrt(5) - 1) / 2
    print("S(1/2) = %.9f  (beta(1/2) = 6.4547837);  S(2/3) = %.6f" % (S(0.5), S(2 / 3)))
    print("Gamma_H at 1/2, 1/4, 1/8, Phi, 1/3, 0.1, 0.01: ", [round(float(gamma_H(x)), 5) for x in (0.5, 0.25, 0.125, Phi, 1 / 3, 0.1, 0.01)])
    ps = np.linspace(0.0005, 0.9995, 2000)
    gh = gamma_H(ps)
    print("min Gamma_H over (0,1): %.6f at p=%.4f ; symmetric? max|G(p)-G(1-p)| = %.2e" % (gh.min(), ps[np.argmin(gh)], np.abs(gh - gh[::-1]).max()))
    Dmin, where, D, P, Q = check()
    print("admissibility of Gamma_H: min D = %+.7f at p=%.4f q=%.4f" % (Dmin, where[0], where[1]))
    # tight set
    idx = np.argsort(D)[:12]
    print("smallest D pairs:", [(round(float(D[i]), 6), round(float(P[i]), 4), round(float(Q[i]), 4)) for i in idx])
    # D along p = q
    for p in (0.1, 0.25, 0.382, 0.5, 0.618, 0.7, 0.9):
        pp = np.array([p]); qq = np.array([p])
        d = float((qq * (gamma_H(pp) + h2(4 * pp * (1 - pp))) + pp * (gamma_H(qq) + h2(4 * qq * (1 - qq))) - Ht_and(pp, qq) - gamma_H(pp * qq))[0])
        print("  D(%.3f,%.3f) = %+.6f" % (p, p, d))
    # D(p, q) with q = 1/(1+p)^-1 ... the construction step: AND(F_m, F_{m+1}) has measures (q_m, q_{m+1}); check D there
    for p in (0.5, 2/3, 0.6, Phi):
        q = 1 / (1 + p)
        pp = np.array([p]); qq = np.array([q])
        d = float((qq * (gamma_H(pp) + h2(4 * pp * (1 - pp))) + pp * (gamma_H(qq) + h2(4 * qq * (1 - qq))) - Ht_and(pp, qq) - gamma_H(pp * qq))[0])
        print("  construction pair D(%.4f, %.4f) = %+.7f" % (p, q, d))
    # compare with the numerical value-iteration Gamma (N=600, C=6.4548)
    try:
        Gnum = np.load(r"~\AppData\Local\Temp\claude\<project>\07f56e82-b3da-42b4-8041-02c1a661a843\scratchpad\fei\gamma_N600_C64548_final.npy")
        psn = np.arange(1, 600) / 600
        diff = Gnum - gamma_H(psn)
        print("Gamma_num - Gamma_H: min %.5f at p=%.4f, max %.5f at p=%.4f" % (diff.min(), psn[np.argmin(diff)], diff.max(), psn[np.argmax(diff)]))
    except Exception as e:
        print("no numerical gamma file:", e)
