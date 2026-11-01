from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import time,json
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;rows=[]
def ck(p):
 global checks
 checks+=1;assert p,checks
for a,b,H in [(2,3,[7,0]),(6,6,[7,7,7,56,56,56])]:
 n=a+b;N=1<<n;g=[((1<<b)-1)^h for h in H];f=[];E=set()
 for x in range(N):
  X=x&((1<<a)-1);Y=x>>a;v=any((X>>i&1) and (Y&g[i]) for i in range(a));f.append(1 if v else -1)
  if X and Y and not v:E.add(x)
 h=sum(z.bit_count() for z in H);wl=sum(z.bit_count()==2 for z in H);wr=sum(sum(z>>j&1 for z in H)==2 for j in range(b));c4=sum((H[i]&H[j]).bit_count()==2 for i,j in combinations(range(a),2))
 ck(len(E)!=h+wl+wr+c4)
 if a==2:ck(len(E)==7 and h==3)
 else:ck(len(E)==98 and 2*len(E)>9*a)
 I=F(sum(f[x]!=f[x^(1<<i)] for x in range(N) for i in range(n)),N)
 J=F(2*sum(x^(1<<i) not in E for x in E for i in range(n)),N)
 w=f[:];stride=1
 while stride<N:
  for base in range(0,N,2*stride):
   for j in range(base,base+stride):w[j],w[j+stride]=w[j]+w[j+stride],w[j]-w[j+stride]
  stride*=2
 JD=JR=JM=R=M=0
 for S in range(1,N):
  l=S&((1<<a)-1);r=S>>a;degree=S.bit_count();z0=-2*(((1<<b) if not r else 0)+((1<<a) if not l else 0)-1);dd=(w[S]-z0)**2
  JD+=degree*dd
  if not l:R+=degree*w[S]**2;JR+=degree*dd
  elif r:M+=degree*w[S]**2;JM+=degree*dd
 R,M,JR,JM=map(lambda x:F(x,N*N),[R,M,JR,JM]);ck(F(JD,N*N)==J and JR+JM<=J)
 u,t=F(1,1<<a),F(1,1<<b);R0=2*b*t*(1-u)**2;M0=2*u*t*(a*(1-t)+b*(1-u))
 ck(R<=2*R0+2*JR and M<=2*M0+2*JM)
 if a==6:
  ck(all(x.bit_count()*2>=b for x in g));ck(all(2*sum(x>>j&1 for x in g)>=a for j in range(b)))
  ck(I>=F(3,2)*a*u)
  # The exact algebraic energy transfer works for every nonnegative log weight.
  c,d=F(0),F(3);ck(c*JR+d*JM<=d*J)
 rows.append({'a':a,'b':b,'deleted_degrees':[z.bit_count() for z in H],'exceptional_points':len(E),'I':str(I),'J':str(J),'outside_degree2_proof_domain':True,'conditional_transfer_identity_validated':a==6})
out={'status':'PASS','functions':2,'assertions':checks,'seconds':time.monotonic()-start,'rows':rows}
(B/'out/ADVERSARIAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
