from pathlib import Path
src=(Path(__file__).parent/'check.py').read_text(encoding='utf-8').split('fixtures=')[0]
exec(compile(src,str(Path(__file__).parent/'check.py'),'exec'),globals())
POSITIVE=0;NEGATIVE=0;ZERO=0

def het(widths):
 n=sum(widths)
 def val(z):
  s=1;off=0
  for r in widths:
   if (z>>off)&((1<<r)-1)==(1<<r)-1:s=-s
   off+=r
  return s
 t=tuple(val(z) for z in range(1<<n));q={0:F(1)};off=0
 for r in widths:
  p,v=factorref(r);q={a|(b<<off):wa*wb for a,wa in q.items() for b,wb in v.items()};off+=r
 return t,q

def rec(w,t,co,q,assigned=None,sign=None):
 return dict(w=w,t=t,co=co,q=q,assigned=assigned or {},sign=sign)

def query(v,i):
 kids,cn,Q,ghost,release=node(v['t'],v['co'],v['q'],i)
 rows=[]
 for b in (0,1):
  assigned=dict(v['assigned'])
  if i>=3:assigned[i]=b
  rows.append(rec(v['w']/2,kids[b],cn,Q[b],assigned,b if i==1 else v['sign']))
 return rows,E.scale(release,v['w'])

def fresh(v,widths,alpha):
 # Reconstruct each actual conditional point from physical assignments.
 q={0:F(1)};off=3
 for r in widths:
  bits=list(range(off,off+r));left=[i for i in bits if i not in v['assigned']]
  killed=any(v['assigned'].get(i)==0 for i in bits)
  if killed or not left:qq={0:F(1)}
  elif len(left)==1:qq={1<<left[0]:F(1)}
  else:
   k=len(left);d=F(1,1<<k);vv=4*d*(1-d);full=sum(1<<i for i in left)
   qq={0:(1-2*d)**2}
   for s in range(1,1<<k):
    mask=sum(1<<i for j,i in enumerate(left) if (s>>j)&1)
    qq[mask]=(1-alpha)*4*d*d+(alpha*vv if mask==full else 0)
  q={s|u:w*a for s,w in q.items() for u,a in qq.items()};off+=r
 ck(sum(q.values())==1)
 p,ii=spectrum(v['t'],v['co']);dm=sum(1<<i for i in v['co'] if i>=3)
 # Both a children retain x. Copy ALL actual vacuum/control mass.
 Rq={s:w for s,w in p.items() if not s&dm}
 for s,w in q.items():
  if s:
   for c in (0,1):Rq[s|c]=w/4
 ck(sum(Rq.values())==1)
 ck(all(Rq.get(s,F(0))>0 for s,w in p.items() if w))
 # Verify lift KL against actual core law, independently of target generator.
 j=v['co'].index(0);g=E.restrict(v['t'],j,1);cc=tuple(i for i in v['co'] if i!=0)
 pg,_=spectrum(g,cc)
 ck(q.get(0,F(0))==pg.get(0,F(0)))
 close(E.add(E.kl(p,Rq),E.scale(E.kl(pg,q),F(-1,2))))
 return Rq

def reset(v,widths,alpha):
 global POSITIVE,NEGATIVE,ZERO
 p,_=spectrum(v['t'],v['co']);Q=fresh(v,widths,alpha)
 old=E.kl(p,v['q']);new=E.kl(p,Q);sig=E.add(new,E.scale(old,-1))
 lo,hi=E.bounds(sig)
 if not sig:ZERO+=1
 elif lo>0:POSITIVE+=1
 elif hi<0:NEGATIVE+=1
 # A sign is diagnostic only; no uncertain sign is used in payment.
 vv=dict(v);vv['q']=Q
 return vv,E.scale(sig,v['w']),E.scale(new,v['w'])

def totals(rows):
 Hf={};If=F(0);K={}
 ck(sum(v['w'] for v in rows)==1)
 for v in rows:
  p,ii=spectrum(v['t'],v['co']);w=v['w']
  Hf=E.add(Hf,E.scale(ent(p),w));If+=w*sum(ii.values());K=E.add(K,E.scale(E.kl(p,v['q']),w))
 return Hf,If,K

def view(rows,A,H,I,release,sig1,sig2,M):
 hf,ii,k=totals(rows);sigma=E.add(sig1,sig2)
 close(E.add(A,sigma,E.scale(release,-1),E.scale(k,-1)))
 S=E.add({2:4*ii},E.scale(hf,-1));ge(E.add(S,{2:-1}))
 net=E.add(A,H,E.scale(hf,-1),{2:-4*(I-ii)},sigma)
 close(E.add(S,E.scale(net,-1),E.scale(M,-1),sigma))
 ge(E.add(M,E.scale(sigma,-1),{2:-1}))
 lo,hi=E.bounds(net);ck(not net or lo>0 or hi<0)
 bank=E.add(S,E.scale(net,-1)) if lo>0 else S
 ge(E.add(bank,{2:-1}))
 after=E.add(bank,{2:F(-1,4)});ge(E.add(after,{2:F(-3,4)}))
 return dict(leaves=len(rows),S=E.serial(S),terminal_KL=E.serial(k),query_releases=E.serial(release),sigma1=E.serial(sig1),sigma2=E.serial(sig2),actual_net=E.serial(net),after_old_quarter_interval=list(map(str,E.bounds(after))))

def run2(widths,policy,den,prefix):
 t,q=het(widths);full,P,I,Q=lift(t,q);co=tuple(range(len(full).bit_length()-1));H=ent(P);A=E.kl(P,Q);It=sum(I.values());M=E.add({2:4*It},E.scale(E.add(H,A),-1))
 bs,rel=query(rec(F(1),full,co,Q),2);active=[bs[1]];rows=[bs[0]]
 if prefix:
  active,rr=query(active[0],3);rel=E.add(rel,rr)
 first=[];sig1={};T1={}
 for v in active:
  aa,rr=query(v,1);rel=E.add(rel,rr)
  for c in aa:
   c,ss,tt=reset(c,widths,F(1,7));first.append(c);sig1=E.add(sig1,ss);T1=E.add(T1,tt)
 sig2={};T2={};second=[]
 for v in first:
  chosen=policy=='both' or (policy=='plus' and v['sign']==0) or (policy=='minus' and v['sign']==1)
  if not chosen:rows.append(v);continue
  i=min(i for i in v['co'] if i>=3)
  kids,rr=query(v,i);rel=E.add(rel,rr)
  for k in kids:
   k,ss,tt=reset(k,widths,F(1,den));second.append(k);sig2=E.add(sig2,ss);T2=E.add(T2,tt)
 snapshot=view(rows+second,A,H,It,rel,sig1,sig2,M)
 # Check gross variance bounds separately; NEVER add them as extra ledger debts.
 base=sum((F(1,1<<r)*(1-F(1,1<<r)) for r in widths),F(0))
 ge(E.add({F(7,6):base},E.scale(T1,-1)))
 ge(E.add({F(den,den-1):base},E.scale(T2,-1)))
 ge(E.add(T1,T2,E.scale(E.add(sig1,sig2),-1)))
 continued=list(rows)
 for v in second:
  data=[i for i in v['co'] if i>=3]
  if data:
   kids,rr=query(v,min(data));rel=E.add(rel,rr);continued+=kids
  else:continued.append(v)
 after=view(continued,A,H,It,rel,sig1,sig2,M)
 key='r'+'_'.join(map(str,widths))+f'_{policy}_a{den}_prefix{prefix}'
 obj=dict(widths=widths,policy=policy,second_alpha=f'1/{den}',prefix=prefix,root_source_KL=E.serial(A),root_margin=E.serial(M),fresh_KL1=E.serial(T1),fresh_KL2=E.serial(T2),reset_frontier=snapshot,continued_without_reset=after,old_booking='1/4, unchanged')
 save('CASE_'+key+'.json',obj)

pilot='--pilot' in sys.argv
families=[(2,)] if pilot else [(2,),(3,),(4,),(5,),(2,2),(2,3),(3,3)]
policies=['both'] if pilot else ['plus','minus','both']
prefixes=[0] if pilot else [0,1]
cases=0
for widths in families:
 for policy in policies:
  for den in (11,7):
   for prefix in prefixes:run2(widths,policy,den,prefix);cases+=1

# Pure integer certificates underpin the analytic unbounded-width application.
ck(22**56<2**31*15**56)
ck(14**20<2**13*9**20)
ck(14**8>2**5*9**8)
ck(F(31,56)+F(14,127)>F(13,20))
ck(F(31,56)+F(16,255)<F(5,8))
for r in range(2,8):ck(F(31,56)+F(2*r,(1<<r)-1)>F(13,20))
result=dict(status='PASS',histories=cases,checkpoints=2*cases,assertions=COUNT,primitive_assertions=E.COUNT,physical_query_nodes=NODES,retained_reference_only_rows=GHOSTS,reset_nodes_positive=POSITIVE,reset_nodes_negative=NEGATIVE,reset_nodes_zero=ZERO,runtime_seconds=time.perf_counter()-START,scope='finite tests plus separate analytic cumulative-variance theorem; no all-width same1/7 sign claim')
save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps(result))
