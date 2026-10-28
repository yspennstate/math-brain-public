from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v,checks
 checks+=1
 assert time.perf_counter()-start<50
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [enc(x) for x in v]
 return v
@lru_cache(None)
def p_of(v):
 return tuple(F(sum(a*(1-2*((x&t).bit_count()%2)) for x,a in enumerate(v))**2,len(v)**2) for t in range(len(v)))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def mul(w,a):return (w*a[0],w*a[1]) if w>=0 else (w*a[1],w*a[0])
Z=(F(0),F(0))
@lru_cache(None)
def log2(x):
 ck(x>0);n=x.numerator**4096;d=x.denominator**4096;k=n.bit_length()-d.bit_length()
 def lower(j):return n>=(d<<j) if j>=0 else (n<<(-j))>=d
 if not lower(k):k-=1
 ck(lower(k) and not lower(k+1))
 return F(k,4096),F(k+1,4096)
@lru_cache(None)
def H(p):
 s=Z
 for x in p:
  if x:s=add(s,mul(x,log2(1/x)))
 return s
@lru_cache(None)
def CE(p,q):
 s=Z
 for x,y in zip(p,q):
  if x:ck(y>0);s=add(s,mul(x,log2(1/y)))
 return s
@lru_cache(None)
def KL(p,q):
 s=Z
 for x,y in zip(p,q):
  if x:ck(y>0);s=add(s,mul(x,log2(x/y)))
 return s
def inflate(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def cut(v,i,b):return tuple(a for x,a in enumerate(v) if (x>>i&1)==b)
def project(q,i):
 out=[F(0)]*(len(q)//2)
 for x,a in enumerate(q):out[(x&((1<<i)-1))|((x>>(i+1))<<i)]+=a
 return tuple(out)
def infl(v):return F(sum(v[x]!=v[x^(1<<i)] for i in range((len(v)-1).bit_length()) for x in range(len(v))),len(v))
@lru_cache(None)
def update(p,q):
 q0=q[0];ck(0<q0<1);r=(p[0]+q0)/2
 v=(r,)+tuple(x*(1-r)/(1-q0) for x in q[1:]);ck(sum(v)==1)
 return v,KL(v,q)
src=Path('agents/A012/runs/20261023T053904Z-account03-A012-sparse-activation-accounting/out/NEXT_TARGET.json')
d=json.loads(src.read_text(encoding='utf-8'));f=tuple(d['F']);q=tuple(map(F,d['root_Q']));p=p_of(f);ck(p==q);ck(infl(f)==F(7,8))
l2lo=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(20)),F(0));l2hi=l2lo+F(2,41*3**41)*F(9,8)
K=(4+2/l2hi,4+2/l2lo);old=(F(5,4)/l2hi,F(5,4)/l2lo)
capacity=mul(F(7,8),K);initial=sub(sub(capacity,H(p)),old)
@lru_cache(None)
def generate(available):
 out=[('stop',)]
 for j in reversed(available):
  smaller=tuple(x for x in available if x!=j)
  out.extend((j,a,b) for a in generate(smaller) for b in generate(smaller))
 return tuple(out)
def canon(t):return tuple(canon(x) if isinstance(x,list) else x for x in t)
trees=generate((0,1,2));author=json.loads((R/'out/ALL_POLICIES.json').read_text(encoding='utf-8'))
ck(len(trees)==244);ck(set(trees)=={canon(x['tree']) for x in author['records']})
def rec(t,v=f,ref=q,coords=(0,1,2,3,4,5),fixed=(),reach=F(1)):
 pp=p_of(v);h=H(pp);fee=Z
 if set(fixed)=={0,1}:ref,c=update(pp,ref);fee=mul(reach,c)
 if t[0]=='stop':return {'CE':mul(reach,CE(pp,ref)),'KL':mul(reach,KL(pp,ref)),'H':mul(reach,h),'I':reach*infl(v),'dH':Z,'fees':fee,'retired':F(0),'remaining_old':sum(2*reach*F(sum(v[x]!=v[x^(1<<coords.index(j))] for x in range(len(v))),len(v)) for j in (0,1,2) if j in coords)}
 original=t[0];i=coords.index(original);cc=tuple(x for x in coords if x!=original);parts=[]
 for bit in (0,1):parts.append(rec(t[bit+1],cut(v,i,bit),project(ref,i),cc,fixed+(original,),reach/2))
 out={k:add(parts[0][k],parts[1][k]) for k in ('CE','KL','H','dH','fees')}
 local=sub(h,mul(F(1,2),add(H(p_of(cut(v,i,0))),H(p_of(cut(v,i,1))))))
 out['dH']=add(out['dH'],mul(reach,local));out['fees']=add(out['fees'],fee)
 ii=F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
 out['I']=sum(x['I'] for x in parts);out['retired']=sum(x['retired'] for x in parts)+2*reach*ii;out['remaining_old']=sum(x['remaining_old'] for x in parts)
 return out
minimum=None;records=[]
for t in trees:
 v=rec(t);total=add(add(v['CE'],v['dH']),v['fees']);m=sub(sub(capacity,old),total)
 simple=sub(initial,add(v['KL'],v['fees']));ck(sub(m,simple)[0]<=0<=sub(m,simple)[1]);ck(m[0]>F(3,10));ck(v['retired']+v['remaining_old']==F(5,4))
 if minimum is None or m[0]<minimum[0]:minimum=m
 records.append({'tree':t,'margin_bits':m,'full_terminal_KL_bits':v['KL'],'all_conversion_fees_bits':v['fees'],'executed_entropy_bits':v['dH'],'remaining_I':v['I']})
chain=(0,(1,(2,('stop',),('stop',)),(2,('stop',),('stop',))),(1,(2,('stop',),('stop',)),(2,('stop',),('stop',))))
fixed=next(x for x in records if x['tree']==chain);ck(fixed['margin_bits'][0]>F(5,8));ck(fixed['all_conversion_fees_bits'][0]>0)
fixed_values=rec(chain)
query_owner=sub(sub(mul(F(5,8),K),old),fixed_values['dH'])
terminal_owner=sub(mul(F(1,4),K),fixed_values['CE'])
ck(query_owner[0]>F(1,32));ck(terminal_owner[0]>F(23,32));ck(fixed_values['fees'][1]<F(1,8));ck(3**12>2**19)
# Independent full-reference trace for the concrete next private query.
frontier=[(f,q)]
for step in range(3):
 nextfront=[]
 for vv,qq in frontier:
  for bit in (0,1):
   vnew=cut(vv,0,bit);qnew=project(qq,0)
   if step==1:qnew,_=update(p_of(vnew),qnew)
   nextfront.append((vnew,qnew))
 frontier=nextfront
expected=(F(229,352),F(229,352),F(29,32),F(29,32),F(277,352),F(277,352),F(29,32),F(29,32))
ck(tuple(qq[0] for vv,qq in frontier)==expected)
next_target={'status':'UNPRICED_NEXT_PRIVATE_QUERY','physical_query':'original U, index0 in each current [U,V,z] terminal','root_truth':f,'original_root_Q':q,'K':'4+2/ln2','original_root_I':'7/8','original_old_booking':'5/(4ln2), retained once','paid_half_profile_conversion_bits':fixed_values['fees'],'current_original_owner_margin_bits':fixed['margin_bits'],'terminals':[{'reach':'1/8','truth':vv,'P':p_of(vv),'Q_current':qq,'coords':['U','V','z'],'full_KL_bits':KL(p_of(vv),qq)} for vv,qq in frontier],'required_next_bill':'Retain original K Iroot, old booking and executed half-profile fee; add the actual next entropy cost and use complete post-query terminal KL. No renewed variance source or stale conditional means.'}
(R/'out/NEXT_TARGET_U.json').write_text(json.dumps(enc(next_target),indent=2)+'\n',encoding='utf-8')
# Retaining the same old booking in a REMAINING-only account has a universal
# nonnegative-cost floor at this frontier, irrespective of a reference choice.
floor=sub(mul(F(1,4),K),old);ck(floor[1]<0);ck(l2hi<F(3,4))
out={'status':'PASS','assertions':checks,'cases':244,'all_margin_bits_gt':'3/10','minimum_margin_bits_interval':minimum,'fixed_third_query_chain':fixed,'fixed_query_owner_surplus_bits':query_owner,'fixed_terminal_owner_surplus_bits':terminal_owner,'fixed_conversion_bits':fixed_values['fees'],'integer_owner_certificate':'3^12>2^19 implies3-H(root)>1/32','remaining_influence_floor':floor,'records':records,'seconds':time.perf_counter()-start}
(R/'out/INDEPENDENT_REPLAY.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':checks,'cases':244,'minimum_margin_bits':list(map(float,minimum)),'fixed_chain_margin_bits':list(map(float,fixed['margin_bits'])),'seconds':out['seconds']}))
