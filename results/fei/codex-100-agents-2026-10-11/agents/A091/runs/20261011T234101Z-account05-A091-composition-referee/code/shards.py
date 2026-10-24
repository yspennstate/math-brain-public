import subprocess,sys,json,time
from pathlib import Path
root=Path(__file__).resolve().parents[1]
start=time.perf_counter(); results=[]
for law in range(3):
    for lo in range(0,256,16):
        cmd=[sys.executable,'-X','utf8',str(root/'code/check.py'),'--law',str(law),'--start',str(lo),'--end',str(lo+16)]
        p=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
        if p.returncode:
            (root/'out/SHARD_FAILURE.json').write_text(json.dumps({'command':cmd,'stdout':p.stdout,'stderr':p.stderr},indent=2))
            raise RuntimeError(p.stderr)
        result=json.loads(p.stdout);results.append(result)
        print('PASS law='+str(law)+' masks='+str(lo)+':'+str(lo+16),flush=True)
summary={'status':'PASS','shards':len(results),'blocks':sum(r['blocks'] for r in results),'adaptive_trees':sum(r['adaptive_trees'] for r in results),'visited_internal_nodes':sum(r['visited_internal_nodes'] for r in results),'exact_assertions':sum(r['exact_assertions'] for r in results),'runtime_seconds':time.perf_counter()-start,'failed_unsharded_attempt':'law0 watchdog; superseded by complete disjoint mask slices'}
(root/'out/SHARDS.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)
