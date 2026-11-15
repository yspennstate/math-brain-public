"""Independent raw third/fourth-moment recursion, Decimal 45 digits."""
from common import log,memory_check
from decimal import Decimal as D,getcontext
import numpy as np,json,argparse
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=4000);args=p.parse_args()
getcontext().prec=45;N=args.n
R=[[[D(0)]*4 for _ in range(3)] for n in range(N+1)];h=D(0)
reference=np.load('moments.npz')['moments'];worst=[0.]*4
for n in range(2,N+1):
    h+=D(1)/(n-1)
    for i in range(1,n//2+1):
        j=n-i;q=D(n)/(h*i*j)
        if i==j:q/=2
        for k,t in enumerate((n,abs(n-2*i),(n-2*i)**2)):
            a,b=R[i][k],R[j][k]
            c1=a[0]+b[0]
            c2=a[1]+b[1]+2*a[0]*b[0]
            c3=a[2]+b[2]+3*(a[1]*b[0]+a[0]*b[1])
            c4=a[3]+b[3]+4*(a[2]*b[0]+a[0]*b[2])+6*a[1]*b[1]
            R[n][k][0]+=q*(c1+t)
            R[n][k][1]+=q*(c2+2*t*c1+t*t)
            R[n][k][2]+=q*(c3+3*t*c2+3*t*t*c1+t**3)
            R[n][k][3]+=q*(c4+4*t*c3+6*t*t*c2+4*t**3*c1+t**4)
    for k in range(3):
        mu,r2,r3,r4=R[n][k];v=r2-mu*mu;c3=r3-3*mu*r2+2*mu**3;c4=r4-4*mu*r3+6*mu*mu*r2-3*mu**4
        for r,value in enumerate((mu,v,c3,c4)):
            ref=float(reference[n,k,r]);err=abs(float(value)-ref)/max(1,abs(float(value)));worst[r]=max(worst[r],err)
    if n in (100,500,1000,2000,4000,N):log(f'Decimal raw-four n={n}, worst relative errors mean,var,central3,central4={worst}');memory_check()
with open('verification_raw4.json','w') as f:json.dump({'n':N,'worst_relative_errors':worst,'final_raw_moments':[[str(x) for x in row] for row in R[N]]},f,indent=2)
log('Independent Decimal-45 raw moments through order four complete; '+str(worst))
