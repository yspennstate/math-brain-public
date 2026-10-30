import argparse, hashlib, itertools, json, time
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parent.parent
# Source-bound reuse of our prior exact log interval implementation; execute
# only definitions, never its domain/main. No imported-module bytecode is written.
prior=ROOT.parent/'20261013T222025Z-fleet05-A067-hypercontractive-refinement/code/check.py'
prefix=prior.read_text().split('def masks(')[0]
ns={'__file__':str(Path(__file__).resolve())}
exec(prefix,ns)
fwht=ns['fwht']; physical=ns['physical']; info=ns['info']; interval=ns['interval']; combine=ns['combine']; log=ns['log']
START=time.perf_counter(); COUNT=0
def ck(b):
    global COUNT
    COUNT+=1
    assert b
    if time.perf_counter()-START>600:raise RuntimeError('Frozen 600-second bound')
ns['check']=ck
def geometries():
    return [(r,u,v,d) for r in range(6) for u in range(6-r) for v in range(6-r-u) if 2<=r+u and 2<=r+v and 1<=r+u+v<=5 for d in range(r+1)]
def cellmap(t):
    r,u,v,d=t; n=r+u+v
    R=(1<<r)-1; U=((1<<u)-1)<<r; V=((1<<v)-1)<<(r+u); D=(1<<d)-1
    cells={}
    for s in range(1,1<<n):
        flags=(bool(s&U),bool(s&V))
        key=flags+(((s&D).bit_count()%2,) if d and flags==(False,False) else ())
        cells.setdefault(key,[]).append(s)
    for members in cells.values():
        # log2(cardinality)<=2 mean degree, EXACT integer-power comparison.
        degree=sum(s.bit_count() for s in members); size=len(members)
        ck(size**size<=1<<(2*degree))
    ck(len(cells)<=(5 if d else 4))
    return list(cells.values()),R|U,R|V,D
def values(m,g,a,b,t,mode):
    cells,P,Qmask,D=cellmap(t); r=sum(t[:3]); zsize=1<<r
    gs=[1 if (g>>x)&1 else -1 for x in range(1<<m)]
    ps=[int(z&P==0) for z in range(zsize)]
    qs=[int(z&Qmask==D) for z in range(zsize)]
    es=[]; vs=[]
    for z in range(zsize):
        for x in range(1<<m):
            aa=((a>>x)&1)*ps[z]; bb=((b>>x)&1)*qs[z]
            e=(aa^bb) if mode=='xor' else int(bool(aa or bb))
            es.append(e);vs.append(gs[x]*(-1)**e)
    cap=max(sum(es[x+(z<<m)] for z in range(zsize)) for x in range(1<<m))
    if 4*cap>zsize:return None
    coeff=fwht(vs);den=len(vs)**2
    iz=physical(vs,range(m,m+r));ix=physical(vs,range(m));mask=[(-1)**e for e in es]
    ck(ix>=physical(mask,range(m)));ck(iz==physical(mask,range(m,m+r)))
    alpha=Q(sum(coeff[x+(s<<m)]**2 for s in range(1,zsize) for x in range(1<<m)),den)
    rho=Q(sum(es),len(es));ck(alpha<=4*rho);ck(alpha<=iz)
    for x in range(1<<m):
        for cell in cells:
            weights={coeff[x+(s<<m)]**2 for s in cell}
            ck(len(weights)==1)
    # Full access entropy certificate, including the actual leaves.
    full=ns['entropy']([c*c for c in coeff],den)
    leaves=[ns['entropy']([c*c for c in fwht(vs[z*(1<<m):(z+1)*(1<<m)])],1<<(2*m)) for z in range(zsize)]
    acc=combine((full,Q(1)),*((h,-Q(1,zsize)) for h in leaves))
    hi=interval(acc)[1];bound=(Q(9) if t[3]==0 else Q(19,2))*iz+2*ix
    ck(hi<=bound or (not acc and bound==0))
    return {'alpha':str(alpha),'I_Z':str(iz),'I_X':str(ix),'Q_upper':str(hi)}
def domains(mode):
    geoms=geometries()
    if mode=='pilot':
        for t in [(2,1,1,0),(2,1,1,1),(3,0,1,0),(3,0,1,2)]:
            for md in ['xor','or']:
                for g,a,b in [(0,3,3),(1,1,2),(1,3,1),(2,3,3)]:yield 1,g,a,b,t,md
    else:
        for t in geoms:
            for md in ['xor','or']:
                for g,a,b in itertools.product(range(4),repeat=3):yield 1,g,a,b,t,md
        for t in [(2,1,1,0),(2,1,1,1),(3,0,1,2)]:
            for md in ['xor','or']:
                for g,a,b in itertools.product(range(16),repeat=3):yield 2,g,a,b,t,md
def main():
    mode=argparse.ArgumentParser();mode.add_argument('--mode',choices=['pilot','full'],required=True);args=mode.parse_args()
    tested=outside=0;fixtures=[]
    for params in domains(args.mode):
        res=values(*params)
        if res is None:outside+=1
        else:
            tested+=1
            if len(fixtures)<8:fixtures.append({'parameters':params,**res})
    result={'mode':args.mode,'tested':tested,'outside_final_fiber_cap':outside,'assertions':COUNT,'geometry_count':len(geometries()),'runtime_seconds':time.perf_counter()-START,'fixtures':fixtures,'helper_sha256':hashlib.sha256(prior.read_bytes()).hexdigest()}
    (ROOT/'out'/('CHECK_'+args.mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))
if __name__=='__main__':main()
