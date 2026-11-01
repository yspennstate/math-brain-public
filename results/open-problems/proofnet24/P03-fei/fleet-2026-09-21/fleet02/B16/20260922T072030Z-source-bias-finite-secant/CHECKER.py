#!/usr/bin/env python3
"""B16 exact source-side finite-bias reduction for the n=18 FEI source gate.

This does NOT evaluate the unavailable current f4 potential bytes. It reconstructs
the source gate, reduces its biased Fourier entropy exactly to ten 9-bit transforms,
and evaluates the source-side threshold at u=1/5000 at high precision.
"""
from hashlib import sha256
import mpmath as mp
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [(TOP,BOT),(TOP,"fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),(TOP,"fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00","fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),(TOP,"fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),(TOP,"fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00",BOT),("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00",BOT),("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00",BOT),("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00",BOT)]
def source_data():
    base=int("".join(SLICES[0]),16); masks=[int("".join(r),16)^base for r in SLICES[1:]]; seen=base; pairs=[]
    for m in masks:
        assert not(seen&m) and m.bit_count()==2; seen|=m; pairs.append(tuple(x for x in range(512) if (m>>x)&1))
    f0=[-1 if (base>>x)&1 else 1 for x in range(512)]
    for P in pairs:
        for x in P: assert f0[x]==1
    signed=[]
    for hm in range(512):
        for x in range(512):
            val=f0[x]
            for j,P in enumerate(pairs):
                if x in P and ((hm>>j)&1): val=-1; break
            signed.append(val)
    assert sha256(",".join(map(str,signed)).encode()).hexdigest()==EXPECTED_SHA and sum(signed)==0
    g0=list(f0)
    for P in pairs:
        for x in P: g0[x]=0
    gs=[g0]
    for P in pairs:
        g=[0]*512
        for x in P: g[x]=-1
        gs.append(g)
    return pairs,gs
def core_transform(h,u,dps):
    mp.mp.dps=dps; p=mp.mpf("0.5")+u; q=1-p; r=mp.sqrt(p*q); a=[mp.mpf(v) for v in h]; step=1
    while step<512:
        for b in range(0,512,2*step):
            lo=a[b:b+step]; hi=a[b+step:b+2*step]
            for j in range(step):
                x0,x1=lo[j],hi[j]; a[b+j]=q*x0+p*x1; a[b+step+j]=r*(x1-x0)
        step*=2
    return a
def entropy_reduced(gs,u,dps):
    mp.mp.dps=dps; H=mp.mpf("0"); mass=mp.mpf("0"); ln2=mp.log(2)
    for g in gs:
        for c in core_transform(g,u,dps):
            w=c*c; mass+=w
            if w: H-=w*mp.log(w)/ln2
    return H,mass
def dc(u): return mp.mpf(513)/256-mp.mpf(315)/16*u**2+mp.mpf(495)/8*u**4-63*u**6+9*u**8
def dh(u): return 9*(mp.mpf(1)/4-u**2)**4
def pout(u): return mp.mpf(1)/2+mp.mpf(513)/256*u-mp.mpf(105)/16*u**3+mp.mpf(99)/8*u**5-9*u**7+u**9
def h2(x): return -(x*mp.log(x)+(1-x)*mp.log(1-x))/mp.log(2) if x not in (0,1) else mp.mpf(0)
def calc(dps):
    mp.mp.dps=dps; pairs,gs=source_data(); u=mp.mpf(1)/5000; H0,M0=entropy_reduced(gs,mp.mpf(0),dps); Hu,Mu=entropy_reduced(gs,u,dps)
    C=mp.mpf("6.5218512"); C0=mp.mpf("6.4548"); a=mp.mpf("0.2682048"); d=dc(u); e=dh(u); delta=pout(u)-mp.mpf("0.5")
    leaf=d*h2(1-4*u*u); D0=C*mp.mpf(133)/128-H0; total=-D0-leaf+(Hu-H0); s1=mp.mpf("0.5")-u; so=mp.mpf("0.5")-delta
    Q=d*s1*(1-s1)+e/4-so*(1-so); dq=a*(Q-mp.mpf(133)/512); base=total-dq; coeff=(d+e-1)-mp.mpf(133)/128; rho=d*u/delta; tau=(base-coeff*C0)/delta
    L=mp.mpf(67383)/8192*u*u*mp.log(1/u**2)/mp.log(2); reg=leaf-(Hu-H0)+L
    return dict(pairs=pairs,H0=H0,Hu=Hu,M0=M0,Mu=Mu,dc=d,dh=e,delta=delta,leaf=leaf,D0=D0,lead=L,source_regular=reg,total_threshold=total,delta_quad=dq,base_threshold=base,coeffC=coeff,rho=rho,tau=tau)
def main():
    r80=calc(80); r=calc(120)
    for k in ("H0","Hu","total_threshold","delta_quad","base_threshold","rho","tau"): assert mp.nstr(r80[k],50)==mp.nstr(r[k],50)
    assert r["M0"]==1 and abs(r["Mu"]-1)<mp.mpf("1e-110")
    print("STATUS PASS"); print("SOURCE_SHA",EXPECTED_SHA); print("PAIRS",r["pairs"])
    for k in ("H0","Hu","dc","dh","delta","leaf","D0","lead","source_regular","total_threshold","delta_quad","base_threshold","coeffC","rho","tau"): print(k,mp.nstr(r[k],65))
    print("INTERPRETATION"); print("For q(t)=(C0-Gamma0(1/2-t))/t, t>0, the source gate at u=1/5000 falsifies the stable candidate iff"); print("q(delta) - rho*q(u) < tau, with rho,tau printed above."); print("No current f4 candidate bytes are evaluated by this checker.")
if __name__=="__main__": main()
