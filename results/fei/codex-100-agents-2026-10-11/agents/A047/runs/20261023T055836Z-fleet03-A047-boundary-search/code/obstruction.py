from pathlib import Path
import sys,json,time
HERE=Path(__file__).resolve().parents[1]
src=(HERE/'code/search.py').read_text(encoding='utf-8').split('for n in ([3]')[0]
exec(compile(src,str(HERE/'code/search.py'),'exec'))
logfile=ROOT/'out'/'OBSTRUCTION_CASES.jsonl';logfile.write_bytes(b'')
pilot='--pilot' in sys.argv
for flip in ([-1] if pilot else range(-1,8)):
 v=tuple((-1 if z>>1&1 else 1) if not z&1 else (-1 if z>>2&1 else 1) for z in range(8))
 if flip>=0:v=tuple(-x if z==flip else x for z,x in enumerate(v))
 t=tuple(v[z>>1] if not z&1 else (-1 if (z>>1).bit_count()%2 else 1) for z in range(16))
 examine(t,4,flip,0,'core')
 for eps in [-1,1]:
  for char in [False,True]:examine(t,4,flip,0,'activation',eps,char)
result={'status':'PASS','cases':len(rows),'positive_count':len(positive),'same_support_positive_count':sum(not z['reference_only_support'] for z in positive),'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'rows':rows}
save('OBSTRUCTION_PILOT.json' if pilot else 'OBSTRUCTION.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
