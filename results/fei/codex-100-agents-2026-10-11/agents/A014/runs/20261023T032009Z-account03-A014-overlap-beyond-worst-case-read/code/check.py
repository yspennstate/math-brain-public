from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(OLD.read_text(encoding='utf-8').split('rows=[];candidates=0;sets=0;wins=')[0],str(OLD),'exec'),globals())
budget=60 if args.pilot else 300
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def times(a,c):return a[0]*c,a[1]*c
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def entropy(a):return CE(a,a)
def KL(a,b):return minus(CE(a,b),entropy(a))
def spectrum(vals):return [F(a*a,len(vals)**2) for a in walsh(vals)]
def test(vals,q,i,label):
 n=(len(vals)-1).bit_length();N=1<<n;p=spectrum(vals);v=1-p[0];m=p[1<<i];w=v-m
 ck(sum(p)==1 and sum(q)==1 and q[0]==0 and min(q[1:])>0)
 private=[j for j in range(n) if j!=i]
 child=[]
 for bit in (0,1):
  cv=[vals[(bit<<i)+sum(((z>>j)&1)<<u for j,u in enumerate(private))] for z in range(1<<(n-1))]
  child.append(spectrum(cv))
 vs=[1-c[0] for c in child];ck(w==sum(vs)/2)
 I=sum((A.bit_count()*pA for A,pA in enumerate(p)),F(0))
 if not v:
  ck(m==w==I==0);return {'label':label,'query':i,'constant':True}
 qi=q[1<<i];ck(0<qi<1)
 qbar=[F(0)];g=[F(0)];pair=[]
 for T in range(1,1<<(n-1)):
  A=sum(((T>>j)&1)<<u for j,u in enumerate(private));B=A|(1<<i)
  a=p[A]+p[B];ck(a==(child[0][T]+child[1][T])/2)
  g.append(a);qbar.append((q[A]+q[B])/(1-qi));pair.append((A,B,a))
 ck(sum(qbar)==1 and sum(g)==w)
 Q=[1-v]+[v*t for t in q[1:]];Qsym=Q[:]
 for A,B,a in pair:Qsym[A]=Qsym[B]=v*(q[A]+q[B])/2
 ck(sum(Qsym)==1 and Qsym[0]==p[0])
 E=minus(CE(p,Qsym),entropy(p));root=times(KL([m/v,w/v],[qi,1-qi]),v)
 phase=(F(0),F(0))
 for A,B,a in pair:
  if a:
   h=entropy([p[A]/a,p[B]/a]);phase=plus(phase,(a*(1-h[1]),a*(1-h[0])))
 ck(phase[0]>=0 and phase[1]<=w)
 Echildren=[];nonempty=[];Cchildren=[]
 for cp,vb in zip(child,vs):
  qb=[1-vb]+[vb*t for t in qbar[1:]];ck(sum(qb)==1)
  Cchildren.append(CE(cp,qb));Echildren.append(minus(Cchildren[-1],entropy(cp)))
  nonempty.append([a/vb for a in cp[1:]] if vb else None)
 avg=times(plus(*Echildren),F(1,2))
 if w:
  proper=[a/w for a in g[1:]];properdebt=times(KL(proper,qbar[1:]),w)
  hmix=entropy(proper);hav=(F(0),F(0))
  for vb,nb in zip(vs,nonempty):
   if vb:hav=plus(hav,times(entropy(nb),vb/(2*w)))
  js=times(minus(hmix,hav),w)
  ck(overlap(properdebt,minus(avg,js)))
 else:
  ck(vs==[0,0]);properdebt=js=(F(0),F(0))
 rhs=plus(plus(root,phase),minus(avg,js));ck(overlap(E,rhs))
 Qcal=Qsym[:];Qcal[1<<i]=m
 for A,B,a in pair:
  T=sum(((A>>u)&1)<<j for j,u in enumerate(private));Qcal[A]=Qcal[B]=w*qbar[T]/2
 ck(sum(Qcal)==1 and Qcal[0]==p[0] and Qcal[1<<i]==m)
 Ecal=minus(CE(p,Qcal),entropy(p));ck(overlap(Ecal,minus(E,root)))
 gap=(F(0),F(0))
 for A,B,a in pair:
  for U in (A,B):
   if p[U]:gap=plus(gap,times(lg(2*q[U]/(q[A]+q[B])),p[U]))
 ck(overlap(gap,minus(CE(p,Qsym),CE(p,Q))));ck(gap[1]<=w)
 avgC=times(plus(*Cchildren),F(1,2));parentC=CE(p,Q)
 ck(parentC[0]>=avgC[1])
 ck(overlap(Ecal,plus(phase,minus(avg,js))))
 return {'label':label,'query':i,'constant':False,'I':str(I),'v':str(v),'m':str(m),'w':str(w),'root_reference_probability':str(qi),'original_CE':outward(parentC),'sym_CE':outward(CE(p,Qsym)),'calibrated_CE':outward(CE(p,Qcal)),'retained_root_debt':outward(root),'phase_cost':outward(phase),'average_child_debt':outward(avg),'average_FULL_child_CE':outward(avgC),'original_source_debit':outward(minus(parentC,avgC)),'JS_credit':outward(js),'sym_cost_change':outward(gap)}

rows=[];harmonic=[F(0)]+[F(1,A) for A in range(1,8)];z=sum(harmonic);harmonic=[a/z for a in harmonic]
for mask in range(256):
 vals=[1-2*((mask>>z)&1) for z in range(8)]
 for i in range(3):rows.append(test(vals,harmonic,i,{'truth_mask':mask}))
# Same concrete reference as stage17's obstruction, now transported by pairing.
triangle=[1-2*int(z.bit_count()<=1) for z in range(8)]
rs=[F(0),F(5,11)]+[F(1,11)]*6;eps=F(1,2**64)
qt=[F(0)]+[eps if A==2 else (1-eps)*rs[A]/F(10,11) for A in range(1,8)]
witness=test(triangle,qt,0,{'triangle_reference':'epsilon=2^-64'})
ck(F(witness['original_CE'][0])>15);ck(F(witness['sym_CE'][1])<5)
rows.append(witness)
graphs=candidates=sets=0
if not args.pilot:
 for n in (3,4,5):
  universe=list(itertools.combinations(range(n),2))
  for mask in range(1<<len(universe)):
   candidates+=1;edges=[e for j,e in enumerate(universe) if mask&(1<<j)]
   if len(components(n,edges))!=1 or any(len(components(n,edges,i))!=1 for i in range(n)):continue
   lam=F(1,max(sum(u in e for e in edges) for u in range(n)))
   D=(1+lam/4)**len(edges)-1;em=[sum(1<<u for u in e) for e in edges]
   vals=[1-2*int(not any(z&e==e for e in em)) for z in range(1<<n)]
   M=[F(0)]+[occupation(n,edges,A,lam,D) for A in range(1,1<<n)];Z=sum(M)
   ck(0<Z<=1 and min(M[1:])>0);q=[a/Z for a in M]
   for i in range(n):rows.append(test(vals,q,i,{'n':n,'edge_mask':mask,'Z':str(Z)}))
   graphs+=1;sets+=(1<<n)-1
   (R/'out/checkpoint.json').write_text(json.dumps({'graphs':graphs,'queries':len(rows),'assertions':assertions,'elapsed_seconds':time.monotonic()-start}),encoding='utf-8')
# Exact algebra for the all-k majority estimate, without increasing dimension.
for k in range(65):
 ck(4*(k+1)**3-(k+2)*(2*k+1)**2==3*k+2)
 a=F(math.comb(2*k,k),4**k);ck(a*a<=F(1,k+1))
out={'mode':'pilot' if args.pilot else 'full','helper':'A014-paired-reference-transport-v1','truth_tables':256,'boolean_queries':768,'triangle_extra':1,'candidate_graphs':candidates,'graphs':graphs,'graph_queries':len(rows)-769,'graph_nonempty_sets':sets,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'triangle_repair':witness,'rows':rows}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','triangle_repair')}))
