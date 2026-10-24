from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1];p=r/'code/check.py';s=p.read_text(encoding='utf-8')
(r/'code/check_v4_timeout.py').write_text(s,encoding='utf-8')
c=json.loads((r/'out/CHECKPOINT.json').read_text());assert c['controllers_finished']==81 and c['roots_finished']==1296 and c['faces_finished']==5184
c['status']='PASS_ROOT_DOMAIN';c['helper']='code/check_v4_timeout.py';c['helper_sha256']=hashlib.sha256(s.encode()).hexdigest()
(r/'out/ROOT_VALIDATION.json').write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8')
(r/'out/FAILED_FULL_v4.json').write_text(json.dumps({'status':'PREFIX_PHASE_RUNTIME_CAP','helper':'code/check_v4_timeout.py','root_domain':'COMPLETE_PASS; out/ROOT_VALIDATION.json','unfinished':'7776-tree prefix phase did not all finish under235-second guard; no full-prefix certificate claimed','reported_assertion_failures':0},indent=2)+'\n',encoding='utf-8')
s=s.replace('PILOT=\'--pilot\' in sys.argv',"PILOT='--pilot' in sys.argv\nPREFIX_ONLY='--prefix-only' in sys.argv")
s=s.replace('else: roots=named','else: roots=[] if PREFIX_ONLY else named')
s=s.replace('(58 if PILOT else 235)','(58 if PILOT else 595)')
s=s.replace("    (ROOT/'out'/'CHECKPOINT.json').write_text", "    (ROOT/'out'/'CHECKPOINT_PREFIX_INIT.json').write_text")
needle="        if time.perf_counter()-START>(58 if PILOT else 595): raise TimeoutError('Frozen execution cap')\n\n# Independent boundary"
replacement="        if time.perf_counter()-START>(58 if PILOT else 595): raise TimeoutError('Frozen execution cap')\n    (ROOT/'out'/'PREFIX_CHECKPOINT.json').write_text(json.dumps({'controllers_finished':controllers.index(ctrl)+1,'trees_finished':TREECOUNT,'distinct_prefix_states':NODECOUNT,'exact_assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'status':'IN_PROGRESS'},indent=2)+'\\n',encoding='utf-8')\n\n# Independent boundary"
assert needle in s;s=s.replace(needle,replacement)
s=s.replace("name='PILOT.json' if PILOT else 'VALIDATION.json'","name='PILOT.json' if PILOT else 'PREFIX_VALIDATION.json' if PREFIX_ONLY else 'VALIDATION.json'")
p.write_text(s,encoding='utf-8');print('Preserved completed root domain; prepared only unfinished prefix phase.')
