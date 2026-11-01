#!/usr/bin/env python3
"""Search then exact-check a finite-state drift certificate for PROB10-10.

The LP is used ONLY to discover a rational potential. After rounding, the
accepted certificate is verified state-by-state with Python integer arithmetic.
No floating-point inequality is used in the theorem check.
"""
from collections import deque, defaultdict
from fractions import Fraction
from hashlib import sha256
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

W,L=4,2
D=10**9
V_CERT_NUM=2667572300  # v = 2.6675723

def key(state):
    p,inf=state
    return str(p)+'|'+';'.join(f'{r},{d}' for r,d in sorted(inf))

def transitions(state):
    p,inf=state
    out=defaultdict(lambda:[0,0])
    for r,d in inf:
        for ds,dd in ((1,1),(1,-1),(-1,1),(-1,-1)):
            rp,dp=r+ds,d+dd
            if abs(dp)>W or rp < -L or rp>1: continue
            if rp<=0 and (rp,dp) in inf: continue
            ni=set(inf)
            if rp==1:
                ni={(rr-1,ddd) for rr,ddd in ni}
                ni.add((0,dp))
                ni={(rr,ddd) for rr,ddd in ni if rr>=-L}
                ns=(1-p,frozenset(ni)); adv=1
            else:
                ni.add((rp,dp)); ns=(p,frozenset(ni)); adv=0
            out[ns][0]+=1; out[ns][1]+=adv
    return [(ns,rate,adv_rate) for ns,(rate,adv_rate) in out.items()]

def reachable():
    start=(0,frozenset({(0,0)}))
    q=deque([start]); seen={start}
    while q:
        s=q.popleft()
        for ns,_,_ in transitions(s):
            if ns not in seen:
                seen.add(ns); q.append(ns)
    return sorted(seen,key=key)

states=reachable(); n=len(states); assert n==6271
idx={s:i for i,s in enumerate(states)}
rows=[]; cols=[]; dat=[]; a=np.zeros(n)
for i,s in enumerate(states):
    total=0
    for ns,rate,adv_rate in transitions(s):
        j=idx[ns]
        rows.append(i); cols.append(j); dat.append(rate)
        total += rate; a[i] += adv_rate
    rows.append(i); cols.append(i); dat.append(-total)
Q=sp.csr_matrix((dat,(rows,cols)),shape=(n,n),dtype=float)
# Maximize c under c-Qh <= a, gauge h(start)=0.
A=sp.hstack([-Q,np.ones((n,1))],format='csr')
b=a.copy(); objective=np.zeros(n+1); objective[-1]=-1
bounds=[(None,None)]*(n+1); bounds[0]=(0,0)
res=linprog(objective,A_ub=A,b_ub=b,bounds=bounds,method='highs')
assert res.success
H=np.rint(res.x[:-1]*D).astype(np.int64)
raw=('\n'.join(str(int(x)) for x in H)+'\n').encode()

# EXACT INTEGER CHECK. Recompute a+Qh without scipy floating arithmetic.
mn=None; mx=None; argmin=None; arcs=0
for i,s in enumerate(states):
    outs=transitions(s)
    lhs=sum(ar for _,_,ar in outs)*D
    for ns,rate,_ in outs:
        arcs += 1
        lhs += int(rate)*(int(H[idx[ns]])-int(H[i]))
    if mn is None or lhs<mn: mn=lhs; argmin=key(s)
    if mx is None or lhs>mx: mx=lhs
assert mn >= V_CERT_NUM
v=Fraction(V_CERT_NUM,D)
diag=Fraction(2,1)/v
assert diag == Fraction(20000000,26675723)
assert diag < Fraction(758507818076,10**12)
print('PROB10-10 exact pruned-Richardson finite-state drift certificate')
print(f'W={W} L={L} reachable_states={n} transition_arcs={arcs}')
print(f'potential_sha256={sha256(raw).hexdigest()}')
print(f'D={D}')
print(f'min_generator_num={mn} min_generator={Fraction(mn,D)}')
print(f'max_generator_num={mx} max_generator={Fraction(mx,D)}')
print(f'certificate_speed={v} approx={float(v):.10f}')
print(f'certificate_margin_num={mn-V_CERT_NUM}')
print(f'diagonal_upper=2/v={diag} approx={float(diag):.12f}')
print('old_diagonal_upper=189626954519/250000000000 approx=0.758507818076')
print(f'argmin_state={argmin}')
print('ALL_EXACT_INTEGER_CHECKS_PASS = True')
