#!/usr/bin/env python3
from fractions import Fraction as F
import itertools, math, time
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
import mpmath as mp
from mpmath import iv
import sympy as sp

mp.mp.dps = 70
iv.dps = 60
NORD = 8
PC = mp.mpf('0.6649244534165579')
BC = mp.mpf('6.197655366469065')
ATARGET = mp.mpf('12.319635')
L = mp.mpf('10')

def ilo(x): return mp.make_mpf(x._mpi_[0])
def ihi(x): return mp.make_mpf(x._mpi_[1])
def absmax(x): return max(abs(ilo(x)), abs(ihi(x)))
CIV = 1/iv.sqrt(2*iv.pi)

DP = 60
DFL = Context(prec=DP, rounding=ROUND_FLOOR)
DCE = Context(prec=DP, rounding=ROUND_CEILING)
DCLO = Decimal('0.398942280401432677939946059934381868475858631164934657665924')
DCHI = Decimal('0.398942280401432677939946059934381868475858631164934657665926')
DHALF = Decimal('0.5')
DXPAD = Decimal('1e-55')
CDF_MAX_TERMS = 0
CDF_MAX_TERM = Decimal(0)

def _dmullo(a,b): return DFL.multiply(a,b)
def _dmulhi(a,b): return DCE.multiply(a,b)
def _ddivlo(a,b): return DFL.divide(a,b)
def _ddivhi(a,b): return DCE.divide(a,b)
def _daddlo(a,b): return DFL.add(a,b)
def _daddhi(a,b): return DCE.add(a,b)
def _dsublo(a,b): return DFL.subtract(a,b)
def _dsubhi(a,b): return DCE.subtract(a,b)

def _dec_bracket_mpf(x):
    y=Decimal(mp.nstr(mp.mpf(x),70))
    return y-DXPAD, y+DXPAD

def Phi_point(x):
    global CDF_MAX_TERMS, CDF_MAX_TERM
    xl,xu=_dec_bracket_mpf(x)
    if xu < 0:
        a,b=Phi_point(-mp.mpf(x))
        return 1-b,1-a
    if xl <= 0 <= xu:
        if max(abs(xl),abs(xu)) <= DXPAD:
            tiny=Decimal('1e-54')
            return mp.mpf(str(DHALF-tiny)),mp.mpf(str(DHALF+tiny))
        raise RuntimeError('unexpected Phi bracket straddling zero')
    if xl >= 8:
        HC=Context(prec=DP+20, rounding=ROUND_CEILING)
        HF=Context(prec=DP+20, rounding=ROUND_FLOOR)
        exlo=HF.divide(HF.multiply(-xu,xu),Decimal(2))
        exhi=HC.divide(HC.multiply(-xl,xl),Decimal(2))
        with localcontext(Context(prec=DP+20)):
            elo=exlo.exp(); ehi=exhi.exp()
        elo=elo.next_minus(HF); ehi=ehi.next_plus(HC)
        phlo=_dmullo(DCLO,elo); phhi=_dmulhi(DCHI,ehi)
        qlo=_ddivlo(_dmullo(phlo,xl), _daddhi(_dmulhi(xu,xu),Decimal(1)))
        qhi=_ddivhi(phhi,xl)
        plo=_dsublo(Decimal(1),qhi); phi=_dsubhi(Decimal(1),qlo)
        return mp.mpf(str(plo)),mp.mpf(str(phi))
    if xl < 0: xl=Decimal(0)
    x2lo=_dmullo(xl,xl); x2hi=_dmulhi(xu,xu)
    lo,hi=xl,xu; Slo,Shi=lo,hi
    maxterm=max(abs(lo),abs(hi)); n=0; sign=-1
    tol=Decimal('1e-50')
    while n<2000:
        num=Decimal(2*n+1); den=Decimal(2*(n+1)*(2*n+3))
        rlo=_ddivlo(_dmullo(x2lo,num),den)
        rhi=_ddivhi(_dmulhi(x2hi,num),den)
        nlo=_dmullo(lo,rlo); nhi=_dmulhi(hi,rhi)
        if sign<0:
            Slo=_dsublo(Slo,nhi); Shi=_dsubhi(Shi,nlo)
        else:
            Slo=_daddlo(Slo,nlo); Shi=_daddhi(Shi,nhi)
        maxterm=max(maxterm,abs(nlo),abs(nhi))
        lo,hi=nlo,nhi; sign=-sign; n+=1
        num2=Decimal(2*n+1); den2=Decimal(2*(n+1)*(2*n+3))
        nrhi=_ddivhi(_dmulhi(x2hi,num2),den2)
        if rhi < 1 and nrhi < 1 and hi < tol:
            rem=_dmulhi(hi,nrhi)
            Slo=_dsublo(Slo,rem); Shi=_daddhi(Shi,rem)
            plo=_daddlo(DHALF,_dmullo(DCLO,Slo))
            phi=_daddhi(DHALF,_dmulhi(DCHI,Shi))
            CDF_MAX_TERMS=max(CDF_MAX_TERMS,n+1)
            CDF_MAX_TERM=max(CDF_MAX_TERM,maxterm)
            return mp.mpf(str(plo)),mp.mpf(str(phi))
    raise RuntimeError('Phi series failed to converge')

def Phi_iv(x):
    lo,hi=ilo(x),ihi(x)
    l,_=Phi_point(lo); _,u=Phi_point(hi)
    l=max(l,mp.mpf(0)); u=min(u,mp.mpf(1))
    assert l<=u
    return iv.mpf([l,u])

class J:
    __slots__=('c',)
    def __init__(self, c):
        if isinstance(c,J): self.c = c.c[:]
        elif isinstance(c,(list,tuple)): self.c = list(c)+[iv.mpf(0)]*(NORD+1-len(c))
        else: self.c = [c]+[iv.mpf(0)]*NORD
    def __add__(self,o):
        o=J(o); return J([self.c[i]+o.c[i] for i in range(NORD+1)])
    __radd__=__add__
    def __neg__(self): return J([-x for x in self.c])
    def __sub__(self,o): return self+(-J(o))
    def __rsub__(self,o): return J(o)-self
    def __mul__(self,o):
        o=J(o); out=[]
        for i in range(NORD+1):
            s=iv.mpf(0)
            for k in range(i+1): s += self.c[k]*o.c[i-k]
            out.append(s)
        return J(out)
    __rmul__=__mul__
    def inv(self):
        y=[1/self.c[0]]
        for n in range(1,NORD+1):
            s=iv.mpf(0)
            for k in range(1,n+1): s += self.c[k]*y[n-k]
            y.append(-s/self.c[0])
        return J(y)
    def __truediv__(self,o): return self*J(o).inv()
    def __rtruediv__(self,o): return J(o)*self.inv()
    def __pow__(self,n):
        if n==0: return J(1)
        if n<0: return (self**(-n)).inv()
        out=J(1); base=self
        while n:
            if n&1: out=out*base
            base=base*base; n//=2
        return out

def jexp(x):
    x=J(x); y=[iv.exp(x.c[0])]
    for n in range(1,NORD+1):
        s=iv.mpf(0)
        for k in range(1,n+1): s += k*x.c[k]*y[n-k]
        y.append(s/n)
    return J(y)

def jlog(x):
    x=J(x)
    xp=J([(i+1)*x.c[i+1] if i<NORD else iv.mpf(0) for i in range(NORD+1)])
    q=xp/x; y=[iv.log(x.c[0])]
    for n in range(1,NORD+1): y.append(q.c[n-1]/n)
    return J(y)

def jPhi(x):
    x=J(x); y0=Phi_iv(x.c[0])
    phi=jexp(-(x*x)/2)*CIV
    xp=J([(i+1)*x.c[i+1] if i<NORD else iv.mpf(0) for i in range(NORD+1)])
    der=phi*xp; y=[y0]
    for n in range(1,NORD+1): y.append(der.c[n-1]/n)
    return J(y)

def point_quant(zv, pp, BB):
    v=1-pp; s=iv.sqrt(v); mu=iv.sqrt(pp)*zv-1
    AA=1+2*BB*v; a=mu/s; vv=mu/(s*iv.sqrt(AA))
    phia=iv.exp(-a*a/2)*CIV
    J0=iv.exp(-BB*mu*mu/AA)/iv.sqrt(AA)*Phi_iv(vv)
    f=Phi_iv(-a)+J0
    J1=(mu*J0+s*phia)/AA
    J2=(mu*J1+v*J0)/AA
    J3=(mu*J2+2*v*J1)/AA
    J4=(mu*J3+3*v*J2)/AA
    fB=-J2; fBB=J4; fmu=-2*BB*J1; fmuB=-2*J1+2*BB*J3
    fmumu=-2*BB*J0+4*BB*BB*J2
    uB=fB/f; umu=fmu/f; uBB=fBB/f-uB*uB
    umuB=fmuB/f-umu*uB; umumu=fmumu/f-umu*umu
    return [iv.log(f), uB, uBB, pp*umu*umu,
            2*pp*umu*umuB,
            umu*umu+pp*(umumu*umumu-2*umu*umu*umumu)]

def weighted_point(zv,pp,BB):
    vals=point_quant(zv,pp,BB)
    wt=iv.exp(-zv*zv/2)*CIV
    return [wt*v for v in vals]

def jet_integrands(zjet,pp,BB):
    v=1-pp; s=iv.sqrt(v); mu=zjet*iv.sqrt(pp)-1
    AA=1+2*BB*v; a=mu/s; vv=mu/(s*iv.sqrt(AA))
    phia=jexp(-(a*a)/2)*CIV
    J0=jexp((mu*mu)*(-BB)/AA)/iv.sqrt(AA)*jPhi(vv)
    f=jPhi(-a)+J0
    J1=(mu*J0+phia*s)/AA
    J2=(mu*J1+J0*v)/AA
    J3=(mu*J2+J1*(2*v))/AA
    J4=(mu*J3+J2*(3*v))/AA
    fB=-J2; fBB=J4; fmu=J1*(-2*BB)
    fmuB=J1*(-2)+J3*(2*BB); fmumu=J0*(-2*BB)+J2*(4*BB*BB)
    uB=fB/f; umu=fmu/f; uBB=fBB/f-uB*uB
    umuB=fmuB/f-umu*uB; umumu=fmumu/f-umu*umu
    vals=[jlog(f), uB, uBB, (umu*umu)*pp,
          (umu*umuB)*(2*pp),
          umu*umu+(umumu*umumu-2*umu*umu*umumu)*pp]
    wt=jexp(-(zjet*zjet)/2)*CIV
    return [wt*x for x in vals]

def tail_bounds(pp,BB,Lv=L):
    pmax=ihi(pp); Bmax=ihi(BB)
    zz=iv.mpf([Lv,Lv]); ph=ihi(iv.exp(-zz*zz/2)*CIV)
    T=[None]*5
    T[0]=2*ph/Lv; T[1]=2*ph
    for r in range(2,5): T[r]=2*(Lv**(r-1))*ph+(r-1)*T[r-2]
    a=ihi(iv.sqrt(pp))
    U=[]
    for r in range(5):
        s=mp.mpf(0)
        for k in range(r+1): s += math.comb(r,k)*(a**k)*(mp.mpf(3)**(r-k))*T[k]
        U.append(s)
    return [Bmax*U[2], U[2], U[4],
            4*pmax*Bmax**2*U[2],
            8*pmax*Bmax*U[2]+16*pmax*Bmax**2*U[4],
            4*pmax*Bmax**2*T[0]+(4*Bmax**2+16*pmax*Bmax**3)*U[2]]

def widen_tails(ints,tb):
    return [iv.mpf([ilo(x)-t, ihi(x)+t]) for x,t in zip(ints,tb)]

def boole_box(pp,BB,h=mp.mpf('.02')):
    n=int(mp.nint(2*L/h)); assert n%4==0
    nodes=[]
    for i in range(n+1):
        z=-L+i*h; nodes.append(weighted_point(iv.mpf([z,z]),pp,BB))
    sums=[iv.mpf(0)]*6; W=[7,32,12,32,7]
    for i in range(0,n,4):
        for j,w in enumerate(W):
            for k in range(6): sums[k]+=w*nodes[i+j][k]
    ints=[s*(2*h/45) for s in sums]
    errs=[mp.mpf(0)]*6
    for i in range(0,n,4):
        a=-L+i*h; b=a+4*h
        js=jet_integrands(J([iv.mpf([a,b]),iv.mpf(1)]),pp,BB)
        for k in range(6): errs[k]+=(mp.mpf(8)/945)*h**7*mp.factorial(6)*absmax(js[k].c[6])
    return [iv.mpf([ilo(ints[k])-errs[k],ihi(ints[k])+errs[k]]) for k in range(6)],errs

def gl4_center(pp,BB,pan=mp.mpf('.025')):
    npan=int(mp.nint(2*L/pan))
    rr=iv.sqrt(iv.mpf(6)/5)
    xout=iv.sqrt(iv.mpf(3)/7+iv.mpf(2)/7*rr)
    xin=iv.sqrt(iv.mpf(3)/7-iv.mpf(2)/7*rr)
    wout=(18-iv.sqrt(30))/36; win=(18+iv.sqrt(30))/36
    xs=[-xout,-xin,xin,xout]; ws=[wout,win,win,wout]
    sums=[iv.mpf(0)]*6; errs=[mp.mpf(0)]*6
    CG=mp.mpf(math.factorial(4)**4)/(9*math.factorial(8)**3)
    for i in range(npan):
        a=-L+i*pan; b=a+pan; mid=(a+b)/2; rad=(b-a)/2
        for xn,wn in zip(xs,ws):
            zv=iv.mpf([mid,mid])+xn*rad
            vals=weighted_point(zv,pp,BB)
            for k in range(6): sums[k]+=(wn*rad)*vals[k]
        js=jet_integrands(J([iv.mpf([a,b]),iv.mpf(1)]),pp,BB)
        for k in range(6): errs[k]+=CG*(b-a)**9*mp.factorial(8)*absmax(js[k].c[8])
    return [iv.mpf([ilo(sums[k])-errs[k],ihi(sums[k])+errs[k]]) for k in range(6)],errs

p,D,B,g=sp.symbols('p D B g', positive=True)
q=p*D**2
gp=(1-q)/(2*D*(1-p))
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
T=sp.Rational(1,2)*(1-p*q)*c-gp+sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g
TD=sp.diff(T,D).subs(g,c/(4*B)); cD=sp.diff(c,D)
A0=sp.simplify(TD/cD); Tsub=sp.simplify(T.subs(g,c/(4*B)))
exprs=[c,cD,A0,sp.diff(A0,p),sp.diff(A0,D),Tsub,
       sp.diff(Tsub,p),sp.diff(Tsub,D),sp.diff(Tsub,B),sp.diff(c,p)]
ifun=sp.lambdify((p,D,B),exprs,modules=[{'log':iv.log,'sqrt':iv.sqrt,'exp':iv.exp}])

def derived_grad(pp,BB,ints):
    I,IB,IBB,K,KB,Kp=ints
    IBp=-KB/(2*pp); Ip=-K/(2*pp)
    R0=K/(-4*pp*pp*BB*BB*IB); DD=iv.sqrt(R0)
    Dp=(DD/2)*(Kp/K-2/pp-IBp/IB)
    DB=(DD/2)*(KB/K-2/BB-IBB/IB)
    cc,ccD,a0,a0p,a0D,ts,tsp,tsD,tsB,ccp=ifun(pp,DD,BB)
    alpha=-cc*cc/(4*BB*BB*IB)
    H=I-BB*IB-4*BB*BB*IB*a0
    Hp=Ip-BB*IBp-4*BB*BB*(IBp*a0+IB*(a0p+a0D*Dp))
    HB=-BB*IBB-8*BB*IB*a0-4*BB*BB*IBB*a0-4*BB*BB*IB*a0D*DB
    ap=alpha*(2*(ccp+ccD*Dp)/cc-IBp/IB)
    aB=alpha*(2*ccD*DB/cc-2/BB-IBB/IB)
    RR=I/(4*BB*BB*IB)
    Rp=(Ip*IB-I*IBp)/(4*BB*BB*IB*IB)
    RB=iv.mpf(1)/(4*BB*BB)+RR*(-2/BB-IBB/IB)
    Psip=tsp+tsD*Dp+(ccp+ccD*Dp)*RR+cc*Rp
    PsiB=tsB+tsD*DB+(ccD*DB)*RR+cc*RB
    Psi=ts+cc*RR
    return dict(D=DD,c=cc,H=H,alpha=alpha,Hp=Hp,HB=HB,
                alphap=ap,alphaB=aB,Psi=Psi,Psip=Psip,PsiB=PsiB)

# Frozen rational approximate inverse of the point Jacobian at the scout.
Aq=[[F(-7294853,100000),F(-504965,10000000)],
    [F(-3028867,1000),F(-3758826,1000000)]]
dr=[F(1,10_000_000),F(1,250_000)]
ranges=[(F(-34,1000),F(-28,1000)),
        (F(32,100000),F(51,100000)),
        (F(246,10),F(254,10)),
        (F(-603,1000),F(-600,1000))]
def mm(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def qvertex(hp,hb,ap,ab):
    AJ=mm(Aq,[[hp,hb],[ap,ab]])
    M=[[F(int(i==j))-AJ[i][j] for j in range(2)] for i in range(2)]
    return max(sum(abs(F(1,dr[i])*M[i][j]*dr[j]) for j in range(2)) for i in range(2))
Q=max(qvertex(*v) for v in itertools.product(*ranges))
EH=F(47,10**13)
EA=F(37,10**12)
ETA=max(F(1,dr[i])*(abs(Aq[i][0])*EH+abs(Aq[i][1])*EA) for i in range(2))
RHO=ETA/(1-Q)
LWEIGHT=F(896,1000)*dr[0]+F(214,10000)*dr[1]
PSI0=F(2308,10**11)
PSIROOTLB=PSI0-LWEIGHT*RHO

t0=time.time()
pp0=iv.mpf([PC,PC]); BB0=iv.mpf([BC,BC])
center,_=gl4_center(pp0,BB0)
center=widen_tails(center,tail_bounds(pp0,BB0))
DC=derived_grad(pp0,BB0,center)
dp=mp.mpf('1e-7'); dB=mp.mpf('4e-6')
ppb=iv.mpf([PC-dp,PC+dp]); BBb=iv.mpf([BC-dB,BC+dB])
box,_=boole_box(ppb,BBb)
box=widen_tails(box,tail_bounds(ppb,BBb))
DBOX=derived_grad(ppb,BBb,box)

assert ilo(DBOX['Hp']) >= mp.mpf('-.034') and ihi(DBOX['Hp']) <= mp.mpf('-.028')
assert ilo(DBOX['HB']) >= mp.mpf('.00032') and ihi(DBOX['HB']) <= mp.mpf('.00051')
assert ilo(DBOX['alphap']) >= mp.mpf('24.6') and ihi(DBOX['alphap']) <= mp.mpf('25.4')
assert ilo(DBOX['alphaB']) >= mp.mpf('-.603') and ihi(DBOX['alphaB']) <= mp.mpf('-.600')
assert abs(ilo(DC['H'])) < mp.mpf('4.7e-12') and abs(ihi(DC['H'])) < mp.mpf('4.7e-12')
assert abs(ilo(DC['alpha'])-ATARGET) < mp.mpf('3.7e-11')
assert abs(ihi(DC['alpha'])-ATARGET) < mp.mpf('3.7e-11')
assert ilo(DC['Psi']) > mp.mpf('2.308e-8')
assert absmax(DBOX['Psip']) < mp.mpf('.896')
assert absmax(DBOX['PsiB']) < mp.mpf('.0214')
assert Q == F(70497781,125000000)
assert ETA == F(7187375731,2000000000000)
assert ETA < 1-Q
assert RHO < 1
assert PSIROOTLB > 0

qbox=ppb*DBOX['D']*DBOX['D']
gpbox=(1-qbox)/(2*DBOX['D']*(1-ppb))
gammabox=DBOX['c']/(4*BBb)
assert ilo(ppb)>0 and ihi(ppb)<1 and ilo(qbox)>0 and ihi(qbox)<1
assert ilo(gpbox)>0 and ilo(gammabox)>0 and ilo(DBOX['c'])>0

print('TARGET_ALPHA',mp.nstr(ATARGET,20))
print('CENTER_BOX p',mp.nstr(PC,18),'+/-',mp.nstr(dp,8))
print('CENTER_BOX B',mp.nstr(BC,18),'+/-',mp.nstr(dB,8))
for k in ['H','alpha','Psi','D']:
    x=DC[k]; print('CENTER',k,mp.nstr(ilo(x),30),mp.nstr(ihi(x),30))
for k in ['Hp','HB','alphap','alphaB','Psip','PsiB','Psi','D']:
    x=DBOX[k]; print('WHOLE_BOX',k,mp.nstr(ilo(x),30),mp.nstr(ihi(x),30))
print('WHOLE_BOX q',mp.nstr(ilo(qbox),30),mp.nstr(ihi(qbox),30))
print('WHOLE_BOX gamma_p',mp.nstr(ilo(gpbox),30),mp.nstr(ihi(gpbox),30))
print('WHOLE_BOX c',mp.nstr(ilo(DBOX['c']),30),mp.nstr(ihi(DBOX['c']),30))
print('WHOLE_BOX gamma',mp.nstr(ilo(gammabox),30),mp.nstr(ihi(gammabox),30))
print('Q_EXACT',Q,float(Q),'ONE_MINUS_Q',1-Q,float(1-Q))
print('ETA_EXACT',ETA,float(ETA),'ETA_LT_ONE_MINUS_Q',ETA<1-Q)
print('RHO_EXACT',RHO,float(RHO))
print('LWEIGHT_EXACT',LWEIGHT,float(LWEIGHT))
print('PSI0_EXACT',PSI0,float(PSI0))
print('PSI_ROOT_LOWER_EXACT',PSIROOTLB,float(PSIROOTLB))
print('RUNTIME_SECONDS',round(time.time()-t0,3))
print('CERTIFIED_ALPHA_U 12.319635')
print('ALL_APOSTERIORI_CONTRACTION_CHECKS_PASS')
