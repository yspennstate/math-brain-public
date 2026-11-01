#!/usr/bin/env python3
"""
P03 FEI child-spectrum Hellinger-defect checker.

Exhaustively checks through dimension 4 (modulo global sign) the exact fiber
formula and the new bounds
  M_i <= j_i,
  JS(P_+,P_-) <= 2 M_i / ln 2,
  B_i <= M_i[log2(1/M_i)-D_2(nu_i||q_i)+1/ln2],
  Delta_i H <= M_i[log2(1/M_i)-D_2(nu_i||q_i)+3/ln2].
Also checks the exact identity Delta_i H=B_i+JS.

This is a sanity checker, not an independent proof audit.
"""
import math, json
import numpy as np

def fwht(vals):
    a=np.array(vals,dtype=float).copy()
    N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a/N

def entropy(P):
    ans=0.0
    for p in P:
        if p>0.0:
            ans -= p*math.log2(p)
    return ans

def restrict(vals,n,i,b):
    out=np.empty(1<<(n-1),dtype=np.int8)
    for y in range(1<<(n-1)):
        lo=y&((1<<i)-1); hi=y>>i
        x=lo | (b<<i) | (hi<<(i+1))
        out[y]=vals[x]
    return out

def influence(vals,n,i):
    bit=1<<i
    c=0
    for x in range(1<<n):
        if not (x&bit) and vals[x]!=vals[x|bit]:
            c+=1
    return c/float(1<<(n-1))

def B_i(vals,n,i):
    F=fwht(vals); p=F*F; bit=1<<i; ans=0.0
    for t in range(1<<n):
        if t&bit: continue
        s=p[t]+p[t|bit]
        if p[t]>0 and p[t|bit]>0:
            x=p[t|bit]/s
            ans += s*(-x*math.log2(x)-(1-x)*math.log2(1-x))
    return ans

stats={
  "coordinate_cases":0,
  "max_M_minus_j":0.0,
  "max_JS_bound_violation":0.0,
  "max_B_formula_error":0.0,
  "max_B_rebate_bound_violation":0.0,
  "max_Delta_identity_error":0.0,
  "max_Delta_rebate_bound_violation":0.0
}

for n in range(1,5):
    N=1<<n
    for mask in range(1<<(N-1)):
        vals=np.ones(N,dtype=np.int8)
        for x in range(1,N):
            if (mask>>(x-1))&1: vals[x]=-1
        Pf=fwht(vals)**2
        Hf=entropy(Pf)
        for i in range(n):
            g=restrict(vals,n,i,0); h=restrict(vals,n,i,1)
            a=fwht(g); b=fwht(h)
            P=a*a; Q=b*b; q=(P+Q)/2
            affinity=float(np.sqrt(P*Q).sum())
            M=(1-affinity)/2
            m=(np.abs(a)-np.abs(b))**2/4
            B=0.0; D=0.0
            if M>1e-15:
                nu=m/M
                for k in range(len(q)):
                    if m[k]>0:
                        r=m[k]/q[k]
                        if 0<r<1:
                            B += q[k]*(-r*math.log2(r)-(1-r)*math.log2(1-r))
                        if nu[k]>0:
                            D += nu[k]*math.log2(nu[k]/q[k])
            JS=entropy(q)-0.5*(entropy(P)+entropy(Q))
            Bactual=B_i(vals,n,i)
            alpha=influence(vals,n,i); j=min(alpha,1-alpha)
            Delta=Hf-0.5*(entropy(P)+entropy(Q))
            if M>1e-15:
                rhsB=M*(math.log2(1/M)-D+1/math.log(2))
                rhsDelta=M*(math.log2(1/M)-D+3/math.log(2))
            else:
                rhsB=rhsDelta=0.0
            stats["coordinate_cases"] += 1
            stats["max_M_minus_j"]=max(stats["max_M_minus_j"],M-j)
            stats["max_JS_bound_violation"]=max(stats["max_JS_bound_violation"],JS-2*M/math.log(2))
            stats["max_B_formula_error"]=max(stats["max_B_formula_error"],abs(B-Bactual))
            stats["max_B_rebate_bound_violation"]=max(stats["max_B_rebate_bound_violation"],B-rhsB)
            stats["max_Delta_identity_error"]=max(stats["max_Delta_identity_error"],abs(Delta-(B+JS)))
            stats["max_Delta_rebate_bound_violation"]=max(stats["max_Delta_rebate_bound_violation"],Delta-rhsDelta)

tol=2e-12
assert stats["max_M_minus_j"]<=tol
assert stats["max_JS_bound_violation"]<=tol
assert stats["max_B_formula_error"]<=tol
assert stats["max_B_rebate_bound_violation"]<=tol
assert stats["max_Delta_identity_error"]<=tol
assert stats["max_Delta_rebate_bound_violation"]<=tol
print(json.dumps({"status":"PASS","stats":stats},indent=2,sort_keys=True))
