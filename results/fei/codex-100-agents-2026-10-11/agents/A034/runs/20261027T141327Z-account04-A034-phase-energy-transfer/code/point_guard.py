from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,time
R=Path(__file__).resolve().parents[1];start=time.monotonic()
sp=importlib.util.spec_from_file_location('stage22',R/'code/check.py');h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
v=[1-2*(x*(y&1)*(y>>1&1)) for y in range(4) for x in range(2)]
W=h.old.walsh(v)
assert sorted(Q(w*w,64) for w in W)==[Q(1,16)]*7+[Q(9,16)]
iy=sum(h.old.influences(v)[1:]);assert iy==Q(1,2)
rows=[[1,1,1,0],[0,0,0,1]]
assert [Q(sum(x*x for x in u),4) for u in rows]==[Q(3,4),Q(1,4)]
ws=[h.old.walsh(u) for u in rows]
assert all(W[k]==2*ws[k&1][k>>1] for k in range(8))
assert sum(sum(h.old.influences(u)) for u in rows)==iy
B=h.bill(v);assert B[1]<=8*iy
lo=hi=Q(0)
for mass in [Q(3,4),Q(1,4)]:
    a,b=h.old.logint(1/mass);lo+=mass*a;hi+=mass*b
assert 0<B[0]-hi and B[1]-lo<=4*iy
assert time.monotonic()-start<5
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='')
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
save(R/'out/point_defect_guard.json',dict(status='PASS',cases=1,mathematical_checks=8,seconds=time.monotonic()-start,block='X1,Y2; M2,d1',IY='1/2',full_spectrum='9/16 and seven1/16',conditional='full H minus h2(1/4), positive; rate4',full_rate=8,helper_sha256=sha(Path(__file__))))
sentence='The three-bit point defect is admitted by two phase cells; its nontrivial conditional entropy is retained.'
replacement='For the three-bit point defect use X=(x), Y=(y1,y2), F=(-1)^(x*y1*y2). The cells y1=0,1 have affine label maps0,y2, so M=2,d=1. The row masses are3/4,1/4 and I_Y=1/2. The full squared spectrum is9/16 and seven copies1/16, and the positive conditional entropy is exactly full H minus h2(1/4). This specifies the physical split; no arbitrary one-coordinate conditional-law admission is inferred.'
proof=R/'PROOF.md';t=proof.read_text(encoding='utf-8')
assert sentence in t or replacement in t
proof.write_text(t.replace(sentence,replacement),encoding='utf-8',newline='')
report=R/'REPORT.md';t=report.read_text(encoding='utf-8')
note='A separately frozen fixed X1,Y2 point-defect guard checks the actual full Walsh spectrum, both row masses, SAME IY=1/2, full rate8 and the positive conditional entropy at rate4 (out/point_defect_guard.json). Its eight fixed checks are additional to the main-job assertion count.'
if note not in t:t=t.replace('## proof dependencies and changed downstream conclusions',note+'\n\n## proof dependencies and changed downstream conclusions')
t=t.replace('Total 39,187 exact assertions PASS.','Main jobs: 39,187 exact assertions PASS.')
report.write_text(t,encoding='utf-8',newline='')
p=load(R/'PROGRESS.json')
for f in ['FROZEN_GUARD.json','code/point_guard.py','out/point_defect_guard.json']:
    if f not in p['source_artifacts']:p['source_artifacts'].append(f)
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
validation=load(R/'out/protocol_validation.json');validation['fixed_point_defect_guard']='PASS: eight additional checks';save(R/'out/protocol_validation.json',validation)
files=[f for f in R.rglob('*') if f.is_file() and f.name!='artifact_receipts.json']
assert all(f.stat().st_size<20_000_000 for f in files)
save(R/'out/artifact_receipts.json',[dict(path=str(f.relative_to(R)),bytes=f.stat().st_size,sha256=sha(f)) for f in files])
assert all(sha(R/x['path'])==x['sha256'] for x in load(R/'out/artifact_receipts.json'))
print(json.dumps(dict(status='FINAL_VERIFIED_LOCAL',main_assertions=39187,additional_point_checks=8,files=len(files)+1,full_fei='OPEN',review='PENDING',lean='NOT_STARTED_MEMOK_HOLD')))
