"""Independent subset-Walsh spectra and sequential actual-credit admission."""
from profile_engine import F,lp,add,mul,neg,mean,minus,pack,ev,cmp,pos,save,Q
from functools import lru_cache
from itertools import product,combinations
from pathlib import Path
import json,time,sys,ctypes
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter();PILOT='--pilot' in sys.argv;CHECKS=0;NODES=0;PEAK=0
N=tuple(['P']+['A'+str(m) for m in range(6)]+['L'+str(m) for m in range(2,7)])
def ck(x):
    global CHECKS
    assert x;CHECKS+=1
def guard():
    global PEAK
    class PMC(ctypes.Structure):
        _fields_=[('cb',ctypes.c_ulong),('faults',ctypes.c_ulong)]+[(n,ctypes.c_size_t) for n in ['peakws','ws','peakpaged','paged','peaknonpaged','nonpaged','peakpagefile','pagefile','private']]
    p=PMC();p.cb=ctypes.sizeof(p)
    getmem=ctypes.windll.psapi.GetProcessMemoryInfo
    getmem.argtypes=[ctypes.c_void_p,ctypes.c_void_p,ctypes.c_ulong]
    ck(getmem(ctypes.c_void_p(-1),ctypes.byref(p),p.cb)!=0)
    PEAK=max(PEAK,p.private);ck(p.private<280*1024**2)
    ck(time.perf_counter()-START<(55 if PILOT else 1500))
def truth(n):
    if n=='P':return (1,)
    m=int(n[1:]);return tuple(-1 if x in ({0} if n[0]=='A' else {0,1,2}) else 1 for x in range(1<<m))
def acts(n):
    if n in ['P','A0']:return ()
    m=int(n[1:])
    if n[0]=='A':return ((0,'A'+str(m-1),'P'),)
    return ((0,'A'+str(m-2),'A'+str(m-1)),)+(((2,'L'+str(m-1),'P'),) if m>=3 else ())
def size(key):return sum(len(truth(n)) for n in key)
def entropy(masses):
    out={}
    for p in masses:
        if p:out=add(out,mul(lp(p),-p))
    return out
def prod(xs):
    r=F(1)
    for x in xs:r*=x
    return r
@lru_cache(None)
def core(n):
    t=truth(n);M=len(t);dim=(M-1).bit_length()
    w=[F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)),M) for s in range(M)]
    ck(sum(z*z for z in w)==1)
    ds=[F(sum(t[x]!=t[x^(1<<i)] for x in range(M)),M) for i in range(dim)]
    I=sum(ds,F(0));ck(I==sum(s.bit_count()*z*z for s,z in enumerate(w)))
    return w[0],entropy(z*z for z in w),I,ds
K=tuple(1 if z in {0,1,2,4,8,10} else -1 for z in range(16))
W=tuple(F(sum(y*(-1 if (z&s).bit_count()%2 else 1) for z,y in enumerate(K)),16) for s in range(16))
PERMS=[tuple((j^2) if ((j%2==0 and a) or (j%2==1 and b)) else j for j in range(4)) for a,b in product([0,1],repeat=2)]
def permkey(key,p):return tuple(key[p[j]] for j in range(4))
def canonical(mask,key):
    return min((sum(((mask>>p[j])&1)<<j for j in range(4)),permkey(key,p)) for p in PERMS)
def full(key):return spectrum(min(permkey(key,p) for p in PERMS))
@lru_cache(None)
def spectrum(key):
    global NODES
    cs=[core(n) for n in key];mus=[c[0] for c in cs];vs=[1-m*m for m in mus]
    coefficients=[sum((W[M]*prod(mus[j] for j in range(4) if (M^U)>>j&1) for M in range(16) if M&U==U),F(0)) for U in range(16)]
    mass=[c*c*prod(vs[j] for j in range(4) if U>>j&1) for U,c in enumerate(coefficients)]
    ck(sum(mass,F(0))==1)
    qs=[]
    for j in range(4):
        q=sum((prod((1-mus[k])/2 if z>>k&1 else (1+mus[k])/2 for k in range(4) if k!=j) for z in range(16) if not(z>>j&1) and K[z]!=K[z|1<<j]),F(0))
        ck(sum(p for U,p in enumerate(mass) if U>>j&1)==q*vs[j]);qs.append(q)
    H=add(entropy(mass),*[mul(minus(c[1],entropy([v,1-v])),q) for c,v,q in zip(cs,vs,qs)])
    I=sum((c[2]*q for c,q in zip(cs,qs)),F(0));S=add({2:4*I},neg(H))
    NODES+=1
    if NODES%128==0:guard();save('CHECKPOINT.json',{'spectra':NODES,'checks':CHECKS,'seconds':time.perf_counter()-START,'private_peak_bytes':PEAK})
    return S,I
def children(key,j,a,b):
    out=[]
    for n in [a,b]:
        z=list(key);z[j]=n;out.append(tuple(z))
    return out
def hull(mask,key):return solve(*canonical(mask,key))
@lru_cache(None)
def solve(mask,key):
    S,I=full(key);r=pos(neg(S))
    for j,n in enumerate(key):
        if mask>>j&1:
            for _,a,b in acts(n):
                kids=children(key,j,a,b);v=mean([hull(mask,k) for k in kids])
                if cmp(v,r)>0:r=v
    return r
def validate_domain():
    # Literal physical restriction census independently derives the profile transitions.
    G=truth('L6')
    def strip(t):
        while len(t)>1:
            dim=(len(t)-1).bit_length();i=next((i for i in range(dim) if all(t[x]==t[x^(1<<i)] for x in range(len(t)))),None)
            if i is None:break
            t=tuple(y for x,y in enumerate(t) if not(x>>i&1))
        return t
    lookup={truth(n):n for n in N};rows=0
    for pat in product([-1,0,1],repeat=6):
        free=[i for i,b in enumerate(pat) if b==-1];fixed=sum((b==1)<<i for i,b in enumerate(pat))
        raw=tuple(G[fixed|sum(((x>>k)&1)<<i for k,i in enumerate(free))] for x in range(1<<len(free)));n=lookup[strip(raw)]
        for i in range(len(free)):
            kids=tuple(lookup[strip(tuple(y for x,y in enumerate(raw) if x>>i&1==b))] for b in [0,1]);rows+=1
            ck(kids==(n,n) or kids in [(a,b) for _,a,b in acts(n)])
    ck(rows==1458)
    for p in PERMS:
        for z in range(16):ck(K[z]==K[sum(((z>>p[j])&1)<<j for j in range(4))])
    return rows
def key_for(mask,ns):
    z=['L6']*4
    for j,n in zip([j for j in range(4) if mask>>j&1],ns):z[j]=n
    return tuple(z)
def allkeys(mask):return [key_for(mask,ns) for ns in product(N,repeat=mask.bit_count())]
def source_review():
    source=ROOT.parents[2]/'A075'/'runs'/'20261023T043917Z-fleet03-A075-search-to-theorem-bridge'
    count=0;cuts=0
    for triple in [(2,3,4),(2,3,5)]:
        mask=sum(1<<(j-2) for j in triple);tag=''.join(map(str,triple))
        ck(hull(mask,('L6',)*4)==neg(full(('L6',)*4)[0]));seen=set()
        for f in sorted((source/'out').glob('CERT_'+tag+'_*.json')):
            for row in json.loads(f.read_text(encoding='utf-8')):
                key=key_for(mask,row['types']);S,_=full(key)
                ck(key not in seen);seen.add(key)
                ck(S=={int(p):F(v) for p,v in row['S'].items() if F(v)})
                ck(hull(mask,key)=={int(p):F(v) for p,v in row['R'].items() if F(v)});count+=1
        ck(len(seen)==1728)
        # Saved stronger phase cuts are reproduced physically by exact allocations in audit.py.
        for f in sorted((source/'out').glob('PHASE_CUTS_'+tag+'_*.json')):
            rows=json.loads(f.read_text(encoding='utf-8'));ck(len(rows)==144 and len({tuple(row['types']) for row in rows})==144)
            for row in rows:
                incoming={int(p):F(v) for p,v in row['actual_credit'].items() if F(v)}
                path=row['original_physical_path'];pair=tuple(int(j)-2 for j in f.stem.split('_')[-1]);actual=replay_physical(path,pair)
                ck(actual[0]==incoming);ck(actual[1]==tuple(row['types']))
                state=key_for(sum(1<<j for j in pair),row['types']);need=hull(mask,state)
                ck(need=={int(p):F(v) for p,v in row['new_requirement'].items() if F(v)})
                ck(cmp(incoming,need)>=0);ck(row['true_reach']==str(F(1,1<<len(path))));cuts+=1
    ck(count==3456 and cuts==864)
    result={'states_reconstructed':count,'actual_one_then_two_phase_paths':cuts,'verdict':'UNCHANGED_SOURCE_SCOPE_ACCEPTED','method':'new direct Walsh subset spectra, own named-profile Bellman, physical path replay','full_fei':'OPEN'}
    save('SOURCE_REVIEW.json',result)
    return result
def replay_physical(path,pair):
    key=['L6']*4;axes=[list(range(6)) for _ in range(4)];credit=neg(full(tuple(key))[0]);lookup={truth(n):n for n in N}
    for jj,physical_i,b,phase in path:
        j=jj-2;i=axes[j].index(physical_i);t=truth(key[j]);kids=[];maps=[]
        for bit in [0,1]:
            c=tuple(y for x,y in enumerate(t) if x>>i&1==bit);aa=[x for k,x in enumerate(axes[j]) if k!=i]
            while len(c)>1:
                dim=(len(c)-1).bit_length();d=next((k for k in range(dim) if all(c[x]==c[x^(1<<k)] for x in range(len(c)))),None)
                if d is None:break
                c=tuple(y for x,y in enumerate(c) if not(x>>d&1));aa.pop(d)
            kids.append(lookup[c]);maps.append(aa)
        mask=1<<j if phase=='single' else sum(1<<z for z in pair)
        args=children(tuple(key),j,*kids);rs=[hull(mask,x) for x in args];reserve=minus(credit,mean(rs));ck(cmp(reserve,{})>=0)
        credit=add(rs[b],reserve);key=list(args[b]);axes[j]=maps[b]
    return credit,tuple(key[j] for j in pair)
def phase_search():
    root=('L6',)*4;A=neg(full(root)[0]);ck(cmp(A,{})>0);ck(hull(15,root)==A)
    arrivals={1<<j:{root:A} for j in range(4)};paths={1<<j:{root:[]} for j in range(4)};cuts=[];worst={};witness=None
    for k in [1,2,3]:
        for tup in combinations(range(4),k):
            mask=sum(1<<j for j in tup);incoming=arrivals[mask];pp=paths[mask];keys=sorted(allkeys(mask),key=size,reverse=True)
            for key in keys:
                ck(key in incoming);a=incoming[key];ck(cmp(a,hull(mask,key))>=0)
                for j in range(4):
                    if mask>>j&1:continue
                    target=mask|1<<j;need=hull(target,key);gap=minus(need,a)
                    row={'mask':mask,'key':key,'new_core':j+2,'credit':pack(a),'requirement':pack(need),'gap':pack(gap),'path':pp[key],'reach':str(F(1,1<<len(pp[key])))}
                    cuts.append(row)
                    if cmp(gap,worst)>0:worst=gap;witness=row
                    if k<3 and cmp(gap,{})<=0:
                        arrivals.setdefault(target,{});paths.setdefault(target,{})
                        if key not in arrivals[target] or cmp(a,arrivals[target][key])<0:arrivals[target][key]=a;paths[target][key]=pp[key]
                for j,n in enumerate(key):
                    if not(mask>>j&1):continue
                    for i,c,d in acts(n):
                        kids=children(key,j,c,d);rv=[hull(mask,x) for x in kids];reserve=minus(a,mean(rv));ck(cmp(reserve,{})>=0)
                        for b,arg in enumerate(kids):
                            credit=add(rv[b],reserve)
                            if arg not in incoming or cmp(credit,incoming[arg])<0:
                                incoming[arg]=credit;pp[arg]=pp[key]+[[mask,j+2,i,b]]
                if len(cuts)%128==0:guard()
            save('CUTS_MASK_'+str(mask)+'.json',[r for r in cuts if r['mask']==mask])
            save('PHASE_CHECKPOINT.json',{'mask':mask,'cuts_done':len(cuts),'worst_gap':pack(worst),'witness':witness,'seconds':time.perf_counter()-START})
    ck(len(cuts)==8784)
    save('ADMISSION_RESULT.json',{'cuts':len(cuts),'fourth_core_cuts':6912,'threshold':pack(worst),'witness':witness,'all_same_credit':not worst,'root_credit':pack(A),'root_hull':pack(hull(15,root))})
    return worst
def main():
    validate_domain()
    if '--review' in sys.argv:
        result=source_review();guard();result.update({'checks':CHECKS,'seconds':time.perf_counter()-START,'private_peak_bytes':PEAK});save('SOURCE_REVIEW.json',result);print(json.dumps(result));return
    if PILOT:
        import profile_engine as old
        mask=3;keys=allkeys(mask)
        for key in keys:
            s,i=full(key);o=old.full(tuple(truth(n) for n in key));ck(s==o['S'] and i==o['I'])
        ck(hull(mask,('L6',)*4)==neg(full(('L6',)*4)[0]));guard()
        save('PILOT.json',{'states':len(keys),'seconds':time.perf_counter()-START,'checks':CHECKS,'private_peak_bytes':PEAK,'pass':True});print('PILOT PASS',len(keys),time.perf_counter()-START)
        return
    gap=phase_search()
    # Review performed separately after bounded source physical replay is completed.
    guard()
    chunks=[];chunk_id=0
    for key in product(N,repeat=4):
        if key!=min(permkey(key,p) for p in PERMS):continue
        S,I=full(key);chunks.append({'key':key,'S':pack(S),'I':str(I),'R':pack(hull(15,key))})
        if len(chunks)==128:save('FULL_'+str(chunk_id).zfill(3)+'.json',chunks);chunks=[];chunk_id+=1
    if chunks:save('FULL_LAST.json',chunks)
    save('VALIDATION.json',{'checks':CHECKS,'spectra':NODES,'spectrum_orbits_expected':6084,'hull_orbits':solve.cache_info().currsize,'private_peak_bytes':PEAK,'seconds':time.perf_counter()-START,'admission_threshold':pack(gap),'full_fei':'OPEN','independent_review':'PENDING'})
    print(json.dumps({'checks':CHECKS,'spectra':NODES,'seconds':time.perf_counter()-START,'threshold':pack(gap)}))
if __name__=='__main__':
    try:main()
    except Exception as e:
        save('FIRST_FAILURE.json',{'error':type(e).__name__+': '+str(e),'checks':CHECKS,'spectra':NODES,'seconds':time.perf_counter()-START});raise
