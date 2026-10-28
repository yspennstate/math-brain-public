from pathlib import Path
from functools import lru_cache
import sys,time,json
import exact as e
F=e.F
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
COUNTS={'prefix_states':0,'post_states':0,'prefix_query_nodes':0,'post_query_nodes':0,'field_directions':0,'field_reset_children':0}
def ge(a,b,label):
 d=e.plus((1,a),(-1,b)); e.ck(not d or e.interval(d)[0]>=0,label)
def maximum(es):
 best=es[0]
 for x in es[1:]:
  d=e.plus((1,x),(-1,best))
  if d:
   lo,hi=e.interval(d);e.ck(lo>0 or hi<0,'rigorous maximum ordering')
   if lo>0:best=x
 return best
def avg(es):return e.plus(*[(F(1,len(es)),x) for x in es])
@lru_cache(None)
def post(t,R):
 COUNTS['post_states']+=1
 p,ds,H,M,TC=e.stats(t);K=e.kl(p,R);V=e.plus((1,K),(1,M))
 e.eq(TC,e.kl(p,e.product(ds)),'actual full terminal product KL')
 opts=[K,TC]
 for i in range(len(ds)):
  COUNTS['post_query_nodes']+=1
  cs,qs,rr,O,Ks,E,z=e.transport(t,i,R)
  children=[post(cs[b],tuple(qs[b])) for b in (0,1)]
  opts.append(e.plus((1,O),(1,avg(children))))
  ge(V,e.plus((1,O),(1,avg([e.plus((1,Ks[b]),(1,e.stats(cs[b])[3])) for b in (0,1)]))),'post query potential drift')
 best=maximum(opts);ge(V,best,'all post continuation policies paid');return best
@lru_cache(None)
def before(t,R):
 COUNTS['prefix_states']+=1
 p,ds,H,M,TC=e.stats(t);K=e.kl(p,R);V=e.plus((1,K),(2,M))
 reset=post(t,tuple(e.product(ds)))
 ge(e.plus((1,TC),(1,M)),reset,'reset continuation has full TC plus M')
 ge(V,e.plus((1,TC),(1,M)),'actual reset splice paid')
 opts=[K,reset]
 for i in range(len(ds)):
  COUNTS['prefix_query_nodes']+=1
  cs,qs,rr,O,Ks,E,z=e.transport(t,i,R)
  opts.append(e.plus((1,O),(1,avg([before(cs[b],tuple(qs[b])) for b in (0,1)]))))
  ge(V,e.plus((1,O),(1,avg([e.plus((1,Ks[b]),(2,e.stats(cs[b])[3])) for b in (0,1)]))),'ordinary prefix 2M drift')
 best=maximum(opts);ge(V,best,'entire adaptive reset prefix paid');return best
def lift(R):
 N=len(R);return tuple(R[(s>>2)^((N-1) if s&1 else 0)]/4 for s in range(4*N))
def liftcore(Q):
 R=tuple(4*Q[s<<2] for s in range(len(Q)//4));e.ck(tuple(Q)==lift(R),'inherited lift including reference-only rows');return R
def field(l):
 h=e.core(l);m=3*l;G=e.carrier((1,)*len(h));H=e.carrier(h)
 t=tuple((G if not s&1 else H)[s>>1] for s in range(2*len(G)))
 p,ds,Hroot,Mroot,Kroot=e.stats(t)
 cs,qs,rr,O,Ks,E,z=e.transport(t,0,tuple(F(1,len(t)) for _ in t))
 Hh=e.stats(h)[2];Mh=e.stats(h)[3];W=e.constant(m+2)
 S=e.plus((1,e.constant(2*m+2)),(-F(1,2),Hh))
 e.eq(E,{});e.eq(Kroot,e.plus((1,O),(F(1,2),Ks[0]),(F(1,2),Ks[1])))
 ge(W,Mh,'old expected cap pays all-depth prefix envelope')
 ge(e.plus((F(3,4),S),(-1,W)),e.plus((F(1,28),S)),'same owner old quarter retained')
 ge(e.plus((F(13,24),S)),Mh,'optional sharper new policy cap')
 for b,c in enumerate(cs):
  R=liftcore(qs[b]);g=h if b else (1,)*len(h)
  e.eq(e.kl(e.stats(g)[0],R),Ks[b],'core entry K')
  for j in range(m):
   COUNTS['field_directions']+=1
   dc,dq,dr,dO,dKs,dE,dz=e.transport(c,j+2,qs[b])
   gc,gq,gr,gO,gKs,gE,gz=e.transport(g,j,R)
   e.ck(dr==gr,'same actual inherited reference prediction');e.eq(dO,gO);e.eq(dE,gE)
   V=e.plus((1,Ks[b]),(2,e.stats(g)[3]))
   children=[]
   for bb in (0,1):
    e.ck(liftcore(dq[bb])==tuple(gq[bb]),'history preserved actual reference')
    e.eq(dKs[bb],gKs[bb]);Mm=e.stats(gc[bb])[3];Hc=e.stats(gc[bb])[2]
    children.append(e.plus((1,dKs[bb]),(2,Mm)))
    vc,vq,vr,vO,vKs,vE,vz=e.transport(dc[bb],1,dq[bb])
    e.ck(vr==[F(1,2),F(1,2)],'fresh v fair after actual prefix');e.eq(vO,{});e.eq(vE,{})
    for vb in (0,1):
     COUNTS['field_reset_children']+=1
     pp,dd,hh,mm,tc=e.stats(vc[vb]);e.eq(vKs[vb],dKs[bb],'full pre-reset child KL')
     e.eq(hh,Hc,'full terminal entropy');e.eq(mm,Mm,'deterministic u retained');e.eq(tc,e.kl(pp,e.product(dd)))
     ge(children[-1],e.plus((1,tc),(1,mm)),'physical intermediate reset plus continuation guard')
   ge(V,e.plus((1,dO),(1,avg(children))),'field prefix edge 2M drift')
 return {'l':l,'old_cap':m+2,'new_expected_envelope':e.enc(Mh),'same_original_owner':e.enc(S),'old_quarter_and_cap_residual':e.enc(e.plus((F(3,4),S),(-1,W)))}
def main():
 mode='pilot' if '--pilot' in sys.argv else 'main'
 masks=[0,1,7,105,255] if mode=='pilot' else range(256)
 roots=[]
 for mask in masks:
  t=tuple(1 if mask&(1<<s) else -1 for s in range(8));p,ds,H,M,TC=e.stats(t)
  for name,R in [('uniform',tuple(F(1,8) for _ in p)),('mixture',tuple((x+F(1,8))/2 for x in p))]:
   value=before(t,R);roots.append({'mask':mask,'reference':name,'minimum':e.enc(value),'incoming_K':e.enc(e.kl(p,R))})
  e.ck(time.perf_counter()-START<55,'frozen runtime bound')
 fields=[field(l) for l in ([2] if mode=='pilot' else [2,3])]
 e.ck(3**12>2**19,'all-width entropy power certificate');e.ck(time.perf_counter()-START<55,'final runtime bound')
 result={'status':'PASS','mode':mode,'root_cases':len(roots),'counts':COUNTS,'assertions':e.COUNT,'seconds':time.perf_counter()-START,'field_records':fields,'root_records':roots,'scope':'finite certificates plus analytic all-width/all-depth proof; full FEI OPEN'}
 (ROOT/'out'/('PILOT.json' if mode=='pilot' else 'MAIN.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('root_records','field_records')}))
if __name__=='__main__':main()
