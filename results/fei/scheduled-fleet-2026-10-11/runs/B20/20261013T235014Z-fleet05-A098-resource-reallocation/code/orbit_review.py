from pathlib import Path
from fractions import Fraction as F
from math import comb
import json, time, sys

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
start=time.perf_counter(); checks=0
def check(value):
    global checks
    checks+=1
    assert value, checks
    assert time.perf_counter()-start<55, 'Frozen runtime exceeded'
def save(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def pairs(items):
    if not items:
        yield ()
    else:
        first=items[0]
        for other in items[1:]:
            rest=tuple(x for x in items if x not in (first,other))
            for tail in pairs(rest): yield ((first,other),)+tail
def spectrum(blocks):
    truth=[-1 if any(all(x>>i&1 for i in b) for b in blocks) else 1 for x in range(256)]
    a=truth[:]; step=1
    while step<256:
        for j in range(0,256,2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step]; a[k],a[k+step]=u+v,u-v
        step*=2
    p=[F(v*v,256**2) for v in a]
    check(sum(p)==1)
    for i in range(8):
        physical=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(256)),256)
        spectral=sum(p[s] for s in range(256) if s>>i&1)
        check(physical==spectral==F(27,128))
    # Direct character sum for every coefficient, independent of FWHT layout.
    for s in range(256):
        direct=sum(truth[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(256))
        check(direct==a[s])
    return p

pilot='pilot' in sys.argv
orbit=list(pairs(tuple(range(8))))
check(len(orbit)==105 and len(set(orbit))==105)
ps=[]
with (OUT/('ORBIT_PILOT.jsonl' if pilot else 'ORBIT_CASES.jsonl')).open('w',encoding='utf-8') as log:
    for blocks in orbit[:1] if pilot else orbit:
        ps.append(spectrum(blocks))
        log.write(json.dumps({'blocks':blocks,'influence_each':'27/128','spectrum_physical_check':'PASS'})+'\n');log.flush()
if not pilot:
    average=[sum(p[s] for p in ps)/105 for s in range(256)]
    degree=[sum(average[s] for s in range(256) if s.bit_count()==d) for d in range(9)]
    check(sum(degree)==1)
    for s in range(256): check(average[s]==degree[s.bit_count()]/comb(8,s.bit_count()))
    # Exact symbolic CE(p_pi, average) = H(average): each degree pays same log atom.
    for p in ps:
        for d in range(9):
            check(sum(p[s] for s in range(256) if s.bit_count()==d)==degree[d])
    save('ORBIT_AVERAGE.json',{'orbit_count':105,'degree_mass':[str(v) for v in degree],
        'reference_atom_by_degree':[str(degree[d]/comb(8,d)) for d in range(9)],
        'exact_symbolic_CE_equality':'CE(P_pi,barP)=H(barP) for every orbit element',
        'minimax':'inf_complete_subprobability_Q max_pi CE(P_pi,Q)=H(barP)',
        'influence':'27/16'})
    rows=[]
    with (OUT/'SYMBOLIC_CASES.jsonl').open('w',encoding='utf-8') as log:
        for w in [2,3,4,6,8,10,12]:
            k=2**w; n=k*w; delta=F(1,k)
            a=(1-delta)**(2*(k-1))
            high=sum(comb(w,m) for m in range((w+1)//2,w+1))
            mass=4*k*delta**2*a*high
            I=2*w*(1-delta)**(k-1)
            check(high>=2**(w-1));check(a>=F(1,9));check(mass>=F(2,9));check(I<=2*w)
            for m in range((w+1)//2,w+1):
                # binom(n,m) >= (n/m)^m >= k^m >= 2^(w^2/2).
                check(comb(n,m)*m**m>=n**m)
                check(n>=k*m);check(2*w*m>=w*w)
            check(F(w*w,9)/(2*w)==F(w,18))
            row={'w':w,'k':k,'n':n,'high_degree_one_block_mass_ge':'2/9',
                 'entropy_orbit_lower_bound_bits':str(F(w*w,9)),
                 'influence_upper_bound':2*w,'CE_over_I_lower_bound':str(F(w,18)),
                 'exact_integer_power_and_binomial_checks':'PASS'}
            rows.append(row);log.write(json.dumps(row)+'\n');log.flush()
    save('SYMBOLIC_SUMMARY.json',rows)
save('ORBIT_PILOT_SUMMARY.json' if pilot else 'ORBIT_REVIEW_CHECK.json',
     {'status':'PASS','orbit_cases':len(ps),'symbolic_cases':0 if pilot else 7,
      'assertions':checks,'runtime_seconds':time.perf_counter()-start,
      'arithmetic':'integers/Fraction; no numerical entropy estimates',
      'source_helper_imported':False,'memory_estimate_mb':60})
print(json.dumps({'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start}))
