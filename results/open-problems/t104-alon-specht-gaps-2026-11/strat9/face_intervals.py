"""PROVED: inclusion arithmetic for the exact zero-face numerator."""
from fractions import Fraction as F
from math import isqrt


class Interval:
    def __init__(self,lo,hi=None):
        self.lo=F(lo)
        self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def wrap(x):
        return x if isinstance(x,Interval)else Interval(x)
    def __add__(self,other):
        other=self.wrap(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):
        return Interval(-self.hi,-self.lo)
    def __sub__(self,other):
        return self+-self.wrap(other)
    def __rsub__(self,other):
        return self.wrap(other)+-self
    def __mul__(self,other):
        other=self.wrap(other)
        vals=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return Interval(min(vals),max(vals))
    __rmul__=__mul__
    def square(self):
        return Interval(0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi),
                        max(self.lo*self.lo,self.hi*self.hi))


def evaluate(box):
    t,v1,z1,v2,z2,z=[Interval(*v)for v in box]
    V=[(v1,z1),(v2,z2),(1-t-v1-v2,-z-z1-z2),(t,Interval(0)),(Interval(-1),z)]
    R=[[sum(V[i][a]*V[j][a]for a in range(2))for j in range(5)]for i in range(5)]
    for i in range(5):
        R[i][i]=sum(x.square()for x in V[i])
    M00=sum(v[0].square()for v in V)
    M11=sum(v[1].square()for v in V)
    M01=sum(v[0]*v[1]for v in V)
    Delta=M00*M11-M01.square()
    N=M00+M11
    D=20*t-N
    adj=((M11,-M01),(-M01,M00))
    Q=[[sum(V[i][a]*adj[a][b]*V[j][b]for a in range(2)for b in range(2))
        for j in range(5)]for i in range(5)]
    P=[[Delta*(5*int(i==j)-1)-5*Q[i][j]for j in range(5)]for i in range(5)]
    trace2=M00.square()+M11.square()+2*M01.square()
    sumPR2=sum(P[i][j]*R[i][j].square()for i in range(5)for j in range(5))
    sumPR=sum(P[i][i]*R[i][i]for i in range(5))
    edge=Interval(0)
    for i in range(5):
        for j in range(i+1,5):
            if(i,j)==(3,4):continue
            gg=t+R[i][j]
            qdiff=Q[i][i]+Q[j][j]-2*Q[i][j]
            rdiff=R[i][i]+R[j][j]-2*R[i][j]
            edge+=gg*(2*Delta-qdiff)*rdiff
    common=Delta*(40*t*N-8*trace2)
    p0=160*common+384*sumPR2+(D-10*t)*(3920*t*Delta-160*D*Delta-48*sumPR)-1280*edge
    p1=80*common+160*sumPR2+(D-10*t)*(1720*t*Delta-40*D*Delta-8*sumPR)-640*edge
    p2=10*common+16*sumPR2+(D-10*t)*(200*t*Delta)-80*edge
    return t,Delta,D,(p0,p1,p2)


def source_chart(source,permutation=None):
    from rational_rays import frame_data
    U,W=source['U'],source['W']
    r=F(source['r'])
    data=frame_data(U,W,r)
    a,b,la=data['a'],data['a']*r,data['lam']
    uu,ww=sum(x*x for x in U),sum(x*x for x in W)
    pairs=[(i,j)for i in range(5)for j in range(i+1,5)]
    edge=pairs[data['weights'].index(F(0))]
    perm=list(permutation)if permutation is not None else [i for i in range(5)if i not in edge]+list(edge)
    U=[U[i]for i in perm]
    W=[W[i]for i in perm]
    k=3
    first=lambda i:5*(a*F(U[k]*U[i],uu)+b*F(W[k]*W[i],ww))/la
    t=first(3)
    radicand=a*b/(la*la*uu*ww)
    firsts=[first(i)for i in range(5)]
    seconds=[5*(U[k]*W[i]-W[k]*U[i])for i in range(5)]
    assert firsts[3]==t and firsts[4]==-1 and seconds[3]==0
    assert sum(firsts)==sum(seconds)==0
    for i in range(5):
        for j in range(5):
            gap=a*F(U[i]*U[j],uu)+b*F(W[i]*W[j],ww)
            assert firsts[i]*firsts[j]+seconds[i]*seconds[j]*radicand==5*t*gap/la
    trace=sum(firsts[i]*firsts[i]+seconds[i]*seconds[i]*radicand for i in range(5))
    assert 10*t/(20*t-trace)==la
    scale=10**12
    low=isqrt(radicand.numerator*scale*scale//radicand.denominator)
    root=Interval(F(low,scale),F(low+1,scale))
    assert root.lo*root.lo<=radicand<=root.hi*root.hi
    second=lambda i:5*(U[k]*W[i]-W[k]*U[i])*root
    coordinates=[Interval(t),Interval(first(0)),second(0),Interval(first(1)),second(1),second(4)]
    return coordinates,perm,data
