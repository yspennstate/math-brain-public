import math, numpy as np
from fei_core import *
lowprio()
g = load_numaro()
sp = Spec.from_table(g)
print("numaro n", sp.n, "H bits", sp.H()/LN2, "I", sp.I(), "H/(I-1)", sp.H()/LN2/(sp.I()-1))
# finite-difference check of dH/dt
for t in [0.0, 0.3, 1.0, 3.0]:
    a = sp.tilt(t); b = sp.tilt(t+1e-6); c = sp.tilt(max(t-1e-6,0))
    fd = -(b['H']-c['H'])/((t+1e-6)-max(t-1e-6,0))
    print("t",t,"mdHdt",a['mdHdt'],"fd",fd, "dlogZ/dt", (b['logZ']-c['logZ'])/((t+1e-6)-max(t-1e-6,0)), "-2E",-2*a['Ek'])
# level-blindness decomposition
W,h = sp.levels()
for t in [0.0, 0.7, 5.0]:
    a = sp.tilt(t)
    pi = W*np.exp(-2*t*np.arange(sp.n+1)); pi/=pi.sum()
    Hpi = -sum(p*math.log(p) for p in pi if p>0)
    print("t",t,"H(q_t)",a['H'],"H(pi)+sum pi h", Hpi+float((pi*h).sum()))
K,R,inf = sp.kkl_split()
print("KKL split nats: K",K,"R",R,"K/I",K/sp.I(),"R/I",R/sp.I(), "H/I nats", sp.H()/sp.I())
for name,f in [("maj11",majority(11)),("bent10",inner_product(5)),("tribes3x4",tribes(3,4)),("addr3",addressing(3))]:
    s=Spec.from_table(f); K,R,_=s.kkl_split()
    print(name,"H/I bits",s.H()/LN2/s.I(),"K/I nats",K/s.I(),"R/I nats",R/s.I())
