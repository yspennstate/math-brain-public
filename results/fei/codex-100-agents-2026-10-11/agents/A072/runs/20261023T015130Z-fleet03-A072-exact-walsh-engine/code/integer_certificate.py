"""Integer full-Walsh certificate by occupied sectors; flat actual 12-bit boundary."""
from component_audit import add,times,minus,entp,evalp
from continue_spent import *
from functools import reduce
from math import gcd

checks=0
def test(x):
    global checks
    assert x
    checks+=1
def transform(a):
    a=list(a);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return a

@lru_cache(None)
def inner(t):
    N=len(t);w=transform(t);direct=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(N)]
    test(w==direct);test(sum(z*z for z in w)==N*N);test(transform(w)==[N*y for y in t])
    edges=[]
    for i in range((N-1).bit_length()):
        e=sum(t[x]!=t[x|1<<i] for x in range(N) if not x>>i&1);edges.append(e)
        test(F(2*e,N)==sum(F(z*z,N*N) for s,z in enumerate(w) if s>>i&1))
    return dict(N=N,w=w,gcd=reduce(gcd,w[1:],0),edges=edges,H=entp([F(z*z,N*N) for z in w]))

def main():
    start=time.perf_counter();saved=json.loads((ROOT/'out/HULL_CASES.json').read_text(encoding='utf-8'))
    spec=dict(version='A072-integer-sector-v1',family='24 existing other-core profiles; no new dimension or family',cases=24,flat_boundary='actual paired core fixed-1; remaining ignored core removed pointwise; 12 physical relevant bits',arithmetic='integer FWHT/inverse/Parseval/edges, Fraction centered sector coefficients,192-bit log enclosure',memory_estimate_mb=120,max_runtime_seconds=55)
    (ROOT/'INTEGER_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
    outertruth=tuple(-H[x<<2] for x in range(16));ow=transform(outertruth)
    records=[]
    for orbit in saved['orbits']:
        j=orbit['core_orbit']
        for state in orbit['states']:
            ts=[G,G,G,G];ts[j-2]=tuple(state['truth']);cs=[inner(t) for t in ts]
            N=1
            for c in cs:N*=c['N']
            mus=[F(sum(t),len(t)) for t in ts];vs=[1-m*m for m in mus]
            raw=[];masses=[];sectorbases=[]
            for T in range(16):
                a=F(0)
                for U in range(16):
                    if U&T!=T:continue
                    z=F(ow[U],16)
                    for k in range(4):
                        if (U^T)>>k&1:z*=mus[k]
                    a+=z
                raw.append(a);v=F(1);base=N*a;possible=True
                for k,c in enumerate(cs):
                    if T>>k&1:
                        v*=vs[k]
                        if not c['gcd']:possible=False
                        base*=F(c['gcd'],c['N'])
                masses.append(v*a*a)
                if possible:test(base.denominator==1)
                else:test(v==0)
                sectorbases.append(str(base) if possible else 'zero sector')
            test(sum(masses)==1);test(N*N*sum(masses)==N*N)
            for x,y in enumerate(outertruth):
                value=F(0)
                for T,a in enumerate(raw):
                    z=a
                    for k in range(4):
                        if T>>k&1:z*=1-2*(x>>k&1)-mus[k]
                    value+=z
                test(value==y)
            hf=entp(masses);inf=F(0);physical_edges=[]
            for k,c in enumerate(cs):
                q=F(0)
                for x in range(16):
                    if x>>k&1 or outertruth[x]==outertruth[x|1<<k]:continue
                    prob=F(1)
                    for l,m in enumerate(mus):
                        if l!=k:prob*=(1-m)/2 if x>>l&1 else (1+m)/2
                    q+=prob
                test(sum(masses[T] for T in range(16) if T>>k&1)==q*vs[k])
                hf=add(hf,times(minus(c['H'],entp([vs[k],1-vs[k]])),q))
                es=[]
                for e in c['edges']:
                    di=q*F(2*e,c['N']);full_edges=F(N,2)*di
                    test(full_edges.denominator==1);es.append(str(full_edges));inf+=di
                physical_edges.append(es)
            test(inf==F(state['I']));iv=evalp(hf);test(iv[0]<=state['H'][1] and state['H'][0]<=iv[1])
            records.append(dict(core=j,truth=state['truth'],physical_dimension=N.bit_length()-1,Walsh_scale=N,
                outer_centered_coefficients=list(map(str,raw)),inner_Walsh=[c['w'] for c in cs],sector_integer_gcd_bases=sectorbases,
                exact_mask_masses=list(map(str,masses)),physical_edge_counts=physical_edges,I=str(inf),H=iv))
    test(len(records)==24)
    # Literal boundary: core3=-1 leaves only cores2 and4 relevant.
    for a,b,c in __import__('itertools').product([0,1],repeat=3):
        test(-H[(a<<2)|(1<<3)|(b<<4)|(c<<5)]==-H[(a<<2)|(1<<3)|(b<<4)])
    truth=[]
    for x in range(1<<12):
        mask=((G[x&63]==-1)<<2)|(1<<3)|((G[x>>6]==-1)<<4)
        truth.append(-H[mask])
    N=len(truth);w=transform(truth);test(sum(z*z for z in w)==N*N);test(transform(w)==[N*y for y in truth])
    edge=[]
    for i in range(12):
        e=sum(truth[x]!=truth[x|1<<i] for x in range(N) if not x>>i&1);edge.append(e)
        test(F(2*e,N)==sum(F(z*z,N*N) for s,z in enumerate(w) if s>>i&1))
    inf=F(2*sum(edge),N);hf=evalp(entp([F(z*z,N*N) for z in w]))
    boundary=next(r for r in records if r['core']==3 and r['truth']==[-1]);test(inf==F(boundary['I']))
    test(hf[0]<=boundary['H'][1] and boundary['H'][0]<=hf[1])
    (ROOT/'out/FLAT12_WALSH.json').write_text(json.dumps(dict(n=12,truth=truth,integer_Walsh=w,edge_counts=edge,I=str(inf),H=hf),indent=2)+'\n',encoding='utf-8')
    (ROOT/'out/INTEGER_SECTORS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    result=dict(version=spec['version'],compressed_full_profiles=len(records),flat_boundary_dimension=12,flat_truth_entries=N,integer_checks=checks,runtime_seconds=time.perf_counter()-start,arithmetic='integer/Fraction; entropy comparisons after inverse/Parseval/edge checks')
    test(result['runtime_seconds']<55)
    (ROOT/'out/INTEGER_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
