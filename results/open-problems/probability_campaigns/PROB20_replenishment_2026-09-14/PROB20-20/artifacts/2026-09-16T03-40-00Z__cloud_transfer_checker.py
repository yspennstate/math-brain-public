import itertools, math
from functools import lru_cache

pi = {0:0.28,1:0.24,2:0.20,3:0.14,4:0.09,5:0.05}
nu = sum(k*p for k,p in pi.items())
K = 1
N0, M0 = 4, 8
stop_mass = 3

@lru_cache(None)
def configs(N,M):
    keys=tuple(sorted(pi))
    out=[]
    for xs in itertools.product(keys, repeat=N):
        if sum(xs)!=M:
            continue
        w=1.0
        for x in xs:
            w*=pi[x]
        if w>0:
            out.append((xs,w))
    Z=sum(w for _,w in out)
    return tuple((xs,w/Z) for xs,w in out) if Z else tuple()

@lru_cache(None)
def alpha(N,M):
    if M<=0:
        return 0.0
    return sum(prob*sum(x for x in xs if x>K)/M for xs,prob in configs(N,M))

def stopped_cloud_paths():
    records=[]
    states=set()
    for xs,p0 in configs(N0,M0):
        def rec(cur, selected, steps, w):
            if selected>=stop_mass:
                records.append((xs,steps,w,max(xs)))
                return
            N,M=len(cur),sum(cur)
            states.add((N,M))
            a=alpha(N,M)
            if a<=0:
                return
            for i,x in enumerate(cur):
                if x>K:
                    nxt=cur[:i]+cur[i+1:]
                    rec(nxt,selected+x,steps+1,w*(x/M)/a)
        rec(xs,0,0,p0)
    return records,states

records,states=stopped_cloud_paths()
path_total=sum(r[2] for r in records)
a0=min(alpha(*st) for st in states)
print(f"nu={nu:.12f}")
print(f"cloud_path_total={path_total:.15f}")
print(f"encountered_states={sorted(states)}")
print(f"a0={a0:.15f}")
assert abs(path_total-1.0)<1e-12

for threshold in (4,5):
    Qevent=sum(p for xs,p in configs(N0,M0) if max(xs)>=threshold)
    for r in (1,2,3):
        Pcl=sum(w for xs,tau,w,mx in records if tau<=r and mx>=threshold)
        rhs=(a0**(-r))*Qevent
        ok=Pcl<=rhs+1e-12
        print(f"transfer threshold={threshold} r={r}: Pcl={Pcl:.15f} rhs={rhs:.15f} ok={ok}")
        assert ok

eta=0.40
a=nu+eta/2
s0=0.05
cstar=s0*a-nu*(math.exp(s0)-1)
assert cstar>0
print(f"cstar={cstar:.15e}")
for cutoff in range(1,6):
    mgf=sum(p*math.exp((s0/cutoff)*(k if k<=cutoff else 0)) for k,p in pi.items())
    objective=(s0/cutoff)*a-math.log(mgf)
    lower=cstar/cutoff
    ok=objective+1e-14>=lower
    print(f"cramer K={cutoff}: objective={objective:.15e} cstar/K={lower:.15e} ok={ok}")
    assert ok

print("ALL_CHECKS_PASSED")
