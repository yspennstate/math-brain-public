"""v1: exact balanced-seed, correlation, and signed Renyi ledger tests."""
from pathlib import Path
import json,time,hashlib
from fractions import Fraction as Q
import check as c

r=Path(__file__).resolve().parents[1]
start=time.monotonic(); count=0
pa,pb=c.spectrum(c.A),c.spectrum(c.B)
ha,hb=c.entropy([p/Q(5,8) for p in pa]),c.entropy([p/Q(3,8) for p in pb])
hm=c.entropy([Q(5,8),Q(3,8)])
def renyi(v):
    # R of normalized squared row; log of rational L1^2/(P*support_count).
    w=c.walsh(v)
    mass=sum(c.spectrum(v))
    rat=Q(sum(abs(x) for x in w)**2,len(v)**2)/mass
    return dict(c.log_vector(rat))
ra,rb=renyi(c.A),renyi(c.B)
c.require(ra=={2:Q(3),3:Q(2),5:Q(-1)})
c.require(rb=={2:Q(1),3:Q(1)})
for n in range(3):
    p=1<<n
    for code in range(1<<p):
        f=[1-2*((code>>j)&1) for j in range(p)]
        hf=c.entropy(c.spectrum(f)); inf=c.energy(f);rf=renyi(f)
        for t in [1,2,3]:
            h=[]
            for j in range(1<<(1+n*t)):
                val=1-2*(j&1)
                for k in range(t):val*=f[(j>>(1+n*k))&(p-1)]
                h.append(val)
            ph=c.spectrum(h)
            c.require(sum(h)==0 and ph[0]==0)
            c.require(c.entropy(ph)==c.add((t,hf)))
            c.require(c.energy(h)==1+t*inf)
            c.require(renyi(h)==c.add((t,rf)))
            truth=[c.A[u]+z*c.B[u]*h[x] for z in [1,-1] for x in range(len(h)) for u in range(16)]
            sp=c.spectrum(truth)
            conditional=c.add((Q(5,8),ha),(Q(3,8),hb),(Q(3,8)*t,hf))
            c.require(c.entropy(sp)==c.add((1,hm),(1,conditional)))
            c.require(c.energy(truth)==Q(5,2)+Q(3,8)*t*inf)
            # Seed-frequency marginal: only branch0 can occupy the empty seed set.
            seedlaw=[Q(5,8)*(j==0)+Q(3,8)*x for j,x in enumerate(ph)]
            mutual=c.add((1,c.entropy(seedlaw)),(-Q(3,8),c.entropy(ph)))
            c.require(mutual==hm)
            gap=c.add((1,hm),(-Q(5,8),ra),(-Q(3,8),rb),(-Q(3,8)*t,rf))
            c.require(gap==c.add((1,{2:Q(3,4),3:Q(-2)}),(-Q(3,8)*t,rf)))
            ledger=c.add((Q(5,8),c.add((1,ha),(1,ra))),
                         (Q(3,8),c.add((1,hb),(1,rb),(t,hf),(t,rf))), (1,gap))
            c.require(ledger==c.entropy(sp))
            count+=1
out={'status':'PASS','balanced_seed_cases':count,'assertions':c.checks,'seconds':time.monotonic()-start,
     'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'Renyi_a':c.as_json(ra),'Renyi_b':c.as_json(rb),'signed_gap_constant':{'2':'3/4','3':'-2'}}
(r/'out/balanced_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
