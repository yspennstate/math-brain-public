# Rigorous interval fixed-point enclosure for T03 complete-second-lift scalar data.
# Uses mpmath interval arithmetic, a proved alternating-series enclosure for Phi,
# 2-point Gauss-Legendre on each z subinterval with explicit 4th-derivative remainder,
# and the previously proved |z|>9 tail bounds on 3/5<p<2/3, 0<B<5.
import mpmath as mp, sympy as sp, time
iv=mp.iv; iv.dps=60; NORD=5
SQRT2PI=iv.sqrt(2*iv.pi); INV_SQRT2PI=1/SQRT2PI

def hull(a,b): return iv.mpf([min(a.a,b.a),max(a.b,b.b)])
def phi_iv(x): return iv.exp(-x*x/2)*INV_SQRT2PI

def Phi_point(x):
    xf=float(x.a)
    if xf < 0: return 1-Phi_point(-x)
    if xf > 8:
        ph=phi_iv(x); term=1/x; s=term; n=0
        while True:
            nxt=-term*(2*n+1)/(x*x)
            if (2*(n+1)+1)/(xf*xf) >= 1:
                return 1-ph*hull(s,s+nxt)
            s=s+nxt; term=nxt; n+=1
    term=x; s=term; n=0; x2=x*x
    while True:
        nxt=-term*(x2/2)*(2*n+1)/((n+1)*(2*n+3))
        next_ratio=(xf*xf/2)*(2*(n+1)+1)/((n+2)*(2*(n+1)+3))
        if n>xf*xf/2+5 and next_ratio<1 and max(abs(float(nxt.a)),abs(float(nxt.b)))<1e-48:
            return iv.mpf('0.5')+INV_SQRT2PI*hull(s,s+nxt)
        s=s+nxt; term=nxt; n+=1

def Phi_iv(x):
    lo=Phi_point(x.a); hi=Phi_point(x.b)
    return iv.mpf([lo.a,hi.b])

class S:
    __slots__=('a',)
    def __init__(self,a):
        if isinstance(a,S): self.a=a.a[:]
        elif isinstance(a,(list,tuple)):
            self.a=[x if hasattr(x,'a') else iv.mpf(x) for x in a]+[iv.mpf(0)]*(NORD-len(a)); self.a=self.a[:NORD]
        else: self.a=[a if hasattr(a,'a') else iv.mpf(a)]+[iv.mpf(0)]*(NORD-1)
    @staticmethod
    def coerce(x): return x if isinstance(x,S) else S(x)
    def __add__(self,o): o=S.coerce(o); return S([self.a[i]+o.a[i] for i in range(NORD)])
    __radd__=__add__
    def __neg__(self): return S([-x for x in self.a])
    def __sub__(self,o): return self+(-S.coerce(o))
    def __rsub__(self,o): return S.coerce(o)+(-self)
    def __mul__(self,o):
        o=S.coerce(o); return S([sum((self.a[k]*o.a[n-k] for k in range(n+1)),iv.mpf(0)) for n in range(NORD)])
    __rmul__=__mul__
    def inv(self):
        b=[1/self.a[0]]
        for n in range(1,NORD): b.append(-sum((self.a[k]*b[n-k] for k in range(1,n+1)),iv.mpf(0))/self.a[0])
        return S(b)
    def __truediv__(self,o): return self*S.coerce(o).inv()
    def __rtruediv__(self,o): return S.coerce(o)*self.inv()
    def __pow__(self,n):
        r=S(1)
        for _ in range(n): r=r*self
        return r

def sexp(x):
    x=S.coerce(x); b=[iv.exp(x.a[0])]
    for n in range(1,NORD): b.append(sum((k*x.a[k]*b[n-k] for k in range(1,n+1)),iv.mpf(0))/n)
    return S(b)
def slog(x):
    x=S.coerce(x); dx=S([(i+1)*x.a[i+1] for i in range(NORD-1)]+[0]); q=dx/x
    b=[iv.log(x.a[0])]+[q.a[n-1]/n for n in range(1,NORD)]; return S(b)
def ssqrt(x):
    x=S.coerce(x); b=[iv.sqrt(x.a[0])]
    for n in range(1,NORD): b.append((x.a[n]-sum((b[k]*b[n-k] for k in range(1,n)),iv.mpf(0)))/(2*b[0]))
    return S(b)
def sPhi(x):
    x=S.coerce(x); ph=sexp(-x*x/2)/SQRT2PI; dx=S([(i+1)*x.a[i+1] for i in range(NORD-1)]+[0]); q=ph*dx
    return S([Phi_iv(x.a[0])]+[q.a[n-1]/n for n in range(1,NORD)])
def sphi(x): x=S.coerce(x); return sexp(-x*x/2)/SQRT2PI

def kernel(z,pint,Bint):
    p=S(pint); B=S(Bint); s=ssqrt(1-p); rp=ssqrt(p); mu=rp*z-1; A=1+2*B*s*s; a=mu/s; v=mu/(s*ssqrt(A))
    phia=sphi(a); J0=sexp(-B*mu*mu/A)/ssqrt(A)*sPhi(v); f=sPhi(-a)+J0
    J1=(mu*J0+s*phia)/A; J2=(mu*J1+s*s*J0)/A; J3=(mu*J2+2*s*s*J1)/A; J4=(mu*J3+3*s*s*J2)/A
    fB=-J2; fBB=J4; fmu=-2*B*J1; fmuB=-2*J1+2*B*J3; fmumu=-2*B*J0+4*B*B*J2
    uB=fB/f; umu=fmu/f; uBB=fBB/f-uB*uB; umuB=fmuB/f-umu*uB; umumu=fmumu/f-umu*umu
    vals=[slog(f),uB,uBB,p*umu*umu,2*p*umu*umuB,umu*umu+p*(umumu*umumu-2*umu*umu*umumu)]
    w=sphi(z); return [w*g for g in vals]

def integrate_point(pv,Bv,n,L=9):
    # The appended full-line tail constants were proved on this coarse parameter domain.
    assert 0.6 < float(pv) < 2/3 and 0 < float(Bv) < 5
    p=iv.mpf([str(pv),str(pv)]); B=iv.mpf([str(Bv),str(Bv)]); h=iv.mpf(2*L)/n; rt3=iv.sqrt(3); out=[iv.mpf(0) for _ in range(6)]
    for i in range(n):
        aa=iv.mpf(-L)+(iv.mpf(2*L)*i)/n; bb=iv.mpf(-L)+(iv.mpf(2*L)*(i+1))/n; mid=(aa+bb)/2; off=h/(2*rt3)
        v1=kernel(S([mid-off,1,0,0,0]),p,B); v2=kernel(S([mid+off,1,0,0,0]),p,B); box=kernel(S([iv.mpf([aa.a,bb.b]),1,0,0,0]),p,B)
        for k in range(6): out[k]+=h*(v1[k].a[0]+v2[k].a[0])/2 + (h**5)/4320*(24*box[k].a[4])
    tails=['3e-16','1.2e-16','1.4e-14','6.4e-14','6.4e-11','4.8e-13']
    for k,t in enumerate(tails): tt=iv.mpf(t); out[k]+=iv.mpf([-tt.b,tt.b])
    return p,B,out

# deterministic reconstruction
p,D,B,g=sp.symbols('p D B g', positive=True); q=p*D**2; gp=(1-q)/(2*D*(1-p)); c=(1-D**2)/(D*(1-p)*(1-p*D**2))
T=sp.Rational(1,2)*(1-p*q)*c-gp+sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g
TD=sp.diff(T,D).subs(g,c/(4*B)); cD=sp.diff(c,D); A0=sp.simplify(TD/cD); Tsub=sp.simplify(T.subs(g,c/(4*B)))
exprs=[c,cD,A0,sp.diff(A0,p),sp.diff(A0,D),Tsub,sp.diff(Tsub,p),sp.diff(Tsub,D),sp.diff(Tsub,B),sp.diff(c,p)]
FF=sp.lambdify((p,D,B),exprs,modules=[{'log':iv.log,'sqrt':iv.sqrt}])

def reconstruct(p,B,v):
    I,IB,IBB,K,KB,Kp=v; Ip=-K/(2*p); IBp=-KB/(2*p); R=K/(-4*p*p*B*B*IB); Dv=iv.sqrt(R)
    Dp=Dv/2*(Kp/K-2/p-IBp/IB); DB=Dv/2*(KB/K-2/B-IBB/IB)
    cc,ccD,a0,a0p,a0D,ts,tsp,tsD,tsB,ccp=FF(p,Dv,B); alpha=-cc*cc/(4*B*B*IB); H=I-B*IB-4*B*B*IB*a0
    Hp=Ip-B*IBp-4*B*B*(IBp*a0+IB*(a0p+a0D*Dp)); HB=-B*IBB-8*B*IB*a0-4*B*B*IBB*a0-4*B*B*IB*a0D*DB
    alphap=alpha*(2*(ccp+ccD*Dp)/cc-IBp/IB); alphaB=alpha*(2*ccD*DB/cc-2/B-IBB/IB)
    Sterm=cc*I/(4*B*B*IB); Psi=ts+Sterm
    return {'I':I,'IB':IB,'IBB':IBB,'K':K,'KB':KB,'Kp':Kp,'D':Dv,'H':H,'alpha':alpha,'Psi':Psi,'Hp':Hp,'HB':HB,'alphap':alphap,'alphaB':alphaB}

def fpair(x): return float(x.a),float(x.b)
def show(tag,pv,Bv,n):
    t=time.time(); pp,BB,v=integrate_point(pv,Bv,n); r=reconstruct(pp,BB,v); print('POINT',tag,'p',pv,'B',Bv,'n',n,'seconds',time.time()-t)
    for k in ['H','alpha','Psi','D','Hp','HB','alphap','alphaB','I','IB','K']:
        lo,hi=fpair(r[k]); print(tag,k,repr(lo),repr(hi),'width',repr(hi-lo))
    return r

if __name__ == "__main__":
    import sys
    pc=0.6457670646889506; bc=4.929229200895245
    which=sys.argv[1] if len(sys.argv)>1 else "center"
    if which=="center":
        r=show('CENTER',pc,bc,600)
        assert float(r['Psi'].a)>0.015
        assert float(r['HB'].a)>0 and float(r['alphap'].a)>0
        print('CENTER_RIGOROUS_PASS')
    elif which=="ll":
        r=show('LOWER_LEFT_VALID',pc-0.0015,bc-0.055,600)
        assert float(r['H'].a)>0 and float(r['alpha'].a)>12.75
        print('LOWER_LEFT_VALID_RIGOROUS_PASS')
    elif which=="rt":
        r=show('UPPER_RIGHT_VALID',pc+0.0015,bc+0.055,600)
        assert float(r['H'].b)<0 and float(r['alpha'].b)<12.75
        print('UPPER_RIGHT_VALID_RIGOROUS_PASS')
    else:
        raise SystemExit('unknown point')
