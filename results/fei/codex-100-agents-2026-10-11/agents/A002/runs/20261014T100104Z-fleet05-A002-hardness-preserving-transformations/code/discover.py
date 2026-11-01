import json, math, time, hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def spectrum(v):
    w=list(v);s=1
    while s<len(w):
        for k in range(0,len(w),2*s):
            for j in range(k,k+s):a,b=w[j],w[j+s];w[j],w[j+s]=a+b,a-b
        s*=2
    return w
def child(v,i,b):
    return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2))
def entropy(v):
    N=len(v)
    return sum(-((a/N)**2)*math.log2((a/N)**2) for a in spectrum(v) if a)
spec={'helper_version':'interaction-discovery-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'all labelled Boolean tables n=1..4','domain':[1,2,3,4],'case_count':65812,'symmetry':'none','arithmetic':'integer Walsh; floating entropy discovery ONLY, no proof','memory_estimate_MB':60,'max_runtime_seconds':55}
(R/'out/DISCOVERY_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n')
start=time.perf_counter();cache={};best=(0,None);pairs=0
for n in range(1,5):
    for mask in range(1<<(1<<n)):
        if time.perf_counter()-start>55:raise TimeoutError('frozen cap')
        v=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));w=spectrum(v);h=entropy(v)
        def H(u):
            if u not in cache:cache[u]=entropy(u)
            return cache[u]
        ds=[sum(a*a for s,a in enumerate(w) if s>>i&1)/(len(v)**2) for i in range(n)]
        hs=[sum(H(child(v,i,b)) for b in (0,1))/2 for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if ds[i]+ds[j]==0:continue
                hab=sum(H(child(child(v,j,b),i,a)) for a in (0,1) for b in (0,1))/4
                omega=hs[i]+hs[j]-h-hab;pairs+=1
                ratio=-omega/(ds[i]+ds[j])
                if ratio>best[0]+1e-12:best=(ratio,{'n':n,'mask':mask,'pair':[i,j],'omega':omega,'I_pair':ds[i]+ds[j]})
out={'status':'DISCOVERY_ONLY','tables':65812,'pairs':pairs,'max_negative_interaction_per_queried_influence':best,'seconds':time.perf_counter()-start}
(R/'out/DISCOVERY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
