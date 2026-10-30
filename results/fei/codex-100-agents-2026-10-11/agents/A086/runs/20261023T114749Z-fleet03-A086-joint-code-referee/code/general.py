"""Exhaustive small labelled Boolean sources; exact full-reference challenge."""
from pathlib import Path
from fractions import Fraction as F
from time import perf_counter
import importlib.util,json,sys,hashlib
R=Path(__file__).resolve().parents[1];sp=importlib.util.spec_from_file_location('stage20_actual_models',R/'code/check.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
start=perf_counter();checks=cases=path_edges=0
def ck(b,label):
 global checks
 checks+=1
 if not b:raise AssertionError(label)
 if perf_counter()-start>58:raise TimeoutError('frozen58sec guard')
def chi(P,Q,pad):return sum((m.count(k,pad)*(P[k]-Q[k])**2/Q[k] for k in P),F(0))
def cert():
 u=F(1,256);e=F(1,256)
 ck(5+6*e+u+6*e*u<6,'all-source old floor chi coefficient')
 ck(F(1,2)+54*u==F(91,128)<1,'all-source Dfloor upper')
 ck(4+u<F(33,8),'all-source canonical chi coefficient')
 ck(F(3,2)*F(33,8)**2*F(128,127)<26,'all-source Dcan upper including a0')
 ck((1-u)*(1-6*e)/(1+3*e)>F(15,16),'all-source complement mass gap')
 ck(F(75,512)-26*u==F(23,512)>0,'positive uniform conversion coefficient')
 # Formal rational polynomial identities for the actual nonempty ratios.
 aa=F(-7,8);bb=F(1,8)
 ck((2*aa*bb*(bb-aa),bb*bb-aa*aa,6*(aa-bb))==(-F(7,32),-F(3,4),-F(6)),'concrete nonempty ratio cross-product')
 return {'status':'PASS','Dfloor_upper_coefficient':'91/128','Dcan_upper_coefficient':'13/128','difference_lower_coefficient':'23/512','domain':'all a>=0,m>=8 via Boolean quantization, not finite extrapolation'}
def path(g,pad):
 global path_edges
 a=(len(g)-1).bit_length();eps=F(1,2**(a+pad));src=g;P=m.true(src,pad);current=m.floor(src,pad);initial=m.CE(P,current,pad);ce=initial
 G={};T={};reset={};reach=F(1);book=F(0)
 for k in range(a):
  kids,Ps,Qs,Z=m.inherit(src,current,pad,0)
  old0=m.CE(Ps[0],Qs[0],pad);old1=m.CE(Ps[1],Qs[1],pad)
  G=m.plus((1,G),(reach,ce),(-reach/2,old0),(-reach/2,old1));T=m.plus((1,T),(reach/2,old1))
  src=kids[0];reach/=2;current=m.floor(src,pad);ce=m.CE(Ps[0],current,pad)
  actual=m.plus((reach,ce),(-reach,old0));charge=m.interval(actual)
  ck(charge[1]<eps,'ACTUAL inherited matching-child positive charge bounded')
  book+=max(charge[1],0);reset=m.plus((1,reset),(1,actual))
  ck(book<(k+1)*eps,'all source-path positive bookings retained')
  ck(m.plus((1,G),(1,T),(reach,ce))==m.plus((1,initial),(1,reset)),'EXACT whole query+all terminal ledger at every frontier')
  path_edges+=1
 return book
def main():
 global cases
 pilot='--pilot' in sys.argv;certificate=cert();by_a={}
 existing=R/'out/GENERAL_RESULTS.json'
 if not pilot and existing.exists() and json.loads(existing.read_text(encoding='utf-8')).get('cases')==276:
  (R/'out/GENERAL_INITIAL_RESULTS.json').write_bytes(existing.read_bytes())
 for a in ([0,1,2] if pilot else [0,1,2,3]):
  hits=0;pad=8;eps=F(1,2**(a+pad))
  for bits in range(2**(2**a)):
   g=tuple(1 if (bits>>x)&1 else -1 for x in range(2**a));g=tuple(g[0]*v for v in g)
   co=m.spectrum(g);support=[j for j,v in enumerate(co) if v];N=len(support)
   ck(all(abs(co[j])>=F(1,2**a) for j in support),'Boolean source quantization')
   ck(N*eps<=F(1,256),'support count times edit mass')
   P=m.true(g,pad);Q=m.canonical(g,pad);Qnew=m.floor(g,pad)
   ck(m.total(Q,pad)==m.total(Qnew,pad)==m.total(P,pad)==1,'full source and reference masses')
   ck(sum(m.count(k,pad) for k in P)==2**(a+pad+1),'every joint Fourier mask counted once')
   chican=chi(P,Q,pad);chifloor=chi(P,Qnew,pad)
   ck(F(3,2)*chican<26*N*eps*eps<=F(13,128)*eps,'exact canonical D upper')
   ck(F(3,2)*chifloor<F(91,128)*eps,'exact full floor D upper')
   # Independent data marginal chi-square equals the entire conditional-lift sum.
   dat=F(0)
   for s in range(2**a):
    for d in (0,1):
     pp=P[s,d,0]+P[s,d,1];qq=Qnew[s,d,0]+Qnew[s,d,1]
     dat+=m.count((s,d,0),pad)*(pp-qq)**2/qq
   ck(dat==chifloor,'EXACT complete conditional-kernel cancellation')
   xx=2*eps*(1-N*eps);yy=3*eps*(1-N*eps)/(1+3*eps)
   ck((yy-xx)**2/(2*yy)>F(75,512)*eps,'binary KL lower via exact curvature')
   s=support[0]
   ck(Qnew[s,0,1]/Q[s,0,1]!=Qnew[0,1,1]/Q[0,1,1],'actual conditional NONEMPTY profile changed')
   difference=m.interval(m.plus((1,m.CE(P,Qnew,pad)),(-1,m.CE(P,Q,pad))))
   ck(difference[0]>F(23,512)*eps and difference[1]<eps,'actual positive complete CE conversion')
   alt=m.mix(Q,pad,F(1,4));alt={k:v/2 for k,v in alt.items()}
   for incoming in (P,alt):
    cost=m.interval(m.plus((1,m.CE(P,Qnew,pad)),(-1,m.CE(P,incoming,pad))))
    ck(cost[1]<eps,'arbitrary finite-cost true/half-mass incoming reference conversion')
   future=path(g,pad)
   ck(max(difference[1],0)+future<(a+1)*eps,'entry plus ALL future positive conversion bookings')
   Ig=m.old.influence(g)
   if Ig:ck((a+1)*eps<=F(1,256)*Ig,'ONE original source influence pays entire new phase')
   hits+=1;cases+=1
  by_a[a]=hits
 fixed=[];core_edges=path_edges
 if not pilot:
  actual=json.loads((R/'out/EXACT_RESULTS.json').read_text(encoding='utf-8'))['rows']
  src=tuple(1 if x==0 else -1 for x in range(16))
  for row in actual:
   pad=row['m'];future=path(src,pad);remain=F(row['remaining_lower'])-future/4
   ck(remain>F(187,16384),'ACTUAL original-rate4 account after ALL four source queries/floors')
   fixed.append({'m':pad,'future_positive_booking_upper':str(future/4),'remaining_lower':str(remain)})
 out={'status':'PASS','cases':cases,'incoming_comparisons':3*cases,'core_path_edges':core_edges,'path_edges':path_edges,'paid_fixed_paths':fixed,'assertions':checks,'helper_assertions':m.checks,'seconds':perf_counter()-start,'domain':by_a,'constants_included':True,'certificate':certificate,'arithmetic':'Fraction character sums, complete full-joint references and exact log-linear whole paths; chi-square and binary curvature; rigorous18-term atanh log intervals on outward96-bit grid','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out'/('GENERAL_PILOT.json' if pilot else 'GENERAL_RESULTS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':
 try:main()
 except Exception as e:
  (R/'out'/'GENERAL_FAILURE.json').write_text(json.dumps({'status':'FAIL_OR_INCOMPLETE','error':repr(e),'cases':cases,'assertions':checks,'seconds':perf_counter()-start}),encoding='utf-8');raise
