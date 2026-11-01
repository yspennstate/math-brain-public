from fractions import Fraction

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
M=5_000_000_000_000_000_000
alpha=a%b
h=707_440_146_652_911_839
assert (alpha*h)%b == 1
c=[q**(6-k)*d*p**k for k in range(7)] + [p**7]
c0=c[0]
assert c0 % p != 0
assert all(c[k] % p == 0 for k in range(1,8))
c0inv=pow(c0,-1,p)

# exact candidate from exploratory search
s0=340
V0=4_184_337_266_622_593_636
rchild=99
Vchild=2_509_342_348_533_291_597
assert V0 <= M and Vchild <= M
assert (alpha*V0-s0)%b == 0
assert (alpha*Vchild-rchild)%b == 0
u0=(a*V0-s0)//b
z0=(u0*c0inv)%p
assert Vchild % p == z0
D=Fraction(a*s0+b*c0*rchild,V0)

# Any row with parent slack >= CUT is automatic from a*s/V and V<=M.
CUT=442
assert Fraction(a*CUT,M) > D

def accepted_values_for_slack(s):
    """Possible accepted successor witness values V in [1,M] with s == alpha V mod b."""
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
    if s==0:
        return [b]   # tight parent: V=b because b<=M<2b and gcd(a,b)=1
    return accepted_values_for_slack(s)

parents=[]
RGLOBAL=0
for s in range(CUT):
    for V in parent_values_for_slack(s):
        # exact parent row sum u=(aV-s)/b
        assert (a*V-s)%b == 0
        u=(a*V-s)//b
        z=(u*c0inv)%p
        rem=D*V-a*s
        if rem <= 0:
            req=0
        else:
            # Require b*c0*R >= rem; req is least integer R that guarantees D.
            num=rem.numerator
            den=rem.denominator*b*c0
            req=(num+den-1)//den
        parents.append((s,V,z,req))
        if req>0:
            RGLOBAL=max(RGLOBAL,req-1)
assert RGLOBAL == 1442, RGLOBAL

# Each of the two type-0 labels is either rejected (V=0, slack contribution 0)
# or accepted with some slack r and witness V compatible with the row-slack congruence.
opts=[(0,0)]
for r in range(RGLOBAL+1):
    for V in accepted_values_for_slack(r):
        opts.append((r,V))

# Min total successor slack R=r1+r2 for each type-0 witness-sum residue mod p,
# restricting to potentially violating R<=RGLOBAL.
INF=10**30
minR=[INF]*p
arg=[None]*p
for r1,V1 in opts:
    if r1>RGLOBAL: continue
    for r2,V2 in opts:
        R=r1+r2
        if R>RGLOBAL: continue
        z=(V1+V2)%p
        if R<minR[z]:
            minR[z]=R
            arg[z]=(r1,V1,r2,V2)

best=None
bestdata=None
checked=0
for s,V,z,req in parents:
    checked += 1
    if req==0:
        # a*s/V already certifies the target defect even if type-0 successor slack is zero.
        val=Fraction(a*s,V)
        assert val >= D
        if best is None or val<best:
            best=val;bestdata=(s,V,z,0,None)
        continue
    mr=minR[z]
    if mr==INF:
        # No relaxed two-label configuration exists with R<=RGLOBAL >= req-1,
        # so every actual row has R>=req and is safe.
        continue
    val=Fraction(a*s+b*c0*mr,V)
    assert val >= D, (s,V,z,req,mr,val,D,arg[z])
    if best is None or val<best:
        best=val;bestdata=(s,V,z,mr,arg[z])

# Candidate must be achieved in the relaxation by rejected + (r=99,Vchild).
assert best == D, (best,D,bestdata)
assert bestdata[0] == s0 and bestdata[1] == V0 and bestdata[3] == rchild, bestdata
print('P02 T02 type-0 successor-slack dual checker')
print('alpha=',alpha)
print('h=',h)
print('c0=',c0)
print('c0_mod_p=',c0%p)
print('c0inv_mod_p=',c0inv)
print('CUT_parent_slack=',CUT)
print('RGLOBAL=',RGLOBAL)
print('parent_cases=',len(parents))
print('label_options=',len(opts))
print('checked_parent_cases=',checked)
print('D_type0_num=',D.numerator)
print('D_type0_den=',D.denominator)
print('candidate_parent_s=',s0)
print('candidate_parent_V=',V0)
print('candidate_type0_target=',z0)
print('candidate_child_slack=',rchild)
print('candidate_child_V=',Vchild)
print('relaxed_argmin=',bestdata)
print('TYPE0_DIVISIBILITY_STRUCTURE=PASS')
print('PARENT_SLACK_TRUNCATION=PASS')
print('TWO_TYPE0_LABEL_RELAXED_ENUMERATION=PASS')
print('GLOBAL_TWO_STEP_DEFECT_LOWER_BOUND=PASS')
print('RELAXATION_SHARPNESS_AT_CANDIDATE=PASS')
print('ALL_EXACT_CHECKS_PASS')
