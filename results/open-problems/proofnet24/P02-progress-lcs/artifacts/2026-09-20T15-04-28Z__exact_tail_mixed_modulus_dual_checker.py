from fractions import Fraction
from math import gcd

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
M=5_000_000_000_000_000_000
alpha=a%b
h=707_440_146_652_911_839
assert (alpha*h)%b == 1
assert b <= M < 2*b
assert gcd(p,b)==1
binv=pow(b,-1,p)

c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
mult=[2,4,4,4,4,4,4,4]
assert all(c[k]%(p**k)==0 for k in range(8))
assert all((c[k]//(p**k))%p != 0 for k in range(8))
cinv=[pow((c[k]//(p**k))%p,-1,p) for k in range(8)]

Dmm=Fraction(655209040831815247751186134103526570372190622578374697627001555,
             925139970226099634)
D=2*Dmm
assert D>Dmm

def aggregate_W(R,z,m):
    rb=(h*R)%b
    ell=((z-rb)%p)*binv % p
    W=rb+ell*b
    if W <= m*M:
        return W,ell
    return None

def parent_values(s):
    if s==0:
        return [b]
    r=(h*s)%b
    out=[]
    if 1 <= r <= M:
        out.append(r)
    if r+b <= M:
        out.append(r+b)
    return out

def ceil_frac(fr):
    return (fr.numerator + fr.denominator - 1)//fr.denominator

def z_digit(u, priorW, k):
    rem=u-sum(c[j]*priorW[j] for j in range(k))
    assert rem % (p**k)==0
    return ((rem//(p**k))%p)*cinv[k] % p

def Rmax_for_violation(s,V, priorR, k):
    used=a*s + b*sum(c[j]*priorR[j] for j in range(k))
    rem=D*V-used
    if rem <= 0:
        return -1
    return ceil_frac(rem/Fraction(b*c[k],1))-1

CUT=ceil_frac(D*Fraction(M,a))
assert CUT==3550
assert Fraction(a*CUT,M)>=D
assert Fraction(a*(CUT-1),M)<D

states=[]
for s in range(CUT):
    for V in parent_values(s):
        assert (a*V-s)%b==0
        u=(a*V-s)//b
        states.append((s,V,u,[],[]))
assert len(states)==4207

stage_counts=[]
max_budgets=[]
scan_counts=[]
for k in range(7):
    nxt=[]
    maxR=-1
    scans=0
    for s,V,u,Rs,Ws in states:
        Rmax=Rmax_for_violation(s,V,Rs,k)
        if Rmax<0:
            continue
        maxR=max(maxR,Rmax)
        scans += Rmax+1
        z=z_digit(u,Ws,k)
        for R in range(Rmax+1):
            aw=aggregate_W(R,z,mult[k])
            if aw is not None:
                W,ell=aw
                nxt.append((s,V,u,Rs+[R],Ws+[W]))
    states=nxt
    stage_counts.append(len(states))
    max_budgets.append(maxR)
    scan_counts.append(scans)

assert stage_counts == [75,18,4,2,7,61,1163]
assert max_budgets == [11683,29870,58533,134553,377503,861374,2517577]

# Exact-tail closure. After types 0..6 are fixed, the row equation
# u=sum_{k=0}^7 c_k W_k forces W_7 exactly. Any actual row must have an
# integer W_7 in [0,4M]. No surviving relaxed branch has such a W_7.
exact_tail_integer=0
exact_tail_in_range=0
residue_consistent_tail=0
for s,V,u,Rs,Ws in states:
    rem=u-sum(c[k]*Ws[k] for k in range(7))
    if rem % c[7] != 0:
        continue
    exact_tail_integer += 1
    W7=rem//c[7]
    if not (0 <= W7 <= mult[7]*M):
        continue
    exact_tail_in_range += 1
    R7=(alpha*W7)%b
    if (h*R7-W7)%b==0:
        residue_consistent_tail += 1

assert exact_tail_in_range==0
assert residue_consistent_tail==0

print('P02 T02 mixed-modulus exact-tail dual checker')
print('Dmm_num=',Dmm.numerator)
print('Dmm_den=',Dmm.denominator)
print('Dtail_num=',D.numerator)
print('Dtail_den=',D.denominator)
print('CUT=',CUT)
print('parent_cases=',4207)
for k in range(7):
    print(f'type{k}_max_R_budget=',max_budgets[k])
    print(f'type{k}_scan_count=',scan_counts[k])
    print(f'type{k}_aggregate_branches=',stage_counts[k])
print('exact_tail_integer_candidates=',exact_tail_integer)
print('exact_tail_in_range_candidates=',exact_tail_in_range)
print('exact_tail_residue_consistent_candidates=',residue_consistent_tail)
print('D_TAIL_EQ_2_D_MM=PASS')
print('MIXED_MODULUS_PREFIX_FILTER=PASS')
print('EXACT_TYPE7_ROW_EQUALITY_CLOSURE=PASS')
print('GLOBAL_TWO_STEP_DEFECT_D_TAIL=PASS')
print('ALL_EXACT_CHECKS_PASS')
