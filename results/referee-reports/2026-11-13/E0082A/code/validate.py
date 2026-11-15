"""Independent formula, scaling, numerical, and artifact checks."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import csv
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import gammaln
from exact_waiting import patterns, matching


def prob(l,b):
    if l==0:
        return float(b==0)
    if abs(b)>l or (b+l)%2:
        return 0.
    return math.comb(l,(l+b)//2)/2**l


def check_columns():
    worst=0
    checked=0
    for n in range(2,11):
        for a in range(-n,n+1,2):
            for fam in ('BR','FP'):
                if fam=='FP' and a>=0:continue
                words=patterns(n,a,fam)
                col=matching(n,words).sum(axis=0)/2**n
                formula=[]
                for word in words:
                    s=0;val=1.
                    for l in range(1,n):
                        s+=1 if (word>>(n-l))&1 else -1
                        val+=prob(l,s)*(1 if fam=='BR' else (-s/l if s<0 else 0))
                    formula.append(val)
                worst=max(worst,float(np.max(np.abs(col-formula),initial=0)))
                checked+=len(words)
    assert worst<1e-12
    return dict(words_checked=checked,max_column_error=worst)


def return_potential():
    g=[];records=[]
    checkpoints={16,64,256,1024,4096,16384}
    for l in range(1,max(checkpoints)+1):
        # Values beyond 10 sqrt(l) have exponentially negligible contribution.
        b=np.arange(1 if l%2 else 2,min(l,int(10*math.sqrt(l)))+1,2,dtype=float)
        p=np.exp(gammaln(l+1)-gammaln((l+b)/2+1)-gammaln((l-b)/2+1)-l*math.log(2))
        v=float(np.sum(b*p*p)/l);g.append(v)
        if l in checkpoints:
            records.append(dict(m=l,m_times_g_m=l*v,G_m=1+sum(g),log_coefficient=1/(2*math.pi)))
    with Path('data/return_potential.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=records[0].keys());w.writeheader();w.writerows(records)
    return records[-1]


def main():
    report={'nice':os.getpriority(os.PRIO_PROCESS,0),'columns':check_columns(),
            'return_potential':return_potential()}
    exact=list(csv.DictReader(Path('data/exact_waiting.csv').open()))
    report['exact_rows']=len(exact)
    report['rational_rows']=sum(bool(r['exact_rational']) for r in exact)
    report['largest_matching_vs_markov_difference']=max(abs(float(r['matching_mean'])-float(r['markov_mean'])) for r in exact)
    report['largest_matching_equation_residual']=max(float(r['equation_residual']) for r in exact)
    mc=list(csv.DictReader(Path('data/monte_carlo.csv').open()))
    small=[]
    for row in mc:
        if int(row['n'])!=8 or int(row['gaussian']):continue
        ref=next(r for r in exact if r['n']=='8' and r['family']==row['family'] and float(r['alpha'])==float(row['alpha']))
        z=(float(row['mean'])-float(ref['matching_mean']))/float(row['se'])
        small.append(dict(family=row['family'],alpha=float(row['alpha']),z=z))
        assert abs(z)<5
    report['simulator_vs_exact_z_scores']=small
    constants=list(csv.DictReader(Path('data/slepian_constants.csv').open()))
    zero=next(c for c in constants if float(c['alpha'])==0)
    reference=.75-1/math.pi
    z=(float(zero['first_slab'])-reference)/float(zero['first_slab_se'])
    assert abs(z)<5
    report['zero_first_slab']={'exact':reference,'quadrature':float(zero['first_slab']),'z':z}
    lower=[]
    for n,printed in [(100,179.805),(200,358.249),(500,893.041),(1000,1800.002),(2000,3682.022)]:
        from exact_waiting import level
        a=-level(-1,n)
        f=a/n*prob(n,a)
        lower.append(dict(n=n,drop=a,lower_bound=1/f,source_table=printed))
    report['source_table_lower_bound_check']=lower
    forbidden=[str(p) for p in Path('.').rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg','.gif','.webp','.tif','.tiff'}]
    assert not forbidden
    assert all(p.suffix=='.txt' for p in Path('sources').iterdir())
    assert Path('REPORT.md').read_text().splitlines()[0]=='PARTIAL'
    report['forbidden_paper_artifacts']=forbidden
    Path('data/validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
