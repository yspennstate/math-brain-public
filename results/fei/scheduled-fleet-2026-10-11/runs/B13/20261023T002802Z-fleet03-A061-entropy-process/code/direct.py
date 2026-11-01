"""Direct full-physical second-query replay, separate transport and GF4 realization."""
import check as c
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import time,json
ROOT=Path(__file__).resolve().parents[1];COUNT=0
def ck(b,label='direct assertion'):
 global COUNT
 COUNT+=1
 if not b:raise AssertionError(label)
def gf4(a,b):
 a0=a&1;a1=a>>1;b0=b&1;b1=b>>1
 return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)
def make():
 h=tuple((-1 if s&1 else 1)*(-1 if (s>>4)==gf4(s&3,(s>>2)&3) else 1) for s in range(64))
 G=[];H=[]
 for t in range(256):
  u=t.bit_count()%2;v=(t>>1)&1;b=1-2*u*v
  G.append(b);H.append(b*h[t>>2])
 parent=tuple((G if not t%2 else H)[t//2] for t in range(512))
 return h,tuple(G),tuple(H),parent
@lru_cache(None)
def st(a):
 n=len(a);w=[sum(a[t]*(1-2*((s&t).bit_count()%2)) for t in range(n)) for s in range(n)]
 p=tuple(F(v*v,n*n) for v in w);ck(sum(p)==1,'direct Parseval');dims=n.bit_length()-1
 ds=[]
 for j in range(dims):
  d=sum((p[s] for s in range(n) if (s>>j)&1),F());e=F(sum(a[t]!=a[t^(1<<j)] for t in range(n)),n)
  ck(d==e,'direct physical edge influence');ds.append(d)
 H=c.entropy(p);M=c.plus(*[(1,c.entropy([d,1-d])) for d in ds]);return p,ds,H,c.plus((1,M),(-1,H))
def move(a,j,R):
 p=st(a)[0];N=len(a);ids=[s for s in range(N) if not (s>>j)&1];tables=[tuple(a[s|(b<<j)] for s in ids) for b in [0,1]];ps=[st(t)[0] for t in tables]
 pe=[p[s]+p[s|(1<<j)] for s in ids];re=[R[s]+R[s|(1<<j)] for s in ids];un=[[],[]];refs=F()
 for k in range(N//2):
  if not pe[k]:refs+=re[k]
  for b in [0,1]:un[b].append(re[k]*(ps[b][k]/(2*pe[k]) if pe[k] else F(1,2)))
 reach=[sum(x) for x in un];ck(sum(reach)==1 and min(reach)>0,'direct positive normalization');rr=[tuple(x/reach[b] for x in un[b]) for b in [0,1]]
 for b in [0,1]:ck(sum(rr[b])==1 and all(not x or y>0 for x,y in zip(ps[b],rr[b])),'direct source-support retained')
 K=c.kl(p,R);E=c.plus((1,K),(-1,c.kl(pe,re)));O=c.plus((F(-1,2),c.log(4*reach[0]*reach[1])));Kc=[c.kl(ps[b],rr[b]) for b in [0,1]]
 ck(not c.plus((1,K),(-1,E),(-1,O),(F(-1,2),Kc[0]),(F(-1,2),Kc[1])),'direct complete chain identity')
 return tables,rr,reach,O,E,Kc,refs
def liftcheck(Rfull,Rcore):
 mask=len(Rcore)-1
 for s,x in enumerate(Rfull):ck(x==Rcore[(s>>2)^(mask if s&1 else 0)]/4,'exact actual lift after physical exposure')
def main():
 start=time.perf_counter();h,G,H,parent=make();ck(h==c.core(2),'separate GF4 agrees with declared field');RH,RG,_,_=c.initial(h)
 ck(all(d==F(1,2) for d in st(parent)[1]+st(G)[1]+st(H)[1]),'all original parent/child influences1/2')
 ss,rs,pred,Os,Es,Ks,refs=move(parent,0,tuple([F(1,512)]*512));ck(pred==[F(1,8),F(7,8)],'original selector normalization');ck(not Es,'selector erasure0')
 ck(ss==[G,H],'actual selector children');liftcheck(rs[0],RG);liftcheck(rs[1],RH)
 S=c.plus((1,c.const(16)),(F(-1,2),st(G)[2]),(F(-1,2),st(H)[2]));ck(S==c.const(F(23,2)),'SAME original bank independently rechecked')
 first=move(H,2,rs[1]);corefirst=c.transport(h,0,RH);records=[]
 ck(first[2]==corefirst[2] and first[3:5]==corefirst[3:5],'first normalized data outcome agrees')
 for b in [0,1]:
  liftcheck(first[1][b],corefirst[1][b]);ck(first[5][b]==c.kl(c.stats(corefirst[0][b])[0],corefirst[1][b]),'first K equals core K')
  # Original x0 is index4, then3 after removing original a0; carrier prefix has two bits.
  second=move(first[0][b],5,first[1][b]);coresecond=c.transport(corefirst[0][b],3,corefirst[1][b])
  ck(second[2]==coresecond[2] and second[3:5]==coresecond[3:5],'SECOND normalized data outcome agrees')
  for d in [0,1]:
   leaf=second[0][d];ref=second[1][d];cg=coresecond[0][d];cr=coresecond[1][d];liftcheck(ref,cr)
   ck(second[5][d]==c.kl(c.stats(cg)[0],cr),'second K equals core K')
   carrier=move(leaf,1,ref);ck(carrier[2]==[F(1,2),F(1,2)] and not carrier[3],'exact fair carrier after TWO proper data queries')
   HH=c.stats(cg)[2];TC=c.stats(cg)[4]
   for terminal in carrier[0]:ck(st(terminal)[2]==HH and st(terminal)[3]==TC,'BOTH full H+TC retained')
   records.append({'first_outcome':b,'second_outcome':d,'carrier_reference_only_mass':str(carrier[6]),'full_terminal_H':c.value(HH),'full_terminal_TC':c.value(TC),'incoming_K':c.value(second[5][d]),'core_marginal_envelope':c.value(c.stats(cg)[3])})
 ck(any(F(x['carrier_reference_only_mass'])>0 for x in records),'nontrivial reference-only countercheck')
 ck(time.perf_counter()-start<55,'direct frozen runtime');out={'status':'PASS','direct_assertions':COUNT,'shared_scalar_arithmetic_assertions':c.COUNT,'seconds':time.perf_counter()-start,'original_Sbar':c.value(S),'records':records,'scope':'actual nine-bit source, second proper core query and all full carrier terminals; scalar log dictionaries shared, GF4/direct spectrum/transport separate'}
 (ROOT/'out'/'DIRECT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
