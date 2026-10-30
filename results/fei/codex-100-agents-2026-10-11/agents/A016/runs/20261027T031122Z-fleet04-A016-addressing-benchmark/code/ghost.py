import json,time
from itertools import product
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def ev(x):return (-1 if x&7==0 else 1)*(-1 if x&25==0 else 1)
def spectrum(t):return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t))**2,len(t)**2) for s in range(len(t))]
orig=[ev(x) for x in range(32)];op=spectrum(orig)
def proj(keep):
    out=[F(0)]*(1<<len(keep))
    for s,v in enumerate(op):out[sum(((s>>i)&1)<<j for j,i in enumerate(keep))]+=v
    return out
def main():
    start=time.perf_counter();rows=[];mx=F(1);witness=None;checks=0
    for ass in product((-1,0,1),repeat=5):
        free=[i for i,v in enumerate(ass) if v<0];base=sum(v<<i for i,v in enumerate(ass) if v>=0)
        truth=[orig[base+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))]
        essential=[j for j in range(len(free)) if any(truth[x]!=truth[x^(1<<j)] for x in range(len(truth)))]
        keep=[free[j] for j in essential];clean=[truth[sum(((x>>j)&1)<<i for j,i in enumerate(essential))] for x in range(1<<len(essential))]
        P=spectrum(clean);unc=proj(free);cl=proj(keep);ratios=[]
        for s,v in enumerate(P):
            if v:
                lift=sum(((s>>j)&1)<<i for j,i in enumerate(essential));ratio=cl[s]/unc[lift]
                assert ratio>=1;checks+=1;ratios.append(str(ratio))
                if ratio>mx:mx=ratio;witness={'assignment':ass,'clean_frequency':s,'ratio':str(ratio)}
        rows.append({'assignment':ass,'free':free,'essential':keep,'actual_support_ratios':ratios})
    out={'status':'PASS','assignments':len(rows),'checks':checks,'max_ratio':str(mx),'witness':witness,'all_original_atoms_at_least_1_over_64':min(op)==F(1,64),'seconds':time.perf_counter()-start,'rows':rows}
    assert out['seconds']<60
    (R/'out/GHOST_ROWS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
