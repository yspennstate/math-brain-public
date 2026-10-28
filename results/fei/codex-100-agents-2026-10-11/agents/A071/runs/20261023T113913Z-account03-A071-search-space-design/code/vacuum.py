from profile_engine import F,add,mul,minus,mean,neg,pack,cmp,lp
from pathlib import Path
import json,time
from functools import lru_cache
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
def psi(p):return mul(lp(p),-p) if p else {}
def un(p):return {int(k):F(v) for k,v in p.items() if F(v)}
a=json.loads((R/'out/INDEPENDENT_AUDIT.json').read_text(encoding='utf-8'))
p0=[F(z['integer_Walsh'][0],len(z['integer_Walsh']))**2 for z in a['rows']]
ck(p0==[F(1,4096),F(25,1024),F(1,64)])
empty=minus(mean([psi(p) for p in p0[1:]]),psi(p0[0]));rem=minus(un(a['drift']),empty)
ck(empty=={2:F(85,512),5:F(-25,1024)})
ck(rem=={2:F(-1269,512),3:F(-567,512),7:F(3087,2048)})
ck(7**3087<2**5076*3**2268)
@lru_cache(None)
def metrics(t):
 N=len(t);n=(N-1).bit_length();mu=F(sum(t),N);I=F(sum(t[x]!=t[x^(1<<j)] for x in range(N) for j in range(n)),N)
 return psi(mu*mu),I
for code in range(256):
 t=tuple(1 if code>>x&1 else -1 for x in range(8));p,I=metrics(t)
 ck(cmp(minus({2:F(3,2)*I},p),{})>=0)
 for j in range(3):
  kids=[tuple(v for x,v in enumerate(t) if x>>j&1==b) for b in [0,1]];zs=[metrics(k) for k in kids]
  d=F(sum(t[x]!=t[x^(1<<j)] for x in range(8)),8);ck(I-sum(z[1] for z in zs)/2==d)
  ck(cmp(add(p,{2:3*d},neg(mean([z[0] for z in zs]))),{})>=0)
out={'empty_masses':list(map(str,p0)),'empty_term_drift':pack(empty),'nonempty_remainder_drift':pack(rem),'remainder_sign_certificate':'7^3087 < 2^5076 * 3^2268','universal_component':'V(f)=-mu²log2(mu²)+3I(f) is full-query superharmonic and0<=V<=9I/2','proof':'VACUUM_PROOF.md','three_bit_tables':256,'query_rows':768,'checks':checks,'seconds':time.perf_counter()-start,'full_fei':'OPEN'}
ck(out['seconds']<55);(R/'out/VACUUM.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
