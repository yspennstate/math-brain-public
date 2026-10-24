import shared as sh
from prior import *

N=0
def ck(x):
 global N
 N+=1
 assert x

def fresh(f):
 p0=mean(f)**2;v=1-p0
 if len(f)==1:return (Q(1),)
 weights=[Q(1<<(j-1)) for j in range(1,len(f))]
 return (p0,)+tuple(v*w/sum(weights) for w in weights)

def pos(x):return x if nonnegative(x) else {}

def scalar_checks():
 source=[];endpoint=[]
 for code in range(256):
  f=table(3,code);cost=ce(prob(f),phase_ref(f,False));margin=add({2:3*influence(f)},cost,-1)
  ck(nonnegative(margin));source.append({'code':code,'I':str(influence(f)),'CE':ser(cost),'source3I_margin':ser(margin)})
 for k in range(3):
  for code in range(1<<(1<<k)):
   f=table(k,code);rr=fresh(f);cost=ce(prob(f),rr)
   ck(sum(rr)==1);ck(rr[0]==mean(f)**2)
   ck(nonnegative(add({2:3*influence(f)},cost,-1)))
   endpoint.append({'bits':k,'code':code,'I':str(influence(f)),'CE':ser(cost)})
 return source,endpoint

def reset_state(s):
 ru,rv=fresh(s.u),fresh(s.v)
 ck(len(s.u)<=4)
 for old,new,f in [(s.ru,ru,s.u),(s.rv,rv,s.v)]:
  ck(sum(new)==1);ck(new[0]==old[0]==mean(f)**2)
  for j in range(1,len(new)):ck(new[j]*7>=old[j])
  delta=add(ce(prob(f),new),ce(prob(f),old),-1)
  ck(nonnegative(add({2:3*influence(f)},delta,-1)))
 c=State(s.u,s.v,ru,rv,s.na,s.nb,s.ea,s.eb,s.z)
 du=add(c.cu,s.cu,-1);dv=add(c.cv,s.cv,-1)
 pu=scale(du,s.pi*s.a*(1-s.a));pv=scale(dv,(1-s.pi)*s.b*(1-s.b))
 price=add(pu,pv)
 ck(price==add(c.CE,s.CE,-1))
 ck(nonnegative(add({2:7*c.I},c.CE,-1)))
 # Original reset flags are consumed here; source references are fully
 # replaced by fresh(), with no interpolation parameter or inherited atom.
 positive=add(pos(pu),pos(pv))
 ck(nonnegative(add({2:3*s.core},positive,-1)))
 return c,price,positive

def history(s,i,kind):
 first,cs=sh.shared(s,i)
 old=[];prefix_normalizers=[]
 for c in cs:
  ds=transport(c,kind);old.extend(ds)
  def zero(j0):
   am=(j0>>c.k)&((1<<c.na)-1);bm=(j0>>(c.k+c.na))&((1<<c.nb)-1);owner=c.label(j0)[0]
   if kind=='z' and owner in ['a','b']:return [Q(owner=='a'),Q(owner=='b')]
   if (kind=='A' and am and c.ea) or (kind=='B' and bm and c.eb):return [Q(1),Q(0)]
   return [Q(1,2)]*2
  raw=sh.pull(c.P,c.Q,[d.P for d in ds],c.index(kind),zero)
  zs=[sum(q) for q in raw]
  ck(all(z>0 for z in zs));ck(sum(zs)==1)
  prefix_normalizers.append([str(z) for z in zs])
 old_terminal={};reset_terminal={};price={};positive={};source_owner=Q(0);reset_states=[]
 for d in old:
  c,p,pp=reset_state(d);reset_states.append(c)
  old_terminal=add(old_terminal,d.CE,Q(1,4));reset_terminal=add(reset_terminal,c.CE,Q(1,4))
  price=add(price,p,Q(1,4));positive=add(positive,pp,Q(1,4));source_owner+=d.core/4
 ck(add(reset_terminal,old_terminal,-1)==price)
 old_debit=add(s.CE,old_terminal,-1);ck(nonnegative(old_debit))
 spent=edge_inf(s.f,i)+sum((edge_inf(c.f,c.index(kind)) for c in cs),Q(0))/2
 ck(s.I==spent+sum((d.I for d in old),Q(0))/4)
 ck(source_owner<=s.core)
 ck(nonnegative(add({2:3*s.core},positive,-1)))
 original_bound=add(add(scale(s.cu,s.pi*s.a),s.cv,(1-s.pi)*s.b),{2:s.core+7*s.ctrl})
 unused=add(add({2:7*s.I},original_bound,-1),positive,-1)
 ck(nonnegative(unused))
 final={};remaining=Q(0);post_spent=Q(0);normalizers=[];fullkl={}
 for c in reset_states:
  rec,ds=sh.shared(c,0);normalizers.append(rec['root_normalizers'])
  post_spent+=edge_inf(c.f,0)/4
  for d in ds:
   final=add(final,d.CE,Q(1,8));remaining+=d.I/8;fullkl=add(fullkl,d.debt,Q(1,8))
 ck(s.I==spent+post_spent+remaining)
 post_debit=add(reset_terminal,final,-1);ck(nonnegative(post_debit))
 # Complete actual-channel ledger includes the old debit and every full
 # complementary terminal; the signed reset is not dropped or renewed.
 complete=add(add(old_debit,post_debit),final)
 ck(complete==add(s.CE,price))
 ck(nonnegative(add({2:7*s.I},complete,-1)))
 ck(nonnegative(add({2:7*remaining},final,-1)))
 return {'shared_query':i,'private_query':kind,'old_spent_influence':str(spent),'new_spent_influence':str(post_spent),'remaining_influence':str(remaining),'signed_reset_price':ser(price),'positive_reset_debit':ser(positive),'old_actual_CE_debit':ser(old_debit),'post_actual_CE_debit':ser(post_debit),'full_final_terminal_CE':ser(final),'full_final_terminal_KL':ser(fullkl),'unused_original_rate7_capacity':ser(unused),'both_first_children_nonconstant':all(c.I>0 for c in cs),'all_four_reset_states_nonconstant':all(c.I>0 for c in reset_states),'first_query_root_normalizers':first['root_normalizers'],'first_query_phase_u_normalizers':first['phase_u_normalizers'],'first_query_phase_v_normalizers':first['phase_v_normalizers'],'private_prefix_normalizers':prefix_normalizers,'post_query_normalizers':normalizers,'fresh_u_reference_example':[str(q) for q in reset_states[0].ru]},len(reset_states)

def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;lane=int(sys.argv[sys.argv.index('--lane')+1]) if '--lane' in sys.argv else None
 source,end=scalar_checks();pairs=[(85,1),(1,16),(2,1),(105,150),(23,113),(7,31),(128,127),(3,63)]
 domain=[]
 for uc,vc in pairs:
  for na,nb in [(0,0),(0,1),(1,0),(1,1),(2,1)]:
   kinds=(['A'] if na else [])+(['B'] if nb else [])+['z']
   for i in range(3):
    for kind in kinds:domain.append((uc,vc,na,nb,i,kind))
 ck(len(domain)==264)
 if pilot:domain=[(85,1,2,1,1,'A')]
 elif lane is not None:domain=[x for j,x in enumerate(domain) if j%2==lane]
 records=[];states=positive=both=0
 for uc,vc,na,nb,i,kind in domain:
  if time.perf_counter()-start>55:raise RuntimeError('Frozen55second limit')
  u,v=table(3,uc),table(3,vc);s=State(u,v,phase_ref(u,False),phase_ref(v,False),na,nb)
  try:rec,n=history(s,i,kind)
  except Exception:
   (R/'out/FAILURE.json').write_text(json.dumps({'u':uc,'v':vc,'widths':[na,nb],'i':i,'kind':kind,'assertions_completed':N},indent=2),encoding='utf-8');raise
  rec.update(u=uc,v=vc,widths=[na,nb]);records.append(rec);states+=n
  positive+=bool(rec['positive_reset_debit']);both+=rec['all_four_reset_states_nonconstant']
 result={'status':'PASS','helper_version':'A056-prescribed-fresh-reset-v1','pilot':pilot,'lane':lane,'source_functions':len(source),'endpoint_functions':len(end),'histories':len(records),'reset_states':states,'post_reset_shared_queries':states,'positive_reset_histories':positive,'all_four_reset_states_nonconstant_histories':both,'own_assertions':N,'transport_assertions':sh.COUNT,'runtime_seconds':time.perf_counter()-start,'source_certificates':source,'endpoint_certificates':end,'histories_with_all_costs':records}
 name='pilot.json' if pilot else f'lane{lane}.json' if lane is not None else 'checks.json'
 (R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ['source_certificates','endpoint_certificates','histories_with_all_costs']},indent=2))
if __name__=='__main__':main()
