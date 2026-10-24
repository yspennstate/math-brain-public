from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,obj):(ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
summary=json.loads((ROOT/'out/summary.json').read_text())
assert summary['exact_assertions']==131327 and not summary['pilot'] and summary['failures']==0
assert summary['restriction_validation']['histories']==3964 and summary['restriction_validation']['physical_split_checks']==7438
assert summary['compressed_orbits']==76 and summary['exact_K6_orbits']==1
src=Path('~/brain_workers/FEI100_20261011/agents/A075/runs/20261013T212622Z-account05-A075-search-to-theorem-bridge/CLAIMS.json')
claims=json.loads(src.read_text())
assert len(claims)==1
c=claims[0];old=(c['exact_statement'],c['hypotheses'],c['version'],c['statement_sha256'])
c['review_records'].append({'reviewer':'account05/A074','at':NOW,'verdict':'ACCEPT_AT_STATED_SCOPE','scope':'Full original matching hereditary/sharpness/tree/limits and graph-path root claim; no all-Boolean extension','method':'Independent generating-polynomial convolution and direct physical sparse character sums; exhaustive simultaneous histories through six bits; Fraction conditional-entropy cutoff; analytic proof reconstruction','source':str(ROOT/'REPORT.md'),'exact_assertions':summary['exact_assertions'],'substantive_repair_supplied':False})
c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_REVIEW'
assert old==(c['exact_statement'],c['hypotheses'],c['version'],c['statement_sha256'])
write('CLAIMS.json',claims)
p={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A074','gap_id':'G-R-SELECT','attempt_id':'A074-INDEPENDENT-REPRODUCTION-3','method':'Generating-polynomial and direct physical sparse character reconstruction; all-history closure and analytic tail review','mathematical_delta':'A075 sparse matching hereditary/sharp K6/tree/limits and graph-path root theorem independently accepted at original scope;131327 exact assertions,3964 histories,7438 splits,49 cutoff parameter pairs; no universal constant advance.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'A075_SCOPED_THEOREM_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'use':'independent review target, not assumed premise'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'scope-preserving independent acceptance appended; mathematical statement and hash unchanged'}],'source_artifacts':['REPORT.md','INDEPENDENT_REPRODUCTION.py','REPRODUCTION_REPORT.json','FROZEN_SPEC.json','out/summary.json','out/restrictions_summary.json','out/analytic_cutoffs.json','out/compressed_r6_k3.json'],'next_consumers':['A075','A072','A080','A085','A092','B15','B20'],'next_action':'Audit A071/A072 f6 signed-admission signatures and high-E common-orientation guard, retaining every new coordinate, inherited B_i and terminal H(g); no sparse or finite-census replay.','stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A074']}
write('PROGRESS.json',p);write('PACKET_DELTA.json',p)
script=(ROOT/'code/review.py').read_text()
standalone=script.replace('ROOT=Path(__file__).resolve().parents[1]','ROOT=Path(__file__).resolve().parent')
(ROOT/'INDEPENDENT_REPRODUCTION.py').write_text(standalone,encoding='utf-8')
assert standalone.replace('ROOT=Path(__file__).resolve().parent','ROOT=Path(__file__).resolve().parents[1]')==script
write('REPRODUCTION_REPORT.json',{**summary,'review_of':{'claim_id':c['claim_id'],'version':c['version'],'verdict':'ACCEPT_AT_STATED_SCOPE'},'first_differing_quantity':None,'full_fei':'OPEN','remaining_gap':'Arbitrary-inner-core signed admission with one physical influence reserve and full terminal entropy'})
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
req=json.loads(protocolpath.read_text())['required_per_run']
assert set(p)=={s.split(' (')[0] for s in req['progress_fields']}
for row in claims:assert set(row)==set(req['claim_fields'])
for field in req['report_fields']:assert '## '+field in (ROOT/'REPORT.md').read_text()
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
paths=[protocolpath,src,src.parent/'REPORT.md',Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B15/STREAM_NOTES.md'),Path('~/brain_workers/FEI100_20261011/agents/A080/runs/20261013T212642Z-account05-A080-universal-counterexample-standard/MATCHING_ASYMPTOTICS.md'),Path('~/brain_workers/FEI100_20261011/agents/A080/runs/20261013T212642Z-account05-A080-universal-counterexample-standard/CLAIMS.json')]
receipts=[]
for path in paths:
 data=path.read_bytes();receipts.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'scope':'Stage source consultation; no code imported or executed'})
write('out/source_receipts.json',receipts)
(AGENT/'STATUS.md').write_text('STATE: A074 stage3 complete: A075 sharp hereditary matching K6, terminal tree ledger and graph/path root no-growth independently accepted;131327 exact assertions PASS; full FEI OPEN.\nNEXT: A085/A092 challenge; audit A071/A072 f6 signed-admission signatures and high-E orientation guard, retaining new coordinates, inherited erasure and terminal H(g).\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} {ROOT.name}: Read BOARD23:59/B15v2/own status and A075/A080 sources. Reconstructed matching via generating polynomials and direct sparse character sums, not binomial/FWHT/source code.49 compressed cases,76 orbits,one exact K6 equality orbit,3964 simultaneous histories,7438 splits,1100 graphs,28 paths;131327 exact assertions PASS,0.8842519s. Analytic tail/point-descendant/JS/tree/limits/graph-path proofs independently reconstructed. A075 @1 scoped acceptance; full FEI OPEN. Next changes to live signed-admission signatures.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} stage3: Matching sparse spectra have indicator-sum generating polynomial(z^3+3z^-1)^k(z+z^-1)^l; replace exactly one empty Fourier atom. All-zero histories leave partial matchings; one fixed one leaves a point defect with possible partner dummy; a fixed matched pair leaves a point defect; other multi-one histories are constant.\nIndependent reconstruction confirms sharp hereditary K6 at(k,l)=(3,0). U(r)=2+8/(r-3)+(3r+2)(2r+3/2)/2^r falls below368/125 at13 and decreases forever. Matching E tends to2,H/I tends to4; sparse dimension escalation is retired.\nThe class tree ledger keeps E H(leaf) and consumed influence I(root)-E I(leaf); it does not pay arbitrary inner-core admission. Next audit the actual f6 signed empty-row signature and high-E guard, including every new coordinate and terminal core cost.\n')
manifest=[]
for path in ROOT.rglob('*'):
 if path.is_file() and path.name!='manifest.json':
  data=path.read_bytes();assert len(data)<20*1024*1024
  manifest.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
write('out/manifest.json',manifest)
print(json.dumps({'protocol_schema':'PASS','standalone_equivalence':'PASS','claims_preserved':'PASS','files':len(manifest),'largest_bytes':max(row['bytes'] for row in manifest),'assertions':summary['exact_assertions']},indent=2))
