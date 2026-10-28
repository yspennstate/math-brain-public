"""Fixed no-core physical witness. Independent direct-character arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
run=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1;assert x
    assert time.perf_counter()-start<55
def characters(v):
    return tuple(Q(sum(z*(-1 if (s&i).bit_count()%2 else 1) for i,z in enumerate(v)),len(v)) for s in range(len(v)))
def sp(v):return tuple(x*x for x in characters(v))
def edge(v,i):return Q(sum(z!=v[k^(1<<i)] for k,z in enumerate(v)),len(v))
def restrict(v,i,a):return tuple(z for k,z in enumerate(v) if k>>i&1==a)
maj=tuple(1 if y.bit_count()<=1 else -1 for y in range(8))
f=tuple((-1 if (t+x)%2 else 1)*maj[y] for y in range(8) for x in range(2) for t in range(2))
pf=sp(f);W=(1,2,4,7)
ck(sum(pf)==1);ck(tuple(i for i,p in enumerate(pf) if p)==tuple(3+4*j for j in W));ck(sum(edge(f,i) for i in range(5))==Q(7,2))
children=[restrict(f,0,s) for s in [0,1]]
leaves=[restrict(g,0,s) for g in children for s in [0,1]]
for g in children:
 a=characters(g);ck(edge(g,0)==1);ck(a[1]==0);ck(all(a[k]*a[k+1]==0 for k in range(0,len(a),2)))
for g in leaves:ck(sp(g)==sp(maj));ck(sum(edge(g,i) for i in range(3))==Q(3,2))
rows=[]
for K in range(4,33):
 eps=Q(1,1<<(3*K));heavy=1-3*eps
 ck(Q(1,2)<heavy<1)
 # c=9K/4 + log2(1/heavy)/4, so 9K/4<c<(9K+1)/4.
 # Prove every needed bank bound by rational coefficients after 0<log<1.
 lower_old=Q(K,4)-Q(1,2);upper_raw=-Q(3*K,4)-Q(1,4)
 mid=Q(5*K,2)-Q(9,4);final=Q(3*K,2)-Q(9,4)
 ck(lower_old>0);ck(upper_raw<0);ck(mid>0);ck(final>=Q(15,4))
 ck(Q(2)-Q(5*K,4)<=-3);ck(mid-K==final)
 A=tuple((2 if j&1 else 0)^(4 if j&2 else 0)^(7 if j&4 else 0) for j in range(8))
 # Independent brute orbit generation on the FOUR actual frequency labels.
 q={j:heavy if j==1 else eps for j in W};orbit=[];current=q
 for turn in range(4):orbit.append(current);current={A[j]:v for j,v in current.items()}
 ck(current==q)
 avg={j:sum(z.get(j,Q(0)) for z in orbit)/4 for j in W}
 ck(all(v==Q(1,4) for v in avg.values()));ck(sum(avg.values())==1)
 # No actual reference mass discarded: the uniformized complete cost is2.
 ck(sum(q.values())==1)
 rows.append({'K':K,'epsilon':str(eps),'old_bank_strict_lower':str(lower_old),'raw_bank_strict_upper':str(upper_raw),'prequery_after_orbit_bank':str(mid),'final_original_bank':str(final)})
out={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'domain':'fixed five-bit physical truth table, BOTH prefix children and FOUR terminals; K=4..32 rational coefficient/orbit certificates; universal K argument in DERIVATION','rows':rows,'formal':'NO_COMPILER_OR_FORMAL_CERTIFICATE'}
(run/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
