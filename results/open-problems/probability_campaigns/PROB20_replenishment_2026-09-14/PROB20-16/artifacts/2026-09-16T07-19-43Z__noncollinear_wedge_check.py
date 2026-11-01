from fractions import Fraction as F
import itertools, math
import numpy as np

def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def outer(w):
    return [[w[i]*w[j] for j in range(len(w))] for i in range(len(w))]
def frob2(A):
    return sum(A[i][j]*A[i][j] for i in range(len(A)) for j in range(len(A[0])))
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def fmt(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)

a=F(1,2); c=a*(1-a)
w0=[F(1,20),F(1,30)]
w1=[F(3,50),F(41,1000)]
B0=[[F(9,20),F(3,25)],[F(3,25),F(11,20)]]
dB=[[F(1,20),F(1,50)],[F(1,50),-F(1,25)]]
B1=mat_add(B0,dB)

wedge=w0[0]*w1[1]-w0[1]*w1[0]
assert wedge == F(1,20000)
assert wedge*wedge == F(1,400000000)

dw=[w1[i]-w0[i] for i in range(2)]
A=[[F(0),dw[0],dw[1]],[dw[0],dB[0][0],dB[0][1]],[dw[1],dB[1][0],dB[1][1]]]
detA=det3(A)
assert detA == F(743,180000000)

U0=[[outer(w0)[i][j]/c for j in range(2)] for i in range(2)]
U1=[[outer(w1)[i][j]/c for j in range(2)] for i in range(2)]
F10=[[B0[i][j]-(1-a)*U0[i][j] for j in range(2)] for i in range(2)]
F11=[[B1[i][j]-(1-a)*U1[i][j] for j in range(2)] for i in range(2)]
F00=[[B0[i][j]+a*U0[i][j] for j in range(2)] for i in range(2)]
F01=[[B1[i][j]+a*U1[i][j] for j in range(2)] for i in range(2)]
assert F10[0][1] == F(7,60)
assert F11[0][1] == F(3377,25000)
assert F00[0][1] == F(37,300)
assert F01[0][1] == F(3623,25000)
kappa=F(7,60)
assert all(M[0][1] >= kappa for M in [F10,F11,F00,F01])

D1=[[F11[i][j]-F10[i][j] for j in range(2)] for i in range(2)]
D0=[[F01[i][j]-F00[i][j] for j in range(2)] for i in range(2)]
assert D1[0][0] == F(239,5000)
assert D1[0][0] > F(1,25)

m11=F(9,2500)
m22=F(1681,1000000)
m12=F(123,50000)
b11_min,b11_max=F(9,20),F(1,2)
b22_min,b22_max=F(51,100),F(11,20)
b12_min,b12_max=F(3,25),F(7,50)

f1_low=[b11_min-2*m11-b12_max, b22_min-2*m22-b12_max]
f1_up=[b11_max+b12_max, b22_max+b12_max]
f0_low=[b11_min-(b12_max+2*m12), b22_min-(b12_max+2*m12)]
f0_up=[b11_max+2*m11+(b12_max+2*m12), b22_max+2*m22+(b12_max+2*m12)]
assert f1_low == [F(757,2500),F(183319,500000)]
assert f1_up == [F(16,25),F(69,100)]
assert f0_low == [F(7627,25000),F(9127,25000)]
assert f0_up == [F(16303,25000),F(349141,500000)]
for q in f1_low+f0_low:
    assert q > F(1,4)
for q in f1_up+f0_up:
    assert q < F(3,4)

S_exact=a*kappa*kappa*frob2(D1)+(1-a)*kappa*kappa*frob2(D0)
S_crude=a*kappa*kappa*F(1,25)**2
assert S_exact > S_crude == F(49,4500000)
wedge_scale=(wedge*wedge)/c
assert wedge_scale == F(1,100000000)
penalty_upper=8*wedge_scale
assert penalty_upper == F(1,12500000)
cert_coeff=2*S_crude-penalty_upper
assert cert_coeff == F(2441,112500000)
assert cert_coeff > 0

def adj2(M):
    return [[M[1][1],-M[0][1]],[-M[1][0],M[0][0]]]
def quad(v,M):
    return sum(v[i]*M[i][j]*v[j] for i in range(2) for j in range(2))
assert quad(dw,adj2(outer(dw))) == 0
assert quad(dw,adj2(outer(w0))) == wedge*wedge
assert quad(dw,adj2(outer(w1))) == wedge*wedge

def npK(B,w):
    return np.array([[float(a),float(w[0]),float(w[1])],
                     [float(w[0]),float(B[0][0]),float(B[0][1])],
                     [float(w[1]),float(B[1][0]),float(B[1][1])]],dtype=float)
K0=npK(B0,w0); K1=npK(B1,w1)
def exact_probs(K):
    n=K.shape[0]
    dets={}
    for mask in range(1<<n):
        idx=[i for i in range(n) if (mask>>i)&1]
        dets[mask]=1.0 if not idx else float(np.linalg.det(K[np.ix_(idx,idx)]))
    p=np.zeros(1<<n)
    for S in range(1<<n):
        p[S]=sum(((-1)**((T^S).bit_count()))*dets[T]
                 for T in range(1<<n) if (T&S)==S)
    return p
def entropy(K):
    p=exact_probs(K)
    assert p.min() > -1e-13
    return -sum(x*math.log(x) for x in p if x>0)
p0=exact_probs(K0); p1=exact_probs(K1)
assert abs(p0.sum()-1)<1e-12 and abs(p1.sum()-1)<1e-12
assert p0.min()>0 and p1.min()>0
gap=entropy((K0+K1)/2)-(entropy(K0)+entropy(K1))/2

print("EXACT CERTIFICATE")
print("wedge =",fmt(wedge))
print("wedge^2 =",fmt(wedge*wedge))
print("det(direction) =",fmt(detA))
print("F10,F11,F00,F01 offdiag =",*[fmt(M[0][1]) for M in [F10,F11,F00,F01]])
print("Delta1_11 =",fmt(D1[0][0]))
print("F1 Gersh lower =",*[fmt(q) for q in f1_low])
print("F1 Gersh upper =",*[fmt(q) for q in f1_up])
print("F0 Gersh lower =",*[fmt(q) for q in f0_low])
print("F0 Gersh upper =",*[fmt(q) for q in f0_up])
print("S exact =",fmt(S_exact),float(S_exact))
print("S crude >",fmt(S_crude))
print("wedge penalty using Lambda<8 <",fmt(penalty_upper))
print("certified bracket >",fmt(cert_coeff),float(cert_coeff))
print("certified midpoint gap >",float(cert_coeff/F(4)))
print()
print("DIAGNOSTICS ONLY")
print("eig(K0) =",np.linalg.eigvalsh(K0))
print("eig(K1) =",np.linalg.eigvalsh(K1))
print("eig(direction) =",np.linalg.eigvalsh(K1-K0))
print("min exact-atom K0 =",p0.min())
print("min exact-atom K1 =",p1.min())
print("midpoint entropy gap =",gap)
print("ALL EXACT ASSERTIONS PASSED")
