from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
import importlib.util,json,time,hashlib,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
old=R.parent/'20261023T031904Z-fleet03-A073-certified-logarithms/code/check.py'
sp=importlib.util.spec_from_file_location('own_exact_boolean',old);b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
def save(n,d):(O/n).write_text(json.dumps(d,indent=2,default=str)+'\n',encoding='utf-8')
def coreq(blocks,ass,alpha):
 qs=[]
 for block in blocks:
  labels=[a for a in block if a not in ass];k=len(labels)
  if any(ass.get(a,1)==0 for a in block):q={0:F(1)}
  elif k<=1:q=b.pointq(labels)
  else:
   d=F(1,1<<k);q={sum(1<<labels[j] for j in range(k) if s>>j&1):(1-alpha)*4*d*d for s in range(1,1<<k)}
   q[0]=(1-2*d)**2;q[sum(1<<a for a in labels)]+=alpha*4*d*(1-d)
  qs.append(q)
 return b.tensor(qs)
def lift(node,q):
 ref={s:v for s,v in node.p.items() if s>>3==0}
 for s,v in q.items():
  if s:
   for x in (0,1):ref[s|x]=v/4
 assert sum(ref.values())==1
 return b.Node(node.t,node.labels,ref)
def diff(p,new,old):
 if new==old:return F(0),F(0)
 lo,hi=b.ce(p,new);a,c=b.ce(p,old);return lo-c,hi-a
def data_spectrum(node):
 return {s:v for s,v in node.p.items() if s>>3}
def nonempty_profile(q):
 d={}
 for s,v in q.items():
  if s>>3:d[s&~1]=d.get(s&~1,F(0))+v
 z=sum(d.values())
 return {s:v/z for s,v in d.items()} if z else {}
def hypothetical(blocks,ass,order,bits,alpha):
 # Independent core-only recurrence representation.  Ignore global vacuum
 # rows of the activation, whose incoming reference need not be calibrated.
 qs=[]
 for block in blocks:
  remaining=[a for a in block if a not in ass]
  if any(ass.get(a,1)==0 for a in block):q={0:F(1)};alive=False
  else:q=coreq([block],ass,alpha);alive=True
  for j,y in zip(order,bits):
   if j not in remaining:continue
   k=len(remaining);remaining.remove(j)
   if not alive or y==0 or k<=2:
    alive=alive and bool(y);q=b.pointq(remaining) if alive and len(remaining)==1 else {0:F(1)}
    continue
   d=F(1,1<<k);a=q[1<<remaining[0]];c=q[0];full=q[sum(1<<z for z in remaining)+(1<<j)]
   c1=(c+a)*(1-4*d)**2/(1-4*d+8*d*d);a1=4*a;full1=2*(a+full)
   z=c1+((1<<len(remaining))-2)*a1+full1
   q={sum(1<<remaining[j] for j in range(len(remaining)) if s>>j&1):a1/z for s in range(1,1<<len(remaining))}
   q[0]=c1/z;q[sum(1<<j for j in remaining)]=full1/z
  qs.append(q)
 return b.tensor(qs)
def run(pilot=False):
 start=time.monotonic();widthslist=[(3,)] if pilot else [(3,),(4,),(2,3),(3,3)]
 ik=0 if pilot else 1;sk=1 if pilot else 2;alpha=F(1,7)
 count=sum(sum(len(list(permutations(range(sum(w)),k)))*2**k*2*sum(len(list(permutations(range(sum(w)-k),l)))*2**l for l in range(sk+1)) for k in range(ik+1)) for w in widthslist)
 tag='PILOT' if pilot else 'MAIN'
 save(tag+'_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_helper_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'family':'actual A050 point-tensor lift; b, incoming data prefix, a BOTH signs, first full alpha1/7 reset; one chosen sign has ordered data suffix then second full alpha1/7 reset; all complements retained','widths':widthslist,'incoming_prefix_max':ik,'suffix_max':sk,'case_count':count,'symmetry':'none','arithmetic':'Fraction actual truth tables/Walsh/coherent references; fixed16-term certified atanh bounds; integer products','memory_MB':160,'max_runtime_seconds':55 if pilot else 240})
 cases=checks=negative=0;fixture=None
 for widths in widthslist:
  root,blocks,_,_=b.make(widths);data=tuple(a for block in blocks for a in block)
  ce0=b.ce(root.p,root.q);H0=b.ent(root.p);A0=(ce0[0]-H0[1],ce0[1]-H0[0]);assert 4*root.I-ce0[1]>1
  b0=root.child(2,0);b1=root.child(2,1)
  for k in range(ik+1):
   for order in permutations(data,k):
    for bits in product((0,1),repeat=k):
     ass=dict(zip(order,bits));node=b1;w=F(1,2);base=[(w,b0)]
     for j,y in zip(order,bits):base.append((w/2,node.child(j,1-y)));node=node.child(j,y);w/=2
     children=[node.child(1,y) for y in (0,1)];first=[lift(n,coreq(blocks,ass,alpha)) for n in children]
     ds=[diff(n.p,r.q,n.q) for n,r in zip(children,first)];sig1lo=w*sum(t[0] for t in ds)/2;sig1hi=w*sum(t[1] for t in ds)/2
     remaining=tuple(j for j in data if j not in ass)
     for y in (0,1):
      for ell in range(sk+1):
       for suffix in permutations(remaining,ell):
        for outcomes in product((0,1),repeat=ell):
         assert time.monotonic()-start<(55 if pilot else 240)
         cur=first[y];leaves=list(base)+[(w/2,first[1-y])];reach=w/2;ass2=dict(ass)
         for j,z in zip(suffix,outcomes):leaves.append((reach/2,cur.child(j,1-z)));cur=cur.child(j,z);reach/=2;ass2[j]=z
         target=lift(cur,coreq(blocks,ass2,alpha));lo,hi=diff(cur.p,target.q,cur.q)
         if cur.q!=target.q:assert hi<0;negative+=1
         else:assert lo==hi==0
         checks+=1
         hyp=hypothetical(blocks,ass,suffix,outcomes,alpha);hn={s:v for s,v in hyp.items() if s};hz=sum(hn.values());hn={s:v/hz for s,v in hn.items()} if hz else {}
         assert nonempty_profile(cur.q)==hn;checks+=1
         # Mutating the vacuum mass is deliberately NOT part of the hypothesis:
         # actual zero-data rows are compared by their full conditional KL.
         leaves.append((reach,target));assert sum(t for t,n in leaves)==1;checks+=1
         hlo=hhi=F(0);If=F(0);termKLlo=F(0)
         for t,n in leaves:
          a,c=b.ent(n.p);hlo+=t*a;hhi+=t*c;If+=t*n.I
          d,e=b.ce(n.p,n.q);termKLlo+=t*(d-c)
         assert 4*If-hhi>F(3,4);checks+=1
         ehi=H0[1]-hlo-4*(root.I-If)
         net_hi=A0[1]+ehi+sig1hi+reach*hi
         reserve=4*If-hhi-max(F(0),net_hi)-F(1,4)
         assert reserve>=F(3,4);checks+=1
         assert termKLlo<=A0[1]+sig1hi+reach*hi;checks+=1
         cases+=1
         if widths==(4,) and k==0 and y==1 and suffix==(3,4) and outcomes==(1,1):
          fixture={'widths':widths,'a_outcome':y,'suffix':suffix,'outcomes':outcomes,'source_spectrum':cur.p,'inherited_reference':cur.q,'fresh_reference':target.q,'signed_reset_interval':[lo,hi],'first_reset_interval':[sig1lo,sig1hi],'second_weight':reach,'old_booking':F(1,4),'remaining_same_owner_lower':reserve,'full_terminal_count':len(leaves)}
  save(tag+'_CHECKPOINT.json',{'root':widths,'cases':cases,'checks':checks,'status':'PASS_so_far'})
 assert cases==count
 save(tag+'_CHECK.json',{'status':'PASS','cases':cases,'checks':checks,'strictly_negative_resets':negative,'alpha':alpha,'same_original_reserve':'>=3/4 after old1/4','runtime_seconds':time.monotonic()-start,'finite_scope':'frozen prefixes only; arbitrary widths/load/histories are proved analytically in PROOF.md'})
 if fixture:save('ACTIVATION_FIXTURE.json',fixture)
 assert 7**4<2*6**4
 save('FIRST_RESET_INTEGER_SIGN.json',{'claim':'log2(7/6)<1/4','lhs':7**4,'rhs':2*6**4,'positive_integer_margin':2*6**4-7**4})
 print(json.dumps({'mode':tag,'status':'PASS','cases':cases,'checks':checks,'negative':negative,'runtime_seconds':time.monotonic()-start}))
if __name__=='__main__':run('--pilot' in sys.argv)
