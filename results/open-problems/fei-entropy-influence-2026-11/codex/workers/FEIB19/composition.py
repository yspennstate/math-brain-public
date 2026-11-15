"""Optimized filtration composition law, independently compared with full tables."""
import json, math, time, os, resource
import numpy as np
from experiment import phi,wht,masses,best_order,compose_table,analyse,gate,bits

def state(f,n):
    fh=wht(f);a=analyse(f,n)
    return dict(n=n,b=float(fh[0]),rows=[dict(d=r['inf'],c=float(fh[1<<r['i']]),E=r['E']*r['inf'],L=r['F']*r['inf'],path=[r['i']]) for r in a['rows']])

def compose(F,children):
    w=len(children);K=wht(F);idx=np.arange(1<<w);v=[1-g['b']**2 for g in children]
    for j,g in enumerate(children):
        lo=idx[((idx>>j)&1)==0];K[lo]+=g['b']*K[lo+(1<<j)]
    rows=[]
    for j,g in enumerate(children):
        lo=idx[((idx>>j)&1)==0];weight=np.ones(len(lo))
        for l in range(w):
            if l!=j:weight*=np.where((lo>>l)&1,v[l],1)
        alpha=float(np.sum(K[lo+(1<<j)]**2*weight))
        if not alpha:continue
        for r in g['rows']:
            p=K[lo]**2*weight;q=r['c']**2*K[lo+(1<<j)]**2*weight
            init=float(phi(g['b']**2,r['c']**2))
            L=alpha*(r['L']-init)+best_order(p,q)[0]
            E=alpha*(r['E']-init)+float(phi(p,q).sum())
            rows.append(dict(d=alpha*r['d'],c=float(K[1<<j])*r['c'],E=E,L=L,path=[j]+r['path']))
    return dict(n=sum(g['n'] for g in children),b=float(K[0]),rows=rows)

def validate():
    rng=np.random.default_rng(191911);errs={'E':0.,'L':0.,'influence':0.,'singleton':0.,'mean':0.};count=0
    for t in range(100):
        sizes=[2,2,2] if t%2 else [3,2,1]
        gs=[rng.choice([-1.,1.],1<<n) for n in sizes];F=rng.choice([-1.,1.],8)
        full=compose_table(F,gs);ss=compose(F,[state(g,n) if not np.all(g==g[0]) else dict(n=n,b=float(g[0]),rows=[]) for g,n in zip(gs,sizes)])
        fh=wht(full);errs['mean']=max(errs['mean'],abs(ss['b']-fh[0]))
        actual={r['i']:r for r in analyse(full,6)['rows']} if ss['rows'] else {}
        offsets=np.cumsum([0]+sizes)
        for r in ss['rows']:
            i=int(offsets[r['path'][0]]+r['path'][1]);z=actual[i];count+=1
            for k,err in [('E','E'),('L','L')]:
                val=z['inf']*z['E' if k=='E' else 'F'];errs[err]=max(errs[err],abs(r[k]-val))
            errs['influence']=max(errs['influence'],abs(r['d']-z['inf']))
            errs['singleton']=max(errs['singleton'],abs(r['c']-fh[1<<i]))
    return dict(coordinates=count,errors=errs)

def small_towers():
    rows=[];leaf=state(np.array([1.,-1.]),1)
    for arity in [3,5,7,9]:
        F=np.where(bits(arity).sum(axis=1)*2>arity,-1.,1.);ss=leaf
        for depth in range(1,5):
            # Symmetry lets one representative stand for all children.
            ss=compose(F,[ss]*arity);ss['rows']=ss['rows'][:1];r=ss['rows'][0]
            rows.append(dict(name=f'MAJ{arity}_depth{depth}',n=ss['n'],F=r['L']/r['d'],E=r['E']/r['d'],d=r['d']))
    for seq in [('MAJ','AND','OR'),('AND','MAJ','OR'),('MAJ','XOR','AND','OR'),('OR','AND','MAJ','XOR'),('MAJ','MAJ','MAJ','MAJ')]:
        for arity in [3,5,7]:
            ss=leaf
            for kind in seq:
                F=np.where(gate(kind,bits(arity)),-1.,1.);ss=compose(F,[ss]*arity);ss['rows']=ss['rows'][:1]
            r=ss['rows'][0];rows.append(dict(name=f'{seq}_arity{arity}',n=ss['n'],F=r['L']/r['d'],E=r['E']/r['d'],d=r['d']))
    return rows

if __name__=='__main__':
    start=time.time();d=dict(validation=validate(),rows=small_towers());d.update(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(d,open('composition.json','w'),indent=2);print(json.dumps(d,indent=2))
