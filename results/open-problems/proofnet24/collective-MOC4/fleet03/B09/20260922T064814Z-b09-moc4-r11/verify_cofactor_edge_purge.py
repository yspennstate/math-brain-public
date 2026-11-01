#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

S4=list(permutations(range(4))); S3=list(permutations(range(3)))
E=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
BITS=((0,0,0),(0,1,1),(1,0,1),(1,1,0)); BIDX={b:i for i,b in enumerate(BITS)}
PAIR_CLASSES=(
 frozenset((frozenset((0,1)),frozenset((2,3)))),
 frozenset((frozenset((0,2)),frozenset((1,3)))),
 frozenset((frozenset((0,3)),frozenset((1,2)))),
)
PCIDX={pc:i for i,pc in enumerate(PAIR_CLASSES)}

def rho_of(p):
 return tuple(PCIDX[frozenset(frozenset(p[i] for i in S) for S in pc)] for pc in PAIR_CLASSES)
def pm(p,n): return tuple(tuple(F(int(p[i]==j)) for j in range(n)) for i in range(n))
def tr(A): return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))
def mm(A,B):
 BT=tr(B); return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0)) for j in range(len(BT))) for i in range(len(A)))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def sc(c,A): return tuple(tuple(c*A[i][j] for j in range(len(A[0]))) for i in range(len(A)))
EF=tuple(tuple(F(x) for x in row) for row in E); ET=tr(EF)
J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))

def endpoint(sig):
 P=pm(sig,4); D=sc(F(1,4),mm(mm(ET,P),EF)); R=pm(rho_of(sig),3)
 return P,sc(F(1,2),add(R,D)),sc(F(1,2),add(R,sc(F(-1),D)))
def external(tau,rp):
 rt=rho_of(tau)
 P=sc(F(1,3),add(J4,sc(F(-1),pm(tau,4))))
 D=sc(F(1,4),mm(mm(ET,P),EF))
 R=add(sc(F(1,3),pm(rt,3)),sc(F(2,3),pm(rp,3)))
 return P,sc(F(1,2),add(R,D)),sc(F(1,2),add(R,sc(F(-1),D)))
def gauge_B(P,qp,qm,r,c):
 B=tuple(tuple(qm[a][b] if (r[a]^c[b])==0 else qp[a][b] for b in range(3)) for a in range(3))
 return F(1)-P[BIDX[r]][BIDX[c]],B
def cofdata(P,qp,qm,r,c,a,b):
 t2,B=gauge_B(P,qp,qm,r,c)
 rows=[sum(row,F(0)) for row in B]
 cols=[sum(B[i][j] for i in range(3)) for j in range(3)]
 rr=[i for i in range(3) if i!=a]; cc=[j for j in range(3) if j!=b]
 ent=(B[rr[0]][cc[0]],B[rr[0]][cc[1]],B[rr[1]][cc[0]],B[rr[1]][cc[1]])
 return t2-rows[a],t2-cols[b],ent
def poly_prod(x0,x1,y0,y1): return (x0*y0,x0*y1+x1*y0,x1*y1)
def edge_polys(de,dt):
 ae,be,ee=de; a0,b0,e0=dt
 x=poly_prod(a0,ae-a0,b0,be-b0)
 u=poly_prod(e0[0],ee[0]-e0[0],e0[3],ee[3]-e0[3])
 v=poly_prod(e0[1],ee[1]-e0[1],e0[2],ee[2]-e0[2])
 return x,u,v
ZERO=(F(0),F(0),F(0)); LOW_X=(F(0),F(1,3),F(-1,3)); LOW_U=(F(0),F(0),F(1,9))

externals=[]
for tau in S4:
 rt=rho_of(tau)
 for rp in S3:
  if all(rp[i]!=rt[i] for i in range(3)): externals.append((tau,rp))
assert len(externals)==48
zero_counts=[]
for tau,rp in externals:
 Pe,qpe,qme=external(tau,rp); zero_recs=[]
 for r in BITS:
  for c in BITS:
   for a in range(3):
    for b in range(3):
     de=cofdata(Pe,qpe,qme,r,c,a,b); ae,be,ee=de
     if ae*be>0 and ee[0]*ee[3]==0 and ee[1]*ee[2]==0: zero_recs.append((r,c,a,b,de))
 assert len(zero_recs)==24; zero_counts.append(len(zero_recs))
 for sig in S4:
  P0,qp0,qm0=endpoint(sig); found=False
  for r,c,a,b,de in zero_recs:
   x,u,v=edge_polys(de,cofdata(P0,qp0,qm0,r,c,a,b))
   if u==ZERO and v==ZERO: found=True; break
  if sig==tau: assert not found
  else: assert found,(tau,rp,sig)
 P0,qp0,qm0=endpoint(tau); got_lower=got_upper=False
 for r in BITS:
  for c in BITS:
   for a in range(3):
    for b in range(3):
     x,u,v=edge_polys(cofdata(Pe,qpe,qme,r,c,a,b),cofdata(P0,qp0,qm0,r,c,a,b))
     if x==LOW_X and sorted((u,v))==sorted((ZERO,LOW_U)): got_lower=True
     if x==LOW_U and sorted((u,v))==sorted((ZERO,LOW_X)): got_upper=True
 assert got_lower and got_upper,(tau,rp)

A=((4,2),(-2,3),(0,-2),(-3,-2)); BS=((-4,-4),(0,-2),(1,2),(-3,3)); ETA=(1,-1)
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
def fval(sig):
 z=(1,0)
 for i in range(4): z=cmul(z,cadd(A[i],BS[sig[i]]))
 return F(cmul(ETA,z)[0])
f={s:fval(s) for s in S4}
def extval(tau,rp):
 rt=rho_of(tau)
 B1=sum((f[s] for s in S4 if rho_of(s)==rt),F(0))/4
 B2=sum((f[s] for s in S4 if rho_of(s)==rp),F(0))/4
 return F(2,3)*(B1+B2)-F(1,3)*f[tau]
vals=[(extval(t,r),t,r) for t,r in externals]
Emax,topt,ropt=max(vals); M=max(f.values())
assert M==240 and Emax==F(740,3) and f[topt]==-1538
rt=rho_of(topt)
B1=sum((f[s] for s in S4 if rho_of(s)==rt),F(0))/4
B2=sum((f[s] for s in S4 if rho_of(s)==ropt),F(0))/4
safe=F(1,2)*(B1+B2)
assert F(3,4)*Emax+F(1,4)*f[topt]==safe and safe<=M

print('PASS MOC4-SPINOR-COFACTOR-EDGE-PURGE-v1')
print('external_vertices =',len(externals))
print('zero_rhs_cofactor_violations_per_external =',min(zero_counts))
print('external_weyl_edges_checked =',len(externals)*len(S4))
print('forbidden_open_edges_sigma_ne_tau =',len(externals)*(len(S4)-1))
print('exceptional_tau_edges =',len(externals))
print('tau_edge_cofactor_compatible_lambda = {0, 3/4}')
print('tau_edge_lambda_3_4_functional = 1/2(B_rho_tau+B_rho_prime), hence Weyl-safe')
print('structured_endpoint_max =',M)
print('structured_unique_external_max =',Emax)
print('structured_external_tau_endpoint =',f[topt])
print('structured_tau_edge_safe_point =',safe)
