"""Retained-marker exposure, exact signed spectra and same original bank."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import importlib.util,json,time,argparse,hashlib
R=Path(__file__).resolve().parents[1]
source=R.parents[0]/'20261023T001357Z-account03-A031-convolution-identity/code/check_nonfair.py'
sp=importlib.util.spec_from_file_location('signed_prior',source);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
T=m.Triangle; ck=m.ck;add=m.add;sub=m.sub;mul=m.mul;saved=m.saved
def avg(xs):return mul(add(*xs),F(1,len(xs)))
def fifth(t,h):
 by=t.row(h,0)[2];old=t.full_ce(h,lambda S:t.lift(h,0,S))[0]
 incoming=lambda S:t.p(h,S)+t.p(h,S|1)
 fresh=[];inherited=[];children=[]
 for u in [0,1]:
  hh=h+((0,u),);ce,ghost=t.full_ce(hh,lambda S:t.lift(hh,2,S));ci,gi=t.full_ce(hh,incoming)
  fresh.append(ce);inherited.append(ci)
  for mult,S in t.labels(hh):ck(t.amp(hh,S)==t.amp(h,S)+(-1)**u*t.amp(h,S|1))
  children.append({'a_outcome':u,'CE_full':saved(ce),'ghost_mass':str(ghost),'incoming_ghost_mass':str(gi)})
 rho=sub((F(1),F(1)),by);delta=sub(avg(fresh),avg(inherited));net=sub(add(by,avg(fresh)),old)
 m.zero(sub(net,sub(delta,rho)))
 # Actual marker query refund is fair and is used ONCE here, not at earlier nonfair queries.
 ja=t.js(h,0);bc=avg([t.row(h+((0,u),),2)[2] for u in [0,1]])
 m.zero(sub(net,sub(sub(by,ja),bc)))
 ck(net[0]<=by[1]);s,tbit=dict(h)[3],dict(h)[1]
 if (s,tbit)==(1,1):
  ck(old==(F(1),F(1)));ck(by==(F(0),F(0)))
  for z in fresh:ck(z==(F(1),F(1)))
 return by,old,add(by,avg(fresh)),{'history':list(h),'net':saved(net),'Delta':saved(delta),'rho':saved(rho),'B_a':saved(by),'children':children}
def case(L):
 t=T(L);root=[t.row((),i) for i in [0,1,2,3,4,4+L]]
 M=add(*(mul(z[1],1 if j<4 else L) for j,z in enumerate(root)))
 q=F(1,1<<L);I=root[3][0]+L*(root[4][0]+root[5][0]);ck(I==(2-2*q+q*q)/8+2*L*q*(3-q)/8)
 Bx=root[3][2];Bb=[];old=[];private=[];frontier=[];marker=[];nodes=[];AB=[]
 for s in [0,1]:
  Bb.append(t.row(((3,s),),1)[2])
  for b in [0,1]:
   h=((3,s),(1,b));old.append(t.full_ce(h,lambda S:t.lift(h,0,S))[0]);private.append(t.row(h,4)[2])
   second=[]
   for y in [0,1]:
    hy=h+((4,y),);second.append(t.row(hy,L+4)[2])
    for z in [0,1]:
     hz=hy+((L+4,z),);ba,ce,bill,node=fifth(t,hz);frontier.append(ce);marker.append(bill);nodes.append(node);AB.append(ba)
   private.append(avg(second))
 D=add(M,Bx,avg(Bb));bill2=add(D,avg(old));private_total=mul(add(*private),F(1,4))
 bill4=add(D,private_total,avg(frontier));bill5=add(D,private_total,avg(marker));spare=sub((17*I,17*I),bill2);spare5=sub((17*I,17*I),bill5)
 ck(spare[0]>F(7,8));ck(spare5[0]>F(1,8));ck(avg(AB)[1]<=F(3,4))
 # Overlap identities certify formulas; analytic nonnegativity, not interval signs, gives the all-L comparison.
 ck(sub(bill4,bill2)[0]<=0);ck(sub(bill5,bill4)[0]<=F(3,4))
 # Same original bank, not a renewed post-y/z influence.
 return {'L':L,'I_private_original':str(I),'original_debits':saved(D),'second_reset_bill':saved(bill2),'second_reset_spare':saved(spare),'fourth_bill':saved(bill4),'marker_exposure_bill':saved(bill5),'marker_exposure_spare':saved(spare5),'average_B_a':saved(avg(AB)),'nodes':nodes}
def tail():
 # C_infinity = M(h)+B_x(h)+3/2, retaining both constant-child Fair_a bills.
 cinf=add((F(39,16),F(39,16)),m.logs([(F(1,4),F(10)),(F(9,16),F(10,9))]))
 poly=lambda L:2*L*L+124*L+3270
 spare=sub((F(17,4),F(17,4)),add(cinf,(F(4*poly(20)+17,4*(1<<20)),)*2))
 ck(poly(20)==6550);ck(spare[0]>F(7,8))
 # Positive polynomial certifies P(L)/2^L decreases throughout L>=20.
 coeff=[3270,124,2]
 shifted=[sum(coeff[k]*__import__('math').comb(k,j) for k in range(j,3)) for j in range(3)]
 ck([2*coeff[j]-shifted[j] for j in range(3)]==[3144,120,2])
 return {'C_infinity':saved(cinf),'P':'2L^2+124L+3270','L0':20,'P_L0':6550,'tail_original_spare_lower':str(spare[0]),'comparison':'strictly greater than7/8','monotonicity_polynomial':'2P(L)-P(L+1)=2L^2+120L+3144>0'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');a=ap.parse_args();start=time.monotonic()
 domain=[1,2,3] if a.pilot else list(range(1,21))+[32,64];rows=[]
 for L in domain:
  rows.append(case(L));ck(time.monotonic()-start<(55 if a.pilot else 180))
  (R/'out/CHECKPOINT.json').write_text(json.dumps({'cases':rows},indent=2)+'\n',encoding='utf-8')
 cert=tail();result={'cases':rows,'tail':cert,'checks':m.CHECKS,'seconds':time.monotonic()-start,'prior_helper_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
 name='PILOT.json' if a.pilot else 'CHECK.json';(R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'output':name,'widths':len(rows),'checks':m.CHECKS,'seconds':result['seconds']}))
