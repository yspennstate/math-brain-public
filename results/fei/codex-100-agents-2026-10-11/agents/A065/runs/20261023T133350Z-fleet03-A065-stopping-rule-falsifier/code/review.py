from pathlib import Path
from fractions import Fraction as F
import json,sys,time
import exact as e

ROOT=Path(__file__).resolve().parents[1]; START=time.perf_counter(); N=0
P=(F(1,2),F(1,8),F(3,8),F(0)); Q=(F(1,64),F(1,64),F(3,4),F(7,32))
PB=((F(1),F(0),F(0),F(0)),(F(0),F(1,4),F(3,4),F(0)))
RL=(F(1,8),F(7,8))
QL=tuple(tuple(Q[z]*(PB[b][z]/(2*P[z]) if P[z] else F(1,2))/RL[b] for z in range(4)) for b in (0,1))

def ck(x,s=''):
 global N
 N+=1
 if not x: raise AssertionError(s)
def eq(a,b,s=''):ck(not e.plus((1,a),(-1,b)),s)
def add(*a):return e.plus(*[(1,z) for z in a])
def sub(a,b):return e.plus((1,a),(-1,b))
def pos(a):
 if not a:return {}
 lo,hi=e.interval(a);ck(lo>0 or hi<0,'strict sign certificate');return a if lo>0 else {}
def maximum(a,b):return b if pos(sub(b,a)) else a
def tensor(a,b):return tuple(x*y for x in a for y in b)

def raw():
 mult=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2)); tt=[]
 for z in range(512):
  s=z&1;u=z>>1&1;v=z>>2&1;y=z>>3;a=y&3;b=y>>2&3;x=y>>4
  h=(-1 if a&1 else 1)*(-1 if x==mult[a][b] else 1)
  tt.append((-1 if (u^v^(y.bit_count()&1))&v else 1)*(h if s else 1))
 return tuple(tt)

def direct(t):
 return tuple(F(sum(v*(-1 if (s&x).bit_count()&1 else 1) for x,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))

def step(t,i,q,sp):
 # Outside four cells are never merged; their within-cell weights are uniform.
 pp=e.stats(t)[0]; cc=[e.child(t,i,b) for b in (0,1)]; pc=[e.stats(c)[0] for c in cc]
 p=tensor(pp,sp);pe=[];qe=[];un=[[],[]];reentry=F(0);rho=F(0)
 for a in range(len(pp)//2):
  a0=e.insert(a,i,0);a1=e.insert(a,i,1);base=pp[a0]+pp[a1]
  if bool(pp[a0]) != bool(pp[a1]):rho+=base
  for z in range(4):
   ep=base*sp[z];eqv=q[4*a0+z]+q[4*a1+z];pe.append(ep);qe.append(eqv)
   if ep:
    reentry+=sum(q[4*aa+z] for aa in (a0,a1) if not pp[aa]*sp[z])
   kk=[pc[b][a]*sp[z]/(2*ep) if ep else F(1,2) for b in (0,1)]
   ck(sum(kk)==1,'fair extension on ALL zero-source rows')
   for b in (0,1):un[b].append(eqv*kk[b])
 r=[sum(u) for u in un];ck(sum(r)==1 and min(r)>0)
 qs=[tuple(x/r[b] for x in un[b]) for b in (0,1)]
 K=e.kl(p,q);E=sub(K,e.kl(pe,qe));O=e.kl((F(1,2),F(1,2)),r)
 Ks=[e.kl(tensor(pc[b],sp),qs[b]) for b in (0,1)]
 eq(K,add(E,O,e.plus((F(1,2),Ks[0]),(F(1,2),Ks[1]))),'global KL chain')
 ck(not E or e.interval(E)[0]>=0,'nonnegative actual erasure')
 ck(not O or e.interval(O)[0]>=0,'nonnegative actual outcome')
 return cc,qs,r,E,O,Ks,reentry,rho

def main():
 mode='pilot' if '--pilot' in sys.argv else 'main'
 t=raw();p,ds,H,M,TC=e.stats(t);ck(p==direct(t),'raw Boolean source Walsh independently checked')
 ck(all(x==F(1,2) for x in ds),'genuine actual root product uniform')
 eq(H,e.constant(F(13,2)));eq(TC,e.constant(F(5,2)))
 cs,lq,rr,oo,ks,ee,z=e.transport(t,0,tuple(F(1,512) for _ in t))
 ck(rr==list(RL));eq(ee,{})
 cps=[e.stats(c)[0] for c in cs]
 counts=[sum(1 for a in range(256) if (0 if cps[0][a] else 1 if cps[1][a]==F(1,16) else 2 if cps[1][a] else 3)==z) for z in range(4)]
 ck(counts==[4,4,192,56],'actual outside-cell degeneracies')
 rg=(F(53,256),F(203,256)); rows=[]; branch_booking=[{},{}]; initial_d=[]; witnessed=[]
 for b in (0,1):
  d=e.log(rg[b]/RL[b]);initial_d.append(d);branch_booking[b]=pos(e.plus((-1,d)))
  for side in (0,1):
   target=cs[b] if side==0 else t; tp=e.stats(target)[0]
   sp=P if side==0 else PB[b]; sq=Q if side==0 else QL[b]
   tq=lq[b] if side==0 else tuple(F(1,512) for _ in t)
   if side==0:
    q=tuple(F(1,256)*Q[z]*(cps[b][a]/(cps[0][a]+cps[1][a]) if (cps[0][a]+cps[1][a])*P[z] else F(1,2))/rg[b] for a in range(256) for z in range(4))
   else:
    q=tuple(F(1,512)*Q[z]*(PB[b][z]/(2*P[z]) if tp[a]*P[z] else F(1,2))/rg[b] for a in range(512) for z in range(4))
   ck(sum(q)==1,'exact actual reference normalized after selector')
   G=e.kl(tensor(tp,sp),q);L=add(e.kl(tp,tq),e.kl(sp,sq));eq(sub(G,L),d,'both compressed orientations agree')
   indices=[2] if mode=='pilot' else list(range(6))
   for j in indices:
    i=j+(2 if side==0 else 3)
    child,qchild,r,Eg,Og,Kg,reentry,rho=step(target,i,q,sp)
    lc,lqc,lr,Ol,lk,El,_=e.transport(target,i,tq)
    ck(child==lc);dc=[];books=[];fullH=[]
    for v in (0,1):
     ck(e.stats(child[v])[0]==direct(child[v]),'EVERY actual child independently direct Walsh checked')
     Lt=add(lk[v],e.kl(sp,sq));dv=sub(Kg[v],Lt);dc.append(dv);books.append(pos(e.plus((-1,dv))))
     fullH.append(add(e.stats(child[v])[2],e.constant(F(13,2) if side==0 else 2+5*b)))
     # A real installation: next kernel uses tensor T globally, not local fiction.
     installed=tensor(lqc[v],sq)
     nxt=step(child[v],0,installed,sp)
     eq(e.kl(tensor(e.stats(child[v])[0],sp),installed),Lt,'actual installed reference cost')
     ck(len(nxt[0])==2,'actual fair continuation after installation')
    avgd=e.plus((F(1,2),dc[0]),(F(1,2),dc[1]))
    eq(sub(avgd,d),add(sub(El,Eg),sub(Ol,Og)),'FULL signed cocycle independently checked')
    defect=sub(El,Eg)
    if side==0:eq(defect,{},'selected-module ordinary erasure correction cancels')
    else:
     expected=(F(0),F(5,8),F(5,8),F(5,8),F(7,64),F(7,64))[j]
     ck(rho==expected,'raw physical spectrum singleton-pair occupancy')
     eq(defect,e.plus((rho,e.log(F(4,3)))),'missing erasure cost = rho log(4/3)')
    booking=pos(sub(e.plus((F(1,2),books[0]),(F(1,2),books[1])),Eg))
    branch_booking[b]=maximum(branch_booking[b],booking)
    if defect:witnessed.append([b,side,j])
    rows.append({'selector_outcome':b,'queried_module':side+1,'ordinary_coordinate':j,'actual_prediction':[str(x) for x in r],'source_zero_to_positive_erased_reference_mass':str(reentry),'rho':str(rho),'erasure_global':e.enc(Eg),'erasure_local':e.enc(El),'erasure_defect':e.enc(defect),'erasure_defect_interval':e.enciv(defect),'outcome_global':e.enc(Og),'outcome_local':e.enc(Ol),'child_signed_defects':[e.enc(x) for x in dc],'child_full_H':[e.enc(x) for x in fullH],'pending_booking':e.enc(booking)})
 eq(branch_booking[0],{},'G branch requires zero extra reserve')
 eq(branch_booking[1],e.log(F(32,29)),'H branch sharp selector-only reserve survives ALL data choices')
 B=e.plus((F(1,2),branch_booking[1]));eq(B,e.plus((F(5,2),e.constant(1)),(-F(1,2),e.log(F(29)))))
 ck(32**4<2*29**4,'strict B<1/8 integer certificate')
 # Worst old quarter and original A remain consumed; no new account.
 residual=sub(e.constant(F(3,4)*23-5),B);ck(e.interval(sub(residual,e.constant(F(97,8))))[0]>0)
 ck(time.perf_counter()-START<55,'frozen maximum runtime')
 out={'status':'PASS','mode':mode,'query_cases':len(rows),'physical_children':2*len(rows),'actual_installation_continuations':2*len(rows),'own_checks':N,'helper_checks':e.COUNT,'total_checks':N+e.COUNT,'seconds':time.perf_counter()-START,'branch_extra_booking':[e.enc(x) for x in branch_booking],'root_extra_booking':e.enc(B),'root_extra_booking_interval':e.enciv(B),'nonzero_erasure_defect_cases':witnessed,'reentry_cases':sum(F(x['source_zero_to_positive_erased_reference_mass'])>0 for x in rows),'rows':rows}
 (ROOT/'out'/('PILOT.json' if mode=='pilot' else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','nonzero_erasure_defect_cases')}))
if __name__=='__main__':main()
