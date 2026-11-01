from pathlib import Path
src=(Path(__file__).parent/'check.py').read_text(encoding='utf-8').split('fixtures=')[0]
exec(compile(src,str(Path(__file__).parent/'check.py'),'exec'),globals())
def record(w,t,co,q):
 p,ii=spectrum(t,co);return (w,ent(p),sum(ii.values()),E.kl(p,q))
def mixed(label,t,qraw,controller,selected):
 p,ii=spectrum(t,tuple(range(len(t).bit_length()-1)));q,cal=calibrate(p,qraw)
 full,P,I,Q=lift(t,q);H=ent(P);A=E.kl(P,Q);CE=E.add(H,A);co=tuple(range(len(full).bit_length()-1))
 bs,bco,B,_,eb=node(full,co,Q,2)
 ds,dco,D,_,ed=node(bs[1],bco,B[1],3)
 rows=[record(F(1,2),bs[0],bco,B[0])];release=E.add(eb,E.scale(ed,F(1,2)))
 for bit in (0,1):
  if selected=='zero' and bit==1:
   rows.append(record(F(1,4),ds[bit],dco,D[bit]));continue
  cs,cco,C,_,ec=node(ds[bit],dco,D[bit],controller)
  release=E.add(release,E.scale(ec,F(1,4)))
  for b in (0,1):rows.append(record(F(1,8),cs[b],cco,C[b]))
 Hf={};If=F(0);KLf={}
 for w,h,i,kl in rows:Hf=E.add(Hf,E.scale(h,w));If+=w*i;KLf=E.add(KLf,E.scale(kl,w))
 close(E.add(A,E.scale(release,-1),E.scale(KLf,-1)))
 S=E.add({2:4*If},E.scale(Hf,-1));ge(E.add(S,{2:F(-1 if controller==1 else -2)}))
 edge=E.add(H,E.scale(Hf,-1),{2:-4*(sum(I.values())-If)})
 net=E.add(A,edge);lo,hi=E.bounds(net);ck(lo>0 or hi<0 or not net)
 sharp=net if lo>0 else {};reserve=E.add(S,E.scale(sharp,-1))
 ge(E.add(reserve,{2:F(-1)}));ge(E.add(reserve,{2:F(-1,4)-F(3,4)}))
 margin=E.add({2:4*sum(I.values())},E.scale(CE,-1));close(E.add(S,E.scale(net,-1),E.scale(margin,-1)))
 out={'core':label,'controller':'a' if controller==1 else 'x','selected_data_children':selected,'final_leaves':len(rows),'full_original_source_KL':E.serial(A),'all_releases':E.serial(release),'full_terminal_KL':E.serial(KLf),'final_H':E.serial(Hf),'final_I':str(If),'final_actual_S':E.serial(S),'signed_transaction':E.serial(net),'remaining_same_owner':E.serial(reserve),'old_booking':'1/4','after_old_booking_bound':'>=3/4','reference_reset':False}
 save('MIXED_'+label+f'_{controller}_{selected}.json',out);return out
fixtures=[('m1r2',core(1,2),tensorref(1,2))]
if '--pilot' not in sys.argv:
 fixtures += [('m2r2',core(2,2),tensorref(2,2)),('m2r3',core(2,3),tensorref(2,3)),('parity3',tuple((-1)**z.bit_count() for z in range(8)),{s:F(1,8) for s in range(8)})]
rows=[]
for label,t,q in fixtures:
 for controller in (0,1):
  for selected in ('all','zero'):rows.append(mixed(label,t,q,controller,selected))
res={'status':'PASS','histories':len(rows),'assertions':COUNT,'primitive_assertions':E.COUNT,'physical_nodes':NODES,'retained_reference_only_rows':GHOSTS,'runtime_seconds':time.perf_counter()-START,'all_dimensions':'analytic proof for stated supplied core/frontier certificates; these are finite controls'}
save('MIXED_PILOT.json' if '--pilot' in sys.argv else 'MIXED_CHECK.json',res);print(json.dumps(res))
