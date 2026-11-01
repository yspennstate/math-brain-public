from pathlib import Path
from fractions import Fraction as F
import json,hashlib,itertools,time
import adaptive as h
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'out/FULL.json').read_text(encoding='utf-8'))
assert d['status']=='PASS' and {x['mask'] for x in d['records']}==set(range(256))
checks=0; ratios=[]
for x in d['records']:
 W=tuple(F(a) for a in x['all_policy_total_booking']);S=tuple(F(a) for a in x['original_mean_S4'])
 assert 20*W[1]<S[0];checks+=1;ratios.append((W[1]/S[0],x['mask']))
m=max(ratios)[1];v=tuple(1 if m&(1<<s) else -1 for s in range(8));root=h.compose(v)
seen=set();witnesses=[]
def visit(t,labels,path):
 key=(t,labels)
 if key in seen:return
 seen.add(key)
 P=h.add(h.stats(t)[3],h.worst(t))
 for i,label in enumerate(labels):
  cs,D,O,Z=h.transaction(t,i)
  for b,c in enumerate(cs):
   C=h.add(h.stats(c)[3],h.worst(c));gain=h.sub(C,P)
   if gain[0]>0:
    witnesses.append({'path':path,'next_label':label,'outcome':b,'child_reach_from_original_root':str(F(1,2**(len(path)+1))),'parent_reference_potential':h.enc(P),'child_reference_potential':h.enc(C),'gain':h.enc(gain),'query_signed_debit':h.enc(D),'reference_only_mass':str(Z)})
   visit(c,labels[:i]+labels[i+1:],path+[(label,b)])
for b in (0,1):visit(h.child(root,1,b),('x','b','y0','y1','y2'),[('a',b)])
assert witnesses
w=max(witnesses,key=lambda x:(len(x['path']),F(x['gain'][0])))
o={'status':'PASS','strict_one_twentieth_comparisons':checks,'maximum_upper_ratio':str(max(ratios)[0]),'maximizing_core':m,'witness_states':len(seen),'branch_growth_witness':w,'seconds':time.perf_counter()-h.START,'helper_sha256':hashlib.sha256((R/'code/adaptive.py').read_bytes()).hexdigest(),'full_certificate_sha256':hashlib.sha256((R/'out/FULL.json').read_bytes()).hexdigest()}
assert o['seconds']<20
(R/'out/READBACK.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
print(json.dumps(o))
