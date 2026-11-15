"""Five-vertex D=2 formulas and exact-stratum parametrization."""
import numpy as np
from scipy.linalg import helmert
H = np.eye(5)-np.ones((5,5))/5
BASIS = helmert(5, full=False).T
IJ = np.triu_indices(5, 1)
PAIRS = list(zip(*IJ))

def frame(theta):
    R=np.eye(4)
    for t,(i,j) in zip(theta,[(0,1),(0,2),(0,3),(1,2),(1,3)]):
        c,s=np.cos(t),np.sin(t)
        ci,cj=R[:,i].copy(),R[:,j].copy()
        R[:,i]=c*ci+s*cj
        R[:,j]=-s*ci+c*cj
    return BASIS@R[:,:2]

def matrices(a,b,U):
    lam=(2+a+b)/4
    G=(U*np.array([a,b]))@U.T
    Pi=H-U@U.T
    L=lam*H-G
    weights=(lam/5+G)[IJ]
    return lam,G,Pi,L,weights

def moments(U):
    u,w=U.T
    return np.array([sum(u**4),sum(w**4),sum(u*u*w*w),sum(u**3),sum(u*u*w),sum(u*w*w),sum(w**3),sum(u**3*w),sum(u*w**3)])

def closed(a,b,U):
    A,B,C,d,e,f,h,odd1,odd2=moments(U)
    lam=(2+a+b)/4
    s=a+b
    K=a*a*A+b*b*B+2*a*b*C-(a*a+b*b)/5-a*a*(d*d+e*e)-2*a*b*(e*e+f*f)-b*b*(f*f+h*h)
    X1=2*(lam*s-a*a-b*b)
    X2=10*K/3
    diag=.8-np.sum(U*U,axis=1)
    t=np.dot(diag,a*U[:,0]**2+b*U[:,1]**2)
    X3=(1-lam)/3*(2*s-10*t/3)
    S5=lam/5*(6*s-5*(a*(A+C)+b*(B+C)))+a*a*(-2+4*A-3*d*d)+b*b*(-2+4*B-3*h*h)-3*a*b*(e*e+f*f)-s*(a*(d*f+2*e*e-2*C)+b*(h*e+2*f*f-2*C))
    return np.array([X1,X2,X3,2*S5])

def direct(a,b,U):
    lam,G,Pi,L,weights=matrices(a,b,U)
    S1=2*(2*lam-np.trace(L@L))
    S2=np.dot(np.diag(Pi),np.diag(G))
    S3=sum(z*(Pi[i,i]*G[i,i]+Pi[j,j]*G[j,j]-2*Pi[i,j]*G[i,j]) for z,(i,j) in zip(weights,PAIRS))
    S4=2*(4*lam-2)
    S5=sum(z*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for z,(i,j) in zip(weights,PAIRS))
    return np.array([S1,10/3*(lam*S2-S3),(1-lam)/3*(S4-10*S2/3),2*S5])

def pair_terms(a,b,U):
    lam,G,Pi,L,weights=matrices(a,b,U)
    ev,V=np.linalg.eigh(Pi)
    top=V[:,-2:]
    out=np.zeros(4)
    for gap,v in zip([a,b],U.T):
        mu=lam-gap
        for x in top.T:
            p=x*v
            norm=1-10/3*np.dot(p,p)
            out[0]+=gap*mu
            out[1]+=gap*10/3*(lam*np.dot(p,p)-p@L@p)
            out[2]+=gap*(1-lam)/3*norm
            out[3]+=gap*2*sum(z*((x[i]-x[j])*(v[i]-v[j]))**2 for z,(i,j) in zip(weights,PAIRS))
    return out

def tmax(r,U):
    C=(1+r)/20+(np.outer(U[:,0],U[:,0])+r*np.outer(U[:,1],U[:,1]))[IJ]
    return min(np.min(-.1/C[C<0]),2/(3-r))

def ratio(terms):
    den=sum(terms[:3])
    return 1-terms[3]/den if den>1e-15 else np.nan
