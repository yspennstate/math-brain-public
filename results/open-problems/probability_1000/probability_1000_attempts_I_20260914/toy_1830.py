# Toy check of the mechanism behind the counterexample to Janson Problem 18.30(ii):
# bulk atoms {0,1,2}; rare atom A at L_A with n p_A = delta; rarer atom B at L_B = L_A / eps with n p_B = eps (so B's mean shift = L_A).
import numpy as np
def power(p, N, L):
    res = np.zeros(L+1); res[0]=1.0; base = p[:L+1].copy()
    while N:
        if N&1: res = np.convolve(res, base)[:L+1]
        N >>= 1
        if N: base = np.convolve(base, base)[:L+1]
    return res
def run(n, LA, eps, delta):
    LB = int(round(LA/eps)); pA = delta/n; pB = eps/n
    a=b=0.25
    p = np.zeros(LB+1); p[0]=1-a-b-pA-pB; p[1]=a; p[2]=b; p[LA]+=pA; p[LB]+=pB
    nu = (np.arange(LB+1)*p).sum(); m = int(round(nu*n))
    sd = np.sqrt(n*((np.arange(3)**2*p[:3]).sum() - (p[1]+2*p[2])**2))
    tot = power(p, n, m)[m]
    pb = p.copy(); pb[LA:] = 0.0        # no box >= LA
    P0 = power(pb, n, m)[m]
    Pn1 = power(pb, n-1, m)
    P1A = n*pA*Pn1[m-LA] if m>=LA else 0.0
    P1B = n*pB*Pn1[m-LB] if m>=LB else 0.0
    print(f"n={n} LA={LA} LB={LB} delta={delta} eps={eps} nu={nu:.4f} m={m} bulk sd={sd:.1f} Lambda=LA/sd={LA/sd:.2f}: "
          f"P(Y(1)>=LA | S=m)={1-P0/tot:.4f} [one A box: {P1A/tot:.4f}, one B box: {P1B/tot:.2e}]  vs  nP(xi>=LA)={delta+eps:.3f}")
run(4000, 250, 0.05, 0.05)
run(4000, 400, 0.05, 0.05)
run(8000, 600, 0.03, 0.03)
