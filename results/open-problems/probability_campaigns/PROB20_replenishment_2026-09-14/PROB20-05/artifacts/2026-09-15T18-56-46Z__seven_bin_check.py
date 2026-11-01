"""
PROB20-05 exact/self-check artifact for the seven-consecutive-bin theorem.

New items checked:
- displacement-group aggregation transport and its exact quadratic threshold certificate;
- exact enumeration of all 3447 indecomposable S_7 permutations;
- exactly 14 failures of the universal 2/5 displacement-group threshold,
  split into 4 type-A and 10 type-B patterns;
- finite bridge n=7,...,13 using exact group-threshold, endpoint, and integer cell certificates;
- exact n=14,...,20 interval bridge plus special-pattern checks;
- three exact boundary transports covering all type-B symmetry orbits;
- analytic inequalities used for n>=21.

SciPy Hungarian matching is used only to FIND balanced assignments. Every successful
cell certificate is recomputed by exact integer arithmetic.
"""
import itertools
from collections import defaultdict
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment

def consecutive_components(perm):
    n=len(perm); out=[]; start=0
    for k in range(1,n+1):
        if set(perm[start:k])==set(range(start,k)):
            out.append((start,k)); start=k
    assert start==n
    return out

def inverse_perm(p):
    out=[0]*len(p)
    for i,j in enumerate(p): out[j]=i
    return tuple(out)

def reverse_conjugate(p):
    m=len(p)
    return tuple(m-1-p[m-1-i] for i in range(m))

def orbit4(p):
    return {p,inverse_perm(p),reverse_conjugate(p),inverse_perm(reverse_conjugate(p))}

def displacement_groups(p):
    g=defaultdict(list)
    for j,s in enumerate(p): g[j-s].append(j)
    return [(d,sorted(js)) for d,js in sorted(g.items())]

def B_group(p):
    m=len(p); cum=Fraction(0); B=Fraction(0)
    for d,js in displacement_groups(p):
        alpha=Fraction(len(js),m)
        mu=-1+2*cum+alpha
        B += alpha*d*mu
        cum += alpha
    return B

def F_pieces(p):
    m=len(p); breaks={Fraction(0),Fraction(1)}; groups=[]
    for d,js in displacement_groups(p):
        k=len(js); pcs=[]
        for r,j in enumerate(js):
            lo=Fraction(r,k); hi=Fraction(r+1,k)
            pcs.append((lo,hi,Fraction(2*k),Fraction(2*j-d-m-2*r)))
            breaks.add(lo); breaks.add(hi)
        groups.append((d,js,pcs))
    out=[]; br=sorted(breaks)
    for a,b in zip(br[:-1],br[1:]):
        mid=(a+b)/2; sl=Fraction(0); ic=Fraction(0)
        for d,js,pcs in groups:
            alpha=Fraction(len(js),m)
            for lo,hi,s,q in pcs:
                if lo <= mid < hi:
                    sl += alpha*s; ic += alpha*q; break
        out.append((a,b,sl-Fraction(2*m),ic+Fraction(m)))
    return out

def quad_max(A2,A1,A0,a,b):
    cand=[(A2*a*a+A1*a+A0,a),(A2*b*b+A1*b+A0,b)]
    if A2<0:
        v=-A1/(2*A2)
        if a<=v<=b: cand.append((A2*v*v+A1*v+A0,v))
    return max(cand,key=lambda z:z[0])

def threshold_ok(p,ratio):
    B=B_group(p); coeff=2*B/ratio
    cum=Fraction(0); worst=(Fraction(-10**9),None)
    for a,b,sl,ic in F_pieces(p):
        A2=sl/2; A1=ic; A0=cum-A2*a*a-A1*a
        val,pt=quad_max(A2+coeff,A1-coeff,A0,a,b)
        if val>worst[0]: worst=(val,pt)
        cum += sl*Fraction(b*b-a*a,2)+ic*(b-a)
    assert cum==0
    return worst[0] <= 0, B, worst

def HGS_interval(a,b):
    a=sp.Rational(a) if not isinstance(a,sp.Basic) else a
    b=sp.Rational(b) if not isinstance(b,sp.Basic) else b
    L=sp.simplify(b-a); mid=sp.simplify((a+b)/2)
    rt2=sp.sqrt(2); half=sp.Rational(1,2)
    def Hleft(x): return rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    def Hright(x): return -rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    def Qleft(x): return -x+rt2*sp.Rational(2,3)*x**sp.Rational(3,2)
    def Qright(x): return x+rt2*sp.Rational(2,3)*(1-x)**sp.Rational(3,2)
    def Ileft(x):
        return (-x**2/sp.Integer(2)+mid*x
                +rt2*(sp.Rational(2,5)*x**sp.Rational(5,2)
                       -sp.Rational(2,3)*mid*x**sp.Rational(3,2)))
    def Iright(x):
        return (x**2/sp.Integer(2)-mid*x
                -rt2*(sp.Rational(2,3)*(mid-1)*(1-x)**sp.Rational(3,2)
                       +sp.Rational(2,5)*(1-x)**sp.Rational(5,2)))
    def piece(F1,F2,x,y):
        ans=sp.S(0)
        if x<half:
            z=y if y<=half else half
            ans += F1(z)-F1(x)
        if y>half:
            z=x if x>=half else half
            ans += F2(y)-F2(z)
        return sp.simplify(ans)
    H=sp.simplify(piece(Hleft,Hright,a,b)/L)
    G=sp.simplify(4*piece(Ileft,Iright,a,b)/L**2)
    S=sp.simplify((piece(Qleft,Qright,mid,b)-piece(Qleft,Qright,a,mid))/L)
    return H,G,S

def psi12(k):
    k=abs(k)
    if k==0: return 8
    if k==1: return 13
    return 12*k

def J_fraction(p):
    n=len(p); S=0
    for i in range(n):
        for j in range(n):
            d=i-j; e=p[i]-p[j]
            S += abs(d-e)*psi12(d+e)
    return Fraction(S,12*n**4)

def global_perm(n,k,local):
    p=list(range(n))
    for j,v in enumerate(local): p[k+j]=k+v
    return tuple(p)

def matching_certificate(p):
    n=len(p)
    a=np.array([2*i+1-n for i in range(n)],dtype=np.int64)
    cells=[(r,s) for r in range(n) for s in range(n)]
    labels=[i for i in range(n) for _ in range(n)]
    lab=np.array(labels,dtype=np.int64)
    lx=a[lab]; ly=a[np.array([p[i] for i in labels],dtype=np.int64)]
    M=np.empty((n*n,n*n),dtype=np.int64)
    for rr,(r,s) in enumerate(cells): M[rr,:]=a[r]*lx+a[s]*ly
    rows,cols=linear_sum_assignment(-M)
    counts=[0]*n; W=0
    for rr,cc in zip(rows,cols):
        i=labels[cc]; counts[i]+=1; r,s=cells[rr]
        W += int(a[r])*int(a[i])+int(a[s])*int(a[p[i]])
    assert counts==[n]*n
    return W,15*W-7*n*n*(n*n-1)

S7=list(itertools.permutations(range(7)))
inde=[p for p in S7 if max(b-a for a,b in consecutive_components(p))==7]
assert len(inde)==3447
bad25=[]
for p in inde:
    ok,B,w=threshold_ok(p,Fraction(2,5))
    if not ok: bad25.append((p,B,w))
assert len(bad25)==14

typeA=[p for p,B,w in bad25 if B==Fraction(50,49)]
typeB=[p for p,B,w in bad25 if B==Fraction(8,7)]
assert len(typeA)==4 and len(typeB)==10
A_pieces=[(Fraction(0),Fraction(1,2),Fraction(-76,7),Fraction(36,7)),
          (Fraction(1,2),Fraction(1),Fraction(-76,7),Fraction(40,7))]
B_pieces=[(Fraction(0),Fraction(1),Fraction(-12),Fraction(6))]
assert all(F_pieces(p)==A_pieces for p in typeA)
assert all(F_pieces(p)==B_pieces for p in typeB)

thresholds={7:Fraction(7,10),8:Fraction(11,20),9:Fraction(1,2),10:Fraction(9,20),
            11:Fraction(7,16),12:Fraction(29,70),13:Fraction(29,70)}
fail_counts={Fraction(7,10):2272,Fraction(11,20):532,Fraction(1,2):180,
             Fraction(9,20):50,Fraction(7,16):30,Fraction(29,70):14}
for rat,cnt in fail_counts.items():
    assert sum(not threshold_ok(p,rat)[0] for p in inde)==cnt

expected_res={7:2,8:8,9:172,10:192,11:150,12:84,13:98}
expected_minmargin={7:3396,8:4956,9:7080,10:10260,11:12480,12:14916,13:17256}
finite_summary={}
for n,rat in thresholds.items():
    for k in range(n-6):
        H,G,S=HGS_interval(sp.Rational(k,n),sp.Rational(k+7,n))
        assert sp.simplify(rat*H-G).is_nonnegative is True
    passset={p for p in inde if threshold_ok(p,rat)[0]}
    residual=[]
    for k in range(n-6):
        for p in inde:
            if p in passset: continue
            gp=global_perm(n,k,p)
            if J_fraction(gp)>=Fraction(2,15): continue
            residual.append((k,p))
    assert len(residual)==expected_res[n]
    margins=[]
    for k,p in residual:
        W,mar=matching_certificate(global_perm(n,k,p))
        assert mar>=0
        margins.append(mar)
    assert min(margins)==expected_minmargin[n]
    finite_summary[n]=(len(residual),min(margins))

def A_bracket(H,G,S):
    return sp.simplify(sp.Rational(50,49)*H-sp.Rational(19,7)*G+sp.Rational(2,7)*S)
def B_bracket(H,G): return sp.simplify(sp.Rational(8,7)*H-3*G)
for n in range(14,21):
    for k in range(n-6):
        H,G,S=HGS_interval(sp.Rational(k,n),sp.Rational(k+7,n))
        assert sp.simplify(2*H-5*G).is_nonnegative is True
        assert A_bracket(H,G,S).is_positive is True
        if 0<k<n-7: assert B_bracket(H,G).is_positive is True

rt2=sp.sqrt(2)
EsL=rt2/3; EsH=(4-rt2)/3; EsF=sp.Rational(2,3)
EsrL=rt2/5; EsrH=sp.Rational(4,15)+2*rt2/15; EsrF=sp.Rational(2,5)
stat={'L':(EsL,EsrL),'H':(EsH,EsrH),'F':(EsF,EsrF)}
def zmean(idx): return sp.Rational(2*idx-6,7)
def exact_q2_score(p,assignment):
    total=sp.S(0)
    for j in range(7):
        cells=assignment[j]; bands=[a for a,z in cells]; zs=[z for a,z in cells]
        if bands[0]==bands[1]:
            typ='L' if bands[0]==0 else 'H'; zm=(zmean(zs[0])+zmean(zs[1]))/2
        else:
            assert set(bands)=={0,1} and zs[0]==zs[1]; typ='F'; zm=zmean(zs[0])
        Es,Esr=stat[typ]
        total += sp.Rational(1,2)*((j+p[j])*Es+2*Esr+(j-p[j])*Es*zm)
    return sp.simplify(total/7)
rep1=(1,4,2,0,6,3,5); rep2=(1,4,0,2,6,5,3); rep3=(1,4,0,3,6,2,5)
assign1={0:[(0,1),(0,2)],1:[(0,0),(1,0)],2:[(0,3),(0,4)],3:[(0,5),(0,6)],4:[(1,1),(1,2)],5:[(1,5),(1,6)],6:[(1,3),(1,4)]}
assign2={0:[(0,1),(0,2)],1:[(0,0),(1,0)],2:[(0,5),(0,6)],3:[(0,3),(0,4)],4:[(1,1),(1,2)],5:[(1,3),(1,4)],6:[(1,5),(1,6)]}
assign3={0:[(0,1),(0,2)],1:[(0,0),(1,0)],2:[(0,5),(0,6)],3:[(0,3),(0,4)],4:[(1,1),(1,2)],5:[(1,5),(1,6)],6:[(1,3),(1,4)]}
sc1=exact_q2_score(rep1,assign1); sc2=exact_q2_score(rep2,assign2); sc3=exact_q2_score(rep3,assign3)
assert sp.simplify(sc1-(sp.Rational(2591,735)-52*rt2/147))==0
assert sp.simplify(sc2-(sp.Rational(877,245)-8*rt2/21))==0
assert sp.simplify(sc3-(sp.Rational(857,245)-50*rt2/147))==0
for sc in (sc1,sc2,sc3): assert sp.simplify(sc-sp.Rational(14,5)).is_positive is True
assert 533**2-2*260**2==148889>0
assert 573**2-2*280**2==171529>0
assert 513**2-2*250**2==138169>0
covered=set()
for rep in (rep1,rep2,rep3): covered |= (orbit4(rep)&set(typeB))
assert covered==set(typeB)

r=sp.symbols('r', nonnegative=True)
R=2*(1-r)*(r**2+3*r+1)/(5*(r+1)*(r**2+r+1))
assert sp.factor(sp.diff(R,r)) == -4*r*(4*r**2+7*r+4)/(5*(r+1)**2*(r**2+r+1)**2)
r0=sp.sqrt(2)/4
assert sp.simplify(sp.Rational(8,21)-R.subs(r,r0)) == 2*(785-288*sp.sqrt(2))/7665
assert 785**2 > 2*288**2
P=22*r**4+22*r**3+32*r**2+22*r+22
sq=sp.factor(P**2-450*(r+1)**2*(r**2+1)**3)
assert sq == 2*(r-1)**2*(17*r**6+68*r**5+165*r**4+100*r**3+165*r**2+68*r+17)
t=sp.symbols('t', real=True)
K1=3*t-4*t*(1-t)
neg=-2*sp.integrate(K1,(t,0,sp.Rational(1,4)))
pos=2*sp.integrate(K1,(t,sp.Rational(1,4),sp.Rational(1,2)))
assert neg==sp.Rational(1,48) and pos==sp.Rational(5,48)
assert 5-sp.sqrt(3)>0
assert sp.simplify(sp.Rational(50,49)-sp.Rational(53,21)*sp.Rational(2,5))==sp.Rational(8,735)

print("EXACT SEVEN-BIN CHECKS PASSED")
print("indecomposable S7:",len(inde))
print("2/5 displacement-group exceptions:",len(bad25),"typeA",len(typeA),"typeB",len(typeB))
print("finite n=7..13 residual cell checks:",finite_summary)
print("boundary type-B scores:",sc1,sc2,sc3)
