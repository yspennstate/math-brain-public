import itertools,json,time
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1
    assert x
def prod(xs):
    y=F(1)
    for x in xs:y*=x
    return y
def series(x):
    z=(x-1)/(x+1);ck(0<=z<=F(1,3))
    lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
    return lo,lo+2*z**65/F(65)/(1-z*z)
L2=series(F(2))
def ln(x):
    ck(x>=1);k=0
    while x>=2:x/=2;k+=1
    lo,hi=series(x)
    return lo+k*L2[0],hi+k*L2[1]
mask=33152;p=[F(1,2)]*3+[F(1,1024)]
v=[4*t*(1-t) for t in p]
values=[F(1 if mask>>x&1 else -1) for x in range(16)]
ck([x for x in range(16) if values[x]==1]==[7,8,15])
ck(all(any(values[x]!=values[x^(1<<j)] for x in range(16)) for j in range(4)))
blocks=[]
for b in (2,3):
    for B in itertools.combinations(range(4),b):
        C=[j for j in range(4) if j not in B]
        rows={tuple(values[sum(((a>>j)&1)<<B[j] for j in range(b))+
                               sum(((z>>j)&1)<<C[j] for j in range(4-b))]
                    for z in range(2**(4-b))) for a in range(2**b)}
        ck(len(rows)>2)
        blocks.append({'block':[j+1 for j in B],'cofactor_row_count':len(rows)})
mobius=[sum(((-1)**((s^u).bit_count())*values[u] for u in range(16) if u&s==u),F(0)) for s in range(16)]
mass=[];cs=[];Elo=Ehi=F(0);Slo=Shi=F(0)
for s in range(16):
    c=sum((mobius[u]*prod(p[j] for j in range(4) if u>>j&1 and not s>>j&1)
           for u in range(16) if u&s==s),F(0))/2**s.bit_count()
    cs.append(c)
    moment=sum((values[x]*prod(p[j] if x>>j&1 else 1-p[j] for j in range(4))*
                prod(F((x>>j)&1)-p[j] for j in range(4) if s>>j&1) for x in range(16)),F(0))
    direct=moment**2/prod(p[j]*(1-p[j]) for j in range(4) if s>>j&1)
    ck(direct==prod(v[j] for j in range(4) if s>>j&1)*c*c)
    mass.append(direct)
    if s.bit_count()>=2 and direct:
        lo,hi=ln(1/c**2);Elo+=direct*lo;Ehi+=direct*hi
    if s.bit_count()==1 and direct:
        lo,hi=ln(1/c**2);Slo+=direct*lo;Shi+=direct*hi
ck(sum(mass)==1)
delta=sum(((s.bit_count()-1)*mass[s] for s in range(1,16)),F(0))
R=sum(((s.bit_count()-2)*mass[s] for s in range(16) if s.bit_count()>=3),F(0))
L4=ln(F(4))
gaplo=Elo-L4[1]*delta-2*R
gaphi=Ehi-L4[0]*delta-2*R
ck(gaplo>F(13,100))
singleton_slack_lo=4*delta-2*R-Shi
singleton_slack_hi=4*delta-2*R-Slo
total_margin_lo=(4+L4[0])*delta-Ehi-Shi
total_margin_hi=(4+L4[1])*delta-Elo-Slo
ck(total_margin_lo>F(9,20))
out={'helper':'A043-prime-reserve-obstruction-v1','mask':mask,'positive_assignments':[7,8,15],
     'probabilities':[str(t) for t in p],'prime':True,'block_row_counts':blocks,
     'mass':[str(t) for t in mass],'normalized_coefficients':[str(t) for t in cs],
     'delta':str(delta),'reserve_R':str(R),'companion_gap_interval':[str(gaplo),str(gaphi)],
     'certified_gap_lower_bound':'13/100','display_only':[float(gaplo),float(gaphi)],
     'singleton_slack_interval':[str(singleton_slack_lo),str(singleton_slack_hi)],
     'total_Cstar_margin_interval':[str(total_margin_lo),str(total_margin_hi)],
     'certified_total_margin_lower_bound':'9/20',
     'assertions':checks,'runtime_seconds':time.perf_counter()-start,'all_passed':True,
     'false_statement':'For all essential primes and interior product laws E_ge2 <= ln4*delta + 2*sum_{|S|>=3}(|S|-2)P(S)',
     'not_a_refutation':'Neither full FEI nor the sharp ternary bound nor the signed singleton reserve is refuted.'}
(ROOT/'out'/'prime_obstruction.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('mass','normalized_coefficients','companion_gap_interval','block_row_counts','singleton_slack_interval','total_Cstar_margin_interval')}))
