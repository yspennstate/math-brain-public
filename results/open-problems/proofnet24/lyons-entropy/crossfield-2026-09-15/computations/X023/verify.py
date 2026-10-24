"""Deterministic checks for the proved X023 internal-bridge cavity closure.
Checks corroborate the proof; none is used to infer a universal sign.
"""
from itertools import product
from fractions import Fraction as Q
from pathlib import Path
import json
import numpy as np
import sympy as sp

OUT={}

def matchings(edges):
    ans=[]
    for bits in product((0,1),repeat=len(edges)):
        ids=[i for i,b in enumerate(bits) if b]
        vv=[v for i in ids for v in edges[i]]
        if len(vv)==len(set(vv)): ans.append(ids)
    return ans

def likelihood(edges,w,t,deleted=None):
    return sum((np.prod([w[e]*t[e] for e in M],dtype=object) for M in matchings(edges)
                if deleted is None or all(deleted not in edges[e] for e in M)), Q(0))

# Exact cavity identities for two branched rooted shapes, including depth three.
ca=[]
for edges,z in [([(0,1),(1,2),(1,3)],['1/5','1/6','1/7']),
                 ([(0,1),(1,2),(2,3),(1,4)],['1/4','1/7','1/6','1/8'])]:
    z=list(map(sp.Rational,z));w=[4*x*x for x in z]
    n=1+max(max(e) for e in edges);C=sp.zeros(n)
    for (i,j),v in zip(edges,z): C[i,j]=C[j,i]=2*v
    assert all(x>0 for x in (sp.eye(n)-C).cholesky().diagonal())
    c=(sp.eye(n)-C).inv()[0,0];mean=0;kap=0;maxR=0;total=0
    for t in product((-1,1),repeat=len(edges)):
        q=sp.Rational(likelihood(edges,w,t));qm=sp.Rational(likelihood(edges,w,t,0))
        assert q>0 and qm>0
        R=qm/q;assert R<=c
        total+=q;mean+=q*R;kap+=q*R*R;maxR=max(maxR,R)
    den=2**len(edges)
    assert total==den and mean==den and maxR==c and kap>=den
    ca.append(dict(edges=edges,assignments=den,cavity_max=str(c),kappa=str(kap/den)))
OUT['exact_cavity_checks']=ca

# Twelve-site theorem example, edge order = core, branches, moving bridges.
core=[(0,1),(1,2),(2,3)]
branch=[(4,5),(6,7),(8,9),(10,11)]
bridge=[(0,4),(1,6),(2,8),(3,10)]
edges=core+branch+bridge;n=12;m=len(edges);mm=matchings(edges)
zc=list(map(sp.Rational,['3/20','1/10','3/20']))
zb=[sp.Rational(1,4)]*4
z0=list(map(sp.Rational,['1/4','1/5','1/6','1/7']))
z1=list(map(sp.Rational,['1/7','1/6','1/5','1/4']))
zz=zc+zb+z0;hh=[sp.Rational(0)]*7+[y-x for x,y in zip(z0,z1)]
K=sp.eye(n)/2;A=sp.zeros(n)
for (i,j),z,h in zip(edges,zz,hh): K[i,j]=K[j,i]=z;A[i,j]=A[j,i]=h

# Deterministic exact mixed-column determinant jets at representative atoms.
def vertex_spins(t):
    spins={0:1}
    while len(spins)<n:
        for e,(i,j) in enumerate(edges):
            if i in spins and j not in spins:spins[j]=-int(t[e])*spins[i]
            elif j in spins and i not in spins:spins[i]=-int(t[e])*spins[j]
    return [spins[j] for j in range(n)]

assign=[tuple([-1]*m),tuple([1]*m)]
assign += [tuple(1 if j==i else -1 for j in range(m)) for i in range(m)]
assign += [tuple((-1)**j for j in range(m))]
exact_jets=0
for t in assign:
    spins=vertex_spins(t)
    M=sp.Matrix.hstack(*[(K[:,j] if spins[j]>0 else sp.eye(n)[:,j]-K[:,j]) for j in range(n)])
    V=sp.Matrix.hstack(*[(A[:,j] if spins[j]>0 else -A[:,j]) for j in range(n)])
    p=M.det();R=M.inv()*V
    detjets=[p,p*sp.trace(R),p*(sp.trace(R)**2-sp.trace(R*R))]
    qj=[sp.Rational(0)]*3
    for mat in mm:
        pol=[sp.Rational(1),sp.Rational(0),sp.Rational(0)]
        for e in mat:
            aa=[4*zz[e]**2,8*zz[e]*hh[e],4*hh[e]**2]
            pol=[sum(pol[k]*aa[j-k] for k in range(j+1))*t[e] for j in range(3)]
        qj=[a+b for a,b in zip(qj,pol)]
    assert detjets==[qj[0]/2**n,qj[1]/2**n,2*qj[2]/2**n]
    exact_jets+=3
OUT['exact_mixed_column_jet_equalities']=exact_jets

# Full 2048-sign finite entropy identity and strength Hessian.
ts=np.array(list(product((-1.,1.),repeat=m)))
mmcore=matchings(core)
weights0=4*np.array(list(map(float,zc+zb)))**2
kap=16/15

def reduced(z):
    w=np.r_[weights0,4*z*z];q=np.ones(len(ts));gq=np.zeros((len(ts),4));hq=np.zeros((len(ts),4,4))
    for mat in mm:
        if not mat:continue
        tm=np.prod(ts[:,mat],axis=1);q+=tm*np.prod(w[mat])
        for i in range(4):
            e=7+i
            if e not in mat:continue
            gq[:,i]+=tm*np.prod(w[[k for k in mat if k!=e]])
            for j in range(4):
                f=7+j
                if e!=f and f in mat:hq[:,i,j]+=tm*np.prod(w[[k for k in mat if k not in (e,f)]])
    assert min(q)>0
    F=np.mean(q*np.log(q));g=np.mean(gq*np.log(q[:,None]),axis=0)
    H=np.einsum('ti,tj,t->ij',gq,gq,1/q)/len(q)+np.einsum('tij,t->ij',hq,np.log(q))/len(q)
    return F,q,g,H

def recursion(z):
    # Two-vertex reservoirs have qj=1+(1/4)t_internal and Rj=1/qj.
    a=4*z*z;wc=weights0[:3];Frec=0;err=0
    for tb in product((-1.,1.),repeat=4):
        qb=1+.25*np.array(tb);R=1/qb;mu=np.prod(qb)/16
        for tau in product((-1.,1.),repeat=4):
            Qv=1+a*np.array(tau)*R;eff=np.array([wc[e]/(Qv[i]*Qv[j]) for e,(i,j) in enumerate(core)])
            Fc=0
            for tc in product((-1.,1.),repeat=3):
                qc=sum(np.prod([eff[e]*tc[e] for e in M]) for M in mmcore)
                Fc+=qc*np.log(qc)/8
                direct=float(likelihood(edges,list(wc)+[.25]*4+list(a),list(tc)+list(tb)+list(tau)))
                err=max(err,abs(direct-np.prod(qb)*np.prod(Qv)*qc))
            Frec+=mu/16*(sum(Qv*np.log(Qv))+np.prod(Qv)*Fc)
    phi=lambda x:.5*((1+x)*np.log1p(x)+(1-x)*np.log1p(-x))
    return 4*phi(.25)+Frec,err

Z0=np.array(list(map(float,z0)));Z1=np.array(list(map(float,z1)));dz=Z1-Z0
rows=[]
for u in [0.,.5,1.]:
    z=(1-u)*Z0+u*Z1;F,q,g,H=reduced(z);Fr,err=recursion(z)
    assert abs(F-Fr)<3e-14 and err<3e-14
    ev=float(np.linalg.eigvalsh(H-kap*np.eye(4))[0]);assert ev>-1e-12
    assert min(g-kap*4*z*z)>-1e-12
    adot=8*z*dz;addot=8*dz*dz
    curvature=float(adot@H@adot+g@addot)
    quartic=float(kap*(adot@adot+(4*z*z)@addot))
    assert curvature>=quartic-1e-12
    km=np.eye(n)/2
    for (i,j),val in zip(edges,np.r_[np.array(list(map(float,zc+zb))),z]):km[i,j]=km[j,i]=val
    eig=np.linalg.eigvalsh(km)
    rows.append(dict(t=u,entropy=float(n*np.log(2)-F),min_kernel_eigenvalue=float(eig[0]),
                     max_kernel_eigenvalue=float(eig[-1]),recursion_error=abs(F-Fr),
                     maximum_atom_factorization_error=err,min_strength_hessian_excess=ev,
                     minus_entropy_curvature=curvature,quartic_curvature_bound=quartic))
Hm=rows[1]['entropy'];gap=Hm-(rows[0]['entropy']+rows[2]['entropy'])/2
qgap=float(8*kap*((np.sum(Z0**4)+np.sum(Z1**4))/2-np.sum(((Z0+Z1)/2)**4)))
assert gap>=qgap>0
OUT['internal_bridge_example']=dict(vertices=n,changing_edges=bridge,direction_inertia=[4,4],
    branch_cavity_max='4/3',branch_kappa='16/15',samples=rows,Jensen_gap=gap,quartic_gap_bound=qgap)
OUT['status']='PASS'
Path(__file__).with_name('results.json').write_text(json.dumps(OUT,indent=2))
print(json.dumps(OUT,indent=2))
