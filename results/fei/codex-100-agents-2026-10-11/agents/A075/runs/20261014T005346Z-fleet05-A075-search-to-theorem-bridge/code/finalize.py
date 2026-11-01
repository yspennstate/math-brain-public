from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime,sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
OLD=ROOT.parent/'20261013T212622Z-fleet05-A075-search-to-theorem-bridge'/'code'/'check_matching.py'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
BASE=Path('~/brain_workers/FEI100_20261011')
S84=BASE/'agents/A084/runs/20261014T000747Z-fleet05-A084-continuum-parameters'
def sha(data):return hashlib.sha256(data).hexdigest()
def dump(name,x): (ROOT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if '--prepare' in sys.argv:
    (ROOT/'code/arithmetic.py').write_text(OLD.read_text().split('\nfinite=[];')[0],encoding='utf-8')
    dump('out/FINAL_HELPER_FREEZE.json',{'version':'A075-rare-tail-v1-final-serialization-and-standalone-packaging','domain_unchanged':True,'max_runtime_seconds':60,'memory_estimate_MB':100,'files':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in (ROOT/'code').glob('*.py')},'amendments':'Exact coefficient checks and both first-block coordinates implement the original frozen fixture domain; point-defect parent is compressed, never enumerated; standalone helper is a byte copy of own earlier definitions.'})
    print('Standalone helper and final fixture freeze saved.')
    raise SystemExit

protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
loss=json.loads((ROOT/'out/INFINITE_LOSS_CERTIFICATE.json').read_text())
kap=Q(loss['total_upper']);assert kap<Q(457,500)
continuum=json.loads((ROOT/'out/INDEPENDENT_CONTINUUM_CERTIFICATE.json').read_text())
assert len(continuum['boxes'])==208
assert all(Q(x['slope_interval'][0])>0 for x in continuum['boxes'])
valid=json.loads((ROOT/'out/VALIDATION.json').read_text())
assert valid['direct_cores']==14 and valid['point_defects']==5
direct=json.loads((ROOT/'out/DIRECT_PHYSICAL_FIXTURES.json').read_text())
assert all(len(x['B_identity_intervals'])==2 for x in direct)
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',S84/'REPORT.md',S84/'PROOF.md',S84/'CLAIMS.json',S84/'out/MINORITY_ORIENTATION.json',S84/'out/COMPLEMENT_ORIENTATION.json',S84/'code/save_stage.py',BASE/'agents/A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine/REPORT.md',BASE/'agents/A089/runs/20261014T000812Z-fleet05-A089-repair-specialist/REPORT.md',BASE/'agents/A074/runs/20261014T000656Z-fleet05-A074-independent-reproducer/REPORT.md',OLD]
receipts=[]
for p in sources:
    assert p.is_file(),str(p)
    receipts.append({'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'role':'hash-convention locator only; not executed' if p.name=='save_stage.py' else ('accepted mathematical dependency' if S84 in p.parents else 'protocol, board, context or own helper')})
dump('out/SOURCE_RECEIPTS.json',receipts)
consumers=['A071','A072','A074','A084','A089','A092','B15','B20']
review=json.loads((S84/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert review['claim_id']=='A084-F6-CONTINUUM-ADMISSION' and review['version']==1
assert sha(json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},sort_keys=True,separators=(',',':')).encode())==review['statement_sha256']
review['review_records'].append({'reviewer':'A075','decision':'ACCEPT_AT_STATED_SCOPE','independence':'Independent exact uniform-Walsh polynomial reconstruction and 192-bit interval implementation; convexity in logarithmic packet ratio proves the all-t step; analytic complement endpoint independently checked; no substantive repair','source':str(ROOT/'PROOF.md'),'certificates':['out/INDEPENDENT_PACKET_ALGEBRA.json','out/INDEPENDENT_CONTINUUM_CERTIFICATE.json'],'source_statement_hash_preserved':True})
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_A075_LOCAL_RECORD'
statement=("For every nonconstant Boolean g on any finite uniform cube and every delta,eta>0, a finite oriented composition F of six disjoint identical copies at each level with the six-bit gate negative on {0,1,2,4,8,16,32,6,17,40} has minority probability<=delta, I(F)<=eta, and E(F)>=E(g)-kappa, E=min_(Inf_i>0) H(S_i|S_-i)/Inf_i, where kappa="+str(kap)+"<457/500. The single orientation policy is minority-negative up to minority 7/32 and complemented above it, followed by output orientation to its minority. Every actual dyadic bias enters minority<1/16 in finite time; all relevant coordinates remain relevant and no new coordinate type is admitted. At every finite rare-tail depth d, H(g0)/I(g0)-24/5<=H(g_d)/I(g_d)<=H(g0)/I(g0)+16, retaining the exact full starting entropy via H(g_(s+1))=6q_s H(g_s)+C_(p_s). Thus for every fixed delta,eta>0, the supremum M of E over actual cores with minority<=delta and I<=eta satisfies sup_g E(g)-kappa<=M<=sup_g E(g), in the extended-real sense. A finite M implies full FEI with constant M+kappa+2/ln(2); no finite M or universal FEI bound is asserted.")
new={'claim_id':'A075-RARE-CORE-LOCALIZATION','version':1,'exact_statement':statement,'hypotheses':['Finite arbitrary-dimensional uniform physical cube; actual nonconstant Boolean signs','Six independent identical copies on disjoint supports at every finite level; specified matching gate','Entropy in bits; true conditional spectral erasure and true physical influence','A084-F6-CONTINUUM-ADMISSION@1 independently accepted at unchanged stated scope in this run','delta,eta are arbitrary positive real numbers; no uniform dimension/depth bound claimed'],'statement_sha256':sha(statement.encode()),'contributors':['A075'],'proof_source':{'proof':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),'certificates':['out/INFINITE_LOSS_CERTIFICATE.json','out/BIAS_DYNAMICS_CERTIFICATE.json','out/INDEPENDENT_PACKET_ALGEBRA.json','out/INDEPENDENT_CONTINUUM_CERTIFICATE.json'],'validation':['out/VALIDATION.json','out/DIRECT_PHYSICAL_FIXTURES.json','out/POINT_DEFECT_FIXTURES.json']},'proof_dependencies':['A084-F6-CONTINUUM-ADMISSION@1; accepted independently by A075 in this run'],'review_records':[],'status':'AUTHOR_PROVED_UNIVERSAL_REDUCTION_REVIEW_PENDING_FULL_FEI_OPEN','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':consumers}
claims=[review,new]
claimfields=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==claimfields for c in claims)
dump('CLAIMS.json',claims)
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B15','packet_id':'A075','gap_id':'G-R-SELECT','attempt_id':'A075-RARE-LOCALIZATION-3','method':'Independent continuum review; actual-bias polynomial iteration; signed reserve convexity and summable rare error; full entropy composition ledger','mathematical_delta':'All-dimensional actual-core localization to arbitrarily rare and small-influence cores with E loss<0.914; complete rare-tail H/I correction between -24/5 and +16; A084 continuum admission independently accepted; full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'UNIVERSAL_LOCALIZATION_REDUCTION_PROVED_REVIEW_PENDING; RARE_CORE_SUPREMUM_BOUND_OPEN; FULL_FEI_OPEN','claim_versions_used':['A084-F6-CONTINUUM-ADMISSION@1 independently accepted at stated scope','A075-SPARSE-MATCHING-HEREDITARY-CLOSURE@1 accepted by A074; dispatch context only','A089 sharp boundary test independently reconstructed; source context, not premise','C005 physical restriction scalar bound independently reconstructed, not unreviewed premise'],'claims_created_or_changed':['A075-RARE-CORE-LOCALIZATION@1','A084-F6-CONTINUUM-ADMISSION@1 local independent acceptance record only'],'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','out/FROZEN_SPEC.json','out/CONTINUUM_REVIEW_SPEC.json','out/FINAL_HELPER_FREEZE.json','out/VALIDATION.json','out/INFINITE_LOSS_CERTIFICATE.json','out/BIAS_DYNAMICS_CERTIFICATE.json','out/INDEPENDENT_PACKET_ALGEBRA.json','out/INDEPENDENT_CONTINUUM_CERTIFICATE.json','out/DIRECT_PHYSICAL_FIXTURES.json','out/POINT_DEFECT_FIXTURES.json','out/SOURCE_RECEIPTS.json','out/MANIFEST.json','code/check_rare.py','code/check_continuum.py','code/arithmetic.py','code/finalize.py'],'next_consumers':consumers,'next_action':'Bound or construct unbounded E among actual arbitrary-dimensional cores with p_min<=1/16 and arbitrarily small total influence, using the new localization reduction and identifying a realizability constraint beyond singleton bounds. A074/A092 review rare loss, bias escape and terminal entropy constants.','stagnant_substantive_attempts':0,'blockers':['No dimension-independent bound on localized rare-core E supremum; full FEI remains open','Moderate-prefix entropy bill not uniformly paid; composition ledger is not restriction-tree ownership','New localization independent review and supervisor/mirror adoption pending'],'packet_ids':['A075']}
progressfields=set(protocol['required_per_run']['progress_fields']);progressfields.remove('packet_ids (one primary ID, for compatibility)');progressfields.add('packet_ids')
assert set(progress)==progressfields
dump('PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.strip().split('\n')[-1].startswith('**Universal bridge:**')
status='STATE: A075 stage3 complete: all-dimensional rare/small-I localization with erasure loss<0.914 and retained rare-tail H/I bill in [-24/5,+16]; A084 continuum independently accepted; new theorem review pending; FEI OPEN.\nNEXT: Bound or disprove the localized rare-core E supremum in arbitrary dimension; A074/A092 review infinite-loss certificate, irrational bias escape and terminal entropy ledger.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
tag='2026-10-14 stage3 20261014T005346Z'
work='\n'+tag+': consumed A084 continuum dependency after A074 accepted stage2. Independently reconstructed32 packets/four weights/208 interval boxes (6365 assertions); proved actual dyadic bias escape from unique irrational fixed point; rare signed losses sum to kappa<0.914; retained full entropy identity and rare-tail correction [-24/5,+16]. Final rare fixtures: '+str(valid['checks'])+' assertions, '+str(valid['runtime_seconds'])+' seconds. Serialization-only pilot issue repaired. Full FEI gap is localized rare-core E bound; no finite scan promoted to theorem.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    if tag not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'):f.write(work)
lesson='\n'+tag+' durable: For every actual Boolean g and delta,eta>0, finite oriented disjoint f6 composition produces p_min<=delta,I<=eta,E>=E(g)-kappa, kappa<0.914. Moderate continuum independently reviewed; rare U/D>=49p^2 and beta^2/Inf<=2p imply loss<=2p log2(1/(49p^2)); tau<=12p^2 makes the total summable. Unique moderate fixed point solves2p^5-12p^4+27p^3-28p^2+12p-1=0 and is irrational, so actual dyadic biases cannot stick. Exact Hnext=6qH+C, Inext=6qI; rare C in[-144p^2,360p^2], retained-tail H/I in[start-24/5,start+16]. No bound on arbitrary rare-core E, or uniform moderate-prefix entropy payment, follows. A finite localized E supremum M would give FEI constant M+kappa+2/ln2.\n'
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    if tag not in (AGENT/'LEARNED.md').read_text(encoding='utf-8'):f.write(lesson)
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.name=='MANIFEST.json' or '__pycache__' in p.parts:continue
    assert p.stat().st_size<20*1024*1024,str(p)
    files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
dump('out/MANIFEST.json',{'local_only':True,'files':files,'commands':['python -X utf8 code/check_rare.py','python -X utf8 code/check_continuum.py','python -X utf8 code/finalize.py'],'packet_delta_byte_identical':True,'statement_hashes_checked':True,'full_fei':'OPEN','supervisor_copy':'PENDING','independent_review_new_claim':'PENDING'})
print(json.dumps({'claims':len(claims),'rare_checks':valid['checks'],'continuum_checks':continuum['checks'],'kappa_upper':float(kap),'files':len(files),'full_fei':'OPEN'}))
