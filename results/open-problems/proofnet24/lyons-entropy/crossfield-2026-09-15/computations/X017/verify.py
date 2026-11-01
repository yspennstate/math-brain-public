#!/usr/bin/env python3
"""Exact minor/derivative checks for X017; logarithms are diagnostic floats."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json, math
from pathlib import Path

OUT = Path(__file__).resolve().parent
n, r = 12, 5
Qnum = [[(6 if i == j else 0) - 1 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        assert sum(Qnum[i][k] * Qnum[j][k] for k in range(n)) == (36 if i == j else 0)

def det_int(a):
    a = [row[:] for row in a]
    if not a: return 1
    sign, previous = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,len(a)) if a[j][k]), None)
            if j is None: return 0
            a[k],a[j] = a[j],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]

def minor(rows, cols):
    return F(det_int([[Qnum[i][j] for j in cols] for i in rows]), 6**len(cols))

def law(cols):
    ans = {}
    for S in combinations(range(n),len(cols)):
        d = minor(S,cols)
        if d: ans[S] = d*d
    assert sum(ans.values()) == 1
    return ans

R = tuple(range(r)); Iu = R+(5,); Iv = R+(6,); Itop = R+(5,6)
a, c, dlaw, b = law(R), law(Iu), law(Iv), law(Itop)
e = {}
for U in combinations(range(n),r+1):
    row = minor(U,Iu), minor(U,Iv)
    if any(row): e[U] = row
for i in range(2):
    for j in range(2):
        assert sum(z[i]*z[j] for z in e.values()) == (1 if i == j else 0)
m = {U:(eu*eu+ev*ev)/2 for U,(eu,ev) in e.items()}
assert sum(m.values()) == 1
assert all(len(p)==36 and set(p.values())=={F(1,36)} for p in [a,c,dlaw,b])
assert len(set(c)&set(dlaw)) == 10
assert Counter(m.values()) == Counter({F(1,36):10,F(1,72):52})

# M=(first diagonal, second diagonal, real upper offdiagonal, imaginary upper offdiagonal).
def determinant(M):
    aa,dd,x,y = M
    return aa*dd-x*x-y*y

def strict(M):
    aa,dd,x,y = M
    return aa>0 and determinant(M)>0 and 1-aa>0 and determinant((1-aa,1-dd,-x,-y))>0

def shifted(M,A,t): return tuple(x+t*y for x,y in zip(M,A))

def atoms(M):
    aa,dd,x,y = M
    dm = determinant(M); d0 = 1-aa-dd+dm
    ans = {S:d0*p for S,p in a.items()}
    ans.update({T:dm*p for T,p in b.items()})
    ans.update({U:(aa-dm)*eu*eu+(dd-dm)*ev*ev+2*x*eu*ev for U,(eu,ev) in e.items()})
    assert all(p>0 for p in ans.values()) and sum(ans.values())==1
    return ans

def derivatives(M,A):
    aa,dd,x,y = M; aA,dA,xA,yA = A
    first = dd*aA+aa*dA-2*x*xA-2*y*yA
    delta = determinant(A)
    ans1 = {S:(-aA-dA+first)*p for S,p in a.items()}
    ans2 = {S:2*delta*p for S,p in a.items()}
    ans1.update({T:first*p for T,p in b.items()})
    ans2.update({T:2*delta*p for T,p in b.items()})
    ans1.update({U:(aA-first)*eu*eu+(dA-first)*ev*ev+2*xA*eu*ev for U,(eu,ev) in e.items()})
    ans2.update({U:-2*delta*(eu*eu+ev*ev) for U,(eu,ev) in e.items()})
    assert sum(ans1.values())==sum(ans2.values())==0
    return ans1,ans2

def entropy(p): return -sum(float(v)*math.log(float(v)) for v in p.values())
def hessian(M,A):
    p=atoms(M); dp,ddp=derivatives(M,A)
    fisher=sum(float(dp[S]**2/p[S]) for S in p)
    acceleration=sum(float(ddp[S])*math.log(float(p[S])) for S in p)
    return -fisher-acceleration, fisher

M0 = (F(1,3),F(2,3),F(1,10),F(1,7))
M1 = (F(3,5),F(2,5),F(0),F(1,8))
assert strict(M0) and strict(M1)
comm_real = (M0[0]-M0[1])*M1[2]-(M1[0]-M1[1])*M0[2]
comm_imag = (M0[0]-M0[1])*M1[3]-(M1[0]-M1[1])*M0[3]
assert (comm_real,comm_imag) == (F(-1,50),F(-59,840))
As = {
 'definite':(F(2,7),F(1,5),F(-1,11),F(2,13)),
 'indefinite':(F(1,5),F(-2,7),F(1,9),F(1,11)),
 'rank_one':(F(1),F(1),F(0),F(1)),
}
assert determinant(As['definite'])>0
assert determinant(As['indefinite'])<0
assert determinant(As['rank_one'])==0

# Exact quadratic identity checks, including complex active entries.
t = F(1,1000); checks = {}
for name,A in As.items():
    plus,minus=shifted(M0,A,t),shifted(M0,A,-t)
    assert strict(plus) and strict(minus)
    p,pp,pm=atoms(M0),atoms(plus),atoms(minus)
    dp,ddp=derivatives(M0,A)
    for S in p:
        assert pp[S]-pm[S]==2*t*dp[S]
        assert pp[S]+pm[S]-2*p[S]==t*t*ddp[S]
    hh,fi=hessian(M0,A)
    checks[name]={'det_A':str(determinant(A)),'H_second':hh,'Fisher':fi}

beta_star = F(13,9)*math.log(2)
assert abs(2*entropy(m)-entropy(a)-entropy(b)-float(beta_star))<2e-13
Cbeta = 8-F(10,9)*math.log(2)
center = (F(1,2),F(1,2),F(0),F(0))
unit = (F(1),F(1),F(0),F(0))
hcenter,_=hessian(center,unit)
assert abs(hcenter+float(Cbeta))<2e-13

# Exact coefficients of the full central Hessian, logarithms evaluated numerically.
Lstar=2*math.log(2)-float(beta_star)
for A in As.values():
    tr=A[0]+A[1]
    a0,d0=A[0]-tr/2,A[1]-tr/2
    norm0=a0*a0+d0*d0+2*(A[2]*A[2]+A[3]*A[3])
    middle=4*sum(float((a0*eu*eu+d0*ev*ev+2*A[2]*eu*ev)**2/(eu*eu+ev*ev)) for eu,ev in e.values())
    expected=float(Cbeta)/4*float(tr*tr)+Lstar*float(norm0)+middle
    got,_=hessian(center,A)
    assert abs(-got-expected)<2e-12

# Information identities at one noncentral point. These are diagnostics, not universal tests.
P=atoms(M0); dm=determinant(M0); d0m=1-M0[0]-M0[1]+dm
f1=M0[0]+M0[1]-2*dm
T=float(f1)/(2*math.sqrt(float(dm*d0m)))
nu={U:P[U]/f1 for U in e}
D=sum(float(m[U])*math.log(float(m[U]/nu[U])) for U in m)
Lambda=sum(2*float(m[U])*math.log(float(P[U])) for U in e)-math.log(float(dm*d0m))+entropy(a)+entropy(b)
assert -1e-14<=D<=math.log(T)+1e-14
assert abs(Lambda-(2*math.log(2*T)-float(beta_star)-2*D))<2e-13
assert Lambda>=2*math.log(2)-float(beta_star)-1e-13
for name,A in As.items():
    delta=float(determinant(A)); hh,fi=hessian(M0,A)
    assert abs(hh-(-fi+2*delta*Lambda))<2e-13
    if delta>0:
        lower=delta*(float(Cbeta)+4*(T-1-math.log(T))+4*D)
        assert -hh>=lower-1e-13

result={
 'status':'PASS',
 'exact_checks':['integer orthogonality','all projection minors','middle frame isometry','10/52 fair-middle atom counts','strict noncommuting endpoints','quadratic atom derivatives for three direction types'],
 'n':n,'r':r,'middle_mass_counts':{str(k):v for k,v in Counter(m.values()).items()},
 'beta_star_exact':'(13/9) log 2','C_beta_exact':'8 - (10/9) log 2',
 'center_second':hcenter,
 'endpoint_determinants':{'M0':str(determinant(M0)),'M1':str(determinant(M1))},
 'commutator_01':{'real':str(comm_real),'imag':str(comm_imag)},
 'diagnostic_information':{'T':T,'D':D,'log_T_minus_D':math.log(T)-D,'Lambda':Lambda},
 'diagnostic_curvatures':checks,
 'scope':'Exact algebra checks and one deterministic floating-log diagnostic. Universal claims rest on the report proofs.'
}
(OUT/'verified_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
