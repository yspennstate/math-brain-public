from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
FACT=[]
for a in range(257):
    z=a; row={}; p=2
    while p*p<=z:
        while z%p==0: row[p]=row.get(p,0)+1; z//=p
        p+=1
    if z>1: row[z]=row.get(z,0)+1
    FACT.append(row)
def add(*terms):
    d={}
    for c,row in terms:
        for p,z in row.items(): d[p]=d.get(p,0)+c*z
    return {p:z for p,z in d.items() if z}
def H(masses):
    # Represents 256*entropy in exact integer coefficients of log2(prime).
    d={2:2048}
    for a in masses:
        for p,z in FACT[a].items(): d[p]=d.get(p,0)-a*z
    return {p:z for p,z in d.items() if z}
HB=[H([a,256-a]) for a in range(257)]
def fw(t):
    t=t.copy(); width=1
    while width<len(t):
        for j in range(0,len(t),2*width):
            for s in range(j,j+width): t[s],t[s+width]=t[s]+t[s+width],t[s]-t[s+width]
        width*=2
    return t
def marginal(p,n): return [sum(x for s,x in enumerate(p) if s>>i&1) for i in range(n)]
def run(limit):
    start=time.perf_counter(); checks=0; iso=0
    for bits in range(limit):
        # First truth value +1; global negation supplies all other signs.
        tab=[1]+[1 if bits>>(x-1)&1 else -1 for x in range(1,16)]
        p=[x*x for x in fw(tab)]; d=marginal(p,4); hp=H(p)
        assert sum(p)==256; checks+=1
        kp=add(*[(1,HB[x]) for x in d],(-1,hp))
        for i in range(4):
            ps=[]
            for y in [0,1]:
                child=[tab[(s&((1<<i)-1))|((s>>i)<<(i+1))|(y<<i)] for s in range(8)]
                ps.append([4*x*x for x in fw(child)])
            ds=[marginal(z,3) for z in ps]
            q=[]
            for s in range(8):
                idx=(s&((1<<i)-1))|((s>>i)<<(i+1)); q.append(p[idx]+p[idx|(1<<i)])
            assert [2*x for x in q]==[a+b for a,b in zip(*ps)]; checks+=1
            assert all(ds[0][j]+ds[1][j]==2*d[j+(j>=i)] for j in range(3)); checks+=1
            hc=[H(z) for z in ps]; hq=H(q)
            B=add((1,hp),(-1,hq)); JS2=add((2,hq),(-1,hc[0]),(-1,hc[1]))
            I=add((1,HB[d[i]]),(-1,B))
            Gamma2=add(*[(2,HB[d[j]]) for j in range(4) if j!=i],*[(-1,HB[x]) for row in ds for x in row])
            KC2=add(*[(1,HB[x]) for row in ds for x in row],(-1,hc[0]),(-1,hc[1]))
            assert add((2,kp),(-2,I),(1,JS2),(-1,Gamma2),(-1,KC2))=={}; checks+=1
            if ps[0]==ps[1]:
                assert JS2=={} and Gamma2=={}; checks+=1; iso+=1
        if bits%256==0: assert time.perf_counter()-start<(60 if limit<=256 else 1700)
    out={'status':'PASS','representatives':limit,'full_sign_functions_covered':2*limit,'coordinate_splits_checked':4*limit,'full_sign_splits_covered':8*limit,'assertions':checks,'isospectral_representative_splits':iso,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh; integer coefficients of formal logarithms of primes; no floating sign checks','global_sign_symmetry':'f and -f have identical parent and named child squared spectra'}
    name='CENSUS4_PILOT.json' if limit<=256 else 'CENSUS4.json'
    (ROOT/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__': run(int(sys.argv[1]) if len(sys.argv)>1 else 32768)
