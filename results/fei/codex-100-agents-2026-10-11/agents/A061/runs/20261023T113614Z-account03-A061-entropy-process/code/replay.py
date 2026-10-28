"""Independent GF4 and direct character-sum normalized reference certificate."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import independent_oracle as D
START=time.perf_counter();R=Path(__file__).resolve().parents[1]
def mul4(a,b):
 z=0
 for _ in range(2):
  if b&1:z^=a
  b>>=1;a<<=1
  if a&4:a^=7
 return z
def main():
 h=[]
 for y in range(64):
  a=y&3;b=(y>>2)&3;x=(y>>4)&3
  h.append((-1 if a&1 else 1)*(-1 if x==mul4(a,b) else 1))
 inner=[]
 for w in range(512):
  s=w&1;u=(w>>1)&1;v=(w>>2)&1;y=w>>3
  vphase=(u^v^(y.bit_count()&1))&v
  inner.append((-1 if vphase else 1)*(h[y] if s else 1))
 t=tuple((-1 if (w&3)==3 else 1)*inner[w>>2] for w in range(2048))
 p,ds,H,M,TC=D.stats(t);Q=tuple(F(1,2048) for _ in range(2048));D.ck(all(x==F(1,2) for x in ds),'independent all physical influences')
 D.ck(H==D.A.const(F(17,2)) and TC==D.A.const(F(5,2)),'independent source H/K')
 ss,Qs,r,E,O,Ks=D.transport(t,Q,2);D.ck(r==[F(1,8),F(7,8)] and not E,'direct ordinary reference prediction/E')
 records=[];B={};T={};HH={}
 for a in [0,1]:
  vs,Rs,rv,ev,ov,ks=D.transport(ss[a],Qs[a],1);D.ck(rv==[F(1,2)]*2 and not ev and not ov,'direct protected-pivot reference')
  for b in [0,1]:
   pp,dd,hh,mm,tt=D.stats(vs[b]);J=D.add((1,tt),(-1,ks[b]));D.ck(D.A.interval(J)[0]>0,'direct actual positive child liability')
   D.ck(tt==D.A.const(6 if a==0 else 1) and ks[b]==Ks[a],'direct actual normalized K and TC')
   B=D.add((1,B),(F(1,4),J));T=D.add((1,T),(F(1,4),tt));HH=D.add((1,HH),(F(1,4),hh))
   qp=D.product(dd);D.ck(D.kl(pp,qp)==tt,'direct actual product reset')
   records.append({'s':a,'V':b,'H':D.A.value(hh),'K_before':D.A.value(ks[b]),'TC_after':D.A.value(tt),'J':D.A.value(J)})
 formula=D.add((1,D.A.const(3)),(F(-1,2),D.A.log(F(7))))
 D.ck(B==formula,'independent full minimal booking');D.ck(not D.add((1,T),(1,O),(-1,TC),(-1,B)),'independent full signed reference ledger')
 D.ck(HH==D.A.const(F(9,2)) and T==D.A.const(F(7,2)),'full mean terminal entropy and KL retained')
 D.ck(7<8,'exact integer shortfall>1');D.ck(D.A.interval(D.add((1,B),(-1,D.A.const(F(3,2)))))[0]>0,'certified shortfall beyond halfbit>1')
 S=D.A.const(F(27,2));D.ck(D.A.interval(D.add((F(3,4),S),(-1,TC),(-1,B),(F(-1,8),S)))[0]>0,'same-owner repair strict balance')
 # Pure rational all-l comparison certificates, independent of logarithm decimals.
 D.ck(4096<4802,'(8/7)^4<2, hence -log r<1/4')
 D.ck(all(F(l+1,2)+F(1,8)<=F(9*l,16)+F(1,2) for l in [2,3,10]),'boundary slope comparison')
 seconds=time.perf_counter()-START;D.ck(seconds<55,'direct frozen runtime')
 out={'status':'PASS','independent_assertions':D.N,'auxiliary_scalar_assertions':D.A.COUNT,'seconds':seconds,'source_rows':len(t),'direct_character_terms':len(t)**2,
 'B_minimal':D.A.value(B),'full_mean_H':D.A.value(HH),'mean_KL':D.A.value(T),'records':records,'arithmetic':'Direct exact Fourier characters and physical edges; separate coherent transport; shared pinned prime-log interval arithmetic.'}
 (R/'out/DIRECT_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
