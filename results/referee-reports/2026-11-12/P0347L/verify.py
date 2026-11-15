"""Independent rational and 60-digit raw moments; finite-size fits and proof checks.
Memory preflight: CSV objects, decoded tables and verification arrays < 128 MB;
no object of size O(N^2) is allocated. Numerical libraries use one thread.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import csv,json,math,resource,sys,time
from decimal import Decimal,localcontext
from fractions import Fraction
import numpy as np
from numpy.polynomial import Polynomial
N=8000
planned=128_000_000
print('Preflight total numerical storage budget:',planned,'bytes',flush=True)
assert planned<4_000_000_000
rows=list(csv.DictReader(open('finite_moments.csv')))
data={s:{int(r['n']):{k:float(v) for k,v in r.items() if k not in ('index','n')} for r in rows if r['index']==s} for s in ('S','C')}
constants=json.load(open('constants.json'))
a=list(map(float,constants['moments']))
# This recurrence uses uncentered integer-scale moments; centers only at the end.
def raw_recurrence(N,kind):
    Q=Fraction if kind=='rational' else Decimal
    fact=math.factorial
    out={}
    for s in ('S','C'):
        r=[[Q(0)]*7 for _ in range(N+1)]
        r[1][0]=Q(1);h=Q(0);worst=[0.]*7
        for n in range(2,N+1):
            h+=Q(1)/Q(n-1);acc=[Q(0)]*7
            for i in range(1,n//2+1):
                j=n-i;q=Q(n)/Q(2)/h/Q(i)/Q(j)*Q(1 if i==j else 2)
                toll=Q(n if s=='S' else abs(n-2*i))
                tp=[Q(1)]
                for k in range(1,7):tp.append(tp[-1]*toll)
                conv=[sum((Q(math.comb(k,b))*r[i][b]*r[j][k-b] for b in range(k+1)),Q(0)) for k in range(7)]
                for k in range(1,7):
                    acc[k]+=q*sum((Q(math.comb(k,b))*tp[k-b]*conv[b] for b in range(k+1)),Q(0))
            r[n]=acc;r[n][0]=Q(1)
            mu=r[n][1]
            worst[1]=max(worst[1],abs(float(mu/Q(n))-data[s][n]['mean_per_n'])/max(1,abs(float(mu/Q(n)))))
            for k in range(2,7):
                centered=sum((Q(math.comb(k,b))*(Q(1) if k==b else (-mu)**(k-b))*r[n][b] for b in range(k+1)),Q(0))
                scaled=float(centered/Q(n)**k)/math.log(n)**k
                e=abs(scaled-data[s][n]['m'+str(k)])/max(abs(scaled),1e-20)
                # Deterministic n=2,3 have exact zero central moments.
                if abs(scaled)>1e-15:worst[k]=max(worst[k],e)
        out[s]=dict(max_relative_error_by_order=worst,n=N,final_mean=str(r[N][1]))
    return out
start=time.time()
rational=raw_recurrence(20,'rational')
print('Rational check finished',time.time()-start,flush=True)
with localcontext() as ctx:
    ctx.prec=60
    decimal=raw_recurrence(200,'decimal')
print('Decimal check finished',time.time()-start,flush=True)
fits=[]
for s in ('S','C'):
    for lo in (256,1000,2000):
        ns=np.unique(np.geomspace(lo,8000,160).astype(int))
        t=1/np.log(ns)
        for k in range(2,7):
            vals=np.array([data[s][int(n)]['m'+str(k)] for n in ns])
            for degree in (2,3,4):
                p=Polynomial.fit(t,vals,degree)
                intercept=float(p(0));residual=float(np.max(np.abs(p(t)-vals)))
                fits.append(dict(index=s,k=k,n_min=lo,n_max=8000,degree=degree,intercept=intercept,limit=a[k],relative_intercept_error=(intercept-a[k])/a[k],max_fit_residual=residual))
with open('fits.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=list(fits[0]));w.writeheader();w.writerows(fits)
# Exact defect expression at n=8000: check all p=r=k in the transfer lemma.
x=np.arange(1,N,dtype=float)/N;y=1-x;L=math.log(N)
H=-x*np.log(x)-y*np.log(y)
h=sum(1/j for j in range(1,N))
q=1/(2*h*N*x*y)
defects=[]
for k in range(2,7):
    value=float(h*np.sum(q*(1-x**k*(1+np.log(x)/L)**k-y**k*(1+np.log(y)/L)**k)))
    defects.append(dict(k=k,value=value,limit=sum(1/j for j in range(1,k))))
b=0.5772156649015329/(math.pi**2/6)+1.2020569031595943/(math.pi**2/6)**2
proof_checks={
 'entropy_first_integral_mesh':float(h*np.sum(q*H)/(math.pi**2/6)),
 'max_split_centering_error':max(abs(d['mean_B']) for s in data.values() for d in s.values()),
 'max_uniform_B_remainder':{s:max(d['max_B_error'] for d in data[s].values()) for s in data},
 'S_mean_remainder_range':[min(d['mean_per_n']-math.log(n)**2/(2*(math.pi**2/6))-b*math.log(n) for n,d in data['S'].items()),max(d['mean_per_n']-math.log(n)**2/(2*(math.pi**2/6))-b*math.log(n) for n,d in data['S'].items())],
 'transfer_defects':defects,
 'planned_bytes':planned,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
res=dict(rational=rational,decimal60=decimal,proof_checks=proof_checks)
json.dump(res,open('verification.json','w'),indent=2)
for s in ('S','C'):
    for n in (1000,2000,4000,8000):
        print(s,n,*[f'{data[s][n]["m"+str(k)]:.10f}' for k in range(2,7)])
print('Fits, window [1000,8000]:')
for f in fits:
    if f['n_min']==1000:print(f['index'],f['k'],f['degree'],f'{f["intercept"]:.10f}',f'rel err {f["relative_intercept_error"]:.4g}')
print(json.dumps(res,indent=2))

assert len(data['S'])==7999 and len(data['C'])==7999
assert all(max(v['max_relative_error_by_order'])<1e-10 for check in (rational,decimal) for v in check.values())
assert proof_checks['max_split_centering_error']<1e-10
assert all(math.isfinite(d['m'+str(k)]) for table in data.values() for d in table.values() for k in range(2,7))
