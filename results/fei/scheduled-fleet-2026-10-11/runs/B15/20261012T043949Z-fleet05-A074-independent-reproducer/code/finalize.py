from pathlib import Path
import json,hashlib,datetime
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,obj):
 (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
summary=json.loads((ROOT/'out/summary.json').read_text())
assert summary['exact_assertions']==329427 and not summary['pilot']
assert 2**53*5**100<3**180
w5=json.loads((ROOT/'out/witness_n5.json').read_text());w6=json.loads((ROOT/'out/witness_n6.json').read_text())
assert F(w6['minimum_interval'][0])>F(w5['minimum_interval'][1])
for n in range(5):
 d=json.loads((ROOT/'out'/f'census_n{n}.json').read_text())
 path=ROOT/'out'/f'census_n{n}_decisions.jsonl';data=path.read_bytes()
 assert data.count(b'\n')==1<<(1<<n)
 assert hashlib.sha256(data).hexdigest()==d['decision_sha256']
 assert not d['failures']
srclead=Path('~/brain_workers/FEI100_20261011/claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch/CLAIMS.json')
srcfinite=Path('~/brain_workers/FEI100_20261011/agents/A082/runs/20261011T221008Z-fleet05-A082-finite-inequalities/CLAIMS.json')
lead=json.loads(srclead.read_text())['claims'][0];finite=json.loads(srcfinite.read_text())[0]
claims=[lead,finite]
for c in claims:
 original=(c['exact_statement'],c['version'],c['statement_sha256'])
 c['review_records'].append({'reviewer':'fleet05/A074','at':NOW,'verdict':'ACCEPT_AT_STATED_SCOPE','scope':'Original finite statement only; no universal FEI or affine bridge acceptance','method':'Direct character-sign bitset sums, exact joint conditional law, Fraction positive-series logarithms and exhaustive unreduced n<=4 mask census with exact symbolic ties','source':str(ROOT/'REPORT.md'),'exact_assertions':summary['exact_assertions']})
 c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_REVIEW'
 assert original==(c['exact_statement'],c['version'],c['statement_sha256'])
write('CLAIMS.json',claims)
p={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B15','packet_id':'A074','gap_id':'G-R-SELECT','attempt_id':'A074-INDEPENDENT-REPRODUCTION-2','method':'Direct character sums, Fraction joint conditional entropy, positive logarithm series; full unreduced n<=4 census','mathematical_delta':'Independently accepted fixed f5/f6 erasure obstructions and sharp n<=4 selection constant; 329427 exact assertions, 65470 strict and 64 exact four-bit extremizers; no all-dimensional payment.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'TWO_EXISTING_FINITE_CLAIMS_INDEPENDENTLY_ACCEPTED_AT_SCOPE_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'use':'independent review target, not assumed proof premise'} for c in claims],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'independent acceptance at original finite scope; statement unchanged'} for c in claims],'source_artifacts':['REPORT.md','INDEPENDENT_REPRODUCTION.py','REPRODUCTION_REPORT.json','FROZEN_SPEC.json','out/summary.json','out/witness_n5.json','out/witness_n6.json','out/census_n4.json','out/census_n4_decisions.jsonl'],'next_consumers':['A075','A072','A073','A082','A085','A092','B15','B20'],'next_action':'Reconstruct A075 sparse matching family and actual physical restriction formulas with terminal entropy; freeze bounded parameters aimed at its unpaid dimension bridge.','stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A074']}
write('PROGRESS.json',p);write('PACKET_DELTA.json',p)
protocolpath=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
req=json.loads(protocolpath.read_text())['required_per_run']
assert set(p)=={s.split(' (')[0] for s in req['progress_fields']}
for c in claims:assert set(c)==set(req['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text()
for field in req['report_fields']:assert '## '+field in report
script=(ROOT/'code/reproduce.py').read_text()
standalone=script.replace('ROOT=Path(__file__).resolve().parents[1]','ROOT=Path(__file__).resolve().parent')
(ROOT/'INDEPENDENT_REPRODUCTION.py').write_text(standalone,encoding='utf-8')
write('REPRODUCTION_REPORT.json',{**summary,'review_verdicts':[{'claim_id':c['claim_id'],'version':c['version'],'verdict':'ACCEPT_AT_STATED_SCOPE'} for c in claims],'first_differing_quantity':None,'full_fei':'OPEN','method_independent':True,'original_code_imported_or_executed':False})
paths=[protocolpath,srclead,srcfinite,Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B15/STREAM_NOTES.md')]
for agent,run in [('A072','20261012T004036Z-fleet05-A072-exact-walsh-engine'),('A071','20261011T233808Z-fleet05-A071-search-space-design')]:
 base=AGENT.parent/agent/'runs'/run
 paths+=[base/'REPORT.md']
 if agent=='A072':paths+=[base/'CLAIMS.json',base/'out/witness_n5.json',base/'out/witness_n6.json',base/'out/comparison.json']
paths+=[srcfinite.parent/'REPORT.md']
receipts=[]
for path in paths:
 data=path.read_bytes();receipts.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'scope':'stage source consultation and finite review; no imported code'})
write('out/source_receipts.json',receipts)
(AGENT/'STATUS.md').write_text('STATE: A074 stage2 complete: f5/f6 and unreduced n<=4 census independently accepted at finite scope; 329427 exact assertions PASS, 64 n4 extremizers; full FEI OPEN.\nNEXT: A085/A092 challenge; reconstruct A075 sparse matching family and actual physical descendants with terminal entropy, targeting the dimension-dependent erasure payment.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW}: Stage2 read BOARD04:39/B15v2; replaced prior tax target per lead. Direct character-sign bitsets and conditional joint-law entropy reproduced f5/f6, minima0,1,3/all6. Unreduced n0..4 census65814 tables; n4 strict65470/equal64/fail0. 329427 exact assertions,1.3684112s. Positive rational log enclosure certifies signs; mpmath60 digits evidence only. Local scoped acceptance of B15 finite witness and A082 finite leaf claims, no new broad candidate or full FEI assertion.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} stage2: Direct spectrum from negative set A: W0=N-2|A|, W_s=-2(|A|-2 count_(A) odd(x&s)) for s!=0. Bitset character sums are a separate implementation from FWHT/Gray transforms.\nDirect conditional spectral law gives B_i=-sum p_j log2(p_j/q). Fixed-point outward packet bounds allow an exact fast census; equality needs symbolic cancellation, not numerical tolerance.\nReproduced E(f5)=2.6958875201531... at coordinates0,1,3 and E(f6)=2.94449530387185... at all6. Both beat sharp n<=4 Kstar; they supply no unbounded family. All65536 four-bit tables reproduce65470 strict nonconstants and64 exact extremizers, precisely embedded3-bit point defects. No n5 upper or affine bridge was audited here.\n')
manifest=[]
for path in ROOT.rglob('*'):
 if path.is_file() and path.name!='manifest.json':
  data=path.read_bytes();assert len(data)<20*1024*1024
  manifest.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
write('out/manifest.json',manifest)
print(json.dumps({'schema':'PASS','hash_and_row_checks':'PASS','files':len(manifest),'largest_bytes':max(row['bytes'] for row in manifest),'assertions':summary['exact_assertions']},indent=2))
