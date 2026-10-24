from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,hashlib
import arithmetic as A
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 if time.perf_counter()-start>58:raise RuntimeError('Frozen pilot watchdog')
A.log=lru_cache(None)(A.log)
@lru_cache(None)
def ent(p):return A.entropy(p)
def H(p):return ent(tuple(sorted(x for x in p if x)))
def sub(a,b):return A.add(a,A.mul(-1,b))
def phi(a,b):return sub(H((a,b)),H((a+b,)))
@lru_cache(None)
def spectrum(t):
 a=tuple(A.walsh(t));return a,tuple(v*v for v in a)
def nbits(t):return len(t).bit_length()-1
def slice_(t,i,bit):return tuple(t[x] for x in range(len(t)) if (x>>i&1)==bit)
@lru_cache(None)
def influences(t):return tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(nbits(t)))
def totalI(t):return sum(influences(t),Q(0))
def row(p,i):return tuple((p[s],p[s|(1<<i)]) for s in range(len(p)) if not s>>i&1)
def Bi(p,i):return A.add(*(phi(a,b) for a,b in row(p,i)))
def Mi(p,i):return A.add(*(A.mul(b,A.log((a+b)/b)) for a,b in row(p,i) if b))
def Ci(p,i):return A.add(*(A.mul(a,A.log((a+b)/a)) for a,b in row(p,i) if a))
def KL(mu,r):
 ck(sum(mu)==1);ck(sum(r)==1)
 return A.add(*(A.mul(m,A.log(m/q)) for m,q in zip(mu,r) if m))
def auditrow(p,i):
 e=sum(b for a,b in row(p,i));b=Bi(p,i);m=Mi(p,i);c=Ci(p,i)
 ck(b==A.add(m,c))
 if e:
  rr=tuple(a+b0 for a,b0 in row(p,i));mu=tuple(b0/e for a,b0 in row(p,i))
  d=KL(mu,rr);ck(m==A.mul(e,sub(A.log(1/e),d)))
 return e,b,m,c
def paritylift(t,J):
 # Physical replacement, independently evaluated rather than spectrum relabeling.
 labels=[];pos=0
 for i in range(nbits(t)):
  labels.append((pos,pos+1) if i in J else (pos,));pos+=2 if i in J else 1
 values=tuple(t[sum((sum((x>>j)&1 for j in slots)%2)<<i for i,slots in enumerate(labels))] for x in range(1<<pos))
 return values,labels
seeds=[];paritycases=0
for n in range(4):
 for mask in range(1<<(1<<n)):
  t=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));_,p=spectrum(t);es=influences(t)
  ck(tuple(sum(p[s] for s in range(len(p)) if s>>i&1) for i in range(n))==es)
  seedM=A.add(*(Mi(p,i) for i in range(n)))
  for i in range(n):auditrow(p,i)
  for jm in range(1<<n):
   J=[i for i in range(n) if jm>>i&1];lift,labels=paritylift(t,J);_,lp=spectrum(lift);le=influences(lift)
   ck(H(lp)==H(p));ck(totalI(lift)==totalI(t)+sum((es[i] for i in J),Q(0)))
   ck(A.add(*(Mi(lp,j) for j in range(nbits(lift))))==sub(seedM,A.add(*(Mi(p,i) for i in J))))
   for i in J:
    u,v=labels[i];ck(le[u]==es[i]);ck(le[v]==es[i]);ck(not Mi(lp,u) and not Bi(lp,u))
    if not es[i]:continue
    # Marginalization implemented on expanded actual lifted row, retaining all other coordinates.
    keep=[j for j in range(nbits(lift)) if j not in (u,v)];rr={};mm={}
    for s in range(len(lp)):
     if s>>u&1:continue
     key=sum(((s>>j)&1)<<a for a,j in enumerate(keep))
     rr[key]=rr.get(key,Q(0))+lp[s]+lp[s|(1<<u)]
     mm[key]=mm.get(key,Q(0))+lp[s|(1<<u)]/es[i]
    coarseD=KL(tuple(mm[k] for k in sorted(rr)),tuple(rr[k] for k in sorted(rr)))
    originalD=sub(A.log(1/es[i]),A.mul(1/es[i],Mi(p,i)))
    ck(coarseD==originalD)
    ck(A.mul(es[i],sub(A.log(1/es[i]),coarseD))==Mi(p,i))
    # Opposite binary quotient keeps partner occupancy with full derivative-free reference atom.
    binaryr=[Q(0),Q(0)];binarymu=[Q(0),Q(0)]
    for s in range(len(lp)):
     if not s>>u&1:
      bit=(s>>v)&1;binaryr[bit]+=lp[s]+lp[s|(1<<u)];binarymu[bit]+=lp[s|(1<<u)]/es[i]
    ck(binaryr==[1-es[i],es[i]]);ck(binarymu==[0,1]);ck(KL(binarymu,binaryr)==A.log(1/es[i]))
   paritycases+=1
  seeds.append((n,mask,t))
(R/'out/PARITY_REVIEW.json').write_text(json.dumps({'status':'PASS','seeds':len(seeds),'partial_parity_cases':paritycases,'assertions_so_far':checks},indent=2)+'\n',encoding='utf-8')
print('PARITY_PASS',checks,flush=True)
maj=(1,1,1,-1,1,-1,-1,-1)
def encoderwalk(outer,i,h,policy,branch=0):
 # Outer distinguished-bit children after physical partner query; composed rest kept actual.
 n=nbits(outer);restplus=slice_(outer,i,0);restminus=slice_(outer,i,1);delta=influences(outer)[i]
 def compose(h):return tuple((restplus if h[x&((1<<nbits(h))-1)]==1 else restminus)[x>>nbits(h)] for x in range(1<<(nbits(h)+n-1)))
 F=compose(h);_,fp=spectrum(F);_,hp=spectrum(h)
 if len(h)==1:return {'Q':{},'inner':{},'spent':Q(0),'leafH':H(fp),'leafI':totalI(F)}
 j=0 if policy=='forward' or h[0]>0 else nbits(h)-1
 gamma=spectrum(h)[0][1<<j];seedB=Bi(spectrum(outer)[1],i)
 values=[encoderwalk(outer,i,slice_(h,j,z),policy,branch*2+z) for z in (0,1)]
 out={}
 for key in ('Q','inner','leafH'):out[key]=A.mul(Q(1,2),A.add(*(v[key] for v in values)))
 for key in ('spent','leafI'):out[key]=sum(v[key] for v in values)/2
 out['Q']=A.add(out['Q'],A.mul(gamma*gamma,seedB));out['inner']=A.add(out['inner'],A.mul(delta,Bi(hp,j)))
 out['spent']+=influences(F)[j]
 ck(influences(F)[j]==delta*influences(h)[j])
 ck(totalI(F)==out['leafI']+out['spent'])
 return out
unlockcases=0;records=[]
selected=[z for z in seeds if z[0] in (1,2) or z[0]==3 and z[1] in [0,1,7,15,105,150,232,255]]
for n,mask,t in selected:
 _,p=spectrum(t)
 for i in range(n):
  delta,B,M,C=auditrow(p,i);gplus=slice_(t,i,0);gminus=slice_(t,i,1)
  avgH=A.mul(Q(1,2),A.add(H(spectrum(gplus)[1]),H(spectrum(gminus)[1])))
  JS=sub(sub(H(p),avgH),B);deficit=sub({2:2*totalI(t)},H(p))
  T2=sub({2:2*(totalI(t)-delta)},avgH)
  shadowmargin=sub(T2,A.add(B,{2:delta}));klmargin=sub(T2,A.add(M,{2:delta}))
  ck(shadowmargin==A.add(deficit,JS,{2:-3*delta}))
  ck(klmargin==A.add(shadowmargin,C))
  # Original parity pair, independent physical partner followed by Maj3 encoder.
  slots=[j for j in range(n) if j!=i]
  F=[]
  for x in range(1<<(n+3)):
   h=maj[x&7];u=1 if not x>>3&1 else -1;rest=x>>4
   y=(0 if h*u==1 else 1)<<i
   y+=sum(((rest>>j)&1)<<coordinate for j,coordinate in enumerate(slots));F.append(t[y])
  F=tuple(F);_,pf=spectrum(F)
  ck(H(pf)==A.add(H(p),{2:2*delta}));ck(totalI(F)==totalI(t)+Q(3,2)*delta)
  ck(not Bi(pf,3));ck(influences(F)[3]==delta)
  for policy in ('forward','adaptive_reverse'):
   # Partner signs correspond to original outer and z-reflected outer, both checked physically.
   reflected=tuple(t[x^(1<<i)] for x in range(len(t)))
   tree1=encoderwalk(t,i,maj,policy);tree2=encoderwalk(reflected,i,maj,policy)
   for tr in (tree1,tree2):
    ck(tr['Q']==B);ck(tr['inner']==({2:delta} if delta else {}));ck(tr['spent']==Q(3,2)*delta)
   ck(A.mul(Q(1,2),A.add(tree1['leafH'],tree2['leafH']))==avgH)
   ck((tree1['leafI']+tree2['leafI'])/2==totalI(t)-delta)
  if n==2 and mask==1 and i==0:
   ck(delta==Q(1,2));ck(B=={2:Q(1)});ck(M=={2:Q(1,2)});ck(C=={2:Q(1,2)})
   ck(T2=={2:Q(1)});ck(shadowmargin=={2:Q(-1,2)});ck(not klmargin)
   records.append({'witness':'AND2 sign one positive atom; distinguished coordinate 0','delta':str(delta),'B':'1','M':'1/2','C_up':'1/2','terminal_S2':'1','inherited_Maj3_bill':'1/2','shadow_margin':'-1/2','KL_margin':'0','both_actual_terminal_children':'constant and dictator, entropy 0, K2-certified'})
  unlockcases+=1
(R/'out/TERMINAL_WITNESS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('UNLOCK_PASS',checks,flush=True)
bent=[]
for d in (2,4,6,8):
 delta=Q(1,1<<d)
 b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(d//2)) for x in range(1<<d))
 g=tuple(b[x>>1] if x>>1 else (1 if not x&1 else -1) for x in range(1<<(d+1)))
 _,gp=spectrum(g);e,B,M,C=auditrow(gp,0);ck(e==delta)
 marginlow=sub(M,{2:delta*(d-1)});marginhigh=sub({2:delta*d},M)
 ck(not marginlow or A.bounds(marginlow)[0]>=0);ck(not marginhigh or A.bounds(marginhigh)[0]>=0)
 G,labels=paritylift(g,[0]);ck(totalI(G)==Q(d,2)+(d+2)*delta)
 ck(A.bounds(sub({2:3*totalI(G)},H(spectrum(G)[1])))[0]>=0)
 leafH=A.mul(Q(1,2),A.add(H(spectrum(b)[1]),H(spectrum(tuple(-1 if x==0 else b[x] for x in range(len(b))))[1])))
 T2=sub({2:d+2*d*delta},leafH);margin=sub(T2,A.add(B,{2:delta}))
 if d>=4:ck(A.bounds(margin)[0]>0)
 bent.append({'d':d,'delta':str(delta),'M_log_form':{str(k):str(v) for k,v in M.items()},'B_log_form':{str(k):str(v) for k,v in B.items()},'terminal_margin_log_form':{str(k):str(v) for k,v in margin.items()}})
(R/'out/BENT_CONTROLS.json').write_text(json.dumps(bent,indent=2)+'\n',encoding='utf-8')
ck(paritycases==2122);ck(unlockcases==60)
result={'helper_version':'A004-KL-shadow-owner-v1','status':'PASS','assertions':checks,'seeds':len(seeds),'partial_parity_substitutions':paritycases,'unlocking_compositions':unlockcases,'unlocking_trees':2*unlockcases,'partner_child_encoder_walks':4*unlockcases,'bent_controls':len(bent),'runtime_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256((R/'code/arithmetic.py').read_bytes()).hexdigest()}
(R/'out/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result),flush=True)
