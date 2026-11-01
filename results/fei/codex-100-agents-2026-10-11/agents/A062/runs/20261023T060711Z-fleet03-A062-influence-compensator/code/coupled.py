"""Actual interacting Boolean controls; preserve original and actual child reference."""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import sys,json,time
sys.dont_write_bytecode=True
import kernel as k
from check import plus,scale,log,hb,kl_atoms,serial,LOGE_LO
ROOT=Path(__file__).resolve().parents[1]
def spectrum(tt):
 w=k.walsh(tt);return {s:F(v*v,len(tt)**2) for s,v in enumerate(w)}
def block_laws(p,dims):
 result=[];offset=0
 for dim in dims:
  row={s:F(0) for s in range(1<<dim)}
  for s,v in p.items():row[(s>>offset)&((1<<dim)-1)]+=v
  result.append(row);offset+=dim
 return result
def tensor(rows,dims):
 ans={}
 for s in range(1<<sum(dims)):
  v=F(1);offset=0
  for row,dim in zip(rows,dims):v*=row[(s>>offset)&((1<<dim)-1)];offset+=dim
  ans[s]=v
 return ans
def marginals(p,n):return [sum(v for s,v in p.items() if s&(1<<j)) for j in range(n)]
def marginal_product(ds):return {s:prod(d if s&(1<<j) else 1-d for j,d in enumerate(ds)) for s in range(1<<len(ds))}
def entropy(p):return plus(*(scale(log(v),-v) for v in p.values() if v))
def eligible(pp,rr,dim):
 ds=marginals(pp,dim);q=marginal_product(ds)
 if pp==q:return {'eligible':True,'reason':'zero total correlation; no reset obstacle'}
 if not all(0<d<1 for d in ds):return {'eligible':False,'reason':'degenerate marginal; not reduced here'}
 if pp[0]<q[0]:return {'eligible':False,'reason':'empty dominance fails'}
 weights={s:rr[s]/q[s] for s in pp if s}
 if not all(v>0 for v in weights.values()):return {'eligible':False,'reason':'reference nonempty shape not positive'}
 single=weights[1]
 if dim<2:return {'eligible':True,'reason':'singleton block'}
 lam=weights[3]/single
 return {'eligible':0<lam<=1 and all(v==single*lam**(s.bit_count()-1) for s,v in weights.items()),'reason':'exact common-attenuation equations','lambda_candidate':lam}
def account(p,R,dims):
 ds=marginals(p,sum(dims));M=plus(*(hb(d) for d in ds));H=entropy(p);K=kl_atoms(p,R);TC=k.sub(M,H);T=k.sub(TC,K)
 pb=block_laws(p,dims);Rb=block_laws(R,dims);productR=tensor(Rb,dims)
 coupling=plus(*(scale(log(R[s]/productR[s]),v) for s,v in p.items() if v))
 local=[]
 for pp,rr,dim in zip(pb,Rb,dims):
  mm=plus(*(hb(d) for d in marginals(pp,dim)));ce=plus(*(scale(log(rr[s]),-v) for s,v in pp.items() if v));local.append(k.sub(mm,ce))
 difference=k.sub(T,plus(*local,coupling));k.check(difference[0]<=0<=difference[1])
 k.check(sum(R.values())==sum(p.values())==1 and all(R[s]>0 for s,v in p.items() if v))
 return {'I':sum(ds),'H':H,'M':M,'K':K,'TC':TC,'T':T,'block_T':local,'coupling':coupling,'block_eligibility':[eligible(pp,rr,dim) for pp,rr,dim in zip(pb,Rb,dims)],'reference_factorizes':R==productR,'source_factorizes':p==tensor(pb,dims),'marginals':ds}
def root_reference(p,widths,choice):
 if choice=='coordinate-product':return marginal_product(marginals(p,sum(widths)))
 rows=[]
 for pp,dim in zip(block_laws(p,widths),widths):
  ds=marginals(pp,dim);q=marginal_product(ds);empty=pp[0]
  k.check(0<empty<1 and 0<q[0]<1)
  rows.append({s:(empty if s==0 else (1-empty)*v/(1-q[0])) for s,v in q.items()})
 return tensor(rows,widths)
def run(widths,flip,choice):
 n=sum(widths);truth=[]
 for x in range(1<<n):
  offset=bit=0
  for w in widths:bit^=int(((x>>offset)&((1<<w)-1))==0);offset+=w
  truth.append(bit^int(x==flip))
 truth=bytes(truth);p=spectrum(truth);R=root_reference(p,widths,choice);root=account(p,R,widths)
 eligible=[]
 for pp,dim in zip(block_laws(p,widths),widths):
  ds=marginals(pp,dim);eligible.append(all(0<d<1 for d in ds) and pp[0]>=prod(1-d for d in ds))
 if all(eligible):k.check(F(root['T'][1],k.SCALE)<=LOGE_LO*root['I'])
 k.check(root['reference_factorizes'])
 children=[]
 for i in range(n):
  a,b=k.children(truth,i);bit=1<<i;erase=lambda s:(s&(bit-1))|((s>>(i+1))<<i)
  q={s:F(0) for s in range(1<<(n-1))};bar=dict(q)
  for s,v in p.items():q[erase(s)]+=v;bar[erase(s)]+=R[s]
  k.check(F(sum(x!=y for x,y in zip(a,b)),len(a))==root['marginals'][i])
  dims=list(widths);dims[0 if i<widths[0] else 1]-=1
  pred=[];ks=[]
  for outcome,tt in enumerate((a,b)):
   pc=spectrum(tt);un={s:bar[s]*(pc[s]/(2*q[s]) if q[s] else F(1,2)) for s in q};pi=sum(un.values());k.check(pi>0);pred.append(pi)
   rc={s:v/pi for s,v in un.items()};row=account(pc,rc,dims);row.update({'query':i,'outcome':outcome,'prediction':pi,'source':pc,'inherited_reference':rc,'dimensions':dims});children.append(row);ks.append(row['K'])
  k.check(sum(pred)==1)
  E=k.sub(root['K'],kl_atoms(q,bar));O=kl_atoms({0:F(1,2),1:F(1,2)},dict(enumerate(pred)))
  chain=k.sub(root['K'],plus(E,O,scale(plus(*ks),F(1,2))));k.check(chain[0]<=0<=chain[1])
 return {'widths':widths,'flip':flip,'original_reference':choice,'root':root,'root_block_eligible':eligible,'children':children}
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;families=[[2,3]] if pilot else [[2,3],[3,3],[3,4]];rows=[]
 for widths in families:
  points=[1] if pilot else [0,1,1<<widths[0],1+(1<<widths[0])]
  for flip in points:
   for choice in ['coordinate-product','block-source-empty']:
    rows.append(run(widths,flip,choice))
    (ROOT/'out/COUPLED_PARTIAL.json').write_text(json.dumps(serial(rows)),encoding='utf-8')
    k.check(time.monotonic()-start<55)
 childrows=[(r,c) for r in rows for c in r['children']]
 positive=[(r,c) for r,c in childrows if c['coupling'][0]>0]
 negative=[(r,c) for r,c in childrows if c['coupling'][1]<0]
 witness=None
 if positive:
  r,c=max(positive,key=lambda rc:rc[1]['coupling'][0]);witness={'widths':r['widths'],'flip':r['flip'],'original_reference':r['original_reference'],'child':c}
  k.check(not c['reference_factorizes'])
 out={'status':'PASS','roots':len(rows),'child_rows':len(childrows),'positive_coupling_rows':len(positive),'negative_coupling_rows':len(negative),'nonfactorized_child_references':sum(not c['reference_factorizes'] for r,c in childrows),'root_eligibility_failures':sum(not all(r['root_block_eligible']) for r in rows),'child_block_eligibility_failures':sum(not all(t['eligible'] for t in c['block_eligibility']) for r,c in childrows),'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start,'witness':witness,'results':rows,'scope':'coupling identity checked, not a theorem that coupling tax or reset reserve is paid'}
 (ROOT/'out'/('COUPLED_PILOT.json' if pilot else 'COUPLED.json')).write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
 print(json.dumps({s:out[s] for s in ['status','roots','child_rows','positive_coupling_rows','negative_coupling_rows','nonfactorized_child_references','root_eligibility_failures','assertions','seconds']}))
if __name__=='__main__':main()
