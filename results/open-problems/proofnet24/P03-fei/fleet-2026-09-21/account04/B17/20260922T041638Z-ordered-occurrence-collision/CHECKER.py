from fractions import Fraction
from itertools import combinations
from math import log2, factorial, comb

TOL=2e-11

def entropy(ps):
    return sum(float(p)*(-log2(float(p))) for p in ps if p)

def walsh_masses(vals):
    N=len(vals); n=N.bit_length()-1
    a=[]
    for s in range(N):
        z=0
        for x,v in enumerate(vals):
            parity=(s & x).bit_count() & 1
            z += v * (-1 if parity else 1)
        a.append(Fraction(z,N))
    return [x*x for x in a]

def influence(masses):
    return sum((Fraction(s.bit_count(),1)*p for s,p in enumerate(masses)), Fraction(0))

def elementary_symmetric(q, k):
    dp=[Fraction(0)]*(k+1); dp[0]=Fraction(1)
    for x in q:
        for j in range(k,0,-1):
            dp[j]+=dp[j-1]*x
    return dp[k]

def check_one(vals):
    masses=walsh_masses(vals)
    n=(len(vals)).bit_length()-1
    H=entropy(masses)
    I=influence(masses)
    if I == 1:
        return None
    beta=I-1
    assert masses[0]==0
    W=[Fraction(0)]*(n+1)
    j=[Fraction(0)]*n
    for s,p in enumerate(masses):
        if not p: continue
        k=s.bit_count(); W[k]+=p
        for i in range(n):
            if (s>>i)&1: j[i]+=p
    assert sum(W)==1
    assert sum(j)==I
    q=[x/I for x in j]
    Hq=entropy(q)
    HK=entropy(W)
    elogfact=sum(float(W[k])*log2(factorial(k)) for k in range(1,n+1) if W[k])
    Dord=0.0
    for s,p in enumerate(masses):
        if not p: continue
        k=s.bit_count(); wk=W[k]
        prod=Fraction(1)
        for i in range(n):
            if (s>>i)&1: prod*=q[i]
        ratio=float(p)/(float(wk)*factorial(k)*float(prod))
        Dord += float(p)*log2(ratio)
    rhs=float(I)*Hq+HK-elogfact-Dord
    if abs(rhs-H)>TOL:
        raise AssertionError((n,H,rhs,Dord))
    coll_lb=0.0
    elog_e=0.0
    for k in range(1,n+1):
        if not W[k]: continue
        ek=elementary_symmetric(q,k)
        assert ek>0
        coll_lb += float(W[k])*(-log2(float(factorial(k)*ek)))
        elog_e += float(W[k])*log2(float(ek))
    if Dord+TOL < coll_lb:
        raise AssertionError(('data_processing',Dord,coll_lb))
    Ccoll=float(I)*Hq+elog_e
    if H > Ccoll+HK+TOL:
        raise AssertionError(('upper',H,Ccoll,HK))
    return float(Ccoll/float(beta)), H/float(beta), Dord-coll_lb

def and_suspend(vals):
    out=[]
    for y in (1,-1):
        for h in vals:
            num=1+y+h-y*h
            assert num in (-2,2)
            out.append(num//2)
    mh=walsh_masses(vals); mg=walsh_masses(out)
    Ih=influence(mh); Ig=influence(mg)
    Hh=entropy(mh); Hg=entropy(mg)
    if Ig != (1+Ih)/2:
        raise AssertionError(('I_susp',Ig,Ih))
    if abs(Hg-(2+Hh/2))>TOL:
        raise AssertionError(('H_susp',Hg,Hh))
    return Hh, Ih, Hg, Ig

def balanced_vals(n):
    N=1<<n
    for pos_rest in combinations(range(1,N), N//2-1):
        pos={0,*pos_rest}
        yield [1 if i in pos else -1 for i in range(N)]

max_coll=(-1,None)
max_true=(-1,None)
count=0
susp_count=0
for n in range(1,5):
    cn=0
    for vals in balanced_vals(n):
        cn+=1; count+=1
        r=check_one(vals)
        if r:
            cr,tr,gap=r
            if cr>max_coll[0]: max_coll=(cr,(n,vals.copy(),tr,gap))
            if tr>max_true[0]: max_true=(tr,(n,vals.copy(),cr,gap))
        and_suspend(vals); susp_count+=1
    print(f'balanced_n{n}={cn}')
print(f'balanced_total={count}')
print(f'suspension_checked={susp_count}')
print('max_collision_ratio_n_le_4=%.15f n=%d true_ratio=%.15f KL_extra=%.15f' % (max_coll[0],max_coll[1][0],max_coll[1][2],max_coll[1][3]))
print('max_true_ratio_n_le_4=%.15f n=%d collision_ratio=%.15f KL_extra=%.15f' % (max_true[0],max_true[1][0],max_true[1][2],max_true[1][3]))

print('ADDRESSING')
for m in range(1,11):
    I=Fraction(m+2,2); beta=Fraction(m,2); N=1<<m
    qa=Fraction(1,m+2)
    qd=Fraction(2, N*(m+2))
    q=[qa]*m+[qd]*N
    Hq=entropy(q)
    Ccoll=float(I)*Hq
    HK=0.0
    elog_e=0.0
    for b in range(m+1):
        wk=Fraction(comb(m,b),1<<m); k=1+b
        HK += float(wk)*(-log2(float(wk))) if wk else 0.0
        ek=Fraction(0)
        for a in range(max(0,k-N),min(m,k)+1):
            d=k-a
            if d<=N:
                ek += Fraction(comb(m,a))*qa**a*Fraction(comb(N,d))*qd**d
        elog_e += float(wk)*log2(float(ek))
    Ccoll += elog_e
    lower=(2*m-HK)/float(beta)
    print(f'm={m} Ccoll/beta={Ccoll/float(beta):.15f} true_H/beta=4.000000000000000 lower_from_H_minus_HK={lower:.15f}')

print('NONBOOLEAN_LEVEL2_RELAXATION')
for n in (3,8,32,128):
    C=log2(n*(n-1)/2)
    print(f'n={n} Ccoll/beta={C:.15f}')
print('n=3_uniform_level2_boolean_convolution_obstruction=PASS')
print('PASS')
