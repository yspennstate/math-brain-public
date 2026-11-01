from fractions import Fraction as Q
from itertools import product

STATES = [tuple(b) for b in product((0,1), repeat=5)]
W = (6,8,4,7,6)

A=(0,0,1,1,1)
B=(0,1,0,0,1)
C=(0,1,0,1,0)
D=(0,1,1,0,0)
E=(0,1,1,0,1)
F=(1,0,1,0,1)
G=(1,1,1,0,0)
H=(1,0,1,1,0)
I=(0,0,1,1,0)
J=(1,0,0,0,1)
K=(1,1,0,0,0)

T0=[A,B,C,D,E,F]
T1=[A,C,D,E,F,G]
T2=[A,C,D,F,H,G]
K15=[I,A,C,D,F,H]
T12=[A,C,D,J,H,K]

SSTAR=Q(20,27)
SMAX=Q(4,5)


def dot(w,b):
    return sum(Q(x)*y for x,y in zip(w,b))

def hinge(b,t):
    return max(Q(0), dot(W,b)-Q(t))

def solve_linear(M,y):
    A=[list(map(Q,row))+[Q(rhs)] for row,rhs in zip(M,y)]
    n=len(A)
    for col in range(n):
        piv=next(r for r in range(col,n) if A[r][col] != 0)
        A[col],A[piv]=A[piv],A[col]
        z=A[col][col]
        A[col]=[v/z for v in A[col]]
        for r in range(n):
            if r==col: continue
            z=A[r][col]
            if z:
                A[r]=[A[r][c]-z*A[col][c] for c in range(n+1)]
    return [A[i][-1] for i in range(n)]

def det(M):
    A=[list(map(Q,row)) for row in M]
    n=len(A); d=Q(1)
    for col in range(n):
        piv=next((r for r in range(col,n) if A[r][col] != 0),None)
        if piv is None: return Q(0)
        if piv!=col:
            A[col],A[piv]=A[piv],A[col]; d=-d
        z=A[col][col]; d*=z
        for r in range(col+1,n):
            f=A[r][col]/z
            for c in range(col,n): A[r][c]-=f*A[col][c]
    return d

def common_lower_simplex(supp):
    M=[[1,*b] for b in supp]
    d=det(M)
    assert d != 0
    thresholds=sorted(set(int(dot(W,b)) for b in STATES))
    min_slack=None
    for t in thresholds:
        coeff=solve_linear(M,[hinge(b,t) for b in supp])
        for b in STATES:
            ell=coeff[0]+sum(coeff[i+1]*b[i] for i in range(5))
            sl=hinge(b,t)-ell
            if min_slack is None or sl<min_slack: min_slack=sl
            assert sl >= 0, (supp,t,b,sl,coeff)
    return d, len(thresholds), min_slack

def p_of(s):
    return (
        Q(1,10)+Q(19,50)*s,
        Q(4,5)-Q(57,100)*s,
        Q(7,10)+Q(1,10)*s,
        Q(3,10)+Q(31,50)*s,
        Q(1,2)-Q(23,100)*s,
    )

# barycentric masses q=a+b*s for the three existence simplices
Q0=[(Q(1,10),Q(19,100)), (Q(1,10),Q(-53,100)), (Q(1,5),Q(43,100)), (Q(3,10),Q(-1,5)), (Q(1,5),Q(-27,100)), (Q(1,10),Q(19,50))]
Q1=[(Q(0),Q(18,25)), (Q(3,10),Q(-1,10)), (Q(3,10),Q(-1,5)), (Q(3,10),Q(-4,5)), (Q(1,5),Q(-3,20)), (Q(-1,10),Q(53,100))]
Q2=[(Q(3,10),Q(-2,25)), (Q(3,10),Q(-1,10)), (Q(3,10),Q(-1,5)), (Q(1,5),Q(-3,20)), (Q(-3,10),Q(4,5)), (Q(1,5),Q(-27,100))]

def verify_bary(supp, forms, lo, hi):
    # Endpoint nonnegativity suffices because each mass is affine in s.
    for x in (lo,hi):
        qs=[a+b*x for a,b in forms]
        assert min(qs) >= 0, (supp,x,qs)
        assert sum(qs)==1
        p=p_of(x)
        for i in range(5):
            assert sum(q*st[i] for q,st in zip(qs,supp))==p[i], (supp,x,i,qs,p)

verify_bary(T0,Q0,Q(0),Q(10,53))
verify_bary(T1,Q1,Q(10,53),Q(3,8))
verify_bary(T2,Q2,Q(3,8),SSTAR)
print('EXISTENCE_BARYCENTRIC_INTERVALS_PASS')

for name,T in [('T0',T0),('T1',T1),('T2',T2)]:
    d,nk,ms=common_lower_simplex(T)
    print(f'{name}_COMMON_LOWER_PASS det={d} thresholds={nk} min_slack={ms}')

# Nonexistence side, s in (20/27, 4/5].
# threshold 15 dual ell15=-6+2b1+3b2+3b3+3b4+2b5

def ell15(b): return Q(-6)+2*b[0]+3*b[1]+3*b[2]+3*b[3]+2*b[4]
sl15={b: hinge(b,15)-ell15(b) for b in STATES}
assert min(sl15.values()) >= 0
TIGHT15={b for b,v in sl15.items() if v==0}
assert TIGHT15==set(K15), (TIGHT15,set(K15))
print('T15_DUAL_TIGHT_SET_PASS', sorted(''.join(map(str,b)) for b in TIGHT15))

# threshold 12 Jensen/mean lower plane ell12=S-12, tight exactly where S>=12

def ell12(b): return dot(W,b)-12
sl12={b: hinge(b,12)-ell12(b) for b in STATES}
assert min(sl12.values()) >= 0
TIGHT12={b for b,v in sl12.items() if v==0}
assert TIGHT12=={b for b in STATES if dot(W,b)>=12}
print('T12_DUAL_TIGHT_SET_PASS size=',len(TIGHT12))

# sharp primal witnesses for both objectives over the entire nonexistence interval
Q15=[(Q(-1,5),Q(27,100)), (Q(3,10),Q(-2,25)), (Q(3,10),Q(-1,10)), (Q(1,2),Q(-47,100)), (Q(1,5),Q(-3,20)), (Q(-1,10),Q(53,100))]
Q12=[(Q(7,10),Q(-1,2)), (Q(-1,10),Q(8,25)), (Q(3,10),Q(-1,5)), (Q(-1,5),Q(27,100)), (Q(-3,10),Q(4,5)), (Q(3,5),Q(-69,100))]
verify_bary(K15,Q15,SSTAR,SMAX)
verify_bary(T12,Q12,SSTAR,SMAX)
print('NONEXISTENCE_INDIVIDUAL_OPTIMA_PASS')

# The common tight intersection has five states and lies on the affine hyperplane
# -3 + b1 + 2 b2 + b3 + b4 + b5 = 0.
INTER=TIGHT12 & TIGHT15
expected={A,C,D,F,H}
assert INTER==expected, (INTER,expected)
def hyper_b(b): return Q(-3)+b[0]+2*b[1]+b[2]+b[3]+b[4]
assert all(hyper_b(b)==0 for b in INTER)

# Along p(s), the same affine functional equals (20-27s)/100,
# hence it is nonzero for s>20/27.
def hyper_p(s):
    p=p_of(s)
    return Q(-3)+p[0]+2*p[1]+p[2]+p[3]+p[4]
assert hyper_p(SSTAR)==0
assert hyper_p(SMAX)<0
assert hyper_p(Q(0))==Q(1,5)
assert hyper_p(Q(1))==Q(-7,100)
print('COMMON_FACE_OBSTRUCTION_PASS hyper_p(s)=(20-27s)/100')

# Sanity: all probabilities stay in [0,1] on the declared line interval.
for x in (Q(0),SMAX):
    assert all(Q(0)<=z<=Q(1) for z in p_of(x))
print('PARAMETER_DOMAIN_PASS')
print('CRITICAL_s=20/27')
print('ALL_EXACT_CHECKS_PASS')
