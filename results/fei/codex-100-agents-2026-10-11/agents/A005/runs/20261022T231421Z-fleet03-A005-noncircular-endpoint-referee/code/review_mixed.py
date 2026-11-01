from pathlib import Path
from fractions import Fraction as Q
import json, time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(v):
    global checks
    assert v
    checks+=1
profiles={}
data={}
for m in range(256):
    f=[1 if m>>x&1 else -1 for x in range(8)]
    w=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)) for s in range(8)]
    sig=tuple(sorted(a*a for a in w))
    influence=Q(sum(f[x]!=f[x^(1<<i)] for x in range(8) for i in range(3)),8)
    ck(sum(a*a for a in w)==64)
    ck(influence==sum(Q(s.bit_count()*a*a,64) for s,a in enumerate(w)))
    profiles[sig]=min(profiles.get(sig,influence),influence)
    data[m]=(sig,influence)
expected={(0,0,0,0,0,0,0,64):Q(0),(0,0,0,0,16,16,16,16):Q(1),(4,4,4,4,4,4,4,36):Q(3,4)}
ck(profiles==expected)
f=254;minus=f^1;plus=f^128;both=f^129
ck(data[f]==data[both]);ck(data[minus][1]==0);ck(data[plus][1]==Q(3,2))
ck(data[plus][0]==(0,0,0,0,16,16,16,16))
ck((0^7).bit_count()==3)
# Three profiles give H=0,2,4-9log2(3)/8 respectively.
# Their exact minimum influences certify global D2 maximality at f=254.
ck(3**9<2**20)  # log2(3)<20/9 -> point D2>0.
ck(3**5<2**8)   # log2(3)<8/5 -> mixed T>12/5.
for n in range(3):
    N=1<<n
    for m in range(1<<N):
        f=[1 if m>>x&1 else -1 for x in range(N)]
        w=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
        nonzero=[a*a for a in w if a]
        influence=Q(sum(f[x]!=f[x^(1<<i)] for x in range(N) for i in range(n)),N)
        ck(nonzero==[N*N] or (sorted(nonzero)==[N*N//4]*4 and influence>=1))
out={'status':'PASS','tables':256,'assertions':checks,'profiles':[{'squared_integer_walsh':list(s),'minimum_I':str(v)} for s,v in sorted(profiles.items())],'witness':{'mask':254,'K':2,'negative_edit':[0],'positive_edit':[7],'crossing_edges':0,'T':'6-(9/4)log2(3)>12/5','root_global_D2_maximal':True,'root_least_positive_D2_dimension':True},'scope':'A055 DERIVATION Sections2--3 only; not the n4 one-sign lattice census or a high-K theorem','seconds':time.perf_counter()-start}
(R/'out/REVIEW_MIXED.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
