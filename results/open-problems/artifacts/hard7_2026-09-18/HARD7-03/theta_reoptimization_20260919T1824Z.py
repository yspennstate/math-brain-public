from fractions import Fraction as F
from itertools import permutations, combinations
from math import factorial

# HARD7-03 exact parameter-uniform all-pair envelope and theta-reoptimization certificate.
# Reconstructs the 17:21Z exact all-pair value at the inherited theta,
# then evaluates the same proved rational formulas at a new rational theta
# and certifies the improved Chernoff/plateau rational using only exact arithmetic.

A_VARS=(-1,0,1)
BASES_ALL={-2:{-1},-1:{-1,0},0:{-1,0,1},1:{0,1},2:{1}}
U=(F(1),F(0),F(0))
V=(F(0),F(1),F(0))
W=(F(0),F(0),F(1))
ORDERED=(U, tuple(U[i]+V[i] for i in range(3)), tuple(U[i]+V[i]+W[i] for i in range(3)))
LOW=(F(1),F(0),F(0))
MID=(F(1),F(1),F(0))
HIGH=(F(1),F(1),F(1))
ORDER_VECS=(LOW,MID,HIGH)

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
    E=edge_chain_terms_full(t)
    N=exact_max_terms(t,BASES_ALL,-1,0,[1,2])
    C=exact_max_terms(t,BASES_ALL,2,1,[-2,-1,0])
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
    assert je==Jedge(t); assert jo==Jouter(t); assert ji==Jinner(t)
    return F(8)/(F(2)-t)*(je+jo+ji),(je,jo,ji)

def vadd(*vs):
    return tuple(sum((v[i] for v in vs),F(0)) for i in range(3))

def vsub(v,w): return tuple(v[i]-w[i] for i in range(3))

def vscale(c,v): return tuple(c*x for x in v)

def integ_density_exp(L,w_power=0):
    rates=[-x for x in L]
    assert all(r>0 for r in rates),(L,rates)
    if w_power==0:return F(1)/(rates[0]*rates[1]*rates[2])
    assert w_power==1
    return F(1)/(rates[0]*rates[1]*rates[2]**2)

def near_transform(t):
    q=F(1)-t; a=F(2)-t; b=F(3)-t
    c0=F(1)/q-q/(a*a); c1=F(2)*q/(a*b)
    total=F(0)
    for order in permutations(range(3)):
        vals=[None]*3
        for rank,varidx in enumerate(order): vals[varidx]=ORDERED[rank]
        x,y,z=vals
        rank={var:order.index(var) for var in range(3)}
        m=x if rank[0]>rank[1] else y
        d=vsub(y,x) if rank[1]>rank[0] else (F(0),F(0),F(0))
        D=vsub(z,m) if rank[2]>max(rank[0],rank[1]) else (F(0),F(0),F(0))
        density_sum=vadd(x,y,z)
        base=vadd(vscale(t,m),vscale(F(-1),density_sum),vscale(-q,D))
        val=c0*integ_density_exp(base)
        if D!=(F(0),F(0),F(0)):
            assert D==W
            val+=F(1)/a*integ_density_exp(base,1)
        base_d=vadd(base,vscale(F(-1),d))
        val+=(c0-F(2)/a)*integ_density_exp(base_d)
        if D!=(F(0),F(0),F(0)):val+=F(1)/a*integ_density_exp(base_d,1)
        base3=vadd(vscale(t,m),vscale(F(-1),density_sum),vscale(F(-1),d),vscale(-a,D))
        val+=c1*integ_density_exp(base3)
        assert val>0
        total+=val
    return total

def subsets(items):
    for k in range(len(items)+1):
        for S in combinations(items,k): yield S

def cone_integral_density(coef, exponent):
    rates=(F(3)-exponent[0],F(2)-exponent[1],F(1)-exponent[2])
    assert all(r>0 for r in rates),(rates,exponent)
    return coef/(rates[0]*rates[1]*rates[2])

def W_terms_t(t,i,shifts,universe):
    q=F(1)-t; sD=shifts["D"]; others=[j for j in universe if j!=i]; out=[]
    for S in subsets(others):
        k=len(S);coef=F((-1)**k)/(q+k)
        exponent=vadd(shifts[i],*(shifts[j] for j in S),vscale(-(q+k),sD))
        out.append((coef,exponent))
    return out

def R_terms_t(t,i,shifts,universe):
    q=F(1)-t;sD=shifts["D"];others=[j for j in universe if j!=i];out=[]
    for S in subsets(others):
        k=len(S);coef=q*F((-1)**k)/(q+k)
        exponent=vadd(*(shifts[j] for j in S),vscale(-(q+k),sD))
        out.append((coef,exponent))
    return out

def center_exact(t):
    a=F(2)-t
    outer_coef=(F(4)-t)/(a*a)
    labels=("Am","A0","A1"); universe=("X","Z","C","D")
    P=Q=F(0)
    for perm in permutations(labels):
        rank={lab:r for r,lab in enumerate(perm)}
        avec={perm[r]:ORDER_VECS[r] for r in range(3)}
        sX=avec["Am"]; sC=avec["Am"] if rank["Am"]>rank["A0"] else avec["A0"]
        sD=HIGH; sZ=avec["A0"] if rank["A0"]>rank["A1"] else avec["A1"]
        shifts={"X":sX,"C":sC,"D":sD,"Z":sZ}
        Pt=[]
        for i in ("C","D"):
            for coef,exponent in W_terms_t(t,i,shifts,universe):
                Pt.append((F(2)/a*coef,exponent))
        for i in ("X","Z"):
            for coef,exponent in R_terms_t(t,i,shifts,universe):
                Pt.append((outer_coef*coef,vadd(shifts[i],exponent)))
        Qt=[]
        for i in ("C","D"):
            for coef,exponent in W_terms_t(t,i,shifts,("C","D")):
                Qt.append((F(2)/a*coef,exponent))
        P+=sum((cone_integral_density(c,e) for c,e in Pt),F(0))
        Q+=sum((cone_integral_density(c,e) for c,e in Qt),F(0))
    return P,Q,P-Q

def U4_allpairs(t, details=False):
    assert F(0)<t<F(1)
    q=F(1)-t;a=F(2)-t
    C_common,js=pair_common(t)
    Hnew,parts=Hnew_all(t)
    Uc=(F(3)*A3(t)-C_common-Hnew)/q
    E_edge=(F(5)*t*t-F(14)*t+F(10))/(a**4*q**2)
    E_near=near_transform(t)
    J_edge,J_out,J_in=js
    P_edge=(J_edge-t/a*E_edge)/q;P_near=(J_out-t/a*E_near)/q
    Q_edge=F(2)/a*J_edge;Q_near=F(2)/a*J_out
    Pc,Qc,dc=center_exact(t)
    delta_pair=F(4)*((P_edge-Q_edge)+(P_near-Q_near)+dc)
    Unew=Uc-delta_pair/q
    if details:return Unew, dict(U_common=Uc,Hnew=Hnew,C_common=C_common,E_edge=E_edge,E_near=E_near,
                                 P_edge=P_edge,Q_edge=Q_edge,P_near=P_near,Q_near=Q_near,
                                 P_center=Pc,Q_center=Qc,delta_center=dc,delta_pair=delta_pair,parts=parts)
    return Unew

if __name__ == "__main__":
    theta_old=F(723,1250)
    U_old_expected=F(
        21591569424418754612288415153750985225648747506850585937500000,
        25076909157153837194356898290721189577238989596959847067723,
    )
    U_old_rebuilt, old_details=U4_allpairs(theta_old,True)
    assert U_old_rebuilt == U_old_expected

    theta=F(57343,100000)
    U_new, details=U4_allpairs(theta,True)
    q=F(1)-theta
    assert U_new > 0
    assert details["P_edge"] > details["Q_edge"]
    assert details["P_near"] > details["Q_near"]
    assert details["delta_center"] > 0
    assert details["delta_pair"] > 0

    A_old=F(29210369,10000000)
    L_old=F(2500000,29210369)
    assert L_old == F(1)/(F(4)*A_old)

    A_new=F(36511391,12500000)
    assert A_new == F(292091128,100000000)
    assert A_new < A_old
    x=F(4)*theta*A_new
    S32=sum(x**k/F(factorial(k)) for k in range(33))
    margin=S32-U_new
    assert margin > 0

    L_new=F(1)/(F(4)*A_new)
    assert L_new == F(3125000,36511391)
    assert L_new > L_old

    assert U_new < S32
    print("HARD7-03 parameter-uniform exact-pair theta-reoptimization certificate")
    print(f"theta_old = {theta_old}")
    print(f"U_old_rebuilt = {U_old_rebuilt}")
    print(f"U_old_matches_1721Z = {U_old_rebuilt == U_old_expected}")
    print(f"theta_new = {theta}")
    print(f"U_common_new = {details['U_common']}")
    print(f"edge_pair_gain_new = {details['P_edge']-details['Q_edge']}")
    print(f"near_pair_gain_new = {details['P_near']-details['Q_near']}")
    print(f"center_pair_gain_new = {details['delta_center']}")
    print(f"total_pair_subtraction_gain_new = {details['delta_pair']}")
    print(f"U_new = {U_new}")
    print(f"A_old = {A_old}")
    print(f"A_new = {A_new}")
    print(f"x = {x}")
    print(f"S32_minus_U_new = {margin}")
    print(f"L_old = {L_old}")
    print(f"L_new = {L_new}")
    print(f"metric_gain = {L_new-L_old}")
    print(f"U_old_float = {float(U_old_rebuilt):.15f}")
    print(f"U_new_float = {float(U_new):.15f}")
    print(f"A_old_float = {float(A_old):.15f}")
    print(f"A_new_float = {float(A_new):.15f}")
    print(f"S32_minus_U_new_float = {float(margin):.15e}")
    print(f"L_old_float = {float(L_old):.15f}")
    print(f"L_new_float = {float(L_new):.15f}")
    print(f"metric_gain_float = {float(L_new-L_old):.15e}")
    print("ALL_EXACT_CHECKS_PASS = True")
