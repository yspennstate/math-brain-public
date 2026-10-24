from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):return p.read_text(encoding='utf-8-sig')
def obj(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):(RUN/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=obj(BASE/'EXECUTION_PROTOCOL.json');report=read(RUN/'REPORT.md')
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert set(obj(RUN/'PROGRESS.json'))=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in obj(RUN/'CLAIMS.json'):assert set(c)==set(protocol['required_per_run']['claim_fields'])
val=obj(RUN/'out/VALIDATION.json')
dag=obj(RUN/'out/PROOF_DEPENDENCIES.json')
dag['open_leaves'][0]['prior_valid_but_weaker_conditional_constant']=dag['open_leaves'][0]['conditional_constant']
dag['open_leaves'][0]['conditional_constant']='K+2/ln2, by exact optimal higher-tail equality'
save('out/PROOF_DEPENDENCIES.json',dag)
buildok=len(val['build'])==2 and all(b.get('returncode')==0 for b in val['build'])
val['pdf_complete_two_passes']=buildok
val['previous_build_attempt']='BUILD_ATTEMPT_1.json records the first 60-second timeout; retry output is retained separately'
save('out/VALIDATION.json',val)
if not buildok:
    report=report.replace('manuscript source and PDF','manuscript source and compiler outputs (complete PDF build blocked)')
    report=report.replace('there is no local save blocker.','the source/protocol save is complete, while a verified complete PDF build is blocked by the recorded compiler result.')
    (RUN/'REPORT.md').write_text(report,encoding='utf-8')
    progress=obj(RUN/'PROGRESS.json')
    progress['source_artifacts']=[x for x in progress['source_artifacts'] if x!='out/CANDIDATE_MANUSCRIPT.pdf']
    progress['blockers'].append('Verified complete PDF unavailable: bounded compiler attempt failed; source is saved')
    save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
assert all(p.stat().st_size<20_000_000 for p in RUN.rglob('*') if p.is_file())
(ROOT/'STATUS.md').write_text('STATE: A099 v3 saved: A090 low-influence acceptance consumed; A090 tail and A096 normalized refund independently reconstructed; shared-bit transfer assembled; full FEI OPEN, integrated audits pending.\nNEXT: A096/A001/A073 pay signed-Boolean terminal-core KL with one reference and influence reserve; A094 reconstruct integrated chain; A097 name nonreused collision seed reserve.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: {RUN.name}: assembled v3, consumed A090 acceptance of low-v2, independently reconstructed A090 fixed-tail and A096 terminal KL formulas; 96 frozen direct-character cases/3432 exact assertions PASS. A097 shared-bit transfer and bent/flip boundary retained at author scope. Hash conventions resolved without statement changes. First PDF attempt timed out at 60 seconds; bounded retry complete={buildok}. Full FEI and both integrated audits open.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nEvery fixed higher-tail cutoff optimum equals K_E: fresh ell>=2 parity forces all arbitrary seed erasure into retained layers without erasure on its own relevant coordinates. R_ge2<=KI would therefore imply FEI at K+2/ln2, without root/T12 overhead; it supplies no finite K.\n\nA096 source M is exactly aggregate downward L, not the marginal entropy sum. Its complete conditional-edge KL refund transports the arbitrary seed divergence and refunds only added activation rarity; the universal retained seed lower bound remains C018 strength.\n\nA099 v2 canonical statement-plus-hypotheses JSON hash and A090 raw statement hash describe the same statement. Reviews bind both conventions plus source bytes; a fragment acceptance is never an integrated-chain acceptance.\n\nOne shared data bit permits both collision atoms to be calibrated and selector transfer at 2+4/ln2 with full terminal bills. Unrestricted overlap defeats any absolute selector-only tax via bent/point-flip, and requires an explicitly owned terminal seed reserve.\n')
assert len(read(ROOT/'STATUS.md').splitlines())==2
save('out/SCHEMA_CHECK.json',{'report_fields':True,'claim_fields':True,'progress_fields':True,'compatibility_identical':True,'all_files_below_20MB':True,'rolling_status_two_lines':True,'PDF_complete':buildok,'independent_integrated_audits':'PENDING','external_mirror':'NOT_VERIFIED'})
files=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
save('out/PERSISTENCE_RECEIPTS.json',{'run_id':RUN.name,'files':files,'self_excluded':True,'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],'mirror':'NOT_VERIFIED'})
assert all(sha(RUN/x['path'])==x['sha256'] for x in files)
print(json.dumps({'status':'SAVED','receipt_files':len(files),'PDF_complete':buildok,'full_FEI':'OPEN','integrated_audits':'PENDING'}))
