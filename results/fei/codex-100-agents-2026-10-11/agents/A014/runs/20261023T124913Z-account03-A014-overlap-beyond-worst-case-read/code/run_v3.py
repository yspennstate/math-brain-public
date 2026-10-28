from pathlib import Path
import sys,json,time,runpy,contextlib
R=Path(__file__).resolve().parents[1]
for source,target in [('checkpoint.json','timeout_v2_checkpoint.json'),('pilot.json','pilot_v2.json'),('RUNNER.json','RUNNER_v2.json')]:
    if not (R/'out'/target).exists():(R/'out'/target).write_bytes((R/'out'/source).read_bytes())
with (R/'out/ATTEMPTS.txt').open('a',encoding='utf-8',newline='\n') as f:f.write('V2 full child terminated by its own runner at explicit300-second wall cap. No complete full output. Pilot enclosing wall87.0680733s exceeded60s although internal checker passed. V3 changes log evaluator to directed integer intervals; domains/caps unchanged.\n')
current=(R/'code/check.py').read_text(encoding='utf-8')
assert current.count('from rigorous_log import lg\n')==1
v2=current.replace('from rigorous_log import lg\n','').replace('profile-v3','profile-v2')
(R/'code/check_v2.py').write_text(v2,encoding='utf-8',newline='\n')
rows=[]
for script,args,label in [('check.py',['--pilot'],'pilot_v3'),('check.py',[],'full_v3'),('history.py',[],'history_v3'),('scalar.py',[],'scalar_v3')]:
    start=time.monotonic();sys.argv=[str(R/'code'/script)]+args
    with (R/f'out/{label}.log').open('w',encoding='utf-8',newline='\n') as out:
        with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):runpy.run_path(str(R/'code'/script),run_name='__main__')
    elapsed=time.monotonic()-start;assert elapsed<(60 if args else 300)
    rows.append({'script':script,'args':args,'returncode':0,'elapsed_seconds':elapsed})
    (R/'out/RUNNER_v3.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(rows[-1]),flush=True)
