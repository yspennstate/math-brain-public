import itertools,json,pathlib
P=pathlib.Path(__file__).parent
rows=[]
for m in range(2,7):
 choices=[[b for b in range(m) if b!=a] for a in range(m)]
 count=0;cycle_types={}
 for T in itertools.product(*choices):
  alive=set(range(m));peeled=0
  while True:
   incoming={a:0 for a in alive}
   for a in alive:incoming[T[a]]+=1
   leaves=[a for a in alive if incoming[a]==0]
   if not leaves:break
   for a in leaves:alive.remove(a);peeled+=1
  seen=set();lengths=[]
  for a in sorted(alive):
   if a in seen:continue
   cycle=[];v=a
   while v not in cycle:cycle.append(v);seen.add(v);v=T[v]
   assert v==a and len(cycle)>=2
   lengths.append(len(cycle))
  assert peeled+sum(lengths)==m
  key=','.join(map(str,sorted(lengths)));cycle_types[key]=cycle_types.get(key,0)+1;count+=1
 rows.append({'vertices':m,'all_nonself_maps_checked':count,'remaining_cycle_types':cycle_types})
(P/'nearest_neighbor_graph_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print('Functional-graph peeling checked:',sum(r['all_nonself_maps_checked'] for r in rows),'maps through m=6.')
