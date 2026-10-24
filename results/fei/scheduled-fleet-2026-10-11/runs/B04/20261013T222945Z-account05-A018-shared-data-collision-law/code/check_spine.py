from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[0]/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
fw=ns['fw'];add=ns['add'];grid=ns['grid'];logq=ns['logq'];ent=ns['ent'];SCALE=ns['SCALE']
start=time.perf_counter();checks=0;rows=[]
def ck(v):
 global checks
 checks+=1;assert v;assert time.perf_counter()-start<120
def probs(w):return [F(t*t,len(w)**2) for t in w]
def inf(w,bit):return sum(p for s,p in enumerate(probs(w)) if s&(1<<bit))
def comp(v,query):
 n=(len(v)).bit_length()-1;anf=[int(t<0) for t in v]
 for bit in range(n):
  for mask in range(len(v)):
   if mask&(1<<bit):anf[mask]^=anf[mask^(1<<bit)]
 edges=[set() for _ in range(n)]
 for mask,c in enumerate(anf):
  if c:
   subset=[i for i in range(n) if mask&(1<<i)]
   for i in subset:edges[i].update(subset)
 seen={query};todo=[query]
 while todo:
  for j in edges[todo.pop()]-seen:seen.add(j);todo.append(j)
 return seen
def phi(q0,q1):
 q=q0+q1
 return add((q,logq(q)) if q else (0,{}),(-q0,logq(q0)) if q0 else (0,{}),(-q1,logq(q1)) if q1 else (0,{}))
for a,m in ((1,4),(2,4),(3,4),(1,6),(2,6)):
 n=1+a*m;delta=F(1,1<<m)
 def val(index):
  z=index&1;result=1
  for j in range(a):
   block=(index>>(1+j*m))&((1<<m)-1);x=block&1;t=block>>1
   exponent=z*(t&1)+sum(((t>>k)&1)*((t>>(k+1))&1) for k in range(1,m-1,2))
   b=1-2*(exponent%2)
   if not z and not t and x:b=-b
   result*=b
  return result
 truth=[val(i) for i in range(1<<n)];w=fw(truth);P=probs(w)
 for bit in range(n):
  physical=F(sum(truth[i]!=truth[i^(1<<bit)] for i in range(len(truth))),len(truth))
  ck(inf(w,bit)==physical)
 dz=(1-(-2*delta)**a)/2;V=F(m-1,2)+m*delta;I=sum(p*s.bit_count() for s,p in enumerate(P))
 ck(I==a*V+dz and inf(w,0)==dz)
 for j in range(a):
  ck(inf(w,1+j*m)==delta)
  for k in range(1,m):ck(inf(w,1+j*m+k)==F(1,2)+delta)
 ck(len(comp(truth,0))==n)
 total=F(0);nodes=0
 for depth in range(a):
  fixed=[1+j*m for j in range(depth)];coords=[i for i in range(n) if i not in fixed]
  qi=coords.index(1+depth*m)
  for history in range(1<<depth):
   def original(index):
    z=sum(((index>>j)&1)<<bit for j,bit in enumerate(coords))
    return z+sum(((history>>j)&1)<<bit for j,bit in enumerate(fixed))
   v=[val(original(i)) for i in range(1<<len(coords))];wn=fw(v);pn=probs(wn)
   ck(inf(wn,qi)==delta)
   component=comp(v,qi)
   ck(len(component)==len(coords)-(depth-history.bit_count())*(m-2))
   indices=[i for i in range(len(v)) if not(i&(1<<qi))]
   D=[F(v[i]-v[i|(1<<qi)],2) for i in indices];wd=fw(D);pd=probs(wd)
   ck(sum(pd)==delta)
   derivativecoords=[i for i in range(len(coords)) if i!=qi]
   reduced=sum(p*sum(bool(s&(1<<j)) for j,c in enumerate(derivativecoords) if c in component) for s,p in enumerate(pd))
   total+=2*reduced/(1<<depth)
   B={}
   for i in indices:
    B=add((1,B),(1,phi(pn[i],pn[i|(1<<qi)])))
   margin=add((1,B),(-delta*F(m-1,2),{2:1}))
   ck(grid(margin)[0]>=0);nodes+=1
 expected=a*m*delta+delta*a*(a-1)*(F(3*(m-2),4)+(4*m-2)*delta)
 ck(total==expected)
 # Reconstruct both separator children and the normalized complete reference.
 v0=truth[0::2];v1=truth[1::2];w0=fw(v0);w1=fw(v1)
 I0=sum(p*s.bit_count() for s,p in enumerate(probs(w0)));I1=sum(p*s.bit_count() for s,p in enumerate(probs(w1)))
 ck(I0==a*(F(m-2,2)+2*m*delta) and I1==F(a*m,2))
 ck(I==dz+(I0+I1)/2)
 def supported(T):return all(not(T&(1<<(j*m))) and T&(1<<(j*m+1)) for j in range(a))
 q0=F(1,1<<(a*m));q1=F(1,1<<(a*(m-2)))
 qsum=F(0);alpha=F(0);CE={}
 for S,p in enumerate(P):
  T=S>>1;hit=supported(T);q=(q0+(q1 if hit else 0))/4;qsum+=q
  if hit:alpha+=p
  if p:CE=add((1,CE),(-p,logq(q)))
 ck(qsum==1 and alpha==(1+delta**a)/2)
 formula=add((a*m+2,{2:1}),(-alpha,logq(1+4**a)))
 ck(CE==formula)
 ck(grid(add((F(8,3)*I,{2:1}),(-1,CE)))[0]>=0)
 ck(grid(add((1,CE),(-1,ent(P))))[0]>=0)
 ck(ent(probs(w1))=={2:F(a*(m-2))})
 ck(dz>=F(3,8))
 rows.append({'a':a,'m':m,'I':str(I),'d_z':str(dz),'T_factor':str(total),'selector_descendant_nodes':nodes,'alpha':str(alpha),'reference_normalization':'1','status':'PASS'})
 (ROOT/'out/SPINE_PARTIAL.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','fixtures':rows,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'scope':'Independent proof review and exact physical/ANF/reference reconstruction; no imported A016 helper','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out/SPINE_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','checks':checks,'fixtures':len(rows),'elapsed_seconds':out['elapsed_seconds']},indent=2))
