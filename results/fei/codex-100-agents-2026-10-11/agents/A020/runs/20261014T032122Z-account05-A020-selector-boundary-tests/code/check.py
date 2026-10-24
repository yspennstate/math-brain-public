from pathlib import Path
from fractions import Fraction as Q
import json,time,argparse,importlib.util
R=Path(__file__).resolve().parents[1]
# Reuse only own already checked Walsh/log arithmetic, not another agent's checker.
spec=importlib.util.spec_from_file_location('arith',R.parent/'20261014T002716Z-account05-A020-selector-boundary-tests/code/check.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
def I(v):return a.energy(v)
def p(v):return [Q(t*t,len(v)**2) for t in a.walsh(v)]
def review(m):
    N=1<<m;count=0
    for gm in range(1<<N):
        g=[1-2*((gm>>x)&1) for x in range(N)]
        for em in range(1<<N):
            E=[(em>>x)&1 for x in range(N)];b=[t*(1-2*e) for t,e in zip(g,E)];D=[Q(t*e) for t,e in zip(g,E)]
            pin=pout=Q(0)
            for x in range(N):
                for i in range(m):
                    y=x^(1<<i)
                    if g[x]!=g[y]:
                        if E[x] and E[y]:pin+=Q(1,N)
                        if not E[x] and not E[y]:pout+=Q(1,N)
            J=(I(g)+I(b))/2;kap=I(D)
            assert 2*kap-J==pin-pout;count+=1
    return count
def calibrate(m):
    N=1<<m;rows=[];ln2lo,_=a.logint(2)
    for hm in range(1<<N):
        h=[1-2*((hm>>y)&1) for y in range(N)]
        if sum(h):continue
        for sm in range(16):
            s=[1-2*((sm>>z)&1) for z in range(4)]
            # bit0 z, bit1 w, bit2 x, bits>=3 private h coordinates
            v=[1 if not(t&4) else h[t>>3]*s[t&3] for t in range(1<<(m+3))];pp=p(v);hp=p(h);sp=p(s)
            J=Q(1,2)*(I(h)+1);d=I(s)/2
            assert I(v)==J+d
            assert [a.edges(v,i) for i in [0,1]]==[a.edges(s,i)/2 for i in [0,1]]
            Tprivate=2*sum((pp[t]*(t>>2).bit_count()*(t&3).bit_count() for t in range(len(pp))),Q(0))
            Ezw=sum((pp[t] for t in range(len(pp)) if t&3==3),Q(0))
            T=Tprivate+2*Ezw
            assert Tprivate==(I(h)+Q(1,2))*I(s) and Ezw==sp[3]/2
            # Rowwise erasure exact for root; children w have disjoint sectors.
            B0=a.erasure(pp,0);Bs=a.erasure(sp,0)
            assert B0==(Bs[0]/2,Bs[1]/2)
            inf=a.edges(v,0)
            # All two-bit masks have either absent or equal-weight erasure pairs.
            # Certify equality at the sharp K2 threshold structurally, not by intervals.
            exactB=Q(0)
            for t in range(0,len(pp),2):
                if pp[t] and pp[t|1]:
                    assert pp[t]==pp[t|1];exactB+=pp[t]+pp[t|1]
            assert exactB<=2*inf
            for z in [0,1]:
                child=[v[(t<<1)|z] for t in range(len(v)//2)]
                cp=p(child);assert all(not(cp[t] and cp[t|1]) for t in range(0,len(cp),2))
            # Exact conditional-shared code: known private-row marginal, supplied h reference hp.
            q=[Q(0)]*len(pp)
            for t in range(len(pp)):
                private=t>>2;shared=t&3;y=private>>1
                q[t]=Q(1,4) if y==0 and shared==0 else (hp[y]*sp[shared]/4 if y else Q(0))
            assert q==pp and sum(q)==1
            rows.append(dict(m=m,h_mask=hm,s_mask=sm,Ih=str(I(h)),J=str(J),d=str(d),W=str(Tprivate-2*J),T=str(T),T_over_I=str(T/I(v)),K2_bad_bill='0',reference_normalized=True))
    return rows
def main(pilot):
    start=time.perf_counter();ms=[1] if pilot else [1,2];r=sum(review(m) for m in ms);rows=[]
    for m in ([1] if pilot else [1,2,3]):
        rows+=calibrate(m)
        (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(dict(status='PASS',review_pairs=r,calibration_cases=len(rows),rows=rows,runtime_seconds=time.perf_counter()-start),indent=2))
        assert time.perf_counter()-start<60
    print(json.dumps(dict(status='PASS',review_pairs=r,calibration_cases=len(rows),runtime_seconds=time.perf_counter()-start)))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
