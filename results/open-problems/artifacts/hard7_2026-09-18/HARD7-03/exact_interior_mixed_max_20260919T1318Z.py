from fractions import Fraction as F
from itertools import permutations
from math import factorial

A_VARS=(-1,0,1)
BASES_ALL={
    -2:{-1},
    -1:{-1,0},
    0:{-1,0,1},
    1:{0,1},
    2:{1},
}

def A3(t):
    return F(2) * (
        F(2268) - F(4408)*t + F(3748)*t**2 - F(1918)*t**3
        + F(652)*t**4 - F(143)*t**5 + F(18)*t**6 - t**7
    ) / ((F(3)-t)**4*(F(2)-t)**3*(F(1)-t)**3)

def M2(z,t):
    z=abs(z)
    if z==2: return F(1)/(F(1)-t)**2
    if z==1: return F(2)/((F(1)-t)**2*(F(2)-t))
    if z==0: return F(6)/((F(1)-t)**2*(F(2)-t)*(F(3)-t))
    raise ValueError(z)

def pair_correction(t):
    return F(8)/(F(2)-t)*(M2(0,t)+M2(1,t)+M2(2,t))

def kappa(t):
    return t/((F(2)-t)*(F(3)-t))

def ordered_exp_integral(c):
    c1,c2,c3=c
    rates=[
        F(3)-(c1+c2+c3),
        F(2)-(c2+c3),
        F(1)-c3,
    ]
    assert all(r>0 for r in rates), (c,rates)
    return F(1)/(rates[0]*rates[1]*rates[2])

def ordered_exp_gap_integral(c,lo,hi):
    assert 0<=lo<hi<=2
    c1,c2,c3=c
    rates=[
        F(3)-(c1+c2+c3),
        F(2)-(c2+c3),
        F(1)-c3,
    ]
    assert all(r>0 for r in rates)
    base=F(1)/(rates[0]*rates[1]*rates[2])
    return base*sum(F(1,rates[j]) for j in range(lo+1,hi+1))

def ordered_exp_gap2_integral(c,lo,hi):
    assert 0<=lo<hi<=2
    c1,c2,c3=c
    rates=[
        F(3)-(c1+c2+c3),
        F(2)-(c2+c3),
        F(1)-c3,
    ]
    assert all(r>0 for r in rates)
    base=F(1)/(rates[0]*rates[1]*rates[2])
    inv=[F(1,rates[j]) for j in range(lo+1,hi+1)]
    return base*(sum(inv)**2+sum(x*x for x in inv))

def weighted_target_max(t,bases,target):
    labels=list(bases)
    competitors=[j for j in labels if j!=target]
    total=F(0)
    for perm in permutations(A_VARS):
        rank={var:i for i,var in enumerate(perm)}
        br={label:max(rank[v] for v in subset) for label,subset in bases.items()}
        M=max(br.values())
        for mask in range(1<<len(competitors)):
            S=[competitors[k] for k in range(len(competitors)) if (mask>>k)&1]
            q=F(1)-t+len(S)
            c=[F(0),F(0),F(0)]
            c[br[target]]+=1
            for j in S: c[br[j]]+=1
            c[M]-=q
            term=ordered_exp_integral(c)/q
            total += -term if len(S)%2 else term
    return total

def interval_integral(c,q,Lrank,Urank=None):
    if Urank is not None and Urank<=Lrank:
        return F(0)
    cL=list(c)
    cL[Lrank]-=q
    ans=ordered_exp_integral(cL)/q
    if Urank is not None:
        cU=list(c)
        cU[Urank]-=q
        ans-=ordered_exp_integral(cU)/q
    return ans

def weighted_chain(t,bases,upper,target,lowers):
    total=F(0)
    for perm in permutations(A_VARS):
        rank={var:i for i,var in enumerate(perm)}
        br={label:max(rank[v] for v in subset) for label,subset in bases.items()}
        Lrank=max([br[target]]+[br[l] for l in lowers])
        Urank=br[upper]
        for mask in range(1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1]
            sign=-1 if len(S)%2 else 1
            c=[F(0),F(0),F(0)]
            c[br[target]]+=1
            for l in S: c[br[l]]+=1
            q1=F(1)-t+len(S)
            total += sign*interval_integral(c,q1,Lrank,Urank)
            c2=list(c)
            c2[Urank]+=1
            q2=q1+1
            total += sign*interval_integral(c2,q2,max(Lrank,Urank),None)
    return total

def local_minimum_correction(t):
    M2loc=weighted_target_max(t,{2:{1},1:{0,1}},2)
    M1_target=weighted_target_max(t,{0:{-1,0,1},1:{0,1},2:{1}},1)
    M1_chain=weighted_chain(t,BASES_ALL,upper=-1,target=2,lowers=[0,1])
    M1loc=M1_target+M1_chain
    M0_target=weighted_target_max(t,{-1:{-1,0},0:{-1,0,1},1:{0,1}},0)
    M0_chain=weighted_chain(t,BASES_ALL,upper=2,target=-1,lowers=[0,1])
    M0loc=M0_target+2*M0_chain
    Hloc=kappa(t)*(2*M2loc+2*M1loc+M0loc)
    return Hloc,M2loc,M1loc,M0loc

def weighted_penalty_complement(t,bases,target,lowers):
    r=F(2)-t
    total=F(0)
    lowers=list(lowers)
    for perm in permutations(A_VARS):
        rank={var:i for i,var in enumerate(perm)}
        br={label:max(rank[v] for v in subset) for label,subset in bases.items()}
        rt=br[target]
        m=max(br[l] for l in lowers)
        for mask in range(1,1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1]
            nS=len(S)
            coeff=F(((-1)**(nS+1))*nS)
            c=[F(0),F(0),F(0)]
            for l in S: c[br[l]]+=1
            if rt<=m:
                q=F(nS)+F(1)-t
                c2=list(c); c2[rt]+=1; c2[m]-=q
                total += coeff/r/q*ordered_exp_integral(c2)
            else:
                if nS==1:
                    c_mid=list(c); c_mid[rt]+=t-F(1)
                    total += coeff/r*ordered_exp_gap_integral(c_mid,m,rt)
                else:
                    qmid=F(nS-1)
                    cA=list(c); cA[rt]+=t-F(1); cA[m]-=qmid
                    cB=list(c); cB[rt]+=t-F(nS)
                    total += coeff/r/qmid*(ordered_exp_integral(cA)-ordered_exp_integral(cB))
                q=F(nS)+F(1)-t
                cU=list(c); cU[rt]+=F(1)-q
                total += coeff/r/q*ordered_exp_integral(cU)
    return total

def edge_chain_terms_full(t):
    aa=F(1)-t
    bb=F(2)-t
    cc=F(3)-t
    T1=T2=T3=F(0)
    for perm in permutations(A_VARS):
        rank={var:i for i,var in enumerate(perm)}
        r0=max(rank[v] for v in {-1,0,1})
        r1=max(rank[v] for v in {0,1})
        r2=rank[1]
        assert r0>=r1>=r2

        c=[F(0),F(0),F(0)]
        c[r2]+=1
        c[r1]-=aa
        term1=F(0)
        if r1>r2:
            term1 += ordered_exp_gap_integral(c,r2,r1)/bb
        term1 += ordered_exp_integral(c)/(bb**2)
        c2=[F(0),F(0),F(0)]
        c2[r1]+=1
        c2[r2]+=1
        c2[r0]-=bb
        if r0>r2:
            term1 += ordered_exp_gap_integral(c2,r2,r0)*(F(1,cc)-F(1,bb))
        term1 += ordered_exp_integral(c2)*(F(1,cc**2)-F(1,bb**2))
        T1 += term1

        c3=[F(0),F(0),F(0)]
        c3[r2]+=1
        c3[r0]-=aa
        term2=F(0)
        if r1>r2:
            term2 += ordered_exp_gap_integral(c3,r2,r1)/bb
        term2 += ordered_exp_integral(c3)/bb
        if r0>r2:
            term2 += ordered_exp_gap_integral(c2,r2,r0)/bb*(F(-1)+F(1,cc))
        term2 += ordered_exp_integral(c2)/bb*(F(-1)+F(1,cc**2))
        T2 += term2

        base2=ordered_exp_integral(c2)
        s1=ordered_exp_gap_integral(c2,r2,r0) if r0>r2 else F(0)
        s2=ordered_exp_gap2_integral(c2,r2,r0) if r0>r2 else F(0)
        d2=ordered_exp_gap2_integral(c2,r2,r1) if r1>r2 else F(0)
        term3=F(1,2)*((s2-d2)/cc+F(2)*s1/(cc**2)+F(2)*base2/(cc**3))
        T3 += term3
    return T1,T2,T3

def chain_max_transform(bases, upper, target, lowers, p, q):
    lowers=list(lowers)
    total=F(0)
    lam0=F(2)-p-q
    assert F(1)-p>0 and lam0>0
    for perm in permutations(A_VARS):
        rank={var:i for i,var in enumerate(perm)}
        br={label:max(rank[v] for v in subset) for label,subset in bases.items()}
        ru,rt=br[upper],br[target]
        assert ru<=rt, (perm,upper,target,ru,rt)
        mL=max(br[l] for l in lowers)
        y0=max(rt,mL)
        for mask in range(1,1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1]
            n=len(S)
            sign=F((-1)**(n+1))
            c=[F(0),F(0),F(0)]
            c[rt]+=1
            c[ru]+=1
            for j in S:
                c[br[j]]+=1
            if n==1:
                c1=list(c)
                c1[y0]-=lam0
                gap=ordered_exp_gap_integral(c1,mL,y0) if y0>mL else F(0)
                val=gap/lam0 + ordered_exp_integral(c1)/(lam0**2)
                total += sign*val/(F(1)-p)
            else:
                coeff=sign*F(n,n-1)/(F(1)-p)
                cA=list(c)
                cA[mL]-=F(n-1)
                cA[y0]-=lam0
                cB=list(c)
                cB[y0]-=lam0+F(n-1)
                val=ordered_exp_integral(cA)/lam0 - ordered_exp_integral(cB)/(lam0+F(n-1))
                total += coeff*val
    return total

def exact_max_terms(t,bases,upper,target,lowers):
    aa=F(1)-t
    bb=F(2)-t
    return (
        chain_max_transform(bases,upper,target,lowers,F(0),t-F(1)),
        chain_max_transform(bases,upper,target,lowers,-aa,F(0)),
        chain_max_transform(bases,upper,target,lowers,-bb,F(1)),
    )

def mix_corr_from_T(t,T1,T2,T3):
    aa=F(1)-t
    bb=F(2)-t
    return t/(aa*bb)*(T1-T2)-kappa(t)*(T1-T3)

print("HARD7-03 exact interior mixed-sign max certificate")

theta=F(117261,200000)
a_shape=F(29645831,10000000)
old_L=F(2500000,29648439)

Hloc,M2loc,M1loc,M0loc=local_minimum_correction(theta)
P2=weighted_penalty_complement(theta,{1:{0,1},2:{1}},1,[2])
P10=weighted_penalty_complement(theta,{0:{-1,0,1},1:{0,1},2:{1}},0,[1,2])
P12=weighted_penalty_complement(theta,BASES_ALL,2,[-1,0,1])
P01=weighted_penalty_complement(theta,BASES_ALL,1,[-2,-1,0])
P2_closed=(
    F(1)/((F(1)-theta)*(F(2)-theta)**3)
    + F(2)/(F(2)-theta)**4
)
assert P2==P2_closed
Hbase=Hloc+kappa(theta)*(2*P2+2*(P10+P12)+2*P01)

E1,E2,E3=edge_chain_terms_full(theta)
assert E1>E2>E3>0
edge_corr=mix_corr_from_T(theta,E1,E2,E3)
assert edge_corr>0

# Near-edge strict mixed branch:
# Y_{-1} > Y_0 > max(Y_1,Y_2).
N1,N2,N3=exact_max_terms(
    theta,BASES_ALL,upper=-1,target=0,lowers=[1,2]
)
assert N1>N2>N3>0
near_corr=mix_corr_from_T(theta,N1,N2,N3)
assert near_corr>0

# Central strict mixed branch:
# Y_2 > Y_1 > max(Y_{-2},Y_{-1},Y_0).
C1,C2,C3=exact_max_terms(
    theta,BASES_ALL,upper=2,target=1,lowers=[-2,-1,0]
)
assert C1>C2>C3>0
center_corr=mix_corr_from_T(theta,C1,C2,C3)
assert center_corr>0

# Reflection supplies the second edge, near-edge, and central orientations.
Hnew=Hbase+2*edge_corr+2*near_corr+2*center_corr
U4=(F(3)*A3(theta)-pair_correction(theta)-Hnew)/(F(1)-theta)

x=F(4)*theta*a_shape
S32=sum(x**k/F(factorial(k),1) for k in range(33))
margin=S32-U4
assert margin>0

new_L=F(1)/(F(4)*a_shape)
gain=new_L-old_L
assert new_L==F(2500000,29645831)
assert gain==F(6520000000,878952612007809)
assert gain>0

print(f"theta = {theta}")
print(f"a_shape = {a_shape}")
print(f"Hloc = {Hloc}")
print(f"P2_identity_exact = {P2 == P2_closed}")
print(f"Hbase = {Hbase}")
print(f"edge_T1 = {E1}")
print(f"edge_T2 = {E2}")
print(f"edge_T3 = {E3}")
print(f"edge_corr = {edge_corr}")
print(f"near_T1 = {N1}")
print(f"near_T2 = {N2}")
print(f"near_T3 = {N3}")
print(f"near_corr = {near_corr}")
print(f"center_T1 = {C1}")
print(f"center_T2 = {C2}")
print(f"center_T3 = {C3}")
print(f"center_corr = {center_corr}")
print(f"Hnew = {Hnew}")
print(f"U4 = {U4}")
print(f"x = {x}")
print(f"S32_minus_U4 = {margin}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {gain}")
print(f"Hbase_float = {float(Hbase):.15f}")
print(f"edge_corr_float = {float(edge_corr):.15f}")
print(f"near_corr_float = {float(near_corr):.15f}")
print(f"center_corr_float = {float(center_corr):.15f}")
print(f"Hnew_float = {float(Hnew):.15f}")
print(f"U4_float = {float(U4):.15f}")
print(f"x_float = {float(x):.15f}")
print(f"S32_minus_U4_float = {float(margin):.15e}")
print(f"old_L_float = {float(old_L):.15f}")
print(f"new_L_float = {float(new_L):.15f}")
print(f"metric_gain_float = {float(gain):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")
