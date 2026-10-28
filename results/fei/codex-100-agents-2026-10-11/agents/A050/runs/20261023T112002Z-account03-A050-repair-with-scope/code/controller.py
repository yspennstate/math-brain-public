from pathlib import Path
src=(Path(__file__).parent/'reset.py').read_text(encoding='utf-8').split("pilot='--pilot'")[0]
exec(compile(src,str(Path(__file__).parent/'reset.py'),'exec'),globals())

def coretarget(v,widths):
 q={0:F(1)};off=3
 for r in widths:
  bits=list(range(off,off+r));left=[i for i in bits if i not in v['assigned']]
  killed=any(v['assigned'].get(i)==0 for i in bits)
  if killed or not left:qq={0:F(1)}
  elif len(left)==1:qq={1<<left[0]:F(1)}
  else:
   k=len(left);d=F(1,1<<k);vv=4*d*(1-d);fm=sum(1<<i for i in left);qq={0:(1-2*d)**2}
   for s in range(1,1<<k):
    mask=sum(1<<i for j,i in enumerate(left) if s>>j&1)
    qq[mask]=F(6,7)*4*d*d+(vv/7 if mask==fm else 0)
  q={s|u:w*a for s,w in q.items() for u,a in qq.items()};off+=r
 ck(sum(q.values())==1);return q

def core_reset(v,widths):
 p,_=spectrum(v['t'],v['co']);q=coretarget(v,widths)
 sig=E.add(E.kl(p,q),E.scale(E.kl(p,v['q']),-1));ge(E.scale(sig,-1))
 z=dict(v);z['q']=q;return z,E.scale(sig,v['w'])

def surplus(v):
 p,ii=spectrum(v['t'],v['co']);S=E.add({2:4*sum(ii.values())},E.scale(ent(p),-1));ge(S)
 if 0 in v['co']:
  j=v['co'].index(0);g=E.restrict(v['t'],j,1);cc=tuple(i for i in v['co'] if i!=0)
  pg,ig=spectrum(g,cc);mu=F(sum(g),len(g));sg=E.add({2:4*sum(ig.values())},E.scale(ent(pg),-1))
  ge(E.add(sg,{2:abs(mu)-1}))
 return S

def case(widths,rule,prefix):
 t,q=het(widths);full,P,I,Q=lift(t,q);co=tuple(range(len(full).bit_length()-1));H=ent(P);A=E.kl(P,Q);It=sum(I.values());M=E.add({2:4*It},E.scale(E.add(H,A),-1))
 bs,rel=query(rec(F(1),full,co,Q),2);rows=[bs[0]];active=[bs[1]]
 if prefix:active,rr=query(active[0],3);rel=E.add(rel,rr)
 first=[];sig1={};later={};xs=0
 for v in active:
  aa,rr=query(v,1);rel=E.add(rel,rr)
  for v in aa:
   v,ss,tt=reset(v,widths,F(1,7));sig1=E.add(sig1,ss);first.append(v)
 current=[]
 for v in first:
  data=[i for i in v['co'] if i>=3]
  if data:
   kids,rr=query(v,min(data) if v['sign']==0 else max(data));rel=E.add(rel,rr)
  else:kids=[v]
  for v in kids:
   v,ss,tt=reset(v,widths,F(1,7));ge(E.scale(ss,-1));later=E.add(later,ss);surplus(v);current.append(v)
 before=view(rows+current,A,H,It,rel,sig1,later,M)
 for v in current:
  j=v['co'].index(0);g=E.restrict(v['t'],j,1);mu=F(sum(g),len(g));s=1-2*v['sign']
  chosen=rule=='both' or rule=='plus' and s==1 or rule=='minus' and s==-1 or rule=='aligned' and s*mu>=0 or rule=='antialigned' and s*mu<0
  if not chosen:rows.append(v);continue
  xx,rr=query(v,0);rel=E.add(rel,rr);xs+=1
  # The complete constant sibling remains on its inherited full law.
  rows.append(xx[0]);v,ss=core_reset(xx[1],widths);later=E.add(later,ss)
  data=[i for i in v['co'] if i>=3]
  if data:
   kids,rr=query(v,min(data));rel=E.add(rel,rr)
   for k in kids:
    k,ss=core_reset(k,widths);later=E.add(later,ss);rows.append(k)
  else:rows.append(v)
 for v in rows:surplus(v)
 after=view(rows,A,H,It,rel,sig1,later,M)
 obj={'widths':widths,'selected_x_rule':rule,'prefix':prefix,'x_queries':xs,'original_source_KL':E.serial(A),'original_margin':E.serial(M),'before_x':before,'after_x_and_core_query_reset':after,'old_booking':'1/4, no new bank'}
 save('CASE_'+('_'.join(map(str,widths)))+'_'+rule+f'_p{prefix}.json',obj)
 return xs

pilot='--pilot' in sys.argv;roots=[(2,)] if pilot else [(2,),(3,),(4,),(2,3),(3,3)];prefixes=[0] if pilot else [0,1]
cases=xs=0
for ws in roots:
 for rule in ['aligned','antialigned','both','plus','minus']:
  for prefix in prefixes:xs+=case(ws,rule,prefix);cases+=1
res={'status':'PASS','histories':cases,'checkpoints':2*cases,'selected_x_queries':xs,'assertions':COUNT,'primitive_assertions':E.COUNT,'physical_query_nodes':NODES,'retained_reference_only_rows':GHOSTS,'runtime_seconds':time.perf_counter()-START,'scope':'specified finite histories; analytic proof supplies all-width/arbitrary-selected-frontier theorem'}
save('PILOT.json' if pilot else 'CHECK.json',res);print(json.dumps(res))
