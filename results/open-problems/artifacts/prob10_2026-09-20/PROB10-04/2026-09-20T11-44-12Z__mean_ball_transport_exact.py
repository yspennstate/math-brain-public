from fractions import Fraction as F
from itertools import combinations
from math import factorial

def mat(rows):
    return [[F(x) for x in row] for row in rows]
def I3():
    return [[F(int(i==j)) for j in range(3)] for i in range(3)]
def mt(A):
    return [list(r) for r in zip(*A)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A,B,sgn=1):
    return [[A[i][j]+sgn*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(A,c):
    return [[c*x for x in row] for row in A]
def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def sylvester_pd(A):
    return A[0][0] > 0 and det2([row[:2] for row in A[:2]]) > 0 and det3(A) > 0
def inv3(A):
    d=det3(A)
    assert d != 0
    cof = [
      [ A[1][1]*A[2][2]-A[1][2]*A[2][1], -(A[1][0]*A[2][2]-A[1][2]*A[2][0]), A[1][0]*A[2][1]-A[1][1]*A[2][0] ],
      [-(A[0][1]*A[2][2]-A[0][2]*A[2][1]), A[0][0]*A[2][2]-A[0][2]*A[2][0], -(A[0][0]*A[2][1]-A[0][1]*A[2][0]) ],
      [ A[0][1]*A[1][2]-A[0][2]*A[1][1], -(A[0][0]*A[1][2]-A[0][2]*A[1][0]), A[0][0]*A[1][1]-A[0][1]*A[1][0] ],
    ]
    return mscale(mt(cof), F(1,1)/d)
def qform(A,d):
    v=[F(z) for z in d]
    return sum(v[i]*A[i][j]*v[j] for i in range(3) for j in range(3))
def sub_scalar_I(A,c):
    return [[A[i][j]-(c if i==j else F(0)) for j in range(3)] for i in range(3)]
def scalar_I_minus(A,c):
    return [[(c if i==j else F(0))-A[i][j] for j in range(3)] for i in range(3)]

# Finite-decimal saddle surrogate copied verbatim from the preceding archived checker.
# Every calculation below treats these decimals as exact rationals. Therefore the final
# ball is an exact certificate for this surrogate only, NOT a source interval certificate.
SV=mat([
["13.04608076804903","-2.851455378646798","-6.207676502398775"],
["-2.851455378646798","0.881598407384783","1.205533454959895"],
["-6.207676502398774","1.205533454959895","3.471419855287467"],
])
SC=mat([
["1.386137482513434","-0.3052089430374908","0.08919474817932224"],
["-0.3052089430374908","0.3201370259500949","-0.2260392208152745"],
["0.08919474817932227","-0.2260392208152745","1.06520209021245"],
])
T=mat([
["0.325811","0.026584","0.244991"],
["0.276295","0.421851","-0.006373"],
["0.399423","-0.105053","0.566593"],
])
I=I3()
ImT=madd(I,T,-1)
RV=mm(mm(mt(T),SV),T)
RC=mm(mm(mt(ImT),SC),ImT)

lp=F("8.150767890649966")
ln=F("5.269860599061735")
u=F("5.856667999143172")
v=F("0.5364470108663389")
w=F("1.153411776660164")
D=[[F(0) for _ in range(3)] for _ in range(3)]
D[0][0]=u*(lp-u)/lp
D[1][1]=v*(ln-v)/ln
D[2][2]=w*(ln-w)/ln
D[1][2]=D[2][1]=-v*w/ln
M0=madd(madd(D,RV,-1),RC,-1)

# Exact center spectral envelopes by Sylvester tests.
eta=F(7,100)
rv_bound=F(32,125)       # 0.256
rc_bound=F(1057,1000)    # 1.057
BinvV=F(619,100)         # ||SV^-1|| <= 6.19
BinvC=F(103,20)          # ||SC^-1|| <= 5.15
assert sylvester_pd(sub_scalar_I(M0,eta))
assert sylvester_pd(scalar_I_minus(RV,rv_bound))
assert sylvester_pd(scalar_I_minus(RC,rc_bound))
assert sylvester_pd(sub_scalar_I(SV,1/BinvV))
assert sylvester_pd(sub_scalar_I(SC,1/BinvC))

invV=inv3(SV)
invC=inv3(SC)

# Exact support enumeration. Variable states are compared only inside one log-sum-exp
# block; clause states are compared only inside one syntactic positive-count class r.
M=23
var_blocks=[[(0,1,0),(0,0,1)]]
for i in range(1,M+1):
    for j in range(1,i+1):
        var_blocks.append([(i,0,0)]+[(0,k,j-k) for k in range(1,j+1)])

max_euclid2_V=F(-1)
max_maha2_V=F(-1)
arg_euclid_V=None
arg_maha_V=None
paircountV=0
for block in var_blocks:
    for a,b in combinations(block,2):
        d=tuple(a[k]-b[k] for k in range(3))
        eu=F(sum(z*z for z in d))
        ma=qform(invV,d)
        paircountV += 1
        if eu>max_euclid2_V:
            max_euclid2_V=eu; arg_euclid_V=(a,b)
        if ma>max_maha2_V:
            max_maha2_V=ma; arg_maha_V=(a,b)

def clause_states(r):
    out=[]
    for ps in range(4):
        for ns in range(4-ps):
            for pu in range(4-ps-ns):
                nu=3-ps-ns-pu
                if ps+ns<1 or ps+pu!=r:
                    continue
                ns1=ns if ps+ns==1 else 0
                ns2=0 if ps+ns==1 else ns
                out.append(((ps,ns1,ns2),(ps,ns,pu,nu)))
    return out

max_euclid2_C=F(-1)
max_maha2_C=F(-1)
arg_euclid_C=None
arg_maha_C=None
paircountC=0
for r in range(4):
    block=clause_states(r)
    for aa,bb in combinations(block,2):
        a,atype=aa; b,btype=bb
        d=tuple(a[k]-b[k] for k in range(3))
        eu=F(sum(z*z for z in d))
        ma=qform(invC,d)
        paircountC += 1
        if eu>max_euclid2_C:
            max_euclid2_C=eu; arg_euclid_C=(r,aa,bb)
        if ma>max_maha2_C:
            max_maha2_C=ma; arg_maha_C=(r,aa,bb)

assert max_euclid2_V == F(1058) # (23 sqrt2)^2
assert max_euclid2_C == F(10)
assert max_maha2_V < F(2068)
assert max_maha2_C < F(931,100)

# Rational Euclidean-ball coefficients obtained from the Mahalanobis theorem:
# a_*^2 <= L_*^2 ||Sigma_0^-1||.
assert F(2068)*BinvV < F(114*114)
assert F(931,100)*BinvC < F(7*7)
aV=F(114)
aC=F(7)

# Copy covariance Lipschitz sqrt(6) < 49/20.
LD=F(49,20)
assert F(6) < LD*LD

# Exact anisotropic-surrogate mean-ball certificate at rho=0.0015.
rho=F(3,2000)
sV=aV*rho
sC=aC*rho
assert sV<1 and sC<1
degradation = LD*rho + (sV/(1-sV))*rv_bound + (sC/(1-sC))*rc_bound
slack=eta-degradation
assert slack>0

# Conservative isotropic comparison using L_V=23 sqrt(2), L_C=sqrt(10).
sqrt2_up=F(283,200)
sqrt10_up=F(317,100)
assert F(2) < sqrt2_up*sqrt2_up
assert F(10) < sqrt10_up*sqrt10_up
aV_iso=F(202)
aC_iso=F(82,5) # 16.4
assert F(23)*sqrt2_up*BinvV < aV_iso
assert sqrt10_up*BinvC < aC_iso
rho_iso=F(21,25000) # 0.00084
siV=aV_iso*rho_iso
siC=aC_iso*rho_iso
degradation_iso = LD*rho_iso + (siV/(1-siV))*rv_bound + (siC/(1-siC))*rc_bound
slack_iso=eta-degradation_iso
assert slack_iso>0

print("PROB10_04_MEAN_BALL_TRANSPORT_CHECK")
print("FINITE_DECIMAL_SURROGATE_ONLY_NOT_SOURCE_INTERVAL_CERTIFICATE")
print("variable_within_block_pair_count =",paircountV)
print("clause_within_block_pair_count =",paircountC)
print("max_euclid2_variable =",max_euclid2_V,"arg =",arg_euclid_V)
print("max_euclid2_clause =",max_euclid2_C,"arg =",arg_euclid_C)
print("max_maha2_variable_exact =",max_maha2_V)
print("max_maha2_variable_decimal =",float(max_maha2_V),"arg =",arg_maha_V)
print("max_maha2_clause_exact =",max_maha2_C)
print("max_maha2_clause_decimal =",float(max_maha2_C),"arg =",arg_maha_C)
print("center_eta_lower =",float(eta))
print("RV_op_upper =",float(rv_bound))
print("RC_op_upper =",float(rc_bound))
print("invSV_op_upper =",float(BinvV))
print("invSC_op_upper =",float(BinvC))
print("anisotropic_euclidean_transport_coeff_upper_V =",float(aV))
print("anisotropic_euclidean_transport_coeff_upper_C =",float(aC))
print("rho_isotropic_certified_surrogate =",float(rho_iso))
print("isotropic_remaining_slack_exact =",slack_iso)
print("isotropic_remaining_slack_decimal =",float(slack_iso))
print("rho_anisotropic_certified_surrogate =",float(rho))
print("anisotropic_over_isotropic_radius_factor =",float(rho/rho_iso))
print("sV_upper =",float(sV))
print("sC_upper =",float(sC))
print("degradation_upper_exact =",degradation)
print("degradation_upper_decimal =",float(degradation))
print("remaining_LMI_slack_exact =",slack)
print("remaining_LMI_slack_decimal =",float(slack))
print("EXACT_SUPPORT_ENUMERATION_PASS =", True)
print("EXACT_CENTER_SPECTRAL_ENVELOPES_PASS =", True)
print("EXACT_SURROGATE_MEAN_BALL_LMI_PASS =", True)
