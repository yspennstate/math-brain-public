#!/usr/bin/env python3
from itertools import product
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb

# ---------- local exact affine-slice fiber caps ----------
def proj_vectors(dim,p):
    # one representative per nonzero projective vector in F_p^dim
    for j in range(dim):
        for tail in product(range(p), repeat=dim-j-1):
            yield (0,)*j+(1,)+tail

@lru_cache(None)
def local_data(s,k,p):
    # relation has k coefficients +1 and s-k coefficients -1; p>s here.
    v=(1,)*k+(-1,)*(s-k)
    xs=[x for x in product((0,1), repeat=s) if sum(v[i]*x[i] for i in range(s))%p==0]
    assert len(xs)==comb(s,k)
    q=0
    # quotient dual by span(v): gauge first ambient coefficient to zero,
    # then projectivize the remaining s-1 coefficients.
    for u in proj_vectors(s-1,p):
        a=(0,)+u
        cnt=Counter(sum(a[i]*x[i] for i in range(s))%p for x in xs)
        q=max(q,max(cnt.values()))
    return len(xs),q

def Ltype(s,k):
    # projective +/- sign relations on a fixed support, classified by k=min(#plus,#minus)
    if 2*k==s:
        return comb(s,k)//2
    return comb(s,k)

def plane_count(m,a,b):
    s,k=a; t,l=b
    La,Lb=Ltype(s,k),Ltype(t,l)
    z=comb(m,s)*comb(m-s,t)*La*Lb
    if a==b: z//=2
    return z

def family_count(m,p,a,b):
    s,k=a; t,l=b
    free=m-s-t
    Hs,qs=local_data(s,k,p)
    Ht,qt=local_data(t,l,p)
    h=Hs*Ht*(2**free)
    caps=[qs*Ht*(2**free), qt*Hs*(2**free)]
    if free: caps.append(h//2)
    Q=max(caps)
    B=1
    for j in range(m-2):
        B*=max(0,h-min(2**j,Q))
    tail=max(0,h-m+1)*max(0,h-m)
    N=plane_count(m,a,b)
    return N*B*tail,(N,h,Q,B,tail,Hs,qs,Ht,qt)

m=10; p=11
# exact local q table used by every new family
qtable=[]
for s in range(3,8):
    for k in range(1,s//2+1):
        H,q=local_data(s,k,p)
        qtable.append((s,k,H,q))
expected_q=[
 (3,1,3,2),
 (4,1,4,3),(4,2,6,4),
 (5,1,5,4),(5,2,10,6),
 (6,1,6,5),(6,2,15,10),(6,3,20,12),
 (7,1,7,6),(7,2,21,15),(7,3,35,20),
]
assert qtable==expected_q

types=[(s,k) for s in range(3,m-2) for k in range(1,s//2+1)]
entries=[]
total_E=0
total_planes=0
for i,a in enumerate(types):
    for b in types[i:]:
        if a[0]+b[0]>m: continue
        # Retained R03 disjoint-plane catalog already paid the pair if both
        # local sign relations were maximally balanced. Keep only genuinely
        # new symmetry-broken type pairs.
        old=(a[1]==a[0]//2 and b[1]==b[0]//2)
        if old: continue
        E,info=family_count(m,p,a,b)
        if E:
            entries.append((a,b,E,info))
            total_E+=E
            total_planes+=info[0]

assert len(entries)==18
assert total_planes==363720
assert total_E==265896069414475904006400

D=5
c=Fraction(p*(p*p-1),p**D-1)
# Every new plane is disjoint from all previously credited M2 plane families:
# at least one sparse generator is non-maximally-balanced, and a disjoint-support
# plane has only its two generators below full support. Thus the retained C253
# bound has not yet received even the -c credit for these exact-nullity-2 matrices.
# Their old pointwise contribution is p+1, so exact nullity 2 permits the full
# subtraction p (not merely p-c).
full_slack=Fraction(p)
corr=Fraction(2**(m+1-m*m))*full_slack*total_E
assert corr==Fraction(11425221732653261500275,2417851639229258349412352)

old_num=4080135425100039167106240490725
old_den=7787900129957441143457185792
new=Fraction(old_num,old_den)-corr
assert new==Fraction(2040049312230419145475474052475,3893950064978720571728592896)

print('R03 RUN30 EXACT CHECK')
print('local q table (s,k,H,q) =',qtable)
print('new unbalanced disjoint type pairs =',len(entries))
for a,b,E,info in sorted(entries,key=lambda z:z[2],reverse=True):
    N,h,Q,B,tail,Hs,qs,Ht,qt=info
    print('type',a,b,'planes',N,'h',h,'Q',Q,'bases_lb',B,'tail',tail,'E',E)
print('new planes total =',total_planes)
print('new exact-corank-2 matrices lower bound E =',total_E)
print('full new-plane exact-nullity-2 slack =',full_slack)
print('normalized correction =',corr,'=',float(corr))
print('new r(11) upper =',new,'=',float(new))
print('SELF-CHECK PASS')
