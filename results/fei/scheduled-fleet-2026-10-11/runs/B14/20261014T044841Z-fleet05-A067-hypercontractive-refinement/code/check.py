import argparse,hashlib,itertools,json,time
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
PRIOR=ROOT.parent/'20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check.py'
ns={'__file__':str(Path(__file__).resolve())};exec(PRIOR.read_text().split('def masks(')[0],ns)
START=time.perf_counter();ASSERTIONS=0;LIMIT=600
def ck(b):
    global ASSERTIONS
    ASSERTIONS+=1
    assert b
    assert time.perf_counter()-START<LIMIT
ns['check']=ck
fwht=ns['fwht'];physical=ns['physical'];combine=ns['combine'];interval=ns['interval']
@lru_cache(None)
def H(weights,den):return ns['entropy'](weights,den)
def entropy(a):return H(tuple(sorted(c*c for c in a)),len(a)**2)
@lru_cache(None)
def flag_cert(a,d,j):
    # Exact integer-power certificate h2(a/d)<=2j/d. 0^0=1.
    return d**d <= (a**a if a else 1)*((d-a)**(d-a) if a<d else 1)*(1<<(2*j))
def geometries():
    return [(r,u,v,d) for r in range(6) for u in range(6-r) for v in range(6-r-u) if 2<=r+u and 2<=r+v and 1<=r+u+v<=5 for d in range(r+1)]
@lru_cache(None)
def structural(t):
    r,u,v,d=t;n=r+u+v;R=(1<<r)-1;U=((1<<u)-1)<<r;V=((1<<v)-1)<<(r+u);D=(1<<d)-1
    cells={}
    for s in range(1,1<<n):
        flags=(bool(s&U),bool(s&V));key=flags+(((s&D).bit_count()%2,) if d and not any(flags) else ())
        cells.setdefault(key,[]).append(s)
    for cell in cells.values():ck(len(cell)**len(cell)<=1<<(2*sum(s.bit_count() for s in cell)))
    ck(len(cells)<=(5 if d else 4))
    states=[int(z&(R|U)==0)+2*int(z&(R|V)==D) for z in range(1<<n)]
    return list(cells.values()),states
def branches(m,hs,t):
    cells,states=structural(t);r=sum(t[:3]);width=1<<m
    v=[1 if hs[state]>>x&1 else -1 for state in states for x in range(width)]
    a=fwht(v);den=len(v)**2;iy=physical(v,range(m));iz=physical(v,range(m,m+r))
    j=sum(s.bit_count()*c*c for s,c in enumerate(a));ck(Q(j,den)==iy+iz)
    tail=sum(a[x+(s<<m)]**2 for s in range(1,1<<r) for x in range(width))
    ck(flag_cert(tail,den,j));ck(Q(tail,den)<=iz)
    for x in range(width):
        for cell in cells:ck(len({a[x+(s<<m)]**2 for s in cell})==1)
    leaves=[entropy(fwht(v[z*width:(z+1)*width])) for z in range(1<<r)]
    coreavg=combine(*((h,Q(1,1<<r)) for h in leaves))
    access=combine((entropy(a),Q(1)),(coreavg,Q(-1)))
    bound=(Q(9) if not t[3] else Q(19,2))*iz+2*iy
    ck(interval(access)[1]<=bound or (not access and bound==0))
    # All m<=2 actual cores are independently H<=4I certified.
    ck(interval(entropy(a))[1]<=(Q(9) if not t[3] else Q(19,2))*(iy+iz) or not entropy(a))
    return {'I_X':str(iy),'I_Z':str(iz),'alpha':str(Q(tail,den)),'access_upper':str(interval(access)[1])}
def universal_flags(n):
    cases=0
    for truth in range(1<<(1<<n)):
        v=[1 if truth>>x&1 else -1 for x in range(1<<n)];a=fwht(v);den=len(v)**2
        weights=[c*c for c in a];j=sum(s.bit_count()*w for s,w in enumerate(weights));mass=weights[:]
        for i in range(n):
            for s in range(1<<n):
                if s>>i&1:mass[s]+=mass[s^(1<<i)]
        for Z in range(1<<n):
            tail=den-mass[((1<<n)-1)^Z];ck(flag_cert(tail,den,j));cases+=1
    return cases
def main():
    global LIMIT
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['pilot','full'],required=True);mode=p.parse_args().mode;LIMIT=60 if mode=='pilot' else 600
    flagcases=universal_flags(3 if mode=='pilot' else 4);tested=0;fixtures=[]
    geoms=[(1,1,1,0),(1,1,1,1)] if mode=='pilot' else geometries()
    for t in geoms:
        for hs in itertools.product(range(4),repeat=4):
            row=branches(1,hs,t);tested+=1
            if len(fixtures)<4:fixtures.append({'geometry':t,'branches':hs,**row})
    if mode=='full':
        for t in [(1,1,1,0),(1,1,1,1)]:
            for hs in itertools.product(range(16),repeat=4):branches(2,hs,t);tested+=1
    beta=Q(16384,16785409);ck(1024*beta<1);ck(4095**2+128**2==4097**2)
    result={'mode':mode,'branch_cases':tested,'universal_flag_cases':flagcases,'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'geometry_count':len(geoms),'entropy_cache':H.cache_info()._asdict(),'flag_cache':flag_cert.cache_info()._asdict(),'normalized_real_beta':str(beta),'fixtures':fixtures,'prior_helper_sha256':hashlib.sha256(PRIOR.read_bytes()).hexdigest()}
    (ROOT/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))
if __name__=='__main__':main()
