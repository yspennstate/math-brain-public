"""Frozen K_m,m certificates; no posterior or spectrum sampling."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import factorial
import json,time,argparse
import check as own

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();counts={'assertions':0,'functions':0,'forced_owner_maps':0}
def ck(x):
 counts['assertions']+=1
 assert x
 assert time.perf_counter()-start<55
def run(m):
 a=F(1,1<<m);n=2*m
 tab=tuple((1<<i)|(1<<(m+j)) for i in range(m) for j in range(m))
 g=own.truth(tab,n);gh=own.walsh(g);I=own.influence(g,n)
 ck(I==4*m*a*(1-a));ck(sum(x*x for x in gh)==1<<(2*n))
 v=1-F(gh[0],1<<n)**2;ck(v<=8*a)
 within_degree=F(0);within_excess=F(0);cross=F(0)
 for T in range(1,1<<n):
  P=F(gh[T]*gh[T],1<<(2*n));left=bool(T&((1<<m)-1));right=bool(T>>m)
  ck(abs(F(gh[T],1<<n))==(2*a*a if left and right else 2*a*(1-a)))
  if left and right:cross+=P
  else:within_degree+=P*T.bit_count();within_excess+=P*(T.bit_count()-1)
 ck(within_degree==I*(1-a));ck(within_excess==4*a*(1-a)**2*(m-2+2*a))
 ck(cross==4*a*a*(1-a)**2)
 # Every map on either within-side set owns distinct primes; all roots, no selected edges.
 if m<=4:
  for side in (0,1):
   for s in range(1,m+1):
    for chosen in combinations(range(m),s):
     T=sum(1<<(i+side*m) for i in chosen)
     for choices in product(range(m),repeat=s):
      owners=[i*m+j if side==0 else j*m+i for i,j in zip(chosen,choices)]
      ck(len(set(owners))==s)
      ck(all((tab[l]&T).bit_count()==1 for l in owners))
      counts['forced_owner_maps']+=1
     # Fifth-power form of the exact J1 formula, with all credits.
     j5=F(factorial(s),m**s)**5*2**(4*(s-1))
     ck(j5<=2**(4*(s-1)))
 if m>=4:
  ck((1-a)*F(m-2+2*a,m)>=F(15,32))
  ck(8*m<=2**(m+1));ck(F(m+1,2**m)<=F(5,16))
  ck((F(2,m)+F(3,8))/(1-a)<=F(14,15))
 D=(1+F(1,4*m))**(m*m)-1;Dp=(1+F(1,8*m*m))**(m*m)-1
 ck(Dp>=F(1,8));ck(Dp<=D/(2*m))
 # All possible edge-owner local congestion ratios used in the cross upper bound.
 for sl,kap in [(1,1),(1,2),(2,2)]:
  w0=F(kap,kap+1)**sl
  w1=F(sl+1,kap+1)**(sl+1)/F(sl,kap)**sl
  ck(w0<=1 and w1<=1)
  ck(w1==(F(8,9) if (sl,kap)==(1,2) else 1))
 counts['functions']+=1
 row={'m':m,'I':str(I),'variance':str(v),'M_lower':str(within_excess),
      'M_lower_over_I':str(within_excess/I),'cross_mass':str(cross),'D':str(D),'Dprime':str(Dp)}
 (ROOT/'out'/('KMM_'+str(m)+'.json')).write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
 for m in ([2,3] if args.pilot else [2,3,4,5,6]):run(m)
 result={'status':'PASS','helper_version':'A015-leafless-scale-v1','counts':counts,
         'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh/Fraction; no numerical logarithms',
         'scope':'exact finite identities; analytic inequality (10) supplies all-dimensional fixed-reference obstruction'}
 (ROOT/'out'/('LEAFLESS_PILOT.json' if args.pilot else 'LEAFLESS_EXACT.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
