"""Exact certificates for the C070 conditional 2x2 factorization.

All identities and matrix signs use rational arithmetic. Natural logarithms
are enclosed by a dyadically reduced rational atanh series. The analytic
proof in agents/C070.md is dimension-uniform; these are finite corroborations.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent

def q(x):
    x=sp.Rational(x)
    return F(int(x.p),int(x.q))

def log_interval(x, terms=32):
    x=F(x); assert x>0
    k=0
    while x>=2: x/=2;k+=1
    while x<1: x*=2;k-=1
    def base(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return lo,lo+tail
    lo,hi=base(x);l2,h2=base(F(2))
    if k>=0:return lo+k*l2,hi+k*h2
    return lo+k*h2,hi+k*l2

def linear_interval(const, coefs):
    lo=hi=F(const)
    for x,c in coefs.items():
        if not c:continue
        l,h=log_interval(x)
        if c>=0:lo+=c*l;hi+=c*h
        else:lo+=c*h;hi+=c*l
    return lo,hi

def enc(x):return str(x)
def down(x):
    scale=10**18
    return F((x.numerator*scale)//x.denominator,scale)
def up(x):return -down(-x)
def interval_enc(it):
    return {'lower':str(down(it[0])),'upper':str(up(it[1])),'decimal_lower':float(it[0]),'decimal_upper':float(it[1])}

def atom_data(K,A):
    n=K.rows;ps=[];dp=[];dd=[]
    for mask in range(1<<n):
        N=K-sp.diag(*[0 if mask>>i&1 else 1 for i in range(n)])
        det=(-1)**(n-mask.bit_count())*N.det()
        assert det>0
        V=N.inv()*A;tr=sp.trace(V)
        ps.append(q(det));dp.append(q(det*tr));dd.append(q(det*(tr*tr-sp.trace(V*V))))
    assert sum(ps)==1 and sum(dp)==sum(dd)==0
    return ps,dp,dd

def generator(p,n,i,r,s):
    out=[F(0)]*len(p)
    for mask in range(1<<n):
        if mask>>i&1:continue
        other=mask|(1<<i);flow=r*p[mask]+s*p[other]
        out[mask]=-flow;out[other]=flow
    return out

def addcoef(out,x,c):out[x]=out.get(x,F(0))+c

def pd(M):
    return all(M[:j,:j].det()>0 for j in range(1,M.rows+1))

def check(name,K,alpha,beta):
    n=K.rows;D=sp.diag(*beta);A=alpha*K+D
    r=list(map(q,beta));s=[q(alpha+b) for b in beta]
    T=sp.diag(*[sp.Rational(b)/(alpha+2*b) for b in beta])
    assert pd(K) and pd(sp.eye(n)-K)
    assert pd(T-K) or pd(K-T)
    p,dp,dd=atom_data(K,A)
    gp=[generator(p,n,i,r[i],s[i]) for i in range(n)]
    assert [sum(gp[i][x] for i in range(n)) for x in range(1<<n)]==dp
    dd_channels=[F(0)]*len(p)
    for i in range(n):
        for j in range(i+1,n):
            part=generator(gp[j],n,i,r[i],s[i])
            dd_channels=[a+2*b for a,b in zip(dd_channels,part)]
    assert dd_channels==dd
    fisher=sum((z*z/x for z,x in zip(dp,p)),F(0))
    own=sum((z*z/x for row in gp for z,x in zip(row,p)),F(0))
    product_bound=sum((q(A[i,i])**2/(q(K[i,i])*(1-q(K[i,i]))) for i in range(n)),F(0))
    assert own>=product_bound
    curvature_coefs={}
    for pp,zz in zip(p,dd):addcoef(curvature_coefs,pp,-zz)
    hess_interval=linear_interval(-fisher,curvature_coefs)
    pair_log_coeffs={};cross_fisher=F(0);pairs=0;strict=0;min_det=None
    pair_min_lower=None
    for i in range(n):
        for j in range(i+1,n):
            for base in range(1<<n):
                if base>>i&1 or base>>j&1:continue
                ids=[base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)]
                mass=sum(p[k] for k in ids)
                a,b,c,d=[p[k]/mass for k in ids]
                R=a*d/(b*c);assert 0<R<=1
                X=r[i]*r[j]*a+s[i]*s[j]*d
                Y=r[i]*s[j]*b+s[i]*r[j]*c
                parity=X-Y;assert parity>=0
                if parity>0:strict+=1
                min_det=parity if min_det is None else min(min_det,parity)
                rat=X*(1/R-1)+Y*(1-R)
                C=X+Y
                factored=linear_interval(rat,{R:C})
                assert factored[1]>=0 # analytic factorization supplies nonnegativity
                if R<1: assert factored[0]>0
                pair_min_lower=factored[0] if pair_min_lower is None else min(pair_min_lower,factored[0])
                # Match the direct conditional Fisher cross exactly.
                gi=[-(r[i]*a+s[i]*c),-(r[i]*b+s[i]*d),r[i]*a+s[i]*c,r[i]*b+s[i]*d]
                gj=[-(r[j]*a+s[j]*b),r[j]*a+s[j]*b,-(r[j]*c+s[j]*d),r[j]*c+s[j]*d]
                direct=sum((z*w/pp for z,w,pp in zip(gi,gj,[a,b,c,d])),F(0))
                assert direct==rat
                cross_fisher+=mass*rat
                # C log R expands into original full atom logs; mass cancels.
                for ind,sign in zip(ids,[1,-1,-1,1]):addcoef(pair_log_coeffs,p[ind],2*mass*C*sign)
                # Recover the exact conditional principal determinant from atoms.
                x=c+d;y=b+d;rho=x*y-d
                ti=q(T[i,i]);tj=q(T[j,j])
                assert parity==(r[i]+s[i])*(r[j]+s[j])*((ti-x)*(tj-y)-rho)
                pairs+=1
    assert fisher==own+2*cross_fisher
    for pp in set(pair_log_coeffs)|set(curvature_coefs):
        assert pair_log_coeffs.get(pp,F(0))==-curvature_coefs.get(pp,F(0))
    assert hess_interval[1]<-product_bound
    return {'name':name,'dimension':n,'K':[[str(x) for x in row] for row in K.tolist()],
        'A':[[str(x) for x in row] for row in A.tolist()],
        'alpha':str(alpha),'beta':[str(b) for b in beta],
        'threshold':[str(T[i,i]) for i in range(n)],
        'atom_count':len(p),'conditional_pairs_checked':pairs,'strict_parity_pairs':strict,
        'minimum_parity':str(min_det),'minimum_pair_cross_lower':str(down(pair_min_lower)),
        'fisher':str(fisher),'own_fisher':str(own),'product_curvature_bound':str(product_bound),
        'hessian_interval':interval_enc(hess_interval),
        'strict_gap_lower':str(down(-product_bound-hess_interval[1])),'status':'PASS'}

V=sp.Matrix([[1,0],[1,1],[0,1],[1,-1],[2,1],[1,2]])
P=V*(V.T*V).inv()*V.T
assert P*P==P and sp.trace(P)==2
cases=[]
for t in [sp.Rational(0),sp.Rational(1,5)]:
    a=sp.Rational(2,5)+t;b=sp.Rational(1,100)+sp.Rational(6,5)*t
    K=a*P+b*(sp.eye(6)-P)
    u=sp.Rational(1);v=sp.Rational(6,5)
    alpha=(u-v)/(a-b);beta=(a*v-b*u)/(a-b)
    cases.append(check('rank_two_spectral_t_'+str(t),K,alpha,[beta]*6))
K=sp.diag(sp.Rational(1,10),sp.Rational(3,20),sp.Rational(1,10),sp.Rational(1,5))+sp.ones(4)/100
cases.append(check('nonconstant_diagonal_intersection',K,sp.Rational(1),[sp.Rational(i) for i in range(1,5)]))
# Exact obstruction to an unconditional sign for every conditional cross term.
a=b=d=F(1,1000);c=F(997,1000);R=a*d/(b*c)
X=a+d;Y=b+c;obstruction=linear_interval(X*(1/R-1)+Y*(1-R),{R:X+Y})
assert obstruction[1]<0
out={'status':'PASS','cases':cases,'projection':[[str(x) for x in row] for row in P.tolist()],
     'outside_threshold_cross_obstruction':{'table':[str(z) for z in [a,b,c,d]],'Q_interval':interval_enc(obstruction)}}
(HERE/'verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(cases),'exact kernel cases;',sum(z['conditional_pairs_checked'] for z in cases),'conditional pair factorizations')
for z in cases:print(z['name'],z['hessian_interval']['decimal_upper'],'<=',-float(F(z['product_curvature_bound'])))
