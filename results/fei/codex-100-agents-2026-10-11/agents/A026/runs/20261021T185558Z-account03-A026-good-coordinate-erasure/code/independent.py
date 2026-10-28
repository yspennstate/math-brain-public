"""Independent direct character-sum spectra and hypothesis guards; no core import."""
from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A026-independent-character-sums-v1','family':'same three point/bent roots, plus common-dictator continuation; two hypothesis counterchecks','parameter_domain':{'m':[2,4,6]},'case_count':'3 roots, 6 j-restrictions, 3 common-dictator lifts, 2 hypothesis guards, 11 scalar certificate fixtures','symmetry':'one explicit family, no class exhaustion','arithmetic':'direct integer character sums, physical edges, Fraction, exact rational inequalities','memory_estimate_mb':60,'max_runtime_seconds':55}
(R/'INDEPENDENT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0
def ck(a):
 global checks
 assert a;checks+=1
def specsum(f):
 N=len(f)
 return [sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(f)) for s in range(N)]
def split(f,b):return f[b::2]
rows=[]
for m in [2,4,6]:
 N=1<<m;t=F(1,N);u=F(1,1<<(m//2))
 q=tuple((-1)**sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(m//2)) for x in range(N))
 G=tuple(-1 if x==0 else 1 for x in range(2*N));H=tuple(q[x>>1] for x in range(2*N))
 wg=specsum(G);wh=specsum(H)
 ck(wg[0]==2*N-2);ck(all(w==-2 for w in wg[1:]));ck(all(w==0 for w in wh[1::2]));ck(all(F(w*w,(2*N)**2)==t for w in wh[::2]))
 ck(F(sum(a!=b for a,b in zip(G,H)),2*N)==(1-u+t)/2)
 for b in [0,1]:
  gs=split(G,b);hs=split(H,b);w=specsum(gs)
  ck(hs==q)
  ck((w[0]==N and all(z==0 for z in w[1:])) if b else (w[0]==N-2 and all(z==-2 for z in w[1:])))
 # Common fresh dictator: duplicate with opposite signs on the new high bit.
 Gt=G+tuple(-x for x in G);Ht=H+tuple(-x for x in H)
 for b in [0,1]:
  ck(len(set(split(Gt,b)))==2);ck(len(set(split(Ht,b)))==2)
 wgt=specsum(Gt);wht=specsum(Ht)
 ck(all(x==0 for x in wgt[:2*N]));ck(wgt[2*N:]==[2*x for x in wg]);ck(wht[2*N:]==[2*x for x in wh])
 ck(F(sum(G[x]!=G[x^1] for x in range(2*N)),2*N)==t)
 rows.append({'m':m,'disagreement':str((1-u+t)/2),'queried_branch_influence':str(t),'both_lifted_original_children_nonconstant':True})
 ck(time.perf_counter()-start<55)
for m in range(4,15):
 t=F(1,1<<m)
 ck(m*t/2<=F(1,8));ck(t<=F(1,16));ck((1-t)*(2+F(3,4)*(1+t))<=F(11,4));ck(24*t*t<=F(3,32))
ck(F(1,8)+F(11,4)+F(3,32)==F(95,32));ck(F(95,32)<3)
# A constant (unbalanced) encoder with G=1,H=x returns a constant, entropy zero.
# An independent uniform shadow has four Fourier squares 1/4, entropy two.
G=(1,1);H=(1,-1);shadow=tuple(y for pair in zip(H,G) for y in pair)
ck(sorted(x*x for x in specsum(shadow))==[4,4,4,4]);ck(len(set(G))==1)
# Reuse the same x as encoder and data: (1+x)/2+x(1-x)/2=x, entropy zero.
overlap=tuple((1+x)//2+x*(1-x)//2 for x in [1,-1]);ck(overlap==(1,-1))
out={'status':'PASS','assertions':checks,'elapsed_seconds':time.perf_counter()-start,'rows':rows,'hypothesis_guards':'balance and physical disjointness cannot be dropped; explicit zero-versus-two-bit examples','rung':'exact finite reconstruction, not Lean verification'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
