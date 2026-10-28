import sys, json, time, importlib.util, hashlib
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parent.parent
OLD=RUN/'code/exact_helper.py'
if not OLD.exists():
    OLD=RUN.parents[1]/'runs/20261014T051435Z-account05-A028-stopping-tree-payment/code/exact.py'
spec=importlib.util.spec_from_file_location('prior_exact',OLD)
e=importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
START=time.monotonic(); COUNTS={'cases':0,'assertions':0,'data_rows':0,'control_rows':0,'histories':0}
def ck(b):
    COUNTS['assertions']+=1
    assert b,COUNTS
    assert time.monotonic()-START < (55 if MODE=='pilot' else 240), 'runtime guard'
def eq(x,y): ck(e.add(x,e.scale(y,-1))=={})
def nonneg(x): ck(e.enclosure(x)[0]>=0)
@lru_cache(None)
def restrict(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def avg(x,y): return e.scale(e.add(x,y),Q(1,2))
def sub(x,y): return e.add(x,e.scale(y,-1))
@lru_cache(None)
def state(a,g,h):
    p=Q(a.count(-1),len(a)); V=4*p*(1-p)
    gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g))
    pg,hpg,hg,ig=e.stats(g); ph,hph,hh,ih=e.stats(h)
    pa,hpa,ha,ia=e.stats(a)
    f=tuple(g[x] if z==1 else h[x] for z in a for x in range(len(g)))
    hf=e.stats(f)[2]
    q=tuple((1-p)*x+p*y for x,y in zip(pg,ph))
    gw=e.walsh(g); hw=e.walsh(h)
    wt=tuple(V*Q((x-y)**2,4*len(g)**2) for x,y in zip(gw,hw))
    B=e.add(*(e.add(e.eta(w),e.eta(qi-w),e.scale(e.eta(qi),-1)) for qi,w in zip(q,wt)))
    HA=e.entropy(tuple(x/V for x in pa[1:])) if V else {}
    L=e.add(B,e.scale(HA,V*gamma))
    T=e.add(e.scale(hg,1-p),e.scale(hh,p))
    J=sub(e.entropy(q),T)
    return {'p':p,'V':V,'gamma':gamma,'J':J,'L':L,'T':T,'HF':hf,'Q':gamma*ia,
            'q':q,'w':wt,'Hplus':hpa,'R':V*e.stats(tuple(x*y for x,y in zip(g,h)))[3]/2}
def children(a,g,h,kind,i):
    if kind=='C': return [state(restrict(a,i,b),g,h) for b in (0,1)]
    return [state(a,restrict(g,i,b),restrict(h,i,b)) for b in (0,1)]
def test(a,g,h):
    s=state(a,g,h); COUNTS['cases']+=1
    eq(s['HF'],e.add(s['T'],s['J'],s['L']))
    ck(sum(s['q'])==1); ck(sum(s['w'])==s['V']*s['gamma'])
    nonneg(s['J']); nonneg(s['L'])
    nonneg(sub(e.entropy((s['p'],1-s['p'])),s['J']))
    nonneg(sub({2:Q(26,9)*s['Q']},s['J']))
    Lbound=e.add(e.scale(s['Hplus'],s['gamma']),{2:Q(13,9)*s['gamma']*s['V']+s['R']})
    nonneg(sub(Lbound,s['L']))
    for kind,n in [('C',len(a).bit_length()-1),('D',len(g).bit_length()-1)]:
        for i in range(n):
            x,y=children(a,g,h,kind,i)
            dJ=sub(s['J'],avg(x['J'],y['J']))
            if kind=='C':
                COUNTS['control_rows']+=1
                nonneg(dJ); eq(s['T'],avg(x['T'],y['T']))
            else:
                COUNTS['data_rows']+=1
                debit=sub(sub(sub(s['HF'],avg(x['HF'],y['HF'])),sub(s['T'],avg(x['T'],y['T']))),
                          sub(s['L'],avg(x['L'],y['L'])))
                eq(debit,dJ)

def history(a,g,h,depth,policy=0):
    s=state(a,g,h)
    if depth==0 or (len(a)==len(g)==1): return {},{},s['J'],s['L'],s['T'],s['HF'],0
    # Physical adaptive policies; each branch may pick a different next block.
    C=len(a)>1; D=len(g)>1
    kind='D' if D and (not C or (depth+policy)%2==0) else 'C'
    i=(depth+policy) % ((len(g) if kind=='D' else len(a)).bit_length()-1)
    args=[(restrict(a,i,b),g,h) if kind=='C' else (a,restrict(g,i,b),restrict(h,i,b)) for b in (0,1)]
    ch=[history(*args[b],depth-1,policy+b+1) for b in (0,1)]
    ss=[state(*z) for z in args]
    local=sub(s['J'],avg(ss[0]['J'],ss[1]['J']))
    d=e.add(avg(ch[0][0],ch[1][0]),local if kind=='D' else {})
    c=e.add(avg(ch[0][1],ch[1][1]),local if kind=='C' else {})
    j=avg(ch[0][2],ch[1][2]); l=avg(ch[0][3],ch[1][3]); t=avg(ch[0][4],ch[1][4]); hf=avg(ch[0][5],ch[1][5])
    eq(e.add(d,c,j),s['J']); nonneg(c); nonneg(j); nonneg(sub(s['J'],d))
    # Complete source and structural terminals remain, rather than being dropped.
    eq(e.add(t,j,l),hf)
    return d,c,j,l,t,hf,1+ch[0][6]+ch[1][6]

mx=1 if MODE=='pilot' else 2
tabs=list(e.tables(mx))
for _,_,a in tabs:
    for n in range(mx+1):
        ts=[t for k,_,t in tabs if k==n]
        for g in ts:
            for h in ts: test(a,g,h)
fixtures=[]
if MODE=='full':
    # Fixed extra fixtures, declared before this full run in SPEC_AMENDMENT.
    baseg=tuple(-1 if x==0 else 1 for x in range(8))
    baseh=tuple(-1 if x.bit_count()<=1 else 1 for x in range(8))
    g=baseg+tuple(-z for z in baseg); h=baseh+tuple(-z for z in baseh)
    a=tuple(-1 if x in (0,1,2) else 1 for x in range(8))
    test(a,g,h)
    ck(a.count(-1)==3)
    # Query bit zero: all four original source terminals are nonconstant.
    ck(all(len(set(restrict(t,0,b)))==2 for t in (g,h) for b in (0,1)))
    ck(sum(g)!=sum(h) or e.stats(g)[0]!=e.stats(h)[0])
    for depth in (1,2,3,5,7):
        for policy in (0,1):
            z=history(a,g,h,depth,policy); COUNTS['histories']+=1
            fixtures.append({'depth':depth,'policy':policy,'nodes':z[6],
                             'signed_data_interval':list(map(str,e.enclosure(z[0]))),
                             'remaining_original_interval':list(map(str,e.enclosure(sub(state(a,g,h)['J'],z[0]))))})
out={'mode':MODE,'status':'PASS','counts':COUNTS,'seconds':time.monotonic()-START,
     'helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'fixtures':fixtures}
(RUN/'out'/f'check_{MODE}.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
