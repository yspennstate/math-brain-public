#!/usr/bin/env python3
"""
Exact fixed-point interval certificate for R18 / I0080 run 2.

Certified theorem ingredients:
  * on every b in [1/320,167/250],
      H_b(35/4)>H_b(2),
      2 H_b(1/2)>H_b(2)+H_b(35/4);
  * at b=167/250, the matched time T lies in (3.648,3.649);
  * the dynamic-level branch begins below the previously certified endpoint
      125/(585344*pi), so the two proofs overlap;
  * for the large-time branch b=1/10, kappa=3/2, d=19/20, ell>=100,
      the three required high/low/high inequalities hold;
  * the large-time branch begins at 100/(95*pi)<0.34, overlapping the
      intermediate branch whose endpoint exceeds 3.648.

All certificate arithmetic uses Python integers with outward-rounded fixed-point
intervals; no floating-point value participates in an assertion. Printed floats
are diagnostic renderings only. Monotonicity facts used by interval wrappers
are proved in the immutable run report.
"""
S=10**45

def fldiv(a,b):
    assert b>0
    return a//b

def ceild(a,b):
    assert b>0
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def rat(n,d=1):
        if n>=0:
            return I((n*S)//d, ceild(n*S,d))
        return -I.rat(-n,d)
    def __add__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return self+(-o)
    def __rsub__(self,o): return I.rat(o)-self
    def __mul__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(fldiv(min(vals),S),ceild(max(vals),S))
    __rmul__=__mul__
    def div_int(self,n):
        return I(fldiv(self.lo,n),ceild(self.hi,n))
    def inv(self):
        assert self.lo>0 or self.hi<0
        return I(fldiv(S*S,self.hi),ceild(S*S,self.lo))
    def __truediv__(self,o):
        if not isinstance(o,I): o=I.rat(o)
        return self*o.inv()
    def __rtruediv__(self,o): return I.rat(o)/self
    def f(self): return (self.lo/S,self.hi/S)

def sin_point(x,n=16):
    assert x.lo>=0 and x.hi<=S
    x2=x*x; term=x; partial=I(0)
    for k in range(n+1):
        partial=partial+(term if k%2==0 else -term)
        term=(term*x2).div_int((2*k+2)*(2*k+3))
    nxt=partial+(term if (n+1)%2==0 else -term)
    return I(min(partial.lo,nxt.lo),max(partial.hi,nxt.hi))

def cos_point(x,n=16):
    assert x.lo>=0 and x.hi<=S
    x2=x*x; term=I(S); partial=I(0)
    for k in range(n+1):
        partial=partial+(term if k%2==0 else -term)
        term=(term*x2).div_int((2*k+1)*(2*k+2))
    nxt=partial+(term if (n+1)%2==0 else -term)
    return I(min(partial.lo,nxt.lo),max(partial.hi,nxt.hi))

def atan_small_point(x,n=42):
    assert x.lo>=0 and x.hi<=S//2+2
    x2=x*x; powx=x; partial=I(0)
    for k in range(n+1):
        term=powx.div_int(2*k+1)
        partial=partial+(term if k%2==0 else -term)
        powx=powx*x2
    term=powx.div_int(2*(n+1)+1)
    nxt=partial+(term if (n+1)%2==0 else -term)
    return I(min(partial.lo,nxt.lo),max(partial.hi,nxt.hi))

ONE=I(S)

def atan_pos_point(x,PI):
    assert x.lo>=0
    if x.hi<=S//2: return atan_small_point(x)
    if x.hi<=2*S and x.lo>=S//2:
        return PI.div_int(4)+atan_any_point((x-ONE)/(x+ONE),PI)
    if x.lo>=2*S:
        return PI.div_int(2)-atan_small_point(ONE/x)
    raise AssertionError(('range',x.f()))

def atan_any_point(x,PI):
    if x.hi<0: return -atan_pos_point(-x,PI)
    if x.lo>=0: return atan_pos_point(x,PI)
    lo=-atan_pos_point(I(-x.lo,-x.lo),PI).hi
    hi=atan_pos_point(I(x.hi,x.hi),PI).hi
    return I(lo,hi)

A=atan_small_point(I.rat(1,5),50)
B=atan_small_point(I.rat(1,239),16)
PI=I(16*A.lo-4*B.hi,16*A.hi-4*B.lo)
print('pi width',(PI.hi-PI.lo)/S,PI.f())

def cosh_point(x,n=36):
    assert x.lo>=0 and x.hi<=7*S
    x2=x*x; term=I(S); partial=I(0)
    for k in range(n+1):
        partial=partial+term
        term=(term*x2).div_int((2*k+1)*(2*k+2))
    ratio_hi=ceild(x.hi*x.hi,S*(2*n+3)*(2*n+4))
    assert ratio_hi<S
    tail_hi=ceild(term.hi*S,S-ratio_hi)
    return I(partial.lo,partial.hi+tail_hi)

def sinh_point(x,n=36):
    assert x.lo>=0 and x.hi<=7*S
    x2=x*x; term=x; partial=I(0)
    for k in range(n+1):
        partial=partial+term
        term=(term*x2).div_int((2*k+2)*(2*k+3))
    ratio_hi=ceild(x.hi*x.hi,S*(2*n+4)*(2*n+5))
    assert ratio_hi<S
    tail_hi=ceild(term.hi*S,S-ratio_hi)
    return I(partial.lo,partial.hi+tail_hi)

def sinc_point(x):
    if x.hi==0:return I(S)
    return sin_point(x)/x

def sinhc_point(x):
    if x.hi==0:return I(S)
    return sinh_point(x)/x

def tanhc_point(x):
    if x.hi==0:return I(S)
    return (sinh_point(x)/cosh_point(x))/x

def zcot_point(x):
    return x*cos_point(x)/sin_point(x)

def dec_interval(func,xlo,xhi):
    A=func(xhi);B=func(xlo)
    return I(A.lo,B.hi)

def inc_interval(func,xlo,xhi):
    A=func(xlo);B=func(xhi)
    return I(A.lo,B.hi)

def atan_interval(X):
    loI=atan_any_point(I(X.lo,X.lo),PI)
    hiI=atan_any_point(I(X.hi,X.hi),PI)
    return I(loI.lo,hiI.hi)

def khat_interval(blo,bhi,y_num,y_den=1):
    # z=b/2; pi*K_b(y)=A(z)cos(z)/(y^2 B(yz)^2+A(z)^2)
    zlo=blo.div_int(2); zhi=bhi.div_int(2)
    A=dec_interval(sinc_point,zlo,zhi)
    C=I(cos_point(zhi).lo,cos_point(zlo).hi)
    y=I.rat(abs(y_num),y_den)
    Bc=I(S) if y.hi==0 else inc_interval(sinhc_point,y*zlo,y*zhi)
    return (A*C)/((Bc*Bc)*(y*y)+(A*A))

def phi_interval(blo,bhi,v_num,v_den=1):
    zlo=blo.div_int(2); zhi=bhi.div_int(2)
    U=dec_interval(zcot_point,zlo,zhi)
    av=I.rat(abs(v_num),v_den)
    if av.hi==0: X=I(0)
    else:
        C=dec_interval(tanhc_point,av*zlo,av*zhi)
        mag=av*C*U
        X=mag if v_num>=0 else -mag
    return atan_interval(X)

p=I.rat(3,50); woverell=I.rat(47,950)
ys=[(1,2),(2,1),(35,4)]

def H_interval(blo,bhi,y):
    yn,yd=y
    k=khat_interval(blo,bhi,yn,yd)
    ph=phi_interval(blo,bhi,yn,yd)
    pm=phi_interval(blo,bhi,yn-19*yd,yd)
    return p*k+woverell*(ph-pm)

b0=I.rat(1,320); bend=I.rat(167,250); step=I.rat(1,5000)
assert b0.lo==b0.hi and bend.lo==bend.hi and step.lo==step.hi
cur=b0.lo; end=bend.lo; st=step.lo
count=0; min_g23=None; min_g1=None; min_b23=None; min_b1=None
while cur<end:
    nxt=min(cur+st,end)
    blo=I(cur,cur); bhi=I(nxt,nxt)
    H1,H2,H3=[H_interval(blo,bhi,y) for y in ys]
    g23=H3-H2; g1=2*H1-H2-H3
    if min_g23 is None or g23.lo<min_g23:
        min_g23=g23.lo; min_b23=(cur,nxt)
    if min_g1 is None or g1.lo<min_g1:
        min_g1=g1.lo; min_b1=(cur,nxt)
    if g23.lo<=0 or g1.lo<=0:
        print('FAIL bin',cur/S,nxt/S,'g23',g23.f(),'g1',g1.f()); raise SystemExit(2)
    count+=1; cur=nxt
print('PASS bins',count)
print('min g23',min_g23/S,'bin',min_b23[0]/S,min_b23[1]/S)
print('min g1 ',min_g1/S,'bin',min_b1[0]/S,min_b1[1]/S)

bendI=I(end,end)
H2=H_interval(bendI,bendI,ys[1]); H3=H_interval(bendI,bendI,ys[2])
T=(I.rat(2)*(bendI*bendI))/(H2+H3)
print('T endpoint interval',T.f(),'width',(T.hi-T.lo)/S)
assert T.lo>I.rat(3648,1000).hi
assert T.hi<I.rat(3649,1000).lo

bs=I(b0.lo,b0.lo)
Hs2=H_interval(bs,bs,ys[1]); Hs3=H_interval(bs,bs,ys[2])
tstart=I.rat(2)*(bs*bs)/(Hs2+Hs3)
Told=I.rat(125,585344)/PI
print('new branch start t',tstart.f())
print('old endpoint T',Told.f())
assert tstart.hi<Told.lo
print('PASS')

# Large-time branch b=1/10, kappa=3/2, d=19/20, ell>=100.
bfix=I.rat(1,10); kappa=I.rat(3,2); d=I.rat(19,20); ell0=100
one_minus=I.rat(1)-kappa/I.rat(ell0)
y1=(2,5); y2=(13,5)
K1=khat_interval(bfix,bfix,*y1)
P1=phi_interval(bfix,bfix,*y1)
P1m=phi_interval(bfix,bfix,y1[0]-ell0*y1[1],y1[1])
M1=kappa*K1+one_minus*(P1-P1m)
level=d*PI
print('large branch M100(y1)-pi*d',(M1-level).f())
assert (M1-level).lo>0

K2=khat_interval(bfix,bfix,*y2)
P2=phi_interval(bfix,bfix,*y2)
Minf2=kappa*K2+P2+(PI-bfix).div_int(2)
print('large branch pi*d-Minf(y2)',(level-Minf2).f())
assert (level-Minf2).lo>0

P50=phi_interval(bfix,bfix,50,1)
Msym_lower=one_minus*(I.rat(2)*P50)
print('large branch symmetric lower-pi*d',(Msym_lower-level).f())
assert (Msym_lower-level).lo>0

Tlarge_start=I.rat(100,95)/PI
print('large branch start time',Tlarge_start.f())
assert Tlarge_start.hi<I.rat(34,100).lo
print('PASS large-time branch')
