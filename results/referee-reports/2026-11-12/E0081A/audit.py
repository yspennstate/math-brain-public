#!/usr/bin/env python3
"""Independent finite checks of the proof identities and numerical fit summaries."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
import csv
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import re
import numpy as np
from scipy.optimize import least_squares

ROOT=Path(__file__).resolve().parent


def p(s,b):
    return F(math.comb(s,(s+b)//2),2**s) if abs(b)<=s and (s+b)%2==0 else F(0)


def fp(s,b):
    return F(b,s)*p(s,b) if b>0 else F(0)


def walk(word):
    return list(itertools.accumulate(word,initial=0))


def is_fp(w,a):
    return w[-1]==-a and min(w[:-1])>-a


def record_range(x,y):
    low=0;sites={0}
    for s in range(1,len(y)):
        if y[s]<low:
            low=y[s];sites.add(x[s]-y[s])
    return sites


def checks():
    overlaps=0
    for n in range(2,9):
        for word in itertools.product([-1,1],repeat=n):
            w=walk(word);a=-w[-1]
            if a<=0 or not is_fp(w,a):continue
            for s in range(1,n):
                completions=0
                for suffix in itertools.product([-1,1],repeat=s):
                    nw=walk(word[s:]+suffix)
                    completions+=is_fp(nw,a)
                assert F(completions,2**s)==fp(s,-w[s])
                overlaps+=1
    # Exact return-probability identity, checked by summation independently.
    for s in range(1,101):
        g=sum((F(b,s)*p(s,b)**2 for b in range(1,s+1)),F(0))
        assert g==F(math.comb(s-1,(s-1)//2)**2,4**s)
    ranges=[]
    for m in range(1,8):
        paths=[walk(w) for w in itertools.product([-1,1],repeat=m)]
        erange=F(sum(len(record_range(x,y)) for x in paths for y in paths),4**m)
        G=1+sum((F(math.comb(s-1,(s-1)//2)**2,4**s) for s in range(1,m+1)),F(0))
        EV=1+sum((sum((fp(s,b) for b in range(1,s+1)),F(0)) for s in range(1,2*m+1)),F(0))
        assert G*erange<=EV
        ranges.append({'m':m,'E_range_exact':str(erange),'G_times_E_range':str(G*erange),'E_V_2m':str(EV)})
    inclusions=0
    for n in range(2,9):
        m=n//2
        for word in itertools.product([-1,1],repeat=n+m):
            w=walk(word);x=w[:m+1];y=[w[n+s]-w[n] for s in range(m+1)]
            B=w[n]-w[m];R=record_range(x,y)
            for a in range(1,n+1):
                hit=any(w[n+s]-w[s]==-a and min(w[s:n+s])>w[n+s] for s in range(m+1))
                if hit:assert B+x[m]+a in R
                inclusions+=1
    return {'overlap_word_shift_cases':overlaps,'return_identity_times':100,
            'middle_segment_path_endpoint_cases':inclusions,'exact_range_checks':ranges}


def readcsv(name):
    with (ROOT/'data'/name).open() as f:return list(csv.DictReader(f))


def fits(rows):
    rows=[r for r in rows if int(r['n'])>=100]
    x=np.array([int(r['n']) for r in rows],dtype=float)
    y=np.array([float(r['mean'])/float(r['n']) for r in rows])
    se=np.array([float(r['se'])/float(r['n']) for r in rows])
    models={
        'A*n':(lambda b:b[0]*np.ones_like(x),[4.]),
        'A*n*log(n)':(lambda b:b[0]*np.log(x),[.7]),
        'A*n**beta':(lambda b:np.exp(b[0]+(b[1]-1)*np.log(x)),[1.,1.05]),
        'n*(A+B*log(n))':(lambda b:b[0]+b[1]*np.log(x),[2.7,.3]),
    }
    out={}
    for label,(fun,start) in models.items():
        res=least_squares(lambda b:(fun(b)-y)/se,start)
        par=res.x.tolist()
        if label=='A*n**beta':par=[math.exp(par[0]),par[1]]
        out[label]={'parameters':par,'weighted_squared_residual':float(np.sum(res.fun**2)),
                    'degrees_of_freedom':len(x)-len(start),'n_min':int(min(x)),'n_max':int(max(x))}
    (ROOT/'data/fits.json').write_text(json.dumps(out,indent=2)+'\n')
    return out


def insert_table(text,marker,table):
    start='<!-- '+marker+' -->';end='<!-- END_'+marker+' -->'
    block=start+'\n\n'+table+'\n\n'+end
    if end in text:return re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:block,text,flags=re.S)
    return text.replace(start,block)


def main():
    result=checks();rows=readcsv('monte_carlo.csv');result['fits']=fits(rows)
    (ROOT/'data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
    table='| n | a | Trials | Mean T | Approx. 95% CI | Mean / n | Mean / (n log n) |\n|---:|---:|---:|---:|---:|---:|---:|\n'
    for r in rows:
        table+=f"| {int(r['n']):,} | {r['a']} | {int(r['reps']):,} | {float(r['mean']):,.3f} | [{float(r['ci95_low']):,.3f}, {float(r['ci95_high']):,.3f}] | {float(r['mean_over_n']):.4f} | {float(r['mean_over_nlogn']):.4f} |\n"
    report=(ROOT/'REPORT.md').read_text();report=insert_table(report,'MONTE_CARLO_TABLE',table.rstrip())
    table='| m | Trials | Mean range | Standard error | Mean record visits | Mean range × log(m) / sqrt(m) |\n|---:|---:|---:|---:|---:|---:|\n'
    for r in readcsv('record_range.csv'):
        table+=f"| {int(r['m']):,} | {int(r['reps']):,} | {float(r['range_mean']):.4f} | {float(r['range_se']):.4f} | {float(r['visits_mean']):.4f} | {float(r['range_logm_over_sqrtm']):.4f} |\n"
    report=insert_table(report,'RANGE_TABLE',table.rstrip());(ROOT/'REPORT.md').write_text(report)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
