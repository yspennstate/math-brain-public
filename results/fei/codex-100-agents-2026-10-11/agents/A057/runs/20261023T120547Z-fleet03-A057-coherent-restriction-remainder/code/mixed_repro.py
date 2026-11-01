from pathlib import Path
from fractions import Fraction as Q
import time,json
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T060651Z-fleet03-A057-coherent-restriction-remainder/code/independent_repro.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for code in ([0,3,5,15]')[0],ns)
H,mix,ph,positive,restrict=[ns[k] for k in ['H','mix','ph','positive','restrict']]
start=time.monotonic();checks=nodes=leaves=positiveold=0
def ck(b):
 global checks
 assert b;checks+=1
 if time.monotonic()-start>55:raise RuntimeError('frozen55s cap')
G=tuple(-1 if y==0 else 1 for y in range(8))
table=tuple(G[(a>>4)&7]*(-1)**((a>>7).bit_count()) if a&15==15 else (-1)**((a&1)*(a>>1&1)+(a>>2&1)*(a>>3&1)) for a in range(512))
order=[4,7,0,8,1];terminalH={};terminalB={};sumD={}
def ticket(fix):
 if 4 not in fix or all(j in fix for j in [7,8]):return {}
 g=tuple(G[y] for y in range(8) if y&1==fix[4]);q=Q(sum(g),len(g))**2
 r=sum(i in fix for i in range(4));t=Q(1,1<<(4-r)) if all(fix.get(i,1)==1 for i in range(4)) else Q(0)
 return mix((q,ph(t)),(t,ph(q)),(1,{2:Q(9,2)*t*q}))
def walk(fix,depth,B,reach):
 global checks,nodes,leaves,positiveold,terminalH,terminalB,sumD
 vals,rem=restrict(table,fix);T=ticket(fix)
 ck(positive(mix((1,B),(-1,T),(-1,{2:Q(7,8)}))))
 if depth==len(order):
  terminalH=mix((1,terminalH),(reach,H(vals)));terminalB=mix((1,terminalB),(reach,B));leaves+=1;return
 i=order[depth];hs=[]
 for bit in [0,1]:
  ff=dict(fix);ff[i]=bit;vc,rc=restrict(table,ff);hs.append(H(vc))
 D=mix((1,H(vals)),(-Q(1,2),hs[0]),(-Q(1,2),hs[1]));ck(positive(D));sumD=mix((1,sumD),(reach,D));nodes+=1
 if depth==0:ck(positive(mix((1,D),(-1,{2:Q(1,16000)}))));positiveold=1
 for bit in [0,1]:
  ff=dict(fix);ff[i]=bit;walk(ff,depth+1,mix((1,B),(-1,D)),reach/2)
walk({},0,{2:Q(7)},Q(1))
ck(sumD==mix((1,H(table)),(-1,terminalH)))
ck(sumD==mix((1,{2:Q(7)}),(-1,terminalB)))
out={'status':'PASS','query_order':order,'physical_internal_nodes':nodes,'full_terminal_leaves':leaves,'positive_old_debit':positiveold,'exact_assertions':checks,'seconds':time.monotonic()-start,'arithmetic':'independent direct character sums and48-term rigorous log bounds','exact_entropy_and_original_owner_telescopes':'PASS'}
(ROOT/'out/mixed_repro.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
