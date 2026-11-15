"""Independent group-law, integer-recurrence, spectrum and theorem-bound audit."""
from experiment import *
import csv

def independent_crossing(g, selected, model, time_value, epsilon=Fraction(1,4)):
    support=set(selected)|{g.inv(s) for s in selected}
    freq=Counter()
    if model=='union':
        freq.update({s:1 for s in support}); hold=len(support)
    else:
        for s in selected:freq[s]+=1;freq[g.inv(s)]+=1
        hold=2*len(selected)
    denom=2*hold;counts=[0]*g.n;counts[g.e]=1;power=1
    before=None
    # Scatter along forward products; experiment.py instead gathers via permutations.
    for t in range(time_value+1):
        if t>=time_value-1:
            tv=Fraction(sum(abs(g.n*c-power) for c in counts),2*g.n*power)
            if t==time_value-1:before=tv
            if t==time_value:assert tv<=epsilon and (before is None or before>epsilon)
        if t<time_value:
            nxt=[hold*c for c in counts]
            for i,c in enumerate(counts):
                if not c:continue
                for s,mult in freq.items():nxt[g.index[g.mul(g.elements[i],s)]]+=mult*c
            counts=nxt;power*=denom

def audit():
    rows=[json.loads(line) for line in (ROOT/'data'/'samples.jsonl').read_text().splitlines()]
    rng=np.random.default_rng(930094)
    factories=[lambda:abelian([11,11]),lambda:abelian([2]*8),lambda:dihedral(31),
               lambda:symmetric(8),lambda:psl(11),lambda:heisenberg(7)]
    notes=[]
    for f in factories:
        g=f()
        for _ in range(100):
            x,y,z=[g.elements[i] for i in rng.integers(g.n,size=3)]
            assert g.mul(g.mul(x,y),z)==g.mul(x,g.mul(y,z))
            assert g.mul(x,g.inv(x))==g.elements[g.e]
            assert g.mul(g.elements[g.e],x)==x
        notes.append(f'{g.name}: 100 independent associativity/inverse/identity checks passed')
        rec=next(r for r in rows if r['group']==g.name and r['model']=='union')
        selected=[tuple(s) for s in rec['generators']]
        support,maps,multiplicities=kernel(g,selected)
        weights=np.ones(len(maps),dtype=np.int64)
        gap,residual,_=spectrum(g,maps,weights,len(maps),2*len(maps))
        assert abs(gap-rec['gap'])<2e-9
        notes.append(f'{g.name}: independent ARPACK start agrees, absolute gap discrepancy {abs(gap-rec["gap"]):.3g}')
    # Different exact recurrence implementation, representatives of every family.
    for f in [lambda:abelian([31]),lambda:dihedral(7),lambda:symmetric(4),lambda:psl(5),lambda:heisenberg(3)]:
        g=f()
        for model in ['union','tuple']:
            r=next(r for r in rows if r['group']==g.name and r['model']==model)
            independent_crossing(g,[tuple(s) for s in r['generators']],model,r['times']['1/4'])
        notes.append(f'{g.name}: forward-scatter rational TV crossing agrees for both kernels')
    # Full dihedral spectrum, not merely the numerical gap.
    for p in [3,5,7,17]:
        g=dihedral(p)
        for selected in [[(0,1),(1,1)],[(1,0),(0,1)]]:
            support,maps,mult=kernel(g,selected);m=len(maps)
            _,_,mat=spectrum(g,maps,np.ones(m,dtype=np.int64),m,2*m)
            actual=np.linalg.eigvalsh(mat.toarray())
            if all(s[1] for s in selected):
                expected=[.5+.5*math.cos(math.pi*j/p) for j in range(2*p)]
            else:expected=[.5+(2*math.cos(2*math.pi*j/p)+sig)/6 for j in range(p) for sig in [-1,1]]
            assert max(abs(actual-np.sort(expected)))<1e-12
        notes.append(f'D{2*p}: both complete spectral formulas agree with dense diagonalization')
    max_analytic=max(abs(r['gap']-r['analytic_gap']) for r in rows if r['analytic_gap'] is not None)
    assert all(r['times']['1/4']<=r['spectral_tv_upper'] for r in rows)
    assert all(r['eigen_residual']<1e-9 for r in rows)
    assert all(c['below_margin']>=0 and (c['previous_above_margin'] is None or c['previous_above_margin']>0)
               for r in rows for c in r['exact_integer_certificates'].values())
    for r in rows:
        if r['family']=='dihedral' and r['k']==2 and r['model']=='union':
            p=r['parameters']['p']
            assert math.log(2)*(3*p*p/(2*math.pi**2)-1)<=r['times']['1/4']<=2*p*p
        if r['family'] in ['abelian','heisenberg']:
            M=r['order'] if r['family']=='abelian' else r['parameters']['p']**2
            lower=(max(0,(M/2)**(1/r['k'])-1))**2/8
            assert r['times']['1/4']+1e-9>=lower
    h=(1.5*math.log(1.5)+.5*math.log(.5))/2
    notes.extend([f'All {len(rows)} records have four integer-certified first TV crossings.',
                  f'Maximum character/dihedral gap discrepancy: {max_analytic:.6g}',
                  f'J(1/2)={h:.15g}; 2/J(1/2)={2/h:.15g}.',
                  f'Maximum recorded RSS: {max(r["peak_rss_raw"] for r in rows)/1024**2:.3f} MiB on macOS.',
                  'All measured t_mix(1/4) are below the spectral upper bound.',
                  'All tested abelian/Heisenberg quotient lower bounds are satisfied.',
                  'All sampled prime-dihedral generating pairs satisfy both explicit quadratic bounds.',
                  'Resource usage: one process, one BLAS thread, priority 10.'])
    groups={}
    for r in rows:
        key=(r['group'],r['k'],r['model'])
        groups.setdefault(key,[]).append(r)
    fields=['group','order','k','model','samples','gap_min','gap_max','t25_min','t25_max','spectral_upper_min','spectral_upper_max']
    with (ROOT/'data'/'summary.csv').open('w') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
        for (name,k,model),rs in groups.items():
            writer.writerow(dict(group=name,order=rs[0]['order'],k=k,model=model,samples=len(rs),
                                 gap_min=min(r['gap'] for r in rs),gap_max=max(r['gap'] for r in rs),
                                 t25_min=min(r['times']['1/4'] for r in rs),t25_max=max(r['times']['1/4'] for r in rs),
                                 spectral_upper_min=min(r['spectral_tv_upper'] for r in rs),spectral_upper_max=max(r['spectral_tv_upper'] for r in rs)))
    (ROOT/'data'/'audit.txt').write_text('\n'.join(notes)+'\n')
    print('\n'.join(notes))

if __name__=='__main__':
    with threadpool_limits(limits=1):audit()
