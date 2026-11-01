import importlib.util,json,time,argparse
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('helper',R/'code/check.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter();rows=[]
for m in ([1] if args.pilot else [1,2,3]):
    N=1<<m
    for hm in range(1<<N):
        h=[1-2*((hm>>y)&1) for y in range(N)];beta=Q(sum(h),N);hp=t.p(h)
        v=[1 if not(x&4) else h[x>>3]*(-1)**((x&3).bit_count()) for x in range(1<<(m+3))];pp=t.p(v)
        expected=[Q(0)]*len(pp);expected[0]=expected[4]=Q(1,4)
        for y in range(N):expected[(y<<3)|3]=expected[(y<<3)|7]=hp[y]/4
        assert pp==expected and sum(pp)==1
        assert t.I(v)==(t.I(h)+3)/2
        assert all(not(pp[x] and pp[x|1]) for x in range(0,len(pp),2))
        for z in [0,1]:
            cp=t.p([v[(x<<1)|z] for x in range(len(v)//2)])
            mixed=[]
            for x in range(0,len(cp),2):
                if cp[x] and cp[x|1]:mixed.append((cp[x],cp[x|1]))
            assert mixed==([] if beta==0 else [(Q(1,4),beta*beta/4)]*2)
            assert t.a.edges([v[(x<<1)|z] for x in range(len(v)//2)],0)==Q(1,2)
        rows.append(dict(m=m,h_mask=hm,beta=str(beta),Ih=str(t.I(h)),early_shared_B='0',final_B_formula='(1+beta^2)/2*h2(beta^2/(1+beta^2))<=1',K2_bad_bill='0'))
    assert time.perf_counter()-start<30
    (R/'out'/('PARITY_PILOT.json' if args.pilot else 'PARITY_CORE.json')).write_text(json.dumps(dict(status='PASS',cases=len(rows),rows=rows,runtime_seconds=time.perf_counter()-start),indent=2))
print(json.dumps(dict(status='PASS',cases=len(rows),runtime_seconds=time.perf_counter()-start)))
