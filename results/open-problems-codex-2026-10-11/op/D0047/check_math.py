import pathlib,sympy as sp,math,json
p=pathlib.Path('.')
s,c,L,th,x,r,a=sp.symbols('s c L th x r a',nonzero=True)
V=sp.Function('V')(s,th);H=1-(th+s)/L+s*V/L
op=lambda F:-c*s*sp.diff(F,s)+c*s*sp.diff(F,th)+(1-sp.cos(th))*sp.diff(F,th,2)
checks=[]
def ck(name,value):
 assert sp.simplify(value)==0,(name,value);checks.append(name+': PASS')
ck('discounted hitting operator identity',op(H)-s/L*(op(V)-c*V))
U=sp.Function('U')(s,x);S=1+x*x
ang1=-S/2*sp.diff(U,x)
ang2=S*S/4*sp.diff(U,x,2)+x*S/2*sp.diff(U,x)
ck('cotangent generator map',2*(-c*s*sp.diff(U,s)+c*s*ang1+2/S*ang2)-(-2*c*s*sp.diff(U,s)+S*sp.diff(U,x,2)+(2*x-c*s*S)*sp.diff(U,x)))
g=sp.Function('g')(s);w=[g]
for n in range(12):
 lower=sum(sp.binomial(n,k)*((-1)**(k//2+1) if k%2==0 else 0)*w[n-k+2] for k in range(2,n+1))
 nxt=sp.diff(w[n],s)-lower/(c*s);w.append(nxt)
 ck('boundary jet equation '+str(n),c*s*(w[n+1]-sp.diff(w[n],s))+lower)
ck('fourth boundary jet',w[4]-(sp.diff(g,s,4)-4*sp.diff(g,s,3)/(c*s)+sp.diff(g,s,2)/(c*s*s)+3*sp.diff(g,s,2)/(c*c*s*s)))
PV=lambda sig:sp.expand((r*sp.diff(sig,r,2))**2+4*(r*sp.diff(sig,r)-sig)*(r*sp.diff(sig,r)-sig+sp.diff(sig,r)**2))
ck('linear sigma branch',PV(-a*r))
fake=-a*r-8*r*r
res=sp.factor(PV(fake));assert res!=0;checks.append('generic trace with same slope fails PV; residual='+str(res))
z=sp.symbols('z');pair=sp.series((1/(2*sp.pi))**2*(1-(sp.sin(z/2)/(z/2))**2),z,0,6)
checks.append('two-point determinant Taylor series: '+str(pair))
y=sp.symbols('y');ck('double integral constant',sp.integrate(sp.integrate((x-y)**2,(x,0,s)),(y,0,s))-s**4/6)
try:
 import numpy as np
 nodes,weights=np.polynomial.legendre.leggauss(64)
 for gap in [0.2,0.5,1.0]:
  pts=gap*(nodes+1)/2;ws=gap*weights/2;dif=pts[:,None]-pts[None,:]
  kernel=np.sinc(dif/(2*np.pi))/(2*np.pi);B=np.sqrt(ws[:,None])*kernel*np.sqrt(ws[None,:])
  sign,ld=np.linalg.slogdet(np.eye(64)-B);det=sign*np.exp(ld)
  ratio=(det-(1-gap/(2*np.pi)))/gap**4
  checks.append(f'Nystrom 64: gap={gap}, determinant={det:.15g}, quartic ratio={ratio:.12g}, expected limit={1/(576*math.pi**2):.12g}; exponential={math.exp(-gap/(2*math.pi)):.15g}')
except ImportError as e:checks.append('Nystrom skipped: '+str(e))
(p/'checks.txt').write_text('\n'.join(checks)+'\n',encoding='utf8');print('\n'.join(checks))
