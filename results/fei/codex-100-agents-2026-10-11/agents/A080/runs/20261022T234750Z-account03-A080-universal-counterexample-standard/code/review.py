from exact import *
from pathlib import Path
from itertools import product
import time,argparse
R=Path(__file__).resolve().parents[1];ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
negative={0,1,2,4,8,16,32,6,17,40};h=[-1 if x in negative else 1 for x in range(64)];J=[-h[x^1] for x in range(64)];W=walsh(J)
g=[-1 if x in {0,1,2} else 1 for x in range(64)]
def core(tab):
 w=walsh(tab);sq=[x*x for x in w];I=sum(i.bit_count()*sq[i] for i in range(len(sq)))
 for j in range((len(tab)).bit_length()-1):ck(Q(sum(tab[x]!=tab[x^(1<<j)] for x in range(len(tab))),len(tab))==sum(sq[s] for s in range(len(sq)) if s>>j&1))
 return {'mean':w[0],'var':1-w[0]**2,'I':I,'H':ent_counts(Counter(sq)),'nonempty':Counter(x for x in sq[1:] if x),'dimension':len(tab).bit_length()-1}
def composed(cores):
 means=[c['mean'] for c in cores];variances=[c['var'] for c in cores];P={};mass_counts=Counter();Qocc=[Q(0)]*6
 for B in range(64):
  ids=[i for i in range(6) if B>>i&1]
  if any(not variances[i] for i in ids):continue
  L=Q(0)
  for T in range(64):
   if T&B!=B:continue
   v=W[T]
   for j in range(6):
    if (T^B)>>j&1:v*=means[j]
   L+=v
  PB=L*L
  for i in ids:PB*=variances[i]
  P[B]=PB
  for i in ids:Qocc[i]+=PB/variances[i]
  if not L:continue
  choices=[list(cores[i]['nonempty'].items()) for i in ids]
  for cat in product(*choices):
   mass=L*L;cnt=1
   for amp,multiplicity in cat:mass*=amp;cnt*=multiplicity
   mass_counts[mass]+=cnt
 ck(sum(P.values())==1);ck(sum(v*c for v,c in mass_counts.items())==1)
 qdirect=[]
 for i in range(6):
  q=Q(0)
  for z in range(64):
   if z>>i&1:continue
   if J[z]==J[z|(1<<i)]:continue
   pr=Q(1)
   for j in range(6):
    if j!=i:pr*=(1-means[j])/2 if z>>j&1 else (1+means[j])/2
   q+=pr
  qdirect.append(q)
  if variances[i]:ck(q==Qocc[i])
 I=sum(qdirect[i]*cores[i]['I'] for i in range(6))
 ck(I==sum(Qocc[i]*cores[i]['I'] for i in range(6)))
 H=ent_counts(mass_counts)
 occupancy=ent(P.values())
 for i,c in enumerate(cores):occupancy=add(occupancy,scale(qdirect[i],sub(c['H'],h2(c['var']))))
 ck(overlap(H,occupancy))
 return H,I,sub((4*I,4*I),H)
states=[];negative_rows=[]
domain=[(0,(0,0)),(1,(0,0))] if args.pilot else list(product([0,1],product([None,0,1],repeat=2)))
for b,state in domain:
 free=[i for i,x in enumerate(state) if x is None];tab=[]
 for x in range(1<<len(free)):
  vals=list(state)
  for j,i in enumerate(free):vals[i]=(x>>j)&1
  tab.append(-1 if vals==[0,0] else 1)
 gb=[-1 if ((x<<1)|b) in {0,1,2} else 1 for x in range(32)]
 cores=[core(tab),core(gb)]+[core(g) for _ in range(4)]
 H,I,S=composed(cores);ck(I>0)
 row={'b':b,'state':state,'H':H,'I':I,'S4':S,'ambient_dimension':sum(c['dimension'] for c in cores)}
 if state==(0,0):
  low,high=(Q(-56,1000),Q(-55,1000)) if b==0 else (Q(-46,1000),Q(-45,1000))
  ck(low<S[0] and S[1]<high);negative_rows.append(row)
 else:ck(S[0]>0)
 states.append(row)
dump(R/'out'/('REVIEW_PILOT_STATES.json' if args.pilot else 'REVIEW_STATES.json'),states)
allocations=0
for s0,s1,w in product([Q(-2),Q(-1),Q(0),Q(1),Q(2)],[Q(-2),Q(-1),Q(0),Q(1),Q(2)],[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]):
 ss=[s0,s1];ws=[w,1-w];P=sum(ws[i]*max(ss[i],0) for i in range(2));N=sum(ws[i]*max(-ss[i],0) for i in range(2));mean=P-N
 if mean<0:continue
 for T in sorted({Q(0),mean/2,mean}):
  if P:
   ker=[max(s,0)/P for s in ss];d=[T*x for x in ker];flow=[max(-ss[i],0)-N*ker[i] for i in range(2)]
  else:ker=[Q(1),Q(1)];d=[Q(0),Q(0)];flow=[Q(0),Q(0)]
  ck(sum(ws[i]*d[i] for i in range(2))==T);ck(sum(ws[i]*flow[i] for i in range(2))==0)
  ck(sum(ws[i]*max(flow[i],0) for i in range(2))==N)
  for i in range(2):
   if ws[i]:ck(d[i]>=0 and ss[i]+flow[i]-d[i]>=0)
  # A genuinely signed old label is carried without division by T.
  L=Q(-3,2);ck(sum(ws[i]*L*ker[i] for i in range(2))==L)
  allocations+=1
# Nonnegative-net-debit hypothesis is essential.
s=[Q(-1),Q(1)];d=s;flow=[Q(0),Q(0)];weights=[Q(1,2),Q(1,2)]
ck(sum(weights[i]*d[i] for i in range(2))==0)
ck(all(s[i]+flow[i]-d[i]>=0 for i in range(2)))
ck(sum(weights[i]*max(flow[i],0) for i in range(2))<Q(1,2))
ck(d[0]<0)
lifts=[]
for row in negative_rows:
 H=row['H'];I=row['I'];Rlo,Rhi=H[0]/I,H[1]/I;eps=Rlo-4;ck(eps>0)
 k=((8*Rlo+16)/eps).__ceil__()+8;t=(Q(k*k)/I).__ceil__()
 lower=Rlo/(1+Q(2,k))-Q(1,k*k);upper=max(Rhi,4+Q(5,k))
 ck(lower>4);ck(Rhi>=Rlo);ck(k>=I);ck(k*k<=t*I<=k*k+I)
 lifts.append({'b':row['b'],'seed_R_interval':[Rlo,Rhi],'k':k,'t':t,'actual_ambient_dimension':row['ambient_dimension']*t+k,'ratio_lower':lower,'ratio_upper':upper,'minority_upper':str(Q(1,1<<k)),'influence_upper':str(Q(k*k+3*k,1<<k)),'scope':'explicit finite rare seed lift; ratio remains bounded, not a FEI disproof'})
dump(R/'out'/('RARE_LIFTS_PILOT.json' if args.pilot else 'RARE_LIFTS.json'),lifts)
ck(time.perf_counter()-start<55)
out={'verdict':'PASS','physical_states':len(states),'negative_states':len(negative_rows),'allocation_cases':allocations,'assertions':checks,'seconds':time.perf_counter()-start,'independence':'new direct outer Walsh and full atom-category multiplicities; no A089 executable imported','scope':'generic finite signed allocation, all18 terminal spectra; ancestry bookings accepted only where supplied by declared saturation'}
dump(R/'out'/('REVIEW_PILOT.json' if args.pilot else 'REVIEW_VALIDATION.json'),out);print(json.dumps(out))
