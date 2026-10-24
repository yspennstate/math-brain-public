import json, math, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def walsh(v):
    v=v[:]; h=1
    while h<len(v):
        for k in range(0,len(v),2*h):
            for j in range(k,k+h):
                a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def run(n):
    N=1<<n; best=(-1,None); counts=0
    # Gray traversal toggles one of the nonzero vertices each time.
    signs=[[1 if (s&x).bit_count()%2==0 else -1 for s in range(N)] for x in range(N)]
    a=[N]+[0]*(N-1);old=0
    for k in range(1<<(N-1)):
        g=k^(k>>1)
        if k:
            x=(g^old).bit_length();delta=-2 if g&(1<<(x-1)) else 2
            a=[u+delta*v for u,v in zip(a,signs[x])]
        old=g; sq=[u*u for u in a];rat=[]
        for i in range(n):
            bit=1<<i;D=sum(sq[s] for s in range(N) if s&bit)
            if D==0:continue
            B=0.0
            for s in range(N):
                if s&bit:continue
                u,v=sq[s],sq[s|bit];w=u+v
                if u and v:B+=w*math.log2(w)-u*math.log2(u)-v*math.log2(v)
            rat.append(B/D)
        if rat and min(rat)>best[0]:best=(min(rat),g)
        counts+=1
    return {'n':n,'cases':counts,'max_min_ratio_float':best[0],'truth_mask_nonzero_vertices':best[1]}
if __name__=='__main__':
    import sys
    t=time.perf_counter();data=[run(n) for n in ([1,2,3] if '--pilot' in sys.argv else [4])]
    out={'discovery_only':True,'results':data,'elapsed_seconds':time.perf_counter()-t}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/('pilot.json' if '--pilot' in sys.argv else 'discovery.json')).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
