"""Full signed ledger for one private DATA exposure after control histories."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,importlib.util,itertools,json,time
HERE=Path(__file__).resolve().parent.parent
OLD=HERE.parent/'20261022T211502Z-fleet03-A068-antichain-beyond-one-order'/'code'/'verify.py'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()=='af436c9eaac4e0f2617d170517f163636ef03d669d83b7e93ca41ee3f0fde5d0'
sp=importlib.util.spec_from_file_location('arithmetic',OLD);a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
START=time.monotonic()
def project(p,keep):
 out=[F(0)]*(1<<len(keep))
 for s,t in enumerate(p):out[sum(((s>>j)&1)<<k for k,j in enumerate(keep))]+=t
 return out
def restrict(truth,assignment):
 n=(len(truth)-1).bit_length();D=dict(assignment);free=[j for j in range(n) if j not in D]
 base=sum(bit<<j for j,bit in D.items())
 return [truth[base+sum(((z>>k)&1)<<j for k,j in enumerate(free))] for z in range(1<<len(free))],free
def policies(remaining=(0,3,4),assignment=()):
 if 0 not in remaining:yield (assignment,),()
 for j in remaining:
  rest=tuple(k for k in remaining if k!=j)
  for ll,li in policies(rest,assignment+((j,0),)):
   for rl,ri in policies(rest,assignment+((j,1),)):
    yield ll+rl,((assignment,j),)+li+ri
POLICIES=list(policies());assert len(POLICIES)==131
def fixture(h,beta):
 ny=(len(h)-1).bit_length();controlvars=(ny+1,ny+2)
 ph=[v*v for v in a.walsh(h)]
 qh=[(v+int(i==0))/2 for i,v in enumerate(ph)]
 gh=a.ce(ph,qh);Ih=sum(a.influence(h));p=(1+F(sum(beta),4))/2
 a.nonnegative(a.combine((1,{2:F(143,16)*Ih}),(-1,gh)),'supplied complete h rate premise')
 qroot=[F(0)]*(2*len(h))
 for s,v in enumerate(qh):qroot[2*s]=(1-p)*v
 qroot[1]+=p
 qafter=[(1-p)*v for v in qh];qafter[0]+=p
 truth=[(-1 if z&1 else 1) if beta[z>>(ny+1)]==1 else h[(z>>1)&(len(h)-1)] for z in range(8*len(h))]
 nodes={}
 for labels in itertools.product((-1,0,1),repeat=3):
  ass=tuple((j,bit) for j,bit in zip((0,)+controlvars,labels) if bit!=-1)
  f,free=restrict(truth,ass);coeff=a.walsh(f);P=[v*v for v in coeff]
  phase,_=restrict(beta,[(j-ny-1,bit) for j,bit in ass if j>=ny+1]);pb=[v*v for v in a.walsh(phase)]
  D=dict(ass)
  d=F(1,2) if 0 not in D else F(sum(v!=(-1 if D[0] else 1) for v in h),len(h))
  C=[d*v for v in pb];C[0]+=1-d
  qdata=qroot if 0 not in D else qafter
  nd=ny+1 if 0 not in D else ny
  R=[u*v for v in C for u in qdata]
  a.check(sum(R)==1,'current full reference normalized')
  gamma=a.ce(P,R);inf=a.influence(f)
  for z,v in enumerate(C):a.check(sum(P[z*len(qdata)+i] for i in range(len(qdata)))==v,'actual activation profile after DATA/control queries')
  nodes[frozenset(ass)]={'P':P,'R':R,'C':C,'G':gamma,'I':sum(inf),'IC':sum(inf[nd:]),'free':free,'inf':inf,'nd':nd}
 edges={}
 for key,parent in nodes.items():
  for j in (0,)+controlvars:
   if j not in parent['free']:continue
   relative=parent['free'].index(j)
   inherited=project(parent['R'],[k for k in range(len(parent['free'])) if k!=relative])
   if j==0:inheritedC=parent['C']
   else:
    controlpos=[v for v in parent['free'] if v>=ny+1].index(j)
    inheritedC=project(parent['C'],[k for k in range((len(parent['C'])-1).bit_length()) if k!=controlpos])
   children=[]
   for bit in (0,1):
    child=nodes[key|{(j,bit)}]
    oldbill=a.ce(child['P'],inherited)
    kl=a.combine((1,a.ce(child['C'],inheritedC)),(-1,a.entropy(child['C'])))
    a.nonnegative(kl,'actual source-return credit nonnegative')
    a.check(a.combine((1,oldbill),(-1,child['G']),(-1,kl))=={},'DATA/control return FULL credit exact')
    children.append(child)
   debit=a.combine((1,{2:25*parent['inf'][relative]}),(F(1,2),children[0]['G']),(F(1,2),children[1]['G']),(-1,parent['G']))
   edges[(key,j)]=debit
 root=nodes[frozenset()]
 rootbank=a.combine((1,{2:25*root['I']}),(-1,root['G']))
 count=0
 for leaves,internal in policies((0,)+controlvars):
  gamma={};I=IC=F(0);debit={}
  for ass in leaves:
   nd=nodes[frozenset(ass)];weight=F(1,1<<len(ass))
   gamma=a.combine((1,gamma),(weight,nd['G']));I+=weight*nd['I'];IC+=weight*nd['IC']
  for ass,j in internal:debit=a.combine((1,debit),(F(1,1<<len(ass)),edges[(frozenset(ass),j)]))
  a.check(I-IC==(1-p)*Ih,'all-path DATA cut remaining core influence')
  bank=a.combine((1,{2:25*I}),(-1,gamma))
  a.check(a.combine((1,rootbank),(-1,debit),(-1,bank))=={},'SAME original owner minus ALL old DATA/control transactions')
  a.nonnegative(a.combine((1-p,gh),(1,{2:4*Ih+2*IC}),(-1,gamma)),'private literal exposure inherited-source bound')
  a.nonnegative(a.combine((1,bank),(-1,{2:(1-p)*Ih/F(16)+23*IC})),'rate25 same-owner remainder after DATA cut')
  count+=1
 return count,len(nodes)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
 result={'status':'RUNNING','pilot':args.pilot};parents=policies_count=nodecount=0
 try:
  for h in itertools.product((-1,1),repeat=4):
   for code in range(16):
    beta,r=a.quadratic(2,code)
    count,nodes=fixture(h,beta);parents+=1;policies_count+=count;nodecount+=nodes
    if time.monotonic()-START>55:raise RuntimeError('frozen runtime exhausted')
    if args.pilot and parents==8:break
   if args.pilot and parents==8:break
  targeted=0
  if not args.pilot:
   for k in (1,3,5):
    h=(1,)+(-1,)*((1<<k)-1)
    for code in (0,2,8):
     beta,r=a.quadratic(2,code)
     count,nodes=fixture(h,beta);parents+=1;policies_count+=count;nodecount+=nodes;targeted+=1
     if time.monotonic()-START>55:raise RuntimeError('frozen runtime exhausted')
  result.update(status='PASS',parents=parents,policy_frontiers=policies_count,partial_nodes=nodecount,targeted_parents=targeted)
 except Exception as exc:
  result.update(status='FAIL',error=repr(exc),parents=parents,policy_frontiers=policies_count);raise
 finally:
  result.update(assertions=a.CHECKS,certified_log_signs=len(a.SIGN_CACHE),seconds=time.monotonic()-START,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
  path=HERE/'out'/('transfer_pilot.json' if args.pilot else 'transfer.json')
  path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
