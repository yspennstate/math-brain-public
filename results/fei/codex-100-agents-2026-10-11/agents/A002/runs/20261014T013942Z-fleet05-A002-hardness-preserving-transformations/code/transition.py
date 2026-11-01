from pathlib import Path
from fractions import Fraction as Q
import time,json
import check as V
R=Path(__file__).resolve().parents[1];start=time.perf_counter();V.deadline=start+60
C=Q(8,3);seed=V.vals(3,254);out=[]
for t in [1,2,3]:
    d,rows=V.root(V.tensor_values(seed,3,t),C)
    V.ck(V.sign(d)>0)
    V.ck(all(V.sign(r['sigma'])==(1 if t<3 else -1) for r in rows))
    V.ck(all(r['q']==rows[0]['q'] for r in rows))
    out.append({'t':t,'dimension':3*t,'delta_interval':[str(x) for x in V.interval(d)],'sigma_sign':1 if t<3 else -1,'corrected_price_interval':[str(x) for x in V.interval(rows[0]['q'])]})
t=2;k=3;p=Q(1,8);core=V.tensor_values(seed,3,t)
g=[core[x&63]*(-1 if x>>6 else 1) for x in range(128)]
active=[g[x&127] if x>>7==0 else 1 for x in range(1024)]
edited=[active[x&1023] for x in range(4096)];edited[0]*=-1
controls=[]
for vals,name in [(active,'activation'),(edited,'full_support_edit')]:
    a,pp,h,I=V.measure(tuple(vals));delta,rows=V.root(vals,C)
    V.ck(V.sign(delta)>0);V.ck(I<Q(1));V.ck(max(r['d'] for r in rows)<Q(1,4));V.ck(a.get(0,Q(0))>Q(3,4))
    if name=='full_support_edit':V.ck(len(a)==4096)
    controls.append({'name':name,'dimension':len(vals).bit_length()-1,'I':str(I),'mean':str(a.get(0,Q(0))),'delta_interval':[str(x) for x in V.interval(delta)]})
result={'status':'PASS','helper_version':'A002-positive-gap-transition-v1','roots':5,'exact_assertions':V.checks,'failures':0,'seconds':time.perf_counter()-start,'tensor_transition':out,'rare_full_support_controls':controls}
(R/'out/TRANSITION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':result['status'],'roots':5,'exact_assertions':V.checks,'seconds':result['seconds']}))
