import numpy as np
rng=np.random.default_rng(714)
mn=1e30; worst=None
mnfull=1e30
for it in range(100000):
 a=1/(1+np.exp(rng.uniform(-18,18)))
 c=a+(1-a)/(1+np.exp(rng.uniform(-18,18)))
 if c-a<1e-13:continue
 v=2*a*(1-a)+c*(1-c)
 p0=(1-a)**2*(1-c)
 p3=a*a*c
 p1=(1-a)*(2*a*(1-c)+(1-a)*c)/3
 p2=a*(a*(1-c)+2*(1-a)*c)/3
 l0=np.log(p1*p1/(p0*p2));l1=np.log(p2*p2/(p1*p3))
 m=(1-c)*l0+c*l1;t=(1-a)*l0+a*l1
 C=np.array([[v,-p0*(2*a+c)],[-p0*(2*a+c),p0*(1-p0)]])
 J=np.array([[2,1],[-2*p0/(1-a),-p0/(1-c)]])
 F=J.T@np.linalg.solve(C,J)
 G=F-np.array([[2*m,2*t],[2*t,0]])
 # scale to avoid underflow
 e=np.linalg.eigvalsh(G)[0]
 if e<mn:
  mn=e;worst=(a,c,l0,l1,G)
 if e<-1e-5:break
print(mn,worst)
