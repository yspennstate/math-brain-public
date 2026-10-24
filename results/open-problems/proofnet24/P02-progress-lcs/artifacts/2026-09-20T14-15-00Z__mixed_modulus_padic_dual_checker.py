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

D01=Fraction(97*a,1_094_462_055_227_467_919)
s_target=110
V_target=1_850_279_940_452_199_268
R0_target=1815
assert (alpha*V_target-s_target)%b==0
D=Fraction(a*s_target+b*c[0]*R0_target,V_target)
assert D > 4*D01

def aggregate_W(R,z,m):
    rb=(h*R)%b
    k=((z-rb)%p)*binv % p
    W=rb+k*b
    if W <= m*M:
        return W,k
    return None

def parent_values(s):
    if s==0:
        return [b]
    r=(h*s)%b
    out=[]
    if 1 <= r <= M: out.append(r)
    if r+b <= M: out.append(r+b)
    return out

def ceil_frac(fr):
    return (fr.numerator + fr.denominator - 1)//fr.denominator

CUT=ceil_frac(D*Fraction(M,a))
assert CUT==1775
assert Fraction(a*CUT,M) >= D
assert Fraction(a*(CUT-1),M) < D

parents=[]
for s in range(CUT):
    for V in parent_values(s):
        assert (a*V-s)%b==0
        u=(a*V-s)//b
        parents.append((s,V,u))
assert len(parents)==2105

def z_digit(u, priorW, k):
    rem=u-sum(c[j]*priorW[j] for j in range(k))
    assert rem % (p**k)==0
    return ((rem//(p**k))%p)*cinv[k] % p

def Rmax_for_violation(s,V, priorR, k):
    used=a*s + b*sum(c[j]*priorR[j] for j in range(k))
    rem=D*V-used
    if rem <= 0:
        return -1
    req=ceil_frac(rem/Fraction(b*c[k],1))
    return req-1

branches0=[]
maxR0=-1
for s,V,u in parents:
    Rmax=Rmax_for_violation(s,V,[],0)
    if Rmax<0:
        continue
    maxR0=max(maxR0,Rmax)
    z=z_digit(u,[],0)
    for R in range(Rmax+1):
        aw=aggregate_W(R,z,mult[0])
        if aw is not None:
            W,k=aw
            branches0.append((s,V,u,R,W,k,z,Rmax))

expected0=[
(17,3585578471836378705,2676,2347331680252628172,0,136502,4168),
(88,3168404756614383926,1212,665699585122209231,0,143890,3441),
(120,4704229396349756379,1102,7256323665933132521,1,77741,5144),
(181,1433106225230204489,351,3525274858541501307,0,68699,1087),
(269,4601510981844588415,1563,4190974443663710538,0,212589,4528),
(291,3283386165682403757,2166,8732181812213421555,2,130010,2902),
(340,4184337266622593636,99,2509342348533291597,0,219977,3801),
(347,4915966282561415230,3488,2807257316524707496,0,83332,4640),
(362,2866212450460408978,702,7050549717083002614,1,137398,2175),
(418,4498792567339420451,2024,1125625221394288555,0,90720,3913),
(511,2763494035955241014,1163,3985200494813580631,0,15529,1559),
(621,4613773976407440282,2978,9192107448485500879,2,76840,3374),
(692,4196600261185445503,1514,7510475353355081938,1,84228,2647),
(763,3779426545963450724,50,5828843258224662997,1,91616,1920),
(841,4093881846680277539,1975,4445126131085659955,1,219076,2032),
(912,3676708131458282760,511,2763494035955241014,0,226464,1304),
(1186,3374515825304307812,1,9148344167916034397,2,219972,39),
]
obs0=[(s,V,R,W,k,z,Rmax) for s,V,u,R,W,k,z,Rmax in branches0]
assert obs0==expected0
assert maxR0==5820

branches1=[]
maxR1=-1
for s,V,u,R0,W0,k0,z0,Rmax0 in branches0:
    Rmax=Rmax_for_violation(s,V,[R0],1)
    if Rmax<0: continue
    maxR1=max(maxR1,Rmax)
    z=z_digit(u,[W0],1)
    for R1 in range(Rmax+1):
        aw=aggregate_W(R1,z,mult[1])
        if aw is not None:
            W1,k=aw
            branches1.append((s,V,u,R0,W0,R1,W1,k,z,Rmax))

expected1=[
(362,2866212450460408978,702,7050549717083002614,459,12401578526950999455,2,131302,4591),
(511,2763494035955241014,1163,3985200494813580631,705,731966135778615573,0,104199,1236),
(621,4613773976407440282,2978,9192107448485500879,946,10847865075131040170,2,106749,1236),
(763,3779426545963450724,50,5828843258224662997,923,3017645723377190431,0,232951,5828),
]
obs1=[(s,V,R0,W0,R1,W1,k,z,Rmax) for s,V,u,R0,W0,R1,W1,k,z,Rmax in branches1]
assert obs1==expected1
assert maxR1==12597

maxR2=-1
z2_records=[]
branches2=[]
for s,V,u,R0,W0,R1,W1,k1,z1,Rmax1 in branches1:
    Rmax=Rmax_for_violation(s,V,[R0,R1],2)
    maxR2=max(maxR2,Rmax)
    z=z_digit(u,[W0,W1],2)
    z2_records.append((s,z,Rmax))
    for R2 in range(Rmax+1):
        aw=aggregate_W(R2,z,mult[2])
        if aw is not None:
            branches2.append((s,V,R0,W0,R1,W1,R2,aw,z,Rmax))
assert z2_records==[(362,79595,12879),(511,193213,1657),(621,194825,906),(763,14479,15287)]
assert branches2==[]

print('P02 T02 mixed-modulus p-adic aggregate dual checker')
print('D01_num=',D01.numerator)
print('D01_den=',D01.denominator)
print('Dnew_num=',D.numerator)
print('Dnew_den=',D.denominator)
print('CUT=',CUT)
print('parent_cases=',len(parents))
print('type0_max_R_budget=',maxR0)
print('type0_aggregate_branches=',len(branches0))
print('type1_max_R_budget=',maxR1)
print('type1_aggregate_branches=',len(branches1))
print('type2_max_R_budget=',maxR2)
print('type2_records=',z2_records)
print('type2_aggregate_branches=',len(branches2))
print('D_NEW_GT_4_D_01=PASS')
print('MIXED_MODULUS_AGGREGATE_LEMMA=PASS')
print('PARENT_CUTOFF=PASS')
print('TYPE0_FILTER=PASS')
print('TYPE1_FILTER=PASS')
print('TYPE2_OBSTRUCTION=PASS')
print('GLOBAL_TWO_STEP_DEFECT_D_NEW=PASS')
print('ALL_EXACT_CHECKS_PASS')
