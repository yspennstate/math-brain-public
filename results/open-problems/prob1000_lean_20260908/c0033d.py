import numpy as np
rng=np.random.default_rng(11)
def pieces(a,b,c):
    t=c*c
    p00=(1-a)*(1-b)-t; p10=a*(1-b)+t; p01=(1-a)*b+t; p11=a*b-t
    return p00,p10,p01,p11,t
print("Binding direction q=(1,1,a+b).  Need  F := [sum of squares] - 2|L| >= 0.")
print("Also test the STRONGER sufficient form using log(1+z)<=z:  F2 := [sum] - 2t/(p00 p11) >= 0.")
worstF=1e9; worstF2=1e9; wp=None; wp2=None; n=0; nF=0; nF2=0
while n<200000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    p00,p10,p01,p11,t=pieces(a,b,c)
    if min(p00,p10,p01,p11)<=1e-9: continue
    n+=1
    S=(a+b-2)**2/p00 + (1-a-b)**2*(1/p10+1/p01) + (a+b)**2/p11
    absL=np.log(p10*p01/(p00*p11))
    F=S-2*absL
    F2=S-2*t/(p00*p11)
    if F<worstF: worstF=F; wp=(a,b,c)
    if F2<worstF2: worstF2=F2; wp2=(a,b,c)
    if F<0: nF+=1
    if F2<0: nF2+=1
print(f"  n={n}")
print(f"  F  : violations {nF:<5} min {worstF:+.6f} at {tuple(round(v,4) for v in wp)}")
print(f"  F2 : violations {nF2:<5} min {worstF2:+.6f} at {tuple(round(v,4) for v in wp2)}")
print()
print("Sanity: is p10*p01 - p00*p11 == t exactly?")
a,b,c=0.37,0.71,0.23; p00,p10,p01,p11,t=pieces(a,b,c)
print(f"  p10*p01 - p00*p11 = {p10*p01-p00*p11:.12f}   t = c^2 = {t:.12f}")
