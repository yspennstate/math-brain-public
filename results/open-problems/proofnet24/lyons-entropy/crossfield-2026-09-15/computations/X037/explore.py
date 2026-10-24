import numpy as np,itertools
E=[]
for j in range(4):
 for u in [1,1j]:
  b=np.zeros((2,2),complex);b.flat[j]=u;E.append(b)
E=np.array(E)
def datum(C):
 w=np.abs(C)**2; d=np.linalg.det(C);delta=abs(d)**2
 dv=np.array([C[1,1]*b[0,0]+C[0,0]*b[1,1]-C[1,0]*b[0,1]-C[0,1]*b[1,0] for b in E])
 dH=np.array([[2*np.real(np.conj(dv[i])*dv[j])+2*np.real(np.conj(d)*(a[0,0]*b[1,1]+a[1,1]*b[0,0]-a[0,1]*b[1,0]-a[1,0]*b[0,1])) for j,b in enumerate(E)] for i,a in enumerate(E)])
 wv=2*np.real(np.conj(C)[None,:,:]*E)
 wH=2*np.real(np.conj(E)[:,None,:,:]*E[None,:,:,:])
 I=np.zeros((8,8));F=np.zeros_like(I);lp=[0.,0.]
 for eta,r,u in itertools.product([-1,1],repeat=3):
  q=1+eta*delta+r*(w[0,0]+eta*w[1,1])+u*(w[0,1]+eta*w[1,0])
  qv=eta*2*np.real(np.conj(d)*dv)+r*(wv[:,0,0]+eta*wv[:,1,1])+u*(wv[:,0,1]+eta*wv[:,1,0])
  qH=eta*dH+r*(wH[:,:,0,0]+eta*wH[:,:,1,1])+u*(wH[:,:,0,1]+eta*wH[:,:,1,0])
  if q<=0:return
  I+=np.outer(qv,qv)/q/8
  F-=np.log(q)*qH/8
  lp[(eta+1)//2]+=np.log(q)
 return 2*(lp[0]-lp[1]),np.linalg.eigvalsh(F)[-1],np.linalg.eigvalsh(F-I)[-1]
def rot(t,p):
 return np.array([[np.cos(t),np.sin(t)*np.exp(1j*p)],[-np.sin(t)*np.exp(-1j*p),np.cos(t)]])
if __name__=='__main__':
 for s in [(0.98,.6),(.98,.9),(.9,.7),(.98,.1)]:
  for theta in [.15,.5,.8]:
   for phi in [0.,.7,1.5]:
    C=rot(theta,.3)@np.diag(s)@rot(.4,phi)
    dat=datum(C)
    if dat[0]>4 or dat[1]>1e-10:print(s,theta,phi,dat)
