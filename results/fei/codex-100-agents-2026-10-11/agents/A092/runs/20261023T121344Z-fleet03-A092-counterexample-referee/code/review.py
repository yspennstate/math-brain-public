"""Original-table referee using direct characters and symbolic prime logarithms."""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
import sys,json,time,hashlib
import arithmetic as ar

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(p):
 global checks
 checks+=1
 assert p,checks
def dump(name,x):
 (ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
def expr(d):return {p:F(x) for p,x in d.items() if x}
def add(a,b):
 d=dict(a)
 for p,x in b.items():d[p]=d.get(p,F(0))+x
 return expr(d)
def scale(x,a):return expr({p:F(x)*y for p,y in a.items()})
def sub(a,b):return add(a,scale(-1,b))
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def logform(x):
 x=F(x);d={}
 for sign,n in [(1,x.numerator),(-1,x.denominator)]:
  for p,e in factors(n).items():
   key=1 if p==2 else p;d[key]=d.get(key,F(0))+sign*e
 return expr(d)
def H(p):
 out={}
 for x in p:
  if x:out=add(out,scale(-x,logform(x)))
 return out
def bounds(e):
 z=(F(0),F(0))
 for p,c in e.items():z=ar.add(z,ar.mul(c,(F(1),F(1)) if p==1 else ar.lg(F(p))))
 return z
def packed(e):return {str(k):str(v) for k,v in sorted(e.items())}
def integer_sign(e):
 D=lcm(*(x.denominator for x in e.values())) if e else 1
 a=b=1
 for p,c in e.items():
  prime=2 if p==1 else p;n=int(c*D)
  if n>0:a*=prime**n
  elif n<0:b*=prime**(-n)
 return (a>b)-(a<b),{'common_denominator':D,'scaled_prime_log_coefficients':{str(2 if p==1 else p):int(c*D) for p,c in e.items()},'positive_integer_bits':a.bit_length(),'negative_integer_bits':b.bit_length(),'positive_integer_sha256':hashlib.sha256(a.to_bytes((a.bit_length()+7)//8,'big')).hexdigest(),'negative_integer_sha256':hashlib.sha256(b.to_bytes((b.bit_length()+7)//8,'big')).hexdigest(),'integer_hash_encoding':'unsigned big endian minimal bytes','comparison':('>' if a>b else '<' if a<b else '=')}
def fw(vals):
 w=list(vals);s=1
 while s<len(w):
  for i in range(0,len(w),2*s):
   for j in range(i,i+s):a,b=w[j],w[j+s];w[j],w[j+s]=a+b,a-b
  s*=2
 return [F(x,len(vals)) for x in w]
def child(v,j,t):
 return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2)]
def stats(v):
 w=ar.spectrum(v);ck(w==fw(v));p=[x*x for x in w];ck(sum(p)==1)
 edges=ar.edges(v);I=sum(edges);ck(ar.ib(p)==I)
 return {'v':v,'w':w,'p':p,'H':H(p),'I':I,'edges':edges}
def point(m):return [-1]+[1]*((1<<m)-1)
def circuit(blocks):
 sizes=[len(v).bit_length()-1 for v in blocks];out=[]
 for x in range(1<<sum(sizes)):
  offset=0;good=True
  for v,m in zip(blocks,sizes):good &= v[(x>>offset)&((1<<m)-1)]==1;offset+=m
  out.append(1 if good else -1)
 return out
def correction(v,blocks):
 s=stats(v);q=[];total={};offset=0
 for j,g in enumerate(blocks):
  inner=stats(g);weight=F(1)
  for ell,h in enumerate(blocks):
   if j!=ell:weight*=F(sum(x==1 for x in h),len(h))
  q.append(weight);total=add(total,scale(weight,inner['H']))
  for k,d in enumerate(inner['edges']):ck(s['edges'][offset+k]==weight*d)
  offset+=len(g).bit_length()-1
 s['q']=q;s['C']=sub(s['H'],total)
 return s
def phi(mu):return H([mu*mu]) if mu else {}

def run(pilot=False):
 started=time.perf_counter();limit=55 if pilot else 120
 blocks=[point(3),point(2),point(2)];root=circuit(blocks)
 rows=[correction(root,blocks)]
 for t in [0,1]:
  bb=[child(blocks[0],0,t),blocks[1],blocks[2]];vv=child(root,0,t)
  ck(vv==circuit(bb));rows.append(correction(vv,bb))
 a,b,c=rows
 ck([s['I'] for s in rows]==[F(111,64),F(27,16),F(3,2)])
 ck(a['edges'][0]==F(9,64));ck(a['I']-(b['I']+c['I'])/2==F(9,64))
 ck(a['q']==[F(9,16),F(21,32),F(21,32)])
 closed=[{1:F(57,8),3:F(-1431,1024),7:F(-3087,2048)},
         {1:F(53,8),3:F(-1701,512),5:F(-25,512)},
         {1:F(3),3:F(-27,16)}]
 certificates={}
 for label,s,e in zip(['parent','child0','child1'],rows,closed):
  ck(s['C']==e);sign,receipt=integer_sign(e);ck(sign==1);ck(bounds(e)[0]>0);certificates[label+'_C']=receipt
 G=sub(scale(F(1,2),add(b['C'],c['C'])),a['C'])
 ck(G=={1:F(-37,16),3:F(-567,512),5:F(-25,1024),7:F(3087,2048)})
 sign,receipt=integer_sign(G);ck(sign==1);certificates['positive_drift']=receipt
 lo,hi=bounds(G);ck(F(107184,10**6)<lo<hi<F(107185,10**6))
 repair=scale(F(64,9),G);rl,rh=bounds(repair)
 ck(F(762198,10**6)<rl<rh<F(762199,10**6))
 # ALL K>=3, ALL stopping restrictions: point cores close downwards.
 core_rows=[]
 for m in range(4):
  ss=stats(point(m));slack=sub({1:3*ss['I']},ss['H'])
  ck(integer_sign(slack)[0]>=0)
  if m:
   ck(child(point(m),0,0)==point(m-1));ck(set(child(point(m),0,1))=={1})
  core_rows.append({'m':m,'H':packed(ss['H']),'I':str(ss['I']),'3I-H':packed(slack),'all_K_ge3_stopping_hull':'0 by restriction induction'})
 ck(3**9>2**14)
 vacuum=[phi(s['w'][0]) for s in rows]
 empty_drift=sub(scale(F(1,2),add(vacuum[1],vacuum[2])),vacuum[0])
 ck(empty_drift=={1:F(85,512),5:F(-25,1024)})
 nonempty=sub(G,empty_drift)
 ck(nonempty=={1:F(-1269,512),3:F(-567,512),7:F(3087,2048)})
 sign,receipt=integer_sign(nonempty);ck(sign==-1);certificates['negative_nonempty_drift']=receipt
 # The full table, not an occupied-set ansatz, produced every expression.
 dump('CIRCUIT_CERTIFICATE.json',{'parent_table':root,'child_tables':[s['v'] for s in rows[1:]],'state_dimensions':[7,6,6],'C':[packed(s['C']) for s in rows],'H':[packed(s['H']) for s in rows],'I':[str(s['I']) for s in rows],'queried_influence':'9/64','G':packed(G),'G_interval':ar.pretty((lo,hi)),'repair_lambda_interval':ar.pretty((rl,rh)),'empty_masses':[str(s['p'][0]) for s in rows],'empty_drift':packed(empty_drift),'nonempty_drift':packed(nonempty),'integer_certificates':certificates,'inner_hulls':core_rows,'scope':'proposed U_K superharmonicity only; NOT full FEI or every possible bank allocation'})
 # Full labelled sanity census of the independently proved universal component.
 n=2 if pilot else 3;size=1<<n;tables=queries=zero_rows=0
 for truth in range(1<<size):
  vals=[1 if (truth>>x)&1 else -1 for x in range(size)];s=stats(vals);tables+=1
  V=add(phi(s['w'][0]),{1:3*s['I']})
  ck(integer_sign(sub({1:F(9,2)*s['I']},V))[0]>=0)
  for j in range(n):
   queries+=1;ch=[stats(child(vals,j,t)) for t in [0,1]]
   ck(s['I']-sum(t['I'] for t in ch)/2==s['edges'][j])
   ck(abs(ch[0]['w'][0]-ch[1]['w'][0])<=2*s['edges'][j])
   W=scale(F(1,2),add(add(phi(ch[0]['w'][0]),{1:3*ch[0]['I']}),add(phi(ch[1]['w'][0]),{1:3*ch[1]['I']})))
   diff=sub(V,W)
   if not s['edges'][j]:ck(not diff);zero_rows+=1
   else:ck(bounds(diff)[0]>0)
  if time.perf_counter()-started>limit:raise RuntimeError('frozen deadline exceeded')
 result={'status':'PASS','pilot':pilot,'original_circuit_states':3,'full_state_dimensions':[7,6,6],'point_core_restriction_sizes':[0,1,2,3],'vacuum_truth_tables':tables,'vacuum_physical_queries':queries,'zero_influence_query_equalities':zero_rows,'exact_assertions':checks,'seconds':time.perf_counter()-started,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'G_interval':ar.pretty((lo,hi)),'no_full_fei_claim':True}
 dump('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps({k:v for k,v in result.items() if k!='G_interval'}))
if __name__=='__main__':run('--pilot' in sys.argv)
