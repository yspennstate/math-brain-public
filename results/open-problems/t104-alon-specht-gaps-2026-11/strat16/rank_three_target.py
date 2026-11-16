"""Exact matrix targets on the five-vertex zero-edge gap chart.

This module constructs identities, not a sign proof by itself.
"""
from functools import lru_cache
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


@lru_cache(None)
def construct():
    rr,t,x,y,v,w,z=ring('t,x,y,v,w,z',QQ)
    V=[(x,y),(v,w),(1-t-x-v,-z-y-w),(t,rr.zero),(-rr.one,z)]
    R=[[sum(V[i][a]*V[j][a]for a in range(2))for j in range(5)]for i in range(5)]
    tau=sum(R[i][i]for i in range(5));T=5*t;Z=3*T-tau
    rv=sum(R[i][j]**2 for i in range(5)for j in range(5))
    ds=[R[i][i]for i in range(5)]
    rd=[sum(R[i][j]*ds[j]for j in range(5))for i in range(5)]
    cs=[QQ(16,5)*tau*T-4*rv+2*Z*T,
        Z*(-QQ(47,5)*T+2*tau),QQ(6,5)*Z*T]
    mats=[]
    for c in range(3):
        H=[[rr.zero for j in range(5)]for i in range(5)]
        for i in range(5):
            for j in range(5):
                H[i][j]=int(i==j)*cs[c]
                if c<2:H[i][j]+=(-4 if c==0 else 8)*R[i][j]**2
                if c==0:H[i][j]+=2*T*R[i][j] # add S, annihilating selected u
            if c==0:H[i][i]+=-4*T*ds[i]-4*rd[i]+8*sum(R[i][j]**2 for j in range(5))
            else:H[i][i]+=(-2 if c==1 else -4)*Z*ds[i]
        # Constant rational basis e_i-e_4 of 1-perpendicular.
        mats.append([[H[i][j]-H[i][4]-H[4][j]+H[4][4]for j in range(4)]for i in range(4)])
    controls=[mats[0],[[mats[0][i][j]+mats[1][i][j]/10 for j in range(4)]for i in range(4)],
              [[mats[0][i][j]+mats[1][i][j]/5+mats[2][i][j]/25 for j in range(4)]for i in range(4)]]
    gs={'g'+str(i)+str(j):t+R[i][j]for i in range(5)for j in range(i+1,5)if(i,j)!=(3,4)}
    bounds=[(1,4),(-1,0),(-4,4),(-1,QQ(1,2)),(-4,4),(0,4)]
    for i,(a,b)in enumerate(bounds):gs['box'+str(i)]=(rr.gens[i]-a)*(b-rr.gens[i])
    return rr,V,R,mats,controls,gs,bounds
