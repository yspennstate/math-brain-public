from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
import arithmetic as M
R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
validation=json.loads((R/'out'/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS' and validation['assertions']==12284 and validation['runtime_seconds']<60
source=HOME.parent/'A003'/'runs'/'20261013T222630Z-fleet05-A003-minimal-target-formulation'/'CLAIMS.json'
claims=json.loads(source.read_text(encoding='utf-8'))
stamp=datetime.now(timezone.utc).isoformat()
review_hash=hashlib.sha256((R/'REVIEW.md').read_bytes()).hexdigest()
hashchecks=[]
source_finalizer=source.parent/'code'/'finalize.py'
source_bytes=source_finalizer.read_bytes()
(R/'out'/'sources'/'A003-finalize.py').write_bytes(source_bytes)
manifest=json.loads((R/'out'/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
if not any(q['path']==str(source_finalizer) for q in manifest):
 manifest.append({'path':str(source_finalizer),'snapshot':'out/sources/A003-finalize.py','sha256':hashlib.sha256(source_bytes).hexdigest(),'bytes':len(source_bytes)})
write(R/'out'/'SOURCE_MANIFEST.json',manifest)
for c in claims:
 raw=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
 computed=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
 hashchecks.append({'claim_id':c['claim_id'],'version':c['version'],'source_statement_sha256':c['statement_sha256'],'recomputed_source_convention_sha256':computed,'source_convention':'sorted compact JSON of statement and hypotheses; default ensure_ascii=True, per A003 code/finalize.py line 21','raw_statement_utf8_sha256':raw,'matches':computed==c['statement_sha256']})
 assert computed==c['statement_sha256']
 c['review_records'].append({'reviewer':'A004','at_utc':stamp,'run_id':R.name,'decision':'ACCEPT_AT_EXACT_STATED_ABSTRACT_SCOPE',
  'scope':'Complete all-r sliced-majority and arbitrary disjoint Boolean-rest interface; complete all-k conditional two-query prefix. The B05 instantiated construction and universal FEI/payment are outside acceptance.',
  'independent_method':'Direct binomial/Krawtchouk coefficient counts, separate hyperbolic Phi proof, independent physical composition and adaptive trees; reconstructed density/cutoff/eligibility proof.',
  'substantive_repair':False,'proof_path':'REVIEW.md','proof_sha256':review_hash,'validation_path':'out/VALIDATION.json'})
 c['status']='INDEPENDENTLY_ACCEPTED_LOCAL_ONE_REVIEW_AT_STATED_SCOPE'
write(R/'CLAIMS.json',claims);write(R/'out'/'SOURCE_STATEMENT_HASH_CHECK.json',hashchecks)
l2,u2=M.ln_interval(Q(2));bitlo=Q(2)+Q(59,512)+2/u2;bithi=Q(2)+Q(59,512)+2/l2
assert bithi<Q(5001,1000)
def round_interval(lo,hi):
 scale=1<<100;return {'lower':str(Q((lo*scale).__floor__(),scale)),'upper':str(Q((hi*scale).__ceil__(),scale))}
write(R/'out'/'UNIT_CONSTANTS.json',{'prefix_bits':round_interval(bitlo,bithi),'prefix_nats':round_interval(2+(2+Q(59,512))*l2,2+(2+Q(59,512))*u2),
 'JS_price_bits':round_interval(2/u2,2/l2),'JS_price_nats':'2','collision_bits':'59/512','collision_nats':'(59/512)*ln(2)',
 'slice_bits':'2*rho','slice_nats':'2*ln(2)*rho','indicator_Dirichlet_RHS_conversion':'multiply sign-pivotal coefficient by 4; do not use raw indicator masses as a probability law'})
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
p={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A004','gap_id':'C018-C019-SIGNED-TERMINAL-COLLISION','attempt_id':'A004-independent-review-stage-3',
 'method':'Independent source-bound review using direct Krawtchouk coefficients, hyperbolic packet inequality, exact coherent collision and full-terminal stopping ledger',
 'mathematical_delta':'Independently accepted both A003 stage-3 scoped claims, without repair or acceptance of the instantiated B05 chain. 12284 exact assertions pass; full terminal mixing and bit/nat prefix constants retained. No universal payment improvement.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_SAVED_PENDING_SUPERVISOR_ADOPTION','mathematical_status':'TWO_SCOPED_CLAIMS_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims]+[{'claim_id':'A004-NORMALIZATION-LEDGER','version':2,'scope':'previous algebra reapplied, not self-independent acceptance'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'A004 independent acceptance appended; statement unchanged'} for c in claims],
 'source_artifacts':['REPORT.md','REVIEW.md','CLAIMS.json','out/SOURCE_MANIFEST.json','out/VALIDATION.json','out/KRAWTCHOUK_CERTIFICATE.json','out/UNIT_CONSTANTS.json'],
 'next_consumers':['A003','A026','A057','A087','A094','A096','B01','B06','B20'],
 'next_action':'Audit A096 actual conditional-edge KL refund against the coherent signed empty-row collision on the same arbitrary terminal seed and one physical influence budget.',
 'stagnant_substantive_attempts':0,'blockers':['No local save blocker. Universal signed collision and terminal-core payment open; supervisor adoption and remote mirroring unverified.'],
 'packet_ids':['A004']}
write(R/'PROGRESS.json',p);write(R/'PACKET_DELTA.json',p)
expected={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(p)==expected
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
report=(R/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
# Preserve exact source hashes; the report carries the copied historical values.
for c in claims:assert c['statement_sha256'] in report
write(R/'out'/'SCHEMA_CHECK.json',{'status':'PASS','progress_fields_exact':True,'claim_fields_exact':True,'all_report_fields':True,
 'compatibility_byte_identical':(R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes(),'statement_hash_checks':hashchecks,'source_claim_count':len(claims)})
(HOME/'STATUS.md').write_text('STATE: A004 stage 3 complete locally: both A003 sliced-majority/two-query claims independently accepted at stated scope; 12,284 exact assertions PASS; full FEI OPEN.\nNEXT: Audit A096 conditional-edge KL refund versus coherent signed empty-row collision, retaining arbitrary terminal core and one physical influence budget.\n',encoding='utf-8')
if 'Stage 3 recovered prior final save' not in (HOME/'WORKLOG.md').read_text(encoding='utf-8'):
 with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Stage 3 recovered prior final save, then independently accepted A003 sliced-majority and abstract two-query prefix without repair. Direct Krawtchouk representation, hyperbolic Phi proof, physical coherent compositions and adaptive full-terminal trees: 12,284 assertions PASS in {validation["runtime_seconds"]:.3f}s. Bit prefix coefficient <5.001; natural coefficient 2+(2+59/512)ln2. Arbitrary collision/terminal payment still open.\n')
if 'Stage 3 durable review:' not in (HOME/'LEARNED.md').read_text(encoding='utf-8'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 3 durable review: A003-ONCE-SLICED-MAJORITY-ERASURE@1 and A003-TWO-QUERY-ELIGIBLE-PREFIX@1 independently accepted by A004 at exact abstract scope; instantiated B05 example not independently reviewed. Boundary coefficient d_l=2^-2r sum_j(-1)^j binom(l,j)binom(2r-l,r-j) independently reconstructs inherited erasure. In bits Phi<=2sqrt(ab); in nats constant 2ln2. Scoped prefix price is 2+59/512+2/ln2 bits, 2+(2+59/512)ln2 nats. Signed stopping deficit K I-H retains terminal h2(v)+vH(R); empty corrections cancel only under identical laws/weights. No fixed arbitrary-outer collision price or terminal-core refund follows. Next align actual KL and signed coherent reserves.\n')
hashlesson='Source hash convention: A003 hashes sorted compact JSON of statement and hypotheses, not the statement UTF8 alone. Recompute using source code; preserve both the historical hash and any explicitly labelled raw-text hash.'
if hashlesson not in (HOME/'LEARNED.md').read_text(encoding='utf-8'):
 with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+hashlesson+'\n')
receipts=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and '__pycache__' not in str(f) and f.name!='RECEIPTS.json':
  b=f.read_bytes();assert len(b)<20_000_000
  receipts.append({'path':str(f.relative_to(R)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 b=(HOME/name).read_bytes();receipts.append({'path':'../../'+name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
write(R/'out'/'RECEIPTS.json',{'status':'LOCAL_SAVED_READBACK_VERIFIED','at_utc':stamp,'files':receipts,'remote_verification':False})
print(json.dumps({'status':'LOCAL_COMPLETE','assertions':validation['assertions'],'reviewed_claims':len(claims),'files':len(receipts),'statement_hashes_match':all(q['matches'] for q in hashchecks)}))
