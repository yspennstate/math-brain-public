from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
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
src=Path('agents/A012/runs/20261023T053904Z-account03-A012-sparse-activation-accounting/out/NEXT_TARGET.json')
d=json.loads(src.read_text(encoding='utf-8'));q=list(map(F,d['root_Q']));f=d['F']
def spectrum(v):
 return [F(sum(a*(1-2*((x&t).bit_count()%2)) for x,a in enumerate(v))**2,len(v)**2) for t in range(len(v))]
def infl(v):
 return F(sum(v[x]!=v[x^(1<<j)] for j in range((len(v)-1).bit_length()) for x in range(len(v))),len(v))
def factor(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def addlog(a,w,x):
 for s,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in factor(n).items():a[p]=a.get(p,F(0))+s*w*e
 return {p:c for p,c in a.items() if c}
def ce_sig(p,q):
 sig={}
 for x,y in zip(p,q):
  if x:ck(y>0);sig=addlog(sig,x,1/y)
 return sig
def linear(*terms):
 out={}
 for w,s in terms:
  for p,c in s.items():out[p]=out.get(p,F(0))+w*c
 return {p:c for p,c in out.items() if c}
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def sub(a,b):return (a[0]-b[1],a[1]-b[0])
def scale(w,a):return (w*a[0],w*a[1]) if w>=0 else (w*a[1],w*a[0])
@lru_cache(None)
def log2_interval(x):
 # floor(log2(n^4096/d^4096)) is certified by exact integer comparisons.
 x=F(x);n=x.numerator**4096;den=x.denominator**4096;k=n.bit_length()-den.bit_length()
 def holds(j):return n>=(den<<j) if j>=0 else (n<<(-j))>=den
 if not holds(k):k-=1
 ck(holds(k) and not holds(k+1))
 return F(k,4096),F(k+1,4096)
def sig_interval(s):
 out=(F(0),F(0))
 for p,c in s.items():out=add(out,scale(c,log2_interval(F(p))))
 return out
ln2lo=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(20)),F(0))
ln2hi=ln2lo+F(2,41*3**41)*F(9,8)
invln2=(1/ln2hi,1/ln2lo);K=add((F(4),F(4)),scale(2,invln2));old=scale(F(5,4),invln2)
states={}
for s in product((-1,0,1),repeat=3):
 free=[j for j in range(6) if j>=3 or s[j]==-1]
 verts=[x for x in range(64) if all(a==-1 or (x>>j&1)==a for j,a in enumerate(s))]
 v=[f[x] for x in verts];p=spectrum(v)
 qp=[sum(q[t] for t in range(64) if sum(((t>>j)&1)<<k for k,j in enumerate(free))==mask) for mask in range(len(v))]
 i=infl(v);sig=ce_sig(p,qp);c=sig_interval(sig)
 states[s]={'p':p,'q':qp,'f':v,'i':i,'sig':sig,'ce':c,'margin':sub(sub(scale(i,K),c),old)}
 ck(sum(p)==sum(qp)==1)
root=(-1,-1,-1);a=states[root];ck(a['p']==q)
childp=[spectrum(d[k]) for k in ('G','H')]
childsig=[ce_sig(p,p) for p in childp]
# For this actual target each private conditional spectrum is uniform, so its
# 15/16 mixture with the supplied uniform private prior is exactly P_child.
for p in childp:ck(all(x==F(1,64) for x in p[8:]))
avgchildsig=linear((F(1,2),childsig[0]),(F(1,2),childsig[1]))
avgchildce=sig_interval(avgchildsig)
postvariance=sub((F(3),F(3)),avgchildce)
# Exact reconciliation of ORIGINAL root stock as postvariance child bank plus
# UNUSED selector allowance; no second variance debit/refund is inserted.
delta=linear((1,a['sig']),(-1,avgchildsig))
selector=sub(add((F(1,2),F(1,2)),scale(F(1,2),invln2)),sig_interval(delta))
ck(sub(a['margin'],add(postvariance,selector))[0]<=0<=sub(a['margin'],add(postvariance,selector))[1])
one=[]
for j in range(3):
 daughters=[]
 for b in (0,1):
  s=list(root);s[j]=b;daughters.append(states[tuple(s)])
 i=sum(x['i'] for x in daughters)/2
 cs=linear((F(1,2),daughters[0]['sig']),(F(1,2),daughters[1]['sig']))
 gamma=linear((1,a['sig']),(-1,cs));tau=sub(scale(a['i']-i,K),sig_interval(gamma))
 remain=sub(postvariance,tau);margin=sub(sub(scale(i,K),sig_interval(cs)),old)
 if j==0:ck(remain[0]>F(1,4));ck(tau[0]>0 and tau[1]<F(1,2));ck(selector[0]>F(1,2))
 else:ck(remain[1]<0 and margin[0]>0)
 one.append({'query':j,'remaining_I':i,'queried_influence':a['i']-i,'gamma_log2_signature':gamma,'tau_bits':tau,'remaining_original_CHILD_bank_bits':remain,'remaining_FULL_bank_bits':margin,'daughter_off_target_reference_mass':[sum(y for p,y in zip(x['p'],x['q']) if not p) for x in daughters],'daughter_KLs_bits':[sig_interval(linear((1,x['sig']),(-1,ce_sig(x['p'],x['p'])))) for x in daughters]})
# Reconstruct all244 policy trees from their saved syntax, by direct weighted
# terminal sums; independently telescope the signed local bills along nodes.
author=json.loads((R/'out/HISTORY.json').read_text(encoding='utf-8'));positive=negative=0;bad=[]
def leafsum(tree,state=root,reach=F(1)):
 if tree[0]=='stop':
  x=states[state];return reach*x['i'],linear((reach,x['sig'])),[]
 j=tree[0];ck(state[j]==-1);ii=F(0);ss={};bills=[];ds=[]
 for b in (0,1):
  st=list(state);st[j]=b;st=tuple(st);ds.append(states[st]);i,s,bb=leafsum(tree[b+1],st,reach/2);ii+=i;ss=linear((1,ss),(1,s));bills+=bb
 here=states[state];gamma=linear((1,here['sig']),(-F(1,2),ds[0]['sig']),(-F(1,2),ds[1]['sig']))
 di=here['i']-(ds[0]['i']+ds[1]['i'])/2
 ck(di>=0);ck(sig_interval(gamma)[1]>=0)
 bills.append((reach,di,gamma))
 return ii,ss,bills
for row in author['policies_detail']:
 i,s,bills=leafsum(row['tree']);ck(i==F(row['I']))
 m=sub(sub(scale(i,K),sig_interval(s)),old)
 total=sub(scale(sum(w*di for w,di,g in bills),K),sig_interval(linear(*[(w,g) for w,di,g in bills])))
 ck(linear((1,a['sig']),(-1,s),* [(-w,g) for w,di,g in bills])=={})
 ck(sum(w*di for w,di,g in bills)==a['i']-i)
 ck(sub(sub(a['margin'],total),m)[0]<=0<=sub(sub(a['margin'],total),m)[1])
 sign=1 if m[0]>0 else -1 if m[1]<0 else 0;ck(sign!=0)
 ck(sign==(1 if F(row['margin_ln'][0])>0 else -1))
 if sign>0:positive+=1
 else:negative+=1;bad.append({'tree':row['tree'],'margin_bits':m,'I':i,'CE_signature':s})
# Fixed two-query policy s0 then s1 on BOTH outcomes is a simple control.
fixed2=[0,[1,['stop'],['stop']],[1,['stop'],['stop']]]
i,s,_=leafsum(fixed2);fixedmargin=sub(sub(scale(i,K),sig_interval(s)),old);ck(fixedmargin[1]<-F(15,64))
ck(positive==30 and negative==214)
out={'status':'PASS','assertions':checks,'policies':244,'positive':positive,'negative':negative,'postvariance_original_child_bank_bits':postvariance,'unused_original_selector_allowance_bits':selector,'one_query':one,'two_query_control':{'tree':fixed2,'remaining_I':i,'CE_signature':s,'margin_bits':fixedmargin},'root_CE_signature':a['sig'],'child_CE_signatures':childsig,'source_child_average_I':F(3,4),'old_booking': '5/(4ln2)','original_variance_debit':'1/(4ln2)','worst_negative':min(bad,key=lambda x:x['margin_bits'][0]),'seconds':time.perf_counter()-start}
(R/'out/HISTORY_REPLAY.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':checks,'positive':positive,'negative':negative,'child_bank':list(map(float,postvariance)),'s0_tau':list(map(float,one[0]['tau_bits'])),'s0_child_remainder':list(map(float,one[0]['remaining_original_CHILD_bank_bits'])),'two_query_margin':list(map(float,fixedmargin)),'seconds':out['seconds']}))
