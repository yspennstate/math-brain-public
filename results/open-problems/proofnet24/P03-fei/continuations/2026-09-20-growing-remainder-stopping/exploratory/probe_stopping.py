import math, json
import mpmath as mp
mp.mp.dps=60

def h(x): return -x*mp.log(x,2) if x else mp.mpf(0)
def HH(k,m):
 N=mp.mpf(2)**k;q=1-1/N;z=q**m
 A=-2*q*q*mp.log(q,2)+2*q*k/N
 return h((2*z-1)**2)+4*m*q**(m-1)*A-4*h(z*z)-8*(z-z*z)
def rr(k,m):
 # signed mask at w activated blocks; exact minimum v2 via finite-difference coefficients
 N=2**k;ans=mp.mpf(0);rs=[]
 for b in range(1,m+1):
  r=min(k*j+((math.comb(m-j,b-j)&-math.comb(m-j,b-j)).bit_length()-1) for j in range(b+1))
  p=4*mp.mpf(math.comb(m,b))*mp.mpf(N-1)**(2*m-b)/mp.mpf(N)**(2*m)
  ans+=r*p;rs.append(r)
 return ans,rs
out=[]
for k in range(3,10):
 N=2**k;m=N-1;q=1-mp.mpf(1)/N;L=1
 while math.factorial(L)<N:L*=2
 M=m-L
 Q=2*mp.mpf(k)*L*q**(m-1)/N
 R,rs=rr(k,M)
 dH=HH(k,m)-q**L*HH(k,M)
 dD=dH/2+q**L*R
 assert all(rs[b-1]==0 for b in range(1,min(L,M+1)))
 out.append(dict(k=k,L=L,H_loss_ratio=float(dH/Q),D_loss_ratio=float(dD/Q),R_leaf=float(R),expected_queries_upper=2*L,max_queries=4*L+8*k))
print(json.dumps(out,indent=2))
