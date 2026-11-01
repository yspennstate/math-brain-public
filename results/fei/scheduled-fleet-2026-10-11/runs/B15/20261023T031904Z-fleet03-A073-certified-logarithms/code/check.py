from fractions import Fraction as F
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
def save(n,o):(O/n).write_text(json.dumps(o,indent=2,default=str)+'\n',encoding='utf-8')
@lru_cache(None)
def ln(q):
 q=F(q);e=0
 while q<1:q*=2;e-=1
 while q>=2:q/=2;e+=1
 def unit(x):
  t=(x-1)/(x+1);s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(16)),F(0))
  return s,s+2*t**33/(33*(1-t*t))
 a,b=unit(q);c,d=unit(F(2))
 return (a+e*c,b+e*d) if e>=0 else (a+e*d,b+e*c)
def log2(q):
 a,b=ln(q);c,d=ln(F(2))
 return (a/d,b/c) if a>=0 else ((a/c,b/d) if b<=0 else (a/c,b/c))
def ce(p,q):
 a=b=F(0)
 for s,v in p.items():
  x,y=log2(1/q[s]);a+=v*x;b+=v*y
 return a,b
def ent(p):return ce(p,p)
def spec(t,labels):
 w=list(t);step=1
 while step<len(w):
  for i in range(0,len(w),2*step):
   for j in range(i,i+step):a,b=w[j],w[j+step];w[j],w[j+step]=a+b,a-b
  step*=2
 return {sum(1<<labels[j] for j in range(len(labels)) if s>>j&1):F(v*v,len(t)**2) for s,v in enumerate(w) if v}
def influence(t,labels):
 return sum((F(sum(t[s]!=t[s^(1<<j)] for s in range(len(t))),len(t)) for j in range(len(labels))),F(0))
def marg(q,j):
 d={}
 for s,v in q.items():d[s&~(1<<j)]=d.get(s&~(1<<j),F(0))+v
 return d
class Node:
 def __init__(self,t,labels,q):
  self.t=tuple(t);self.labels=tuple(labels);self.p=spec(t,labels);self.q=q
  assert sum(q.values())==1 and all(q.get(s,0)>0 for s in self.p)
  self.I=sum((s.bit_count()*v for s,v in self.p.items()),F(0))
  assert self.I==influence(t,labels)
 def child(self,j,y):
  k=self.labels.index(j);labels=tuple(a for a in self.labels if a!=j)
  t=[self.t[(s&((1<<k)-1))|((s>>k)<<(k+1))|(y<<k)] for s in range(1<<len(labels))]
  p=spec(t,labels);pe=marg(self.p,j);qe=marg(self.q,j)
  q={s:v*(p.get(s,F(0))/(2*pe[s]) if pe.get(s,0) else F(1,2)) for s,v in qe.items()}
  z=sum(q.values());assert z>0
  return Node(t,labels,{s:v/z for s,v in q.items() if v})
def pointq(labels):
 k=len(labels)
 if not k:return {0:F(1)}
 if k==1:return {1<<labels[0]:F(1)}
 d=F(1,1<<k);p0=(1-2*d)**2;v=4*d*(1-d);full=sum(1<<a for a in labels)
 q={sum(1<<labels[j] for j in range(k) if s>>j&1):F(7,2)*d*d for s in range(1,1<<k)}
 q[0]=p0;q[full]+=v/8
 return q
def tensor(qs):
 d={0:F(1)}
 for q in qs:d={s|t:v*w for s,v in d.items() for t,w in q.items()}
 return d
def make(widths):
 blocks=[];j=3
 for r in widths:blocks.append(tuple(range(j,j+r)));j+=r
 def h(s):return (-1)**sum(all(s>>a&1 for a in b) for b in blocks)
 coreq=tensor([pointq(b) for b in blocks]);corep=spec([h(s<<3) for s in range(1<<(j-3))],tuple(range(3,j)))
 t=[(-1)**(s>>1&1) if not s&1 else (h(s) if s>>2&1 else 1) for s in range(1<<j)]
 p=spec(t,tuple(range(j)));q={s:v for s,v in p.items() if s>>3==0}
 for s,v in coreq.items():
  if s:
   for c in (0,1,4,5):q[s|c]=v/16
 return Node(t,tuple(range(j)),q),blocks,corep,coreq
def fresh(blocks,assignment):
 return tensor([pointq(tuple(a for a in b if a not in assignment)) if all(assignment.get(a,1)==1 for a in b) else {0:F(1)} for b in blocks])
def quotient(corep,coreq,assignment,p):
 mp,mq=corep,coreq
 for a in assignment:mp,mq=marg(mp,a),marg(mq,a)
 raw={s:v*mq[s]/mp[s] for s,v in p.items()};z=sum(raw.values())
 return {s:v/z for s,v in raw.items()}
def shape_reference(blocks,order,bits):
 qs=[]
 for block in blocks:
  labels=list(block);q=pointq(labels);alive=True
  for a,y in zip(order,bits):
   if a not in labels:continue
   k=len(labels);labels.remove(a)
   if not alive or not y or k<=2:
    alive=alive and bool(y)
    q=pointq(labels) if alive and len(labels)==1 else {0:F(1)}
    continue
   d=F(1,1<<k);full=sum(1<<j for j in [a]+labels)
   c=q[0];ordinary=q[1<<labels[0]];b=q[full]
   cnew=(c+ordinary)*(1-4*d)**2/(1-4*d+8*d*d)
   anew=4*ordinary;bnew=2*(ordinary+b)
   z=cnew+((1<<len(labels))-2)*anew+bnew
   q={sum(1<<labels[j] for j in range(len(labels)) if mask>>j&1):anew/z for mask in range(1,1<<len(labels))}
   q[0]=cnew/z;q[sum(1<<j for j in labels)]=bnew/z
  if alive and len(labels)>=2:
   full=sum(1<<a for a in labels);u=F(1,1<<len(labels));v=F(1,1<<len(block))
   assert q[full]/q[1<<labels[0]]==1+(1-v)/(7*u)
  qs.append(q)
 return tensor(qs)

def main():
 start=time.monotonic();widthslist=[(2,),(3,),(4,),(2,3),(3,3),(5,)]
 count=sum(sum(len(list(permutations(range(sum(w)),k)))*2**k for k in range(3)) for w in widthslist)
 save('PHYSICAL_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'actual A050 Boolean lift of heterogeneous point tensors','roots':widthslist,'prefixes':'every ordered distinct data prefix of length0,1,2, all outcomes; b1 followed by x pair; retain b0 and all siblings; then test each next core data query with fresh factor reset','case_count':count,'symmetry':'none','arithmetic':'Fraction Walsh, coherent reference transport, fixed16-term certified atanh logarithms','memory_MB':120,'max_runtime_seconds':240,'pilot':'stage18 pilot45 cases595 checks completed in1.50s; this frozen domain adds one width5 root and length2 prefixes, no automatic escalation'})
 cases=changed=checks=continuations=0;worst=F(10);fixture=None
 for widths in widthslist:
  root,blocks,cp,cq=make(widths);data=tuple(a for b in blocks for a in b);rce=ce(root.p,root.q);rh=ent(root.p)
  assert 4*root.I-rce[1]>1;checks+=1
  b0=root.child(2,0);b1=root.child(2,1)
  for k in range(3):
   for order in permutations(data,k):
    for bits in product((0,1),repeat=k):
     node=b1;leaves=[(F(1,2),b0)];weight=F(1,2);assignment={}
     for a,y in zip(order,bits):
      leaves.append((weight/2,node.child(a,1-y)));node=node.child(a,y);weight/=2;assignment[a]=y
     char=node.child(0,0);core=node.child(0,1);newq=fresh(blocks,assignment)
     predicted=shape_reference(blocks,order,bits)
     if core.q!=predicted:
      save('TRANSPORT_OBJECTION.json',{'root':widths,'order':order,'bits':bits,'actual':core.q,'predicted':predicted,'completed_cases':cases,'statement':'Physical coherent transport does not equal one-shot cumulative erasure formula on this prefix.'})
      raise AssertionError('three-mass recurrence objection saved')
     checks+=1
     resetnode=Node(core.t,core.labels,newq)
     for a in data:
      if a in assignment:continue
      for y in (0,1):
       child=resetnode.child(a,y);assignment2=dict(assignment);assignment2[a]=y
       q2=fresh(blocks,assignment2);c,d=ce(child.p,q2);a0,b0ce=ce(child.p,child.q)
       if q2!=child.q:assert d-a0<0
       continuations+=1;checks+=1
     assert char.q==char.p=={2:F(1)};checks+=1
     freshce=ce(core.p,newq);oldce=ce(core.p,core.q)
     dl,dh=freshce[0]-oldce[1],freshce[1]-oldce[0]
     if newq==core.q:dl=dh=F(0)
     else:assert dh<0;changed+=1
     checks+=1
     leaves.extend(((weight/2,char),(weight/2,core)))
     assert sum(w for w,n in leaves)==1;checks+=1
     hflo=hfhi=F(0);If=F(0)
     for w,n in leaves:
      a,b=ent(n.p);hflo+=w*a;hfhi+=w*b;If+=w*n.I
     # Include the complete inherited terminal KLs: their weighted sum is part
     # of A, never a replacement for A. Reference-only masses remain in each q.
     inherited_lo=inherited_hi=F(0)
     for w,n in leaves:
      c,d=ce(n.p,n.q);a,b=ent(n.p);inherited_lo+=w*(c-b);inherited_hi+=w*(d-a)
     A=(rce[0]-rh[1],rce[1]-rh[0]);assert inherited_lo<=A[1];checks+=1
     ehi=rh[1]-hflo-4*(root.I-If)
     net_hi=A[1]+ehi+weight*dh/2
     reserve=4*If-hfhi-max(net_hi,F(0))-F(1,4)
     assert reserve>=F(3,4);worst=min(worst,reserve);checks+=1;cases+=1
     if widths==(4,) and order==(3,) and bits==(1,):
      assert len(set(core.p.values()))>1 and newq!=core.q
      fixture={'widths':widths,'assignment':assignment,'actual_core_spectrum':core.p,'inherited_reference':core.q,'fresh_reference':newq,'signed_reset_bits_interval':[dl,dh],'retained_terminal_count':len(leaves),'old_booking':F(1,4),'same_owner_reserve_lower':reserve,'complete_inherited_terminal_KL_interval':[inherited_lo,inherited_hi]}
  save('PHYSICAL_CHECKPOINT.json',{'last_root':widths,'cases':cases,'checks':checks,'changed_nonempty_profiles':changed,'status':'PASS_so_far'})
 assert cases==count and fixture
 save('NONFLAT_FIXTURE.json',fixture)
 save('PHYSICAL_CHECK.json',{'status':'PASS','cases':cases,'checks':checks,'continuation_children':continuations,'changed_nonempty_profiles':changed,'reserve_certified_lower':'3/4','minimum_reserve_lower_interval':worst,'fixed_log_series_terms':16,'runtime_seconds':time.monotonic()-start,'no_claim':'This finite check does not prove the all-width statement; PROOF.md supplies that argument. Sequential unreset prefixes are certified by the three-mass recurrence, not cumulative erasure.'})
 print(json.dumps({'status':'PASS','cases':cases,'checks':checks,'continuation_children':continuations,'changed_nonempty_profiles':changed,'runtime_seconds':time.monotonic()-start}))
if __name__=='__main__':main()
