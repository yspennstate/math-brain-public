"""Write tables and small provenance/resource records from saved results."""
import csv,gzip,json,math,os,resource
from decimal import Decimal as D,localcontext,getcontext
from pathlib import Path
import numpy as np
from levels import ROOT,candidates,profile

def main():
    getcontext().prec=70
    families=json.load(open(ROOT/'families.json'));towers=json.load(open(ROOT/'towers_decimal_50.json'));hills=json.load(open(ROOT/'hill.json'))
    large=[]
    for n in [1024,1025,1026]:
        r=json.load(open(ROOT/f'selector_profile_n{n}.json'));r['name']=f'selector_majority1023_parity{n-1024}';large.append(r)
    rows=families+towers+hills+large
    with gzip.open(ROOT/'level_profiles.csv.gz','wt',newline='') as out:
        writer=csv.writer(out);writer.writerow(['name','n','d','A_d_bits','W_d_probability','dW_d','(d-1)W_(d-1)'])
        for i,r in enumerate(rows):
            name=r['name'] if 'name' in r else (f"tower{r['depth']}" if 'depth' in r else f"hill_n{r['n']}_{r['objective']}")
            W=r['W'];A=r['A']
            for d in range(len(W)):
                writer.writerow([name,r['n'],d,A[d],W[d],D(d)*D(str(W[d])),D(d-1)*D(str(W[d-1])) if d else 0])
    best={key:dict(ratio=0.) for key in candidates(np.zeros(3))}
    for r in rows:
        if 'depth' in r:
            for key,entry in r['maxima'].items():
                if float(entry['ratio'])>best[key]['ratio']:
                    best[key]=dict(ratio=float(entry['ratio']),d=entry['d'],n=r['n'],name=f"tower{r['depth']}")
            continue
        W=np.array(r['W']);A=np.array(r['A'])
        for key,den in candidates(W).items():
            ratio=np.divide(A[2:],den[2:],out=np.zeros(len(W)-2),where=den[2:]>1e-100)
            if len(ratio) and ratio.max()>best[key]['ratio']:
                d=int(ratio.argmax()+2);best[key]=dict(ratio=float(ratio[d-2]),d=d,n=r['n'],
                    name=r['name'] if 'name' in r else (f"tower{r['depth']}" if 'depth' in r else f"hill_n{r['n']}_{r['objective']}"))
    # Analytic adjacent-layer non-Boolean examples saturating the level Jensen bound.
    real=[]
    for d in [2,4,8,16,32,64,128]:
        n=d*d;G=d/2*math.log2(1+(n-d+1)/d);I=d-.5
        real.append(dict(d=d,n=n,G=G,I=I,G_over_I=G/I))
    summary=dict(truth_table_families=len(families),towers=len(towers),hills=len(hills),
                 analytic_full_profiles=len(large),maxima_over_saved_profiles=best,nonboolean_layers=real)
    (ROOT/'numerical_summary.json').write_text(json.dumps(summary,indent=2))
    with localcontext() as context:
        context.prec=60
        prior=json.load(open(ROOT/'towers_decimal_40.json'));relative=D(0);mass=D(0)
        for old,new in zip(prior,towers):
            for key in ['W','A']:
                for x,y in zip(old[key],new[key]):
                    a,b=D(x),D(y)
                    if b:relative=max(relative,abs(a-b)/abs(b))
                    else:assert not a
            mass=max(mass,abs(D(new['probability_mass_error'])))
            for key in old['maxima']:assert old['maxima'][key]['d']==new['maxima'][key]['d']
        assert relative<D('1e-30')
        (ROOT/'tower_precision_audit.json').write_text(json.dumps(dict(
            precisions_decimal_digits=[40,50],max_pointwise_relative_difference=str(relative),
            max_mass_error=str(mass),all_level_maximizers_stable=True,
            smallest_positive_W=towers[-1]['min_positive_W']),indent=2))
    # Measure the largest truth-table family once (4-address bits + 16 data bits).
    n=20;x=np.arange(1<<n);address=x&15;f=np.where(((x>>(4+address))&1)!=0,-1.,1.)
    row=profile(f)
    (ROOT/'resources.json').write_text(json.dumps(dict(inherited_nice=os.getpriority(os.PRIO_PROCESS,0),
        numerical_threads={key:os.environ.get(key) for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},
        measured_case='address_4, full 20-variable truth table and every edge',
        max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        audit_case=dict(n=n,I=row['I'],H=row['H'],G=row['G']),
        generator_seen_bitset_bytes=268435456),indent=2))
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
