"""Audit proof identities and outputs, including each induction toll category.
Preflight: CSV objects, O(N) moment tables and mesh workspaces < 128 MB; no N^2 arrays.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import csv,json,math,re,resource
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import quad
root=Path(__file__).resolve().parent
report=(root/'REPORT.md').read_text()
assert report.splitlines()[0]=='PROVED'
links=re.findall(r'\]\(([^)]+)\)',report)
missing=[p for p in links if '://' not in p and not (root/p).exists()]
assert not missing,missing
const=json.load(open('constants.json'));A=np.array(list(map(float,const['moments'])))
raw=json.load(open('raw_audit.json'));ver=json.load(open('verification.json'))
assert max(raw['S_max_relative_errors']+raw['C_max_relative_errors'])<1e-6
assert all(max(d['max_relative_error_by_order'])<1e-10 for method in ('rational','decimal60') for d in ver[method].values())
# A law's first six moments must form a positive semidefinite Hankel matrix.
hankel=np.array([[A[i+j] for i in range(4)] for j in range(4)])
eigs=np.linalg.eigvalsh(hankel)
assert min(eigs)>0
# Integrate the polynomial defect exactly, after division by 2*x*(1-x).
for k in range(2,25):
    coeff=[]
    for j in range(k-1):
        c=Fraction(-math.comb(k,j+1)*(-1)**(j+1),2)
        coeff.append(c+(coeff[-1] if coeff else 0))
    psi=sum((v/Fraction(j+1) for j,v in enumerate(coeff)),Fraction(0))
    assert psi==sum((Fraction(1,j) for j in range(1,k)),Fraction(0))
N=8000
rows=list(csv.DictReader(open('finite_moments.csv')))
records=[];maxdiff=0.;maxcancel=0.
z=math.pi**2/6
for s in ('S','C'):
    mu=np.zeros(N+1);U=np.zeros((7,N+1));U[0,:]=1
    tolls=np.zeros((7,N+1))
    for row in rows:
        if row['index']!=s:continue
        n=int(row['n']);mu[n]=float(row['mean_per_n'])
        for k in range(2,7):U[k,n]=float(row['m'+str(k)])*math.log(n)**k;tolls[k,n]=float(row['t'+str(k)])
    for n in (1000,2000,4000,8000):
        ii=np.arange(1,n);jj=n-ii;x=ii/n;y=1-x
        L=math.log(n);h=sum(1/j for j in range(1,n));q=1/(2*h*n*x*y)
        B=(1 if s=='S' else np.abs(x-y))+x*mu[ii]+y*mu[jj]-mu[n]
        for k in range(2,7):
            vals=np.zeros(4)
            r=k-1
            v=x**r*U[r,ii]+y**r*U[r,jj]
            vals[0]=k*np.sum(q*B*(v-U[r,n]))
            original=k*np.sum(q*B*v)
            maxcancel=max(maxcancel,abs(vals[0]-original)/max(1,abs(vals[0])))
            for a in range(2,k-1):
                b=k-a
                if b>=2:vals[1]+=math.comb(k,a)*np.sum(q*x**a*y**b*U[a,ii]*U[b,jj])
            for a in range(2,k-2):
                b=k-1-a
                if b>=2:vals[2]+=math.factorial(k)/math.factorial(a)/math.factorial(b)*np.sum(q*B*x**a*y**b*U[a,ii]*U[b,jj])
            for c in range(2,k+1):
                for a in range(k-c+1):
                    b=k-c-a
                    if a==1 or b==1:continue
                    vals[3]+=math.factorial(k)/math.factorial(a)/math.factorial(b)/math.factorial(c)*np.sum(q*B**c*x**a*y**b*U[a,ii]*U[b,jj])
            vals*=h/L**k
            maxdiff=max(maxdiff,abs(sum(vals)-tolls[k,n]))
            if n==8000:
                def fun(t,category):
                    y=1-t;g=(t*math.log(t)+y*math.log1p(-t))/z
                    ans=0.
                    if category==0:ans=k*A[k-1]*g*(t**(k-1)+y**(k-1)-1)
                    if category==1:
                        ans=sum(math.comb(k,a)*A[a]*A[k-a]*t**a*y**(k-a) for a in range(2,k-1) if k-a>=2)
                    if category==2:
                        ans=sum(math.factorial(k)/math.factorial(a)/math.factorial(k-1-a)*A[a]*A[k-1-a]*t**a*y**(k-1-a)*g for a in range(2,k-2) if k-1-a>=2)
                    if category==3:
                        for c in range(2,k+1):
                            for a in range(k-c+1):
                                b=k-c-a
                                if a==1 or b==1:continue
                                ans+=math.factorial(k)/math.factorial(a)/math.factorial(b)/math.factorial(c)*A[a]*A[b]*t**a*y**b*g**c
                    return ans/(2*t*y)
                limits=np.array([2*quad(lambda t:fun(t,j),0,.5,epsabs=1e-12,epsrel=1e-12)[0] for j in range(4)])
                assert abs(sum(limits)-sum(1/j for j in range(1,k))*A[k])<1e-10
                records.append(dict(index=s,n=n,k=k,categories=['c1_parent_canceled','c0_cross','c1_cross','c_ge_2'],finite=vals.tolist(),limit=limits.tolist()))
assert maxdiff<1e-9
assert maxcancel<1e-8
out=dict(exact_polynomial_psi_orders_checked=[2,24],report_links_checked=len(links),limit_hankel_eigenvalues=eigs.tolist(),max_toll_decomposition_error=maxdiff,max_relative_parent_cancellation_error=maxcancel,induction_categories=records,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
json.dump(out,open('audit.json','w'),indent=2)
print(json.dumps({k:v for k,v in out.items() if k!='induction_categories'},indent=2))
