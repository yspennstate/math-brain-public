from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import permutations
from math import factorial

getcontext().prec = 80
D=Decimal
M=23

# Rounded source saddle values from the predecessor diagnostic.
a=D("6.718433003118395")
nu_ps=D("1.2782018")
nu_ns1=D("0.33277280")
nu_ns2=D("0.95336927")
ell_ps=D("5.856668036248987")
ell_ns1=D("0.5364470029682571")
ell_nu=D("3.580001818526844")
Q_safe=D("4.380711108236127")
B_can=D("0.4578196810673468")
J_jge2=D("5.368350697300034e-10")
prev_best_JK=D("1.869587880794033e-7")
source_base=(D(1)+D("1e-7"))*D("0.9999998965")
source_margin=-(source_base.ln())

def dec_pow(x,n):
    y=D(1)
    for _ in range(n): y*=x
    return y

def delta_b(i,j):
    if i<j or j<1: return D(0)
    base=(-D(2)*a).exp()*dec_pow(a,i+j)/(D(factorial(i))*D(factorial(j)))
    return base*(D(2) if i>j else D(1))

def Psi(i,j):
    return dec_pow(nu_ps,i)+dec_pow(nu_ns1+nu_ns2,j)-dec_pow(nu_ns2,j)

def tval(i,j):
    return delta_b(i,j)*dec_pow(nu_ps,i)/Psi(i,j)

def fval(i,j,k):
    from math import comb
    return delta_b(i,j)*D(comb(j,k))*dec_pow(nu_ns1,k)*dec_pow(nu_ns2,j-k)/Psi(i,j)

q=Q_safe/ell_ps
b1=B_can/ell_nu
e=[D(0)]*(M+1)
for k in range(1,M+1):
    e[k]=fval(k,1,1)
tail=[D(0)]*(M+2)
for i in range(M,0,-1):
    tail[i]=tail[i+1]+e[i]
Eall=tail[1]

def neglog1m(x):
    return -(D(1)-x).ln()

J_deg=D(0)
J_iid=D(0)
J_rank=D(0)
rows=[]
for i in range(1,M+1):
    ti=tval(i,1)
    hi=tail[i+1] if i<M else D(0)
    p_deg=dec_pow(q,i)*b1*(hi/ell_ns1)
    p_iid=D("0.5")*dec_pow(q,i)*b1*(Eall/ell_ns1)
    eff=hi+D("0.5")*e[i]
    p_rank=dec_pow(q,i)*b1*(eff/ell_ns1)
    jd=ti*neglog1m(p_deg) if p_deg else D(0)
    ji=ti*neglog1m(p_iid)
    jr=ti*neglog1m(p_rank)
    J_deg+=jd; J_iid+=ji; J_rank+=jr
    rows.append((i,ti,e[i],hi,p_deg,p_iid,p_rank,jd,ji,jr))

J_total=J_rank+J_jge2

# Exact finite toy check of the heterogeneous priority-survival product.
# Two centers: class 1 with one ps copy; class 2 with two ps copies.
# P=4 ps targets, Q=2 safe; U=3 nu targets, first two canonical,
# each canonical nu target maps to ns1 target with the same index.
# L=4 ns1 source ranks: 0 (ineligible), 1, 2, 3.
ps_source=("c1","c2a","c2b","other")
nu_source=("c1","c2","other")
ns_source=(0,1,2,3)
safe_targets={0,1}
canonical_targets={0,1}
canon_to_ns={0:0,1:1}

def h(cls,rank):
    if rank>cls: return Fraction(1,1)
    if rank==cls: return Fraction(1,2)
    return Fraction(0,1)

tot=Fraction(0,1); cnt=0
for psp in permutations(ps_source):
    pos_ps={s:t for t,s in enumerate(psp)}
    S1 = pos_ps["c1"] in safe_targets
    S2 = pos_ps["c2a"] in safe_targets and pos_ps["c2b"] in safe_targets
    for nup in permutations(nu_source):
        pos_nu={s:t for t,s in enumerate(nup)}
        t1=pos_nu["c1"]; t2=pos_nu["c2"]
        N1=t1 in canonical_targets; N2=t2 in canonical_targets
        s1=canon_to_ns[t1] if N1 else None
        s2=canon_to_ns[t2] if N2 else None
        for nsp in permutations(ns_source):
            surv=Fraction(1,1)
            if S1 and N1:
                surv *= 1-h(1,nsp[s1])
            if S2 and N2:
                surv *= 1-h(2,nsp[s2])
            tot += surv
            cnt += 1
toy_exact=tot/Fraction(cnt,1)
a1=Fraction(2,4)
a2=Fraction(2*1,4*3)
bb=Fraction(2,3)
eh1=Fraction(5,8)
eh2=Fraction(3,8)
toy_product=(1-a1*bb*eh1)*(1-a2*bb*eh2)

print("PRIORITY_WEIGHTED_RESCUE_DIAGNOSTIC")
print("ROUNDED_SOURCE_INPUTS_ONLY_NOT_INTERVAL_ENDPOINT")
print(f"q_safe = {q}")
print(f"b1 = {b1}")
print(f"Eall = {Eall}")
print(f"J_deg = {J_deg}")
print(f"J_iid = {J_iid}")
print(f"J_rank_jitter = {J_rank}")
print(f"J_jge2_predecessor = {J_jge2}")
print(f"J_total_joint = {J_total}")
print(f"previous_best_JK = {prev_best_JK}")
print(f"J_rank/previous_best_JK = {J_rank/prev_best_JK}")
print(f"J_total/previous_best_JK = {J_total/prev_best_JK}")
print(f"published_rounded_source_log_margin = {source_margin}")
print(f"J_total/source_margin = {J_total/source_margin}")
print("TOP_RANK_JITTER_TERMS")
for r in sorted(rows,key=lambda x:x[-1],reverse=True)[:10]:
    i,ti,ei,hi,pd,pi,pr,jd,ji,jr=r
    print(f" i={i:2d} Jterm={jr} p_rank={pr} t_i1={ti} e_i={ei} E_gt_i={hi}")
print("EXACT_TOY_CHECK")
print(f"toy_exact_survival = {toy_exact} = {float(toy_exact):.17g}")
print(f"toy_product_bound = {toy_product} = {float(toy_product):.17g}")
print(f"toy_inequality_holds = {toy_exact <= toy_product}")
assert toy_exact <= toy_product
assert J_rank > J_deg
assert J_rank > J_iid
assert J_rank > prev_best_JK
assert J_total > J_rank
print("ALL_CHECKS_PASS = True")
