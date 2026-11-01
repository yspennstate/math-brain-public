"""Gauged identity H = H_inf + 2 int_0^inf Cov_{q_t^U}(|S xor U|, log 1/w) dt on Numaro's g and on Maj_13,
and the small-delta expansion of the thinned law H(S_delta)/(delta I) -> log(1/delta) + 1 + sum_i (Inf_i/I) log(1/Inf_i)."""
import math, numpy as np
from fei_core import *
lowprio()
out=[]
for name,f in [("Numaro g", load_numaro()), ("Maj13", majority(13)), ("tribes 3x5", tribes(3,5))]:
    sp=Spec.from_table(f); w=sp.w; n=sp.n; N=1<<n
    U=int(w.argmax()); d=popcounts(n)[np.arange(N)^U].astype(float)
    pos=w>0; L=np.zeros(N); L[pos]=-np.log(w[pos])
    ts=np.concatenate([np.linspace(0,1,2001),np.linspace(1.0005,30,20000)])
    vals=[]
    for t in ts:
        u=np.where(pos,w*np.exp(-2*t*d),0); q=u/u.sum(); Ed=(q*d).sum(); EL=(q*L).sum()
        vals.append(2*(q*(d-Ed)*(L-EL)).sum())
    integ=np.trapezoid(vals,ts); H=sp.H(); Hinf=-math.log(w.max())
    out.append("%-10s H=%.10f H_inf=%.10f H-H_inf=%.10f 2intCov=%.10f  (H_inf/I=%.5f, (H-H_inf)/I=%.5f nats)"%(name,H,Hinf,H-Hinf,integ,Hinf/sp.I(),(H-Hinf)/sp.I()))
# thinning expansion check (exact thinned law) on Maj9 and tribes 2x3
for name,f in [("Maj9",majority(9)),("tribes2x3",tribes(2,3))]:
    sp=Spec.from_table(f); n=sp.n; N=1<<n; w=sp.w; I=sp.I(); inf=sp.influences()
    Hloc=float(sum((x/I)*math.log(1/x) for x in inf if x>0))
    # nu(T) = sum_{S superset T} w(S) via superset-sum transform
    nu=w.copy()
    for i in range(n):
        idx=np.arange(N); sel=((idx>>i)&1)==0
        nu[sel]+=nu[idx[sel]|(1<<i)]
    pc=popcounts(n)
    for delta in [1e-2,1e-3,1e-4]:
        # P_delta(T) = sum_{S sup T} w(S) delta^|T| (1-delta)^{|S|-|T|}: use w_tilde(S)=w(S)(1-delta)^{|S|} then superset sum
        wt=w*(1-delta)**pc
        P=wt.copy()
        for i in range(n):
            idx=np.arange(N); sel=((idx>>i)&1)==0
            P[sel]+=P[idx[sel]|(1<<i)]
        P=P*(delta/(1-delta))**pc
        Hd=float(-(P[P>0]*np.log(P[P>0])).sum())
        out.append("%-9s delta=%g  H(S_d)/(dI)=%.5f  log(1/d)+1+H_loc=%.5f  (H_loc=%.5f, sum P=%.12f)"%(name,delta,Hd/(delta*I),math.log(1/delta)+1+Hloc,Hloc,P.sum()))
txt='\n'.join(out); print(txt); open('../logs/gauged_and_thinning.log','w').write(txt+'\n')
