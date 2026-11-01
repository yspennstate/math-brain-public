from itertools import product, combinations
from fractions import Fraction
from math import factorial

def rank_mod(rows,p):
    A=[list(x%p for x in row) for row in rows]
    if not A: return 0
    nr=len(A); nc=len(A[0]); r=0
    for c in range(nc):
        piv=next((i for i in range(r,nr) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(nr):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(nc)]
        r+=1
        if r==nr: break
    return r

def falling(a,k):
    z=1
    for j in range(k): z*=a-j
    return z

def Nmk(m,k):
    return falling(m,3*k)//(2**k*factorial(k))

def qbinom(n,k,p):
    if k<0 or k>n: return 0
    num=den=1
    for i in range(k):
        num*=p**(n-i)-1
        den*=p**(k-i)-1
    return num//den

def ccoef(p,D):
    return Fraction(p*(p*p-1),p**D-1)

def slack(p,D,k):
    return Fraction(qbinom(k,1,p),1)-ccoef(p,D)*qbinom(k,2,p)-1

def projective_reps(p,d):
    for first in range(d):
        for tail in product(range(p), repeat=d-first-1):
            yield (0,)*first+(1,)+tail

def support_spectrum_k3(p):
    reps=list(projective_reps(p,3))
    hist={3:0,6:0,9:0}
    for a,b,c in reps:
        t=(a!=0)+(b!=0)+(c!=0)
        hist[3*t]+=1
    return hist

def local_T_max(p):
    T=((0,0),(1,0),(0,1))
    mx=0
    for a in range(p):
        for b in range(p):
            if a==0 and b==0: continue
            vals=[(a*x+b*y)%p for x,y in T]
            for target in range(p):
                mx=max(mx,sum(v==target for v in vals))
    return mx

def hybrid_basis(h,d):
    cap=2*h//3
    terms=[h-min(2**j,cap) for j in range(d)]
    z=1
    for x in terms: z*=x
    return z,terms

print("R03 run25 exact checker")
print("local T max p7",local_T_max(7))
print("local T max p11",local_T_max(11))
assert local_T_max(7)==2
assert local_T_max(11)==2

print("support spectrum k3 p7",support_spectrum_k3(7))
print("support spectrum k3 p11",support_spectrum_k3(11))
assert support_spectrum_k3(7)=={3:3,6:18,9:36}
assert support_spectrum_k3(11)=={3:3,6:30,9:100}

# Exact finite core at m=9, k=3, p=7: C_V = T^3 in six free coordinates.
T=((0,0),(1,0),(0,1))
pts=[tuple(sum((list(a) for a in blocks),[])) for blocks in product(T,repeat=3)]
assert len(pts)==27 and pts[0]==(0,0,0,0,0,0)
max_hyp=0
hyp_hist={}
for a in projective_reps(7,6):
    z=sum(sum(ai*xi for ai,xi in zip(a,x))%7==0 for x in pts)
    max_hyp=max(max_hyp,z)
    hyp_hist[z]=hyp_hist.get(z,0)+1
print("m9k3 projective hyperplanes checked",sum(hyp_hist.values()))
print("m9k3 hyperplane zero-count histogram",sorted(hyp_hist.items()))
print("m9k3 max hyperplane intersection",max_hyp)
assert sum(hyp_hist.values())==(7**6-1)//6
assert max_hyp==18

nonzero=pts[1:]
unordered_bases=0
for comb in combinations(nonzero,6):
    if rank_mod(comb,7)==6:
        unordered_bases+=1
ordered_bases=unordered_bases*factorial(6)
print("m9k3 unordered exact bases",unordered_bases)
print("m9k3 ordered exact bases",ordered_bases)
assert unordered_bases==103089
assert ordered_bases==74224080

# Strengthen run24 k=2 family by combining the cube-subspace and 2/3-hyperplane caps.
for m,p,D in [(9,7,4),(10,11,5)]:
    k=2
    h=3**k*2**(m-3*k)
    d=m-k
    oldB=1
    for j in range(d): oldB*=h-2**j
    newB,terms=hybrid_basis(h,d)
    print("k2 m",m,"h",h,"d",d,"hybrid_terms",terms)
    print("k2 basis old/new/ratio",oldB,newB,Fraction(newB,oldB))
    assert newB==3*oldB

# New k=3 family counts.
def family(m,p,D,basis_override=None):
    k=3
    h=3**k*2**(m-3*k)
    d=m-k
    N=Nmk(m,k)
    B,terms=hybrid_basis(h,d)
    if basis_override is not None: B=basis_override
    extra_start=h-m+k-1
    P=falling(extra_start,k)
    E=N*B*P
    s=slack(p,D,k)
    delta=Fraction((2**(m+1))*s.numerator*E,(2**(m*m))*s.denominator)
    return h,d,N,B,terms,extra_start,P,E,s,delta

f9=family(9,7,4,ordered_bases)
f10=family(10,11,5)
for m,f in [(9,f9),(10,f10)]:
    h,d,N,B,terms,start,P,E,s,delta=f
    print("k3 m",m,"h",h,"d",d,"N",N)
    print("k3 hybrid_terms",terms,"basis_used",B)
    print("k3 extra_start/falling",start,P)
    print("k3 E",E)
    print("k3 slack",s,float(s))
    print("k3 normalized_delta",delta,float(delta))

assert f9[0]==27 and f9[2]==7560 and f9[7]==3838156866432000
assert f9[8]==Fraction(2401,50)
assert f9[9]==Fraction(359977134230595,4611686018427387904)

assert f10[0]==54 and f10[2]==75600
assert f10[3]==95386262400
assert f10[4]==[53,52,50,46,38,22,18]
assert f10[7]==656796226922035200000
assert f10[8]==Fraction(2108304,16105)
assert f10[9]==Fraction(1056462182925899124375,7605371220661563616657408)

# Retained run24 baselines and its original k=2 corrections.
r10=Fraction(635761490123149925535,2305843009213693952)
r11=Fraction(4089232687152555736280595956925,7787900129957441143457185792)
old_delta2_9=Fraction(1207729927215,35184372088832)
old_delta2_10=Fraction(319925953077122266875,7427120332677308219392)

# New k=2 family is exactly 3x the prior certified family, so reclaim 2 additional copies
# of the run24 exact-corank-two correction; k=3 is disjoint by exact nullity.
new10=r10-2*old_delta2_9-f9[9]
new11=r11-2*old_delta2_10-f10[9]
print("additional k2 delta n10",2*old_delta2_9,float(2*old_delta2_9))
print("additional k2 delta n11",2*old_delta2_10,float(2*old_delta2_10))
print("new r10",new10,float(new10))
print("new r11",new11,float(new11))
assert new10==Fraction(1271206021115125771515,4611686018427387904)
assert new11==Fraction(4088560671982932827043671156925,7787900129957441143457185792)
assert new10<r10 and new11<r11

print("SELF-CHECK PASS")
