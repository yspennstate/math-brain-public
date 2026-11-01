"""Upward functional U'(f) = sum_S p_S log2(pi(S)/p_S), pi(S)=sum_{T superset S} p_T (= E[(d_S f)^2]).
Check H <= 2(I-Var) + 2U' (granularity theorem) exhaustively for n<=4, and report ratios."""
import numpy as np
from feilib import *

def upper_sets(p, n):
    """pi(S) = sum_{T >= S} p_T via superset zeta transform along each coordinate."""
    pi = p.copy()
    N = 1 << n
    for i in range(n):
        bit = 1 << i
        idx = np.arange(N)
        lo = idx[(idx & bit) == 0]
        pi[..., lo] = pi[..., lo] + pi[..., lo | bit]
    return pi

def Uprime(p, n):
    pi = upper_sets(p, n)
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(p > 0, p * np.log2(np.where(p > 0, pi / np.where(p>0,p,1), 1)), 0.0)
    return t.sum(-1)

if __name__ == "__main__":
    from exhaust import scan
    for n in [2, 3, 4]:
        r = scan(n); nc = r['I'] > 0
        p = r['p'][nc]; H = r['H'][nc]; I = r['I'][nc]; Var = r['Var'][nc]
        U = Uprime(p, n)
        slack = 2 * (I - Var) + 2 * U - H
        print(n, 'min slack of H<=2(I-Var)+2U :', slack.min(), ' max U/I:', (U / I).max(), ' max H/(2(I-Var)+2U):', (H / (2*(I-Var)+2*U)).max())
