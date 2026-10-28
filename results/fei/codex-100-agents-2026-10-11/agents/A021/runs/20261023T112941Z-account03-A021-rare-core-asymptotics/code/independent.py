from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
ROOT=Path(__file__).resolve().parents[1];count=0
def ck(x,label):
 global count
 count+=1;assert x,(count,label)
def add(*xs):
 d={}
 for x in xs:
  for b,c in x.items():d[b]=d.get(b,F(0))+c
 return {b:c for b,c in d.items() if c}
def scale(x,c):return {b:a*c for b,a in x.items() if a*c}
def log(x):
 x=F(x);ans={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while n>1:
   while n%p==0:ans[p]=ans.get(p,0)+s;n//=p
   p+=1
 return {p:F(c) for p,c in ans.items() if c}
@lru_cache(None)
def li(n):
 k=n.bit_length()-1;y=F(n,2**k)
 def ln(y):
  z=(y-1)/(y+1);s=F(0);term=z
  for j in range(48):s+=2*term/(2*j+1);term*=z*z
  return s,s+2*term/(97*(1-z*z))
 a,b=ln(y);c,d=ln(F(2));return k+a/d,k+b/c
def lower(x):return sum((c*li(p)[0 if c>=0 else 1] for p,c in x.items()),F(0))
def spectrum(a):
 N=len(a);return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(a))**2,N*N) for s in range(N)]
def q(d,h):
 ans=[F(1)]
 for block in range(2):
  used=min(3,max(0,d-3*block));obs=(h>>(3*block))% (1<<used)
  if used==0:r=[F(9,16)]+[F(1,16)]*7
  elif used==1:r=[F(1,4)]*4 if obs==0 else [F(13,16)]+[F(1,16)]*3
  elif used==2:r=[F(1,16),F(15,16)] if obs==0 else [F(15,16),F(1,16)]
  else:r=[F(1)]
  ans=[a*b for b in r for a in ans]
 return ans
def main():
 start=time.perf_counter();data=json.loads((ROOT/'out/BELLMAN.json').read_text(encoding='utf-8'));rows=[]
 ck([x['vertex'] for x in data['rows']]==[None]+list(range(64)),'complete function domain')
 for case in data['rows']:
  v=case['vertex'];cert={(x['d'],x['h']):x for x in case['nodes']};ck(len(cert)==63,'complete prefix domain')
  f=[(-1 if (x&7)==0 else 1)*(-1 if (x>>3)==0 else 1)*(-1 if x==v else 1) for x in range(64)]
  def replay(d,h):
   vals=[f[h+(y<<d)] for y in range(1<<(6-d))];prob=spectrum(vals);ref=q(d,h)
   I=sum((F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals)) for i in range(6-d)),F(0))
   ce=add(*(scale(log(r),-p) for p,r in zip(prob,ref) if p));stop=add({2:4*I},scale(ce,-1));node=cert[d,h]
   if d==5:out=stop;ck(node['action']=='stop','terminal action')
   else:
    go=scale(add(replay(d+1,h),replay(d+1,h+(1<<d))),F(1,2))
    if node['action']=='query':ck(lower(add(stop,scale(go,-1)))>=0,'query optimal');out=go
    else:ck(lower(add(go,scale(stop,-1)))>=0,'stop optimal');out=stop
   stored={int(p):F(c) for p,c in node['value'].items()}
   ck(out==stored,'exact direct-character certificate value');return out
  value=replay(0,0);ck(lower(value)>=F(1,4),'all stopping cuts >=1/4')
  rows.append({'vertex':v,'root_expression':{str(p):str(c) for p,c in value.items()}})
 # Integer/rational certificates used in the analytic all-t passage.
 for truth in [3**9>2**14,13**3>2**11,15**3>2**11,15<16,13<16, F(3,2)+F(32,21)<4,F(121,512)>F(3,16),190*128<9*4096,F(37,32)>F(13,12),F(1,32)>F(13,576)]:ck(truth,'all-t scalar certificate')
 out={'status':'PASS','functions':len(rows),'nodes':63*len(rows),'assertions':count,'seconds':time.perf_counter()-start,'rows':rows,'implementation':'no production imports; direct character sums, physical edges,48-term outward rational logs'}
 (ROOT/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
