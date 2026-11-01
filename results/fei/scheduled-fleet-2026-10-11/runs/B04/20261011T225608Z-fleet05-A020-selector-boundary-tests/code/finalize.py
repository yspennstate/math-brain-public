from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
c=json.loads((ROOT/'out'/'census.json').read_text());d=json.loads((ROOT/'out'/'direct_check.json').read_text());f=json.loads((ROOT/'out'/'fixtures.json').read_text())
assert c['cases']==131620 and len(c['domains'])==7 and c['zero_selector']==300
assert c['certified_ratio_cap']=='171/200'
assert d['status']=='PASS' and d['named_tables']==32
assert f['named_cases']==32 and f['random_cases']==1024
canonical=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
sources=[canonical/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
sources += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources+=list((supp/'sources').glob('*'))+list(context.glob('*.txt'))
sources += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B04\STREAM_NOTES.md')]
write('out/source_receipts.json',[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources if p.is_file()])
statement='For every uniform Boolean multiplexer F(x,y)=g_x(y) with a=1 and m in {0,1,2,3}, or a=2 and m in {0,1,2}, entropy in bits and s=I_sel(F), Delta=H(F)-2^-a sum_x H(g_x) satisfies Delta <= (171/200)*[(2/ln(2))*s+a*h2(s/a)], strictly if s>0; if s=0 then Delta=0. This is a finite statement covering 131620 labeled truth tables.'
claim=dict(claim_id='A020-SELECTOR-FINITE-CAP',version=1,exact_statement=statement,hypotheses=['Uniform independent physical selector/data blocks','Actual Boolean +/-1 truth tables','Only the seven specified finite domains','Entropy units bits; h2(0)=h2(1)=0'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A020'],proof_source=['REPORT.md','code/verify.py','CERTIFICATION_SPEC.json','out/census.json','out/certified_census.log'],proof_dependencies=[],review_records=[],status='PROVED_LOCALLY_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A090','A091','A018','A019','A027'])
write('CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B04',packet_id='A020',gap_id='G-LOWSEL-COLLISION',attempt_id='A020-selector-boundary-v1',method='Exhaustive Boolean census; integer Walsh; rational interval logs; exact affine collision fixtures; separate direct character reconstruction',mathematical_delta='131620 tables certify selector increment <=171/200 times the logarithmic bound; 1056 targeted tests pass; explicit unequal and affine-cell ledgers expose lost interference and selector influence. Analytic recovered bent-splice ratio=m+3/ln2+O(2^-m) retained. Universal bridge remains unpaid.',deliverable_status='COMPLETE_LOCAL',mathematical_status='FINITE_TARGET_PROVED_UNIVERSAL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=['A020-SELECTOR-FINITE-CAP/v1'],source_artifacts=['REPORT.md','CLAIMS.json','SELECTOR_FALSIFIER_SUITE.tex','SELECTOR_FAILURE_SCOPE.json','SEARCH_SPEC.json','TARGETED_SPEC.json','CERTIFICATION_SPEC.json','code/verify.py','code/fixtures.py','code/direct_check.py','out/census.json','out/fixtures.json','out/direct_check.json','out/source_receipts.json'],next_consumers=['A090','A091','A018','A019','A027'],next_action='Consume A019 source-complete overlapping rare-translation module ledger; test exact KL-credit and shared physical-influence ownership with terminal core entropy retained.',stagnant_substantive_attempts=0,blockers=['Independent-agent review and supervisor mirror pending; universal rare-selector tree amortization is unproved.'],packet_ids=['A020'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A020 local packet complete: 131620 exact selector certificates, cap 171/200; 1056 targeted cases and 2576 direct checks PASS; review pending; full FEI OPEN.\nNEXT: A090/A091 review; test A019 overlapping-control KL ledger against saved affine/rare-flip fixtures with nonreused influence and terminal entropy.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as out:out.write('\n'+stamp+' — Final rational-cap pass PASS in '+str(c['runtime_seconds'])+' s; direct 32-table reconstruction PASS, '+str(d['exact_assertions'])+' assertions in '+str(d['runtime_seconds'])+' s. Required JSON fields and local persistence validated. Mirrors/adoption/review not asserted.\n')
protocol=json.loads((canonical/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
expected=set(x.split(' (')[0] for x in protocol['progress_fields'])
assert set(progress)==expected,(set(progress),expected)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert '## Universal bridge' in (ROOT/'REPORT.md').read_text()
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='persistence_receipt.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
for p in [ROOT/'CLAIMS.json',ROOT/'PROGRESS.json',ROOT/'PACKET_DELTA.json']:json.loads(p.read_text(encoding='utf-8'))
receipt=dict(at_utc=stamp,schema_validation='PASS: exact claim/progress key sets; identical deltas; two-line status; report universal bridge',readback='PASS',maximum_file_bytes=max(p.stat().st_size for p in files),files=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=sha(p)) for p in files],rolling_files=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],mirrors='NOT VERIFIED',independent_agent_review='PENDING')
write('out/persistence_receipt.json',receipt)
print(json.dumps(dict(status='PASS',cases=c['cases'],cap=c['certified_ratio_cap'],runtime_seconds=c['runtime_seconds'],direct_assertions=d['exact_assertions'],files=len(files),max_bytes=receipt['maximum_file_bytes'],receipt=str(ROOT/'out'/'persistence_receipt.json'))))
