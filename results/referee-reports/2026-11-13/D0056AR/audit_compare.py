#!/usr/bin/env python3
"""Read submitted data only; independently reconstruct tables and regressions."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import sys
sys.set_int_max_str_digits(0)
import csv,json,re,math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import mpmath as mp

ROOT=Path(__file__).parent
D=ROOT/'claim_files/data'
O=ROOT/'audit_results'
text=(ROOT/'CLAIM.md').read_text()
laws={'{0,2}':'two2','{0,5}':'two5','geometric':'geom',
      'b=2.5':'power2.5','b=3':'power3','b=3.5':'power3.5','b=4':'power4',
      'sparse (rho=1)':'sparse'}

def read(path):
    with path.open() as f:return list(csv.DictReader(f))

def indexed(path):return {int(r['n']):r for r in read(path)}

def source(m,law):
    p=D/f'cert_m{m}_{law}.csv'
    return p if p.exists() else D/f'm{m}_{law}.csv'

def table(section):
    body=text.split('### '+section,1)[1].split('\n### ',1)[0]
    ans=[]
    for line in body.splitlines():
        if line.startswith('|'):
            row=[x.strip() for x in line.strip('|').split('|')]
            if row[0].isdigit():ans.append(row)
    return ans


def check():
    checks=[];independent=[];fit_checks=[]
    for row in table('5.0'):
        m,n=int(row[0]),int(row[1]);value=float(indexed(source(m,'sparse'))[n]['n2q'])
        assert row[2]==format(value,'.9f')
        checks.append(['sparse',m,n])
    for row in table('5.1'):
        m,law=int(row[0]),laws[row[1]];saved=indexed(source(m,law))
        assert row[2]==('C' if source(m,law).name.startswith('cert_') else 'F')
        for i,n in enumerate((1000,5000,10000)):
            assert row[3+i]==format(float(saved[n]['n2q']),'.6f')
            checks.append(['main',m,law,n])
        fresh=O/f'm{m}_{law}_N10000.csv'
        if fresh.exists():
            rr=indexed(fresh)
            for n in (1000,5000,10000):
                independent.append(dict(m=m,law=law,n=n,
                    reported=float(saved[n]['n2q']),
                    independent=float(rr[n]['n2q']),
                    difference=float(saved[n]['n2q'])-float(rr[n]['n2q']),
                    source='C' if source(m,law).name.startswith('cert_') else 'F'))
    certified=[]
    for row in table('5.2'):
        m,law,n=int(row[0]),laws[row[1]],int(row[2]);p=source(m,law)
        r=indexed(p)[n];K=json.loads(p.with_suffix('.json').read_text())['K']
        lo=F(r['q_lower_numerator'])/F(r['q_lower_denominator'])*n*n
        hi=(F(r['q_upper_numerator'])/F(r['q_upper_denominator'])+
            F(m*(m**(n+1)-1),(m-1)*m**(K+1)))*n*n
        low,high=map(F,row[3].strip('[]').split(','))
        assert low<=lo<=hi<=high
        fresh=O/f'm{m}_{law}_N10000.csv'
        if fresh.exists():
            rr=indexed(fresh)[n];ll,hh=F(rr['lower']),F(rr['upper'])
            assert low<=ll<=hh<=high
            # Quantization error >= 0 and the audit bound is much smaller than
            # the displayed interval; no comparison of floating-point centres.
            certified.append(dict(m=m,law=law,n=n,value=float(rr['n2q']),
                                  audit_width=float(hh-ll),inside_claim=True))
        checks.append(['endpoint',m,law])
    # Regressions are reconstructed with column L2 normalization.
    for r in read(D/'fits.csv'):
        p=ROOT/'claim_files'/r['source'];saved=read(p)
        z=[x for x in saved if int(x['n'])>=int(r['nmin'])]
        n=np.array([int(x['n']) for x in z],dtype=float)
        y=np.array([float(x['n2q']) for x in z])
        model=r['model']
        if model=='C+a/n+b*log(n)/n':
            x=np.column_stack((np.ones(len(n)),1/n,np.log(n)/n))
        elif model=='C+a/sqrt(n)+b/n':
            # Saved coefficient convention uses sqrt(5000/n), 5000/n.
            x=np.column_stack((np.ones(len(n)),np.sqrt(5000/n),5000/n))
        elif model=='C+a/log(n)+b/log(n)^2':
            x=np.column_stack((np.ones(len(n)),1/np.log(n),1/np.log(n)**2))
        else:raise ValueError(model)
        norm=np.linalg.norm(x,axis=0)
        coeff=np.linalg.lstsq(x/norm,y,rcond=None)[0]/norm
        rmse=np.sqrt(np.mean((x@coeff-y)**2))
        assert abs(coeff[0]-float(r['C']))<2e-9
        assert abs(rmse-float(r['rmse']))<1e-12
        fit_checks.append(dict(m=int(r['m']),law=r['law'],nmin=int(r['nmin']),
                              model=model,C=float(coeff[0]),rmse=float(rmse)))
    for row in table('5.3'):
        m,law=int(row[0]),laws[row[1]]
        if len(row)==5 and row[2].startswith('C+'):
            fit=next(x for x in fit_checks if x['m']==m and x['law']==law and x['model']==row[2])
            assert abs(float(row[3])-fit['C'])<=5.1e-9
        else:
            for nmin,disp in zip((1000,3000,5000),row[2:]):
                fit=next(x for x in fit_checks if x['m']==m and x['law']==law and
                         x['nmin']==nmin and x['model']=='C+a/n+b*log(n)/n')
                assert abs(float(disp)-fit['C'])<=5.1e-9
        checks.append(['fit_table',m,law])
    for row in table('5.4'):
        m,law=int(row[0]),laws[row[1]]
        if not row[2].startswith('4.') and len(row)==4:
            a=float(read(D/f'm{m}_{law}.csv')[-1]['n2q'])
            b=float(read(D/f'check_m{m}_{law}.csv')[-1]['n2q'])
            c=float(read(D/f'cert_m{m}_{law}.csv')[-1]['n2q'])
            assert abs(float(row[2])-(a-b))<max(1e-14,abs(a-b)*6e-5)
            assert abs(float(row[3])-(a-c))<max(1e-14,abs(a-c)*6e-5)
        elif len(row)==5:
            rr=indexed(D/f'long_m{m}_{law}.csv')
            for n,value in zip((10000,50000,100000),row[2:]):
                assert value==format(float(rr[n]['n2q']),'.8f')
        checks.append(['float_diagnostic',m,law])
    mp.mp.dps=90
    leaf_checks=[]
    for r in read(D/'sparse_leaf_bounds.csv'):
        m,j,n=int(r['m']),int(r['j']),int(r['n'])
        A=(m-1)*mp.zeta(2)-mp.polylog(2,mp.mpf(1)/2)
        T=sum(mp.mpf(m)**(-2**i)/(i*i*2**i) for i in range(1,16))
        c=1/(A+T)
        bound=n*n*(-mp.expm1(-c/(m*j*j*2**j)))
        # Submitted initialization was at 70 decimal digits; extra printed
        # digits in this diagnostic CSV do not increase its input precision.
        assert abs(bound-mp.mpf(r['n2_leaf_bound']))<mp.mpf('1e-65')
        assert bound<=mp.mpf(r['n2_observed'])
        leaf_checks.append([m,j,n,str(bound)])
    for m in (2,3):
        p=O/f'm{m}_sparse_N10000.csv'
        if p.exists():
            rr=indexed(p)
            for row in table('5.0'):
                if int(row[0])==m:
                    n=int(row[1]);assert abs(float(rr[n]['n2q'])-float(row[2]))<=5.1e-10
    truncation=[]
    for m in (2,3):
        B=mp.mpf(m)**(mp.mpf(1)/(m-1))
        bound=B*mp.mpf(m)**(-128)/(m-1)
        truncation.append(dict(m=m,report_uniform_support_bound=str(bound),
                               audit_endpoint_bound=str(mp.mpf(10001)*mp.mpf(m)**(-192))))
    long_checks=[]
    for law in ('two2','power3'):
        fresh=O/f'fft_long_{law}_N100000.csv'
        if fresh.exists():
            new=indexed(fresh);old=indexed(D/f'long_m2_{law}.csv')
            for n in (10000,50000,100000):
                a=float(old[n]['n2q']);b=float(new[n]['n2q'])
                long_checks.append(dict(law=law,n=n,submitted=a,independent=b,difference=a-b))
    result=dict(table_checks=len(checks),recomputed_fits=len(fit_checks),
                leaf_checks=len(leaf_checks),certified_endpoints=certified,
                truncation_bounds=truncation,comparisons=independent,
                long_fft_comparisons=long_checks)
    (O/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
    with (O/'independent_comparison.csv').open('w') as f:
        if independent:
            wr=csv.DictWriter(f,fieldnames=independent[0].keys());wr.writeheader();wr.writerows(independent)
    (O/'fits_recomputed.json').write_text(json.dumps(fit_checks,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':check()
