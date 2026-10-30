import json,time,hashlib,itertools,sys
from pathlib import Path
from fractions import Fraction as Q
root=Path(__file__).resolve().parents[1]
prior=root.parent/'20261026T193504Z-fleet04-A058-overlapping-compositions/code/certify.py'
helper=prior.read_text(encoding='utf-8').split('start=time.monotonic();p=')[0]
exec(compile(helper,str(prior),'exec'),globals())
# The imported prefix defines exact outward log arithmetic only, never its run.
A=Q(9,2); cache={}; assertions=0
def sigadd(a,b,q=Q(1)):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,Q(0))+q*v
    return {k:v for k,v in c.items() if v}
def sigscale(a,q):return {k:v*q for k,v in a.items() if v*q}
def factor(n):
    out={};k=2
    while k*k<=n:
        while n%k==0:out[k]=out.get(k,0)+1;n//=k
        k+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def prof(a):
    global assertions
    a=tuple(a)
    if a in cache:return cache[a]
    N=len(a);n=N.bit_length()-1;w=walsh(list(a))
    direct=[sum(v*(-1 if (x&j).bit_count()%2 else 1) for j,v in enumerate(a)) for x in range(N)]
    assert direct==w;assertions+=1
    ps=[Q(v*v,N*N) for v in w];assert sum(ps)==1;assertions+=1
    H=entropy(ps);Is=sum(p*j.bit_count() for j,p in enumerate(ps))
    Ie=sum(Q(a[x]!=a[x^(1<<i)],N) for x in range(N) for i in range(n))
    assert Is==Ie;assertions+=1
    hs={2:Q(2*n)}
    for v in w:
        if v:hs=sigadd(hs,factor(abs(v)),Q(-2*v*v,N*N))
    if not hs:H=(0,0)
    result=dict(H=H,I=Is,hs=hs);cache[a]=result;return result
def restrict(a,i,b):return [v for x,v in enumerate(a) if (x>>i)&1==b]
def interval_text(z):return [str(Q(v,S)) for v in z]
def audit(a,i,old):
    global assertions
    P=prof(a);kids=[prof(restrict(a,i,b)) for b in [0,1]]
    N=len(a);p=sum(Q(a[x]!=a[x^(1<<i)],N) for x in range(N))
    assert sum(k['I'] for k in kids)/2==P['I']-p;assertions+=1
    Davg=scale(add(kids[0]['H'],kids[1]['H']),Q(1,2));D=sub(P['H'],Davg)
    Dsig=sigadd(P['hs'],sigadd(kids[0]['hs'],kids[1]['hs']),Q(-1,2))
    if not Dsig:D=(0,0)
    R=A*P['I']-old
    if R<0 or R<Q(D[0],S):return dict(status='INADMISSIBLE_RECEIVED_CASH')
    assert R>=Q(D[1],S);assertions+=1
    masses=[A*k['I']/2 for k in kids];Msum=sum(masses)
    if not Msum:
        assert all(k['H']==(0,0) for k in kids);assertions+=1
        return dict(status='CONSTANT_CHILDREN')
    indices=[j for j in range(2) if masses[j]]
    if len(indices)==2:
        cross=sigadd(sigscale(kids[0]['hs'],kids[1]['I']),kids[1]['hs'],-kids[0]['I'])
        bound=sub(scale(kids[0]['H'],kids[1]['I']),scale(kids[1]['H'],kids[0]['I']))
        if not cross:pass
        elif bound[1]<0:pass
        else:assert bound[0]>0;indices.reverse()
        assertions+=1
    else:
        assert kids[1-indices[0]]['H']==(0,0);assertions+=1
    L=max(Q(0),Msum-R+Q(D[1],S));remaining=L;qq=[Q(1),Q(1)]
    for j in indices:
        taken=min(remaining,masses[j]);qq[j]=1-taken/masses[j];remaining-=taken
    assert remaining==0 and all(0<=q<=1 for q in qq);assertions+=1
    used=sum((1-qq[j])*masses[j] for j in range(2));assert used==L;assertions+=1
    qhat=[Q((q*256).numerator//(q*256).denominator,256) for q in qq]
    assert Q(D[1],S)+sum(qhat[j]*masses[j] for j in range(2))<=R;assertions+=1
    # Both complete entropy bills retained, using exact prime-log coefficients.
    frozen={};live={}
    for j in range(2):
        frozen=sigadd(frozen,kids[j]['hs'],(1-qhat[j])/2)
        live=sigadd(live,kids[j]['hs'],qhat[j]/2)
    assert sigadd(frozen,live)==sigscale(sigadd(kids[0]['hs'],kids[1]['hs']),Q(1,2));assertions+=1
    frozenI=(0,0);idealI=(0,0);roundI=(0,0)
    for j in range(2):
        frozenI=add(frozenI,scale(kids[j]['H'],(1-qhat[j])/2))
        idealI=add(idealI,scale(kids[j]['H'],(1-qq[j])/2))
        roundI=add(roundI,scale(kids[j]['H'],(qq[j]-qhat[j])/2))
        assert 0<=qq[j]-qhat[j]<Q(1,256);assertions+=1
    common=max(Q(0),1-L/Msum)
    uniformI=scale(Davg,1-common)
    # Exact LP dual certificate on EVERY denominator8 grid competitor.
    competitors=0
    for k0,k1 in itertools.product(range(9),repeat=2):
        xx=[(1-Q(k0,8))*masses[0],(1-Q(k1,8))*masses[1]];u=sum(xx)
        if u<L:continue
        assert u-L>=0;assertions+=1
        if len(indices)==2:
            lo,hi=indices
            assert xx[hi]-max(Q(0),L-masses[lo])>=0;assertions+=1
        competitors+=1
    return dict(status='PASS',R=str(R),p=str(p),D=interval_text(D),I=str(P['I']),masses=[str(m) for m in masses],liquidation=str(L),qhat=[str(q) for q in qhat],frozen_entropy=interval_text(frozenI),ideal_frozen_entropy=interval_text(idealI),common_ideal_frozen_entropy=interval_text(uniformI),improvement_vs_common=interval_text(sub(uniformI,idealI)),physical_improvement_vs_common_ideal=interval_text(sub(uniformI,frozenI)),competitors=competitors)
start=time.monotonic(); rows=[];types={};candidate_rows=0
mode=sys.argv[1] if len(sys.argv)>1 else 'main'
and3=[-1 if x==0 else 1 for x in range(8)];and2=[-1 if x%4==0 else 1 for x in range(8)]
fixture=and3+and2
if mode=='pilot':
    result=audit(fixture,3,Q(0));print(json.dumps(result));raise SystemExit(0)
for n in range(4):
    N=1<<n
    for bits in range(1<<N):
        a=[-1 if (bits>>x)&1 else 1 for x in range(N)]
        for i in range(n):
            candidate_rows+=1
            for old in [Q(0),Q(1,16)]:
                r=audit(a,i,old);types[r['status']]=types.get(r['status'],0)+1
cores=[[-1 if x%2==0 else 1 for x in range(8)],and2,and3,[(-1 if x.bit_count()%2 else 1) for x in range(8)]]
for a,b in itertools.product(cores,repeat=2):
    g=a+b
    for i in range(4):
        candidate_rows+=1
        for old in [Q(0),Q(1,16)]:
            r=audit(g,i,old);types[r['status']]=types.get(r['status'],0)+1
assert candidate_rows==868
fix={str(old):audit(fixture,3,old) for old in [Q(0),Q(1,16)]}
f=fix['0'];assert Q(f['improvement_vs_common'][0])>Q(1,64);assertions+=1
assert Q(f['physical_improvement_vs_common_ideal'][0])>Q(1,80);assertions+=1
assert f['qhat']==['1','235/256'];assertions+=1
assert Q(f['D'][0])>Q(9,16);assertions+=1
out=dict(status='PASS',helper_sha256=hashlib.sha256(helper.encode()).hexdigest(),nominal_coordinate_rows=candidate_rows,received_cash_modes=2,status_counts=types,unique_actual_profiles=len(cache),assertions=assertions,fixture=fix,elapsed_s=time.monotonic()-start,full_FEI='OPEN',independent_agent_review='PENDING')
(root/'out/CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixture'}))
