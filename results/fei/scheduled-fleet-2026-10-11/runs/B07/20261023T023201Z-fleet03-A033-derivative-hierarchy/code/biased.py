"""Independent direct-character certificate of the continued paid biased reset."""
from fractions import Fraction as Q
from pathlib import Path
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
 if time.monotonic()-start>55:raise TimeoutError('frozen 55s bound')
def direct(tt):
 return tuple(sum(Q(v)*(1 if (s&x).bit_count()%2==0 else -1) for x,v in enumerate(tt))/len(tt) for s in range(len(tt)))
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-x*x for x in a)
h=(1,1,1,-1,1,1,1,-1); aa,bb,hh=direct(a),direct(b),direct(h)
ck(sum(x*x for x in bb)==Q(3,8));ck(hh[0]==Q(1,2))
p=tuple(x*x for x in hh);ck(sum(p)==1)
Rt=tuple(p[t]/Q(3,4) for t in range(1,8))
M=(Q(0),)+tuple(Q(7,8)*x+Q(1,56) for x in Rt)
ck(M[1]==Q(13,42));ck(sum(M)==1)
ck(sorted(M[1:])==[Q(1,56)]*4+[Q(13,42)]*3)
L=tuple((M[2*v]+M[2*v+1])/(1-M[1]) for v in range(1,4))
ck(L==(Q(26,29),Q(3,58),Q(3,58)))
N=tuple(Q(7,8)*x+Q(1,8)*(v==2) for v,x in enumerate(L,1))
ck(N==(Q(91,116),Q(79,464),Q(21,464)));ck(sum(N)==1)
ck(21**18>2**79) # prior A032 strict >1/64 release
ck(448**40*7**15>2**8*361**40*8**15) # new strict >1/10 release
fixtures=[]
for sig in (1,-1):
 parent=tuple(a[u]+sig*b[u]*h[x] for x in range(8) for u in range(16))
 wp=direct(parent);pp=tuple(x*x for x in wp)
 incoming=tuple((aa[u]+sig*Q(1,2)*bb[u])**2 if t==0 else bb[u]**2*Q(3,4)*M[t] for t in range(8) for u in range(16))
 ck(sum(incoming)==1);ck(all(not x or q>0 for x,q in zip(pp,incoming)))
 inherited=tuple(incoming[u+16*(2*v)]+incoming[u+16*(2*v+1)] for v in range(4) for u in range(16))
 ck(sum(inherited[:16])==Q(361,448));ck(sum(inherited[16:])==Q(87,448))
 for bit in (0,1):
  hs=h[bit::2];mean=sum(hs,Q(0))/len(hs)
  ck(mean==(1 if bit==0 else 0))
  tt=tuple(a[u]+sig*b[u]*hs[x] for x in range(4) for u in range(16))
  ck(all(abs(x)==1 for x in tt))
  ww=direct(tt);pnew=tuple(x*x for x in ww)
  qnew=tuple((aa[u]+sig*mean*bb[u])**2 if v==0 else bb[u]**2*(1-mean*mean)*N[v-1] for v in range(4) for u in range(16))
  ck(sum(pnew)==sum(qnew)==1)
  ck(all(not x or q>0 for x,q in zip(pnew,qnew)))
  ck(all(not x or q>0 for x,q in zip(pnew,inherited)))
  ck(sum(pnew[16:])==(0 if bit==0 else Q(3,8)))
  ck(qnew[:16]==pnew[:16])
  fixtures.append({'tag_sign':sig,'seed_bit':bit,'seed_mean':str(mean),'true_vacuum_mass':str(sum(pnew[:16])),'inherited_vacuum_mass':str(sum(inherited[:16])),'true_tail_mass':str(sum(pnew[16:])),'full_true_spectrum':list(map(str,pnew)),'full_new_reference':list(map(str,qnew))})
out={'status':'PASS','method':'independent direct character sums and exact integer powers','exact_assertions':checks,'runtime_seconds':time.monotonic()-start,'new_release_strict_lower_bound':'1/10 bit at EACH tag parent','previous_tag_release_strict_lower_bound':'1/64 bit','same_source_bank':True,'current_L':list(map(str,L)),'new_N':list(map(str,N)),'fixtures':fixtures,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'biased_continuation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
