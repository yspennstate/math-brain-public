"""Recompute submitted and independent statistics using scalar math.fsum."""
import csv
import hashlib
import json
import math
import os
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'
os.environ['MPLCONFIGDIR']=str(OUT/'mplconfig')
os.environ['MPLBACKEND']='Agg'
os.environ['XDG_CACHE_HOME']=str(OUT/'cache')

def moments(pairs):
    n=len(pairs)
    x=[p[0] for p in pairs];y=[p[1] for p in pairs]
    xm=math.fsum(x)/n;ym=math.fsum(y)/n
    xx=math.fsum((v-xm)**2 for v in x)
    yy=math.fsum((v-ym)**2 for v in y)
    xy=math.fsum((a-xm)*(b-ym) for a,b in pairs)
    return math.fsum((a-b)**2 for a,b in pairs)/n, xy/math.sqrt(xx*yy)

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    result={}
    raw={}
    samples=ROOT/'claim_files/data/edge_samples.csv'
    for r in csv.DictReader(samples.open()):
        key=(r['model'],int(r['n']),int(r['eigenvalue_rank']),int(r['rep']))
        raw.setdefault(key,{})[float(r['s'])]=float(r['edge_value'])
    errors=[]
    for r in csv.DictReader((ROOT/'claim_files/data/summary.csv').open()):
        key=(r['model'],int(r['n']),int(r['rank']))
        lag=float(r['lag_s'])
        pairs=[(v[0.],v[lag]) for k,v in raw.items() if k[:3]==key]
        assert len(pairs)==int(r['reps'])
        mse,corr=moments(pairs)
        errors.append((abs(mse-float(r['mean_squared_increment'])),abs(corr-float(r['correlation']))))
    result['submitted_summary_rows_checked']=len(errors)
    result['submitted_max_mse_error']=max(e[0] for e in errors)
    result['submitted_max_correlation_error']=max(e[1] for e in errors)
    own=defaultdict(list)
    for r in csv.DictReader((OUT/'independent_samples.csv').open()):
        key=(r['model'],int(r['n']),int(r['rank']),float(r['s']))
        a,b=float(r['initial']),float(r['final'])
        assert abs(b-a-float(r['increment']))<1e-12
        own[key].append((a,b))
    errors=[]
    summary=list(csv.DictReader((OUT/'independent_summary.csv').open()))
    for r in summary:
        key=(r['model'],int(r['n']),int(r['rank']),float(r['s']))
        mse,corr=moments(own[key])
        assert len(own[key])==int(r['replicates'])
        errors.append((abs(mse-float(r['mean_squared_increment'])),abs(corr-float(r['correlation']))))
    result['independent_summary_rows_checked']=len(errors)
    result['independent_max_mse_error']=max(e[0] for e in errors)
    result['independent_max_correlation_error']=max(e[1] for e in errors)
    assert all(v<1e-12 for k,v in result.items() if 'error' in k)
    result['claim_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in (ROOT/'claim_files').rglob('*') if p.is_file()}
    (OUT/'data_audit.json').write_text(json.dumps(result,indent=2))

    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(6,4))
    for model,label,style in [('tridiagonal','Independent radial OU tridiagonal','o-'),('matrix_OU','Hermitian matrix OU / normalized Brownian motion','s-')]:
        rows=[r for r in summary if r['model']==model and int(r['rank'])==1 and float(r['s'])==1]
        ax.errorbar([int(r['n']) for r in rows],[float(r['mean_squared_increment']) for r in rows],
                    yerr=[1.96*float(r['se_squared_increment']) for r in rows],fmt=style,capsize=3,label=label)
    ax.set_xscale('log',base=2)
    ax.set_xlabel('Matrix size n')
    ax.set_ylabel('Mean squared scaled top-eigenvalue increment')
    ax.set_title('DBM edge time s = 1; error bars are ±1.96 standard errors')
    ax.legend(fontsize=8)
    ax.grid(alpha=.25)
    fig.tight_layout()
    fig.savefig(OUT/'independent_edge_increments.svg')
    print(json.dumps({k:v for k,v in result.items() if k!='claim_sha256'},indent=2))

if __name__=='__main__':
    main()
