from arithmetic import *
import arithmetic as ar
import sys
idx=int(sys.argv[1]);assert 0<=idx<8
profile=json.loads((RUN/'out/PILOT_RESULTS.json').read_text())['profiles'][idx]
groups=[[F(a) for a in g] for g in profile['groups']];rel=profile['relative_sign'];grid=1<<48
def rnd(v,up=False):
 x=v*grid
 return F(-((-x.numerator)//x.denominator) if up else x.numerator//x.denominator,grid)
@lru_cache(None)
def entropy_iv(x):
 if not x:return F(0),F(0)
 lo,hi=logiv(1/x)
 return rnd(x*lo),rnd(x*hi,True)
@lru_cache(None)
def phi_hi(a,b):
 if not a or not b:return F(0)
 return entropy_iv(a)[1]+entropy_iv(b)[1]-entropy_iv(a+b)[0]
certs=[];unresolved=[];visited=rare=moderate=0;minimum=None
def box(lp,hp,lq,hq,depth):
 global visited,rare,moderate,minimum
 check(True);visited+=1
 if (hp+hq)/8<=F(1,32):rare+=1;return
 if (lp+lq)/8>=F(1,6):moderate+=1;return
 bound=F(lp+lq,4)+F(lp*lp+lq*lq,4)
 for g in [0,1]:
  sign=rel*(-1 if g else 1)
  kl=(lp+(lq if sign==1 else -hq))/8
  kh=(hp+(hq if sign==1 else -lq))/8
  bb=max(kl*kl,kh*kh)
  for a in groups[g]:bound-=phi_hi(max((a-kl)**2,(a-kh)**2),bb)
 if bound>0:
  low=rnd(bound);check(low>0)
  certs.append({'p':[str(lp),str(hp)],'q':[str(lq),str(hq)],'depth':depth,'gap_lower':str(low)})
  minimum=low if minimum is None else min(minimum,low);return
 if depth==4:
  unresolved.append({'p':[str(lp),str(hp)],'q':[str(lq),str(hq)],'bound':str(bound)});return
 mp=(lp+hp)/2;mq=(lq+hq)/2
 for pl,ph in [(lp,mp),(mp,hp)]:
  for ql,qh in [(lq,mq),(mq,hq)]:box(pl,ph,ql,qh,depth+1)
try:
 for i in range(16):
  for j in range(16):box(F(i,16),F(i+1,16),F(j,16),F(j+1,16),0)
 status='PASS' if not unresolved else 'FIXED_DEPTH_UNRESOLVED'
except RuntimeError:status='RUNTIME_CUTOFF'
result={'status':status,'profile_index':idx,'profile':profile,'visited_boxes':visited,'certified_boxes':len(certs),'rare_boxes':rare,'moderate_boxes':moderate,'unresolved_boxes':unresolved,'minimum_gap':str(minimum),'certificates':certs,'exact_assertions':ar.checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/f'out/CONTINUUM_{idx}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['certificates','unresolved_boxes','profile']}),flush=True)
