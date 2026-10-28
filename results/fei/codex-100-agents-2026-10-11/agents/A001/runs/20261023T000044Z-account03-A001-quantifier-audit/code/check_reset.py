from helpers import *
import helpers

def CE(p,q):
 ck(len(p)==len(q) and sum(q)==1)
 ck(all(b>0 for a,b in zip(p,q) if a))
 return add(*[(-a,log(b)) for a,b in zip(p,q) if a])
def marginal(p,j):
 return tuple(p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2))
def mix(q):return tuple(F(7,8)*x+F(1,8*len(q)) for x in q)
def rec(d):
 a,b=interval(d)
 return {'prime_log':enc(d),'interval':[str(a),str(b)],'millionth_enclosure':[(a*10**6).__floor__(),(b*10**6).__ceil__()]}

start=time.perf_counter()
b=[1 if y&7==0 else -1 for y in range(64)];c=b[:];c[0]=-1
v=tuple(encoded(b,c));p=tuple(spectrum(v));H=entropy(p)
children=[tuple(transport(v,6,s)) for s in (0,1)]
pc=[tuple(spectrum(w)) for w in children]
old=mix(marginal(p,6));ck(min(old)>0)
firstB=erase(v,6)
first=add((1,firstB),*[(F(1,2),CE(q,old)) for q in pc])
oldmargin=add((1,const(3)),(-1,first));ck(interval(oldmargin)[0]>0)
# Data y3=0 child, with five data bits and three encoder bits.
qdata=pc[0]
for _ in range(3):qdata=marginal(qdata,0)
ck(len(qdata)==32 and min(qdata)>0)
g=tuple(-1 if y&7==0 else 1 for y in range(32));pg=tuple(spectrum(g))
mu=F(3,4);e=F(1,32);s=F(1,8)
V=tuple(mu*mu if t==0 else (1-mu*mu)/31 for t in range(32))
ck(sum(V)==1 and V[0]==pg[0])
rows=[];crossed=[]
domain=[F(0),F(1)] if '--pilot' in sys.argv else [F(0),F(1,4),F(1,2),F(3,4),F(1)]
floors={}
for lam in domain:
 ck(time.perf_counter()-start<55)
 R=tuple((1-lam)*a+lam*z for a,z in zip(pg,V))
 Rp=tuple((1-e/s)*a+(e/s)*mu*(t==0)+2*e/32 for t,a in enumerate(R))
 ck(sum(R)==sum(Rp)==1 and min(Rp)>0)
 if not lam:ck(Rp==qdata)
 Q=tuple(Rp[t>>3]*mass/qdata[t>>3] for t,mass in enumerate(pc[0]))
 ck(sum(Q)==1 and all(z>0 for mass,z in zip(pc[0],Q) if mass))
 removed=[j for j,(a,z) in enumerate(zip(old,Q)) if a and not z]
 ck(len(removed)>0 and all(pc[0][j]==0 for j in removed))
 for t in range(32):ck(sum(Q[t*8:(t+1)*8])==Rp[t])
 floors[lam]=Q
 Z=add((1,CE(pc[0],Q)),(-1,CE(pc[0],old)))
 complete=add((1,first),(F(1,2),Z))
 direct=add((1,firstB),(F(1,2),CE(pc[0],Q)),(F(1,2),CE(pc[1],old)))
 ck(complete==direct)
 margin=add((1,const(3)),(-1,complete))
 # Keep the original terminal escrow and root increment; no child-bank renewal.
 T0=add((F(1,2),entropy(spectrum(b))),(F(1,2),entropy(spectrum(c))))
 S=add((1,const(3)),(-1,T0))
 ck(margin==add((1,S),(-1,add((1,H),(-1,T0))),(-1,add((1,first),(-1,H))),(F(-1,2),Z)))
 lo,hi=interval(margin);ck(lo>0 or hi<0)
 Qoff=tuple(R[t>>3] if (t&7)==0 else F(0) for t in range(256))
 ck(sum(Qoff)==1)
 Zoff=add((1,CE(pc[1],Qoff)),(-1,CE(pc[1],old)))
 bothmargin=add((1,margin),(F(-1,2),Zoff))
 a,bound=interval(bothmargin);ck(a>0 or bound<0)
 for alpha in [F(0),F(3,4),F(1)]:
  Roff=tuple((1-alpha)*a+alpha*z for a,z in zip(pg,V))
  Qother=tuple(Roff[t>>3] if (t&7)==0 else F(0) for t in range(256))
  priceoff=add((1,CE(pc[1],Qother)),(-1,CE(pc[1],old)))
  final=add((1,margin),(F(-1,2),priceoff))
  directfinal=add((1,const(3)),(-1,firstB),(F(-1,2),CE(pc[0],Q)),(F(-1,2),CE(pc[1],Qother)))
  ck(final==directfinal)
  flo,fhi=interval(final);ck(flo>0 or fhi<0)
  crossed.append({'lambda':str(lam),'alpha':str(alpha),'opposite_actual_signed_reset':rec(priceoff),'remaining_same_ancestor':rec(final),'outcome':'PAID' if flo>0 else 'FAILS'})
 # Actual KL, not a reference-only worst atom, prices this prescribed reset.
 kl=add((1,CE(pc[0],Q)),(-1,entropy(pc[0])))
 ck(not kl or interval(kl)[0]>0)
 rows.append({'lambda':str(lam),'actual_signed_reset':rec(Z),'canonical_terminal_KL':rec(kl),'complete_bill':rec(complete),'same_original_margin':rec(margin),'outcome':'PAID' if lo>0 else 'FAILS','canonical_reference_sha256':__import__('hashlib').sha256(str(Q).encode()).hexdigest(),'inherited_positive_removed_actual_zero_atoms':len(removed),'complementary_reset_signed_cost':rec(Zoff),'after_both_canonical_resets_margin':rec(bothmargin),'both_canonical_outcome':'PAID' if a>0 else 'FAILS'})
if F(0) in floors and F(1) in floors:
 for lam,Q in floors.items():ck(Q==tuple((1-lam)*a+lam*z for a,z in zip(floors[F(0)],floors[F(1)])))
out={'status':'PASS','assertions':helpers.count,'seconds':time.perf_counter()-start,'cases':len(rows),'crossed_cases':len(crossed),'old_frontier_margin':rec(oldmargin),'root_H':rec(H),'rows':rows,'crossed':crossed,'scope':'complete prescribed reset after y3, old uniform reset in both branches retained; no arbitrary-core statement'}
(RUN/'out'/('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'assertions':out['assertions'],'seconds':out['seconds'],'crossed_cases':len(crossed),'corner':[(x['lambda'],x['alpha'],x['outcome'],x['remaining_same_ancestor']['millionth_enclosure']) for x in crossed if x['lambda']=='1']}))
