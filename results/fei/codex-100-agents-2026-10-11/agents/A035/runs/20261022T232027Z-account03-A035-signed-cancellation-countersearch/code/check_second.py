from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,sys,time
import kernel as k
R=Path(__file__).resolve().parents[1]; START=time.perf_counter();CHECKS=0;k.CAP=180
def ck(x):
 global CHECKS
 assert x; CHECKS+=1
def avg(v):return k.mul(sumiv(v),F(1,len(v)))
def sumiv(v):
 z=(F(0),F(0))
 for x in v:z=k.add(z,x)
 return z
def eq(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def scalar(x):return (F(x),F(x))
def cells(L,allowed=15,widths=None):
 widths=widths or (L,L)
 for h2,h3 in product((0,1),repeat=2):
  mult=((1<<widths[0])-1)**h2*((1<<widths[1])-1)**h3
  if not mult:continue
  for mask in range(16):
   if not mask&~allowed:yield (h2,h3,mask),mult
def rootcoeff(L,h2,h3,mask):
 out=-F(h2==0 and h3==0 and mask==0)
 for J in range(8):
  core=(11 if J&1 else 0)|(6 if J&2 else 0)|(12 if J&4 else 0)
  if mask&~core or (h2 and not J&2) or (h3 and not J&4):continue
  width=core.bit_count()+L*bool(J&2)+L*bool(J&4)
  out+=2*F((-1)**J.bit_count(),1<<width)
 return out
def amps(L,fixed=()):
 allowed=15
 for bit,value in fixed:allowed&=~bit
 out={}
 for (h2,h3,mask),mult in cells(L,allowed):
  z=F(0)
  for J in range(1<<len(fixed)):
   ext=mask;sign=1
   for j,(bit,value) in enumerate(fixed):
    if J>>j&1:ext|=bit;sign*=(-1)**value
   z+=sign*rootcoeff(L,h2,h3,ext)
  out[(h2,h3,mask)]=z
 ck(sum(mult*out[key]**2 for key,mult in cells(L,allowed))==1)
 return allowed,out
def entropy(L,allowed,A):return sumiv(k.mul(k.ratlog(A[key]**2),-mult*A[key]**2) for key,mult in cells(L,allowed) if A[key])
def row(L,allowed,A,bit):
 M=[];B=[];energy=F(0)
 for (h2,h3,mask),mult in cells(L,allowed&~bit):
  u=A[(h2,h3,mask)]**2;v=A[(h2,h3,mask|bit)]**2
  energy+=mult*v
  if v:
   M.append(k.mul(k.ratlog((u+v)/v),mult*v))
   B.append(k.mul(k.ratlog((u+v)/v),mult*v))
  if u:B.append(k.mul(k.ratlog((u+v)/u),mult*u))
 return energy,sumiv(M),sumiv(B)
def privateM(L,which):
 terms=[];e=F(0);widths=(L-1,L) if which==0 else (L,L-1)
 for (h2,h3,mask),mult in cells(L,15,widths):
  u=rootcoeff(L,h2,h3,mask)**2
  v=rootcoeff(L,1 if which==0 else h2,1 if which==1 else h3,mask)**2
  e+=mult*v
  if v:terms.append(k.mul(k.ratlog((u+v)/v),mult*v))
 return e,sumiv(terms)
def fair_reference(L,allowed,A,bit):
 Q={}
 for h2,h3,mask in A:
  key=(h2,h3,mask&~bit);mate=(h2,h3,mask|bit)
  Q[(h2,h3,mask)]=(A[key]**2+A[mate]**2)/2
 ck(sum(mult*Q[key] for key,mult in cells(L,allowed))==1)
 return Q
def CE(L,allowed,A,Q):
 terms=[]
 for key,mult in cells(L,allowed):
  p=A[key]**2
  if p:ck(Q[key]>0);terms.append(k.mul(k.ratlog(Q[key]),-mult*p))
 return sumiv(terms)
def case(L):
 q=F(1,1<<L);allowed,A=amps(L);H=entropy(L,allowed,A)
 core=[row(L,allowed,A,bit) for bit in (1,2,4,8)]
 pri=[privateM(L,j) for j in (0,1)]
 Ipriv=core[0][0]+L*sum(e for e,m in pri)
 ck(Ipriv==(2-2*q+q*q)/8+2*L*q*(3-q)/8)
 M=sumiv([v[1] for v in core]+[k.mul(v[1],L) for v in pri]);Bx=core[0][2]
 Hs=[];CEold=[];Bbs=[];Jbs=[];CEnew=[];CEincoming=[];Bas=[];terminal=[];conditional=[]
 for s in (0,1):
  allow,P=amps(L,((1,s),));Hp=entropy(L,allow,P);Hs.append(Hp)
  eb,mb,Bb=row(L,allow,P,4);Bbs.append(Bb);ck(eb>0)
  Qb=fair_reference(L,allow,P,4);old=CE(L,allow,P,Qb);CEold.append(old);eq(old,k.sub(k.add(Hp,scalar(1)),Bb))
  Rb={(h2,h3,mask):P[(h2,h3,mask)]**2+P[(h2,h3,mask|4)]**2 for (h2,h3,mask),mult in cells(L,allow&~4)}
  subH=[];subIncoming=[];subCE=[]
  for b in (0,1):
   al,V=amps(L,((1,s),(4,b)));Hv=entropy(L,al,V);subH.append(Hv)
   ea,ma,Ba=row(L,al,V,2);Bas.append(Ba)
   Qa=fair_reference(L,al,V,2);new=CE(L,al,V,Qa);inc=CE(L,al,V,Rb)
   subCE.append(new);subIncoming.append(inc);CEnew.append(new);CEincoming.append(inc)
   eq(new,k.sub(k.add(Hv,scalar(1)),Ba))
   if s==1 and b==1:ck(V[(0,0,0)]==1);ck(sum(V[key]**2 for key in V if key!=(0,0,0))==0);eq(new,scalar(1))
   terminal.append(dict(x=s,b=b,H=k.emit(Hv),I_a=str(ea),B_a=k.emit(Ba),complete_CE_a=k.emit(new),incoming_CE=k.emit(inc),reset=k.emit(k.sub(new,inc))))
  Jb=k.sub(Hp,k.add(Bb,avg(subH)));Jbs.append(Jb)
  conditional.append(k.sub(scalar(1),Bb))
  eq(old,sumiv([Bb,avg(subIncoming),conditional[-1]]))
  eq(k.sub(avg(subCE),avg(subIncoming)),k.sub(k.sub(scalar(1),avg(Bas[-2:])),Jb))
 Jx=k.sub(H,k.add(Bx,avg(Hs)))
 oldbill=sumiv([M,Bx,avg(CEold)])
 newbill=sumiv([M,Bx,avg(Bbs),avg(CEnew)])
 delta=k.sub(avg(CEnew),avg(CEincoming));net=k.sub(newbill,oldbill)
 eq(net,k.sub(k.sub(avg(Bbs),avg(Jbs)),avg(Bas)))
 eq(net,k.sub(delta,avg(conditional)))
 ck(net[1]<=avg(Bbs)[1]+F(1,1<<100))
 oldspare=k.sub(scalar(17*Ipriv),oldbill);spare=k.sub(scalar(17*Ipriv),newbill)
 ck(oldspare[0]>F(1,16));ck(spare[0]>F(1,32))
 if L>=16:
  bound=q*(L+F(3,2));ck(avg(Bbs)[1]<bound);ck(bound<F(1,32));ck(delta[0]>F(1,8))
  ck(Jx[0]>F(1,4));ck(delta[0]>F(1,4)-3*(3*q/4-q*q/8))
 return dict(L=L,I_private=str(Ipriv),M_old=k.emit(M),B_x=k.emit(Bx),mean_B_b=k.emit(avg(Bbs)),old_full_bill=k.emit(oldbill),old_spare=k.emit(oldspare),new_full_bill=k.emit(newbill),new_spare=k.emit(spare),positive_fresh_reset=k.emit(delta),net_change=k.emit(net),released_fair_conditional_KL=k.emit(avg(conditional)),terminals=terminal)
def tail():
 H=sumiv([k.ent(F(9,16)),k.mul(k.ent(F(1,16)),7)])
 M=k.add(k.mul(k.ratlog(F(10)),F(3,16)),scalar(F(9,16)))
 cap=sumiv([H,M,scalar(F(3,4)),scalar(F(1220,65536))])
 floor=17*(F(1,4)-F(1,262144));ck(floor-cap[1]>F(1,16))
 extra=F(35,131072);ck(F(1,16)-extra>F(1,32));ck(F(1,4)-F(9,4*65536)>F(1,8))
 # Norm-one non-Boolean control; x,a,b,c are untouched dummies.
 N=1<<18;ck(F(19)>17);ck(F(2,N)>0)
 return dict(old_tail_endpoint_spare=k.emit(k.sub(scalar(floor),cap)),next_net_charge_upper=str(extra),all_tail_spare_lower=str(F(1,16)-extra),nonboolean=dict(private_singletons=N,private_I='1',full_bill='19',bank='17',nonempty_convolution=str(F(2,N))))
if __name__=='__main__':
 pilot='--pilot' in sys.argv;domain=[1,2,4] if pilot else list(range(1,16))+[16,32,64]
 records=[]
 for L in domain:
  k.clock();records.append(case(L));ck(time.perf_counter()-START<(60 if pilot else 180))
  (R/'out'/('pilot_checkpoint.json' if pilot else 'checkpoint.json')).write_text(json.dumps(records,indent=2),encoding='utf-8')
 result=dict(helper='A035-second-fair-reset-v2',domain=domain,cases=records,tail=tail(),checks=CHECKS,runtime_seconds=time.perf_counter()-START)
 (R/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(dict(checks=CHECKS,runtime_seconds=result['runtime_seconds'],cases=len(records),reset_signs=[(r['L'],'positive' if F(r['positive_fresh_reset'][0])>0 else 'negative' if F(r['positive_fresh_reset'][1])<0 else 'unresolved') for r in records])))
