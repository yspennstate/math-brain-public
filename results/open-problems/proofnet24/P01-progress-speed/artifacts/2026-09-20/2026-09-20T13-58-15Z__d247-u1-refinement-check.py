from fractions import Fraction as Q
from math import comb
PMIN=Q(3,8); LAM0=Q(1661,2500); L=Q(2,3)

def bmin(n,l): return Q(n)*(1-l)/(Q(n)-Q(n-1)*l)
def chord(n,l):
    c=1-l; lo=bmin(n,l); hi=Q(n)/(Q(n)+l); s=(hi-lo)/l
    return lo-s*c,s

def lower_high(D,p,l):
    a1,s1=chord(1,l); aD,sD=chord(D,l)
    A=(1-p)*a1+p*aD; S=(1-p)*s1+p*sD
    mu=A/(1-S); return mu,aD+sD*mu

def qpoly(D,p,l,u): return Q(D)*u*u+(l*(D+1)-D)*u+l*l-l*(1+p*(D-1))
def theta(D,p,l):
    t=(1+l)/(Q(D)+l); return p*t/(1-p+p*t),t

def static_margin(D,p):
    th=Q(5)*p/(Q(3*D+2)-Q(3*(D-1))*p)
    d=1-Q(D-1)*th+Q(2*(D-1))*th*th
    return 2*d/(Q(5,3)+Q(D-1)*th)**2

def static_delta(D,p):
    th=Q(5)*p/(Q(3*D+2)-Q(3*(D-1))*p)
    return 1-Q(D-1)*th+Q(2*(D-1))*th*th

def support_margin(p,l): return 2*(1-p)*(1-l-2*p*l*l)/((1-l)*(1+l)**2)

def refined_bounds(D,p0,l0,u,steps):
    U1=u/(l0+u); UD=Q(D)*u/(l0+Q(D)*u)
    hist=[U1]
    assert 0<U1<UD<1
    # Only the one-child conditional mean is iterated. Keeping UD at its
    # valid zeroth upper bound avoids any hidden fixed-point assumption.
    for _ in range(steps):
        f1=U1/(l0+U1); fD=UD/(l0+UD)
        U1n=(1-p0)*f1+p0*fD
        assert 0<U1n<U1<UD
        U1=U1n; hist.append(U1)
    return U1,UD,hist

def jscore(D,pmin,p0,l0,L,u,steps):
    _,M=lower_high(D,pmin,L)
    U1,UD,hist=refined_bounds(D,p0,l0,u,steps)
    pref=Q(D)*M*(M-(1-l0))/l0
    s=Q(0)
    for k in range(D+1):
        pr=Q(comb(D,k))*p0**k*(1-p0)**(D-k)
        den=M+Q(D-k)*U1+Q(k)*UD-(1-L)
        s += pr/(den*den)
    return pref*s,M,U1,UD,hist

def endpoint(D,p,L,J):
    h=D-1; th,t=theta(D,p,L); C=L/(1-L)-p*L*J
    d=1+Q(h)*th-Q(h)*C*th*(1-th)
    m=2*d/(1+Q(h)*th+L)**2
    H=L*J; C0=L/(1-L)
    N=1-C0+p*(C0*(1+t)+t-1+2*H)-3*H*p*p+H*(1-t)*p**3
    Np=C0*(1+t)+t-1+2*H-6*H*p+3*H*(1-t)*p*p
    return d,m,th,C,N,Np

def certify(D,p0,u,steps,target):
    sm=static_margin(D,PMIN); assert sm>target
    slack=1-(2*p0*LAM0*LAM0+LAM0); assert slack>0
    lm=support_margin(p0,LAM0); assert lm>target
    q=qpoly(D,p0,LAM0,u); assert q>0
    qs=(D+1)*u+2*LAM0-(1+p0*(D-1)); assert qs>0
    rs=Q(D)*(1-L)-(1+L); assert rs>0
    J,M,U1,UD,hist=jscore(D,PMIN,p0,LAM0,L,u,steps)
    d,m,th,C,N,Np=endpoint(D,p0,L,J)
    cps=1/(1-LAM0)**2-p0*J; assert cps>0
    C0=LAM0/(1-LAM0)-p0*LAM0*J
    tds=C0*(1-2*th)-1; assert tds>0
    assert N<0 and Np>0 and d>0 and m>target
    return dict(D=D,p0=p0,u=u,target=target,sm=sm,slack=slack,lm=lm,q=q,qs=qs,rs=rs,J=J,M=M,U1=U1,UD=UD,hist=hist,d=d,m=m,N=N,Np=Np,cps=cps,tds=tds)

A=certify(247,Q(19,50),Q(34784,50000),7,Q(1,800000))
B=certify(248,Q(3799,10000),Q(69567,100000),7,Q(1,11000))
assert static_delta(248,Q(3799,10000))<0
# Immediate full-cap D=248 failure after 12 scalar refinements.
Jf,_,_,_,_=jscore(248,PMIN,Q(19,50),LAM0,L,Q(69567,100000),12)
df,mf,*_=endpoint(248,Q(19,50),L,Jf)
assert df<0
print('ALL_EXACT_CHECKS_PASS')
for tag,R in [('D247_FULL',A),('D248_EXT',B)]:
    print(tag)
    print('D',R['D'],'p0',float(R['p0']),'steps',len(R['hist'])-1)
    print('margin',float(R['m']),'target',float(R['target']),'gt',R['m']>R['target'])
    print('delta',float(R['d']),'J',float(R['J']))
    print('U1_sequence',[float(x) for x in R['hist']])
    print('UD_fixed',float(R['UD']))
    print('static_margin_p3/8',float(R['sm']))
    print('lower_strip_margin',float(R['lm']),'support_slack',float(R['slack']))
    print('qcap',float(R['q']),'q_slope',float(R['qs']))
    print('N',float(R['N']),'Np',float(R['Np']))
    print('Cprime_slack',float(R['cps']),'theta_direction_slack',float(R['tds']))
print('D248_p3799_old_static_delta',float(static_delta(248,Q(3799,10000))))
print('D248_fullcap_12ref_delta',float(df),'margin',float(mf))
