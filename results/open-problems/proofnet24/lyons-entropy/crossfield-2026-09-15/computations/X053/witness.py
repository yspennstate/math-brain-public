import numpy as np
from math import log
from fractions import Fraction as F
for pq in [(12,5,13),(4,3,5),(20,21,29),(3,4,5),(5,12,13)]:
    co,si,den=pq
    a=F(3,5);b=F(5,13);R=F(48,65);r=R*F(co,den)-a*b;v=R*F(si,den)
    for eps in [F(1,10**6),F(1,10**12)]:
        r1=r*(1-eps);v1=v*(1-eps)
        C=np.array([[0,float(a),complex(float(r1),-float(v1))],[float(a),0,float(b)],[complex(float(r1),float(v1)),float(b),0]])
        K=(np.eye(3)+C)/2
        x=np.array([abs(C[1,2])**2,abs(C[2,0])**2,abs(C[0,1])**2]);c=np.linalg.det(C).real;ss=sum(x)
        u=np.r_[1-ss,1+ss-2*x]
        p=np.r_[(u+c)/8,(u-c)/8]
        tau=np.log((u+c)/(u-c)).sum()
        J=np.eye(3)-K
        G=abs(J)**2
        nu=3-np.diag(J).real@np.linalg.inv(G)@np.diag(J).real
        covariance=np.diag(np.diag(K).real)-abs(K)**2
        pe=(u[0]-c)/8
        kappa=1-pe-pe*np.ones(3)@np.linalg.inv(covariance)@np.ones(3)/4
        print(pq, 'eps',float(eps),'x',x,'cos',c/np.sqrt(4*np.prod(x)),'nu',nu,'criterion',tau*kappa*(1-1/nu),'c',c,'pE',pe)
