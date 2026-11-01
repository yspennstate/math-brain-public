import exact as e
from exact import Q,ck,cutoff,save,logint
from pathlib import Path
import json,time,hashlib
S=Path(r'~\brain_workers\FEI100_20261011\agents\A013\runs\20261014T051241Z-fleet05-A013-representation-stability')
def Phi(A,B):
    if not A or not B:return Q(0)
    return A*logint(1+B/A)[1]+B*logint(1+A/B)[1]
total=0;receipts=[]
for j in range(8):
    path=S/f'out/CONTINUUM_{j}.json';v=json.loads(path.read_text());ck(v['status']=='PASS');rel=v['profile']['relative_sign'];groups=[[Q(x)for x in g]for g in v['profile']['groups']]
    leaves={tuple(map(Q,c['p']+c['q'])):c for c in v['certificates']};used=set()
    for (lp,hp,lq,hq),cert in leaves.items():
        cutoff();lower=(lp+lq+lp*lp+lq*lq)/4
        for g in range(2):
            sig=rel*(-1 if g else 1);kl=(lp+(lq if sig==1 else -hq))/8;kh=(hp+(hq if sig==1 else -lq))/8
            for a in groups[g]:lower-=Phi(max((a-kl)**2,(a-kh)**2),max(kl*kl,kh*kh))
        ck(lower>=Q(cert['gap_lower'])>0);total+=1
    def tree(lp,hp,lq,hq,depth):
        if (hp+hq)/8<=Q(1,32)or(lp+lq)/8>=Q(1,6):return
        key=(lp,hp,lq,hq)
        if key in leaves:used.add(key);return
        ck(depth<4);mp=(lp+hp)/2;mq=(lq+hq)/2
        for a,b in((lp,mp),(mp,hp)):
            for c,d in((lq,mq),(mq,hq)):tree(a,b,c,d,depth+1)
    for x in range(16):
        for y in range(16):tree(Q(x,16),Q(x+1,16),Q(y,16),Q(y+1,16),0)
    ck(used==set(leaves));receipts.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
save('SOURCE_REVIEW_RESULTS.json',{'status':'PASS','scope':'All4093 saved rectangle signs and exact subdivision coverage ONLY; no source full chain, profile classification, covers or independent acceptance claimed','source_claim':'A013-TWO-ROW-ARBITRARY-EVENT-TRANSPORT@1','contributor_conflict':'A012 supplied earlier ownership/one-row inputs; scoped reconstruction not full-chain independence','certificates':total,'assertions':e.checks,'elapsed':time.perf_counter()-e.start,'receipts':receipts});print(total,e.checks,time.perf_counter()-e.start)
