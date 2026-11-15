"""Exact second-order eigenframe expansion at the specified P0."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def build():
    rr,alpha,beta,theta,p,q,v,z=ring('alpha,beta,theta,p,q,v,z',QQ)
    class J:
        def __init__(self,a=0,b=0,c=0):self.c=tuple(rr(t) for t in (a,b,c))
        def wrap(self,t):return t if isinstance(t,J) else J(t)
        def __add__(self,t):
            t=self.wrap(t);return J(*(a+b for a,b in zip(self.c,t.c)))
        __radd__=__add__
        def __neg__(self):return J(*(-a for a in self.c))
        def __sub__(self,t):return self+-self.wrap(t)
        def __rsub__(self,t):return self.wrap(t)+-self
        def __mul__(self,t):
            t=self.wrap(t);return J(*(sum(self.c[i]*t.c[j-i] for i in range(j+1)) for j in range(3)))
        __rmul__=__mul__
        def __truediv__(self,t):return J(*(a/QQ(t) for a in self.c))
        def __pow__(self,n):
            out=J(1)
            for _ in range(n):out=out*self
            return out
    E=[[-4,0,0,0],[1,1,1,1],[1,-1,1,-1],[1,-1,-1,1],[1,1,-1,-1]]
    H=[[rr.zero,-theta/5,-p/5,-q/5],[theta,rr.zero,-v,-z],
       [p,v,rr.zero,rr.zero],[q,z,rr.zero,rr.zero]]
    H2=[[sum(H[i][k]*H[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    D=[20,4,4,4]
    assert all(D[i]*H[i][j]+D[j]*H[j][i]==0 for i in range(4) for j in range(4))
    U=[J(e[0],sum(e[j]*H[j][0] for j in range(4)),sum(e[j]*H2[j][0] for j in range(4))/2) for e in E]
    W=[J(e[1],sum(e[j]*H[j][1] for j in range(4)),sum(e[j]*H2[j][1] for j in range(4))/2) for e in E]
    assert sum(u*u for u in U).c==(rr(20),rr.zero,rr.zero)
    assert sum(w*w for w in W).c==(rr(4),rr.zero,rr.zero)
    assert sum(u*w for u,w in zip(U,W)).c==(rr.zero,rr.zero,rr.zero)
    A=sum(u**4 for u in U)/400;B=sum(w**4 for w in W)/16
    C=sum(u*u*w*w for u,w in zip(U,W))/80
    d=sum(u**3 for u in U);e=sum(u*u*w for u,w in zip(U,W))
    f=sum(u*w*w for u,w in zip(U,W));h=sum(w**3 for w in W)
    aa=J(1,-alpha);r=J(1,-beta)
    m=A+r*B+(1+r)*C
    HH=(100*(1+r)*m-1600*(A+r*r*B)-1280*(1+r*r)*C-640*r*C+415*(1+r*r)-66*r)/320
    RR=3*d*d/8000+3*r*r*h*h/64+(1+4*r)*e*e/1600+(r*r+4*r)*f*f/320
    RR+=2*(1+r)*(d*f/1600+r*h*e/320)
    T=J(QQ(9,80))+aa*(11*m-2*(1+r))/8+aa*aa*(HH+RR)
    assert T.c[0]==0 and T.c[1]==QQ(11,10)*alpha-beta/20
    # The entire lineality space has vanishing second-order coefficient.
    pure={g:rr.zero for g in (alpha,beta,p,q,v,z)}
    quadratic=T.c[2]
    for g,val in pure.items():quadratic=quadratic.subs(g,val)
    assert quadratic==0
    active=[];active_polys=[]
    lam=(2+aa*(1+r))/4
    for i in range(5):
        for j in range(i+1,5):
            w=lam/5+aa*(U[i]*U[j]/20+r*W[i]*W[j]/4)
            if not w.c[0]:
                active.append(dict(edge=[i,j],linear=str(w.c[1])))
                active_polys.append(w.c[1])
    assert T.c[1]==QQ(11,4)*sum(active_polys[:4])+beta/2
    import sympy as S
    mat=S.Matrix([[S.Rational(g.get(tuple(int(i==j) for i in range(7)),0))
                   for j in range(7)] for g in active_polys])
    assert mat.rank()==6
    assert mat.nullspace()==[S.Matrix([0,0,1,0,0,0,0])]
    return dict(label='PROVED by verify_frame.py',coordinates=list(map(str,rr.gens)),
                linear=str(T.c[1]),quadratic=str(T.c[2]),active_weights=active,
                scale_filter='2*alpha-beta >= 0',ratio_filter='beta >= 0',
                nonnegative_identity='L=(11/4)*(g01+g02+g03+g04)+beta/2',
                active_derivative_rank=6,
                gauge_kernel='alpha=beta=p=q=v=z=0, theta arbitrary',gauge_quadratic='0',
                pressure_direction=dict(alpha='2*s',beta='0',theta='0',p='s',q='0',v='0',z='0',linear_T='11*s/5'))

if __name__=='__main__':
    import json
    from pathlib import Path
    data=build();Path('frame_expansion.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PROVED: eigenframe linear and quadratic expansion saved.',flush=True)
