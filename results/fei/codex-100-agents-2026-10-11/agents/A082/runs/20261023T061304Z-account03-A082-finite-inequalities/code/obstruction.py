from pathlib import Path
from fractions import Fraction as F
import json,time
import exact as e
ROOT=Path(__file__).resolve().parents[1]
def save(n,x):(ROOT/'out'/n).write_text(json.dumps(x,indent=2,default=str),encoding='utf-8')
save('OBSTRUCTION_FROZEN_SPEC.json',dict(helper_version='A082-parity-block-v1',family='actual parity on k=2,3,4 seed bits with original A079 controller',domain='each seed query and both physical outcomes; full exact incoming spectrum; conditional tail mixture63/64 old point+1/64 other nonempty point',case_count=18,symmetry='none',arithmetic='Fraction and exact prime-log forms',memory_estimate_mb=50,max_runtime_seconds=10,pilot_max_runtime_seconds=10,bridge='analytic parity character identity proves all k>=2; finite tests only validate implementation'))
start=time.monotonic();rows=[]
face=json.loads((ROOT/'out/CONTROLLER_FACES.json').read_text(encoding='utf-8'))[0]
A=tuple(map(F,face['A']));B=tuple(map(F,face['B']));beta=F(face['beta'])
def law(p):return tuple(u*u if t==0 else v*v*p[t] for t in range(len(p)) for u,v in zip(A,B))
for k in (2,3,4):
 h=tuple((-1)**i.bit_count() for i in range(1<<k));p=e.spectrum(h);P=law(p)
 for j in range(k):
  M=tuple(P[e.ins(t,j)*16+u]+P[(e.ins(t,j)|(1<<j))*16+u] for t in range(1<<(k-1)) for u in range(16))
  e.ck(not e.sub(e.ent(P),e.ent(M)))
  for v in (0,1):
   pc=e.spectrum(e.child(h,j,v));Pc=law(pc);e.ck(M==Pc)
   # For k=2 the child has one nonempty frequency: no distinct target exists.
   if k==2:rows.append(dict(k=k,j=j,outcome=v,zero_refund=True,distinct_nonempty_target=False));continue
   q=list(pc);q[-1]=F(63,64);q[1]=F(1,64);Q=law(q)
   charge=e.sub(e.ce(Pc,Q),e.ent(Pc));expected=e.scale(e.logform(F(64,63)),beta)
   e.ck(charge==expected);e.ck(e.interval(charge)[0]>0)
   rows.append(dict(k=k,j=j,outcome=v,zero_refund=True,distinct_nonempty_target=True,charge=e.serial_form(charge)))
faces=json.loads((ROOT/'out/CONTROLLER_FACES.json').read_text(encoding='utf-8'))
zero=[z for z in faces if F(z['Gamma'])==0 and F(z['E'])>0]
emin=min(F(z['E']) for z in zero)
save('OBSTRUCTION.json',dict(status='PASS',rows=rows,assertions=e.ASSERTIONS,seconds=time.monotonic()-start,zero_gamma_nonzero_tail_faces=len(zero),minimum_E_on_these_faces=emin))
print('PASS',len(rows),'physical outcomes;',e.ASSERTIONS,'assertions; min E',emin)
