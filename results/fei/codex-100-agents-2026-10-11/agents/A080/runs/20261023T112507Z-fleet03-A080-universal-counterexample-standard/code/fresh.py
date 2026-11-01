from pathlib import Path
from collections import Counter
import sys,time,json
from arithmetic import Q,ell,h2,add,sub,scale,overlap,dump
from audit import influence,mu
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out'
start=time.monotonic();checks=0
def ck(v,s):
 global checks
 checks+=1
 if not v:raise AssertionError(s)
 if time.monotonic()-start>55:raise RuntimeError('frozen55 seconds')
def entropy(tab):
 N=len(tab);w=[]
 for a in range(N):w.append(sum(tab[x]*(-1 if (a&x).bit_count()%2 else 1) for x in range(N)))
 ck(sum(a*a for a in w)==N*N,'full physical Parseval')
 ps=Counter(Q(a*a,N*N) for a in w)
 return add(*(scale(n,ell(p)) for p,n in ps.items()))
def correction(t):return sub(scale(2,h2((1+t)/2)),scale(Q(1,2),h2(t*t)))
def main():
 pilot='--pilot' in sys.argv;count=16 if pilot else 256;means=range(0,257,16) if pilot else range(257)
 for mask in range(count):
  g=[1-2*((mask>>x)&1) for x in range(8)]
  f=[g[x&7] if x&8 else 1 for x in range(16)]
  t=mu(g);p=(1-t)/2;ig=influence(g);iff=influence(f)
  ck(iff==ig/2+p,'retained fresh physical influence')
  hg=entropy(g);hf=entropy(f);c=sub(hf,scale(Q(1,2),hg))
  ck(overlap(c,correction(t)),'actual full signed composition identity')
  if p:
   ck(c[1]<8*p,'fresh source covers complete outer entropy correction')
  else:ck(all(a==1 for a in f),'zero fresh-source boundary is constant')
  ck(2*(1-t*t)<=8*p,'variance collateral charged to distinct fresh coordinate')
 tested=0
 for j in means:
  tested+=1;t=Q(j,128)-1;p=(1-t)/2
  if p:ck(correction(t)[1]<8*p,'all finite means fresh payment')
  else:ck(t==1,'exact zero entropy correction endpoint')
 result={'status':'PASS','pilot':pilot,'actual_compositions':count,'dyadic_means':tested,'checked_assertions':checks,'runtime_seconds':time.monotonic()-start,'exact_all_policy_claim':'R_K(AND_minus(g,y))=R_K(g)/2 for every Boolean g,K>=8; allm guard iteration analytic in PROOF.md section7.','no_disproof':'H(F_m)/I(F_m)<=max(H(g)/I(g),8); earlier stronger activation ratio bounds not repeated as new progress.'}
 dump(OUT/('FRESH_PILOT.json' if pilot else 'FRESH_PAYMENT.json'),result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
