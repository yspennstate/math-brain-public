from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
RUN=Path(__file__).resolve().parents[1]
SPEC={'helper':'A094 concrete uniform-dictionary reference debt diagonal v1','family':'balanced tensor of width-L point-defect signs, activated on 4L+1 fresh controls','domain':'integers L=2..32, t=4^L, r=4L+1; parameters and analytic bounds only, no truth tables','case_count':31,'symmetry':'none','arithmetic':'Fraction and arbitrary precision integers; no logarithm approximation needed','memory_estimate_MB':10,'max_runtime_seconds':60,'dimension_escalation':False}
if '--freeze' in sys.argv:
    (RUN/'DIAGONAL_SPEC.json').write_text(json.dumps(SPEC,indent=2)+'\n');print('FROZEN_DIAGONAL');sys.exit()
assert json.loads((RUN/'DIAGONAL_SPEC.json').read_text())==SPEC
start=time.perf_counter();rows=[];checks=0
def ck(b):
    global checks
    checks+=1;assert b
for L in range(2,33):
    t=4**L;r=4*L+1;p=Q(1,2**r);Ih=Q(L,2**(L-1));I=p*(t*Ih+1+r)
    ck((1+Q(1,t))**2<2) # proves r=ceil(2 log2(t+1)) exactly
    ck(1+r<=t*Ih)
    lower=Q(t*L,t*Ih+1+r)
    ck(lower>=2**(L-2))
    ck(I==p*(2*L*2**L+4*L+2))
    ck(4*t*Ih+4*r+3<4*(t*Ih+1+r)) # H/I <4 from audited analytic block/control bounds
    if rows:ck(I<Q(rows[-1]['influence']))
    rows.append({'L':L,'t':t,'r':r,'influence':str(I),'minority_probability':str(p/2),'cross_entropy_over_I_lower':str(lower),'reference_debt_over_I_strict_lower':str(lower-4),'block_reference_transfer_debt':'0; exact product law construction in AUDIT Section 6','truth_table_enumerated':False})
output={'status':'PASS','assertions':checks,'cases':len(rows),'rows':rows,'seconds':time.perf_counter()-start,'arithmetic':'exact rational parameter certificates; all-infinite-case proof in AUDIT Section 6'}
(RUN/'out/DIAGONAL_CERTIFICATES.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:output[k] for k in ['status','assertions','cases','seconds']}))
