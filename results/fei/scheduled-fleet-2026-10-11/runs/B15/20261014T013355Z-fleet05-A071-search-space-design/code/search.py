import argparse,hashlib,itertools,json,math,sys,time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
NEG={0,1,2,4,8,16,32,6,17,40};PAIRS=((0,4),(1,2),(3,5))
S=1<<96;NAT=1<<160;TERMS=48;ARG=128
def h(x):return -1 if x in NEG else 1
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def ln_unit(a,b):
 u,v=a-b,a+b
 lo=sum(2*NAT*pow(u,2*j+1)//((2*j+1)*pow(v,2*j+1)) for j in range(TERMS))
 num=2*NAT*pow(u,2*TERMS+1)*v*v
 den=(2*TERMS+1)*pow(v,2*TERMS+1)*(v*v-u*u)
 return lo,lo+TERMS+(num+den-1)//den
LN2=ln_unit(2,1)
@lru_cache(None)
def lgint(n):
 assert n>0
 k=n.bit_length()-1
 if n==1<<k:return k*S,k*S
 shift=max(0,k-ARG)
 a=n>>shift;b=1<<(k-shift)
 lo=ln_unit(a,b)[0]
 hi=ln_unit(a+(1 if n!=(a<<shift) else 0),b)[1]
 return k*S+lo*S//LN2[1],k*S+(hi*S+LN2[0]-1)//LN2[0]
@lru_cache(None)
def lg(x):
 a,b=lgint(x.numerator),lgint(x.denominator)
 return Q(a[0]-b[1],S),Q(a[1]-b[0],S)
def xlog(x):return mul(lg(x),x) if x else (Q(0),Q(0))
@lru_cache(None)
def phi(x,y):return sub(sub(xlog(x+y),xlog(x)),xlog(y)) if x and y else (Q(0),Q(0))
def entropy(xs):
 ans=(Q(0),Q(0))
 for x in xs:ans=sub(ans,xlog(x))
 return ans
def enc(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [enc(v) for v in x]
 return x
def save(name,x):
 (ROOT/'out'/name).write_text(json.dumps(enc(x),indent=2),encoding='utf-8')
def fwht(a):
 a=list(a);step=1
 while step<len(a):
  for b in range(0,len(a),2*step):
   for j in range(b,b+step):u,v=a[j],a[j+step];a[j]=u+v;a[j+step]=u-v
  step*=2
 return a
def seed():
 a=[h(x) for x in range(64)];cs=fwht(a);sq=[Q(c*c,4096) for c in cs]
 Bs=[];ds=[]
 for j in range(6):
  B=(Q(0),Q(0))
  for x in range(64):
   if not(x>>j&1):B=add(B,phi(sq[x],sq[x|(1<<j)]))
  Bs.append(B);ds.append(Q(sum(a[x]!=a[x^(1<<j)] for x in range(64)),64))
 assert len(set(Bs))==len(set(ds))==1 and ds[0]==Q(3,16)
 assert all(Q(cs[1<<j]**2,4096)==ds[0]**2 for j in range(6))
 return {'p':Q(5,32),'d':ds[0],'t':ds[0]**2,'B':Bs[0],'H':entropy(sq),'I':Q(9,8),'n':6}
def transform(ps):
 cs=list(map(Q,[h(x) for x in range(64)]))
 for j,p in enumerate(ps):
  for x in range(64):
   if not(x>>j&1):
    u,v=cs[x],cs[x|(1<<j)];cs[x]=(1-p)*u+p*v;cs[x|(1<<j)]=v-u
 sq=[]
 for x,c in enumerate(cs):
  a=c*c
  for j,p in enumerate(ps):
   if x>>j&1:a*=p*(1-p)
  sq.append(a)
 assert sum(sq)==1
 return cs,sq
def compose(g,mask,keep_packets=False):
 ps=[1-g['p'] if mask>>j&1 else g['p'] for j in range(6)]
 cs,sq=transform(ps);rows=[];totalq=Q(0);v=4*g['p']*(1-g['p'])
 for j in range(6):
  q=sum(sq[x] for x in range(64) if x>>j&1)/v
  # Independent direct pivotal expectation on physical outer edges.
  edge=Q(0)
  for x in range(64):
   if not(x>>j&1):
    w=Q(1)
    for k,p in enumerate(ps):
     if k!=j:w*=p if x>>k&1 else 1-p
    edge+=w*Q(h(x)-h(x|(1<<j)),2)**2
  assert q==edge and q>0
  M=(Q(0),Q(0));packets=[]
  for x in range(64):
   if not(x>>j&1):
    a,b=sq[x],g['t']*sq[x|(1<<j)]/v
    M=add(M,phi(a,b))
    if keep_packets:packets.append([a,b])
  R=sub(M,mul(phi((1-2*ps[j])**2,g['t']),q))
  B=add(mul(g['B'],q),R);d=q*g['d'];E=mul(B,1/d);totalq+=q
  row={'block':j,'chosen_p':ps[j],'q':q,'reserve':R,'B':B,'influence':d,'E':E}
  if keep_packets:row['packets']=packets
  rows.append(row)
 Hp=entropy(sq);Cp=sub(Hp,mul(entropy([v,1-v]),totalq))
 H=add(mul(g['H'],totalq),Cp);I=totalq*g['I']
 Emin=(min(r['E'][0] for r in rows),min(r['E'][1] for r in rows))
 return {'mask':mask,'output_p':(1-cs[0])/2,'rows':rows,'E_min':Emin,'H':H,'I':I,
         'H_over_I':mul(H,1/I),'C_p':Cp,'outer_H':Hp,'sum_q':totalq,'bits':6*g['n']}
def advance(g,mask):
 r=compose(g,mask)
 assert mask in (0,63) and len(set(x['q'] for x in r['rows']))==1
 q=r['rows'][0]['q']
 z={'p':r['output_p'],'d':q*g['d'],'t':q*q*g['t'],'B':r['rows'][0]['B'],
    'H':r['H'],'I':r['I'],'n':6*g['n']}
 assert z['I']==z['n']*z['d']
 return z
def permute(x,pi):return sum(((x>>j)&1)<<pi[j] for j in range(6))
def orbits():
 perms=[]
 for order in itertools.permutations(range(3)):
  for flips in itertools.product((0,1),repeat=3):
   pi=[0]*6
   for k,pair in enumerate(PAIRS):
    dest=PAIRS[order[k]]
    for t,j in enumerate(pair):pi[j]=dest[t^flips[k]]
   assert all(h(x)==h(permute(x,pi)) for x in range(64))
   perms.append(pi)
 assert len(set(map(tuple,perms)))==48
 remaining=set(range(64));ans=[]
 while remaining:
  rep=min(remaining);orb=sorted(set(permute(rep,pi) for pi in perms))
  assert set(orb)<=remaining
  ans.append({'representative':rep,'members':orb});remaining-=set(orb)
 assert len(ans)==10 and sum(len(x['members']) for x in ans)==64
 return ans
def main(pilot):
 start=time.perf_counter();cap=55 if pilot else 600;g=seed();trace=[g]
 if not pilot:
  for mask in (0,63,0):
   g=advance(g,mask);trace.append(g);save('core_partial.json',trace)
   if time.perf_counter()-start>cap:raise RuntimeError('frozen cap')
  assert g['n']==1296 and min(g['p'],1-g['p'])<Q(1,16)
  assert mul(g['B'],1/g['d'])[0]>Q(669,200)
 orb=orbits();save('symmetry.json',orb)
 reps=[0,1,5,63] if pilot else [x['representative'] for x in orb]
 records=[]
 for mask in reps:
  r=compose(g,mask,True);records.append(r)
  save('pilot_partial.json' if pilot else 'cases_partial.json',records)
  if time.perf_counter()-start>cap:raise RuntimeError('frozen cap')
 result={'mode':'pilot' if pilot else 'full','core':g,'core_trace':trace,'orbits':orb,
   'cases':records,'runtime_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'K':'669/200','orbit_E_display':[{'mask':r['mask'],'E':[float(x) for x in r['E_min']],
      'coordinate_E':[float(x['E'][0]) for x in r['rows']]} for r in records]}
 if not pilot:
  result['all64_fail_K']=all(r['E_min'][1]<Q(669,200) for r in records)
  result['best_E_enclosure']=(max(r['E_min'][0] for r in records),max(r['E_min'][1] for r in records))
 save('pilot.json' if pilot else 'results.json',result)
 print(json.dumps({k:v for k,v in enc(result).items() if k in ('mode','runtime_seconds','orbit_E_display','all64_fail_K','best_E_enclosure')},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
