from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys
P=Path(__file__).resolve().parents[1]; start=time.monotonic();checks=0;CAP=1800 if '--replay' in sys.argv else 60;SCALE=1<<104
def check(v):
 global checks
 assert v; checks+=1
 if time.monotonic()-start>CAP: raise TimeoutError('frozen time cap')
def ln(t):
 z=(t-1)/(t+1); zz=z*z; power=z; a=Q(0)
 for k in range(35): a+=2*power/(2*k+1);power*=zz
 return a,a+2*power/(71*(1-zz))
ln2=ln(Q(2))
@lru_cache(None)
def lg(n):
 k=n.bit_length()-1
 if n==1<<k:return k*SCALE,k*SCALE
 a,b=ln(Q(n,1<<k));low=(k+a/ln2[1])*SCALE;high=(k+b/ln2[0])*SCALE
 return low.numerator//low.denominator,-((-high.numerator)//high.denominator)
def sign(terms):
 low=high=0
 for n,c in terms:
  a,b=lg(int(n));c=int(c)
  low+=c*(a if c>=0 else b);high+=c*(b if c>=0 else a)
 if not terms:return 0
 check(low>0 or high<0)
 return 1 if low>0 else -1
def influence_num(vals):
 n=(len(vals)).bit_length()-1;boundary=0
 for x in range(len(vals)):
  for k in range(n):
   if not(x>>k&1):boundary+=vals[x]!=vals[x^(1<<k)]
 return 2*boundary
def table(s,L,R,T):
 n=s+L+R+T+1; widths=[s,L,R,T];out=[]
 for x in range(1<<n):
  masks=[];pos=0
  for w in widths:masks.append(((x>>pos)&((1<<w)-1))==0);pos+=w
  S,W,U,V=masks;active=(W and U and V) or (S and U) or (S and V)
  out.append(-1 if active and not(x>>pos&1) else 1)
 return out
def ledger(vals,pos,s):
 N=len(vals)
 if all(v==vals[0] for v in vals):return Q(0),Q(0),Q(0),Q(0)
 # The terminal z bit is always the last remaining coordinate.
 if all(v==(-1 if x<N//2 else 1) for x,v in enumerate(vals)) or all(v==(1 if x<N//2 else -1) for x,v in enumerate(vals)):
  return Q(0),Q(0),Q(1),Q(1)
 a=vals[::2];b=vals[1::2];product=[v*w for v,w in zip(a,b)]
 d=Q(sum(v!=w for v,w in zip(a,b)),len(a));c=Q(influence_num(product),2*len(a))
 left=ledger(a,pos+1,s);right=ledger(b,pos+1,s)
 raw=c if pos<s else Q(0)
 return (raw+(left[0]+right[0])/2,d+(left[1]+right[1])/2,(left[2]+right[2])/2,(left[3]+right[3])/2)
cases=[(s,L,R,T) for s in (1,2) for L in (1,2) for R in (1,2) for T in (1,2)]+[(2,4,1,1),(3,6,1,1)]
rows=[]
for s,L,R,T in cases:
 vals=table(s,L,R,T);N=len(vals);a=Q(1,1<<s);eta=Q(1,1<<(L+R+T));q=Q(1,1<<R);r=Q(1,1<<T);e=q+r-q*r-eta
 JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);p=eta+a*e
 I=s*a*e+(1-a)*JB+a*JC+p;raw=a*(s*(JB+JC)+e*s*(s-1)/2+s*e)
 got=ledger(vals,0,s)
 check(Q(influence_num(vals),N)==I);check(got[0]==raw);check(got[1]+got[3]==I);check(got[2]==p);check(got[3]==p)
 rows.append({'s':s,'L':L,'R':R,'T':T,'n':N.bit_length()-1,'I':str(I),'raw':str(raw),'terminal_probability':str(p),'removed_influence':str(got[1])})
result={'case_count':len(rows),'assertions':checks,'seconds':time.monotonic()-start,'rows':rows,'representation':'direct truth tables; complete S,W,U,V order stopping at z; integer edges'}
(P/'out'/'REPRODUCTION_RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
# A separate replay is invoked by --replay after the pilot succeeds.
import sys
if '--replay' in sys.argv:
 source=json.loads((P/'out'/'full_RESULTS.json').read_text());count=0
 for cert in source['certificates']:
  check(sign(cert['expression'])==cert['sign']);count+=1
 replay={'certificates_replayed':count,'arithmetic':'35-term rational atanh with explicit geometric tail; no saved log intervals used','seconds':time.monotonic()-start,'assertions':checks}
 (P/'out'/'REPLAY_RESULTS.json').write_text(json.dumps(replay,indent=2));print(json.dumps(replay))
