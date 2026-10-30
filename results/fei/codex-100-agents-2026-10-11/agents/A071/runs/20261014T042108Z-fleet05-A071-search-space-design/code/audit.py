import argparse,hashlib,json,math,time,sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1];S=1<<96;NAT=1<<128;TERMS=48
SOURCE=Path('~/brain_workers/FEI100_20261011/agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge')
NEG={0,1,2,4,8,16,32,6,17,40};H=[1-2*(x in NEG) for x in range(64)];J=[-H[x^1] for x in range(64)]
checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def enc(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
def save(name,x):(ROOT/'out'/name).write_text(json.dumps(enc(x),indent=2),encoding='utf-8')
def ln_unit(a,b):
 u,v=a-b,a+b
 lo=sum(2*NAT*pow(u,2*j+1)//((2*j+1)*pow(v,2*j+1)) for j in range(TERMS))
 num=2*NAT*pow(u,2*TERMS+1)*v*v
 den=(2*TERMS+1)*pow(v,2*TERMS+1)*(v*v-u*u)
 return lo,lo+TERMS+(num+den-1)//den
LN2=ln_unit(2,1)
@lru_cache(None)
def lint(n):
 ck(n>0);k=n.bit_length()-1
 if n==1<<k:return k*S,k*S
 a,b=ln_unit(n,1<<k);a+=k*LN2[0];b+=k*LN2[1]
 return a*S//LN2[1],(b*S+LN2[0]-1)//LN2[0]
def lg(x):
 a,b=lint(x.numerator),lint(x.denominator)
 return Q(a[0]-b[1],S),Q(a[1]-b[0],S)
def xlog(x):return mul(lg(x),x) if x else (Q(0),Q(0))
def entropy_prob(xs):
 c=Counter(xs);ans=(Q(0),Q(0))
 for x,count in c.items():ans=sub(ans,mul(xlog(x),count))
 return ans
def h2(p):return entropy_prob([p,1-p])
def hr(a,b):
 ck(0<=a<=b<=1)
 x,y=h2(a),h2(b)
 return min(x[0],y[0]),Q(1) if a<=Q(1,2)<=b else max(x[1],y[1])
def fwht(a):
 a=list(a);step=1
 while step<len(a):
  for b in range(0,len(a),2*step):
   for j in range(b,b+step):u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
  step*=2
 return a
def spectrum(a):
 W=fwht(a);N=len(a);sq=[Q(w*w,N*N) for w in W]
 ck(sum(sq)==1);return W,sq
def core(a):
 W,sq=spectrum(a);N=len(a);n=N.bit_length()-1
 I=sum(s.bit_count()*p for s,p in enumerate(sq))
 inf=[]
 for j in range(n):
  d=Q(sum(a[x]!=a[x^(1<<j)] for x in range(N)),N)
  ck(d==sum(sq[x] for x in range(N) if x>>j&1));inf.append(d)
 ck(sum(inf)==I)
 return {'n':n,'W':W,'p':Q(sum(x<0 for x in a),N),'H':entropy_prob(sq),'I':I,'influences':inf}
def outer(gate,p):
 # Independent direct centered-bit interpolation, as opposed to source uniform-Walsh reexpansion.
 c=list(map(Q,gate));v=p*(1-p)
 for j in range(6):
  for x in range(64):
   if not x>>j&1:
    a,b=c[x],c[x|(1<<j)];c[x]=(1-p)*a+p*b;c[x|(1<<j)]=b-a
 sq=[z*z*v**x.bit_count() for x,z in enumerate(c)];ck(sum(sq)==1)
 qs=[]
 for j in range(6):
  q=Q(0)
  for x in range(64):
   if not x>>j&1 and gate[x]!=gate[x|(1<<j)]:q+=p**x.bit_count()*(1-p)**(5-x.bit_count())
  ck(q==sum(sq[x] for x in range(64) if x>>j&1)/(4*v));qs.append(q)
 return c,sq,qs
def profiles(pilot):
 source=json.loads((SOURCE/'out/COMPACT_PAYMENT_CERTIFICATE.json').read_text())
 boxes=[];idx=0
 for left,right in [(Q(1,16),Q(7,32)),(Q(1,2),Q(25,32))]:
  for k in range(128):
   a=left+(right-left)*Q(k,128);b=left+(right-left)*Q(k+1,128)
   ck(list(map(Q,source['boxes'][idx]['input_bias_box']))==[a,b]);idx+=1
   if pilot and k not in (0,127):continue
   # All factors are nonnegative. Quadratic 1+4p-2p² increases on[0,1].
   qlo=12*a*(1-b)**3*(2-b);qhi=12*b*(1-a)**3*(2-a)
   alo=(1-b)**4*(1+4*a-2*a*a);ahi=(1-a)**4*(1+4*b-2*b*b)
   hp=hr(a,b);ha=hr(alo,ahi);D=qlo*hp[0]-ha[1];ck(D>0)
   vlo=4*min(a*(1-a),b*(1-b));vhi=Q(1) if a<=Q(1,2)<=b else 4*max(a*(1-a),b*(1-b))
   plus=6*vhi*hr(qlo/6,qhi/6)[1];minus=qhi*hr(vlo,vhi)[1]
   ck(max(plus,minus)<64*D)
   boxes.append({'box':[a,b],'D_lower':D,'C_upper':plus,'minus_C_upper':minus,'price_upper':max(plus,minus)/D})
   save('pilot_boxes_partial.json' if pilot else 'boxes_partial.json',boxes)
 ck(idx==256);ck(len(boxes)==(4 if pilot else 256));return boxes
def physical(pilot):
 out=[]
 for mask in ([1,6] if pilot else range(1,15)):
  rawcore=[1-2*((mask>>x)&1) for x in range(4)]
  for name,gate in [('h',H),('J',J)]:
   a=rawcore[:];p=Q(sum(x<0 for x in a),4)
   desired=max(p,1-p) if name=='h' else min(p,1-p)
   if p!=desired:a=[-x for x in a]
   g=core(a);p=g['p'];v=4*p*(1-p);raw,sq,qs=outer(gate,p);Qsum=sum(qs)
   truth=[gate[sum((a[(x>>(2*j))&3]<0)<<j for j in range(6))] for x in range(4096)]
   W,masses=spectrum(truth);pout=Q(sum(x<0 for x in truth),4096)
   ck(pout==(1-raw[0])/2)
   # Centered bit raw coefficient equals (-2)^k times centered sign raw coefficient.
   for T,val in enumerate(W):
    occupied=0;prod=1
    for j in range(6):
     subset=(T>>(2*j))&3
     if subset:occupied|=1<<j;prod*=g['W'][subset]
    k=occupied.bit_count()
    expected=raw[occupied]*Q(prod,(-8)**k)
    ck(Q(val,4096)==expected)
   Is=[]
   for j in range(12):
    edge=Q(sum(truth[x]!=truth[x^(1<<j)] for x in range(4096)),4096)
    ck(edge==qs[j//2]*g['influences'][j%2]);Is.append(edge)
   Iout=sum(Is);ck(Iout==Qsum*g['I'])
   Hp=entropy_prob(sq);C=sub(Hp,mul(h2(v),Qsum));Hout=entropy_prob(masses)
   diff=sub(Hout,add(mul(g['H'],Qsum),C));ck(diff[0]<=0<=diff[1])
   D=sub(mul(h2(p),Qsum),h2(pout));ck(D[0]>0)
   potential=sub(mul(h2(p),1/g['I']),mul(h2(pout),1/Iout))
   ck(max(potential[0],D[0]/Iout)<=min(potential[1],D[1]/Iout))
   eligible=name=='h'
   if eligible:ck(C[1]<64*D[0] and -C[0]<64*D[0])
   out.append({'core_mask':mask,'gate':name,'input_p':p,'output_p':pout,'Q':Qsum,
    'all12_physical_influences':Is,'C':C,'D':D,'identity_interval':diff,
    'legal_price_domain':eligible,'truth_sha256':hashlib.sha256(bytes(x+1 for x in truth)).hexdigest()})
   save('pilot_physical_partial.json' if pilot else 'physical_partial.json',out)
 return out
def rare():
 out=[]
 for n,negative in [(4,{0}),(5,{0}),(6,{0,1,2})]:
  a=[1-2*(x in negative) for x in range(1<<n)];g=core(a);p=g['p'];v=4*p*(1-p)
  ck(p<=Q(1,16))
  for name,gate in [('h',H),('J',J)]:
   raw,sq,qs=outer(gate,p);Qsum=sum(qs);pout=(1-raw[0])/2
   C=sub(entropy_prob(sq),mul(h2(v),Qsum));D=sub(mul(h2(p),Qsum),h2(pout))
   ck(D[0]>0 and max(C[1],-C[0])<64*D[0])
   ck(all(q>0 for q in qs))
   # Every non-dummy actual inner coordinate is retained; no transitivity assumption.
   physical_infs=[q*d for q in qs for d in g['influences']]
   ck(sum(physical_infs)==Qsum*g['I'])
   out.append({'n':n,'negative':sorted(negative),'gate':name,'p':p,'pout':pout,'Q':Qsum,
    'all_physical_influences':physical_infs,'C':C,'D':D,'retained_H':g['H']})
   save('rare_partial.json',out)
 return out
def fixture():
 path=ROOT.parents[1]/'runs/20261014T013355Z-fleet05-A071-search-space-design/out/core_partial.json'
 trace=json.loads(path.read_text());g=trace[-1];p=Q(g['p']);I=Q(g['I']);Hcore=tuple(map(Q,g['H']))
 ck(g['n']==1296 and p<Q(1,16))
 R=mul(Hcore,1/I);Psi=mul(h2(p),1/I);paid=add(R,mul(Psi,64))
 ck(paid[1]<12)
 return {'source':str(path),'R':R,'Psi':Psi,'R_plus64Psi':paid,'all_word_bound':12}
def constants():
 ck(Q(72)+96+Q(48465,256)<360)
 ck(Q(360)*Q(4,105)<14)
 ck(6*4*Q(3,2)/Q(3,4)==48)
 ck(120/Q(3,4)*Q(1,4)==40)
 ck(Q(1,2)+Q(3,2)/8==Q(11,16))
 ck(64*Q(11,16)==44)
 ck(12*Q(7,2)-84*Q(1,4)+12-Q(108,16)==Q(105,4))
 ck(8-20*Q(1,4)-Q(3,2)*Q(24,16)==Q(3,4))
def main(pilot):
 start=time.perf_counter();constants();boxes=profiles(pilot);cases=physical(pilot)
 result={'mode':'pilot' if pilot else 'full','assertions':checks,'compact_boxes':len(boxes),
   'max_compact_price_upper':max(x['price_upper'] for x in boxes),
   'physical_cases':len(cases),'physical_coefficient_checks':len(cases)*4096,
   'all_coordinate_edge_checks':len(cases)*12,'no_counterexample_in_frozen_family':True}
 if not pilot:result['rare_cases']=rare();result['existing_g3_fixture']=fixture()
 result['assertions']=checks;result['runtime_seconds']=time.perf_counter()-start
 ck(result['runtime_seconds']<(55 if pilot else 600))
 save('pilot.json' if pilot else 'validation.json',result)
 print(json.dumps({k:float(v) if isinstance(v,Q) else v for k,v in result.items() if k not in ('rare_cases','existing_g3_fixture')},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
