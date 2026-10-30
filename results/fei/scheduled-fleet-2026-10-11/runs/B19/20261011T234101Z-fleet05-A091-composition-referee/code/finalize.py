import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
REPORTS=Path('~/mop_fei100/reports/fei-2026-10-11')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
summary=read(ROOT/'out/SHARDS.json'); pilot=read(ROOT/'out/PILOT.json'); endpoint=read(ROOT/'out/ENDPOINTS.json')
assert summary['status']==pilot['status']==endpoint['status']=='PASS'
assert summary['shards']==48 and summary['blocks']==6144 and summary['adaptive_trees']==2304
assert pilot['blocks']==224
count=summary['exact_assertions']+pilot['exact_assertions']+endpoint['exact_assertions']
sources=[BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md',REPORTS/'EXECUTION_PROTOCOL.json',REPORTS/'CLAIM_REGISTRY.json',REPORTS/'runs/B09/20261011T195500Z-fleet01-B09-biased-restriction-uncertainty/REPORT.md',REPORTS/'verification/B09_interval_repair_20261011/REPORT.md',BASE/'agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/REPORT.md',BASE/'agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/CLAIMS.json',BASE/'agents/A024/runs/20261011T223622Z-fleet05-A024-biased-child-stability/REPORT.md',ROOT/'out/maassen_uffink_1988.pdf']
receipts=[]
for p in sources:
    if p.exists():receipts.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'receipt_scope':'bytes at finalization; audit scope limited to REPORT source locators'})
    else:receipts.append({'path':str(p),'receipt_scope':'not present at this path; original source read locator remains in REPORT'})
save(ROOT/'out/SOURCE_RECEIPTS.json',receipts)
original=read(BASE/'agents/A093/runs/20261011T223137Z-fleet05-A093-literature-and-priority/CLAIMS.json')[0]
statement_hash=hashlib.sha256(json.dumps({'statement':original['exact_statement'],'hypotheses':original['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert statement_hash==original['statement_sha256']
original['review_records'].append({'reviewer':'A091 fleet05 B19','date_utc':now,'verdict':'ACCEPT_AT_STATED_SCOPE_CORE_ONLY','source':str(ROOT/'REPORT.md'),'method':'Second requested independent review: visually checked primary MU (5)-(6),(10)-(13); direct centered-moment Fraction transform; physical joint marginals; prime-log entropy equalities and proved rational sign enclosures; multi-bit blocks and adaptive trees','validation':{'blocks':6368,'adaptive_trees':2304,'exact_assertions':count,'AND_margin_lower_bound':'1195/10000'},'scope_exclusions':['No optimality assertion','No universal influence or deficit payment','No arbitrary substitution additivity','Finite checks do not replace the all-dimension analytic derivation']})
save(ROOT/'CLAIMS.json',[original])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B19','packet_id':'A091','gap_id':'G-BIASED-TAX','attempt_id':'A091-core-review-2','method':'Source-bound second independent review; direct rational centered moments; prime-log entropy identities; exact adaptive corrected-entropy and deficit telescopes; interval AND and endpoint certificates','mathematical_delta':'Accepted B09-BIASED-BLOCK-UNCERTAINTY v1 core only, preserving its original statement/hash and authorship. Derived terminal-inclusive C019 consumption identity; no universal payment or improved FEI constant. Exhausted 6368 block cases and 2304 adaptive trees under the frozen finite laws.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'CORE_ACCEPTED_C019_PAYMENT_OPEN_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'B09-BIASED-BLOCK-UNCERTAINTY','version':1},{'source':'Maassen-Uffink 1988','locator':'(5)-(6),(10)-(13)'},{'source':'A024 biased-child-stability','scope':'signed outer residue interface only'}],'claims_created_or_changed':[{'claim_id':original['claim_id'],'version':1,'status':original['status'],'change':'Appended second independent core-only review; no statement or author change'}],'source_artifacts':['REPORT.md','CLAIMS.json','out/FROZEN_SPEC.json','out/FROZEN_SHARD_SPEC.json','out/FROZEN_ENDPOINT_SPEC.json','out/SOURCE_RECEIPTS.json','out/SHARDS.json','out/PILOT.json','out/ENDPOINTS.json','out/RECEIPTS.json','code/check.py','code/shards.py','code/endpoints.py'],'next_consumers':['A041','A045','A050','A057','A064','A090','A085','A096','A097','B20'],'next_action':'Evaluate the complete corrected charge on the actual overlapping-control stopping tree using its single-use local deficit reserves, signed outer residue, inner KL credit and certified terminal children; A090/A085 review the ledger application.','stagnant_substantive_attempts':0,'blockers':['The complete conditional spectral charge has no proved universal deficit budget; this is the first unsupported universal step.','Supervisor copy and downstream adoption pending; no local persistence blocker.'],'packet_ids':['A091']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
validation=f"\nFinal executed totals: {6368:,} block experiments (224 pilot plus 6,144 sharded three-variable cases), 2,304 adaptive trees, {count:,} exact assertions including endpoint checks. The first unsharded law-0 job stopped at the frozen 58-second watchdog and produced no law certificate; it is superseded by 48 complete nonoverlapping 16-mask slices, with no domain or dimension increase. Commands: `python -X utf8 code/check.py --pilot`, `python -X utf8 code/endpoints.py`, and `python -X utf8 code/shards.py` (each child uses `--law k --start a --end a+16`). Passed summary: out/SHARDS.json; per-slice outputs out/LAWk_a_b.json. Endpoint certificate: out/ENDPOINTS.json. The repaired AND interval independently gives M in [0.227909707141212807,0.227909707141212808], J in [0.347454723165637765,0.347454723165637766] and J-M in [0.119545016024424957,0.119545016024424958] bits, strictly above 1195/10000. Small-bias remainder inequalities are analytic; at p=2^-40 the fixed numerical mesh does not resolve the p^3-wide remainder band, and the endpoint diagnostic explicitly allows enclosure overlap tolerance. This tolerance is not used as a proof of that band.\n"
report=report.replace('\n# proof dependencies and changed downstream conclusions',validation+'\n# proof dependencies and changed downstream conclusions')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: Stage 20261011T234101Z complete locally: B09 biased-block core independently accepted; 6368 blocks and 2304 trees checked; C019 universal payment and full FEI remain open.\nNEXT: Test the complete corrected charge on the live overlapping-control stopping tree against its single-use local deficit reserves and certified terminal credits; A090/A085 review the ledger.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage 20261011T234101Z: followed B19 v2 request for a second independent B09 core review after consuming A093. Checked primary MU pages 1103-1104; reconstructed physical joint law and block uncertainty; accepted core unchanged. Derived corrected-entropy/deficit tree consumption and literal terminal cancellation. {count:,} exact assertions across 6368 blocks, 2304 trees and endpoints passed; initial full-law watchdog required frozen 16-mask scheduling. AND margin >1195/10000 certified. C019 complete-charge payment is the first unsupported universal step. Local four protocol files and readback receipts saved; remote adoption pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 20261011T234101Z durable facts: B09 core L=M+J and J<=M+Delta follows primary MU on each normalized product fiber; Boolean child Parseval is essential for the actual physical branch law. Delta(p)=r log2((1-r)/r), r=min(p,1-p), tends to zero at deterministic endpoints after deleting deterministic coordinates. For corrected entropy H-h0+sum I_i log2(4p_i(1-p_i)), a block decrement is M+J+normalization credit+E h0(child)-h0(parent); deficit spending is I_A minus spectral mass on nonempty sets supported wholly in A. Adaptive finite trees telescope these exact quantities. Biased literals have zero corrected entropy and deficit, and their credits cancel exactly; the MU upper ledger still overpays them. Hence retained terminal credits and an actual-charge universal budget are necessary before asserting C019 closure. Exhaustive bounded jobs should use explicit disjoint mask slices when the wall watchdog trips.\n')
protocol=read(REPORTS/'EXECUTION_PROTOCOL.json')
def find(obj,key):
    if isinstance(obj,dict):
        if key in obj:return obj[key]
        for v in obj.values():
            got=find(v,key)
            if got is not None:return got
    elif isinstance(obj,list):
        for v in obj:
            got=find(v,key)
            if got is not None:return got
    return None
for key,obj in [('progress_fields',progress),('claim_fields',original)]:
    fields=find(protocol,key);assert fields is not None
    expected=[s.split(' (')[0] for s in fields]
    assert set(obj)==set(expected),(key,set(obj)^set(expected))
for field in find(protocol,'report_fields'):assert '# '+field in report,field
assert read(ROOT/'PACKET_DELTA.json')==read(ROOT/'PROGRESS.json')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
local=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        local.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(ROOT/'out/RECEIPTS.json',{'status':'PASS','timestamp_utc':now,'protocol_schema_checks':'exact claim/progress fields; required report headings; packet delta identical; statement hash unchanged; STATUS exactly two lines','total_exact_assertions':count,'files':local,'external_persistence':'pending supervisor copy; no remote receipt claimed'})
print(json.dumps({'status':'PASS','files':len(local),'blocks':6368,'trees':2304,'exact_assertions':count,'claim_hash':statement_hash}))
