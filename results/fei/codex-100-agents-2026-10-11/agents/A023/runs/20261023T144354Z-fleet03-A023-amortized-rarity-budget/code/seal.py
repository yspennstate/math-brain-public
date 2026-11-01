"""Make realized/expected ledger convention explicit, then re-check saved hashes."""
from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,t):Path(p).write_text(t,encoding='utf-8',newline='\n')
def save(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
before='At first marking charge D_h; at a later query charge E[D_child|h]-D_h. These signed increments telescope pathwise to terminal D, with no clipping and no fresh descendant allowance.'
after='At first marking charge D_h. On each realized later edge charge D_child-D_parent; these realized differences telescope PATHWISE to terminal D, with no clipping and no fresh descendant allowance. Their CONDITIONAL EXPECTATIONS are E[D_child|h]-D_h; those expected node charges telescope only AFTER reach weighting. A conditional average increment is not claimed to telescope on an individual realized path.'
for name in ['PROOF.md','code/stage.py']:
 p=RUN/name;t=read(p);assert before in t;t=t.replace(before,after);write(p,t)
clarification='Ledger precision: realized differences D_child-D_parent telescope pathwise. Conditional expected differences E[D_child|h]-D_parent telescope only in the reach-weighted expected ledger. This also clarifies stage21 PROOF section3 wording; its expected-bound conclusion and exact validations are unchanged. Both full KLs remain in every difference.'
report=read(RUN/'REPORT.md');marker='# executed validation with domain, arithmetic, commands and outputs';assert marker in report;report=report.replace(marker,clarification+'\n\n'+marker);write(RUN/'REPORT.md',report)
pr=json.loads(read(RUN/'PROGRESS.json'));pr['source_artifacts'].append('code/seal.py');pr['mathematical_delta']+=' Realized/expected telescope convention explicitly clarified, including stage21 wording; no bound changes.';save(RUN/'PROGRESS.json',pr);write(RUN/'PACKET_DELTA.json',read(RUN/'PROGRESS.json'))
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+stamp+' stage22 seal: zero enumerated cases (campaign cutoff respected), analytic proof saved; clarify that only realized edge differences telescope pathwise, while conditional averages telescope after reach weighting. Stage21 expected bound unchanged. Independent-person review, initial supplier and full FEI OPEN.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-23 ledger convention: D_child-D_parent telescopes on a realized path; E[D_child|h]-D_parent is its conditional expectation and telescopes only after reach weighting. Do not describe the latter as pathwise cancellation. Stage21/22 expected conversion bounds are unchanged by this precision.\n')
c=json.loads(read(RUN/'CLAIMS.json'))[0];assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
fields=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))['required_per_run'];assert set(c)==set(fields['claim_fields']);assert set(pr)=={s.split(' (')[0] for s in fields['progress_fields']};assert all('# '+s in report for s in fields['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes();assert len(read(ROOT/'STATUS.md').splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'];assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS_LOCAL','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],'rolling':[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'review':'PENDING','mirror':'UNVERIFIED','validation':'SKIPPED_CAMPAIGN_END','pathwise_expectation_convention':'CLARIFIED'}
save(RUN/'out/PERSISTENCE_RECEIPTS.json',receipt)
for item in receipt['files']:assert hashlib.sha256((RUN/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'status':'PASS_LOCAL_ARTIFACT','files_hash_checked':len(files),'claim_version':10,'validation':'SKIPPED_CAMPAIGN_END','new_enumerated_cases':0,'full_FEI':'OPEN','review':'PENDING','running_jobs':0}))
