from fractions import Fraction as F
from itertools import permutations, combinations
from math import factorial
import math

A_VARS=(-1,0,1)
BASES_ALL={-2:{-1},-1:{-1,0},0:{-1,0,1},1:{0,1},2:{1}}

def A3(t):
    return F(2)*(F(2268)-F(4408)*t+F(3748)*t**2-F(1918)*t**3+F(652)*t**4-F(143)*t**5+F(18)*t**6-t**7)/((F(3)-t)**4*(F(2)-t)**3*(F(1)-t)**3)
def M2(z,t):
    z=abs(z)
    if z==2:return F(1)/(F(1)-t)**2
    if z==1:return F(2)/((F(1)-t)**2*(F(2)-t))
    if z==0:return F(6)/((F(1)-t)**2*(F(2)-t)*(F(3)-t))
def pair_correction_old(t): return F(8)/(F(2)-t)*(M2(0,t)+M2(1,t)+M2(2,t))
def kappa(t): return t/((F(2)-t)*(F(3)-t))
def ordered_exp_integral(c):
    c1,c2,c3=c
    rates=[F(3)-(c1+c2+c3),F(2)-(c2+c3),F(1)-c3]
    assert all(r>0 for r in rates),(c,rates)
    return F(1)/(rates[0]*rates[1]*rates[2])
def ordered_exp_gap_integral(c,lo,hi):
    c1,c2,c3=c
    rates=[F(3)-(c1+c2+c3),F(2)-(c2+c3),F(1)-c3]
    assert 0<=lo<hi<=2 and all(r>0 for r in rates)
    base=F(1)/(rates[0]*rates[1]*rates[2])
    return base*sum(F(1,rates[j]) for j in range(lo+1,hi+1))
def ordered_exp_gap2_integral(c,lo,hi):
    c1,c2,c3=c
    rates=[F(3)-(c1+c2+c3),F(2)-(c2+c3),F(1)-c3]
    assert 0<=lo<hi<=2 and all(r>0 for r in rates)
    base=F(1)/(rates[0]*rates[1]*rates[2])
    inv=[F(1,rates[j]) for j in range(lo+1,hi+1)]
    return base*(sum(inv)**2+sum(x*x for x in inv))
def weighted_target_max(t,bases,target):
    labels=list(bases); comps=[j for j in labels if j!=target]; total=F(0)
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        br={j:max(rank[v] for v in S) for j,S in bases.items()}; M=max(br.values())
        for mask in range(1<<len(comps)):
            S=[comps[k] for k in range(len(comps)) if (mask>>k)&1]
            q=F(1)-t+len(S); c=[F(0)]*3; c[br[target]]+=1
            for j in S:c[br[j]]+=1
            c[M]-=q
            term=ordered_exp_integral(c)/q
            total += -term if len(S)%2 else term
    return total
def interval_integral(c,q,Lrank,Urank=None):
    if Urank is not None and Urank<=Lrank:return F(0)
    cL=list(c);cL[Lrank]-=q;ans=ordered_exp_integral(cL)/q
    if Urank is not None:
        cU=list(c);cU[Urank]-=q;ans-=ordered_exp_integral(cU)/q
    return ans
def weighted_chain(t,bases,upper,target,lowers):
    total=F(0)
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        br={j:max(rank[v] for v in S) for j,S in bases.items()}
        Lrank=max([br[target]]+[br[l] for l in lowers]);Urank=br[upper]
        for mask in range(1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1];sign=-1 if len(S)%2 else 1
            c=[F(0)]*3;c[br[target]]+=1
            for l in S:c[br[l]]+=1
            q1=F(1)-t+len(S);total+=sign*interval_integral(c,q1,Lrank,Urank)
            c2=list(c);c2[Urank]+=1;q2=q1+1
            total+=sign*interval_integral(c2,q2,max(Lrank,Urank),None)
    return total
def local_minimum_correction(t):
    M2loc=weighted_target_max(t,{2:{1},1:{0,1}},2)
    M1target=weighted_target_max(t,{0:{-1,0,1},1:{0,1},2:{1}},1)
    M1chain=weighted_chain(t,BASES_ALL,-1,2,[0,1])
    M1loc=M1target+M1chain
    M0target=weighted_target_max(t,{-1:{-1,0},0:{-1,0,1},1:{0,1}},0)
    M0chain=weighted_chain(t,BASES_ALL,2,-1,[0,1])
    M0loc=M0target+2*M0chain
    return kappa(t)*(2*M2loc+2*M1loc+M0loc)
def weighted_penalty_complement(t,bases,target,lowers):
    r=F(2)-t;total=F(0);lowers=list(lowers)
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        br={j:max(rank[v] for v in S) for j,S in bases.items()}
        rt=br[target];m=max(br[l] for l in lowers)
        for mask in range(1,1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1];n=len(S)
            coeff=F(((-1)**(n+1))*n);c=[F(0)]*3
            for l in S:c[br[l]]+=1
            if rt<=m:
                q=F(n)+F(1)-t;c2=list(c);c2[rt]+=1;c2[m]-=q
                total+=coeff/r/q*ordered_exp_integral(c2)
            else:
                if n==1:
                    cm=list(c);cm[rt]+=t-F(1)
                    total+=coeff/r*ordered_exp_gap_integral(cm,m,rt)
                else:
                    qm=F(n-1);cA=list(c);cA[rt]+=t-F(1);cA[m]-=qm
                    cB=list(c);cB[rt]+=t-F(n)
                    total+=coeff/r/qm*(ordered_exp_integral(cA)-ordered_exp_integral(cB))
                q=F(n)+F(1)-t;cU=list(c);cU[rt]+=F(1)-q
                total+=coeff/r/q*ordered_exp_integral(cU)
    return total
def edge_chain_terms_full(t):
    aa=F(1)-t;bb=F(2)-t;cc=F(3)-t;T1=T2=T3=F(0)
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        r0=max(rank[v] for v in {-1,0,1});r1=max(rank[v] for v in {0,1});r2=rank[1]
        c=[F(0)]*3;c[r2]+=1;c[r1]-=aa
        q=F(0)
        if r1>r2:q+=ordered_exp_gap_integral(c,r2,r1)/bb
        q+=ordered_exp_integral(c)/bb**2
        c2=[F(0)]*3;c2[r1]+=1;c2[r2]+=1;c2[r0]-=bb
        if r0>r2:q+=ordered_exp_gap_integral(c2,r2,r0)*(F(1,cc)-F(1,bb))
        q+=ordered_exp_integral(c2)*(F(1,cc**2)-F(1,bb**2));T1+=q
        c3=[F(0)]*3;c3[r2]+=1;c3[r0]-=aa;q=F(0)
        if r1>r2:q+=ordered_exp_gap_integral(c3,r2,r1)/bb
        q+=ordered_exp_integral(c3)/bb
        if r0>r2:q+=ordered_exp_gap_integral(c2,r2,r0)/bb*(F(-1)+F(1,cc))
        q+=ordered_exp_integral(c2)/bb*(F(-1)+F(1,cc**2));T2+=q
        base=ordered_exp_integral(c2);s1=ordered_exp_gap_integral(c2,r2,r0) if r0>r2 else F(0)
        s2=ordered_exp_gap2_integral(c2,r2,r0) if r0>r2 else F(0)
        d2=ordered_exp_gap2_integral(c2,r2,r1) if r1>r2 else F(0)
        T3+=F(1,2)*((s2-d2)/cc+2*s1/cc**2+2*base/cc**3)
    return T1,T2,T3
def chain_max_transform(bases,upper,target,lowers,p,q):
    lowers=list(lowers);total=F(0);lam=F(2)-p-q
    assert F(1)-p>0 and lam>0
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        br={j:max(rank[v] for v in S) for j,S in bases.items()}
        ru,rt=br[upper],br[target];assert ru<=rt
        m=max(br[l] for l in lowers);y0=max(rt,m)
        for mask in range(1,1<<len(lowers)):
            S=[lowers[k] for k in range(len(lowers)) if (mask>>k)&1];n=len(S);sg=F((-1)**(n+1))
            c=[F(0)]*3;c[rt]+=1;c[ru]+=1
            for j in S:c[br[j]]+=1
            if n==1:
                c1=list(c);c1[y0]-=lam
                gap=ordered_exp_gap_integral(c1,m,y0) if y0>m else F(0)
                total+=sg*(gap/lam+ordered_exp_integral(c1)/lam**2)/(F(1)-p)
            else:
                coeff=sg*F(n,n-1)/(F(1)-p)
                cA=list(c);cA[m]-=F(n-1);cA[y0]-=lam
                cB=list(c);cB[y0]-=lam+F(n-1)
                total+=coeff*(ordered_exp_integral(cA)/lam-ordered_exp_integral(cB)/(lam+F(n-1)))
    return total
def exact_max_terms(t,bases,upper,target,lowers):
    aa=F(1)-t;bb=F(2)-t
    return (chain_max_transform(bases,upper,target,lowers,F(0),t-F(1)),
            chain_max_transform(bases,upper,target,lowers,-aa,F(0)),
            chain_max_transform(bases,upper,target,lowers,-bb,F(1)))
def mix_corr_from_T(t,T1,T2,T3):
    aa=F(1)-t;bb=F(2)-t
    return t/(aa*bb)*(T1-T2)-kappa(t)*(T1-T3)
def Hnew_all(t):
    Hloc=local_minimum_correction(t)
    P2=weighted_penalty_complement(t,{1:{0,1},2:{1}},1,[2])
    P10=weighted_penalty_complement(t,{0:{-1,0,1},1:{0,1},2:{1}},0,[1,2])
    P12=weighted_penalty_complement(t,BASES_ALL,2,[-1,0,1])
    P01=weighted_penalty_complement(t,BASES_ALL,1,[-2,-1,0])
    assert P2==F(1)/((F(1)-t)*(F(2)-t)**3)+F(2)/(F(2)-t)**4
    Hbase=Hloc+kappa(t)*(2*P2+2*(P10+P12)+2*P01)
    E=edge_chain_terms_full(t);N=exact_max_terms(t,BASES_ALL,-1,0,[1,2]);C=exact_max_terms(t,BASES_ALL,2,1,[-2,-1,0])
    ce=mix_corr_from_T(t,*E);cn=mix_corr_from_T(t,*N);cc=mix_corr_from_T(t,*C)
    assert ce>0 and cn>0 and cc>0
    return Hbase+2*(ce+cn+cc),(Hbase,ce,cn,cc)

def common_window_mgf(t, labels):
    total=F(0);labels=list(labels)
    for perm in permutations(A_VARS):
        rank={v:i for i,v in enumerate(perm)}
        br={j:max(rank[v] for v in BASES_ALL[j]) for j in labels};m=max(br.values())
        c=[F(0)]*3;c[m]+=t;total+=ordered_exp_integral(c)
        for r in range(1,len(labels)+1):
            for S in combinations(labels,r):
                c=[F(0)]*3
                for j in S:c[br[j]]+=1
                c[m]-=F(r)-t
                total+=t*F((-1)**(r+1))/(F(r)-t)*ordered_exp_integral(c)
    return total
def Jedge(t):return F(1)/(F(1)-t)**2
def Jouter(t):return (F(8)-5*t)/((F(2)-t)**3*(F(1)-t)**2)
def Jinner(t):return F(2)*(F(12)-7*t)/((F(3)-t)*(F(2)-t)**3*(F(1)-t)**2)
def pair_common(t):
    je=common_window_mgf(t,[-2]);jo=common_window_mgf(t,[-2,-1]);ji=common_window_mgf(t,[-1,0])
    assert je==Jedge(t)
    assert jo==Jouter(t)
    assert ji==Jinner(t)
    return F(8)/(F(2)-t)*(je+jo+ji),(je,jo,ji)

theta=F(723,1250)
a_shape=F(2932597567,1000000000)
old_L=F(2500000,29645831)

Hnew,parts=Hnew_all(theta)
Hbase,edge_corr,near_corr,center_corr=parts
C_common,js=pair_common(theta)
J_edge,J_outer,J_inner=js
C_old=pair_correction_old(theta)

assert J_edge==M2(2,theta)
assert J_outer>M2(1,theta)
assert J_inner>M2(0,theta)
assert C_common>C_old

U4_common=(F(3)*A3(theta)-C_common-Hnew)/(F(1)-theta)
U4_oldpair=(F(3)*A3(theta)-C_old-Hnew)/(F(1)-theta)
assert U4_common<U4_oldpair

old_G=F(29645831,10000000)
assert a_shape<old_G

x=F(4)*theta*a_shape
S32=sum(x**k/F(factorial(k),1) for k in range(33))
margin=S32-U4_common
assert margin>0

new_L=F(1)/(F(4)*a_shape)
gain=new_L-old_L
assert new_L==F(250000000,2932597567)
assert gain>0

print("HARD7-03 exact common-overlap pair correction certificate")
print(f"theta = {theta}")
print(f"a_shape = {a_shape}")
print(f"J_edge = {J_edge}")
print(f"J_outer = {J_outer}")
print(f"J_inner = {J_inner}")
print(f"J_edge_equals_old_edge = {J_edge==M2(2,theta)}")
print(f"J_outer_minus_old_outer = {J_outer-M2(1,theta)}")
print(f"J_inner_minus_old_inner = {J_inner-M2(0,theta)}")
print(f"pair_correction_old = {C_old}")
print(f"pair_correction_common = {C_common}")
print(f"pair_correction_gain = {C_common-C_old}")
print(f"Hbase = {Hbase}")
print(f"edge_corr = {edge_corr}")
print(f"near_corr = {near_corr}")
print(f"center_corr = {center_corr}")
print(f"Hnew = {Hnew}")
print(f"U4_oldpair_same_theta = {U4_oldpair}")
print(f"U4_common = {U4_common}")
print(f"old_G_upper = {old_G}")
print(f"new_G_upper = {a_shape}")
print(f"x = {x}")
print(f"S32_minus_U4_common = {margin}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {gain}")
print(f"J_edge_float = {float(J_edge):.15f}")
print(f"J_outer_float = {float(J_outer):.15f}")
print(f"J_inner_float = {float(J_inner):.15f}")
print(f"pair_correction_old_float = {float(C_old):.15f}")
print(f"pair_correction_common_float = {float(C_common):.15f}")
print(f"pair_correction_gain_float = {float(C_common-C_old):.15f}")
print(f"Hnew_float = {float(Hnew):.15f}")
print(f"U4_common_float = {float(U4_common):.15f}")
print(f"old_G_upper_float = {float(old_G):.15f}")
print(f"new_G_upper_float = {float(a_shape):.15f}")
print(f"S32_minus_U4_common_float = {float(margin):.15e}")
print(f"old_L_float = {float(old_L):.15f}")
print(f"new_L_float = {float(new_L):.15f}")
print(f"metric_gain_float = {float(gain):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")