from itertools import product
from fractions import Fraction
from math import comb


def falling(a,k):
    z=1
    for j in range(k): z*=a-j
    return z


def projective_reps(p,d):
    for first in range(d):
        for tail in product(range(p), repeat=d-first-1):
            yield (0,)*first+(1,)+tail


def balanced_slice_points(s,p):
    # Relation: sum_{i<floor(s/2)} x_i = sum of remaining x_i.
    a=s//2
    coeff=[1]*a+[-1]*(s-a)
    pts=[]
    for xs in product((0,1), repeat=s-1):
        sm=sum(coeff[i]*xs[i] for i in range(s-1))
        for xl in (0,1):
            if (sm+coeff[-1]*xl)%p==0:
                pts.append(tuple(xs))
    return pts


def max_projective_fiber(pts,p):
    d=len(pts[0])
    mx=0
    hist={}
    for a in projective_reps(p,d):
        cnt=[0]*p
        for x in pts:
            cnt[sum(ai*xi for ai,xi in zip(a,x))%p]+=1
        z=max(cnt)
        mx=max(mx,z)
        hist[z]=hist.get(z,0)+1
    return mx,hist


def L(s):
    # Number of projective balanced +/-1 relation lines on a fixed support.
    return comb(s,s//2)//2 if s%2==0 else comb(s,s//2)


def H(s):
    # Number of Boolean solutions of a balanced relation in the no-wrap regime used here.
    return comb(s,s//2)


def plane_count(m,s,t):
    if s<t:
        return comb(m,s)*L(s)*comb(m-s,t)*L(t)
    return comb(m,s)*L(s)*comb(m-s,s)*L(s)//2


def ccoef(p,D):
    return Fraction(p*(p*p-1),p**D-1)


def family(m,p,D,s,t,q):
    b=m-s-t
    assert b>=0
    h=H(s)*H(t)*(2**b)
    # Product-slice hyperplane cap: condition on any block on which the functional is nonzero.
    caps=[q[(p,s)]*H(t)*(2**b), q[(p,t)]*H(s)*(2**b)]
    if b>0:
        caps.append(h//2)
    cap=max(caps)
    d=m-2
    terms=[h-min(2**j,cap) for j in range(d)]
    assert min(terms)>0
    B=1
    for x in terms: B*=x
    N=plane_count(m,s,t)
    P=(h-m+1)*(h-m)
    assert P>0
    E=N*B*P
    slack=Fraction(p,1)-ccoef(p,D)
    delta=Fraction(2**(m+1)*slack.numerator*E, 2**(m*m)*slack.denominator)
    return dict(m=m,p=p,D=D,s=s,t=t,b=b,h=h,cap=cap,d=d,terms=terms,B=B,N=N,P=P,E=E,slack=slack,delta=delta)

print('R03 run26 exact checker')

# Exact local hyperplane fibers for every relation-block size used in the new finite families.
q={}
expected={3:(3,2),4:(6,4),5:(10,6),6:(20,12),7:(35,20)}
for p in (7,11):
    for s,(hs,qs) in expected.items():
        pts=balanced_slice_points(s,p)
        assert len(pts)==hs
        mx,hist=max_projective_fiber(pts,p)
        q[(p,s)]=mx
        print('block', 'p',p,'s',s,'H',len(pts),'max_fiber',mx,'hist',sorted(hist.items()))
        assert mx==qs

# New exact-corank-two disjoint-support families beyond the retained (3,3) family.
pairs9=[(3,5),(3,6),(4,5)]
pairs10=[(3,5),(3,6),(3,7),(4,5),(4,6),(5,5)]

total9=Fraction(0)
for st in pairs9:
    f=family(9,7,4,*st,q)
    total9+=f['delta']
    print('m9 family',st,'h',f['h'],'cap',f['cap'],'N',f['N'],'terms',f['terms'],'B',f['B'],'P',f['P'],'E',f['E'],'slack',f['slack'],'delta',f['delta'],float(f['delta']))

total10=Fraction(0)
for st in pairs10:
    f=family(10,11,5,*st,q)
    total10+=f['delta']
    print('m10 family',st,'h',f['h'],'cap',f['cap'],'N',f['N'],'terms',f['terms'],'B',f['B'],'P',f['P'],'E',f['E'],'slack',f['slack'],'delta',f['delta'],float(f['delta']))

print('total additional normalized correction n10',total9,float(total9))
print('total additional normalized correction n11',total10,float(total10))
assert total9==Fraction(2919975760805103,72057594037927936)
assert total10==Fraction(117729341485144277109346125,973487516244680142932148224)

# Retained run25 replay-certified baselines.
r10=Fraction(1271206021115125771515,4611686018427387904)
r11=Fraction(4088560671982932827043671156925,7787900129957441143457185792)
new10=r10-total9
new11=r11-total10
print('new r10',new10,float(new10))
print('new r11',new11,float(new11))
assert new10==Fraction(1271019142666434244923,4611686018427387904)
assert new11==Fraction(4087618837251051672826796387925,7787900129957441143457185792)
assert new10<r10 and new11<r11

print('SELF-CHECK PASS')
