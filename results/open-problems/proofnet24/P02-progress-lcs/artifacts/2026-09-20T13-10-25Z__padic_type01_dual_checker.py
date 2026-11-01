from fractions import Fraction
from decimal import Decimal, getcontext

# Frozen primitive C045 data.
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
assert __import__('math').gcd(p,q)==1 and __import__('math').gcd(p,d)==1

c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
assert all(c[k] % (p**k) == 0 for k in range(8))
assert all((c[k]//(p**k)) % p != 0 for k in range(7))
c0,c1=c[0],c[1]
c0inv=pow(c0,-1,p)
c1div=c1//p
c1divinv=pow(c1div,-1,p)

# Previous durable P02 two-step defect (10:03 matched-successor report).
c7=c[7]
vstar=h+b
D_floor=a//vstar
D_prev=Fraction(D_floor+1500*c7+1,1)

# New target: the first nonexceptional parent-only ratio after the type-0 relaxation.
s_star=97
V_star=1_094_462_055_227_467_919
assert (alpha*V_star-s_star)%b == 0
D=Fraction(a*s_star,V_star)
assert D > D_prev

def accepted_values_for_slack(s):
    """Possible positive witness values V<=M with s == alpha*V (mod b)."""
    if s==0:
        return [b]
    r=(h*s)%b
    vals=[]
    if 1 <= r <= M:
        vals.append(r)
    if r+b <= M:
        vals.append(r+b)
    return vals

def parent_values_for_slack(s):
    return [b] if s==0 else accepted_values_for_slack(s)

def ceil_fraction(x):
    return (x.numerator+x.denominator-1)//x.denominator

# Parent slacks above CUT are certified directly by a*s/V and V<=M.
CUT=444
assert Fraction(a*CUT,M) > D
assert Fraction(a*(CUT-1),M) < D

parents=[]
RGLOBAL=0
for s in range(CUT):
    for V in parent_values_for_slack(s):
        assert (a*V-s)%b == 0
        u=(a*V-s)//b
        z=(u*c0inv)%p
        rem=D*V-a*s
        if rem <= 0:
            req0=0
        else:
            req0=ceil_fraction(rem/Fraction(b*c0,1))
            RGLOBAL=max(RGLOBAL,req0-1)
        parents.append((s,V,u,z,req0))
assert RGLOBAL == 1446

# Type-0 labels: exactly two. Rejected label contributes (slack,witness)=(0,0).
# Accepted label with child slack r has one or two exact possible witness values.
opts0=[(0,0)]
for r in range(RGLOBAL+1):
    for V in accepted_values_for_slack(r):
        opts0.append((r,V))

INF=10**30
minR0=[INF]*p
arg0=[None]*p
pair_tests=0
for r1,V1 in opts0:
    if r1>RGLOBAL: continue
    for r2,V2 in opts0:
        R=r1+r2
        if R>RGLOBAL: continue
        pair_tests += 1
        z=(V1+V2)%p
        if R<minR0[z]:
            minR0[z]=R
            arg0[z]=(r1,V1,r2,V2)

safe_parent=0
safe_type0=0
exceptions=[]
for s,V,u,z,req0 in parents:
    if req0==0:
        assert Fraction(a*s,V) >= D
        safe_parent += 1
        continue
    mr=minR0[z]
    if mr==INF or mr>=req0:
        safe_type0 += 1
        continue
    exceptions.append((s,V,u,z,req0,mr,arg0[z]))

assert safe_parent == 270
assert safe_type0 == 256
assert len(exceptions)==1
s0,V0,u0,z0,req0,mr0,argmin0=exceptions[0]
assert (s0,V0,z0,req0,mr0)==(340,4_184_337_266_622_593_636,219977,103,99)

# Enumerate every type-0 configuration that could still violate D for the unique parent.
# This avoids assuming uniqueness of the minimum-residue representative.
potential0=[]
for r1,V1 in opts0:
    if r1>=req0: continue
    for r2,V2 in opts0:
        R0=r1+r2
        if R0>=req0: continue
        if (V1+V2)%p != z0: continue
        potential0.append((r1,V1,r2,V2,R0,V1+V2))
assert len(potential0)==68
assert {x[4] for x in potential0}=={99}
assert len({x[5] for x in potential0})==1
W0=potential0[0][5]
assert W0==2_509_342_348_533_291_597

# One more p-adic digit.  Since c_k is divisible by p^k, after removing c0*W0
# and dividing by p, all types k>=2 vanish mod p, while c1/p is invertible mod p.
assert (u0-c0*W0)%p == 0
rhs1=((u0-c0*W0)//p)%p
z1=(rhs1*c1divinv)%p
assert z1==218062

# Determine exactly how much type-1 successor slack could be afforded by a violating row.
# Type-0 total slack is fixed at R0=99 over every potential type-0 configuration.
base_defect=Fraction(a*s0+b*c0*99,V0)
assert base_defect < D
rem1=D*V0-(a*s0+b*c0*99)
req1=ceil_fraction(rem1/Fraction(b*c1,1))
# Violation would require R1 <= req1-1.
assert req1-1==10
R1MAX=req1-1

# Type-1 has exactly four labels.  Enumerate rejected/accepted label states with total slack <=10.
opts1=[(0,0)]
for r in range(R1MAX+1):
    for V in accepted_values_for_slack(r):
        opts1.append((r,V))

states={(0,0)}
state_counts=[len(states)]
for _ in range(4):
    nxt=set()
    for R,Wmod in states:
        for r,V in opts1:
            if R+r<=R1MAX:
                nxt.add((R+r,(Wmod+V)%p))
    states=nxt
    state_counts.append(len(states))
hits=sorted((R,w) for R,w in states if w==z1)
assert state_counts==[1,15,28,41,54]
assert hits==[]

# Hence every actual row has normalized two-step defect >= D.
# The exact identity is a^2 V_i-b^2(B^2 V)_i = a*s_i+b*(Bs)_i.
# Convert to a strict rational spectral majorant.
R=Fraction(a,b)
beta=R-D/Fraction(2*a*b,1)
beta_prev=R-D_prev/Fraction(2*a*b,1)
assert beta < beta_prev
assert beta*beta > R*R-D/Fraction(b*b,1)

t=Fraction(p,q)
S=q**6*d
scale=t*t/S
lambda_new=scale*beta
lambda_prev=scale*beta_prev
base=4*t*t
assert 0 < base < 1
assert 0 < lambda_new < lambda_prev < 1

# Exact logarithm enclosure through the positive atanh series with rigorous tail.
def neglog_bounds(z,K=400):
    assert 0 < z < 1
    u=(1-z)/(1+z)
    u2=u*u
    pw=u
    sm=Fraction(0,1)
    for k in range(K):
        sm += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail=2*pw/Fraction(2*K+1,1)/(1-u2)
    return sm,sm+tail

Alo,Ahi=neglog_bounds(base)
Nlo,Nhi=neglog_bounds(lambda_new)
Olo,Ohi=neglog_bounds(lambda_prev)
Unew_lo=Alo/Nhi
Unew_hi=Ahi/Nlo
Uprev_lo=Alo/Ohi
Uprev_hi=Ahi/Olo
assert Unew_hi < Uprev_lo
L=Fraction(99083249,125000000)
assert L < Unew_lo

getcontext().prec=150
def decf(x): return Decimal(x.numerator)/Decimal(x.denominator)
Ud=decf(base).ln()/decf(lambda_new).ln()
Upd=decf(base).ln()/decf(lambda_prev).ln()

sep=None
for digits in range(60,121):
    ten=10**digits
    k=(Unew_hi.numerator*ten)//Unew_hi.denominator+1
    Q=Fraction(k,ten)
    if Unew_hi < Q < Uprev_lo:
        sep=(digits,k,ten,Q)
        break
assert sep is not None

print('P02 T02 p-adic type0+type1 successor dual checker')
print('alpha=',alpha)
print('h=',h)
print('coefficients=',c)
print('D_prev=',D_prev.numerator)
print('D_new_num=',D.numerator)
print('D_new_den=',D.denominator)
print('D_ratio_diag=',decf(D/D_prev))
print('CUT=',CUT)
print('parent_cases=',len(parents))
print('RGLOBAL_type0=',RGLOBAL)
print('type0_label_options=',len(opts0))
print('type0_pair_tests=',pair_tests)
print('safe_parent_only=',safe_parent)
print('safe_after_type0=',safe_type0)
print('exception_parent_s=',s0)
print('exception_parent_V=',V0)
print('exception_type0_residue=',z0)
print('exception_type0_req=',req0)
print('exception_type0_minR=',mr0)
print('potentially_violating_type0_configs=',len(potential0))
print('exception_type0_W0=',W0)
print('forced_type1_residue=',z1)
print('violation_requires_R1_le=',R1MAX)
print('type1_label_options=',len(opts1))
print('type1_reachable_state_counts=',state_counts)
print('type1_target_hits=',len(hits))
print('diag_U_new=',Ud)
print('diag_U_prev=',Upd)
print('diag_source_decrease=',Upd-Ud)
print('separator_digits=',sep[0])
print('separator_num=',sep[1])
print('separator_den=',sep[2])
print('separator_decimal=',format(Decimal(sep[1])/(Decimal(10)**sep[0]),'f'))
print('TYPE0_MOD_P_GLOBAL_REDUCTION=PASS')
print('UNIQUE_TYPE0_EXCEPTION=PASS')
print('TYPE1_MOD_P2_OBSTRUCTION=PASS')
print('GLOBAL_TWO_STEP_DEFECT_D_NEW=PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS')
print('EXACT_LOG_INTERVALS_DISJOINT=PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS')
print('ALL_EXACT_CHECKS_PASS')
