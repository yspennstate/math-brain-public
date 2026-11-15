"""Independent truth-table audit of the linear-DNF proof's local bounds."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import math,itertools,json,time,resource,sys
import numpy as np
import mpmath as mp
from window_search import truth_dnf
sys.path.insert(0,os.path.abspath('inputs'))
from experiment import wht,masses,phi
mp.mp.dps=80

def certificate(L,D,d,k):
    a=mp.mpf(2)**(-L);theta=1-L*(D-1)*a-(d-1)*a/2
    den=1-k*(D-1)*a/2
    if theta<=0 or den<=0 or d*a>mp.mpf(1)/4:return None
    gamma=a*sum(math.comb(L,j) for j in range(k));eps=min(1,d*gamma)
    alpha=mp.mpf(math.comb(L,k))*mp.power(2,math.comb(k,2)-2*k)*((D-1)*a)**k/den
    kap=alpha/(a*theta)
    err=2*eps+8/mp.log(2)*mp.sqrt(kap)+eps*mp.log(mp.e*(3+8/(eps*d*a*theta)),2)
    err+=d*a*mp.log(mp.e*(1+(d*a)**-2),2)
    return dict(L=L,D=D,d=d,k=k,error=float(err),coefficient=float(2+err),eps=float(eps),kappa=float(kap),theta=float(theta))

def examples():
    out=[]
    for L in [15,31,63,127,255]:
        Ds=sorted(set([1,L,round(math.sqrt(1.4*2**L/L)),int(2**(3*L//4)),2**L//(L**2)]))
        for D in Ds:
            candidates=[certificate(L,D,D,k) for k in range(1,min(L,40)+1)]
            candidates=[z for z in candidates if z]
            if candidates:out.append(min(candidates,key=lambda z:z['error']))
            else:out.append(dict(L=L,D=D,status='certificate assumptions not met'))
    return out

def derivative(v,m,J):
    # Direct coordinate differences, separately from Fourier evaluation.
    a=np.array(v,copy=True);remaining=list(range(m))
    for j in sorted(J,reverse=True):
        pos=remaining.index(j);idx=np.arange(len(a));lo=idx[((idx>>pos)&1)==0]
        a=(a[lo]-a[lo+(1<<pos)])/2;remaining.pop(pos)
    return float(np.mean(a*a))

def audit_case(name,n,terms):
    w=len(terms[0]);L=w-1;a=2.**-L
    assert all(len(set(S)&set(T))<=1 for S,T in itertools.combinations(terms,2))
    degrees=[sum(i in T for T in terms) for i in range(n)];D=max(degrees)
    actual=wht(truth_dnf(n,terms))**2
    ratios=[];derivatives=[];errF=0.
    for i in range(n):
        incident=[T for T in terms if i in T];d=len(incident)
        if not d:continue
        orig=[j for j in range(n) if j!=i];inv={j:k for k,j in enumerate(orig)}
        back=[[inv[j] for j in T] for T in terms if i not in T]
        N=(truth_dnf(n-1,back)+1)/2
        A=float(N.mean());F=wht(N);sp=F**2;ids=np.arange(len(sp));m=n-1
        p,q=masses(actual,i);delta=float(q.sum());theta=1-L*(D-1)*a-(d-1)*a/2
        low=d*a*theta;high=d*a
        assert delta/A+1e-12>=low and delta/A<=high+1e-12
        ratios.append(dict(i=i,d=d,delta=delta,A=A,delta_over_A=delta/A,lower=low,upper=high,E_ratio=float(phi(p,q).sum())/delta))
        for T in incident:
            mates=[inv[j] for j in T if j!=i]
            for k in range(1,min(3,L)+1):
                den=1-k*(D-1)*a/2
                if den<=0:continue
                bound=2.**(math.comb(k,2)-2*k)*((D-1)*a)**k/den
                for J in itertools.combinations(mates,k):
                    mask=sum(1<<j for j in J);val=float(sp[(ids&mask)==mask].sum())
                    direct=derivative(N,m,J);errF=max(errF,abs(val-direct))
                    assert abs(val-direct)<1e-12
                    assert val/A<=bound+1e-12,(name,i,J,val/A,bound)
                    derivatives.append(dict(i=i,k=k,observed=val/A,bound=bound,ratio=(val/A)/bound if bound else 0))
    return dict(name=name,n=n,w=w,D=D,coordinates=ratios,derivative_checks=len(derivatives),max_derivative_ratio=max(z['ratio'] for z in derivatives),direct_spectral_residual=errF)

def main():
    start=time.time();rows=[]
    fano=sorted(set(tuple(sorted([a-1,b-1,(a^b)-1])) for a in range(1,8) for b in range(a+1,8)))
    rows.append(audit_case('Fano',7,fano))
    rows.append(audit_case('cyclic_linear_13',13,[[j,(j+1)%13,(j+4)%13] for j in range(13)]))
    rng=np.random.default_rng(2103)
    for n,w in [(12,3),(16,4),(18,5)]:
        candidates=list(itertools.combinations(range(n),w));rng.shuffle(candidates);terms=[]
        for T in candidates:
            if all(len(set(S)&set(T))<=1 for S in terms):terms.append(list(T))
            if len(terms)>=n:break
        rows.append(audit_case('random_linear_'+str(n),n,terms))
    # Broken control: one background term contains all three chosen mates.
    N=(truth_dnf(4,[[0,1,2,3]])+1)/2
    control_actual=derivative(N,4,[0,1,2])/float(N.mean())
    control_bound=2.**(3-6)*(2.**-3)**3/(1-3*2.**-3/2)
    assert control_actual>control_bound
    out=dict(rows=rows,nonlinear_control=dict(actual=control_actual,bound_if_linearity_omitted=control_bound,detected=control_actual>control_bound),certificates=examples(),seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('linear_audit.json','w'),indent=2);print(json.dumps(out,indent=2))
if __name__=='__main__':main()
