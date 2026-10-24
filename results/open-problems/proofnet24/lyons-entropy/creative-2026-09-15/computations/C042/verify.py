#!/usr/bin/env python3
"""Exact certificates for C042. Fraction arithmetic; SymPy only for actual frame minors."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from collections import defaultdict
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
E=tuple(range(6)); ES=set(E)
PAIRS=list(combinations(E,2)); TRIPLES=list(combinations(E,3))
COLS=[(a,b) for a in PAIRS for b in PAIRS if not set(a)&set(b)]
PERMS=list(permutations(range(3)))
V1=((0,1,2),(1,1,1),(2,1,0))
V2=((0,1,2),(1,2,0),(2,0,1))
SEEDS=[
 (V1,[((0,1),(3,4),4,F(1,72)),((0,1),(3,5),8,F(1,24)),
      ((0,1),(4,5),4,F(1,36)),((0,4),(1,3),4,F(1,24)),
      ((0,4),(2,3),8,F(1,72)),((0,5),(1,4),4,F(1,36)),
      ((0,5),(2,3),2,F(1,18))],
  [(2,1,0,5,4,3),(3,4,5,0,1,2)]),
 (V2,[((0,1),(3,4),6,F(1,18)),((0,1),(4,5),6,F(1,36)),
      ((0,4),(2,3),6,F(1,18)),((0,5),(1,4),6,F(1,36))],
  [(1,2,0,5,3,4),(3,4,5,0,1,2)])]

def mapcol(ab,p):return tuple(tuple(sorted(p[i] for i in a)) for a in ab)
def orbit(ab,generators):
 out={ab};todo=[ab]
 while todo:
  a=todo.pop()
  for b in [a[::-1]]+[mapcol(a,p) for p in generators]:
   if b not in out:out.add(b);todo.append(b)
 return out

def laws_from_D(D):
 a={p:F(1,12) if (p[0]<3)==(p[1]<3) else F(D[p[0]][p[1]-3],18) for p in PAIRS}
 h={p:F(0) if (p[0]<3)==(p[1]<3) else F(1,9) for p in PAIRS}
 return a,h

def pair_marginals(x):
 a=defaultdict(F);b=defaultdict(F);h=defaultdict(F);g=defaultdict(F)
 for (A,B),v in x.items():
  J=tuple(sorted(ES-set(A)-set(B)))
  a[A]+=v;b[B]+=v;h[J]+=v
  for j in J:g[tuple(sorted(A+(j,)))]+=v
 return tuple({p:d[p] for p in P} for d,P in [(a,PAIRS),(b,PAIRS),(h,PAIRS),(g,TRIPLES)])

def even_middle(a,h):
 R={p:a[p]+sum(a[b] for b in PAIRS if not set(p)&set(b))-h[p] for p in PAIRS}
 return {m:sum((R[p] for p in combinations(m,2)),F())/2-F(1,2) for m in TRIPLES}

def verify_coupling(D,x):
 assert all(v>=0 for v in x.values()) and sum(x.values(),F())==1
 assert all(x.get((a,b),F())==x.get((b,a),F()) for a,b in COLS)
 a,h=laws_from_D(D);aa,bb,hh,gg=pair_marginals(x)
 assert aa==bb==a and hh==h
 assert gg==even_middle(a,h)
 assert all(gg[m]==gg[tuple(sorted(ES-set(m)))] for m in TRIPLES)
 return gg

vertex_couplings={};seed_data=[]
for D,rows,gens in SEEDS:
 x={}
 for A,B,size,w in rows:
  o=orbit((A,B),gens);assert len(o)==size and not set(x)&o
  for ab in o:x[ab]=w
 verify_coupling(D,x)
 seed_data.append({'D':D,'weights':[{'A':a,'B':b,'w':str(w)} for (a,b),w in sorted(x.items())]})
 for p,q in product(PERMS,repeat=2):
  P=p+tuple(3+j for j in q)
  DD=[[0]*3 for _ in range(3)]
  for i,j in product(range(3),repeat=2):DD[p[i]][q[j]]=D[i][j]
  DD=tuple(tuple(r) for r in DD)
  xx={mapcol(ab,P):w for ab,w in x.items()}
  verify_coupling(DD,xx)
  vertex_couplings.setdefault(DD,xx)
assert len(vertex_couplings)==30
# Independently enumerate all integer capped transportation tables and test the free-edge forest.
def free_cycle(D):
 for cyc in CYCLES:
  if all(0<D[i][j]<2 for i,j,s in cyc):return cyc
 return None
CYCLES=[]
for rr,cc in product(combinations(range(3),2),repeat=2):
 i,k=rr;j,l=cc;CYCLES.append(((i,j,1),(i,l,-1),(k,j,-1),(k,l,1)))
seen=set()
for p,q in product(PERMS,repeat=2):
 if any(p[i]==q[i] for i in range(3)):continue
 cyc=tuple(sorted([(i,p[i],1) for i in range(3)]+[(i,q[i],-1) for i in range(3)]))
 opp=tuple((i,j,-s) for i,j,s in cyc)
 if opp not in seen and cyc not in seen:seen.add(cyc);CYCLES.append(cyc)
assert len(CYCLES)==15
ints=[]
for rows in product([r for r in product(range(3),repeat=3) if sum(r)==3],repeat=3):
 if all(sum(rows[i][j] for i in range(3))==3 for j in range(3)) and free_cycle(rows) is None:ints.append(rows)
assert set(ints)==set(vertex_couplings)

def decompose(D):
 D=tuple(tuple(F(z) for z in r) for r in D)
 assert all(0<=z<=2 for r in D for z in r)
 assert all(sum(r)==3 for r in D) and all(sum(D[i][j] for i in range(3))==3 for j in range(3))
 out=defaultdict(F)
 def rec(d,mass):
  cycle=free_cycle(d)
  if cycle is None:
   assert d in vertex_couplings;out[d]+=mass;return
  ep=min(2-d[i][j] if s>0 else d[i][j] for i,j,s in cycle)
  em=min(d[i][j] if s>0 else 2-d[i][j] for i,j,s in cycle)
  plus=[list(r) for r in d];minus=[list(r) for r in d]
  for i,j,s in cycle:plus[i][j]+=ep*s;minus[i][j]-=em*s
  rec(tuple(map(tuple,plus)),mass*em/(ep+em))
  rec(tuple(map(tuple,minus)),mass*ep/(ep+em))
 rec(D,F(1))
 assert sum(out.values(),F())==1
 assert all(sum(c*d[i][j] for d,c in out.items())==D[i][j] for i,j in product(range(3),repeat=2))
 return dict(out)

def construct(D):
 mixing=decompose(D);x=defaultdict(F)
 for d,c in mixing.items():
  for ab,w in vertex_couplings[d].items():x[ab]+=c*w
 x=dict(x);verify_coupling(D,x);return x,mixing

def construct_with_floor(D):
 D=tuple(tuple(F(z) for z in r) for r in D)
 delta=min(F(1),min(z for r in D for z in r),2-max(z for r in D for z in r))/2
 if not delta:
  x,mixing=construct(D);return x,mixing,delta
 Dprime=tuple(tuple((z-delta)/(1-delta) for z in r) for r in D)
 residual,mixing=construct(Dprime);x=defaultdict(F)
 for ab,w in residual.items():x[ab]+=(1-delta)*w
 for A,B in COLS:
  J=tuple(sorted(ES-set(A)-set(B)))
  if (J[0]<3)==(J[1]<3):continue
  x[(A,B)]+=delta*(F(1,36) if (A[0]<3)==(A[1]<3) else F(1,72))
 x=dict(x);verify_coupling(D,x)
 assert sum(w>0 for w in x.values())==54 and min(w for w in x.values() if w)>=delta/72
 return x,mixing,delta

# Hodge harmonic space: exact rank, complement parity and Vandermonde identity.
L=sp.Matrix([[int(set(p)<=set(m)) for m in TRIPLES] for p in PAIRS])
assert L.rank()==15
MATCHINGS=[((0,1),(2,3),(4,5)),((0,1),(2,4),(3,5)),((0,2),(1,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,4),(2,5))]
QS=[]
for matching in MATCHINGS:
 q={m:0 for m in TRIPLES}
 for bits in product(range(2),repeat=3):q[tuple(sorted(matching[k][bits[k]] for k in range(3)))]=(-1)**sum(bits)
 assert L*sp.Matrix([q[m] for m in TRIPLES])==sp.zeros(15,1)
 assert all(q[m]==-q[tuple(sorted(ES-set(m)))] for m in TRIPLES)
 QS.append(q)
assert sp.Matrix([[q[m] for q in QS] for m in TRIPLES]).rank()==5

def sf(z):
 z=sp.simplify(sp.expand_complex(z));assert z.is_Rational,z
 return F(int(sp.numer(z)),int(sp.denom(z)))
def atomlaw(V,sets):
 return {s:sf(sp.expand_complex(V[list(s),:].det()*sp.conjugate(V[list(s),:].det()))) for s in sets}
def fr_serial(d):return {''.join(map(str,k)):str(v) for k,v in d.items()}

X=sp.Matrix([[2/sp.sqrt(6),0],[-1/sp.sqrt(6),1/sp.sqrt(2)],[-1/sp.sqrt(6),-1/sp.sqrt(2)]])
u=sp.ones(3,1)/sp.sqrt(3)
Us=sp.zeros(6,2);Us[:3,0]=u;Us[3:,1]=u
rotations=[('fully_supported',(sp.eye(2)+sp.I*sp.Matrix([[0,1],[1,0]]))/sp.sqrt(2)),('identity',sp.eye(2)),('real_reflection',sp.diag(1,-1))]
examples=[]
for name,R in rotations:
 Y=X*R;W=X.col_join(Y)/sp.sqrt(2);Z=X.col_join(-Y)/sp.sqrt(2)
 Q=W.row_join(Us).row_join(Z)
 assert sp.simplify(Q.conjugate().T*Q)==sp.eye(6)
 a=atomlaw(W,PAIRS);c=atomlaw(Z,PAIRS);h=atomlaw(Us,PAIRS)
 gu=atomlaw(W.row_join(Us[:,0]),TRIPLES);gv=atomlaw(W.row_join(Us[:,1]),TRIPLES)
 g={m:gu[m]+gv[m] for m in TRIPLES}
 D=tuple(tuple(18*a[(i,3+j)] for j in range(3)) for i in range(3))
 x,mixing,delta=construct_with_floor(D)
 aa,cc,hh,gg=pair_marginals(x)
 assert (aa,cc,hh,gg)==(a,c,h,g)
 assert all(sum(q[m]*g[m] for m in TRIPLES)==0 for q in QS)
 assert all(sf((W*W.conjugate().T)[i,i])==sf((Us*Us.conjugate().T)[i,i])==sf((Z*Z.conjugate().T)[i,i])==F(1,3) for i in E)
 if name=='fully_supported':assert min(a.values())==F(1,72) and len([v for v in a.values() if v])==15
 examples.append({'name':name,'Q':[[str(Q[i,j]) for j in E] for i in E],
  'D':[[str(v) for v in r] for r in D], 'a':fr_serial(a),'c':fr_serial(c),'h':fr_serial(h),'gu':fr_serial(gu),'gv':fr_serial(gv),
  'weights':[{'A':A,'B':B,'w':str(w)} for (A,B),w in sorted(x.items()) if w],
  'residual_mixture':[{'D':d,'coefficient':str(c)} for d,c in mixing.items()],'uniform_mixture_mass':str(delta),'guaranteed_floor':str(delta/72),
  'positive_atoms':sum(w>0 for w in x.values()),'min_positive_weight':str(min(w for w in x.values() if w))})

# A rational generic flag has nonzero Hodge invariant; no universal symmetry cancellation.
v=sp.ones(6,1);w=sp.Matrix([1,2,3,4,5,6])
Q=(sp.eye(6)-2*v*v.T/(v.T*v)[0])*(sp.eye(6)-2*w*w.T/(w.T*w)[0])
Ps=[Q[:,2*k:2*k+2]*Q[:,2*k:2*k+2].T for k in range(3)]
gammas=[]
for q in QS:
 g0=atomlaw(Q[:,:2].row_join(Q[:,2]),TRIPLES)
 g1=atomlaw(Q[:,:2].row_join(Q[:,3]),TRIPLES)
 gamma=sum(q[m]*(g0[m]+g1[m]) for m in TRIPLES);gammas.append(gamma)
 for av,bv,cv in [(2,3,5),(-1,2,4),(3,3,7)]:
  K=av*Ps[0]+bv*Ps[1]+cv*Ps[2]
  value=sum(q[m]*sf(K[list(m),list(m)].det()) for m in TRIPLES)
  assert value==gamma*(av-bv)*(av-cv)*(bv-cv)
assert any(gammas)
cert={'seed_couplings':seed_data,'vertex_count':30,'harmonic_dimension':5,'examples':examples,
 'generic_hodge_example':{'Q':[[str(Q[i,j]) for j in E] for i in E],'gamma_matching_order':MATCHINGS,'gammas':[str(g) for g in gammas]}}
summary={'status':'PASS','seed_orbit_types':[7,4],'vertex_count':30,'harmonic_dimension':5,
 'examples':[{'name':e['name'],'positive_atoms':e['positive_atoms'],'min_positive_weight':e['min_positive_weight']} for e in examples],
 'generic_hodge_gammas':[str(g) for g in gammas]}
(HERE/'certificate.json').write_text(json.dumps(cert,indent=2,default=str)+'\n')
(HERE/'verified_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
