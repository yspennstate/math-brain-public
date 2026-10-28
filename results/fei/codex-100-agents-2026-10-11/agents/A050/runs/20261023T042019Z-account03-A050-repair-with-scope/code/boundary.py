from pathlib import Path
src=(Path(__file__).parent/'reset.py').read_text(encoding='utf-8').split("pilot='--pilot'")[0]
exec(compile(src,str(Path(__file__).parent/'reset.py'),'exec'),globals())
cases=0
for r in (7,8):
 for den in (11,7):
  for prefix in (0,1):run2((r,),'both',den,prefix);cases+=1
res=dict(status='PASS',histories=cases,checkpoints=2*cases,assertions=COUNT,primitive_assertions=E.COUNT,physical_query_nodes=NODES,reset_nodes_positive=POSITIVE,reset_nodes_negative=NEGATIVE,reset_nodes_zero=ZERO,runtime_seconds=time.perf_counter()-START,scope='MANUALLY frozen width7 width-only boundary and width8 total-load theorem; no automatic n increase')
save('BOUNDARY.json',res);print(json.dumps(res))
