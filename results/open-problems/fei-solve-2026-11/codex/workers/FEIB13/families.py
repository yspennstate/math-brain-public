"""Size-independent tribes formulas and exact-integer symmetric-function calculations."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import math,json
import numpy as np
from pathlib import Path
from experiment import KS,TS,TH
LN2=math.log(2)
def ladd(a,b):return float(np.logaddexp(a,b))
def ldiff(a,b):
    if b>=a:return -math.inf
    return a+math.log(-math.expm1(b-a))
def logpowerdiff(loga,logb,m):return m*loga+math.log(-math.expm1(m*(logb-loga))) if loga>logb else -math.inf

def tribes_moments(w,m):
    q=2.**-w;lb=math.log1p(-q);b=1-q
    B=math.exp(m*lb);var=4*B*(-math.expm1(m*lb));I=2*m*w*q*math.exp((m-1)*lb)
    out={}
    for theta in (1.,.5,.25):
        for c in (2.,4.,8.,2**theta/(2**(1-theta)-1) if theta<1 else 16.):
            d=math.expm1(w*math.log1p(2**theta/c))
            loga=math.log1p(math.expm1((2-theta)*lb)+q**(2-theta)*d)
            logW=(1-theta)*math.log(4)+logpowerdiff(loga,(2-theta)*lb,m)
            out[f'W_c{c:.12g}_th{theta:g}']=logW/LN2
            out[f'W_K_c{c:.12g}_th{theta:g}']=var*(logW-math.log(var))/(I*LN2)
    for t in TS:
        tail=math.exp(w*math.log1p(-t/2));ld=math.log1p(q*(tail-2))
        tau0=1-4*B+4*math.exp(m*ld)
        for theta in TH:
            loga0=ld-theta*lb
            hit=q**(2-theta)*math.exp(w*math.log(2-t))*math.expm1(w*math.log1p(t*2**-theta/(2-t)))
            loga=math.log1p(math.expm1(loga0)+hit)
            logmom=ladd(math.log(max(tau0,1e-300)),math.log(4)+logpowerdiff(loga,loga0,m))
            out[f'taumom_t{t:g}_th{theta:g}']=logmom/LN2
    for theta in TH:
        a0=(1-theta)*lb
        hit=q**(1-theta)*math.expm1(w*math.log1p(.5/2**(1+theta)))
        la=math.log1p(math.expm1(a0)+hit)
        out[f'raw_th{theta:g}']=ladd(0.,math.log(4)+logpowerdiff(la,a0,m))/LN2
    return out

def tribes(w,m,quadrature=64):
    q=2.**-w;lb=math.log1p(-q);b=1-q;B=math.exp(m*lb)
    var=4*B*(-math.expm1(m*lb));I=2*m*w*q*math.exp((m-1)*lb)
    Er=4*m*q*B;h=-lb/LN2
    P=w*Er-I+h*(m*var-Er)
    A=P+2*(I-var)
    mu0=(2*B-1)**2;h0=-mu0*math.log2(mu0) if mu0>0 else 0.
    row={'name':f'tribes_w{w}_m{m}','w':w,'m':m,'n':w*m,'I':I,'Var':var,'P':P,'A':A,'H':2*P+2*(I-var)+h0,'empty_entropy':h0}
    for t in TS:
        tail=math.exp(w*math.log1p(-t/2));ld=math.log1p(q*(tail-2))
        r=4*m*q*(1-tail)*math.exp((m-1)*lb)
        v=4*(B-math.exp(m*ld))
        row[f'T{t:g}']=w*r-t*I+h*(m*v-r)
    for K in KS:row[f'Sp{K}']=0.
    for rho in (.25,.5,.75):row[f'ref_tau{rho:g}']=0.
    row['ref_mixture3']=row['ref_mixture_uniform']=0.
    xg,wg=np.polynomial.legendre.leggauss(quadrature);rho=(xg+1)/2;wg=wg/2
    cond=np.array([0.]+[math.comb(w,s)/(2.**w-1) for s in range(1,w+1)])
    prob0=math.exp(m*lb);prob=prob0;dist=np.array([1.]);mass=0.
    for r in range(1,min(m,64)+1):
        prob*=((m-r+1)/r)*q/b;dist=np.convolve(dist,cond)
        weight=4*B*prob;mass+=weight
        s=np.arange(len(dist));lp=r*w-s-(m-r)*lb/LN2
        for K in KS:row[f'Sp{K}']+=float(weight*np.sum(dist*lp*(lp>K*s+1e-12)))
        lts=[]
        for rr in (.25,.5,.75):
            ld=math.log1p(q*(math.exp(w*math.log1p(-rr/2))-2))
            lta=math.log(4)+s*math.log(rr)-2*r*w*LN2+(r*w-s)*math.log(2-rr)+(m-r)*ld
            row[f'ref_tau{rr:g}']-=float(weight*np.sum(dist*lta)/LN2);lts.append(lta)
        lm=np.logaddexp.reduce(np.array(lts),axis=0)-math.log(3)
        row['ref_mixture3']-=float(weight*np.sum(dist*lm)/LN2)
        ld=np.log1p(q*(np.exp(w*np.log1p(-rho/2))-2))
        lt=math.log(4)+s[:,None]*np.log(rho)-2*r*w*LN2+(r*w-s[:,None])*np.log(2-rho)+(m-r)*ld
        lm=np.logaddexp.reduce(lt+np.log(wg),axis=1)
        row['ref_mixture_uniform']-=float(weight*np.sum(dist*lm)/LN2)
    row['omitted_spectral_mass']=max(0.,var-mass)
    tau0s=[]
    for rr in (.25,.5,.75):
        ld=math.log1p(q*(math.exp(w*math.log1p(-rr/2))-2))
        p0=1-4*B+4*math.exp(m*ld);tau0s.append(p0)
        row[f'ref_tau{rr:g}']-=mu0*math.log2(p0)
    row['ref_mixture3']-=mu0*math.log2(sum(tau0s)/3)
    lds=np.log1p(q*(np.exp(w*np.log1p(-rho/2))-2))
    p0mix=1-4*B+4*float(sum(wg*np.exp(m*lds)))
    row['ref_mixture_uniform']-=mu0*math.log2(p0mix)
    inf=2*q*math.exp((m-1)*lb)
    row['ref_product']=w*m*(math.log1p(inf)/LN2-inf*math.log(inf)/LN2)
    # Z=E_mu 2^|U|; nonempty contribution 4(a^m-b^(2m)).
    la=math.log1p(-2*q+q*q*3.**w)
    logZ=ladd(math.log(max((1-2*B)**2,1e-300)),math.log(4)+logpowerdiff(la,2*lb,m))
    row['markov_logZ']=logZ/LN2;row['ref_markov_normalized']=A+logZ/LN2
    row.update(tribes_moments(w,m))
    # Count with up_M(R)=sum_{U>=R, |U|<=M} mu(U); M=ceil(a I).
    # Round a single upward floating-point ulp back at an integer cutoff.
    maxM=int(math.ceil(np.nextafter(4*I,-np.inf)));cutoffs=[int(math.ceil(np.nextafter(a*I,-np.inf))) for a in (2,4)]
    for theta in TH:
        Bfac=math.exp(theta*(lb-math.log(q)))
        sizes=np.arange(w+1)
        hpoly=cond*(1+Bfac*np.expm1(sizes*math.log1p(.5*2**-theta)))
        v=np.array([1.]);vbase=np.array([1.]);tot=np.zeros(maxM+1);base=np.zeros(maxM+1)
        for r in range(1,min(m,maxM)+1):
            factor=((m-r+1)/r)*q/b
            v=np.convolve(v,hpoly)[:maxM+1]*factor
            vbase=np.convolve(vbase,cond)[:maxM+1]*factor
            tot[:len(v)]+=v;base[:len(vbase)]+=vbase
        for a,M in zip((2,4),cutoffs):
            probcut=(1-2*B)**2+4*math.exp(2*m*lb)*base[:M+1].sum()
            raw=probcut+4*math.exp((2-theta)*m*lb)*(tot[:M+1]-base[:M+1]).sum()
            row[f'raw_M{a}I_th{theta:g}']=math.log2(raw)
    return row

def symmetric(n,kind):
    if kind=='AND':
        from highprecision import and_row
        return and_row(n)
    vals=[-1 if (k>n//2 if kind=='majority' else k==n) else 1 for k in range(n+1)]
    mu=[];up=[];p=[];counts=np.array([float(math.comb(n,s)) for s in range(n+1)])
    for s in range(n+1):
        nums=[sum((-1)**j*math.comb(s,j)*vals[k+j] for j in range(s+1)) for k in range(n-s+1)]
        hatsum=sum(math.comb(n-s,k)*v for k,v in enumerate(nums))
        mu.append((hatsum/2.**n)**2)
        up.append(sum(math.comb(n-s,k)*v*v for k,v in enumerate(nums))/2.**(n+s))
        p.append(sum(math.comb(n-s,k) for k,v in enumerate(nums) if v)/2.**(n-s))
    mu=np.array(mu);up=np.array(up);p=np.array(p);s=np.arange(n+1);mass=counts*mu
    lp=-np.log2(np.where(p>0,p,1));lu=-np.log2(np.where(up>0,up,1))
    I=float(sum(mass*s));var=float(sum(mass[1:]));row={'name':f'{kind}_{n}','n':n,'I':I,'Var':var,'P':float(sum(mass*lp)),'A':float(sum(mass*lu)),'H':float(sum(mass*-np.log2(np.where(mu>0,mu,1))))}
    for K in KS:row[f'Sp{K}']=float(sum(mass*lp*(lp>K*s+1e-12)))
    def noise(r):
        return np.array([r**j*sum(math.comb(n-j,k-j)*mu[k]*(1-r)**(k-j) for k in range(j,n+1)) for j in range(n+1)])
    for t in TS:
        tau=noise(t);row[f'T{t:g}']=float(sum(counts*tau*lp))
        for theta in TH:row[f'taumom_t{t:g}_th{theta:g}']=float(np.log2(sum(counts*tau*np.where(p>0,p,1)**-theta)))
    for theta in TH:
        weight=counts*.5**s*np.where(p>0,p,1)**-theta
        row[f'raw_th{theta:g}']=float(np.log2(sum(weight*up)))
        for a in (2,4):
            M=int(math.ceil(a*I));trunc=np.array([sum(math.comb(n-j,k-j)*mu[k] for k in range(j,min(n,M)+1)) for j in range(n+1)])
            row[f'raw_M{a}I_th{theta:g}']=float(np.log2(sum(weight*trunc)))
    for theta in (1.,.5,.25):
        for c in (2.,4.,8.):
            W=float(sum(mass[1:]*c**(-s[1:])*np.where(up[1:]>0,up[1:],1)**-theta))
            row[f'W_c{c:g}_th{theta:g}']=math.log2(W)
            row[f'W_K_c{c:g}_th{theta:g}']=var*math.log2(W/var)/I
    refs={f'tau{r:g}':noise(r) for r in (.25,.5,.75)};refs['mixture3']=sum(refs.values())/3
    refs['mixture_uniform']=np.array([sum(math.comb(n-j,k-j)*mu[k]/((k+1)*math.comb(k,j)) for k in range(j,n+1)) for j in range(n+1)])
    Z=sum(counts*up);refs['markov_normalized']=up/Z
    for name,pi in refs.items():row['ref_'+name]=float(sum(mass*-np.log2(np.where(pi>0,pi,1))))
    inf=up[1];row['ref_product']=n*(math.log2(1+inf)-inf*math.log2(inf))
    row['markov_logZ']=math.log2(Z)
    row['parseval_error']=abs(sum(mass)-1)
    return row

def main():
    result=[]
    for w in (1,2,3,4,6,8,12,16,24,32,48,64):
        for multiplier in (.25,math.log(2),4.):
            m=max(1,round(multiplier*2**w));row=tribes(w,m);result.append(row)
            Path('families.json').write_text(json.dumps(result,indent=2));print(row['name'],'P/I',row['P']/row['I'],'W1c4_K',row['W_K_c4_th1'],flush=True)
    for kind,ns in [('AND',(3,5,9,17,33,65,127)),('majority',(3,5,9,17,33,65,127,255))]:
        for n in ns:
            row=symmetric(n,kind);result.append(row);Path('families.json').write_text(json.dumps(result,indent=2));print(row['name'],'P/I',row['P']/row['I'],flush=True)
if __name__=='__main__':main()
