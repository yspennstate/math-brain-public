"""Independent high-precision raw moments and double central moments to n=200."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import csv,json,math
import mpmath as mp
mp.mp.dps=60
N=200
R=[[mp.mpf(0) for k in range(7)] for n in range(N+1)]
C=[[0. for k in range(7)] for n in range(N+1)]
mu=[0.]*(N+1)
R[1][0]=mp.mpf(1);C[1][0]=1.
h=mp.mpf(0);worst=0.;worst_at=None
for n in range(2,N+1):
    h+=mp.mpf(1)/(n-1);R[n][0]=mp.mpf(1);C[n][0]=1.
    # All raw orders use the conditional binomial sum, followed by deterministic toll n.
    for i in range(1,n):
        j=n-i;q=mp.mpf(n)/(2*h*i*j)
        daughter=[sum(math.comb(d,a)*R[i][a]*R[j][d-a] for a in range(d+1)) for d in range(7)]
        for k in range(1,7):
            R[n][k]+=q*sum(math.comb(k,d)*n**(k-d)*daughter[d] for d in range(k+1))
    # A second algebra in double precision, using directly centered daughters.
    hf=float(h)
    mu[n]=n+sum(n/(2*hf*i*(n-i))*(mu[i]+mu[n-i]) for i in range(1,n))
    for i in range(1,n):
        j=n-i;q=n/(2*hf*i*j);B=n+mu[i]+mu[j]-mu[n]
        daughter=[sum(math.comb(d,a)*C[i][a]*C[j][d-a] for a in range(d+1)) for d in range(7)]
        for k in range(2,7):
            C[n][k]+=q*sum(math.comb(k,d)*B**(k-d)*daughter[d] for d in range(k+1))
    for k in range(2,7):
        ref=sum(math.comb(k,d)*(-R[n][1])**(k-d)*R[n][d] for d in range(k+1))
        if abs(ref)>mp.mpf('1e-35'):
            err=abs(C[n][k]/float(ref)-1)
            if err>worst:worst=err;worst_at=[n,k]
    if n%50==0:print('mp raw',n,'worst',worst,flush=True)
rows=[]
for row in csv.DictReader(open('referee_finite.csv')):
    n=int(row['n'])
    if row['index']!='S' or n>N:continue
    for k in range(2,7):
        ref=sum(math.comb(k,d)*(-R[n][1])**(k-d)*R[n][d] for d in range(k+1))
        normalized=ref/(n*mp.log(n))**k
        rows.append({'n':n,'k':k,'mp_normalized':mp.nstr(normalized,35),'cpp_normalized':row['m'+str(k)]})
cpp_worst=max(abs(float(r['cpp_normalized'])/float(r['mp_normalized'])-1) for r in rows if abs(mp.mpf(r['mp_normalized']))>mp.mpf('1e-30'))
json.dump({'dps':60,'N':N,'double_vs_mp_max_relative_error':worst,'worst_at':worst_at,
           'cpp_vs_mp_max_relative_error':cpp_worst,'rows':rows},open('referee_mp.json','w'),indent=2)
