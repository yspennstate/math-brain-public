from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
import sys,time,json,hashlib
sys.dont_write_bytecode=True
import owner20 as o
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
base=o.ROOTF;initialrefs=(o.ROOTQ,o.ROOTQ)
root=tuple(base[x&63]*base[x>>6] for x in range(4096))
def prod(p,q):return tuple(a*b for b in q for a in p)
@lru_cache(None)
def sp(v):return o.spec(v)
@lru_cache(None)
def hh(v):return o.ent(sp(v))
def locals_at(assigned,block):
 fixed={j-6*block:b for j,b in assigned if j//6==block}
 coords=tuple(j for j in range(6) if j not in fixed)
 v=tuple(base[x] for x in range(64) if all(x>>j&1==b for j,b in fixed.items()))
 return v,coords
o.ck(sp(root)==prod(o.ROOTP,o.ROOTP));o.ck(o.influence(root)==F(7,4));o.ck(hh(root)==o.linear((2,o.ROOTH)))
def chooser(available,assigned,mode):
 if mode==0:return min(available)
 if mode==1:return max(available)
 obs=sum((b+1)*(j+1) for j,b in assigned);depth=len(assigned)
 return min(available,key=lambda j:((j*(2*mode+1)+obs*(mode+3)+(j//6)*depth*(mode+1))%17,j))
def recurse(mode,v=root,coords=tuple(range(12)),refs=initialrefs,assigned=(),updated=(False,False),reach=F(1)):
 refs=list(refs);updated=list(updated);fee={};transaction_count=0
 local=[];localcoords=[]
 for b in range(2):
  lv,lc=locals_at(assigned,b);local.append(lv);localcoords.append(lc)
  fixed={j-6*b for j,bit in assigned if j//6==b}
  if fixed=={0,1} and not updated[b]:
   before=prod(refs[0],refs[1]);new,c=o.half_profile(sp(lv),refs[b]);refs[b]=new
   after=prod(refs[0],refs[1]);o.ck(o.kl(after,before)==c)
   fee=o.linear((1,fee),(reach,c));updated[b]=True;transaction_count+=1
 refs=tuple(refs);updated=tuple(updated)
 available=tuple(j for j in coords if j in (0,1,2,6,7,8));obs=sum((b+1)*(j+1) for j,b in assigned)
 stop=not available or (mode>=8 and len(assigned)>=2 and (obs+mode+len(assigned))%5==0)
 if stop:
  p=sp(v);q=prod(*refs);o.ck(p==prod(sp(local[0]),sp(local[1])));o.ck(sum(q)==1)
  ce=o.ce(p,q);kl=o.kl(p,q)
  o.ck(ce==o.linear((1,o.ce(sp(local[0]),refs[0])),(1,o.ce(sp(local[1]),refs[1]))))
  o.ck(kl==o.linear((1,o.kl(sp(local[0]),refs[0])),(1,o.kl(sp(local[1]),refs[1]))))
  o.ck(o.influence(v)==o.influence(local[0])+o.influence(local[1]))
  digest=hashlib.sha256(json.dumps(o.enc([p,q])).encode('utf-8')).hexdigest()
  return {'ce':o.linear((reach,ce)),'kl':o.linear((reach,kl)),'h':o.linear((reach,hh(v))),'queryh':{},'fees':fee,'I':reach*o.influence(v),'conversions':transaction_count,'leaves':[{'reach':reach,'physical_fixed':assigned,'complete_P_Q_sha256':digest,'off_target_mass':sum(y for x,y in zip(p,q) if not x),'full_KL':kl}]}
 query=chooser(available,assigned,mode);i=coords.index(query);nextcoords=tuple(j for j in coords if j!=query);parts=[]
 for bit in (0,1):
  nextrefs=list(refs);b=query//6;nextrefs[b]=o.marginal(nextrefs[b],localcoords[b].index(query%6))
  parts.append(recurse(mode,o.cofactor(v,i,bit),nextcoords,tuple(nextrefs),assigned+((query,bit),),updated,reach/2))
 out={k:o.linear((1,parts[0][k]),(1,parts[1][k])) for k in ('ce','kl','h','queryh','fees')}
 dh=o.linear((1,hh(v)),(-F(1,2),hh(o.cofactor(v,i,0))),(-F(1,2),hh(o.cofactor(v,i,1))))
 out['queryh']=o.linear((1,out['queryh']),(reach,dh));out['fees']=o.linear((1,out['fees']),(1,fee));out['I']=sum(x['I'] for x in parts)
 out['conversions']=sum(x['conversions'] for x in parts)+transaction_count;out['leaves']=parts[0]['leaves']+parts[1]['leaves']
 return out
records=[]
for mode in range(12):
 x=recurse(mode);o.ck(o.linear((1,x['h']),(1,x['queryh']),(-1,hh(root)))=={})
 cost=o.linear((1,x['ce']),(1,x['queryh']),(1,x['fees']));o.ck(cost==o.linear((1,hh(root)),(1,x['kl']),(1,x['fees'])))
 margin=o.linear((4*F(7,4),{2:F(1)}),(-1,cost));const=F(1)
 iv=o.interval(margin,const);o.ck(o.interval(o.linear((1,margin),(-F(3,5),{2:F(1)})),const)[0]>0)
 records.append({'mode':mode,'margin_bits':o.bits(iv),'margin_natural':iv,'complete_cost_signature':cost,'full_terminal_KL':x['kl'],'all_conversion_fees':x['fees'],'actual_executed_entropy':x['queryh'],'remaining_I':x['I'],'transaction_nodes':x['conversions'],'leaves':x['leaves']})
out={'status':'PASS','policies':12,'truth_entries':4096,'assertions':o.CHECKS,'minimum_margin_bits':min(row['margin_bits'][0] for row in records),'records':records,'seconds':time.perf_counter()-start,'all_dimensions_claim':'Only m=2 tested; all finite m/all adaptive policies require DERIVATION tensor proof.'}
o.save('TENSOR.json',out)
print(json.dumps({'status':'PASS','policies':12,'assertions':o.CHECKS,'minimum_margin_bits':float(out['minimum_margin_bits']),'seconds':out['seconds']}))
