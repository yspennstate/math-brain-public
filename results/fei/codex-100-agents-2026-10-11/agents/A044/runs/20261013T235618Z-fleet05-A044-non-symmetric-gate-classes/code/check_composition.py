from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import math_helper as M
import time,json
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();cases={'composition':0,'constant_selector':0,'constant_data':0,'majority':0,'parity_mux':0}
def gate(kind,x):
    if kind=='AND2':return Q(1 if all(x) else -1)
    if kind=='OR2':return Q(1 if any(x) else -1)
    if kind=='XOR2':return Q(1 if sum(x)%2 else -1)
def mux(z,y0,y1):return y1 if z==1 else y0
def values(kind):return {x:gate(kind,x) for x in product([0,1],repeat=2)}
profiles=[list(map(Q,['1/4','3/4','1/4','3/4','1/4','3/4'])),list(map(Q,['1/8','1/2','3/4','1/4','7/8','1/2']))]
types=['AND2','OR2','XOR2']
def expect(vals,bs):return sum((f*M.prod(q if bit else 1-q for bit,q in zip(x,bs)) for x,f in vals.items()),Q(0))
for bs in profiles:
  for kinds in product(types,repeat=3):
    children=[values(k) for k in kinds]
    Ps=[M.spectrum(c,bs[2*i:2*i+2]) for i,c in enumerate(children)]
    Es=[M.ent(Ps[i],bs[2*i:2*i+2]) for i in range(3)]
    mus=[expect(children[i],bs[2*i:2*i+2]) for i in range(3)]
    vs=[1-m*m for m in mus];rs=[(1+m)/2 for m in mus]
    outer={x:mux(2*x[0]-1,2*x[1]-1,2*x[2]-1) for x in product([0,1],repeat=3)}
    PO=M.spectrum(outer,rs);EO=M.ent(PO,rs)
    alphas=[sum((p for mask,p in enumerate(PO) if mask>>i&1),Q(0))/vs[i] for i in range(3)]
    F={x:mux(children[0][x[:2]],children[1][x[2:4]],children[2][x[4:]]) for x in product([0,1],repeat=6)}
    PF=M.spectrum(F,bs);EF=M.ent(PF,bs)
    M.check(EF==M.combine((Q(1),EO),*((a,e) for a,e in zip(alphas,Es))))
    M.check(M.delta(PF)==M.delta(PO)+sum((a*M.delta(p) for a,p in zip(alphas,Ps)),Q(0)))
    margin={};M.addlog(margin,2*M.delta(PF),Q(2));margin=M.combine((Q(1),margin),(-Q(1),EF))
    M.check(M.interval(margin,4*M.delta(PF))[0]>0)
    cases['composition']+=1
  for const,k0,k1 in product([-1,1],types,types):
    chosen=values(k1 if const==1 else k0);offset=4 if const==1 else 2
    F={x:mux(Q(const),gate(k0,x[2:4]),gate(k1,x[4:])) for x in product([0,1],repeat=6)}
    PF=M.spectrum(F,bs);PC=M.spectrum(chosen,bs[offset:offset+2])
    M.check(M.ent(PF,bs)==M.ent(PC,bs[offset:offset+2]));M.check(M.delta(PF)==M.delta(PC))
    cases['constant_selector']+=1
  for kind,c0,c1 in product(types,[-1,1],[-1,1]):
    F={x:mux(gate(kind,x[:2]),Q(c0),Q(c1)) for x in product([0,1],repeat=6)}
    PF=M.spectrum(F,bs)
    if c0==c1:M.check(M.ent(PF,bs)=={});M.check(M.delta(PF)==0)
    else:
      PC=M.spectrum(values(kind),bs[:2]);M.check(M.ent(PF,bs)==M.ent(PC,bs[:2]));M.check(M.delta(PF)==M.delta(PC))
    cases['constant_data']+=1
# Independent scoped audit of A042 majority main inequality, not its boundary error theorem.
for bs in product([Q(1,4),Q(1,2),Q(3,4)],repeat=3):
    vals={x:Q(1 if sum(x)>=2 else -1) for x in product([0,1],repeat=3)}
    P=M.spectrum(vals,bs);v=[4*q*(1-q) for q in bs];T=M.prod(v)/4
    M.check(P[7]==T)
    B=sum((p for s,p in enumerate(P) if s.bit_count()==2),Q(0));D=M.delta(P)
    M.check(D==B+2*T)
    E=M.ent(P,bs);margin={};M.addlog(margin,2*(D-T),Q(2));margin=M.combine((Q(1),margin),(-Q(1),E))
    # (4+ln4)D-(ln4-1)T-E =4D+T+2(D-T)ln2-E.
    M.check(M.interval(margin,4*D+T)[0]>0)
    cases['majority']+=1
parityqs=[list(map(Q,x)) for x in [('1/8','1/4','1/2'),('1/8','3/4','7/8'),('1/2','1/2','1/2'),('1/16','1/16','1/16')]]
for qs in parityqs:
  for m0,m1 in [(Q(-1,2),Q(1,2)),(Q(-3,4),Q(7,8))]:
    bs=qs+[(1+m0)/2,(1+m1)/2]
    bvals={x:Q(1 if sum(x)%2 else -1) for x in product([0,1],repeat=3)}
    PB=M.spectrum(bvals,qs);EB=M.ent(PB,qs);muB=expect(bvals,qs);qB=(1+muB)/2;beta=(1-m0*m1)/2
    F={x:mux(bvals[x[:3]],Q(2*x[3]-1),Q(2*x[4]-1)) for x in product([0,1],repeat=5)}
    PF=M.spectrum(F,bs);EF=M.ent(PF,bs)
    outer={x:mux(2*x[0]-1,2*x[1]-1,2*x[2]-1) for x in product([0,1],repeat=3)}
    PO=M.spectrum(outer,[qB,(1+m0)/2,(1+m1)/2]);EO=M.ent(PO,[qB,(1+m0)/2,(1+m1)/2])
    M.check(EF==M.combine((Q(1),EO),(beta,EB)))
    M.check(M.delta(PF)==M.delta(PO)+beta*M.delta(PB))
    M.check(M.interval(M.combine((-Q(1),EB)),2*M.delta(PB))[0]>0)
    margin={};M.addlog(margin,2*M.delta(PF),Q(2));margin=M.combine((Q(1),margin),(-Q(1),EF))
    M.check(M.interval(margin,4*M.delta(PF))[0]>0);cases['parity_mux']+=1
M.check(sum(cases.values())==149)
lo,hi=M.LN2;Klo=2+Q(4)/hi;Khi=2+Q(4)/lo
scale=10**12
result={'helper_version':'A044-mux-composition-v3.1','result':'PASS','cases':cases,'total_cases':sum(cases.values()),'exact_assertions':M.checks,'runtime_seconds':time.perf_counter()-start,'constant_lower_10e12':str(Q((Klo*scale).numerator//(Klo*scale).denominator,scale)),'constant_upper_10e12':str(Q(-((-Khi*scale).numerator//(-Khi*scale).denominator),scale)),'majority_review_scope':'main inequality only; not independent-rate error and boundary theorem'}
(ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
