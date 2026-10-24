#!/usr/bin/env python3
# Independent exact audit of P03-CN5-TAIL-RELAXATION-193.
# No peer code is imported or executed.
from math import log2

degree_list=[1]*5+[2]*10+[3]*10+[4]*5+[5]
K=2048
P_candidate=15**225
Q_candidate=80

def candidate_strictly_beats(P,Q):
    # (K-2 log_2 Pc)/Qc > (K-2 log_2 P)/Q
    # Convert exactly to an integer inequality.
    e=K*(Q-Q_candidate)
    if e>=0:
        return (2**e)*(P**(2*Q_candidate)) > P_candidate**(2*Q)
    return P**(2*Q_candidate) > (2**(-e))*(P_candidate**(2*Q))

print("independent exact-integer audit; no peer code imported")
for k in range(7,17):
    allowed=list(range(k%2,k+1,2))
    target=k*(32-k)
    states={(0,0):1}  # (nonconstant square sum,Q) -> minimum P_nonconst
    for degree in degree_list:
        nxt={}
        for (sq,q),prod0 in states.items():
            for a in allowed:
                ns=sq+a*a
                if ns>target:
                    continue
                nq=q+degree*a*a
                fac=1 if a==0 else a**(a*a)
                prod1=prod0*fac
                key=(ns,nq)
                if key not in nxt or prod1<nxt[key]:
                    nxt[key]=prod1
        states=nxt

    constant_mag=16-k
    constant_factor=1 if constant_mag==0 else constant_mag**(constant_mag**2)
    feasible=[]
    for (sq,q),prod_nonconst in states.items():
        if sq!=target or q%16:
            continue
        P=constant_factor*prod_nonconst
        assert candidate_strictly_beats(P,q)
        feasible.append((P,q))

    # Diagnostic decimal only; all decisions above are exact integers.
    best=max((K-2*log2(P))/q for P,q in feasible)
    print(f"k={k:2d} feasible_relaxed_states={len(feasible):2d} "
          f"best_relaxed_ratio={best:.15f}")

print("PASS: every relaxed k=7..16 state is strictly below the one-point C5 candidate")
