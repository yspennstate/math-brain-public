from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import sys,json,time
RUN=Path(__file__).resolve().parents[1];MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
source=RUN.parent/'20261011T234607Z-account05-A022-one-point-surgery/code/oddface_surgery.py'
ns={'__file__':str(source),'__name__':'kernel'}
exec(source.read_text(encoding='utf-8').split('\nmaxima={};')[0],ns)
fwht,factors,canon=ns['fwht'],ns['factors'],ns['canonical']
START=time.perf_counter();LIMIT=60 if MODE=='pilot' else 1800;checks=0
def ck(ok):
    global checks
    assert ok;checks+=1
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen cap')
def add(*terms):
    e=Counter()
    for scale,expr in terms:
        for p,v in expr:e[p]+=scale*v
    return canon(e)
def number(v):return ((2,Q(v)),) if v else ()
def entropy(masses,den):
    e=Counter();total=sum(masses)
    for p,power in factors(den):e[p]+=Q(total*power,den)
    for a,r in Counter(a for a in masses if a).items():
        for p,power in factors(a):e[p]-=Q(r*a*power,den)
    return canon(e)
def bounds(e):
    lo,hi=ns['expr_interval'](e);return Q(lo,ns['SCALE']),Q(hi,ns['SCALE'])
def stats(f):
    w=fwht(f);N=len(f);n=N.bit_length()-1
    ck(sum(x*x for x in w)==N*N)
    return w,entropy([x*x for x in w],N*N),[Q(sum(x*x for S,x in enumerate(w) if S>>i&1),N*N) for i in range(n)]
def seed(k,kind):
    if kind=='bent':return tuple(1-2*(sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(k//2))%2) for x in range(1<<k))
    if kind=='tensor':return tuple(1-2*((((x&1)*((x>>1)&1))+((x>>2).bit_count()))%2) for x in range(1<<k))
    if kind=='parity':return tuple(1-2*(x.bit_count()%2) for x in range(1<<k))
    raise ValueError(kind)
fixtures=[(4,'bent',tuple(range(16)),(128,)*16),(4,'bent',tuple(range(16)),tuple(1<<(j%8) for j in range(16))),
    (4,'bent',tuple(range(16)),(0,)*8+(128,)*8),(4,'bent',(0,1),(170,204)),
    (4,'tensor',(0,1),(170,204)),(4,'parity',(0,1),(170,204))]
if MODE=='full':fixtures += [(6,'bent',tuple(range(64)),(128,)*64),(6,'bent',tuple(range(64)),tuple(1<<(j%8) for j in range(64))),
    (6,'bent',tuple(range(8)),(170,204)*4),(8,'bent',tuple(range(256)),(128,)*256),
    (8,'bent',tuple(range(256)),tuple(1<<(j%8) for j in range(256))),
    (8,'tensor',tuple(range(256)),tuple(1<<(j%8) for j in range(256))),
    (8,'parity',tuple(range(256)),tuple(1<<(j%8) for j in range(256))),
    (4,'bent',tuple(range(16)),(0,)*16)]
rows=[]
for case,(k,kind,D,masks) in enumerate(fixtures):
    ND=1<<k;delta=Q(1,ND);b=seed(k,kind);bw,bH,bI=stats(b)
    A=[tuple((mask>>z)&1 for z in range(8)) for mask in masks]
    aw=[fwht(a) for a in A]
    controls=[stats(tuple(1-2*a for a in aa)) for aa in A]
    alpha=[Q(sum(a),8) for a in A];mu=[1-2*a for a in alpha]
    p=delta*sum(alpha);V=delta*sum(1-m*m for m in mu);rho=delta*len(D)
    bill=add(*[(delta,h) for w,h,i in controls]);ck(p<=Q(1,8));ck(sum(bI)>=Q(k,2))
    lookup=dict(zip(D,masks));f=tuple(b[x]*(1-2*((lookup.get(x,0)>>z)&1)) for z in range(8) for x in range(ND))
    w,H,inf=stats(f)
    for T in range(8):
        for S in range(ND):
            pred=(8*bw[S] if T==0 else 0)-2*sum(b[v]*(-1 if (S&v).bit_count()%2 else 1)*aw[j][T] for j,v in enumerate(D))
            ck(w[S+ND*T]==pred)
    R=[sum(v*v for v in w[T*ND:(T+1)*ND]) for T in range(8)]
    den=len(f)**2;HR=entropy(R,den)
    ck(Q(R[0],den)==1-V)
    for T in range(1,8):ck(Q(R[T],den)==delta*sum(Q(cc[0][T]**2,64) for cc in controls))
    zero_bill=add(*[(delta,entropy([cc[0][0]**2],64)) for cc in controls])
    emptyphi=entropy([R[0]],den)
    upper=add((1,bill),(-1,zero_bill),(1,number(k*V)),(1,emptyphi))
    # Independently assemble exact log-sum mixing refund from each nonempty row.
    refund=()
    for T in range(1,8):
        pieces=[cc[0][T]**2*ND for cc in controls]
        ck(sum(pieces)==R[T])
        refund=add((1,refund),(1,entropy(pieces,den)),(-1,entropy([R[T]],den)))
    ck(add((1,upper),(-1,HR))==refund);ck(bounds(refund)[0]>=0)
    data_deficit=add((1,number(k)),(-1,H),(1,HR));ck(bounds(data_deficit)[0]>=0)
    totalupper=add((1,upper),(1,number(k)))
    ck(add((1,totalupper),(-1,H))==add((1,refund),(1,data_deficit)))
    ck(V<=4*p*(1-p));ck(sum(inf[:k])>=sum(bI)-2*k*p)
    for i in range(k):
        exact=bI[i]+2*delta*sum(alpha[j]*b[v]*b[v^(1<<i)] for j,v in enumerate(D))
        exact-=4*delta*sum(b[v]*b[u]*Q(sum(a*c for a,c in zip(A[j],A[l])),8) for j,v in enumerate(D) for l,u in enumerate(D) if j<l and u==v^(1<<i))
        ck(inf[i]==exact)
    ck(inf[k:]==[delta*sum(cc[2][i] for cc in controls) for i in range(3)])
    gap=bounds(add((1,number(7*sum(inf[:k]))),(1,bill),(-1,H)));ck(gap[0]>=0)
    nominal=[]
    for guard,rate in ((Q(1,8),5),(Q(1,16),3)):
        if rho<=guard:
            gg=bounds(add((1,number(rate*sum(inf[:k]))),(1,bill),(-1,H)));ck(gg[0]>=0)
            nominal.append({'rate':rate,'gap_interval':list(map(str,gg))})
    rows.append({'case':case,'k':k,'seed':kind,'vertices':D,'controller_masks':masks,'p':str(p),'V':str(V),'rho':str(rho),
        'I_seed':str(sum(bI)),'I_data':str(sum(inf[:k])),'I_controller':str(sum(inf[k:])),
        'H_prime_form':[[pp,str(c)] for pp,c in H],'controller_bill':[[pp,str(c)] for pp,c in bill],
        'mix_refund':[[pp,str(c)] for pp,c in refund],'conditional_data_capacity_gap':list(map(str,bounds(data_deficit))),
        'rate7_gap':list(map(str,gap)),'nominal_refinements':nominal})
    (RUN/'out'/f'{MODE}_CASES.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
result={'verdict':'PASS','cases':len(rows),'checks':checks,'runtime_seconds':time.perf_counter()-START}
(RUN/'out'/f'{MODE}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(RUN/'out'/f'{MODE}_LOG_RECEIPTS.json').write_text(json.dumps({'scale':ns['SCALE'],'ln_terms':50,'prime_intervals':ns['PRIME_RECEIPTS']},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
