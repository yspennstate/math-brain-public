"""Exact rational certificate for a proposed Whitt1983 Conjecture1.1 counterexample.

All decisive operations use fractions.Fraction. Numerical matrix probes are
not imported or used. The quadratic rate matrix is enclosed by rational
sub/supersolutions and a globally verified weighted contraction.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json

def zeros(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def ident(n): return [[F(int(i==j)) for j in range(n)]for i in range(n)]
def add(A,B):return [[a+b for a,b in zip(ar,br)]for ar,br in zip(A,B)]
def neg(A):return [[-a for a in row]for row in A]
def mul(A,B):
    return [[sum((A[i][k]*B[k][j]for k in range(len(B))),F(0))
             for j in range(len(B[0]))]for i in range(len(A))]
def le(A,B):return all(a<=b for ar,br in zip(A,B)for a,b in zip(ar,br))
def inv(A):
    n=len(A); aug=[row.copy()+ident(n)[i]for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n)if aug[k][j])
        aug[j],aug[k]=aug[k],aug[j]
        d=aug[j][j];aug[j]=[v/d for v in aug[j]]
        for k in range(n):
            if k!=j:
                d=aug[k][j];aug[k]=[v-d*u for v,u in zip(aug[k],aug[j])]
    R=[row[n:]for row in aug]
    assert mul(A,R)==ident(n) and mul(R,A)==ident(n)
    return R
def decimal(x):
    with localcontext()as ctx:
        ctx.prec=60
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def certify(name,lam,p,ms,ml,cent,weight):
    lam,p,ms,ml=map(F,(lam,p,ms,ml))
    D=zeros(3,3);M=[]
    for i in range(3):
        M.append(lam+i*ms+(2-i)*ml)
        D[i][i]=i*ms*p+(2-i)*ml*(1-p)
        if i:D[i][i-1]=i*ms*(1-p)
        if i<2:D[i][i+1]=(2-i)*ml*p
    C=[[F(v,10**12)for v in row]for row in cent]
    W=[[F(v,1000)for v in row]for row in weight]
    eps=F(1,10**10)
    L=[[c-eps*w for c,w in zip(cr,wr)]for cr,wr in zip(C,W)]
    U=[[c+eps*w for c,w in zip(cr,wr)]for cr,wr in zip(C,W)]
    def phi(R):
        S=mul(mul(R,R),D)
        return [[(S[i][j]+(lam if i==j else 0))/M[j]for j in range(3)]for i in range(3)]
    assert le(zeros(3,3),L) and le(L,U)
    assert le(L,phi(L)) and le(phi(U),U)
    JW=mul(add(mul(U,W),mul(W,U)),D)
    JW=[[JW[i][j]/M[j]for j in range(3)]for i in range(3)]
    assert all(JW[i][j]<W[i][j]for i in range(3)for j in range(3))
    contraction=max(JW[i][j]/W[i][j]for i in range(3)for j in range(3))
    assert contraction<1
    assert max(map(sum,U))<1
    # Positive phi maps[0,U] into itself and is a contraction there,
    # in norm max|Rij|/Wij. Hence its unique fixed point R satisfies L<=R<=U.

    def boundary(R):
        K=zeros(5,5)
        K[0][0]=-(lam+ms);K[0][4]=lam*p;K[0][3]=lam*(1-p)
        K[1][1]=-(lam+ml);K[1][3]=lam*p;K[1][2]=lam*(1-p)
        RD=mul(R,D)
        for i in range(3):
            for j in range(3):K[2+i][2+j]=RD[i][j]-(M[i]if i==j else 0)
        K[2][1]=2*ml
        K[3][0]=ml;K[3][1]=ms
        K[4][0]=2*ms
        A=neg(K)
        assert all(A[i][j]<=0 for i in range(5)for j in range(5)if i!=j)
        AI=inv(A)
        assert le(zeros(5,5),AI)
        b=[[lam*p,lam*(1-p),F(0),F(0),F(0)]]
        x=mul(b,AI)[0]
        assert all(v>0 for v in x)
        RI=inv(add(ident(3),neg(R)))
        assert le(zeros(3,3),RI)
        busy=mul([x[2:]],mul(RI,[[F(1)]]*3))[0][0]
        idle=1+x[0]+x[1]
        return x,busy,idle
    xl,bl,al=boundary(L);xu,bu,au=boundary(U)
    assert all(a<=b for a,b in zip(xl,xu)) and bl<=bu and al<=au
    lower=bl/(au+bl)
    upper=bu/(al+bu)
    assert 0<lower<upper<1
    return {
        "model":name,"lambda_positive":str(lam),"small_probability":str(p),
        "mu_small":str(ms),"mu_large":str(ml),"root_interval_epsilon":str(eps),
        "center_integer_over_10^12":cent,"weight_integer_over_1000":weight,
        "weighted_contraction_constant_display":decimal(contraction),
        "P_delay_lower_display":decimal(lower),"P_delay_upper_display":decimal(upper),
        "lower_exact":lower,"upper_exact":upper,
        "checks":["0<L<=U", "L<=phi(L)","phi(U)<=U",
                  "J(U)W<W", "maximum row sum of U <1",
                  "boundary inverse positive", "stationary probability bounded monotonically"]
    }

BASE=certify("base_H2",F(11,10),F(3,7),F(5),F(5,8),
 [[645435924416,49602947283,1418851601],
  [57824475940,180926269658,1000913825],
  [5450513476,10688133781,103306610564]],
 [[12081,5279,1625],[3773,2173,1203],[2385,1615,1115]])
SPREAD=certify("spread_zero_H2",F(121,140),F(3,11),F(5,2),F(5,8),
 [[586680778400,40002694466,1185264216],
  [81777989182,240684772329,1984662856],
  [14780864226,25599440016,153162276790]],
 [[9144,4036,1362],[4484,2426,1187],[3007,1880,1123]])
assert BASE["lower_exact"]>F(39287,100000)
assert SPREAD["upper_exact"]<F(39172,100000)
GAP=BASE["lower_exact"]-SPREAD["upper_exact"]
assert GAP>F(23,20000)
for x in [BASE,SPREAD]:
    x.pop("lower_exact");x.pop("upper_exact")
print(json.dumps({"arithmetic":"exact rational Fraction; decimals are display only",
                 "models":[BASE,SPREAD],
                 "certified_gap_lower_display":decimal(GAP),
                 "exact_assertions":["P_delay(base)>.39287", "P_delay(spread)<.39172", "gap>.00115"],
                 "conclusion":"Proposed strict counterexample to Whitt1983 Conjecture1.1 at threshold0"},indent=2))
