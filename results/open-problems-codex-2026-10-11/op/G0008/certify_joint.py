from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import defaultdict
import json,time,sympy as S
from joint_boundary import admissible,orbit
r=json.loads(Path('joint_R2.json').read_text());m=r['edges'];groups={}
for st in r['states']:
 tokens=st['tokens'];part=tuple(v>>1 for v in tokens);hit=tuple(v&1 for v in tokens)
 key=tuple(sorted(set(orbit(pi) for pi in admissible(part,hit))))
 poly=groups.setdefault(key,[0]*(m+1))
 for i,v in enumerate(st['weight']):poly[i]+=v
print('GROUPS',len(groups),list(groups),flush=True)
x=S.symbols('x');q=1-x
expr={'s':q*x,'a':q*2*x*(3-2*x)/4,'b':q*(2*x-1)/2,'g':x*q*q*(2-x),'d':q*(2*x**3-7*x*x+8*x-2)/4,'e':-q**4}
def power_to_bern(c,n):return [sum(c[i]*F(comb(k,i),comb(n,i)) for i in range(k+1)) for k in range(n+1)]
scores={k:power_to_bern([F(S.Poly(e,x).nth(i)) for i in range(5)],4) for k,e in expr.items()}
probs={k:[F(c,comb(m,i)) for i,c in enumerate(v)] for k,v in groups.items()}
def split(bb,t):
 row=bb.copy();left=[row[0]];right=[row[-1]]
 while len(row)>1:
  row=[(1-t)*a+t*b for a,b in zip(row,row[1:])];left.append(row[0]);right.append(row[-1])
 return left,list(reversed(right))
def restrict(bb,a,b):
 left=split(bb,b)[0]
 return split(left,a/b)[1] if a else left
weights=[[F(comb(m,i)*comb(4,j),comb(m+4,i+j)) for j in range(5)] for i in range(m+1)]
def certificate(a,b):
 sb={k:restrict(v,a,b) for k,v in scores.items()};out=[F(0)]*(m+5);low={}
 for key,bb in probs.items():
  lb=[min(sb[k][j] for k in key) for j in range(5)];low[key]=lb;pp=restrict(bb,a,b)
  for i,v in enumerate(pp):
   if v:
    for j,u in enumerate(lb):out[i+j]+=v*u*weights[i][j]
 return out,low
start=time.time();todo=[(F(0),F(1),0)];cert=[];failed=[]
while todo:
 a,b,depth=todo.pop();bb,low=certificate(a,b)
 if min(bb)>=0 and max(bb)>0:
  cert.append({'a':str(a),'b':str(b),'coefficients':[str(v) for v in bb], 'score_lower_coefficients':[{'orbits':list(key),'coefficients':[str(v) for v in vals]} for key,vals in low.items()]})
  print('CERT',a,b,'depth',depth,'endpoints',float(bb[0]),float(bb[-1]),flush=True)
 elif depth>=12:
  failed.append((str(a),str(b),str(min(bb))));print('FAIL',a,b,'min',float(min(bb)),flush=True)
 else:
  h=(a+b)/2;todo.append((h,b,depth+1));todo.append((a,h,depth+1))
 if time.time()-start>150:print('TIME_LIMIT',flush=True);break
out={'radius':2,'interior_edges':m,'degree':m+4,'groups':[{'orbits':list(k),'counts':v} for k,v in groups.items()],'score_bernstein':[{'orbit':k,'coefficients':[str(v) for v in vls]} for k,vls in scores.items()],'certificates':cert,'failed':failed,'pending':[(str(a),str(b),d) for a,b,d in todo],'seconds':time.time()-start}
Path('joint_interval_certificates.json').write_text(json.dumps(out,indent=2),encoding='utf8');print('FINAL certs',len(cert),'failures',len(failed),'pending',len(todo),'secs',time.time()-start,flush=True)
