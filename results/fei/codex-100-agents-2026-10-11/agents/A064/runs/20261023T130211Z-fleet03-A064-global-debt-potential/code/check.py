from pathlib import Path
import sys,json,time,hashlib
import exact as x
F=x.F
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
COUNTS={'states':0,'ordinary_transports':0,'pivot_transports':0,'postreset_transports':0,'negative_eligibility_sectors':0,'reference_only_pivots':0}

def add(*es):return x.plus(*es)
def pos(e):
 if not e:return {}
 lo,hi=x.interval(e)
 x.ck(lo>0 or hi<0,'rigorous sign separates zero')
 return e if lo>0 else {}
def ge(a,b,label):
 d=add((1,a),(-1,b))
 x.ck(not d or x.interval(d)[0]>=0,label)
def make(g,h):
 return tuple((h[s>>2]*(-1 if s&1 else 1)) if s&2 else g[s>>2] for s in range(4*len(g)))
def law(w,rs):return [w[s&1]*rs[s&1][s>>2]/2 for s in range(4*len(rs[0]))]

def state(g,h,w,rs):
 COUNTS['states']+=1
 t=make(g,h);Q=law(w,rs);sg,sh=x.stats(g),x.stats(h)
 p,ds,H,M,TC=x.stats(t)
 for s,pv in enumerate(p):x.ck(pv==[sg,sh][s&1][0][s>>2]/4,'actual spectrum sector formula')
 x.eq(H,add((1,x.constant(2)),(F(1,2),sg[2]),(F(1,2),sh[2])),'full source entropy')
 D=[x.kl(s[0],r) for s,r in zip((sg,sh),rs)]
 L=[add((1,d),(-1,s[4])) for d,s in zip(D,(sg,sh))]
 K=x.kl(p,Q);occ=x.kl((F(1,2),F(1,2)),w)
 x.eq(K,add((F(1,2),D[0]),(F(1,2),D[1]),(1,occ)),'sector KL and occupancy split')
 cs,qs,rr,O,Ks,E,ref=x.transport(t,1,Q);COUNTS['pivot_transports']+=1
 COUNTS['reference_only_pivots']+=bool(ref)
 a=[sum((rj for pj,rj in zip(s[0],r) if pj),F()) for s,r in zip((sg,sh),rs)]
 expected=[F(1,2)+(w[0]*a[0]-w[1]*a[1])/2];expected.append(1-expected[0])
 x.ck(rr==expected,'full fair-zero-row prediction')
 x.eq(E,{},'pivot erasure credit zero')
 c=[x.log(w[b]/rr[b]) for b in (0,1)]
 J=[add((1,c[b]),(-1,L[b])) for b in (0,1)]
 B=add(*[(F(1,2),pos(j)) for j in J])
 bound=add((1,x.constant(F(1,2))),*[(F(1,2),pos(add((-1,l)))) for l in L])
 ge(bound,B,'sharp half-bit plus measured eligibility bound')
 x.eq(add((F(1,2),J[0]),(F(1,2),J[1])),add((1,O),(-1,occ),(-F(1,2),L[0]),(-F(1,2),L[1])),'endpoint occupancy identity')
 for b in (0,1):
  x.ck(rr[b]>w[b]/2,'strict reference mass bound')
  x.eq(Ks[b],add((1,D[b]),(1,x.log(rr[b]/w[b]))),'actual inherited child KL')
  x.eq(x.stats(cs[b])[4],[sg,sh][b][4],'full child TC includes surviving u')
  x.eq(J[b],add((1,x.stats(cs[b])[4]),(-1,Ks[b])),'signed actual product debit')
  COUNTS['negative_eligibility_sectors']+=bool(pos(add((-1,L[b]))))
  for atom,pv in enumerate(x.stats(cs[b])[0]):
   if pv:x.ck(qs[b][atom]==w[b]*rs[b][atom>>1]/rr[b],'inherited positive-atom likelihood')
  chosen=max_expr(Ks[b],x.stats(cs[b])[4])
  x.eq(chosen,add((1,Ks[b]),(1,pos(J[b]))),'actual branch choice potential')
  if len(g)>1:
   R=x.product(x.stats(cs[b])[1]);qq=x.transport(cs[b],1,R);COUNTS['postreset_transports']+=1
   ge(x.stats(cs[b])[4],add((1,qq[3]),(F(1,2),qq[4][0]),(F(1,2),qq[4][1])),'proper ordinary continuation paid by current KL')
 if g==h and w[0]==F(1,2) and rs[0]==rs[1]:
  x.eq(B,pos(add((-1,L[0]))),'identical-sector exact eligibility equality')
 # Finite all-direction Snell recursion, with immediate retention and pivot at each node.
 candidates=[{},B]
 for i in range(len(g).bit_length()-1):
  full=x.transport(t,i+2,Q);core=[x.transport(z,i,r) for z,r in zip((g,h),rs)]
  COUNTS['ordinary_transports']+=3
  x.eq(full[5],add((F(1,2),core[0][5]),(F(1,2),core[1][5])),'ordinary signed erasure splits over sectors')
  G=[];childocc=[]
  for e in (0,1):
   pred=sum((w[b]*core[b][2][e] for b in (0,1)),F())
   x.ck(full[2][e]==pred,'actual mixture prediction')
   wn=[w[b]*core[b][2][e]/pred for b in (0,1)]
   rn=[core[b][1][e] for b in (0,1)]
   gn,hn=core[0][0][e],core[1][0][e]
   x.ck(full[0][e]==make(gn,hn),'actual restricted Boolean pair')
   x.ck(full[1][e]==law(wn,rn),'FULL updated reference preserves conditional sectors')
   childocc.append(x.kl((F(1,2),F(1,2)),wn))
   G.append(state(gn,hn,wn,rn))
  x.eq(add((1,occ),(-F(1,2),childocc[0]),(-F(1,2),childocc[1])),add((1,full[3]),(-F(1,2),core[0][3]),(-F(1,2),core[1][3])),'signed occupancy drift')
  candidate=add((F(1,2),G[0]),(F(1,2),G[1]),(-1,full[5]));candidates.append(candidate)
 G={}
 for candidate in candidates:G=max_expr(G,candidate)
 for candidate in candidates:ge(G,candidate,'all declared cuts funded')
 return G

def max_expr(a,b):return add((1,a),(1,pos(add((1,b),(-1,a)))))

def main(mode):
 masks=[0,7] if mode=='pilot' else list(range(16))
 records=[]
 for mg in masks:
  g=tuple(1 if mg&(1<<s) else -1 for s in range(4))
  for mh in masks:
   h=tuple(1 if mh&(1<<s) else -1 for s in range(4))
   ds=[(a+b)/2 for a,b in zip(x.stats(g)[1],x.stats(h)[1])]
   for kind in ('genuine_product','biased_distinct_nonproduct_sectors'):
    if kind=='genuine_product':w=[F(1,2)]*2;rs=[x.product(ds)]*2
    else:w=[F(1,3),F(2,3)];rs=[[F(a,11) for a in z] for z in ((1,2,3,5),(5,3,2,1))]
    G=state(g,h,w,rs)
    records.append({'masks':[mg,mh],'reference':kind,'root_minimal_reserve':x.enc(G),'interval':x.enciv(G)})
 expected=len(masks)**2*2*13
 x.ck(COUNTS['states']==expected,'frozen ordered history count')
 x.ck(time.perf_counter()-START<(55 if mode=='pilot' else 240),'frozen runtime')
 result={'status':'PASS','mode':mode,'ordered_pairs':len(masks)**2,'reference_fixtures_per_pair':2,'history_states_per_fixture':13,'counts':COUNTS,'exact_assertions':x.COUNT,'seconds':time.perf_counter()-START,'records':records}
 (ROOT/'out'/f'{mode.upper()}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':main(sys.argv[1])
