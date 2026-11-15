"""High-precision audit of the load-bearing large structured examples."""
import json,math
from pathlib import Path
import mpmath as mp
mp.mp.dps=100

def majority(n):
    m=(n-1)//2;c=mp.mpf(math.comb(2*m,m))/2**(2*m);mu=[mp.mpf(0)]*(n+1)
    for r in range(m+1):mu[2*r+1]=(c*math.comb(m,r)/math.comb(2*m,2*r))**2
    W=[math.comb(n,k)*mu[k] for k in range(n+1)];I=sum(k*W[k] for k in range(n+1));F=[];ph=[]
    for u in [mp.mpf(0),mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4,mp.mpf(7)/8,mp.mpf(1)]:
        Fu=[sum(math.comb(n-k,j-k)*mu[j]*u**(j-k) for j in range(k,n+1)) for k in range(n+1)]
        ph.append(-sum(W[k]*mp.log(Fu[k],2) for k in range(n+1) if W[k]));F.append(Fu)
    mean=mp.mpf(0);atom=mp.mpf(0);quant=mp.mpf(0)
    for k in range(n+1):
        if not W[k]:continue
        q=[mp.mpf(math.comb(n-k,j-k))*mu[j]/F[-1][k] for j in range(k,n+1)];M=sum(j*q[j] for j in range(len(q)));w=q[0];mean+=W[k]*M
        atom-=W[k]*mp.log(w+(1-w)*2**(-M/(1-w)) if w<1 else 1,2)
        cum=mp.mpf(0);choices=[]
        for j,p in enumerate(q):
            cum+=p
            if cum:choices.append(j-mp.log(cum,2))
        quant+=W[k]*min(choices)
    Z=[sum(math.comb(j,k)*mu[k]/F[-1][k] for k in range(j+1) if mu[k]) for j in range(n+1)]
    KL=sum(W[j]*Z[j]*mp.log(Z[j],2) for j in range(n+1) if W[j] and Z[j]);C=ph[0]-ph[-1]+KL
    return dict(I=I,phi_over_I=[x/I for x in ph],cost_over_I=(ph[2]-ph[-1])/I,mean_Jensen_over_I=mean/I,atom_bound_over_I=atom/I,quantile_bound_over_I=quant/I,conditional_entropy_over_I=C/I,parseval_error=abs(sum(W)-1),kraft_error=abs(sum(w*z for w,z in zip(W,Z))-1))
def andf(n):
    a=mp.mpf(2)**(1-n);I=n*a;M=(1-a)**2;ph=[]
    for u in [mp.mpf(0),mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4,mp.mpf(7)/8,mp.mpf(1)]:
        empty=-M*mp.log1p(-2*a+a*a*(1+u)**n)/mp.log(2)
        ph.append(empty+a*a*((mp.mpf(2)**n-1)*2*(n-1)-(n*mp.mpf(2)**(n-1)-n)*mp.log(1+u,2)))
    return dict(I=I,phi_over_I=[x/I for x in ph],cost_over_I=(ph[2]-ph[-1])/I)

def main():
    saved=json.load(open('families.json'));out=[]
    for family,n,fn in [('majority',513,majority),('AND',256,andf)]:
        r=next(r for r in saved if r['family']==family and r['n']==n);exact=fn(n);maxerr=0
        for k,v in exact.items():
            if k in r and r[k] is not None:
                dif=max(abs(float(a)-b) for a,b in zip(v,r[k])) if isinstance(v,list) else abs(float(v)-r[k]);maxerr=max(maxerr,dif)
        assert maxerr<1e-11,(family,maxerr)
        out.append(dict(family=family,n=n,binary64_max_error=maxerr,high_precision={k:[mp.nstr(x,90) for x in v] if isinstance(v,list) else mp.nstr(v,90) for k,v in exact.items()}))
        print(family,n,maxerr,flush=True)
    Path('large_audit.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()
