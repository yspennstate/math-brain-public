"""Deterministic checks of X014's proved matching/chromatic/pendant identities."""
from itertools import product
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import numpy as np
import sympy as sp

OUT={}

def matchings(edges):
    out=[]
    for mask in product((0,1),repeat=len(edges)):
        ids=[i for i,v in enumerate(mask) if v]
        vs=[v for i in ids for v in edges[i]]
        if len(vs)==len(set(vs)):out.append(ids)
    return out

def coeff_formula(edges,alpha):
    active={i for i,a in enumerate(alpha) if a}
    if not active:return Q(0)
    seen={next(iter(active))}
    while True:
        ext={i for i in active if any(set(edges[i])&set(edges[j]) for j in seen)}
        if ext==seen:break
        seen=ext
    if seen!=active:return Q(0)
    numerator=1
    while len(active)>1:
        deg={v:sum(v in edges[i] for i in active) for v in set(v for i in active for v in edges[i])}
        e=next(i for i in active if any(deg[v]==1 for v in edges[i]))
        neighbors=[j for j in active if j!=e and set(edges[e])&set(edges[j])]
        a=sum(alpha[j] for j in neighbors)
        assert a>=2 and alpha[e]%2==0
        numerator*=factorial(a+alpha[e]-2)//factorial(a-2)
        active.remove(e)
    last=next(iter(active));numerator*=factorial(alpha[last]-2)
    denominator=np.prod([factorial(a) for a in alpha],dtype=object)
    return Q(numerator,int(denominator))

def expansion_check(edges,N):
    m=len(edges);zero=(0,)*m
    v={tuple(int(i in M) for i in range(m)):Q(1) for M in matchings(edges) if M}
    powers={zero:Q(1)};total={}
    for k in range(1,N+1):
        nxt={}
        for a,c in powers.items():
            for b,d in v.items():
                ab=tuple(x+y for x,y in zip(a,b))
                if sum(ab)<=N:nxt[ab]=nxt.get(ab,Q(0))+c*d
        powers=nxt
        f=Q(1) if k==1 else Q((-1)**k,k*(k-1))
        for a,c in powers.items():total[a]=total.get(a,Q(0))+f*c
    count=0
    for alpha in product(range(0,N+1,2),repeat=m):
        if 0<sum(alpha)<=N:
            got=total.get(alpha,Q(0));expected=coeff_formula(edges,alpha)
            assert got==expected,(edges,alpha,got,expected)
            count+=1
    return count
OUT['exact_chromatic_coefficients']=sum(expansion_check(e,8) for e in [[(0,1),(1,2),(2,3)],[(0,1),(1,2),(1,3),(3,4)]])

# Independent exact rational determinant jets, all 64 atoms of a 3-core/3-leaf tree.
edges=[(0,1),(1,2),(0,3),(1,4),(2,5)];n=6
z=list(map(sp.Rational,['3/10','1/4','1/5','1/6','1/7']))
h=list(map(sp.Rational,['0','0','-1/20','1/15','1/30']))
K=sp.eye(n)/2;A=sp.zeros(n)
for (i,j),zz,hh in zip(edges,z,h):K[i,j]=K[j,i]=zz;A[i,j]=A[j,i]=hh
mm=matchings(edges);jet_checks=0
for spins in product((-1,1),repeat=n):
    M=sp.Matrix.hstack(*[(K[:,j] if spins[j]==1 else sp.eye(n)[:,j]-K[:,j]) for j in range(n)])
    D=sp.Matrix.hstack(*[(A[:,j] if spins[j]==1 else -A[:,j]) for j in range(n)])
    p=M.det();R=M.inv()*D
    detjets=[p,p*sp.trace(R),p*(sp.trace(R)**2-sp.trace(R*R))]
    qj=[sp.Rational(0)]*3
    ts=[-spins[i]*spins[j] for i,j in edges]
    for match in mm:
        poly=[sp.Rational(1),sp.Rational(0),sp.Rational(0)]
        for e in match:
            a=[4*z[e]**2,8*z[e]*h[e],4*h[e]**2]
            poly=[sum(poly[k]*a[j-k] for k in range(j+1))*ts[e] for j in range(3)]
        qj=[x+y for x,y in zip(qj,poly)]
    qj=[qj[0]/2**n,qj[1]/2**n,2*qj[2]/2**n]
    assert detjets==qj,(spins,detjets,qj)
    jet_checks+=3
OUT['exact_atom_jet_checks']=jet_checks

# Eight measured coordinates: fixed path core of size four; four independent leaves.
core=[(0,1),(1,2),(2,3)];pend=[(0,4),(1,5),(2,6),(3,7)];edges=core+pend;n=8
zc=np.array([.3,.2,.3]);z0=np.array([1/5,3/20,1/6,1/8]);z1=np.array([1/8,1/5,3/20,1/6]);dz=z1-z0
allm=matchings(edges);spins=np.array(list(product((-1.,1.),repeat=n)));ts=np.array([-spins[:,i]*spins[:,j] for i,j in edges]).T

def kernel(z):
    k=np.eye(n)/2
    for (i,j),v in zip(edges,np.r_[zc,z]):k[i,j]=k[j,i]=v
    return k

def tree_value(z):
    k=kernel(z);p=[]
    for s in spins:
        mat=k.copy()
        for j in range(n):
            if s[j]<0:mat[:,j]=np.eye(n)[:,j]-k[:,j]
        p.append(np.linalg.det(mat))
    p=np.array(p);return float(-np.dot(p,np.log(p))),p

def reduced(z):
    w=4*np.r_[zc,z]**2;q=np.ones(len(spins));d=np.zeros((len(spins),4));dd=np.zeros((len(spins),4,4))
    for M in allm:
        if not M:continue
        term=np.prod(ts[:,M],axis=1);q+=term*np.prod(w[M])
        for i in range(4):
            e=3+i
            if e not in M:continue
            d[:,i]+=term*np.prod(w[[j for j in M if j!=e]])
            for j in range(4):
                f=3+j
                if f!=e and f in M:dd[:,i,j]+=term*np.prod(w[[r for r in M if r not in (e,f)]])
    F=float(np.mean(q*np.log(q)));g=np.mean(d*np.log(q[:,None]),axis=0)
    hh=np.einsum('ti,tj,t->ij',d,d,1/q)/len(q)+np.einsum('tij,t->ij',dd,np.log(q))/len(q)
    adot=8*z*dz;addot=8*dz*dz
    curvature=float(adot@hh@adot+g@addot)
    quartic=float(np.dot(adot,adot)+np.dot(4*z*z,addot))
    return F,q,g,hh,curvature,quartic

def qmatch(w,edges,t):
    return sum(np.prod([w[e]*t[e] for e in M]) for M in matchings(edges))

def phi(a):return .5*((1+a)*np.log1p(a)+(1-a)*np.log1p(-a))

def conditional_factor(z):
    wc=4*zc*zc;a=4*z*z;corr=0.;maxerror=0.
    for tp in product((-1.,1.),repeat=4):
        Qv=1+a*np.array(tp);eff=np.array([wc[e]/(Qv[i]*Qv[j]) for e,(i,j) in enumerate(core)])
        Ft=0.
        for tc in product((-1.,1.),repeat=3):
            qc=qmatch(eff,core,tc);Ft+=qc*np.log(qc)/8
            direct=qmatch(np.r_[wc,a],edges,np.r_[tc,tp])
            maxerror=max(maxerror,abs(direct-np.prod(Qv)*qc))
        corr+=np.prod(Qv)*Ft/16
    return float(sum(phi(a))+corr),maxerror

samples=[]
for u in [0.,.5,1.]:
    z=(1-u)*z0+u*z1;H,p=tree_value(z);F,q,g,hh,curv,quartic=reduced(z);cf,err=conditional_factor(z)
    assert max(abs(p-q/2**n))<2e-15
    assert abs((n*np.log(2)-H)-F)<2e-14 and abs(cf-F)<2e-14
    assert np.linalg.eigvalsh(hh-np.eye(4))[0]>-1e-12
    assert min(g-4*z*z)>-1e-12 and curv>=quartic-1e-12
    samples.append(dict(t=u,entropy=H,min_eigenvalue=float(np.linalg.eigvalsh(kernel(z))[0]),max_eigenvalue=float(np.linalg.eigvalsh(kernel(z))[-1]),min_leaf_hessian_minus_I=float(np.linalg.eigvalsh(hh-np.eye(4))[0]),F_curvature=curv,quartic_curvature_lower_bound=quartic,factorization_max_error=err))
H0,Hm,H1=[x['entropy'] for x in samples];zg=(z0+z1)/2
OUT['rank_eight_example']=dict(core_edges=core,core_kernel_values=zc.tolist(),leaf_edges=pend,z0=z0.tolist(),z1=z1.tolist(),direction_inertia=[4,4],samples=samples,Jensen_gap=Hm-(H0+H1)/2,quartic_gap_lower_bound=float(8*((sum(z0**4)+sum(z1**4))/2-sum(zg**4))))
assert OUT['rank_eight_example']['Jensen_gap']>=OUT['rank_eight_example']['quartic_gap_lower_bound']>0
OUT['status']='PASS'
p=Path(__file__).with_name('results.json');p.write_text(json.dumps(OUT,indent=2));print(json.dumps(OUT,indent=2))
