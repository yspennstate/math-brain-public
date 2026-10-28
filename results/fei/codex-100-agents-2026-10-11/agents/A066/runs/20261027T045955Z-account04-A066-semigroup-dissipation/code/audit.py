"""Direct-character and full-GL reconstruction; imports no primary checker."""
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
import time,json
start=time.monotonic(); count=cases=0
def check(x):
    global count
    count+=1
    assert x
    if time.monotonic()-start>55: raise RuntimeError('55s cap')
def inner(x,y): return sum(((x>>j)&1)*((y>>j)&1) for j in range(3))%2
def linear(cols,s):
    a=0
    for j in range(3):
        if (s>>j)&1:a^=cols[j]
    return a
maps=[]
for cols in product(range(1,8),repeat=3):
    vals=[linear(cols,s) for s in range(8)]
    if len(set(vals))==8: maps.append(vals)
check(len(maps)==168)
for labels in ((1,),(3,),(1,6)):
    V={0}
    for v in labels: V|={u^v for u in tuple(V)}
    g=[(-1)**inner(labels[0],x) if len(labels)==1 else 1-2*int(inner(1,x)==0 and inner(6,x)==0) for x in range(8)]
    for k in range(5):
        for edits in combinations(range(8),k):
            cases+=1
            f=[-a if x in edits else a for x,a in enumerate(g)]
            coeff=[sum(f[x]*(-1)**inner(s,x) for x in range(8)) for s in range(8)]
            diffs=[v^edits[0] for v in edits[1:]] if edits else []
            group=[T for T in maps if all(T[v]==v for v in V) and all(inner(T[s],w)==inner(s,w) for s in range(8) for w in diffs)]
            for s in range(8):
                orbit={T[s] for T in group}
                expected={s} if s in V else {u for u in range(8) if u not in V and all(inner(u,w)==inner(s,w) for w in diffs)}
                check(orbit==expected)
                check(all(coeff[u]**2==coeff[s]**2 for u in orbit))
            # Direct normalized complete source and its actual group-average.
            Q=[Fraction(s+1,36) for s in range(8)]
            Qbar=[sum((Q[T[s]] for T in group),Fraction())/len(group) for s in range(8)]
            check(sum(Qbar)==1)
            for s in range(8):
                orbit={T[s] for T in group}
                check(all(Qbar[u]==Qbar[s] for u in orbit))
                pr=Fraction(1)
                for u in orbit: pr*=Q[u]
                check(pr<=Qbar[s]**len(orbit))
# The earlier exact two-edit obstruction and its repair, including zero source entries.
g=[(-1)**(x&1) for x in range(8)]
f=[-v if x in (0,1) else v for x,v in enumerate(g)]
p=[Fraction(sum(f[x]*(-1)**inner(s,x) for x in range(8))**2,64) for s in range(8)]
check(p==[Fraction(0),Fraction(1,4),Fraction(0),Fraction(1,4),Fraction(0),Fraction(1,4),Fraction(0),Fraction(1,4)])
old=[Fraction(0),p[1]]+[Fraction(1,8)]*6
check(sum(old)==1 and sum(p[s] for s in (3,5,7))==Fraction(3,4))
check(all(p[s]/old[s]==2 for s in (3,5,7)))
G=[T for T in maps if T[1]==1 and all(inner(T[s],1)==inner(s,1) for s in range(8))]
q=[sum((p[T[s]] for T in G),Fraction())/len(G) for s in range(8)]
check(q==p)
out={'status':'PASS','cases':cases,'exact_assertions':count,'seconds':time.monotonic()-start,'full_GL3_maps':len(maps),'two_edit_old_invoice_bits':'3/4','two_edit_repaired_invoice_bits':'0','independence':'separate author implementation, not independent-agent acceptance'}
root=Path(__file__).resolve().parents[1]
(root/'out'/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
