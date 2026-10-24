import pathlib,json
import mpmath as mp
import sympy as sp
BASE=pathlib.Path(__file__).resolve().parent
z=sp.symbols('z'); s=sp.symbols('s'); v,c3,c4,c5=sp.symbols('v c3 c4 c5')
identity=sp.factor((1-3*z)-(1-6*z)*(1+z)**3-z**2*(15+17*z+6*z**2))
uc=-c3*s/2+(c5-6*v*c3)*s**2/8
classical=sp.series(-uc-s*(c3-3*v*uc-uc**3)/2+s**2*(c5-5*c4*uc+10*c3*uc**2-10*v*uc**3-uc**5)/8,s,0,3)
u=-2*c3*s+(3*c5-14*v*c3)*s**2
r=1-v*s+(c4-v**2)*s**2
q3=u**3+3*v*u-c3
q5=u**5+10*v*u**3-10*c3*u**2+5*c4*u-c5
station=sp.series(u-2*s*q3/r+3*s**2*q5/r**2,s,0,3)
mode=sp.series(u+u/r-s*q3/r**2+s**2*q5/r**3,s,0,3)
out={'exact_identity_residual':str(identity),'classical_stationarity_residual':str(classical),'free_stationarity_residual':str(station),'free_mode_series':str(mode),'atomic':[]}
mp.mp.dps=65
laws=[([-1,2],[mp.mpf(2)/3,mp.mpf(1)/3]),([-4,0,1,10],[mp.mpf('0.01'),mp.mpf('0.4'),mp.mpf('0.58'),mp.mpf('0.01')]),([-2,2],[mp.mpf('.5'),mp.mpf('.5')])]
for xs,ps in laws:
 m=sum(p*x for x,p in zip(xs,ps)); ys=[mp.mpf(x)-m for x in xs]
 moments={k:sum(p*y**k for y,p in zip(ys,ps)) for k in range(2,8)}
 vv=moments[2]; a3=moments[3]; a5=moments[5]
 for mult in [100,300,1000]:
  t=mp.mpf(mult)*max(1,vv)
  hc=mp.findroot(lambda h:sum(p*(y-h)*mp.exp(-(y-h)**2/(2*t)) for y,p in zip(ys,ps)),(-a3/(2*t),mp.mpf(0)))
  fu,rr=mp.findroot(lambda u,R:(sum(p/(R+(u-y)**2) for y,p in zip(ys,ps))-1/t,sum(p*(u-y)/(R+(u-y)**2)**2 for y,p in zip(ys,ps))),(-2*a3/t,t-vv))
  mf=fu+t*sum(p*(fu-y)/(rr+(fu-y)**2) for y,p in zip(ys,ps))
  pc=-a3/(2*t)+(a5-6*vv*a3)/(8*t**2)
  pf=-3*a3/t+(5*a5-22*vv*a3)/t**2
  out['atomic'].append({'xs':xs,'t':str(t),'classical_mode_centered':str(hc),'free_mode_centered':str(mf),'classical_error_times_t3':str((hc-pc)*t**3),'free_error_times_t3':str((mf-pf)*t**3),'R':str(rr)})
(BASE/'independent_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
