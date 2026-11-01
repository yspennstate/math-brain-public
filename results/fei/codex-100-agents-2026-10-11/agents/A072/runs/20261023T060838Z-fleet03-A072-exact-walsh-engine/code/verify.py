"""Author audit: direct characters, subset hulls and forward path capital."""
from admission import F,Q,ROOT,add,sub,scale,mean,compare,maximum,entropy,record,save,factor
from functools import lru_cache
from itertools import product
import json,time

start=time.perf_counter();checks=0
def ck(b):
    global checks
    assert b
    checks+=1

@lru_cache(None)
def HG(m):
    if m==0:return {}
    N=1<<m
    return add(entropy([F((N-2)**2,N*N)]),scale(entropy([F(4,N*N)]),N-1))
def infl(r,t):
    m=r+t
    return F(r)+F(2*(m-2*r),1<<m) if m else F(0)
def need(r,t):return maximum([('zero',{}),('deficit',sub(HG(r+t),{2:infl(r,t)}))])[1]

w=json.loads((ROOT/'out/CONSTRUCTED_WITNESS.json').read_text(encoding='utf-8'))
t=tuple(w['truth']);N=len(t);W=[sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
ck(W==w['integer_Walsh']);ck(W==[N*(s==14)-2 for s in range(N)])
ck(sum(z*z for z in W)==N*N)
for x in range(N):ck(sum(W[s]*(-1 if (s&x).bit_count()%2 else 1) for s in range(N))==N*t[x])
eds=[sum(t[x]!=t[x|1<<i] for x in range(N) if not x>>i&1) for i in range(4)]
ck(eds==w['edge_counts']);ck(F(2*sum(eds),N)==infl(3,1));ck(HG(4)==entropy([F(z*z,N*N) for z in W]))

@lru_cache(None)
def local(p,M):
    # Different critical algorithm: enumerate subsets of the unique zero path.
    if 1 in p:return {}
    available=[i for i in range(4) if p[i]<0 and M>>i&1];pay=[]
    for code in range(1<<len(available)):
        done={available[k] for k in range(len(available)) if code>>k&1}
        r=sum(p[i]<0 and i not in done for i in [1,2,3]);d=int(p[0]<0 and 0 not in done)
        pay.append((code,scale(need(r,d),F(1,1<<len(done)))))
    return maximum(pay)[1]
root=(-1,)*4;R=local(root,15);ck(R=={2:F(1,4)})
payoffs=[];nodes=0
def paths(p,M,offset):
    global nodes
    nodes+=1
    r=sum(p[i]<0 for i in [1,2,3]);d=int(p[0]<0)
    b={} if 1 in p else need(r,d)
    payoffs.append((nodes,sub(b,offset)))
    if 1 in p:return # pure parity: all future local hulls/deltas/needs vanish
    for i in range(4):
        if p[i]>=0:continue
        if M>>i&1:
            kids=[p[:i]+(v,)+p[i+1:] for v in [0,1]]
            rs=[local(c,M) for c in kids];av=mean(rs)
            for c,rr in zip(kids,rs):paths(c,M,add(offset,sub(rr,av)))
        else:paths(p,M|1<<i,offset)
paths(root,0,{})
T=maximum(payoffs)[1];ck(T=={2:F(1,2)});ck(json.loads(json.dumps(record(R)))==w['full_hull']);ck(json.loads(json.dumps(record(T)))==w['robust_capital'])

# Fixed formula-only checks, not a growing truth-table search.
rows=[]
for d in range(17):
    n=d+3;ck(compare(sub({2:infl(3,d)},HG(n)),{})>0)
    rs=[(str((r,j)),scale(need(r,j),F(1,1<<(n-r-j)))) for r in range(4) for j in range(d+1)]
    winner,Rd=maximum(rs);bound={2:F(8*(n+1),1<<n)}
    ck(compare(Rd,{})>0);ck(compare(Rd,bound)<=0)
    # This direct analytic atom formula avoids constructing 2^n coefficients.
    NN=1<<n;p0=F((NN-2)**2,NN*NN);pv=F(4,NN*NN)
    ck(HG(n)==add(entropy([p0]),scale(entropy([pv]),NN-1)))
    rows.append({'d':d,'I':str(infl(3,d)),'root_slack':record(sub({2:infl(3,d)},HG(n))),'global_hull':record(Rd),'attaining_remaining_counts':winner,'upper_bound':str(F(8*(n+1),1<<n)),'robust_capital_lower_bound':'1/2'})
    ck(time.perf_counter()-start<120)
save('FAMILY_FORMULA_CHECKS.json',rows)
result={'verdict':'PASS','method':'direct integer characters; unique-zero-path subset hulls; independent forward path capital; fixed d0..16 exact formula checks','checks':checks,'forward_nodes_pruned_after_pure_parity':nodes,'full_hull':record(R),'robust_capital':record(T),'runtime_seconds':time.perf_counter()-start,'external_independent_review':False}
save('AUDIT.json',result);print(json.dumps(result))
