"""Independent raw first/second moments, Decimal 45 digits; rational small n."""
from common import log
import argparse,json
from decimal import Decimal, getcontext
from fractions import Fraction
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=2000);a=p.parse_args()
getcontext().prec=45
def run(N,T,tag):
    zero=T(0);one=T(1);h=zero
    means=[[zero]*3 for _ in range(N+1)];raw2=[[zero]*3 for _ in range(N+1)]
    data=np.load('moments.npz')['moments'];err_mu=0.;err_v=0.
    for n in range(2,N+1):
        h+=one/(n-1)
        for i in range(1,n//2+1):
            j=n-i;q=T(n)/(h*i*j)
            if i==j:q/=2
            toll=(n,abs(n-2*i),(n-2*i)**2)
            for k in range(3):
                u,v=means[i][k],means[j][k];t=toll[k]
                means[n][k]+=q*(u+v+t)
                raw2[n][k]+=q*(raw2[i][k]+raw2[j][k]+2*u*v+2*t*(u+v)+t*t)
        for k in range(3):
            mu=means[n][k];var=raw2[n][k]-mu*mu
            err_mu=max(err_mu,abs(float(mu)-float(data[n,k,0]))/max(1,abs(float(mu))))
            err_v=max(err_v,abs(float(var)-float(data[n,k,1]))/max(1,abs(float(var))))
        if n in (30,500,1000,2000,N):log(tag+' n='+str(n)+' max relative disagreements (mean,var)='+str((err_mu,err_v)))
    out={'n':N,'max_relative_mean':err_mu,'max_relative_variance':err_v,'means':list(map(str,means[N])),'variances':[str(raw2[N][k]-means[N][k]**2) for k in range(3)]}
    with open('verification_'+tag+'.json','w') as f:json.dump(out,f,indent=2)
    log(tag+' check complete: '+json.dumps(out))
run(30,Fraction,'rational')
run(a.n,Decimal,'decimal45')
