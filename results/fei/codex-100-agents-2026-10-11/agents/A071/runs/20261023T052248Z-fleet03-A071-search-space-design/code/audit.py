"""Reverse-predecessor audit, saved spectra only; physical-coordinate transitions."""
from profile_engine import F,add,mul,neg,mean,minus,pack,cmp,pos,save
from pathlib import Path
from itertools import product,combinations
from functools import lru_cache
import json,time
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
def ck(x):
    global CHECKS
    assert x;CHECKS+=1
def guard():
    import ctypes
    class PMC(ctypes.Structure):
        _fields_=[('cb',ctypes.c_ulong),('faults',ctypes.c_ulong)]+[(n,ctypes.c_size_t) for n in ['peakws','ws','peakpaged','paged','peaknonpaged','nonpaged','pagefile','peakpagefile','private']]
    p=PMC();p.cb=ctypes.sizeof(p);g=ctypes.windll.psapi.GetProcessMemoryInfo;g.argtypes=[ctypes.c_void_p,ctypes.c_void_p,ctypes.c_ulong]
    ck(g(ctypes.c_void_p(-1),ctypes.byref(p),p.cb)!=0);ck(p.private<280*1024**2);ck(time.perf_counter()-START<1200)
def un(d):return {int(p):F(v) for p,v in d.items() if F(v)}
N=tuple(['P']+['A'+str(m) for m in range(6)]+['L'+str(m) for m in range(2,7)])
def truth(n):
    if n=='P':return (1,)
    return tuple(-1 if x in ({0} if n[0]=='A' else {0,1,2}) else 1 for x in range(1<<int(n[1:])))
LOOKUP={truth(n):n for n in N}
def strip(t):
    while len(t)>1:
        d=next((i for i in range((len(t)-1).bit_length()) if all(t[x]==t[x^(1<<i)] for x in range(len(t)))),None)
        if d is None:break
        t=tuple(v for x,v in enumerate(t) if not(x>>d&1))
    return t
@lru_cache(None)
def actions(n):
    t=truth(n);out=[]
    for i in range((len(t)-1).bit_length()):
        out.append((i,tuple(LOOKUP[strip(tuple(v for x,v in enumerate(t) if x>>i&1==b))] for b in [0,1])))
    return out
def rank(k):return sum(len(truth(n)) for n in k)
def rep(mask,key):
    # Independently sort each exchangeable physical pair with active flags.
    z=list(key);flags=[mask>>j&1 for j in range(4)]
    for pair in [(0,2),(1,3)]:
        vals=sorted((flags[j],key[j]) for j in pair)
        for j,(b,n) in zip(pair,vals):flags[j]=b;z[j]=n
    return sum(b<<j for j,b in enumerate(flags)),tuple(z)
def setcore(key,j,n):
    z=list(key);z[j]=n;return tuple(z)
SS={};II={};GIVEN={}
for f in sorted((ROOT/'out').glob('FULL_*.json')):
    for row in json.loads(f.read_text(encoding='utf-8')):
        key=rep(15,tuple(row['key']))[1];ck(key not in SS)
        SS[key]=un(row['S']);II[key]=F(row['I']);GIVEN[key]=un(row['R'])
ck(len(SS)==6084)
def S(k):return SS[rep(15,k)[1]]
R={};QUERY_ROWS=0
def getR(mask,key):return R[rep(mask,key)]
def keys(mask):
    axes=[j for j in range(4) if mask>>j&1];out=[]
    for ns in product(N,repeat=len(axes)):
        z=['L6']*4
        for j,n in zip(axes,ns):z[j]=n
        out.append(tuple(z))
    return out
for k in [1,2,3,4]:
    for axes in combinations(range(4),k):
        mask=sum(1<<j for j in axes)
        for key in sorted(keys(mask),key=rank):
            token=rep(mask,key)
            if token in R:continue
            r=pos(neg(S(key)))
            for j in axes:
                for i,kids in actions(key[j]):
                    args=[setcore(key,j,n) for n in kids];v=mean([getR(mask,arg) for arg in args]);QUERY_ROWS+=1
                    if cmp(v,r)>0:r=v
            R[token]=r
            if k==4:ck(r==GIVEN[rep(15,key)[1]])
            if len(R)%128==0:guard()
    guard();save('AUDIT_HULL_PROGRESS.json',{'admitted_size':k,'hulls':len(R),'seconds':time.perf_counter()-START})
root=('L6',)*4;A=neg(S(root));ck(getR(15,root)==A)
# Reverse predecessor lists from actual physical truth-table queries.
PRE={n:[] for n in N}
for parent in N:
    for i,kids in actions(parent):
        for b,n in enumerate(kids):PRE[n].append((parent,i,b,kids))
ARR={};CUT_COUNT=0;PATH_STEPS=0;FINANCIAL_ROWS=0;largest={}
def minimum(xs):
    r=xs[0]
    for a in xs[1:]:
        if cmp(a,r)<0:r=a
    return r
@lru_cache(None)
def walk(path):
    global PATH_STEPS,FINANCIAL_ROWS
    if not path:return root,A,0
    key,a,mask=walk(path[:-1]);newmask,jj,i,b=path[-1]
    j=jj-2;ck(mask&newmask==mask and newmask>>j&1)
    for added in range(4):
        if newmask>>added&1 and not(mask>>added&1):ck(key[added]=='L6')
    mask=newmask;ck(cmp(a,getR(mask,key))>=0)
    kids=next(z for q,z in actions(key[j]) if q==i);args=[setcore(key,j,n) for n in kids]
    rs=[getR(mask,arg) for arg in args];reserve=minus(a,mean(rs));aa=[add(v,reserve) for v in rs]
    ck(mean(aa)==a)
    ds=[add(S(arg),c) for arg,c in zip(args,aa)]
    for c in aa+ds:ck(cmp(c,{})>=0)
    e=minus(mean([S(arg) for arg in args]),S(key))
    ck(mean(ds)==add(S(key),a,e));FINANCIAL_ROWS+=1;PATH_STEPS+=1
    return args[b],aa[b],mask
def replay(path,expect_key,expect_credit):
    key,a,mask=walk(tuple(tuple(x) for x in path))
    ck(key==expect_key and a==expect_credit)
for k in [1,2,3]:
    for axes in combinations(range(4),k):
        mask=sum(1<<j for j in axes);arr={};ARR[mask]=arr
        for key in sorted(keys(mask),key=rank,reverse=True):
            candidates=[]
            if k==1 and key==root:candidates.append(A)
            if k>1:
                for removed in axes:
                    if key[removed]=='L6':candidates.append(ARR[mask^(1<<removed)][key])
            for j in axes:
                for parent,i,b,kids in PRE[key[j]]:
                    parentkey=setcore(key,j,parent)
                    aa=[setcore(parentkey,j,n) for n in kids]
                    candidates.append(add(arr[parentkey],getR(mask,key),neg(mean([getR(mask,arg) for arg in aa]))))
            ck(bool(candidates));arr[key]=minimum(candidates)
            if len(arr)%128==0:guard()
        rows=json.loads((ROOT/'out'/('CUTS_MASK_'+str(mask)+'.json')).read_text(encoding='utf-8'))
        for row in rows:
            key=tuple(row['key']);credit=un(row['credit']);j=row['new_core']-2
            ck(credit==arr[key]);ck(un(row['requirement'])==getR(mask|1<<j,key))
            gap=minus(getR(mask|1<<j,key),credit);ck(gap==un(row['gap']));ck(cmp(gap,{})<=0)
            replay(row['path'],key,credit);ck(row['reach']==str(F(1,1<<len(row['path']))));CUT_COUNT+=1
            if CUT_COUNT%128==0:guard()
        save('AUDIT_PROGRESS.json',{'mask':mask,'cuts_checked':CUT_COUNT,'unique_path_steps':PATH_STEPS,'checks':CHECKS,'seconds':time.perf_counter()-START})
        guard()
ck(CUT_COUNT==8784)
# Positive controls: these alterations cannot be accepted by the exact comparisons.
ck(add(getR(15,root),{2:F(1)})!=GIVEN[rep(15,root)[1]])
ck(add(credit,{2:F(1)})!=arr[key])
result={'all_full_orbits':len(SS),'all_labelled_full_profiles':12**4,'hull_orbits':len(R),'physical_query_rows':QUERY_ROWS,'actual_admission_cuts':CUT_COUNT,'path_steps':PATH_STEPS,'financial_rows':FINANCIAL_ROWS,'checks':CHECKS,'seconds':time.perf_counter()-START,'positive_controls':['altered live root rejected','altered carried credit rejected'],'threshold_exact':'0','scope':'author second implementation; independent external review pending','full_fei':'OPEN'}
save('AUDIT.json',result);print(json.dumps(result))
