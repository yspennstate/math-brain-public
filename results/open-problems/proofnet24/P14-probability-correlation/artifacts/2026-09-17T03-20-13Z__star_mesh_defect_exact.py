#!/usr/bin/env python3
"""Exact checks for P14 anisotropic star-mesh defect identity and route kills.

No floating point arithmetic.  The symbolic star-mesh identity is checked by a
small exact polynomial dictionary in a,b,c after clearing the single denominator
r=1+a+b+c.  A concrete graph witness is then checked by exhaustive forest
enumeration.
"""
from fractions import Fraction as Q
from itertools import combinations

# --- tiny exact polynomial ring Q[a,b,c] ---------------------------------
# monomial key is (ea,eb,ec)

def Pconst(q):
    q = Q(q)
    return {} if q == 0 else {(0,0,0): q}

def Pvar(i):
    e=[0,0,0]; e[i]=1
    return {tuple(e): Q(1)}

def padd(*ps):
    out={}
    for p in ps:
        for m,v in p.items():
            out[m]=out.get(m,Q(0))+v
            if out[m]==0: del out[m]
    return out

def pneg(p): return {m:-v for m,v in p.items()}
def psub(p,q): return padd(p,pneg(q))

def pmul(p,q):
    out={}
    for m,v in p.items():
        for n,w in q.items():
            k=tuple(m[i]+n[i] for i in range(3))
            out[k]=out.get(k,Q(0))+v*w
            if out[k]==0: del out[k]
    return out

def peq(p,q): return psub(p,q)=={}

def psum(ps):
    out=Pconst(0)
    for p in ps: out=padd(out,p)
    return out

a,b,c=(Pvar(0),Pvar(1),Pvar(2))
one=Pconst(1)
r=padd(one,a,b,c)
ab,ac,bc=pmul(a,b),pmul(a,c),pmul(b,c)
abc=pmul(ab,c)

star_D=pmul(padd(one,a),pmul(padd(one,b),padd(one,c)))
star_P=pmul(padd(one,c),padd(one,a,b))
star_Q=pmul(padd(one,b),padd(one,a,c))
star_S=pmul(padd(one,a),padd(one,b,c))
star_T=r

# With u=ab/r, v=ac/r, w=bc/r, the P,Q,S,T identities have no
# denominator after multiplying the triangle transfer by r.
assert peq(star_P, padd(r,ac,bc))
assert peq(star_Q, padd(r,ab,bc))
assert peq(star_S, padd(r,ab,ac))
assert peq(star_T, r)

# D identity after clearing r:
# r*Star_D = r^2 + r(ab+ac+bc) + (ab*ac+ab*bc+ac*bc) + abc.
rhs_D = padd(
    pmul(r,r),
    pmul(r, psum([ab,ac,bc])),
    psum([pmul(ab,ac),pmul(ab,bc),pmul(ac,bc)]),
    abc,
)
assert peq(pmul(r,star_D), rhs_D)

# Unit specialization a=b=c=1: Star = 4*Triangle(1/4,1/4,1/4) + (1/4)D.
t=Q(1,4)
tri_D=1+3*t+3*t*t
tri_P=1+2*t
tri_T=1
assert (Q(8),Q(6),Q(6),Q(6),Q(4)) == (
    4*tri_D+Q(1,4), 4*tri_P, 4*tri_P, 4*tri_P, 4*tri_T
)

# --- exact unit-subgraph environment obstruction -------------------------
# A positive availability environment reproducing Star/4 exists, but EVERY
# such environment must have positive total pair covariance.  One explicit
# symmetric law is used to verify the transfer representation.
edges3=(0,1,2)
mu={frozenset():Q(1,2)}
for i in edges3: mu[frozenset([i])]=Q(1,12)
for ij in combinations(edges3,2): mu[frozenset(ij)]=Q(1,12)
mu[frozenset(edges3)]=Q(0)
assert sum(mu.values(),Q(0))==1
marg=[sum(p for R,p in mu.items() if i in R) for i in edges3]
pair={(i,j):sum(p for R,p in mu.items() if i in R and j in R)
      for i,j in combinations(edges3,2)}
assert marg == [Q(1,4)]*3
assert list(pair.values()) == [Q(1,12)]*3
sum_pair_cov=sum((pair[i,j]-marg[i]*marg[j] for i,j in combinations(edges3,2)),Q(0))
assert sum_pair_cov==Q(1,16)>0
# Transfer coefficients averaged over available unit terminal edges.
# T=1; P_i=1+availability of the two edges not looping in that partition;
# D=1+sum X_i + sum_{i<j} X_i X_j.
avg_T=Q(1)
avg_P=1+marg[1]+marg[2]
avg_D=1+sum(marg,Q(0))+sum(pair.values(),Q(0))
assert (avg_D,avg_P,avg_T)==(Q(2),Q(3,2),Q(1))

# --- exact exhaustive forest checker for a negative cross-polarization ----

def forest_roots(n, edgelist, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,(u,v) in enumerate(edgelist):
        if (mask>>i)&1:
            ru,rv=find(u),find(v)
            if ru==rv:
                return None
            parent[ru]=rv
    return [find(i) for i in range(n)]

def pair_counts(n, edgelist, eidx, fidx):
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(edgelist)):
        roots=forest_roots(n,edgelist,mask)
        if roots is None: continue
        ie=(mask>>eidx)&1; jf=(mask>>fidx)&1
        Z+=1; Ze+=ie; Zf+=jf; Zef+=ie*jf
    return (Z,Ze,Zf,Zef,Ze*Zf-Z*Zef)

def transfer_stats(n, edgelist, terminals, eidx, fidx):
    x,y,z=terminals
    A=[Q(0) for _ in range(4)]   # triangle t=1/4
    Dv=[Q(0) for _ in range(4)]  # all terminals separated
    coeff={'D':Q(31,16),'P':Q(3,2),'Q':Q(3,2),'S':Q(3,2),'T':Q(1)}
    for mask in range(1<<len(edgelist)):
        roots=forest_roots(n,edgelist,mask)
        if roots is None: continue
        xy=roots[x]==roots[y]; xz=roots[x]==roots[z]; yz=roots[y]==roots[z]
        if xy and xz: st='T'
        elif xy: st='P'
        elif xz: st='Q'
        elif yz: st='S'
        else: st='D'
        ie=(mask>>eidx)&1; jf=(mask>>fidx)&1
        inds=(1,ie,jf,ie*jf)
        for k,on in enumerate(inds):
            if on:
                A[k]+=coeff[st]
                if st=='D': Dv[k]+=1
    return A,Dv

H_edges=[(0,2),(0,3),(0,4),(1,4),(2,5),(3,4),(4,5)]
terminals=(1,3,2)
eidx,fidx=(1,6)  # e=(0,3), f=(4,5)
A4,D4=transfer_stats(6,H_edges,terminals,eidx,fidx)
assert A4==[Q(1349,8),Q(1075,16),Q(603,8),Q(475,16)]
assert D4==[Q(46),Q(13),Q(18),Q(5)]
A0,Ae,Af,Aef=A4; D0,De,Df,Def=D4
delta_A=Ae*Af-A0*Aef
delta_D=De*Df-D0*Def
cross=Ae*Df+De*Af-A0*Def-D0*Aef
assert delta_A==Q(3725,64)
assert delta_D==Q(4)
assert cross==Q(-39,2)

# D is exactly the forest polynomial after contracting the three star spokes,
# i.e. identifying the three terminals.  Verify this on the witness.
T=set(terminals); rep=min(T); groups={}; mapping={}
for vtx in range(6):
    key=rep if vtx in T else vtx
    if key not in groups: groups[key]=len(groups)
    mapping[vtx]=groups[key]
quot_edges=[(mapping[u],mapping[v]) for u,v in H_edges]
quot=pair_counts(len(groups),quot_edges,eidx,fidx)
assert quot[:4]==tuple(int(x) for x in D4)
assert quot[4]==4

# Add the unit apex star and verify the full physical source gap.
apex=6
G_edges=H_edges+[(apex,terminals[0]),(apex,terminals[1]),(apex,terminals[2])]
full=pair_counts(7,G_edges,eidx,fidx)
assert full==(686,272,306,120,912)
# Unit decomposition: Z_G = 4 A + (1/4) D, hence
# Delta_G = 16 Delta_A + Cross + (1/16) Delta_D.
for k in range(4):
    assert Q(full[k]) == 4*A4[k] + Q(1,4)*D4[k]
assert Q(full[4]) == 16*delta_A + cross + Q(1,16)*delta_D == Q(912)

print('P14-STAR-MESH-DEFECT-61: PASS')
print('symbolic_anisotropic_identity=PASS')
print('unit_identity=Star = 4*Triangle(1/4,1/4,1/4) + (1/4)*D')
print('unit_environment_marginals=', [str(x) for x in marg])
print('unit_environment_pair_moments=', {str(k):str(v) for k,v in pair.items()})
print('sum_pair_covariance=', sum_pair_cov)
print('witness_H_edges=', H_edges)
print('witness_terminals=', terminals, 'target_edges=', H_edges[eidx], H_edges[fidx])
print('triangle_stats=', [str(x) for x in A4])
print('contracted_D_stats=', [str(x) for x in D4])
print('delta_triangle=', delta_A, 'cross=', cross, 'delta_D=', delta_D)
print('physical_full_counts=', full)
print('ALL_EXACT_CHECKS_PASSED')
