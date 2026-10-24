import numpy as np
import math

rng=np.random.default_rng(20260923)
worst_margin=float('inf')
tests=0
for m,n in [(9,8),(12,10),(20,16)]:
    q=min(m,n)
    for r in [1,2,3]:
        if r>=q-2:
            continue
        for _ in range(100):
            M0=rng.normal(size=(m,n))
            U=rng.normal(size=(m,r)); V=rng.normal(size=(n,r))
            L=(1+20*rng.random())*rng.choice([-1,1])*U@V.T/max(1,r)
            E0=rng.normal(size=(m,n))
            op=np.linalg.svd(E0,compute_uv=False)[0]
            delta=0.05+0.45*rng.random()
            E=delta*E0/op
            s0=np.linalg.svd(M0,compute_uv=False)
            sf=np.linalg.svd(M0+L+E,compute_uv=False)
            for j in range(q-r):
                rhs=max(s0[j+r]-delta,0.0)
                worst_margin=min(worst_margin,float(sf[j]-rhs))
            tests+=1

max_minimax_error=0.0
for _ in range(100):
    M0=rng.normal(size=(12,10))
    r=2; delta=.3
    U,s,Vt=np.linalg.svd(M0,full_matrices=False)
    L=np.zeros_like(M0)
    for k in range(2,min(2+r,len(s))):
        L -= s[k]*np.outer(U[:,k],Vt[k,:])
    E=np.zeros_like(M0)
    for k in range(2+r,len(s)):
        E -= min(delta,s[k])*np.outer(U[:,k],Vt[k,:])
    sf=np.linalg.svd(M0+L+E,compute_uv=False)
    lhs=float(np.sum(sf[2:]**2))
    rhs=float(np.sum(np.maximum(s[2+r:]-delta,0.0)**2))
    max_minimax_error=max(max_minimax_error,abs(lhs-rhs))

m=1024; N=m-3; delta=.01; mu=.04
a=2-delta
B=math.sqrt(N)*(mu-delta)
eps=mu+delta
Csharp=9*math.sqrt(3)*math.e/2
Ce5=9*math.sqrt(3*math.e)
sharp=Csharp/(a*a*B)**(1/3)
e5=Ce5/(a*a*B)**(1/3)
safe=4/sharp

print(f'rank_interlacing_random_tests={tests}')
print(f'minimum_observed_margin={worst_margin:.16g}')
print('exact_minimax_constructions=100')
print(f'max_abs_minimax_error={max_minimax_error:.16g}')
print(f'concrete_m={m}')
print(f'concrete_tail_count={N}')
print(f'delta={delta}')
print(f'mu={mu}')
print(f'a1=a2={a:.16g}')
print(f'B={B:.16g}')
print(f'leakage_bound={eps:.16g}')
print(f'B_over_15={B/15:.16g}')
print(f'gate_pass={eps <= B/15}')
print(f'e5f_Dprime_bound={e5:.16g}')
print(f'c241_tail_bound={sharp:.16g}')
print(f'partner_safe_pivot_threshold={safe:.16g}')
