"""Independent assembly of (4): zero seed atoms and full edit support."""
from pathlib import Path
from fractions import Fraction as F
import json
from check_reference import walsh, chi, ent, phi, log, add, mul, ce
root=Path(__file__).resolve().parents[1]; checks=0; cases=0
for b in [[1,-1,-1,1],[1,1,1,-1],[-1]+[1]*7]:
    N=len(b); k=N.bit_length()-1; d=F(1,N); Pb=[x*x for x in walsh(b)]
    for refsmooth in [F(0),F(1,2)]:
        Q=[(1-refsmooth)*d+refsmooth*p for p in Pb]
        ell=[mul(-1,log(q)) for q in Q]
        K=[mul(d,add(*(mul(chi(s,u),ell[s]) for s in range(N)))) for u in range(N)]
        for mode in range(4):
            # q=N; modes include no edits, full edits, globally correlated,
            # and cycling events with complementary/overlapping fibers.
            A=[[0 if mode==0 else 1 if mode==1 else (z&1) if mode==2 else int((v+z)%3==0) for z in range(4)] for v in range(N)]
            fs=[[b[x]*(1-2*A[x][z]) for x in range(N)] for z in range(4)]
            fh=[walsh(f) for f in fs]
            joint=[[u*u for u in walsh([fh[z][s] for z in range(4)])] for s in range(N)]
            R=[sum(joint[s][t] for s in range(N)) for t in range(4)]
            PX=[sum(row) for row in joint]
            ah=[walsh([1-2*a for a in row]) for row in A]
            mu=[row[0] for row in ah]; V=d*sum(1-m*m for m in mu)
            assert R[0]==1-V; checks+=1
            mix={}
            for t in range(1,4):
                assert R[t]==d*sum(row[t]**2 for row in ah); checks+=1
                if R[t]: mix=add(mix,mul(R[t],ent([d*row[t]**2/R[t] for row in ah])))
            KL=add(*(mul(joint[s][t],add(log(joint[s][t]),mul(-1,log(Q[s]*R[t])))) for s in range(N) for t in range(4) if joint[s][t]))
            cut={}
            for z in range(4):
                cut=add(cut,*(mul(-d*b[x]*b[y],K[x^y]) for x in range(N) for y in range(N) if A[x][z] and not A[y][z]))
            assert add(ce(PX,Q),mul(-1,ce(Pb,Q)))==cut; checks+=1
            rhs=add(ce(Pb,Q),mul(d,add(*(ent([u*u for u in row]) for row in ah))),
                    mul(k*V,log(F(2))),phi(1-V),mul(-d,add(*(phi(m*m) for m in mu))),cut,mul(-1,mix),mul(-1,KL))
            assert ent([u for row in joint for u in row])==rhs; checks+=1; cases+=1
result={'status':'PASS','cases':cases,'assertions':checks,'arithmetic':'exact rational prime-log identities',
        'domain':'parity2 (zero seed atoms), bent2, point3; uniform/half-seed positive references; q=N full-support edits; zero/all/correlated/cycling events; V=0 and V=1 included'}
(root/'out/endpoint_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8'); print(json.dumps(result))
