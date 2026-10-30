"""A068@2 scoped reconstruction, own code, explicit GL(3,2) group."""
from pathlib import Path
from fractions import Fraction as F
import json,time,math
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(b):
    global checks
    checks+=1;assert b,checks;assert time.perf_counter()-t0<45
def lex(terms):
    out={}
    for c,x in terms:
        for v,sg in [(x.numerator,1),(x.denominator,-1)]:
            j=2
            while j*j<=v:
                while v%j==0:out[j]=out.get(j,F(0))+sg*c;v//=j
                j+=1
            if v>1:out[v]=out.get(v,F(0))+sg*c
    return {p:c for p,c in out.items() if c}
def add(*ls):
    return lex((c,F(p)) for l in ls for p,c in l.items())
def neg(l):return {p:-c for p,c in l.items()}
def ce(p,q):return lex((-v,q[i]) for i,v in enumerate(p) if v)
def dkl(p,q):return lex((v,p[i]/q[i]) for i,v in enumerate(p) if v)
def nonnegative(l):
    den=math.lcm(*(c.denominator for c in l.values())) if l else 1
    num=1;bot=1
    for p,c in l.items():
        e=int(c*den)
        if e>0:num*=p**e
        else:bot*=p**(-e)
    return num>=bot
group=[]
for a in range(1,8):
 for b in range(1,8):
  for c in range(1,8):
   perm=[(a if s&1 else 0)^(b if s&2 else 0)^(c if s&4 else 0) for s in range(8)]
   if len(set(perm))==8:group.append(perm)
ck(len(group)==168)
cases=0
for tt in range(256):
    vals=[1 if tt&(1<<s) else -1 for s in range(8)]
    coeff=[F(sum(vals[s]*(-1)**((s&a).bit_count()%2) for s in range(8)),8) for a in range(8)]
    p=[v*v for v in coeff];mass=1-p[0]
    I=sum(a.bit_count()*p[a] for a in range(8))
    ck(mass<=I)
    for q in [p,[v/2+F(1,16) for v in p],[F(j+1,36) for j in range(8)]]:
        qb=[F(0)]*8
        for perm in group:
            for j in range(8):qb[perm[j]]+=q[j]/168
        ck(qb[0]==q[0]);ck(all(qb[j]==sum(q[1:])/7 for j in range(1,8)))
        invoice=add(ce(p,qb),neg(ce(p,q)))
        if mass:
            pc=[p[j]/mass for j in range(1,8)]
            qc=[q[j]/sum(q[1:]) for j in range(1,8)]
            phi=dkl(pc,[F(1,7)]*7);mismatch=dkl(pc,qc)
            rhs={k:v*mass for k,v in add(phi,neg(mismatch)).items()}
            ck(invoice==rhs);ck(nonnegative(phi));ck(nonnegative(mismatch))
            # log7<3 plus H(pc)>=0 provides Phi<=3 mass<=3 I analytically.
        else:ck(invoice=={})
        # Every actual one-coordinate erasure; projected nonempty shape is invariant.
        for er in range(3):
            marginal=[F(0)]*4
            for label in range(8):
                low=label&((1<<er)-1);high=label>>(er+1)
                marginal[low|(high<<er)]+=qb[label]
            ck(sum(marginal)==1);ck(marginal[1]==marginal[2]==marginal[3])
        cases+=1
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-t0,'actual_functions':256,'reference_cases':cases,'explicit_GL3_elements':168,'arithmetic':'Fraction; direct character sums; explicit group average; prime-log identities and exact integer power signs','review_scope':'A068@2 orbit identity, bounded-block inequality logic, residual marginal shape; Maj5 constants checked by primary independent direct character reconstruction','conflict':'A066 supplied earlier prefix mechanism; no conflict-free full-chain acceptance claimed'}
(R/'out/REVIEW_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
