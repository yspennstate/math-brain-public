from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,sys,time
RUN=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
old=RUN.parent/'20261011T234607Z-fleet05-A022-one-point-surgery/code/oddface_surgery.py'
ns={'__file__':str(old),'__name__':'kernel'}
exec(old.read_text(encoding='utf-8').split('\nmaxima={};')[0],ns)
fwht,factors,canonical=ns['fwht'],ns['factors'],ns['canonical']
START=time.perf_counter(); LIMIT=60 if MODE=='pilot' else 1800
checks=0; nodes=0; leaves=0
def ck(ok):
    global checks
    assert ok
    checks+=1
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen runtime')
def add(*terms):
    d=Counter()
    for scale,e in terms:
        for p,v in e:d[p]+=scale*v
    return canonical(d)
def bounds(e):
    lo,hi=ns['expr_interval'](e)
    return Q(lo,ns['SCALE']),Q(hi,ns['SCALE'])
def entropy(w):
    N=len(w); d=Counter({2:Q(2*(N.bit_length()-1))})
    for a,r in Counter(v*v for v in w if v).items():
        for p,e in factors(a):d[p]-=Q(r*a*e,N*N)
    return canonical(d)
def stats(f):
    w=fwht(f);N=len(w);n=N.bit_length()-1
    ck(sum(v*v for v in w)==N*N)
    inf=[Q(sum(v*v for s,v in enumerate(w) if s>>i&1),N*N) for i in range(n)]
    return entropy(w),inf,w
def packet(w):
    d=Counter();N=len(w)
    for (a,b),r in Counter((w[s]**2,w[s+1]**2) for s in range(0,N,2)).items():
        for x,c in ((a+b,a+b),(a,-a),(b,-b)):
            if x:
                for p,e in factors(x):d[p]+=Q(r*c*e,N*N)
    return canonical(d)
def convert(v,m):
    return sum(((v>>(2*i))&1)<<i for i in range(m)) | sum(((v>>(2*i+1))&1)<<(m+i) for i in range(m))
def sign(a,t):return -1 if (a&t).bit_count()%2 else 1
fixtures=[(8,(0,2),(10,12)),(8,(0,5),(10,12)),(8,(0,2),(0,0)),(8,(0,2),(15,15)),
    (12,(0,2,8),(10,12,6)),(12,(0,2,8,32),(10,12,6,8))]
if MODE=='full':
    fixtures += [(12,(0,2,8,10),(15,)*4),(12,(0,2,8,10),(8,)*4),(12,(0,2,8,10),(0,)*4),
        (16,(0,2,8,10,32,34,40,42),(15,)*8),
        (16,(0,2,8,10,32,34,40,42),(10,12,6,8)*2),
        (16,(0,1,4,5,16,17,20,21),(10,12,6,8)*2)]
rows=[]
for case,(k,D,masks) in enumerate(fixtures):
    m=k//2;M=1<<m;ND=1<<k;delta=Q(1,ND);q=len(D)
    ck(q*q<=1<<(m-2));V=tuple(convert(v,m) for v in D)
    ctl=[tuple((mask>>z)&1 for z in range(4)) for mask in masks]
    aw=[fwht(a) for a in ctl]
    ast=[stats(tuple(1-2*x for x in a)) for a in ctl]
    bill=add(*[(delta,s[0]) for s in ast]); ci=[delta*sum(s[1][i] for s in ast) for i in range(2)]
    lookup={v:j for j,v in enumerate(V)}
    f=tuple(sign(x&(M-1),x>>m)*(-1 if x in lookup and ctl[lookup[x]][z] else 1)
        for z in range(4) for x in range(ND))
    H,inf,w=stats(f); ck(inf[k:]==ci)
    # Exact full signed Walsh coefficients, not marginal or squared-only checks.
    for T in range(4):
        for S in range(ND):
            pred=(4*M*sign(S&(M-1),S>>m) if T==0 else 0)
            pred-=2*sum(sign(v&(M-1),v>>m)*(-1 if (S&v).bit_count()%2 else 1)*aw[j][T] for j,v in enumerate(V))
            ck(w[S+ND*T]==pred)
    # All bent edge-correction terms with the actual joint controller expectation.
    for i in range(k):
        total=Q(1,2)
        for j,v in enumerate(V):
            vv=v^(1<<i)
            total+=2*delta*Q(sum(ctl[j]),4)*sign(v&(M-1),v>>m)*sign(vv&(M-1),vv>>m)
            for l in range(j+1,q):
                if V[l]==vv:
                    total-=4*delta*sign(v&(M-1),v>>m)*sign(vv&(M-1),vv>>m)*Q(sum(a*b for a,b in zip(ctl[j],ctl[l])),4)
        ck(total==inf[i])
    def walk(ff,depth,prefix):
        global nodes,leaves
        hh,ii,ww=stats(ff);ndata=k-depth
        if depth==m:
            leaves+=1
            ids=[j for j,v in enumerate(V) if v&(M-1)==prefix]
            lh=add(*[(Q(1,M),ast[j][0]) for j in ids])
            ck(bounds(add((8*sum(ii[:m]),((2,Q(1)),)),(-1,hh),(1,lh)))[0]>=0)
            ck(ii[m:]==[Q(1,M)*sum(ast[j][1][i] for j in ids) for i in range(2)])
            # Reconstruct raw leaf; character cancels from H, changes actual I.
            raw=tuple(1-2*sum(ctl[j][z] for j in ids if V[j]>>m==t) for z in range(4) for t in range(M))
            rh,ri,rw=stats(raw);ck(rh==hh)
            ck(all(ii[i]>=ri[i] for i in range(m)))
            s=sum((Q(sum(ctl[j]),4) for j in ids),Q(0))
            u=sum((Q(sum(ctl[j]),4)**2 for j in ids),Q(0))
            ck(Q(rw[0]**2,(4*M)**2)==(1-2*s/M)**2)
            ck(Q(sum(x*x for x in rw[1:M]),(4*M)**2)==4*u/M-4*s*s/(M*M))
            for T in range(1,4):
                ck(Q(sum(x*x for x in rw[T*M:(T+1)*M]),(4*M)**2)==Q(4,M)*sum(Q(aw[j][T],4)**2 for j in ids))
            return Q(0),sum(ii[:m]),sum(ii[m:]),(),hh
        nodes+=1;d=ii[0];B=packet(ww)
        ck(d>=Q(1,4));ck(bounds(add((4*d,((2,Q(1)),)),(-1,B)))[0]>=0)
        L=walk(ff[::2],depth+1,prefix)
        R=walk(ff[1::2],depth+1,prefix|(1<<depth))
        avg=add((Q(1,2),add((1,L[3]),(1,L[4]))),(Q(1,2),add((1,R[3]),(1,R[4]))))
        gain=add((1,hh),(-1,avg));js=add((1,gain),(-1,B))
        jlo,jhi=bounds(js);ck(jlo>=0);ck(jhi<=2*d*ns['LOG_E'][0])
        return d+(L[0]+R[0])/2,(L[1]+R[1])/2,(L[2]+R[2])/2,add((1,gain),(Q(1,2),L[3]),(Q(1,2),R[3])),add((Q(1,2),L[4]),(Q(1,2),R[4]))
    access,terminal,ctrl,ha,hl=walk(f,0,0)
    ck(access+terminal==sum(inf[:k]));ck(ctrl==sum(inf[k:]));ck(add((1,ha),(1,hl))==H)
    gap=bounds(add((8*sum(inf[:k]),((2,Q(1)),)),(1,bill),(-1,H)))
    ck(gap[0]>=0)
    rows.append({'case':case,'k':k,'vertices':D,'controller_masks':masks,'H_prime_form':[[p,str(v)] for p,v in H],
        'I_data':str(sum(inf[:k])),'I_controller':str(ctrl),'I_access':str(access),'I_terminal_data':str(terminal),
        'controller_entropy_bill':[[p,str(v)] for p,v in bill],'rate8_gap_interval':list(map(str,gap))})
    (RUN/'out'/f'{MODE}_CASES.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'mode':MODE,'case':case,'checks':checks,'elapsed':time.perf_counter()-START}),flush=True)
result={'verdict':'PASS','cases':len(rows),'checks':checks,'nodes':nodes,'leaves':leaves,'runtime_seconds':time.perf_counter()-START,'kernel_checks':ns['ASSERTIONS']}
(RUN/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/f'{MODE}_LOG_RECEIPTS.json').write_text(json.dumps({'scale':ns['SCALE'],'ln_terms':50,'prime_intervals':ns['PRIME_RECEIPTS']},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
