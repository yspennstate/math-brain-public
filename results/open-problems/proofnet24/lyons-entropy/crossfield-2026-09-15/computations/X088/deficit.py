import numpy as np

def jm(t,x,y):
 r=x*x;s=y*y;beta=6*t*(1-t)-1
 f=6*t*t*(1-t)**2+beta*(r+s)+6*r*s;d=2*(r+s);z=d/(2*f)
 jf=(np.log1p(z)+2*np.log1p(-z/2))/3;jd=(np.log1p(z)-np.log1p(-z/2))/6;jzz=1/(2*(1+z)*(1-z/2))
 fg=2*np.array([x*(beta+6*s),y*(beta+6*r)]);dg=4*np.array([x,y])
 fh=np.array([[2*(beta+6*s),24*x*y],[24*x*y,2*(beta+6*r)]])
 q=dg-2*z*fg
 return np.outer(q,q)*jzz/(4*f)+jf*fh+jd*4*np.eye(2)
rng=np.random.default_rng(81);w=(1,None)
for k in range(50000):
 t=rng.uniform(.001,.5);x,y=rng.uniform(-t,t,2)
 m=np.linalg.eigvalsh(jm(t,x,y))[0]
 if m<w[0]:w=(m,[t,x,y])
print(w)
for t in [.1,.3,.49,.5]:
 print(t,np.linalg.eigvalsh(jm(t,t*(1-1e-7),t*(1-1e-7))))
