from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from math import comb
import time,json,sys
import exact as e
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();N=0
COUNTS={'raw_fourier_atoms':0,'cell_histories':0,'cell_transitions':0,'positive_reference_source_zero_rows':0,'compact_prefixes':0,'compact_binomial_cells':0}
def ck(x,s=''):
 global N
 N+=1
 if not x:raise AssertionError(s)
def eq(a,b,s=''):ck(not e.plus((1,a),(-1,b)),s)
def ge(a,b,s=''):
 d=e.plus((1,a),(-1,b));ck(not d or e.interval(d)[0]>=0,s)
def direct(t):
 out=[]
 for s in range(len(t)):
  a=sum(v*(-1 if (s&x).bit_count()&1 else 1) for x,v in enumerate(t));out.append(F(a*a,len(t)**2));COUNTS['raw_fourier_atoms']+=1
 return tuple(out)
def raw_module():
 mult=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2));t=[]
 for z in range(512):
  s=z&1;u=z>>1&1;v=z>>2&1;y=z>>3;a=y&3;b=y>>2&3;x=y>>4
  h=(-1 if a&1 else 1)*(-1 if x==mult[a][b] else 1)
  phase=((u^v^(y.bit_count()&1))&v)
  t.append((-1 if phase else 1)*(h if s else 1))
 t=tuple(t);p=direct(t);pp,ds,H,M,TC=e.stats(t);ck(p==pp,'all raw root Walsh coefficients independently agree')
 ck(all(F(sum(t[x]!=t[x^(1<<i)] for x in range(512)),512)==F(1,2) for i in range(9)),'all original physical influences half')
 eq(H,e.constant(F(13,2)));eq(TC,e.constant(F(5,2)))
 cs,qs,r,O,Ks,E,ref=e.transport(t,0,tuple(F(1,512) for _ in t));ck(r==[F(1,8),F(7,8)]);eq(E,{})
 pc=[direct(c) for c in cs]
 for b in (0,1):ck(pc[b]==e.stats(cs[b])[0],'both full physical child spectra replayed')
 labels=[]
 for j in range(256):
  ck(not(pc[0][j] and pc[1][j]),'disjoint actual child spectra')
  labels.append(0 if pc[0][j] else 1 if pc[1][j]==F(1,16) else 2 if pc[1][j] else 3)
 ck([labels.count(i) for i in range(4)]==[4,4,192,56],'all actual spectral cell counts')
 ps=[sum((pc[0][j]+pc[1][j])/2 for j in range(256) if labels[j]==i) for i in range(4)]
 q0=tuple(F(labels.count(i),256) for i in range(4));ck(ps==list(P0) and q0==Q0,'physical cell laws derived from raw Boolean source')
 for b in (0,1):
  q=tuple(sum(qs[b][j] for j in range(256) if labels[j]==i) for i in range(4))
  ck(q==QL[b],'raw reference descendants including all zero-source mass')
 eq(Ks[0],e.constant(3));eq(Ks[1],e.plus((1,e.log(F(7))),(-1,e.constant(2))))
 return {'dimension':9,'raw_H':e.enc(H),'raw_I':'9/2','initial_K':e.enc(TC),'reference_predictions':[str(x) for x in r],'cell_counts':[4,4,192,56]}
P0=(F(1,2),F(1,8),F(3,8),F());Q0=(F(1,64),F(1,64),F(48,64),F(14,64))
PB=((F(1),F(),F(),F()),(F(),F(1,4),F(3,4),F()))
RR=(F(1,8),F(7,8));ALPHA=F(25,32)
QL=tuple(tuple(Q0[j]*(F(1) if (j==0)==(b==0) else F())/RR[b] if j!=3 else Q0[j]/(2*RR[b]) for j in range(4)) for b in (0,1))
C=e.plus((1,e.constant(2)),(-F(1,2),e.log(F(7))))
def tensor(laws,states):return tuple(__import__('functools').reduce(lambda x,y:x*y,(laws[j][s[j]] for j in range(len(laws))),F(1)) for s in states)
def w(L,t,k):return F(32**L-25**L+25**(L-t)*49**(t-k),32**L)
def cells(L):
 states=list(product(range(4),repeat=L));root=tensor([P0]*L,states);qroot=tensor([Q0]*L,states);depths=[[] for _ in range(L+1)];witness={}
 eq(e.kl(root,qroot),e.constant(F(5*L,2)),'full fixed original product root KL')
 def visit(bits,p,q,rpath,cost):
  COUNTS['cell_histories']+=1;t=len(bits);k=bits.count(0);phys=F(1,2**t);rp=RR[0]**k*RR[1]**(t-k)
  ck(rpath==w(L,t,k)/2**t,'global latent-sector joint likelihood')
  tq=tensor([QL[b] for b in bits]+[Q0]*(L-t),states);K=e.kl(p,q);KT=e.kl(p,tq);d=e.log(rpath/rp)
  for a,x,y in zip(p,q,tq):
   if a:ck(x==y*rp/rpath,'actual-support likelihood correction')
   elif x:COUNTS['positive_reference_source_zero_rows']+=1
  eq(K,e.plus((1,KT),(1,d)),'complete terminal actual-K correction')
  H=e.constant(F(13*L+t,2)-5*k)
  depths[t].append((phys,K,KT,d,cost,H,rpath))
  if L==2 and bits==(0,):
   mass=sum(q[j] for j,s in enumerate(states) if s[0] in (1,2) and s[1]==3)
   ck(mass==F(343,848),'positive global reference mass where tensor reference vanishes')
   ck(all(tq[j]==0 for j,s in enumerate(states) if s[0] in (1,2) and s[1]==3),'forward KL support mismatch')
   ck(rpath==F(53,256),'actual first outcome differs from tensor1/8')
   witness.update({'global_G_prediction':str(rpath),'tensor_G_prediction':'1/8','global_positive_mass_on_tensor_zero':str(mass),'forward_reference_KL':'infinity','actual_source_mass_there':'0','finite_actual_source_correction':e.enc(d)})
  if L==2 and bits==(1,):ck(e.interval(d)[1]<0,'signed correction must retain negative paths')
  if t==L:return
  COUNTS['cell_transitions']+=1
  pcs=[tensor([PB[b] for b in bits]+[PB[nextb]]+[P0]*(L-t-1),states) for nextb in (0,1)]
  un=[];reach=[]
  for b in (0,1):
   u=tuple(q[j]*(pcs[b][j]/(2*p[j]) if p[j] else F(1,2)) for j in range(len(p)));un.append(u);reach.append(sum(u))
  ck(sum(reach)==1 and min(reach)>0,'all global physical predictions normalized')
  qs=[tuple(x/reach[b] for x in un[b]) for b in (0,1)];O=e.kl((F(1,2),F(1,2)),reach)
  eq(K,e.plus((1,O),(F(1,2),e.kl(pcs[0],qs[0])),(F(1,2),e.kl(pcs[1],qs[1]))),'actual E=0 edge account')
  for b in (0,1):visit(bits+(b,),pcs[b],qs[b],rpath*reach[b],e.plus((1,cost),(1,O)))
 visit((),root,qroot,F(1),{})
 records=[]
 for t,rows in enumerate(depths):
  avg=lambda col:e.plus(*[(z[0],z[col]) for z in rows])
  K,KT,d,cost,H=[avg(j) for j in range(1,6)]
  joint=e.plus(*[(-z[0],e.log(2**t*z[6])) for z in rows])
  eq(cost,joint,'conditional global outcome costs equal true joint KL')
  eq(d,e.plus((t,C),(-1,cost)),'growing expected omitted cost exact')
  eq(K,e.plus((1,e.constant(F(5*L,2))),(-1,cost)),'same original bank no renewal')
  eq(KT,e.plus((1,e.constant(F(5*L,2))),(-t,C)),'naive tensor descendant bill')
  eq(H,e.constant(F(13*L,2)-2*t),'FULL terminal entropy retained')
  eq(e.plus((1,H),(1,K),(1,cost)),e.plus((1,H),(1,e.constant(F(5*L,2)))),'full terminal cross-entropy exact bank')
  records.append({'t':t,'global_outcome_KL':e.enc(cost),'expected_omitted_terminal_KL':e.enc(d),'omitted_interval':e.enciv(d),'full_mean_H':e.enc(H),'actual_mean_K':e.enc(K),'naive_tensor_mean_K':e.enc(KT)})
 return {'L':L,'depth_records':records,'negative_control':witness}
# Independent direct rational-log enclosure: no factorization of large integers.
GRID=1<<112
def rnd(a,b):return F((a*GRID).__floor__(),GRID),F((b*GRID).__ceil__(),GRID)
@lru_cache(None)
def ln_m(m):
 z=(m-1)/(m+1);ck(0<=z<=F(1,3),'atanh normalization');power=z;total=F()
 for j in range(40):total+=power/F(2*j+1);power*=z*z
 return rnd(2*total,2*total+2*power/(81*(1-z*z)))
L2=ln_m(F(2))
@lru_cache(None)
def logiv(q):
 ck(q>0,'rational log domain');shift=q.numerator.bit_length()-q.denominator.bit_length();base=F(2)**shift
 if q<base:shift-=1;base/=2
 if q>=2*base:shift+=1;base*=2
 m=q/base;a,b=ln_m(m);return rnd(shift+a/L2[1],shift+b/L2[0])
def compact(L,ts):
 c0,c1=logiv(F(16,7));c0/=2;c1/=2;records=[]
 for t in ts:
  COUNTS['compact_prefixes']+=1;lo=hi=F()
  for k in range(t+1):
   COUNTS['compact_binomial_cells']+=1;a,b=logiv(w(L,t,k));weight=F(comb(t,k),2**t);lo-=weight*b;hi-=weight*a
  dl=t*c0-hi;dh=t*c1-lo
  ck(lo>=0 and hi<=-logiv(1-ALPHA**L)[0],'nonnegative and fair-sector rigorous outcome bound')
  if L>=3:ck(hi<1,'uniform bounded actual global outcome cost')
  if L>=4 and t>=4:ck(dl>F(t,4),'linear omitted actual terminal cost')
  if L==1:ck(dl<=0<=dh,'no defect in one isolated module')
  # Same original owner, prior quarter and original A book, no new debit.
  S=F(23*L,2);A=F(5*L,2);ck(F(3,4)*S-A==F(49*L,8) and F(49*L,8)>S/2,'same original bank balance with old quarter')
  records.append({'t':t,'global_outcome_KL_interval':[str(lo),str(hi)],'omitted_terminal_KL_interval':[str(dl),str(dh)],'full_mean_H':str(F(13*L,2)-2*t),'original_A':str(A),'owner_after_old_quarter_and_A':str(F(49*L,8))})
 return {'L':L,'prefixes':records}
def main():
 mode='pilot' if '--pilot' in sys.argv else 'main';Ls=[1,2] if mode=='pilot' else [1,2,3,4];CL=[1,2,4] if mode=='pilot' else [1,2,3,4,8,16,32,64]
 raw=raw_module();cell=[]
 for L in Ls:cell.append(cells(L));ck(time.perf_counter()-START<55,'cell runtime guard')
 comp=[]
 for L in CL:
  ts=list(range(L+1)) if L<=4 else sorted({0,1,L//2,L});comp.append(compact(L,ts));ck(time.perf_counter()-START<55,'compact runtime guard')
 for cc in cell:
  other=next(z for z in comp if z['L']==cc['L'])
  for row,ind in zip(cc['depth_records'],other['prefixes']):
   a,b=e.interval({int(p):F(c) for p,c in row['global_outcome_KL'].items()});c,d=map(F,ind['global_outcome_KL_interval']);ck(a<=d and c<=b,'full cell replay agrees with separate compact log enclosures')
 ck(2*25**3<32**3 and 16>2*7,'all-L integer linear-growth certificates')
 # Independent scalar enclosure agrees with prime-log helper where both apply.
 for q in [F(16,7),F(53,256),F(203,224),F(25,32)]:
  a,b=logiv(q);c,d=e.interval(e.log(q));ck(a<=d and c<=b,'separate rigorous log implementations overlap')
 out={'status':'PASS','mode':mode,'counts':COUNTS,'own_assertions':N,'helper_assertions':e.COUNT,'primary_assertions':N+e.COUNT,'seconds':time.perf_counter()-START,'raw_actual_Boolean_module':raw,'cell_records':cell,'compact_records':comp,'scope':'fixed original product root; global inherited reference; no FEI counterexample; outcome credit pays signed terminal correction'}
 (ROOT/'out'/('PILOT.json' if mode=='pilot' else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 if mode=='main':
  ww=next(x['negative_control'] for x in cell if x['L']==2);(ROOT/'out/WITNESS.json').write_text(json.dumps(ww,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ('cell_records','compact_records','raw_actual_Boolean_module')}))
if __name__=='__main__':main()
