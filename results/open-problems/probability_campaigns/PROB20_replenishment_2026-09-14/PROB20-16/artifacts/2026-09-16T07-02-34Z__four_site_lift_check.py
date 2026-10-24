#!/usr/bin/env python3
from fractions import Fraction as F
import math
import numpy as np

# PROB20-16 explicit four-site example checker.
# Exact parts use Fractions; floating-point spectra/Jensen gaps are diagnostics only.

def row_margins(diag, edges):
    rows = [F(0), F(0), F(0)]
    for (i,j),(re,im) in edges.items():
        b = abs(re) + abs(im)   # rigorous upper bound on complex modulus
        rows[i] += b
        rows[j] += b
    return [(diag[i], rows[i], diag[i]-rows[i]) for i in range(3)]

# Conditional strictness margins from the report.
F10_diag = [F(43,100), F(43,100), F(41,100)]
F10_edges = {
    (0,1):(F(1,100),F(1,40)),
    (0,2):(-F(7,250),F(3,125)),
    (1,2):(-F(1,75),-F(17,600)),
}
F11_diag = [d+F(1,200) for d in F10_diag]
F11_edges = dict(F10_edges)
adds = {
    (0,1):(F(1,200),F(0)),
    (0,2):(F(0),-F(1,200)),
    (1,2):(F(0),-F(1,200)),
}
for k,(ar,ai) in adds.items():
    re,im = F11_edges[k]
    F11_edges[k] = (re+ar,im+ai)

IF00_diag = [F(53,100),F(53,100),F(51,100)]
F00_edges = {
    (0,1):(F(1,100),-F(3,200)),
    (0,2):(F(3,250),-F(2,125)),
    (1,2):(F(2,75),F(7,600)),
}
F01_edges = dict(F00_edges)
for k,(ar,ai) in adds.items():
    re,im = F01_edges[k]
    F01_edges[k] = (re+ar,im+ai)
IF01_diag = [F(21,40),F(21,40),F(101,200)]

margins = {
    "F10": row_margins(F10_diag,F10_edges),
    "F11": row_margins(F11_diag,F11_edges),
    "I-F00": row_margins(IF00_diag,F00_edges),
    "I-F01": row_margins(IF01_diag,F01_edges),
}
expected = {
    "F10":[F(343,1000),F(53,150),F(949,3000)],
    "F11":[F(87,250),F(209,600),F(241,750)],
    "I-F00":[F(477,1000),F(7,15),F(1331,3000)],
    "I-F01":[F(231,500),F(277,600),F(329,750)],
}
for name, vals in margins.items():
    got = [x[2] for x in vals]
    assert got == expected[name], (name,got,expected[name])
    assert all(x > 0 for x in got)

# Exact theorem parameters.
a = F(1,2)
# v=(1,i,1+i)/10 -> ||v||^2=1/25, so P has operator rank one.
v_norm_sq = F(1,25)
assert v_norm_sq == F(1,100)+F(1,100)+F(1,50)
s0 = F(1,1)/(a*(1-a))
s1 = s0
assert s0 == 4 and s1 == 4
delta_s = s1-s0
assert delta_s == 0

# R=(1/200) r r*, r=(1,1,i), so R is PSD rank one and all diagonal entries are 1/200.
R_diag = [F(1,200)]*3
quant_coeff = F(6,7)*sum(x*x for x in R_diag)
assert quant_coeff == F(9,140000)
midpoint_bound = quant_coeff*F(1,4)
assert midpoint_bound == F(9,560000)

# Scalar-strength defect for z0=1,z1=i:
# [t(1-t)|i-1|^2]/[a(1-a)] = 8 t(1-t).
assert F(2,1)/(a*(1-a)) == 8

# Floating diagnostic construction.
v = np.array([1,1j,1+1j],dtype=complex)/10
P = np.outer(v,v.conj())
B0 = np.eye(3,dtype=complex)*(9/20)
B0[0,1]=1/100+1j/200; B0[1,0]=B0[0,1].conjugate()
B0[0,2]=-1/125+1j/250; B0[2,0]=B0[0,2].conjugate()
B0[1,2]=1/150-1j/120; B0[2,1]=B0[1,2].conjugate()
r = np.array([1,1,1j],dtype=complex)
R = np.outer(r,r.conj())/200
B1 = B0 + R
w0 = v
w1 = 1j*v

K0 = np.block([[np.array([[0.5]],dtype=complex), w0.conj()[None,:]],
               [w0[:,None], B0]])
K1 = np.block([[np.array([[0.5]],dtype=complex), w1.conj()[None,:]],
               [w1[:,None], B1]])

def atoms(K):
    n=K.shape[0]
    out=[]
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        Q=K.copy()
        for i in range(n):
            if i not in S:
                Q[i,i]-=1
        p=(((-1)**(n-len(S)))*np.linalg.det(Q)).real
        out.append(p)
    return np.array(out)

def entropy(K):
    p=atoms(K)
    assert p.min() > -1e-12
    return -sum(float(x)*math.log(float(x)) for x in p if x>0)

for label,K in [("K0",K0),("K1",K1)]:
    assert np.linalg.eigvalsh(K).min() > 0
    assert np.linalg.eigvalsh(np.eye(4)-K).min() > 0
    p=atoms(K)
    assert abs(p.sum()-1) < 1e-12
    assert p.min() > 0

D=K1-K0
evD=np.linalg.eigvalsh(D)
# Rank 3 and indefinite: one negative, two positive, one zero (up to rounding).
assert np.sum(evD < -1e-10) == 1
assert np.sum(evD > 1e-10) == 2
assert np.sum(np.abs(evD) <= 1e-10) == 1

gaps={}
for t in [0.25,0.5,0.75]:
    Kt=(1-t)*K0+t*K1
    gap=entropy(Kt)-(1-t)*entropy(K0)-t*entropy(K1)
    gaps[t]=gap
    assert gap > 0
assert gaps[0.5] > float(midpoint_bound)

print("PASS exact diagonal-dominance margins:")
for name in ["F10","F11","I-F00","I-F01"]:
    print(name, [str(x[2]) for x in margins[name]])
print("PASS exact s0=s1=",s0,"delta_s=",delta_s)
print("PASS exact quantitative coefficient =",quant_coeff)
print("PASS exact midpoint lower bound =",midpoint_bound)
print("PASS exact phase-strength defect coefficient = 8")
print("diagnostic eig(K0) =",np.linalg.eigvalsh(K0))
print("diagnostic eig(I-K0) =",np.linalg.eigvalsh(np.eye(4)-K0))
print("diagnostic eig(K1) =",np.linalg.eigvalsh(K1))
print("diagnostic eig(I-K1) =",np.linalg.eigvalsh(np.eye(4)-K1))
print("diagnostic eig(K1-K0) =",evD)
for t,g in gaps.items():
    print(f"diagnostic Jensen gap t={t}: {g:.15g}")
print("ALL CHECKS PASS")
