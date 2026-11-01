"""Complete reviewable artifacts, validate them, then set the requested review state."""
import sys
sys.dont_write_bytecode=True
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8')
steps=[]
for filename in ['finalize_sources.py','validate_deliverables.py']:
    command=[sys.executable,'-X','utf8',str(ROOT/filename)]
    result=subprocess.run(command,cwd=ROOT,env=env,text=True,encoding='utf-8',capture_output=True)
    steps.append({'command':command,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    if result.returncode:
        (ROOT/'CLOSEOUT.json').write_text(json.dumps({'status':'FAILED','steps':steps},indent=2,ensure_ascii=False),encoding='utf-8')
        print(result.stdout+result.stderr)
        raise SystemExit(result.returncode)
receipt=json.loads((ROOT/'VALIDATION.json').read_text(encoding='utf-8'))
assert receipt['verdict']=='PASS' and receipt['mathematical_entries']==16 and receipt['relations']==41
assert len((ROOT/'AUDIT_STATEMENTS.jsonl').read_text(encoding='utf-8').splitlines())==16
for file in ['REPORT.md','AUDIT_REQUEST.md','patches/01_first_research_bundle.diff','patches/02_remaining_research_bundle.diff']:
    assert (ROOT/file).is_file(),file
timestamp=datetime.now().astimezone().isoformat(timespec='seconds')
(ROOT/'CLOSEOUT.json').write_text(json.dumps({'status':'NEEDS_REVIEW','finished_at':timestamp,'steps':steps,'validation':receipt},indent=2,ensure_ascii=False),encoding='utf-8')
old=(ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines()
log='\n'.join(line for line in old if not line.startswith('STATE:') and not line.startswith('NEXT:')).strip()
status=('STATE: NEEDS_REVIEW\nNEXT: w346 independently audits AUDIT_STATEMENTS.jsonl and full proofs; the reviewer ingests only KEEP entries from bundle_001 and bundle_002.\n\n'+log+'\n'+timestamp+': Complete measured packet: 16 mathematical rows across all ten assigned problems, 2 draft bundles, 41 relations, 82 quoted endpoints verified, 24 existing logical targets resolved, no dependency cycles. Blind audit packet, full proofs, measurement scripts, exact source receipts, requested diffs and apply command are saved. Lean admission refused; exact SymPy checks passed. All claims await w346; local hooks/progress are queued for reviewer publication.\n')
(ROOT/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','problems':10,'mathematical_entries':16,'relations':41,'quoted_endpoints_checked':82,'auditor_KEEPs':0,'report':str(ROOT/'REPORT.md'),'next':'w346 independent full-proof audit, then reviewer ingestion of kept rows'},ensure_ascii=False))
