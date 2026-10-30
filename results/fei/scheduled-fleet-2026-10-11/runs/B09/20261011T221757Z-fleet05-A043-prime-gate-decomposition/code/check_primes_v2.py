"""Exact bounded cofactor census, A043 v2. Save each completed dimension."""
import itertools,json,time,sys
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'out'
limit_n=int(sys.argv[1]); mode='pilot' if limit_n==3 else 'main'
start=time.perf_counter(); checks=0
def ck(q):
    global checks
    assert q
    checks+=1
layouts={}
for n in range(1,5):
    layouts[n]=[]
    for k in range(2,n):
        for B in itertools.combinations(range(n),k):
            D=tuple(i for i in range(n) if i not in B)
            indices=tuple(tuple(sum(((a>>i)&1)<<j for i,j in enumerate(B))|sum(((b>>i)&1)<<j for i,j in enumerate(D)) for b in range(1<<len(D))) for a in range(1<<k))
            layouts[n].append((B,D,indices))
def essential(t,n):
    return all(any(t[x]!=t[x|(1<<i)] for x in range(1<<n) if not x&(1<<i)) for i in range(n))
def factor(t,n):
    for B,D,ix in layouts[n]:
        r0=tuple(t[x] for x in ix[0]); r1=None; labels=[0]
        for row in ix[1:]:
            r=tuple(t[x] for x in row)
            if r==r0: labels.append(0)
            elif r1 is None: r1=r; labels.append(1)
            elif r==r1: labels.append(1)
            else: break
        else:
            if r1 is not None:
                g=tuple((r0 if y%2==0 else r1)[y>>1] for y in range(1<<(len(D)+1)))
                return B,D,ix,tuple(labels),g
    return None
cache={}
def certify(t,n):
    key=(n,t)
    if key in cache: return cache[key]
    ck(essential(t,n)); f=factor(t,n)
    if f is None: ans=True
    else:
        B,D,ix,h,g=f
        ck(2<=len(B)<n); ck(essential(h,len(B))); ck(essential(g,len(D)+1))
        for a,row in enumerate(ix):
            for b,x in enumerate(row): ck(t[x]==g[h[a]|(b<<1)])
        certify(h,len(B)); certify(g,len(D)+1); ans=False
    if n<=3: cache[key]=ans
    return ans
result={'helper':'A043-cofactor-v2','mode':mode,'domain_max_n':limit_n,'symmetry':'none','arithmetic':'exact integers/tuples','counts':[],'complete':False}
def save():
    result['assertions']=checks; result['runtime_seconds']=time.perf_counter()-start
    (OUT/(mode+'_census.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
try:
    for n in range(1,limit_n+1):
        ess=prime=0; total=1<<(1<<n)
        for mask in range(total):
            if mask%256==0 and time.perf_counter()-start>=50:
                result['partial']={'n':n,'tables_completed':mask,'essential':ess,'prime':prime}; raise TimeoutError('50-second computation cap')
            t=tuple((mask>>x)&1 for x in range(1<<n))
            if essential(t,n):
                ess+=1; leaf=certify(t,n); prime+=int(leaf and n>=2)
        terminal=ess if n==1 else 0
        result['counts'].append({'n':n,'truth_tables':total,'essential':ess,'prime':prime,'terminal_literals':terminal,'decomposable':ess-prime-terminal}); save()
        print(json.dumps(result['counts'][-1]),flush=True)
    # All thresholds at the tested dimensions verify the proved classification.
    for n in range(3,limit_n+1):
        for threshold in range(1,n+1):
            t=tuple(int(x.bit_count()>=threshold) for x in range(1<<n))
            ck((factor(t,n) is None)==(2<=threshold<=n-1))
    result['complete']=True
except TimeoutError as e:
    result['stopped_reason']=str(e)
save(); print(json.dumps(result,indent=2),flush=True)
