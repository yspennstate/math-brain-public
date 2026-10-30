from pathlib import Path
import subprocess,sys,json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();results=[]
jobs=[['--phase','controllers','--start',str(lo),'--end',str(lo+9)] for lo in range(0,81,9)]
jobs += [['--phase','activation','--n',str(n)] for n in range(3)]
jobs += [['--phase','activation','--n','3','--start',str(lo),'--end',str(lo+16)] for lo in range(0,256,16)]
for args in jobs:
    if time.perf_counter()-start>1500:raise RuntimeError('frozen driver watchdog')
    cmd=[sys.executable,'-X','utf8',str(R/'code/check.py')]+args
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
    if p.returncode:
        (R/'out/SHARD_FAILURE.json').write_text(json.dumps({'command':cmd,'stdout':p.stdout,'stderr':p.stderr},indent=2));raise RuntimeError(p.stderr)
    result=json.loads(p.stdout);results.append(result);print('PASS '+str(args),flush=True)
summary={'status':'PASS','completed_shards':len(results),'runtime_seconds':time.perf_counter()-start,'counted_exact_assertions':sum(v['counted_exact_assertions'] for v in results),'frontiers':sum(v['frontiers'] for v in results),'phase_totals':{phase:{k:sum(v[k] for v in results if v['phase']==phase) for k in ['roots','trees','frontiers','counted_exact_assertions']} for phase in ['controllers','activation']},'constants_rational':results[0]['constants_rational'],'initial_unsharded_attempt':'watchdog; superseded by exact full slice union'}
(R/'out/CHECK.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)
