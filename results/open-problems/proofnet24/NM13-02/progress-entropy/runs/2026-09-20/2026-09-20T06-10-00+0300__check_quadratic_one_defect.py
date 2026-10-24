#!/usr/bin/env python3
import itertools, math
from fractions import Fraction

CCHI = 2.0 + 1.0/(math.sqrt(math.e)*math.log(2.0))

def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t*math.log2(t)-(1.0-t)*math.log2(1.0-t)

def fwht_int(vals):
    a = list(map(int, vals))
    h=1
    while h < len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def phase(m, edge_mask, linear_mask=0, flip=0):
    edges=[]
    k=0
    for i in range(m):
        for j in range(i+1,m):
            if (edge_mask>>k)&1:
                edges.append((i,j))
            k+=1
    vals=[]
    for x in range(1<<m):
        bit=(x & linear_mask).bit_count() & 1
        for i,j in edges:
            bit ^= ((x>>i)&1)&((x>>j)&1)
        v=-1 if bit else 1
        if x==flip:
            v=-v
        vals.append(v)
    return vals

def row_nonzero(m, edge_mask, i):
    k=0
    for a in range(m):
        for b in range(a+1,m):
            if (edge_mask>>k)&1 and (a==i or b==i):
                return True
            k+=1
    return False

def restrict(vals, m, i, bit):
    rem=[j for j in range(m) if j!=i]
    out=[]
    for y in range(1<<(m-1)):
        x=bit<<i
        for k,j in enumerate(rem):
            x |= ((y>>k)&1)<<j
        out.append(vals[x])
    return out

def influence_i(vals,m,i):
    bad=0
    for x in range(1<<m):
        if ((x>>i)&1)==0:
            bad += vals[x] != vals[x^(1<<i)]
    return Fraction(bad,1<<(m-1))

def local_B(vals,m,i):
    g=restrict(vals,m,i,0)
    h=restrict(vals,m,i,1)
    A=fwht_int(g); B=fwht_int(h)
    N=1<<(m-1)
    total=0.0
    fiber_data=[]
    for a,b in zip(A,B):
        q=Fraction(a*a+b*b,2*N*N)
        e=Fraction((a-b)*(a-b),4*N*N)
        if q:
            t=float(e/q)
            total += float(q)*h2(t)
            fiber_data.append((q,e/q))
    return total, fiber_data

lo,hi=1e-12,0.5
for _ in range(100):
    mid=(lo+hi)/2
    if h2(mid)-CCHI*mid > 0:
        lo=mid
    else:
        hi=mid
rho=(lo+hi)/2

canonical_q=sorted([Fraction(1,8)]*3+[Fraction(5,8)])
patterns=set()
count3=0
for edge_mask in range(1<<3):
    if edge_mask==0:
        continue
    for linear in range(1<<3):
        for flip in range(1<<3):
            vals=phase(3,edge_mask,linear,flip)
            for i in range(3):
                if not row_nonzero(3,edge_mask,i):
                    continue
                delta=influence_i(vals,3,i)
                B,fib=local_B(vals,3,i)
                qs=sorted(q for q,p in fib)
                assert qs==canonical_q, (edge_mask,linear,flip,i,qs)
                ps=sorted(p for q,p in fib)
                assert ps[:3] == [Fraction(1,10),Fraction(1,2),Fraction(1,2)] or \
                       ps[:3] == [Fraction(1,2),Fraction(1,2),Fraction(1,2)]
                assert delta in (Fraction(1,4),Fraction(3,4))
                patterns.add((delta, tuple(ps)))
                count3+=1

exact_B3 = Fraction(3,8) + Fraction(5,8)*h2(0.1)
ratio3 = exact_B3 / 0.25

count2=0
for linear in range(4):
    for flip in range(4):
        vals=phase(2,1,linear,flip)
        W=fwht_int(vals)
        nonzero=sum(w!=0 for w in W)
        assert nonzero==1
        count2+=1

max_ratio=(0.0,None)
counts={}
for m in range(2,6):
    E=m*(m-1)//2
    c=0
    for edge_mask in range(1<<E):
        vals=phase(m,edge_mask,0,0)
        for i in range(m):
            if not row_nonzero(m,edge_mask,i):
                continue
            d=float(influence_i(vals,m,i))
            B,_=local_B(vals,m,i)
            if d>0:
                ratio=B/d
                if ratio>max_ratio[0]:
                    max_ratio=(ratio,(m,edge_mask,i,d,B))
            assert B <= CCHI*d + 5e-12, (m,edge_mask,i,d,B,B/d)
            c+=1
    counts[m]=c

print("PASS")
print(f"CCHI={CCHI:.15f}")
print(f"rho_root_h2_eq_Cchi_t={rho:.15f}")
print(f"h2(3/8)/(3/8)={h2(3/8)/(3/8):.15f}")
print(f"n3_exact_cases={count3}")
print(f"n3_exact_B={exact_B3:.15f}")
print(f"n3_worst_ratio_at_delta_1/4={ratio3:.15f}")
print(f"n2_affine_after_one_flip_cases={count2}")
print("local_nonzero_polar_checks="+repr(counts))
print("max_observed_B_over_delta="+repr(max_ratio))
