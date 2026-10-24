from pathlib import Path
import json,time
import exact as e
from exact import Q,ck,add,Lv,scalar,vint,save
path=Path('~/brain_workers/FEI100_20261011/agents/A013/runs/20261014T021710Z-account05-A013-representation-stability/out/PROFILE_CERTIFICATES.json')
source=json.loads(path.read_text(encoding='utf-8'));ck(len(source)==8)
profiles=json.loads((e.ROOT/'out/CONTINUUM_CERTIFICATES.json').read_text())['profiles'];results=[]
for row in source:
    d=Q(row['d']);ck(d==Q(1,8*(1<<row['r'])))
    total={}
    for c in profiles[row['pattern']]:
        A=(Q(c)-d)**2;B=d*d;total=add((1,total),(1,Lv(A)),(1,Lv(B)),(-1,Lv(A+B)))
    gap=add((1,scalar(2*d+16*d*d)),(-1,total));declared={int(p):Q(v) for p,v in row['gap_prime_log'].items()}
    ck(gap==declared);interval=vint(gap);ck(interval[0]>0)
    ck(Q(row['gap_interval'][0])<=interval[0] and interval[1]<=Q(row['gap_interval'][1]))
    results.append({'pattern':row['pattern'],'r':row['r'],'verdict':'HOLDS_EXACT_VECTOR_AND_INTERVAL','positive_lower':str(Q((interval[0]*(1<<48)).numerator//(interval[0]*(1<<48)).denominator,1<<48))})
save('SOURCE_REVIEW_RESULTS.json',{'status':'PASS_SCOPED_ONLY','certificates':results,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start,'scope':'eight new finite phase certificates and classification; no independent full-chain acceptance of own A012 input'})
print({'status':'PASS_SCOPED_ONLY','assertions':e.checks})
