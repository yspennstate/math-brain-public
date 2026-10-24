from fractions import Fraction
import math
import numpy as np

def mat_frac(S):
    return [[Fraction(x) for x in row] for row in S]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mt(A):
    return [list(r) for r in zip(*A)]

def madd(A,B,sign=1):
    return [[A[i][j]+sign*B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

# Decimal surrogates copied verbatim from the archived run-11 output.
SVs=[
["13.04608076804903","-2.851455378646798","-6.207676502398775"],
["-2.851455378646798","0.881598407384783","1.205533454959895"],
["-6.207676502398774","1.205533454959895","3.471419855287467"],
]
SCs=[
["1.386137482513434","-0.3052089430374908","0.08919474817932224"],
["-0.3052089430374908","0.3201370259500949","-0.2260392208152745"],
["0.08919474817932227","-0.2260392208152745","1.06520209021245"],
]
# Rational 6-decimal split proposed from a floating optimal split, then verified directly.
T6s=[
["0.325811","0.026584","0.244991"],
["0.276295","0.421851","-0.006373"],
["0.399423","-0.105053","0.566593"],
]
Aq=mat_frac(SVs); Bq=mat_frac(SCs); Tq=mat_frac(T6s)
Iq=[[Fraction(int(i==j)) for j in range(3)] for i in range(3)]
ImT=madd(Iq,Tq,sign=-1)

lpq=Fraction("8.150767890649966")
lnq=Fraction("5.269860599061735")
uq=Fraction("5.856667999143172")
vq=Fraction("0.5364470108663389")
wq=Fraction("1.153411776660164")
Dq=[[Fraction(0) for _ in range(3)] for _ in range(3)]
Dq[0][0]=uq*(lpq-uq)/lpq
Dq[1][1]=vq*(lnq-vq)/lnq
Dq[2][2]=wq*(lnq-wq)/lnq
Dq[1][2]=Dq[2][1]=-vq*wq/lnq

Rq=madd(mm(mm(mt(Tq),Aq),Tq), mm(mm(mt(ImT),Bq),ImT))
Mq=madd(Dq,Rq,sign=-1)
lead1=Mq[0][0]
lead2=det2([row[:2] for row in Mq[:2]])
lead3=det3(Mq)
assert lead1>0 and lead2>0 and lead3>0

# Floating diagnostics on exactly the same finite-decimal surrogate.
SV=np.array([[float(x) for x in row] for row in SVs])
SC=np.array([[float(x) for x in row] for row in SCs])
T6=np.array([[float(x) for x in row] for row in T6s])
lp=float(lpq); ln=float(lnq); u=float(uq); v=float(vq); w=float(wq)
D=np.array([[u*(lp-u)/lp,0.0,0.0],
            [0.0,v*(ln-v)/ln,-v*w/ln],
            [0.0,-v*w/ln,w*(ln-w)/ln]])
R6=T6.T@SV@T6+(np.eye(3)-T6).T@SC@(np.eye(3)-T6)
eig_matrix=np.linalg.eigvalsh(D-R6)

t=0.1309
Rscalar=t*t*SV+(1-t)*(1-t)*SC
eig_scalar=np.linalg.eigvalsh(D-Rscalar)

P=np.linalg.inv(np.linalg.inv(SV)+np.linalg.inv(SC))
eig_parallel_gap=np.linalg.eigvalsh(D-P)
Topt=np.linalg.solve(SV+SC,SC)
opt_gap=np.max(np.abs(Topt.T@SV@Topt+(np.eye(3)-Topt).T@SC@(np.eye(3)-Topt)-P))

# Support-only Popoviciu diagnostic. This is deliberately NOT a theorem certificate:
# it tests the much cruder attempt to eliminate Gibbs multipliers entirely.
GAMMA=4.4898
M=23
def root_eq(q):
    return q-(1.0-math.exp(-1.5*GAMMA*q*q))
lo,hi=0.9,1.0
for _ in range(200):
    mid=(lo+hi)/2
    if root_eq(lo)*root_eq(mid)<=0:
        hi=mid
    else:
        lo=mid
q=(lo+hi)/2
a=1.5*GAMMA*q*q
def delta_b(i,j):
    if i<j or j<1:
        return 0.0
    return math.exp(-2*a+(i+j)*math.log(a)-math.lgamma(i+1)-math.lgamma(j+1))*(2.0 if i>j else 1.0)
light=[]
light_p=light_n=0.0
for i in range(1,M+1):
    for j in range(1,i+1):
        d=delta_b(i,j)
        light.append((i,j,d))
        light_p+=i*d
        light_n+=j*d
hns=ln-light_n
gamma_b=(lp+ln)/3.0
from math import comb, factorial
gamma_k=[comb(3,k)*lp**k*ln**(3-k)/(lp+ln)**3*gamma_b for k in range(4)]
def clause_states(K):
    out=[]
    for ps in range(4):
        for ns in range(4-ps):
            for pu in range(4-ps-ns):
                nu=3-ps-ns-pu
                if ps+ns<1 or ps+pu!=K:
                    continue
                ns1=ns if ps+ns==1 else 0
                ns2=0 if ps+ns==1 else ns
                zeros=sum(int(x==0) for x in (ps,ns,pu,nu))
                out.append((ps,ns1,ns2,2.0/factorial(zeros)))
    return out
CST=[clause_states(k) for k in range(4)]
def pop_v(z):
    aa,bb,cc=z
    s=0.0
    for i,j,d in light:
        vals=[aa*i]+[bb*k+cc*(j-k) for k in range(1,j+1)]
        rr=max(vals)-min(vals)
        s+=d*rr*rr/4.0
    s+=hns*(bb-cc)*(bb-cc)/4.0
    return s
def pop_c(z):
    s=0.0
    for K in range(4):
        vals=[z@np.array([ps,ns1,ns2],dtype=float) for ps,ns1,ns2,_ in CST[K]]
        rr=max(vals)-min(vals)
        s+=gamma_k[K]*rr*rr/4.0
    return s
x=np.array([-1.0,10.0,-6.0])
support_upper=pop_v(T6@x)+pop_c((np.eye(3)-T6)@x)
copy_var=float(x@D@x)
support_ratio=support_upper/copy_var

print("PROB10_04_PARALLEL_SUM_SPLIT_CHECK")
print("FINITE_DECIMAL_SURROGATE_ONLY_NOT_SOURCE_INTERVAL_CERTIFICATE")
print("T6 =")
for row in T6s:
    print("  "+" ".join(row))
print("exact_surrogate_leading_principal_minors =")
print("  lead1 =", lead1)
print("  lead2 =", lead2)
print("  lead3 =", lead3)
print("decimal_leading_principal_minors =",
      f"{float(lead1):.16g}", f"{float(lead2):.16g}", f"{float(lead3):.16g}")
print("eig_D_minus_R_T6 =", " ".join(f"{z:.16g}" for z in eig_matrix))
print("scalar_t =", t)
print("eig_D_minus_scalar_split =", " ".join(f"{z:.16g}" for z in eig_scalar))
print("eig_D_minus_exact_parallel_sum =", " ".join(f"{z:.16g}" for z in eig_parallel_gap))
print("optimal_split_identity_residual_inf =", f"{opt_gap:.16g}")
print("support_only_test_direction =", x.tolist())
print("support_only_Popoviciu_upper =", f"{support_upper:.16g}")
print("copy_direction_variance =", f"{copy_var:.16g}")
print("support_only_ratio =", f"{support_ratio:.16g}")
print("SUPPORT_ONLY_SHORTCUT_FAILS_AT_TEST_DIRECTION =", bool(support_ratio>1.0))
print("EXACT_RATIONAL_SURROGATE_LMI_PASS =", True)
print("PARALLEL_SUM_SPLIT_DIAGNOSTIC_COMPLETE =", True)
