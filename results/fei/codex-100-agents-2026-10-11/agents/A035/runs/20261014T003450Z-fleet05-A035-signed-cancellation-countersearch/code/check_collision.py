from pathlib import Path
import sys,time,json,itertools
import kernel as k
from fractions import Fraction as Q
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
k.CAP=50 if PILOT else 180
start=time.perf_counter();checks=0
module=[k.bent(a&15,4)*(-1 if (a&15)==0 and (a>>4)&1 else 1) for a in range(32)]
beta=k.split(module,4)['B'];Hp=k.entropy_table([k.bent(x,4)*(-1 if x==0 else 1) for x in range(16)])
def parts(m,L,y0,fixed):
 ys=1<<m;J=[j for j in range(L) if j not in fixed];D=1<<(4*len(fixed)+5*len(J))
 cp=[];cm=[]
 for y in range(ys):
  a=(-1 if y.bit_count()%2 else 1)*(-1 if y==y0 else 1);b=k.bent(y,m)
  cp.append(b if a==1 else 0);cm.append(b if a==-1 else 0)
 G=[];T=[];labels=[]
 for j in range(L):labels.extend([(j,'x',i) for i in range(4)]+([] if j in fixed else [(j,'z',0)]))
 for v in range(D):
  off=0;g=t=1
  for j in range(L):
   x=(v>>off)&15;off+=4
   z=fixed[j] if j in fixed else (v>>off)&1
   if j not in fixed:off+=1
   b=k.bent(x,4);g*=b;t*=b*(-1 if x==0 and z else 1)
  G.append(g);T.append(t)
 f=[cp[y]*G[v]+cm[y]*T[v] for v in range(D) for y in range(ys)]
 return cp,cm,G,T,f,labels
def hist_entropy(hist,den):
 out=(Q(0),Q(0))
 for v,count in hist.items():out=k.add(out,k.mul(k.ent(Q(v,den)),count))
 return out
cases=[(2,1,y) for y in (0,1,3)] if PILOT else list(itertools.product((2,4,6),(1,2),(0,1,3)))
records=[]
for m,L,y0 in cases:
 k.clock();e=Q(1,1<<m);a0=(-1 if y0.bit_count()%2 else 1);p=Q(1,2)+a0*e
 cp,cm,G,T,f,labels=parts(m,L,y0,{})
 a,I=k.spectrumI(f);assert I==k.influence(f);checks+=1
 # Core derivative averaged over data: adjacent bent and controller cuts.
 tminus=(1-Q(15,16)**L)/2
 expectedI=Q(m,2)-2*e*tminus*(m-2*y0.bit_count())+L*(Q(2)+Q(5,16)*p)
 assert I==expectedI;checks+=1
 H=k.entropy_table(f)
 terminalI=L*(Q(2)+p*Q(1,4))
 terminalH=k.mul(k.add((Q(4),Q(4)),k.mul(k.sub(Hp,(Q(4),Q(4))),p/2)),L)
 assert terminalH[1]<=2*terminalI;checks+=1
 contexts=[]
 for j in range(L):
  for history in range(1<<j):
   fixed={h:(history>>h)&1 for h in range(j)}
   cp,cm,G,T,f,labels=parts(m,L,y0,fixed)
   i=m+labels.index((j,'z',0));row=k.split(f,i)
   expectedW=Q(1,16)*(4*p+Q(m,2)*(1-2*e))
   assert row['d']==p/16 and row['W']==expectedW;checks+=2
   # Independently assemble coherent and incoherent branch Fourier masses.
   ca,cb=k.fwht(cp),k.fwht(cm);ga,gb=k.fwht(G),k.fwht(T);N=len(f);D=len(G);ys=1<<m
   ff=k.fwht(f)
   assert all(ff[s+ys*t]==ca[s]*ga[t]+cb[s]*gb[t] for s in range(ys) for t in range(D));checks+=1
   assert all(ff[s] for s in range(N) if s&(1<<i));checks+=1
   assert sum(ff[s]*ff[s^(1<<i)] for s in range(N) if not s&(1<<i))==0;checks+=1
   slot=i-m;barhist=Counter();Bbar=(Q(0),Q(0));BH=(Q(0),Q(0));Pbar=[];latent_H=(Q(0),Q(0))
   pairs=Counter()
   for s in range(ys):
    for t in range(D):
     mass=ca[s]**2*ga[t]**2+cb[s]**2*gb[t]**2
     Pbar.append(mass);barhist[mass]+=1
    for t in range(D):
     if t&(1<<slot):continue
     u=ca[s]**2*ga[t]**2+cb[s]**2*gb[t]**2
     v=ca[s]**2*ga[t^(1<<slot)]**2+cb[s]**2*gb[t^(1<<slot)]**2
     pairs[u,v]+=1
   assert sum(Pbar)==N*N;checks+=1
   for (u,v),count in pairs.items():Bbar=k.add(Bbar,k.mul(k.phi(Q(u,N*N),Q(v,N*N)),count))
   ideal=k.mul(beta,p);ambiguity=k.sub(Bbar,ideal);signed=k.sub(row['B'],Bbar);delta=k.sub(row['B'],ideal)
   assert ambiguity[1]>=0;checks+=1
   contexts.append(dict(j=j,history=history,d=str(row['d']),W=str(row['W']),B=k.emit(row['B']),ideal=k.emit(ideal),Bbar=k.emit(Bbar),ambiguity=k.emit(ambiguity),signed_interference=k.emit(signed),total_correction=k.emit(delta),coherent_pairs={str(pair):c for pair,c in Counter(zip((x*x for x in k.fwht([(x+y)//2 for x,y in zip(k.restrict(f,i,0),k.restrict(f,i,1))])),(x*x for x in k.fwht([(x-y)//2 for x,y in zip(k.restrict(f,i,0),k.restrict(f,i,1))])))).items()},incoherent_pairs={str(pair):c for pair,c in pairs.items()},denominator=N*N))
   contexts[-1]['rho']='1';contexts[-1]['within_carrier_credit']=k.emit(row['M'])
 rec=dict(m=m,L=L,y0=y0,n=m+5*L,p=str(p),I=str(I),H=k.emit(H),terminal_I=str(terminalI),terminal_H=k.emit(terminalH),contexts=contexts)
 records.append(rec)
 with (ROOT/'out'/('pilot.jsonl' if PILOT else 'cases.jsonl')).open('a',encoding='utf8') as out:out.write(json.dumps(rec)+'\n')
result=dict(helper_version='A035-collision-v2-outward-rounded',runtime_seconds=time.perf_counter()-start,root_count=len(records),context_count=sum(len(r['contexts']) for r in records),checks=checks+k.checks,beta=k.emit(beta),records=records)
for r in records:
 for c in r['contexts']:
  c['incoherent_denominator']=c.pop('denominator')
  c['coherent_denominator']=c['incoherent_denominator']//4
(ROOT/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({key:value for key,value in result.items() if key!='records'}))
for r in records:
 print(r['m'],r['L'],r['y0'],[(v['j'],v['history'],v['total_correction'],v['signed_interference']) for v in r['contexts']])
