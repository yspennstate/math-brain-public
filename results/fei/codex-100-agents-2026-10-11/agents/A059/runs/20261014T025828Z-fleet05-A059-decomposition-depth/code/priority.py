import sys
sys.dont_write_bytecode=True
import exact as e
from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1]
def L(x):return e.add({},e.cost(Q(1,2)),2*x)
def erasure(a,i):
 out={}
 for s in range(len(a)):
  if not (s>>i)&1:out=e.add(out,e.phi(a[s]**2,a[s|(1<<i)]**2))
 return out
def main(pilot):
 start=time.perf_counter();nodes=0;roots=0
 widths=[(2,1)] if pilot else [(2,1),(3,1),(2,2)]
 pairs=list(itertools.product(e.tables(1),repeat=2))
 for r,s in widths:
  for u0,v0 in (pairs[:2] if pilot else pairs):
   # X, private point A, private point B; labels 0=+1,1=u,2=v.
   c0=tuple(0 if z&1 else 1 if not ((z>>1)&((1<<r)-1)) else 2 if not (z>>(1+r)) else 0 for z in range(1<<(1+r+s)))
   for ar in range(r):
    # Fix X live and ar previous A bits to their surviving point values.
    c=c0
    for _ in range(1+ar):c=e.slice_table(c,0,0)
    a=r-ar;q=Q(1,1<<a);b=Q(1,1<<s)
    # Exhaust every earlier data restriction (including no restriction).
    for u in [u0,e.slice_table(u0,0,0),e.slice_table(u0,0,1)]:
     for v in [v0,e.slice_table(v0,0,0),e.slice_table(v0,0,1)]:
      st=e.state(c,u,v);D,kappa,_,_,_=e.node_check(c,u,v,0,0)
      m=Q(sum(u),len(u));mv=Q(sum(v),len(v));n=1-b+b*mv
      Vu=1-m*m;Vv=1-mv*mv;V=1-n*n;delta=m-n;M=n+q*delta
      ko=e.add(e.cost(1-q),e.cost(1-2*q),-Q(1,2))
      expectedK=e.add(L(q*Vu),ko,b*Vv)
      e.ok(kappa==expectedK,'fine reserve release with reused fallback')
      B=erasure(st['a'],0)
      expectedB=e.add(L(q*Vu+(q-2*q*q)*(V+delta*delta)),e.phi((1-q)**2,q*q),V)
      expectedB=e.add(expectedB,e.phi(M*M,q*q*delta*delta))
      e.ok(B==expectedB,'reused fallback exact Fourier erasure')
      inf=e.influence(st['a'],0);e.ok(inf==q*(1-m*n),'actual point-test influence')
      residual=e.add(D,kappa,-1)
      e.leconst(e.add(residual,L(8*inf),-1),2*inf,'controller residual rate 8+2/ln2')
      e.le(e.add(B,kappa,-1),L(8*inf),'erasure payment')
      nodes+=1
   roots+=1
   if time.perf_counter()-start>170:raise RuntimeError('frozen time budget')
 out={'status':'PASS','roots':roots,'private_controller_nodes':nodes,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-start,'pilot':pilot}
 (ROOT/'out'/('priority_pilot.json' if pilot else 'priority_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main('--pilot' in sys.argv)
