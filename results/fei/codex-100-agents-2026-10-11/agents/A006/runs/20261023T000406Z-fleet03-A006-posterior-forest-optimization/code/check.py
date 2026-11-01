"""Exact Boolean spectrum and joint defect-energy certificates; no author imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json,time,sys
B=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def roundhi(x,bits=40):return F(-((-x.numerator*(1<<bits))//x.denominator),1<<bits)
def roundlo(x,bits=40):return -roundhi(-x,bits)
def unitln(y):
 z=(y-1)/(y+1);t=z;s=F(0)
 for j in range(20):s+=2*t/(2*j+1);t*=z*z
 return s,s+2*t/(41*(1-z*z))
LN2=unitln(F(2))
@lru_cache(None)
def log2(x):
 x=F(x);ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:y*=2;k-=1
 ck(1<=y<2);lo,hi=unitln(y)
 return roundlo(k+lo/LN2[1]),roundhi(k+hi/LN2[0])
def walsh(v):
 v=v[:];s=1
 while s<len(v):
  for i in range(0,len(v),2*s):
   for j in range(i,i+s):v[j],v[j+s]=v[j]+v[j+s],v[j]-v[j+s]
  s*=2
 return v
def graphs(a,b):
 choices=[z for z in range(1<<b) if z.bit_count()<=2]
 def rec(rows,ds):
  if len(rows)==a:
   yield tuple(rows);return
  for r in choices:
   if any(ds[j]==2 and r>>j&1 for j in range(b)):continue
   yield from rec(rows+[r],[ds[j]+((r>>j)&1) for j in range(b)])
 yield from rec([],[0]*b)
def case(a,b,H):
 n=a+b;N=1<<n;allr=(1<<b)-1;g=[allr^r for r in H]
 assert max([r.bit_count() for r in H]+[sum(r>>j&1 for r in H) for j in range(b)])<=2
 f=[];defect=[]
 for x in range(N):
  X=x&((1<<a)-1);Y=x>>a
  positive=any((X>>i&1) and (Y&g[i]) for i in range(a))
  f.append(1 if positive else -1)
  if X and Y and not positive:defect.append(x)
 E=set(defect);h=sum(r.bit_count() for r in H)
 wl=sum(r.bit_count()==2 for r in H);wr=sum(sum(r>>j&1 for r in H)==2 for j in range(b))
 c4=sum((H[i]&H[j]).bit_count()==2 for i,j in combinations(range(a),2))
 e=len(E);ck(e==h+wl+wr+c4);ck(4*e<=9*h<=18*a)
 u,t=F(1,1<<a),F(1,1<<b);J=F(2*sum((x^(1<<i)) not in E for x in E for i in range(n)),N)
 ck(J<=2*n*e*u*t)
 W=walsh(f);den=N*N;L=R=M=JR=JM=JD=0
 for S,z in enumerate(W):
  if not S:continue
  w=S.bit_count();left=S&((1<<a)-1);right=S>>a
  z0=-2*(((1<<b) if not right else 0)+((1<<a) if not left else 0)-1)
  delta=z-z0;ck(z*z<=2*z0*z0+2*delta*delta)
  JD+=w*delta*delta
  if not right:L+=w*z*z
  elif not left:R+=w*z*z;JR+=w*delta*delta
  else:M+=w*z*z;JM+=w*delta*delta
 L,R,M,JR,JM=map(lambda z:F(z,den),[L,R,M,JR,JM]);I=L+R+M
 ck(sum(z*z for z in W)==den);ck(F(JD,den)==J)
 ck(I==F(sum(f[x]!=f[x^(1<<i)] for x in range(N) for i in range(n)),N))
 R0=2*b*t*(1-u)**2;M0=2*u*t*(a*(1-t)+b*(1-u))
 ck(R<=2*R0+2*JR and M<=2*M0+2*JM and JR+JM<=J)
 edges=a*b-h
 if not edges:
  ck(a==b==2 and I==0 and all(z==-1 for z in f))
  return {'a':a,'b':b,'H':list(H),'constant':True,'I':'0','exceptional_points':e}
 ck(I>0)
 D=(1+F(1,4*b))**edges-1;vf=1-F(W[0]*W[0],den);q=F(sum(z==-1 for z in f),N)
 ck(vf==4*q*(1-q));root_hi=vf*log2(D)[1];ck(root_hi<F(9,8)*I)
 if b>=4:
  ck(I>=a*2*u*(1-F(1,1<<(b-2)))>=F(3,2)*a*u)
  lb=log2(F(b))[1];ck(J*lb<=12*I)
  if a>=4:
   lr=log2(F(b,a))[1]
   ck(R0*lr<=F(4,3)*I and M0*lb<=F(2,3)*I)
   label=R*lr+M*lb;ck(label<=28*I)
   upper=root_hi+F(25,4)*I+label;ck(upper<36*I)
  else:
   ck(a in [2,3]);ck(R0*lb<=F(32,9)*I and M0*lb<=F(4,3)*I)
   label=(R+M)*lb;ck(label<=F(304,9)*I)
   upper=root_hi+F(25,4)*I+label;ck(upper<42*I)
 else:
  label=log2(F(b))[1]*I;upper=root_hi+F(25,4)*I+label;ck(upper<42*I)
 return {'a':a,'b':b,'H':list(H),'I':str(I),'J':str(J),'L':str(L),'R':str(R),'M':str(M),'exceptional_points':e,'complete_cost_upper_bits':str(roundhi(upper,32)),'bound42I':True,'bound36I':a>=4}
def fixtures():
 for a,b in [(2,8),(3,7),(4,5)]:yield a,b,tuple((1<<i)|(1<<(i+1)) for i in range(a))
 for a,b in [(5,5),(4,8)]:yield a,b,tuple((1<<i)|(1<<((i+1)%a)) for i in range(a))
 yield 6,6,tuple((3<<(2*(i//2))) for i in range(6))
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;top=3 if pilot else 4;tag='PILOT' if pilot else 'CHECK';rows=[];counts={};Ntruth=0
 spec=json.loads((B/'FROZEN_SPEC.json').read_text(encoding='utf-8'))
 with (B/'out'/f'{tag}_ROWS.jsonl').open('w',encoding='utf-8') as out:
  for b in range(2,top+1):
   for a in range(2,b+1):
    key=f'{a},{b}';counts[key]=0
    for H in graphs(a,b):
     r=case(a,b,H);rows.append(r);out.write(json.dumps(r,separators=(',',':'))+'\n');counts[key]+=1;Ntruth+=1<<(a+b)
    out.flush();ck(counts[key]==spec['case_count_by_size'][key]);ck(time.monotonic()-start<(55 if pilot else 175))
  if not pilot:
   for a,b,H in fixtures():
    r=case(a,b,H);rows.append(r);out.write(json.dumps(r,separators=(',',':'))+'\n');out.flush();Ntruth+=1<<(a+b)
 expected=spec['case_count_pilot' if pilot else 'case_count_full'];ck(len(rows)==expected)
 result={'status':'PASS','helper_version':'A006-deleted-degree-two-complete-cost-v1','functions':len(rows),'nonconstant_functions':sum(not r.get('constant',False) for r in rows),'truth_inputs':Ntruth,'counts_by_size':counts,'assertions':checks,'seconds':time.monotonic()-start,'all_cost_bounds':'<42I; a>=4 gives<36I','constant_cases':sum(r.get('constant',False) for r in rows)}
 (B/'out'/f'{tag}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
