from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1];old=R.parent/'20261023T014805Z-account03-A047-boundary-search/code/check.py'
exec(compile(old.read_text(encoding='utf-8').split('cases=')[0],str(old),'exec'))
ROOT=R
def fresh_activation(n,m,r):
 t=n['t'];cc=n['cc'];p,_=spec(t);jx=cc.index(0)
 tc=restrict(t,jx,1);dc=tuple(c for c in cc if c!=0);qcore=fresh_core(tc,dc,m,r,F(1,6))
 q={s:p.get(s,F(0)) for s in [0,1<<jx]}
 for s,w in qcore.items():
  if s:
   target=(s&((1<<jx)-1))|((s>>jx)<<(jx+1));q[target]=w/4;q[target|(1<<jx)]=w/4
 return {s:w for s,w in q.items() if w}
def history(m,r,prefix):
 global DEBITS
 DEBITS={};t=table(m,r);q=root_ref(m,r);cc=tuple(range(3+m*r));p,I0=spec(t);H0=ent(p);A0=kl(p,q)
 b=query(node(t,cc,q,F(1)),2);leaves=[b[0]];active=[b[1]]
 if prefix:active=query(active[0],3)
 for n in active:leaves.extend(query(n,1))
 oldK=totals(leaves)[2]
 for n in leaves[1:]:n['q']=fresh_activation(n,m,r)
 sigma1=add(totals(leaves)[2],scale(oldK,-1));ck(bounds(sigma1)[0]>0)
 sigma2={};transactions=0;frontiers=0
 while True:
  changed=False;new=[]
  for n in leaves:
   pn,_=spec(n['t']);choices=[c for j,c in enumerate(n['cc']) if c>=3 and any(s>>j&1 for s in pn)]
   if 1 in n['cc'] or not choices:new.append(n);continue
   changed=True;jx=n['cc'].index(0);eps=restrict(n['t'],jx,0)[0]
   # Divergent sign-conditioned query order, all physical children retained.
   kids=query(n,min(choices) if eps==1 else max(choices));oldKL=totals(kids)[2]
   for k in kids:k['q']=fresh_activation(k,m,r)
   bill=add(totals(kids)[2],scale(oldKL,-1));ck(not bill or bounds(bill)[1]<=0)
   sigma2=add(sigma2,bill);transactions+=1;new.extend(kids)
  leaves=new;Hf,If,Kf=totals(leaves);S=add({2:4*If},scale(Hf,-1));edge=add(H0,scale(Hf,-1),{2:-4*(I0-If)})
  net=add(A0,edge,sigma1,sigma2);remaining=bounds(S)[0]-max(F(0),bounds(net)[1])-F(1,4)
  ck(bounds(S)[0]>=1);ck(remaining>=F(3,4));ck(sum(k['w'] for k in leaves)==1)
  chain=bounds(add(A0,sigma1,sigma2,scale(DEBITS,-1),scale(Kf,-1)))
  ck(chain[0]<=0<=chain[1] and chain[1]-chain[0]<F(1,1<<80))
  frontiers+=1
  if not changed:break
 row={'m':m,'r':r,'prefix':prefix,'sigma1_interval':list(map(str,bounds(sigma1))),'later_reset_interval':list(map(str,bounds(sigma2))),'transactions':transactions,'complete_frontiers':frontiers,'terminal_count':len(leaves),'S_interval':list(map(str,bounds(S))),'remaining_lower':str(remaining),'old_quarter':'1/4','same_original_source_account':True,'source_chain':'exact per-atom likelihood identity plus reset telescoping; interval equality diagnostic only','divergent_sign_query_orders':True}
 save(f'HISTORY_m{m}_r{r}_p{prefix}.json',row);return row
fixtures=[(1,2,0)] if '--pilot' in sys.argv else [(1,2,0),(1,3,0),(2,2,0),(2,3,1)]
rows=[history(*z) for z in fixtures]
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_nodes':NODES,'runtime_seconds':time.perf_counter()-START,'post_first_reset_transactions':sum(x['transactions'] for x in rows),'rows':rows}
save('HISTORY_PILOT.json' if '--pilot' in sys.argv else 'HISTORY.json',result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
