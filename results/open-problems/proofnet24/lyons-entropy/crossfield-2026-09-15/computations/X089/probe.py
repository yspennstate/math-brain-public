import itertools, json
import numpy as np

def jet(w,v):
    out=[]
    for t in itertools.product([-1,1],repeat=len(w)):
        q0,q1=1.,1.; a0,a1=0.,0.; b0,b1=0.,0.
        for x,h,s in zip(w,v,t):
            q2=q1+s*x*q0
            a2=a1+s*(x*a0+h*q0)
            b2=b1+s*(x*b0+2*h*a0)
            q0,q1,a0,a1,b0,b1=q1,q2,a1,a2,b1,b2
        out.append((q1,a1,b1))
    return np.array(out)

def curvature(w,v):
    q,a,b=jet(w,v).T
    return np.mean(a*a/q+b*np.log(q))

def hess(w):
    m=len(w); eye=np.eye(m)
    diag=[curvature(w,e) for e in eye]
    H=np.diag(diag)
    for i in range(m):
        for j in range(i):
            H[i,j]=H[j,i]=(curvature(w,eye[i]+eye[j])-diag[i]-diag[j])/2
    return H

results=[]
for w in [np.array([.16,.25,.16]),np.array([.2,.2,.3,.1]),np.array([.36,.1,.2,.25]),np.array([.01,.4,.3,.1])]:
    H=hess(w); old=np.zeros_like(H); old[:-1,:-1]=hess(w[:-1]); J=H-old
    ev,vec=np.linalg.eigh(J)
    results.append({'w':w.tolist(),'increment_eigs':ev.tolist(),'min_direction':vec[:,0].tolist(),'total_eigs':np.linalg.eigvalsh(H).tolist()})
print(json.dumps(results,indent=2))

def momentjet(w,v,m):
    A,Ad,Add=jet(w,v).T
    B,Bd,Bdd=jet(w[:-1],v[:-1]).T
    B=np.repeat(B,2); Bd=np.repeat(Bd,2); Bdd=np.repeat(Bdd,2)
    f=B**(m+1)/A**m
    logd=(m+1)*Bd/B-m*Ad/A
    logdd=(m+1)*(Bdd/B-(Bd/B)**2)-m*(Add/A-(Ad/A)**2)
    return np.mean(f),np.mean(f*logd),np.mean(f*(logdd+logd**2))

moment_results=[]
for w in [np.array([.16,.25]),np.array([.2,.2,.3]),np.array([.36,.1,.2,.25])]:
    for m in [1,3,7]:
        E=np.eye(len(w)); jets=[momentjet(w,e,m) for e in E]
        C=jets[0][0]; grad=np.array([j[1] for j in jets]); H=np.diag([j[2] for j in jets])
        for i in range(len(w)):
            for j in range(i):
                H[i,j]=H[j,i]=(momentjet(w,E[i]+E[j],m)[2]-H[i,i]-H[j,j])/2
        T=C*H-(m+1)/m*np.outer(grad,grad)
        ev,vec=np.linalg.eigh(T)
        moment_results.append({'w':w.tolist(),'m':m,'min_eig':ev[0],'direction':vec[:,0].tolist()})
print(json.dumps(moment_results,indent=2))
