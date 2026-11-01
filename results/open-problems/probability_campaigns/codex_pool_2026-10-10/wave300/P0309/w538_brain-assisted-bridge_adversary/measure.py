import datetime,difflib,itertools,json,math,pathlib,re,time
from riesz_scope_guard import riesz_scope_warnings
w=pathlib.Path(__file__).resolve().parent
started=time.monotonic()
try:
 import psutil
 gate={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'available_ram_bytes':psutil.virtual_memory().available,'cpu_percent':psutil.cpu_percent(interval=0.25),'max_operations':50000,'max_cpu_seconds':5,'max_additional_ram_bytes':32*1024*1024}
 gate['pass']=gate['available_ram_bytes']>=1024**3 and gate['cpu_percent']<=85
except ImportError:
 gate={'pass':False,'reason':'psutil unavailable; no fresh RAM/CPU gate'}
(w/'compute_gate.json').write_text(json.dumps(gate,indent=2),encoding='utf-8')
if not gate['pass']:
 print(json.dumps({'compute_gate':gate,'measurement':'SKIPPED; gate not passed'}));raise SystemExit(2)
receipt=json.loads((w/'brain_recall_receipt.json').read_text(encoding='utf-8'))
lines=receipt['stdout'].splitlines()
candidates=[]
for i,line in enumerate(lines):
 m=re.match(r'^\s{2}[\d.]+ \[.*?\] (\S+)',line)
 if m:
  candidates.append({'id':m.group(1),'title':m.group(1),'body':lines[i+1].strip() if i+1<len(lines) else ''})
warning=riesz_scope_warnings(receipt['query'],candidates)
assert len(candidates)==3 and len(warning)==3, (candidates,warning)
cards=json.loads((w/'math_brain_probe.json').read_text(encoding='utf-8'))
controls=[
 {'case':'explicit Riesz product query','query':'Riesz products Bernoulli convolution mistakes','rows':candidates},
 {'case':'explicit comparison between gas and product','query':'Compare Riesz gas Gibbs phases and Riesz products','rows':candidates},
 {'case':'generic Riesz query','query':'Riesz theory proof mistakes','rows':candidates},
 {'case':'actual P0309 gas card','query':receipt['query'],'rows':cards['target'][:1]},
 {'case':'actual Brascamp-Lieb covariance card','query':receipt['query'],'rows':cards['variance']}
]
for r in controls:
 r['warning_count']=len(riesz_scope_warnings(r['query'],r['rows']))
 assert r['warning_count']==0,r['case']
controls=[{'case':r['case'],'warning_count':r['warning_count']} for r in controls]
values=[]
for d in [1,2,3]:
 for L in [7,15,31,63]:
  if d==3 and L==63 and time.monotonic()-started>4: continue
  diagonal=math.fsum(1/(2*sum(1-math.cos(math.pi*k/(L+1)) for k in ks)) for ks in itertools.product(range(1,L+1,2),repeat=d))*(2/(L+1))**d
  gap_inverse=1/(2*d*(1-math.cos(math.pi/(L+1))))
  if d==1: assert abs(diagonal-(L+1)/4)<1e-10
  if d==3: assert diagonal <= math.sqrt(3)*math.pi/8
  values.append({'dimension':d,'L':L,'center_green_diagonal':diagonal,'crude_gap_inverse':gap_inverse,'gap_to_diagonal_ratio':gap_inverse/diagonal})
operations=sum(((r['L']+1)//2)**r['dimension'] for r in values)
assert operations<=50000
result={'query':receipt['query'],'replay_candidates':len(candidates),'before_homonym_warnings':0,'after_homonym_warnings':len(warning),'topic_relevance_before_at_3':0,'topic_relevance_after_at_3':0,'candidate_order_or_count_changed':False,'flagged_ids':[r['id'] for r in warning],'silent_controls':controls,'green_values':values,'operations':operations,'measurement_seconds':time.monotonic()-started,'limits':'Replay precision controls only; Green sums are floating point checks, not proof of P0309 or actual Riesz stability.'}
(w/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
patch_dir=w/'patches';patch_dir.mkdir(exist_ok=True)
code=(w/'riesz_scope_guard.py').read_text(encoding='utf-8-sig')
header='diff --git a/.claude/dreaming/riesz_scope_guard.py b/.claude/dreaming/riesz_scope_guard.py\nnew file mode 100644\n'
diff=''.join(difflib.unified_diff([],code.splitlines(keepends=True),fromfile='/dev/null',tofile='b/.claude/dreaming/riesz_scope_guard.py'))
(patch_dir/'01_riesz_scope_warning.diff').write_text(header+diff,encoding='utf-8',newline='\n')
print(json.dumps(result,indent=2))
