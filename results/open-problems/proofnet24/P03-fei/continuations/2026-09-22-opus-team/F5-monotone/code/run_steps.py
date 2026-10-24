import sys, numpy as np
from step_analysis import analyse, psi_bound_constant
print("psi constant sup_t [psi(t,1)-log2(1+t^2)], argmax, 3/ln2:", psi_bound_constant())
rng = np.random.default_rng(7)
fams = []
n = 16
fams.append(("maj17",np.ones(17),0.0))
for k in [2,4,6]:
    fams.append(("sym16 k=%d"%k, np.ones(16), 16-2*k+1.0))
fams.append(("w=1..16 mid", np.arange(1,17,dtype=float), 0.5))
fams.append(("w=1..16 top", np.arange(1,17,dtype=float), 120.5))
fib=[1,1];
while len(fib)<16: fib.append(fib[-1]+fib[-2])
fams.append(("fib16 mid", np.array(fib,float), 0.5))
fams.append(("fib16 q", np.array(fib,float), 1000.5))
fams.append(("heavy K=4 + 15 ones", np.array([4.0]+[1.0]*15), 0.5))
fams.append(("heavy K=4 + 15 ones th=6", np.array([4.0]+[1.0]*15), 6.5))
fams.append(("heavy K=8 + 15 ones th=4", np.array([8.0]+[1.0]*15), 4.5))
fams.append(("two heavy 6,6 + 14 ones th=3", np.array([6.,6.]+[1.0]*14), 3.5))
for t in range(8):
    w = np.abs(rng.standard_normal(16)); th = rng.standard_normal()*np.linalg.norm(w)*0.8
    fams.append(("gauss%d"%t, w, th))
for t in range(4):
    w = rng.exponential(size=16)**2; th = rng.standard_normal()*np.linalg.norm(w)
    fams.append(("heavytail%d"%t, w, th))
print("%-30s %6s %8s %8s | %7s %7s %7s %7s | %7s %7s"%("name","p","H","I","dH/Inf heavy","light","max","min","lvlbd heavy","slog heavy"))
for name,w,th in fams:
    H,I,st,p = analyse(w,th)
    order = np.argsort(-np.asarray(w))
    ratio = st[:,0]/np.maximum(st[:,1],1e-300)
    rel = st[:,1]>1e-12
    hv = order[0]; lt = [i for i in order[::-1] if rel[i]][0]
    lv = (4.328+st[hv,3]/st[hv,1])
    print("%-30s %6.3f %8.4f %8.4f | %7.3f %7.3f %7.3f %7.3f | %7.3f %7.3f   H/I=%.3f"%(name,p,H,I,ratio[hv],ratio[lt],ratio[rel].max(),ratio[rel].min(), lv, st[hv,2]/st[hv,1], H/I))
