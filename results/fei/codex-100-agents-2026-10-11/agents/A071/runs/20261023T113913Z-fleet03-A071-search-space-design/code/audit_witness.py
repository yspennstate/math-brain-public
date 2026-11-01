"""Whole-cube direct character and edge reconstruction; no producer import."""
from profile_engine import F,add,mul,mean,minus,neg,pack,ev,cmp,pos,lp,Q
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
def ck(x):
 global CHECKS
 assert x;CHECKS+=1
def ent(ps):
 out={}
 for p in ps:
  if p:out=add(out,mul(lp(p),-p))
 return out
def core_info(m):
 if m==0:return {},F(0)
 N=1<<m;mu=F(N-2,N);H=ent([mu*mu]+[F(4,N*N)]*(N-1));I=F(2*m,N)
 ck(cmp(add({2:4*I},neg(H)),{})>=0)
 return H,I
def physical(ms):
 total=sum(ms);N=1<<total;offset=[];z=0
 for m in ms:offset.append(z);z+=m
 # Literal AND of three OR clauses; no macro spectral expansion.
 vals=[1 if all(((x>>s)&((1<<m)-1))!=0 for m,s in zip(ms,offset)) else -1 for x in range(N)]
 W=[sum(v*(-1 if (x&A).bit_count()%2 else 1) for x,v in enumerate(vals)) for A in range(N)]
 ck(sum(w*w for w in W)==N*N)
 for x,v in enumerate(vals):ck(sum(w*(-1 if (x&A).bit_count()%2 else 1) for A,w in enumerate(W))==N*v)
 H=ent(F(w*w,N*N) for w in W);ds=[F(sum(vals[x]!=vals[x^(1<<j)] for x in range(N)),N) for j in range(total)]
 I=sum(ds,F(0));ck(I==F(sum(A.bit_count()*w*w for A,w in enumerate(W)),N*N))
 blockI=[sum(ds[s:s+m],F(0)) for m,s in zip(ms,offset)];C=H
 for m,J in zip(ms,blockI):
  h,i=core_info(m)
  if i:C=add(C,mul(h,-J/i))
  else:ck(J==0)
 return {'H':H,'I':I,'S4':add({2:4*I},neg(H)),'C':C,'U':pos(C),'edges':ds,'W':W,'truth':vals,'blockI':blockI}
def unpack(d):return {int(p):F(v) for p,v in d.items() if F(v)}
def persist(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
# A fixed seven-bit witness; first core queried at original coordinate0.
p=physical([3,2,2]);c0=physical([2,2,2]);c1=physical([2,2]);children=[c0,c1]
given=json.loads((R/'out/COUNTEREXAMPLE.json').read_text(encoding='utf-8'))
ck(given['dimension']==7 and given['core_names']==['A3','A2','A2'] and given['outer_truth_integer']==1)
for actual,source in zip([p]+children,[given['parent']]+given['children']):
 ck(actual['H']==unpack(source['H']));ck(actual['I']==F(source['I']));ck(actual['C']==unpack(source['C']));ck(actual['U']==unpack(source['U']))
gap=minus(mean([z['U'] for z in children]),p['U']);ck(cmp(gap,{})>0);ck(gap==unpack(given['drift']))
d=p['edges'][0];ck(d==F(9,64));ck(p['I']-sum(z['I'] for z in children)/2==d)
price=mul(gap,1/d)
def bounds(v,den=1000000):
 lo,hi=ev(v);return [str(F(lo*den//Q,den)),str(F(-((-hi*den)//Q),den))]
allpositive=all(cmp(z['C'],{})>0 for z in [p]+children);ck(allpositive)
for m in range(4):core_info(m)
# Positive controls reject a corruption in each independent critical lane.
ck(add(p['C'],{2:F(1)})!=unpack(given['parent']['C']));ck(add(gap,{2:F(1)})!=unpack(given['drift']))
out={'literal_boolean':'AND(OR(x0,x1,x2),OR(x3,x4),OR(x5,x6)), bit1 means sign-1 in inner gates; output+1 iff each block is nonzero','dimensions':[7,6,4],'physical_query':0,'entropy_bits':True,'rate_scope':'every K>=4; all inner deficit hulls remain0','all_three_outer_corrections_strictly_positive':allpositive,'parent_C':pack(p['C']),'child_C':[pack(z['C']) for z in children],'drift':pack(gap),'drift_rational_bracket':bounds(gap),'physical_influence':str(d),'necessary_added_influence_coefficient':pack(price),'coefficient_bracket':bounds(price),'checks':CHECKS,'seconds':time.perf_counter()-START,'positive_controls':'altered correction and drift rejected','counterexample_scope':'proposed component envelope only; full FEI OPEN','rows':[]}
for z in [p]+children:out['rows'].append({'H':pack(z['H']),'I':str(z['I']),'S4':pack(z['S4']),'block_influences':list(map(str,z['blockI'])),'integer_Walsh':z['W'],'truth':z['truth']})
ck(out['seconds']<55);persist('INDEPENDENT_AUDIT.json',out)
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','parent_C','child_C','drift','necessary_added_influence_coefficient']}))
