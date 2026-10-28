from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json, hashlib, time, shutil
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T015513Z-account03-A082-finite-inequalities'
for d in ('code','out'):(ROOT/d).mkdir(exist_ok=True)
def save(name,obj):
 (ROOT/'out'/name).write_text(json.dumps(obj,indent=2,default=str),encoding='utf-8')
paths=[Path(x['path']) for x in json.loads((OLD/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))]
SRC=Path('agents/A096/runs/20261023T053800Z-account03-A096-live-gap-ledger')
paths += [SRC/x for x in ('REPORT.md','CLAIMS.json','DERIVATION.md')]
paths += [Path('agents/A079/runs/20261023T034945Z-account03-A079-correlated-auxiliaries/PROOF.md')]
receipts=[]
for p in dict.fromkeys(paths):
 raw=p.read_bytes()
 try:raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:raw.decode('cp1252');enc='cp1252'
 receipts.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc))
save('SOURCE_RECEIPTS.json',receipts)
shutil.copyfile(OLD/'code/exact.py',ROOT/'code/exact.py')
spec=dict(helper_version='A082-controller-face-review-v1',family='All physical restrictions of the displayed A079 four-bit controller; all256 labelled three-bit seeds for rational phase identities; selected24 seeds for complete CE ledgers',domain='81 faces, then256*81*3 rational phase cases; ledger seeds0..15,85,90,105,150,165,170,240,255; both signs, all3 seed queries, uniform conditional tail reference, point target at first singleton',case_count='81 faces;62208 rational cases;144 full ledger policies',symmetry='none; duplicate restricted controllers retained',arithmetic='Fraction character transforms, Gram determinants, exact prime-log CE and proved rational log intervals',memory_estimate_mb=100,max_runtime_seconds=55,pilot_max_runtime_seconds=55,bridge='Every physical controller restriction is one of3^4 faces. All-dimensional phase/Pinsker proof reconstructed separately; no finite seed enumeration claimed exhaustive for arbitrary seeds.')
save('FROZEN_SPEC.json',spec)
import exact as e
start=time.monotonic()
N=0
def ck(x):
 global N
 N+=1
 assert x,N
 if N%1000==0:assert time.monotonic()-start<55,'frozen runtime cap'
def ft(f):return tuple(F(sum(v*(-1 if (t&i).bit_count()%2 else 1) for i,v in enumerate(f)),len(f)) for t in range(len(f)))
a0=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
def restrict(pat):
 free=[j for j,v in enumerate(pat) if v==-1]
 return tuple(a0[sum((pat[j] if pat[j]!=-1 else (x>>free.index(j))&1)<<j for j in range(4))] for x in range(1<<len(free)))
faces=[]
for pat in product((-1,0,1),repeat=4):
 a=restrict(pat);b=tuple(1-z*z for z in a);A=ft(a);B=ft(b)
 C=sum((u*u*v*v for u,v in zip(A,B)),F(0));D=sum((u*v**3 for u,v in zip(A,B)),F(0));E=sum((v**4 for v in B),F(0))
 G=C-D*D/E if E else F(0)
 ck(G>=0);ck(sum(u*v for u,v in zip(A,B))==0);ck((G==0)==(C==0))
 faces.append(dict(pattern=pat,a=a,A=A,B=B,C=C,D=D,E=E,Gamma=G,beta=sum(b,F(0))/len(b)))
save('CONTROLLER_FACES.json',faces)
print('faces',len(faces),'positive',sum(z['Gamma']>0 for z in faces),'min',min(z['Gamma'] for z in faces if z['Gamma']>0),flush=True)
root=faces[0];ck(root['Gamma']==F(9,3584))
phase=0
for code in range(256):
 h=tuple(1 if code>>i&1 else -1 for i in range(8));H=ft(h);m=H[0]
 for z in faces:
  for j in range(3):
   d=H[1<<j];A=z['A'];B=z['B'];C=z['C'];D=z['D'];E=z['E'];G=z['Gamma']
   energy=sum((v*v*(u+m*v)**2 for u,v in zip(A,B)),F(0))
   ck(energy==C+2*m*D+m*m*E);ck(energy>=G)
   vp=tuple((u+(m+d)*v)**2 for u,v in zip(A,B));vm=tuple((u+(m-d)*v)**2 for u,v in zip(A,B))
   ck(sum(((p-q)/2)**2 for p,q in zip(vp,vm))==4*d*d*energy)
   phase+=1
def law(A,B,R,m,s):return tuple((u+s*m*v)**2 if t==0 else v*v*R[t] for t in range(len(R)) for u,v in zip(A,B))
def kl(p,q):return e.sub(e.ce(p,q),e.ent(p))
def average(x,y):return e.scale(e.add(x,y),F(1,2))
policies=positive=0
for code in list(range(16))+[85,90,105,150,165,170,240,255]:
 h=tuple(1 if code>>i&1 else -1 for i in range(8));p=e.spectrum(h);m=ft(h)[0];R=e.references(p)[1]
 A=root['A'];B=root['B'];beta=root['beta']
 for s in (-1,1):
  P=law(A,B,p,m,s);Q=law(A,B,R,m,s)
  ck(sum(P)==sum(Q)==1)
  for j in range(3):
   pb=tuple(v for t in range(4) for v in e.marginal(p,j)[t:t+1]) # seed marginal only
   Pbar=tuple(P[t*16+u]+P[(t|(1<<j))*16+u] for t in [e.ins(t,j) for t in range(4)] for u in range(16))
   Qbar=tuple(Q[t*16+u]+Q[(t|(1<<j))*16+u] for t in [e.ins(t,j) for t in range(4)] for u in range(16))
   occ=e.sub(kl(P,Q),kl(Pbar,Qbar));er=e.sub(e.ent(P),e.ent(Pbar))
   x=root['Gamma']*ft(h)[1<<j]**2
   costs=[];refunds=[];charges=[]
   for v in (0,1):
    hc=e.child(h,j,v);pc=e.spectrum(hc);mc=ft(hc)[0];Rc=e.calibrate(e.marginal(R,j),mc*mc)
    Pc=law(A,B,pc,mc,s);Qc=law(A,B,Rc,mc,s)
    refund=e.sub(e.ce(Pc,Qbar),e.ce(Pc,Qc));refunds.append(refund)
    tau=beta*(1-mc*mc);Rn=list(Rc)
    if tau and x:
     eps=x/(tau+x)
     for t in range(1,4):Rn[t]=(1-eps)*Rc[t]+eps*(1-mc*mc)*(t==1)
    Qn=law(A,B,Rn,mc,s);charge=e.sub(e.ce(Pc,Qn),e.ce(Pc,Qc));charges.append(charge)
    if charge and e.interval(charge)[0]>0:positive+=1
    costs.append(e.ce(Pc,Qn));ck(sum(Qn)==1)
   transaction=e.sub(e.add(er,average(*costs)),e.ce(P,Q))
   ck(e.nonpositive(transaction))
   exact=e.add(occ,e.add(transaction,e.sub(average(*refunds),average(*charges))))
   ck(not exact)
   # Independent analytic bound: transaction + D_occ <= -x/ln2.
   form=e.add(transaction,occ)
   ck(not form if not x and not form else e.interval(form)[1] <= -x/e.LN2[1])
   policies+=1
save('VALIDATION.json',dict(status='PASS',faces=81,positive_faces=sum(z['Gamma']>0 for z in faces),minimum_positive_gamma=min(z['Gamma'] for z in faces if z['Gamma']>0),gamma_histogram=dict(Counter(str(z['Gamma']) for z in faces)),rational_phase_cases=phase,complete_ledger_policies=policies,positive_profile_costs=positive,assertions=N,primitive_assertions=e.ASSERTIONS,seconds=time.monotonic()-start))
print(json.dumps(json.loads((ROOT/'out/VALIDATION.json').read_text(encoding='utf-8'))),flush=True)
