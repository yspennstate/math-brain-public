import numpy as np
from gen import bdrift, noise_basis
def dr(L,g2,m):
    P=np.eye(m)-1.0/m; V=L@L.T
    b=bdrift(V,g2); E=noise_basis(V+1e-30*np.eye(m),g2,att=True,lin=False)
    l=np.trace(V)-V[0,0]; a=V[0,0]
    q=lambda f: sum(f(Ej)**2 for Ej in E)
    d=(np.trace(b)-b[0,0])/l-b[0,0]/a-0.5*q(lambda E_:np.trace(E_)-E_[0,0])/l**2+0.5*q(lambda E_:E_[0,0])/a**2
    W=P@V@P; return d/np.sum(W*W)
if __name__=="__main__":
    s=1e-4
    for g2 in (0.5,0.8,1.0):
        m=3; out=[]
        for name,r2,r3 in [("parallel x2=x3",[s,0,0],[s,0,0]),("parallel x2=-x3",[s,0,0],[-s,0,0]),("parallel x2 only",[s,0,0],[0,0,0]),
                           ("orth xi2=xi3",[0,s,0],[0,s,0]),("orth xi2=-xi3",[0,s,0],[0,-s,0]),("orth xi2 _|_ xi3",[0,s,0],[0,0,s]),("orth xi2 only",[0,s,0],[0,0,0])]:
            L=np.array([[1.0,0,0],r2,r3])+np.diag([0,1e-12,1e-12]); out.append("%s %+.3f"%(name,dr(L,g2,m)))
        print("g2",g2,"|"," | ".join(out))
