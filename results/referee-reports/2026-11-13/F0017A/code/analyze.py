"""Summarize complete-cube counts and fit a descriptive finite-size curve.

No numerical determinant routines or nonstandard Python packages are used.
"""
import collections
import csv
import json
import math
from pathlib import Path
import random
import statistics
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'

def quantile_hist(hist,q):
    total=sum(hist.values())
    def at(rank):
        acc=0
        for z,c in sorted(hist.items()):
            acc+=c
            if rank<acc:return z
        raise ValueError(rank)
    f=(total-1)*q;lo=math.floor(f);hi=math.ceil(f)
    return at(lo)+(at(hi)-at(lo))*(f-lo)

def wilson(k,n):
    z=1.959963984540054;p=k/n;den=1+z*z/n
    center=(p+z*z/(2*n))/den
    radius=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return max(0,center-radius),min(1,center+radius)

def fit(points):
    # log(median Z) = intercept + beta*n - 0.5*log(n!).
    xs=[n for n,m in points];ys=[math.log(m)+.5*math.lgamma(n+1) for n,m in points]
    xm=statistics.mean(xs);ym=statistics.mean(ys)
    beta=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs)
    intercept=ym-beta*xm
    rmse=math.sqrt(statistics.mean((y-intercept-beta*x)**2 for x,y in zip(xs,ys)))
    return dict(intercept=intercept,beta=beta,log_rmse=rmse,discrete_peak_n=math.floor(math.exp(2*beta)))

def logistic_fit(rows):
    rows=[r for r in rows if not r['exact']]
    hits=sum(r['stubborn'] for r in rows);total=sum(r['count'] for r in rows)
    a=math.log(hits/(total-hits));b=0.;origin=12
    def likelihood(a,b):
        return sum(r['stubborn']*(a+b*(r['n']-origin))-r['count']*math.log1p(math.exp(a+b*(r['n']-origin))) for r in rows)
    for _ in range(80):
        ga=gb=iaa=iab=ibb=0.
        for r in rows:
            x=r['n']-origin;p=1/(1+math.exp(-(a+b*x)));w=r['count']*p*(1-p);s=r['stubborn']-r['count']*p
            ga+=s;gb+=x*s;iaa+=w;iab+=x*w;ibb+=x*x*w
        d=iaa*ibb-iab*iab;da=(ibb*ga-iab*gb)/d;db=(iaa*gb-iab*ga)/d
        if max(abs(da),abs(db))<1e-11:break
        step=1.;old=likelihood(a,b)
        while likelihood(a+step*da,b+step*db)<old-1e-12:step*=.5
        a+=step*da;b+=step*db
    se=math.sqrt(iaa/d)
    return dict(formula='logit P(stubborn at n) = intercept_at_n12 + slope*(n-12)',
                intercept_at_n12=a,slope=b,slope_approx95=[b-1.9599639845*se,b+1.9599639845*se],
                predicted_p24=1/(1+math.exp(-(a+12*b))),hits=hits,samples=total,
                warning='Finite-range descriptive binomial model; not a conjectured asymptotic law.')

def svg(rows,model):
    # Standalone vector chart made from our experiment; no source-page imagery.
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="470" viewBox="0 0 1100 470">',
         '<rect width="1100" height="470" fill="white"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#222} .axis{stroke:#555;fill:none} .grid{stroke:#ddd}</style>',
         '<text x="45" y="30" font-size="20">Diagonal sign resilience: exact counts and seeded samples</text>',
         '<text x="45" y="56" font-size="13">Every diagonal completion checked. Finite-size evidence only.</text>']
    x=lambda n,left:left+(n-4)/20*440
    for left,title in [(60,'Probability of stubbornness (95% Wilson intervals)'),(620,'Median number of singular diagonal completions')]:
        out.append(f'<text x="{left}" y="93" font-size="14">{title}</text>')
        out.append(f'<path class="axis" d="M {left} 110 V 390 H {left+440}"/>')
        for n in [4,8,12,16,20,24]:
            xx=x(n,left);out.append(f'<text x="{xx-8}" y="412" font-size="12">{n}</text>')
        out.append(f'<text x="{left+200}" y="438" font-size="13">matrix size n</text>')
    yp=lambda p:390-p/.045*280
    for p in [0,.01,.02,.03,.04]:
        y=yp(p);out.append(f'<path class="grid" d="M60 {y} H500"/><text x="20" y="{y+4}" font-size="12">{p:.2f}</text>')
    yz=lambda z:390-math.log10(z)/4*280
    for z in [1,10,100,1000,10000]:
        y=yz(z);out.append(f'<path class="grid" d="M620 {y} H1060"/><text x="570" y="{y+4}" font-size="12">{z}</text>')
    for r in rows:
        if r['n']<4:continue
        xx=x(r['n'],60);color='#a94818' if r['exact'] else '#155e91'
        if not r['exact']:
            lo,hi=r['wilson95'];out.append(f'<path stroke="{color}" d="M{xx} {yp(lo)} V {yp(hi)} M{xx-3} {yp(lo)} H{xx+3} M{xx-3} {yp(hi)} H{xx+3}"/>')
        out.append(f'<circle cx="{xx}" cy="{yp(r["p_stubborn"])}" r="3.2" fill="{color}"/>')
        out.append(f'<circle cx="{x(r["n"],620)}" cy="{yz(r["median_z"])}" r="3.2" fill="{color}"/>')
    curve=[]
    for j in range(121):
        n=12+j/10;m=math.exp(model['intercept']+model['beta']*n-.5*math.lgamma(n+1));curve.append(f'{x(n,620):.2f},{yz(m):.2f}')
    out.append('<polyline points="'+' '.join(curve)+'" stroke="#278067" stroke-width="2" fill="none"/>')
    out.append('<text x="650" y="460" font-size="12">Orange: exhaustive. Blue: Monte Carlo. Green: descriptive fit, n=12–24.</text></svg>')
    text='\n'.join(out);ET.fromstring(text)
    (DATA/'trend.svg').write_text(text)

def main():
    rows=[];distributions={};samples={}
    for n in range(1,25):
        if n<=6:
            obj=json.loads((DATA/f'exhaustive_{n}.json').read_text());hist={int(k):v for k,v in obj['histogram'].items()};total=obj['representatives'];exact=True
            pair=obj['pair_failures'];no_pair_fail=obj['other_failures']
        else:
            a=[json.loads(x) for x in (DATA/f'monte_{n}.jsonl').read_text().splitlines()]
            hist=collections.Counter(x['singular_switchings'] for x in a);total=len(a);exact=False
            samples[n]=[x['singular_switchings'] for x in a]
            pair=sum(x['pair_events']>0 for x in a)
            no_pair_fail=sum(x['singular_switchings']>0 and x['pair_events']==0 for x in a)
        stubborn=hist.get(0,0)
        row=dict(n=n,exact=exact,count=total,stubborn=stubborn,p_stubborn=stubborn/total,
                 wilson95=None if exact else wilson(stubborn,total),
                 mean_z=sum(z*c for z,c in hist.items())/total,
                 median_z=quantile_hist(hist,.5),q10_z=quantile_hist(hist,.1),q90_z=quantile_hist(hist,.9),
                 min_z=min(hist),max_z=max(hist),pair_failures=pair,other_failures=no_pair_fail)
        rows.append(row);distributions[n]=dict(sorted(hist.items()))
    points=[(r['n'],r['median_z']) for r in rows if r['n']>=12]
    model=fit(points);model['formula']='log(median Z_n) = intercept + beta*n - 0.5*log(n!)'
    model['fit_n']=[n for n,m in points];model['baseline_beta_log4']=math.log(4)
    rng=random.Random(170017999);bs=[]
    for _ in range(300):
        bpoints=[(n,statistics.median(rng.choices(samples[n],k=len(samples[n])))) for n,m in points]
        bs.append(fit(bpoints)['beta'])
    bs.sort();model['beta_bootstrap95']=[bs[7],bs[292]];model['bootstrap_repetitions']=300
    model['warning']='Descriptive fit on n=12..24; no justified asymptotic extrapolation or probability-of-zero model.'
    model['stubbornness_logistic_fit']=logistic_fit(rows)
    (DATA/'summary.json').write_text(json.dumps(rows,indent=2)+'\n')
    with (DATA/'summary.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (DATA/'distributions.json').write_text(json.dumps(distributions,indent=2)+'\n')
    (DATA/'trend_fit.json').write_text(json.dumps(model,indent=2)+'\n')
    prime=2**61-1;ll=4
    for _ in range(59):ll=(ll*ll-2)%prime
    assert ll==0
    checks=dict(mersenne_prime=prime,lucas_lehmer_exponent=61,lucas_lehmer_iterations=59,
                lucas_lehmer_final_residue=ll,
                all_squared_hadamard_bounds_below_half_prime=all(4*n**n<prime**2 for n in range(1,25)),
                n24_hadamard_bound=24**12,half_prime_floor=prime//2,max_n=24)
    (DATA/'arithmetic_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    lines=['| n | matrices / representatives | stubborn | probability (95% Wilson for samples) | median Z | mean Z | 10%–90% Z |',
           '|---:|---:|---:|---|---:|---:|---|']
    for r in rows:
        p=f'{r["p_stubborn"]:.6f}'
        if r['wilson95'] is not None:p+=' ['+', '.join(f'{x:.6f}' for x in r['wilson95'])+']'
        else:p+=' exact'
        lines.append(f'| {r["n"]} | {r["count"]:,} | {r["stubborn"]:,} | {p} | {r["median_z"]:g} | {r["mean_z"]:.3f} | {r["q10_z"]:g}–{r["q90_z"]:g} |')
    (DATA/'table.txt').write_text('\n'.join(lines)+'\n')
    svg(rows,model)
    print(json.dumps(model,indent=2))
    print('\n'.join(lines))

if __name__=='__main__':main()
