from pathlib import Path
from fractions import Fraction as Q
import time,json
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T060651Z-fleet03-A057-coherent-restriction-remainder/code/independent_repro.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for code in ([0,3,5,15]')[0],ns)
H,mix,ph,positive,inf=[ns[k] for k in ['H','mix','ph','positive','inf']]
start=time.monotonic();checks=roots=positive_old=nontrivial=0
def ck(x):
 global checks
 assert x;checks+=1
 if time.monotonic()-start>55:raise RuntimeError('frozen55-second cap')
def sub(g,i,v):return tuple(g[y] for y in range(len(g)) if y>>i&1==v)
def bent(z):return (-1)**((z&1)*(z>>1&1)+(z>>2&1)*(z>>3&1))
def table(g,k,sgn=1):return tuple(sgn*g[y]*(-1)**z.bit_count() if x==15 else bent(x) for z in range(1<<k) for y in range(len(g)) for x in range(16))
c=Q(1,16);B=Q(7)
for n,gt in [(2,8),(2,6),(3,254)]:
 g=tuple(1 if gt>>y&1 else -1 for y in range(1<<n))
 for k in [1,2]:
  f=table(g,k);ck(4*sum(inf(f,i) for i in range(4))==B)
  children=[sub(g,0,v) for v in [0,1]]
  old=mix((1,H(f)),(-Q(1,2),H(table(children[0],k))),(-Q(1,2),H(table(children[1],k))))
  Gdecr=mix((1,H(g)),(-Q(1,2),H(children[0])),(-Q(1,2),H(children[1])))
  ck(old==mix((c,Gdecr)));ck(positive(old));ck(positive(mix((1,{2:2*c}),(-1,old))))
  if positive(mix((1,old),(-1,{2:c/1000}))):positive_old+=1
  final=[];debits=[]
  for h in children:
   q=Q(sum(h),len(h))**2;nontrivial+=q not in [0,1]
   if k==2:ck(H(table(h,2))==H(table(h,1)))
   plus,minus=H(table(h,0,1)),H(table(h,0,-1));final.extend([plus,minus])
   D=mix((1,H(table(h,1))),(-Q(1,2),plus),(-Q(1,2),minus));debits.append(D)
   T=mix((1,{2:c*q*Q(17,2)}),(c,ph(q)))
   # Independent physical Fourier amplitudes of K=b-C.
   K=[0 if x==15 else bent(x) for x in range(16)];L={}
   for s in range(16):
    w=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(K))
    a=Q(w*w,256);bb=q/256
    L=mix((1,L),(1,ph(a)),(1,ph(bb)),(-1,ph(a+bb)))
   J=mix((1,D),(-1,L));ck(positive(J));ck(positive(mix((1,{2:3*c*q}),(-1,J))))
   ck(positive(mix((1,T),(-1,D))))
   ck(positive(mix((1,{2:B}),(-1,old),(-1,D),(-1,{2:Q(29,32)*B}))))
  total=mix((1,H(f)),*[(-Q(1,4),term) for term in final])
  ck(total==mix((1,old),(Q(1,2),debits[0]),(Q(1,2),debits[1])))
  roots+=1
for m in range(4,257,4):
 cc=Q(1,1<<m);bank=2*m-4*m*cc
 ck(cc*(m+Q(13,2))<=Q(3,32)*bank)
for j in range(129):
 q=Q(j,128)
 ck(positive(mix((1,{2:Q(17,2)*(1-q)}),(-1,ph(q)))))
out={'status':'PASS','roots':roots,'positive_old_roots':positive_old,'nontrivial_q_children':nontrivial,'exact_assertions':checks,'seconds':time.monotonic()-start,'arithmetic':'independent direct character sums and48-term log bounds','full_terminal_telescope':'exact equality PASS'}
(ROOT/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
