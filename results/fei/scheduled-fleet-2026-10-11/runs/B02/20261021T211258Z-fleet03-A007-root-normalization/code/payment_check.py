from pathlib import Path
from fractions import Fraction as Q
import time,json
ROOT=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0; forests=0
def ck(x):
    global checks
    assert x; checks+=1
for m in range(2,41):
    a=Q(1,2**m); b=(1-a)**2
    ck(m*a<=Q(1,2)); ck(m*m*a<=Q(9,8)); ck(b>=Q(9,16))
    ck(m<=2**m); ck(Q(11,5)+Q(7,4)+Q(1,20)==4)
    ck(4*m*m*a+Q(211,10)*m*a<=Q(301,20))
    ck(Q(301,20)/Q(9,16)+Q(63,40)==Q(10199,360)<29)
    if m>=3: ck((m+1)**2<=2*m*m)
    if m<=4:
        edges=[{i,m+j} for i in range(m) for j in range(m)]
        for T in range(1,1<<(2*m)):
            coords={i for i in range(2*m) if T>>i&1}
            owned={}
            for i in coords:
                owner=next(h for h,R in enumerate(edges) if i in R)
                owned.setdefault(owner,set()).add(i)
            gates=sorted(owned); n=len(gates)
            adj=[[bool(owned[h]&edges[l]) for l in gates] for h in gates]
            reach=[row[:] for row in adj]
            for k in range(n):
                for i in range(n):
                    for j in range(n): reach[i][j]|=reach[i][k] and reach[k][j]
            comps=[]; left=set(range(n))
            while left:
                i=min(left); comp={j for j in left if reach[i][j] and reach[j][i]}
                comps.append(comp); left-=comp
            roots=[]
            for C in comps:
                if not any(adj[i][j] for i in range(n) if i not in C for j in C): roots.append(min(C))
            seen=set(roots); queue=roots[:]; parents={}
            while queue:
                i=queue.pop(0)
                for j in range(n):
                    if j not in seen and adj[i][j]: seen.add(j); queue.append(j); parents[j]=i
            ck(len(seen)==n); ck(n<=len(coords)); ck(len(roots)<=len(coords))
            for h in gates:
                sl=len(owned[h]); kap=len(coords&edges[h])
                ck(1<=sl<=kap<=2); ck(Q(kap,sl)<=2)
            # Label and root rarity coarse lower bound, before congestion/rank.
            ck(Q(1,m)**n*Q(1,4)**len(roots)>=Q(1,4*m)**len(coords))
            forests+=1
    ck(time.monotonic()-start<55)
d={'status':'PASS','assertions':checks,'selected_forests':forests,'seconds':time.monotonic()-start,
   'scope':'finite independent validation; the all-m statement uses the written induction and source transfer'}
(ROOT/'out/payment_checks.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8'); print(json.dumps(d))
