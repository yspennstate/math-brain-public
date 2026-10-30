"""Exact physical singleton/deficit recursions; no Fourier-table enumeration."""
from fractions import Fraction as Q
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1]; O=R/'out'
pilot='--pilot' in sys.argv
ns=[2,4,8] if pilot else [2,4,8,16,32,64]
ps=[Q(1,2),Q(3,4)] if pilot else [Q(1,2),Q(3,4),Q(7,8),Q(15,16),Q(31,32),Q(63,64),Q(127,128)]
spec={'helper':'A041-physical-compressed-singleton-v1','family':'genuine disjoint AND/OR balanced trees and skew chains on equal independent biases','domain':{'arities':ns,'biases':[str(p) for p in ps],'types':['AND-balanced','alternating-balanced','AND-chain','alternating-chain']},'case_count':len(ns)*len(ps)*4,'symmetry':'none; prescribed labelled representatives only, not a class exhaustion','arithmetic':'Fraction actual means, singleton coefficients, influence and exact integer scales; no floating comparisons','memory_estimate_MB':80,'maximum_runtime_seconds':55,'mode':'pilot' if pilot else 'main'}
(O/('COMPRESSED_PILOT_SPEC.json' if pilot else 'COMPRESSED_SPEC.json')).write_bytes((json.dumps(spec,indent=2)+'\n').encode('utf-8'))
start=time.monotonic();checks=0
def ck(t):
 global checks
 assert t;checks+=1
def scale(t):
 t=abs(t);j=0
 if not t:return 0
 while t<=Q(1,2):t*=2;j+=1
 return j
def leaf(p):
 return {'p':p,'w':4*p*(1-p),'I':4*p*(1-p),'c':[(4*p*(1-p),Q(1))],'D':Q(0),'Rt':Q(0),'T':Q(0),'C1':Q(0),'J1tree':Q(0),'Btree':Q(0),'J1':Q(0),'description':'x'}
def node(l,r,op):
 p,q=l['p'],r['p'];w0,w1=l['w'],r['w']
 if op=='AND':newp=p*q;t0,t1=q,p
 else:newp=p+q-p*q;t0,t1=1-q,1-p
 # Actual singleton derivative and influence of AND/OR at (p,q).
 a0,a1=t0,t1
 ss0,ss1=w0*t0*t0,w1*t1*t1
 dg=w0*w1/4
 jg=ss0*scale(t0)+ss1*scale(t1)
 c=[(v,t0*t) for v,t in l['c']]+[(v,t1*t) for v,t in r['c']]
 A=sum((v*t*t for v,t in c),Q(0));J=sum((v*t*t*scale(t) for v,t in c),Q(0))
 Jl,Jr=l['J1'],r['J1'];Al=sum((v*t*t for v,t in l['c']),Q(0));Ar=sum((v*t*t for v,t in r['c']),Q(0))
 # T/ln4 from actual boundary singleton-to-high events.
 tout=t0*t0*(w0-Al)*scale(t0)+t1*t1*(w1-Ar)*scale(t1)
 tin=(a0-t0*t0)*Jl+(a1-t1*t1)*Jr
 C=sum((v*t0*t0*t*t*(scale(t0*t)-scale(t0)-scale(t)) for v,t in l['c']),Q(0))+sum((v*t1*t1*t*t*(scale(t1*t)-scale(t1)-scale(t)) for v,t in r['c']),Q(0))
 T=tout+tin+a0*l['T']+a1*r['T'];Ctot=C+a0*l['C1']+a1*r['C1']
 Jtree=jg+a0*l['J1tree']+a1*r['J1tree'];D=dg+a0*l['D']+a1*r['D'];Rt=a0*l['Rt']+a1*r['Rt']
 B=2*dg-jg+a0*l['Btree']+a1*r['Btree']
 w=4*newp*(1-newp);I=a0*l['I']+a1*r['I']
 ck(I-w==D);ck(T>=0 and C>=0 and B>=0)
 ck(T+J+B==2*D-Rt+Ctot);ck(T==Jtree-J+Ctot)
 return {'p':newp,'w':w,'I':I,'c':c,'D':D,'Rt':Rt,'T':T,'C1':Ctot,'J1tree':Jtree,'Btree':B,'J1':J,'description':op}
def tree(n,p,alt=False,depth=0):
 if n==1:return leaf(p)
 return node(tree(n//2,p,alt,depth+1),tree(n//2,p,alt,depth+1),'OR' if alt and depth%2 else 'AND')
rows=[]
for n in ns:
 for p in ps:
  for typ in spec['domain']['types']:
   if typ.endswith('balanced'):f=tree(n,p,typ.startswith('alternating'))
   else:
    f=leaf(p)
    for d in range(1,n):f=node(f,leaf(p),'OR' if typ.startswith('alternating') and d%2==0 else 'AND')
   denom=2*f['D']-f['Rt'];ratio=f['T']/denom if denom else Q(0)
   rows.append({'n':n,'p':str(p),'type':typ,'T_over_ln4':str(f['T']),'D':str(f['D']),'C1':str(f['C1']),'ratio_to_2Delta_minus_Rtree':str(ratio)})
   if time.monotonic()-start>55:raise RuntimeError('frozen runtime exceeded')
best=max(rows,key=lambda x:Q(x['ratio_to_2Delta_minus_Rtree']))
out={'status':'PASS','cases':len(rows),'assertions':checks,'runtime_seconds':time.monotonic()-start,'max_row':best,'counterexamples_to_unconditional_2ln4':[x for x in rows if Q(x['ratio_to_2Delta_minus_Rtree'])>1],'rows':rows}
(O/('COMPRESSED_PILOT.json' if pilot else 'COMPRESSED.json')).write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
