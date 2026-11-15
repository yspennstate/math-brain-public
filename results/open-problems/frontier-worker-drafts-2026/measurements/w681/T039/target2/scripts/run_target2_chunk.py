"""Run one joined, bounded certificate chunk and save its measured prefix."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-seconds', type=int, default=360)
    ap.add_argument('--replan', action='store_true')
    cli = ap.parse_args()
    checkpoint = ROOT/'logs/fine_checkpoint.json'
    state = json.loads(checkpoint.read_text(encoding='utf-8'))
    now = datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime('%Y%m%dT%H%M%SZ')
    if cli.replan:
        endpoint = max(r['rho_hi'] for r in state['accepted'])
        assert endpoint == .418, ('Replan only once from the saved prefix', endpoint)
        before = checkpoint.read_bytes()
        (ROOT/f'logs/fine_before_replan_{stamp}.json').write_bytes(before)
        pending = []
        for a,b,denominator,n in [(836,844,2000,1600),(1688,1704,4000,2400),(1704,1720,4000,4000)]:
            pending += [[j/denominator,(j+1)/denominator,n] for j in range(a,b)]
        assert pending[0][0] == endpoint and pending[-1][1] == .43
        assert all(pending[i][1] == pending[i+1][0] for i in range(len(pending)-1))
        state['pending'] = list(reversed(pending))
        state.setdefault('replans',[]).append({'at':now.isoformat(),'reason':'Avoid already-failed wide slabs; refine cells and rho toward the endpoint. Source formulas unchanged.','previous_checkpoint_sha256':hashlib.sha256(before).hexdigest(),'new_pending':pending})
        temporary=checkpoint.with_suffix('.json.part')
        temporary.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
        temporary.replace(checkpoint)
    runlog = ROOT/f'logs/fine_chunk_{stamp}.txt'
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    command=[sys.executable,'-B','-X','utf8',str(ROOT/'scripts/run_fine_certificate.py'),'--max-seconds',str(cli.max_seconds)]
    with runlog.open('w',encoding='utf-8',newline='\n') as output:
        child=subprocess.run(command,cwd=ROOT,env=env,stdout=output,stderr=subprocess.STDOUT,check=False)
    state=json.loads(checkpoint.read_text(encoding='utf-8'))
    accepted=state['accepted']
    result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':command,'exit_code':child.returncode,'run_log':str(runlog.relative_to(ROOT)),'endpoint':max((r['rho_hi'] for r in accepted),default=.4),'accepted_slabs':len(accepted),'pending_slabs':len(state['pending']),'worst_operator_upper':max((r['operator_upper'] for r in accepted),default=None),'complete':not state['pending'] and child.returncode==0}
    with (ROOT/'logs/fine_chunks.jsonl').open('a',encoding='utf-8') as out:out.write(json.dumps(result)+'\n')
    p=ROOT/'STATUS.md'; lines=p.read_text(encoding='utf-8').splitlines()
    lines[0]='STATE: WORKING'
    lines[1]='NEXT: Resume the fine certificate to rho=0.43, validate complete coverage and witnesses, then request independent review. Do not repeat coarse .43 tables (enclosure above 2), fully rescaled kernels (worse), or monolithic table builds (timeout). Exit 3 is a saved time checkpoint; decode the first PowerShell log as UTF-16, later logs are UTF-8.'
    lines += ['',result['at']+' | FINE PREFIX / UNAUDITED | '+json.dumps(result)]
    p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    with (ROOT/'REPORT.md').open('a',encoding='utf-8') as out:out.write(result['at']+' | Target 2 fine prefix: '+json.dumps(result)+'\n')
    with (ROOT/'RESULT_ROWS.jsonl').open('a',encoding='utf-8') as out:out.write(json.dumps({'id':'T039-T2-FINE-PREFIX-'+stamp,'kind':'narrowed','target':2,'status':'proof (unaudited)','measurement':result,'evidence':['logs/fine_checkpoint.json',str(runlog.relative_to(ROOT))]})+'\n')
    print(json.dumps(result),flush=True)
    print(runlog.read_text(encoding='utf-8')[-4500:],flush=True)
    return 0 if child.returncode in (0,3) else child.returncode

if __name__=='__main__':raise SystemExit(main())
