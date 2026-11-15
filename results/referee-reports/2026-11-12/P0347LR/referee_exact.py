"""Fresh exact raw and conditional-central recursions, plus a small full PMF."""
from fractions import Fraction as F
from math import comb, factorial, log
from collections import defaultdict
import csv, json

N=20
raw=[[F(0) for _ in range(7)] for n in range(N+1)]
cen=[[F(0) for _ in range(7)] for n in range(N+1)]
raw[1][0]=cen[1][0]=F(1)
h=F(0)
records=[]
for n in range(2,N+1):
    h+=F(1,n-1)
    for k in range(7):
        for i in range(1,n):
            j=n-i;q=F(n,2*i*j)/h
            for a in range(k+1):
                for b in range(k-a+1):
                    c=k-a-b
                    raw[n][k]+=q*comb(k,a)*comb(k-a,b)*raw[i][a]*raw[j][b]*n**c
    cen[n][0]=F(1)
    for k in range(2,7):
        for i in range(1,n):
            j=n-i;q=F(n,2*i*j)/h;B=n+raw[i][1]+raw[j][1]-raw[n][1]
            for a in range(k+1):
                for b in range(k-a+1):
                    c=k-a-b
                    cen[n][k]+=q*comb(k,a)*comb(k-a,b)*cen[i][a]*cen[j][b]*B**c
        centered_raw=sum(comb(k,j)*(-raw[n][1])**(k-j)*raw[n][j] for j in range(k+1))
        assert cen[n][k]==centered_raw,(n,k)
    records.append({'n':n,'mean':str(raw[n][1]),'central':[str(cen[n][k]) for k in range(2,7)]})

pmf={1:{0:F(1)}};h=F(0)
for n in range(2,13):
    h+=F(1,n-1);p=defaultdict(F)
    for i in range(1,n):
        q=F(n,2*i*(n-i))/h
        for s,u in pmf[i].items():
            for t,v in pmf[n-i].items():p[s+t+n]+=q*u*v
    pmf[n]=dict(p);assert sum(p.values())==1
    for k in range(7):assert sum(F(s)**k*v for s,v in p.items())==raw[n][k]

err=0.;zero_err=0.
for row in csv.DictReader(open('referee_finite.csv')):
    n=int(row['n'])
    if row['index']!='S' or n>N:continue
    for k in range(2,7):
        reference=float(cen[n][k])/(n*log(n))**k;value=float(row['m'+str(k)])
        if reference:err=max(err,abs(value/reference-1))
        else:zero_err=max(zero_err,abs(value))
json.dump({'exact_raw_vs_central':'equal for every n<=20, orders 2..6',
           'exact_pmf_vs_raw':'equal for every n<=12, orders 0..6',
           'max_float_relative_error':err,'max_deterministic_absolute_error':zero_err,
           'records':records},open('referee_exact.json','w'),indent=2)
print('Exact checks passed; float relative error',err)
