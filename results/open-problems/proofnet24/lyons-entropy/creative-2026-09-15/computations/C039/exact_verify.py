#!/usr/bin/env python3
"""Standalone standard-library exact verifier and example for C039.

It independently enumerates every parameter-polytope vertex, verifies every
symmetry-derived transport and the sharp dual, and repairs a complex flag's
signed determinantal lift. No LP, numerical arrays, or external package.
"""
from dataclasses import dataclass
import json
from math import lcm
from pathlib import Path
from core import *

HERE=Path(__file__).resolve().parent

@dataclass(frozen=True)
class K:
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def lift(x):return x if isinstance(x,K) else K(x)
    def __add__(self,y):y=K.lift(y);return K(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,y):return self+-K.lift(y)
    def __rsub__(self,y):return K.lift(y)+-self
    def __mul__(self,y):y=K.lift(y);return K(self.a*y.a-3*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def conj(self):return K(self.a,-self.b)
    def norm(self):return self.a*self.a+3*self.b*self.b
    def __truediv__(self,y):
        y=K.lift(y);z=self*y.conj();return K(z.a/y.norm(),z.b/y.norm())
    def __bool__(self):return bool(self.a or self.b)

def determinant(M):
    n=len(M);out=K()
    for pi in permutations(range(n)):
        v=K((-1)**sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n)))
        for i,j in enumerate(pi):v*=M[i][j]
        out+=v
    return out

def example():
    omega=K(F(-1,2),F(1,2));wp=[K(1),omega,omega*omega]
    vs=[[[K(1),K(0)],[K(0),K(1)]],
        [[K(F(3,5)),K(F(4,5))],[K(F(-4,5)),K(F(3,5))]],
        [[K(F(5,13)),omega*F(12,13)],[-omega.conj()*F(12,13),K(F(5,13))]]]
    q=[[wp[(r*k)%3]*vs[r][s][j] for k in range(3) for j in range(2)] for r in range(3) for s in range(2)]
    assert all(sum((q[k][i].conj()*q[k][j] for k in range(6)),K())==K(3*int(i==j)) for i in range(6) for j in range(6))
    # q is sqrt(3) times the unitary frame, so squared d-minors scale by 3^d.
    def amplitude(rows,cols):return determinant([[q[i][j] for j in cols] for i in rows])
    laws=[]
    for cols in [(0,1),(0,1,2),(0,1,3),(0,1,2,3)]:
        law={rows:amplitude(rows,cols).norm()/F(3)**len(cols) for rows in combinations(E,len(cols))}
        assert sum(law.values())==1; laws.append(law)
    overlaps={}
    for r,s in PAIR_COORDS:overlaps[r,s]=sum((vs[r][0][j]*vs[s][0][j].conj() for j in range(2)),K())
    d=tuple(2*overlaps[r,s].norm()-1 for r,s in PAIR_COORDS)
    bargmann=overlaps[0,1]*overlaps[1,2]*overlaps[0,2].conj()
    t=12*bargmann.b;p=d+(t,)
    assert p==(F(-7,25),F(-607,4225),F(-119,169),F(-864,845))
    a,b,c,t=p;assert t*t==3*(1+2*a*b*c-a*a-b*b-c*c)
    actual=[]
    for X in SETS:
        actual.append(laws[0][X] if len(X)==2 else -laws[1][X]-laws[2][X] if len(X)==3 else laws[3][X])
    assert actual==contrast(p)
    signed=[]
    for A,B in AB:
        J=tuple(i for i in E if i not in A+B);T=tuple(i for i in E if i not in B)
        sign=(-1)**sum(i>j for i in A for j in J)
        val=amplitude(A,(0,1))*amplitude(T,(0,1,2,3)).conj()*amplitude(J,(2,3))*sign
        signed.append(val.a/F(81))
    assert matvec(D,signed)==actual
    return p,q,laws,signed

def main():
    data=json.loads((HERE/'certificate.json').read_text())
    tables=[];R=right_inverse();fs=flows()
    assert all(all(v==0 for v in matvec(D,f)) for f in fs)
    basis=[[fs[j][i] for j in FLOW_COLUMNS] for i in range(90)]
    seed_denominators=[]
    for p,record in zip(SEEDS,data['seed_tables']):
        assert tuple(map(F,record['point']))==p
        x=list(map(F,record['weights']));q=list(map(F,record['flow_coefficients']))
        assert min(x)>=0 and sum(x)==1 and matvec(D,x)==contrast(p)
        assert [a+b for a,b in zip(matvec(R,contrast(p)),matvec(basis,q))]==x
        tables.append(x);seed_denominators.append(lcm(*(v.denominator for v in x)))
    vtables=vertex_tables(tables)
    # Every affine coefficient respects every one of the 48 site symmetries.
    for perm in SYMMETRIES:
        for p in [(F(0),)*4]+[tuple(F(int(i==j)) for i in range(4)) for j in range(4)]:
            b=contrast(p);transformed=[F(0)]*50
            for X,v in zip(SETS,b):transformed[SIX[tuple(sorted(perm[i] for i in X))]]=v
            assert transformed==contrast(act_point(p,perm))
    vertices,nonsingular=exact_vertices()
    assert set(vertices)==set(vtables)==set(tuple(map(F,p)) for p in data['vertices'])
    assert len(vertices)==66 and nonsingular==data['nonsingular_four_facet_intersections']
    for p,x in vtables.items():
        assert min(x)>=0 and sum(x)==1 and matvec(D,x)==contrast(p)
    dual=list(map(F,data['transport_cut_dual']))
    assert [dot(dual,column) for column in zip(*C)]==[9,3,3,3,-2]
    assert min(dot(dual,column) for column in zip(*D))>=0
    small=simple_dual()
    assert [18*dot(small,column) for column in zip(*C)]==[9,3,3,3,-2]
    assert set(dot(small,column) for column in zip(*D))=={F(0),F(1),F(2)}
    # The eight extra cuts arise from the site flips, including all-three flip.
    cuts=set()
    for perm in SYMMETRIES:
        y=[F(0)]*50
        for X,v in zip(SETS,dual):y[SIX[tuple(sorted(perm[i] for i in X))]]=v
        assert min(dot(y,column) for column in zip(*D))>=0
        cuts.add(tuple(dot(y,column) for column in zip(*C)))
    expected={(F(9),)+tuple(F(3*e) for e in eps)+(F(sign*2),)
              for eps in product((-1,1),repeat=3) if eps[0]*eps[1]*eps[2]==1 for sign in (-1,1)}
    assert cuts==expected
    p,q,laws,signed=example()
    positive,bary,steps=coupling(p,vtables)
    assert min(positive)>0 and sum(positive)==1 and matvec(D,positive)==contrast(p)
    assert all(sum((w*v[j] for v,w in bary.items()),F(0))==p[j] for j in range(4))
    corrected=flow_coordinates([x-y for x,y in zip(positive,signed)])
    assert [x+y for x,y in zip(signed,matvec(basis,corrected))]==positive
    # Boundary and seam implementation checks, distinct from all-parameter proof.
    test_points=vertices+[(F(0),)*4,p,(F(1),F(0),F(0),F(0)),(F(-1,2),)*3+(F(0),)]
    maxsteps=0
    for v in test_points:
        x,baryv,number=coupling(v,vtables)
        assert matvec(D,x)==contrast(v) and min(x)>=0 and sum(x)==1
        assert all(sum((w*u[j] for u,w in baryv.items()),F(0))==v[j] for j in range(4))
        maxsteps=max(maxsteps,number)
    artifact={'point':list(map(str,p)),
              'sqrt_three_times_unitary':[[[str(x.a),str(x.b)] for x in row] for row in q],
              'signed_exterior':list(map(str,signed)),
              'positive_coupling':list(map(str,positive)),
              'flow_correction':list(map(str,corrected)),
              'barycentric_vertices':[{'point':list(map(str,v)),'weight':str(w)} for v,w in bary.items()],
              'laws':[[{'set':list(X),'mass':str(w)} for X,w in law.items()] for law in laws]}
    (HERE/'complex_example.json').write_text(json.dumps(artifact,indent=2)+'\n')
    summary={'status':'all exact checks passed','parameter_polytope_vertices':66,
             'seed_denominators':seed_denominators,'seed_positive_atom_counts':[sum(x>0 for x in row) for row in tables],
             'all_vertex_marginal_identities':66*50,'symmetry_coefficient_identities':48*5*50,
             'nonsingular_four_constraint_intersections':nonsingular,
             'transport_cut_duals':len(cuts),'verified_nullspace_flows':len(fs),
             'example_point':list(map(str,p)),'example_signed_negative_entries':sum(v<0 for v in signed),
             'example_signed_minimum':str(min(signed)),'example_positive_atoms':sum(v>0 for v in positive),
             'example_positive_minimum':str(min(positive)),
             'example_nonzero_flow_correction_coefficients':sum(v!=0 for v in corrected),
             'example_radial_steps':steps,'interpolation_implementation_points':len(test_points),
             'maximum_interpolation_steps':maxsteps}
    (HERE/'verified_output.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
