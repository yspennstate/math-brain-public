"""Independent finite checks for the first two research results, with local receipts."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json
import math
import random
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
started=time.perf_counter()
def write(name, value):
    (ROOT/name).write_text(json.dumps(value,indent=2,ensure_ascii=False),encoding='utf-8')
    print(name, json.dumps(value,ensure_ascii=False))

def cube_tv(d,u):
    if u<=0:
        return 1-2.0**(-d)
    q=-math.expm1(-2*u/d)/2
    out=[]
    for k in range(d+1):
        logc=math.lgamma(d+1)-math.lgamma(k+1)-math.lgamma(d-k+1)
        p=math.exp(logc+k*math.log(q)+(d-k)*math.log1p(-q))
        pi=math.exp(logc-d*math.log(2))
        out.append(abs(p-pi))
    return math.fsum(out)/2

def parameters(d):
    N=2**d
    m=max(2,int(N*math.log(d)/4))
    D=d*(m-1)+N-1
    return N,m,D,d*(m-1)/D,N/D

spectrum_errors=[]
joint_checks=[]
for d in [2,3,4]:
    N,m,D,alpha,gamma=parameters(d)
    P=np.zeros((N*m,N*m))
    for h in range(N):
        for z in range(m):
            index=h*m+z
            for i in range(d):
                for a in range(1,m):
                    P[index, (h^(1<<i))*m+(z+a)%m]+=1/D
            for g in range(1,N):
                P[index,(h^g)*m+z]+=1/D
    assert np.max(abs(P-P.T))<1e-14
    assert np.max(abs(P.sum(axis=1)-1))<1e-13
    eig,U=np.linalg.eigh(np.eye(N*m)-P)
    predicted=[0.0]
    predicted += [d*m/D]*(m-1)
    for k in range(1,d+1):
        predicted += [(2*k*(m-1)+N)/D]*math.comb(d,k)
        predicted += [(d*m+N-2*k)/D]*((m-1)*math.comb(d,k))
    error=float(np.max(abs(eig-np.sort(predicted))))
    assert error<1e-12
    spectrum_errors.append({'d':d,'vertices':N*m,'degree':D,'max_error':error})
    for t in [0.1,1.,3.,10.]:
        dist=(U[0,:]*np.exp(-eig*t))@U.T
        full=float(np.sum(abs(dist-1/(N*m)))/2)
        projected=float(np.sum(abs(dist.reshape(N,m).sum(axis=1)-1/N))/2)
        formula=math.exp(-gamma*t)*cube_tv(d,alpha*t)
        bound=math.exp(-alpha*t)+1/m
        assert abs(projected-formula)<1e-12
        assert full-projected>=-1e-12 and full-projected<=bound+1e-12
        joint_checks.append({'d':d,'t':t,'full_tv':full,'projection_tv':projected,'formula_error':abs(projected-formula),'aux_error':full-projected,'aux_bound':bound})

profiles=[]
for d in [8,16,32,64,128,256,512]:
    N,m,D,alpha,gamma=parameters(d)
    T=d*math.log(d)/4
    gap=min((2*(m-1)+N)/D, d*m/D, (d*m+N-2*d)/D)
    def tv(t): return math.exp(-gamma*t)*cube_tv(d,alpha*t)
    mixing=[]
    for eps in [.75,.25]:
        lo,hi=0.,4*T
        for _ in range(45):
            mid=(lo+hi)/2
            if tv(mid)>eps: lo=mid
            else: hi=mid
        mixing.append((lo+hi)/2)
    profiles.append({'d':d,'T':T,'projected_t75_over_t25':mixing[0]/mixing[1],'gap_times_projected_t25':gap*mixing[1],'projected_t25_over_T':mixing[1]/T,'profile':{str(s):tv(s*T) for s in [.2,.5,.8,1.2,1.5,2.]},'full_tv_error_at_t75_bound':math.exp(-alpha*mixing[0])+1/m})
write('p0276_checks.json',{'command':'python -X utf8 check_first_batch.py','spectrum_checks':spectrum_errors,'joint_checks':joint_checks,'profiles':profiles,'asymptotic_ratio':math.log(4/3),'label':'numerical checks of a proof; no audit verdict'})

rng=random.Random(340)
min_gap=math.inf
mass_error=0.
min_probability=1.
min_eigenvalue=1.
def entropy(a,b,z):
    r=abs(z)**2
    p=[a*b-r,(1-a)*(1-b)-r,a*(1-b)+r,(1-a)*b+r]
    assert min(p)>-2e-15
    return -math.fsum(x*math.log(x) for x in p if x>0),p
for trial in range(5000):
    a,b=rng.random(),rng.random()
    if trial<4: a,b=[(0,0),(1,1),(0,1),(1,0)][trial]
    radius=math.sqrt(min(a*b,(1-a)*(1-b)))
    def z():
        angle=rng.uniform(-math.pi,math.pi)
        mag=radius*math.sqrt(rng.random())
        return complex(mag*math.cos(angle),mag*math.sin(angle))
    z0,z1=z(),z()
    t=rng.random()
    H0,p0=entropy(a,b,z0)
    H1,p1=entropy(a,b,z1)
    Hm,pm=entropy(a,b,t*z0+(1-t)*z1)
    gap=Hm-t*H0-(1-t)*H1
    min_gap=min(min_gap,gap)
    assert gap>=-2e-13
    for zz,pp in [(z0,p0),(z1,p1),(t*z0+(1-t)*z1,pm)]:
        K=np.array([[a,zz],[zz.conjugate(),b]],dtype=complex)
        eigen=np.linalg.eigvalsh(K)
        min_eigenvalue=min(min_eigenvalue,float(eigen[0]),float(1-eigen[-1]))
        assert eigen[0]>=-1e-13 and eigen[-1]<=1+1e-13
        det=float(np.linalg.det(K).real)
        assert abs(det-pp[0])<1e-13
        mass_error=max(mass_error,abs(sum(pp)-1))
        min_probability=min(min_probability,min(pp))
write('c0033_checks.json',{'command':'python -X utf8 check_first_batch.py','complex_fixed_diagonal_segments':5000,'violations':0,'min_concavity_gap':min_gap,'max_mass_error':mass_error,'min_probability':min_probability,'min_positive_contraction_margin':min_eigenvalue,'elapsed_seconds':time.perf_counter()-started,'scope':'Only two-site kernels with fixed a,b. Random checks do not prove the unrestricted conjecture.'})
