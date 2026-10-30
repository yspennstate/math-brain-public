"""Persist the owned stage and check protocol schemas and exact receipts."""
from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
HOME=Path(r'~')
CAM=HOME/'mop_fei100/reports/fei-2026-10-11'
C=HOME/'brain_workers/FEI100_20261011'
STAMP=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

protocol=read(CAM/'EXECUTION_PROTOCOL.json')
val=read(R/'out/validation.json');bal=read(R/'out/balanced_validation.json')
assert val['status']==bal['status']=='PASS'
assert val['seed_cases']==278 and bal['balanced_seed_cases']==66
assert sha(R/'code/check.py')==read(R/'FROZEN_SPEC.json')['helper_sha256']==val['helper_sha256']
assert sha(R/'code/balanced.py')==read(R/'BALANCED_SPEC.json')['helper_sha256']==bal['helper_sha256']

origin=C/'agents/A032/runs/20261014T105923Z-fleet05-A032-boolean-phase-realizability'
source=next(x for x in read(origin/'CLAIMS.json') if x['claim_id']=='A032-PRODUCT-BRANCH-MASS-RIGIDITY')
assert source['statement_sha256']==hashlib.sha256(source['exact_statement'].encode('utf-8')).hexdigest()
assert source['proof_source']['sha256']==sha(origin/'MASS_RIGIDITY.md')
review=dict(source)
review['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A079_LOCAL_REGISTRY_ADOPTION_UNVERIFIED'
review['review_records']=list(source['review_records'])+[{'reviewer':'A079','at':STAMP,'verdict':'HOLDS_AT_STATED_SCOPE','source':str(R/'REVIEW_A032.md'),'method':'Independent primitive-integer/mod4/entropy reconstruction; no repair, no author implementation imported','finite_validation':'out/validation.json','formal_verification':'NOT_CLAIMED'}]

statement=('There exist fixed complementary ternary/indicator rows a,b on four uniform physical bits, '
'with E a^2=5/8 and E b^2=3/8, such that for every Boolean seed h on a disjoint uniform cube, '
'F_h(z,u,x)=a(u)+z*b(u)*h(x) is Boolean, its z-frequency0 normalized squared row remains the same '
'coordinate-product law with three fair marginals and one4:1 marginal, its other row is nonproduct, '
'H(F_h)=5-(9/16)log2(3)+(3/8)H(h), I(F_h)=17/8+(3/8)I(h), '
'I_z=3/8 and I_(u,x)=7/4+(3/8)I(h). With X=(z,unused d) and Y=(u,x), '
'H(Y|X)=(5/8)[7/5+log2(5)]+(3/8)[3-(1/2)log2(3)+H(h)] and the signed '
'address/order1/2-Renyi gap is3/4-2log2(3)-(3/8)R(h). For h_t=ell times t independent '
'copies of any nonconstant Boolean seed f, the joint and conditional/data-influence ratios tend '
'to H(f)/I(f), while the address/seed spectral mutual information is exactly h2(3/8). '
'A universal FEI bound on this fixed-mask one-product-branch class therefore implies full FEI '
'at the same constant; no unbounded-ratio Boolean seed or full-FEI proof is supplied.')
claim={'claim_id':'A079-FIXED-NONFAIR-SIBLING-SEED-TRANSPORT','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs on independent uniform physical cube; fixed displayed a,b on16 points',
               'Fresh seed variables and fresh physical address z; optional second address unused',
               'All entropies in bits; influence in original physical coordinates; R is order1/2',
               'Limit uses nonconstant seed I(f)>0 and accounts for balancing sign ell'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':['out/validation.json','out/balanced_validation.json'],'formal_verification':'CORE_LEAN_ATTEMPT_RUNTIME_UNVERIFIED; no theorem certificate'},
 'proof_dependencies':[], 'review_records':[],
 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[], 'refutes':[],
 'first_unproved_line':None,'next_consumers':['A032','A034','A088','A094','A096','A097','B16','B20']}
claims=[review,claim]
expected=set(protocol['required_per_run']['claim_fields'])
assert all(set(x)==expected for x in claims)
save(R/'CLAIMS.json',claims)

next_action=('Transport a supplied incoming reference through one active physical restriction of '
'F_h=a+zbh, retaining both child normalizers, complete complementary seed terminal, signed '
'negative Renyi term and the SAME surviving seed-energy reserve; A088/A094 review and '
'A032/A034/A096/A097 consume the saved handoff.')
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B16','packet_id':'A079',
 'gap_id':'G-PHASE-COND','attempt_id':'A079-stage6-fixed-nonfair-sibling-seed-transport-v1',
 'method':'Consume mass-rigidity dependency; independent proof reconstruction; explicit complementary-mask Boolean embedding; exact full entropy/energy/Renyi ledger and tensor guard',
 'mathematical_delta':'A032 mass rigidity independently HOLDS; unequal two-product target eliminated. Fixed5/8 nonfair product sibling admits arbitrary seed in3/8 complement with exact all-dimensional ratio-preserving and persistently correlated completion. Admission-only extension retains full FEI.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_AND_EXACT_CHECKS',
 'mathematical_status':'FULL_FEI_OPEN; new exact obstruction author-proved, independent review pending; no Lean certificate',
 'claim_versions_used':['A032-PRODUCT-BRANCH-MASS-RIGIDITY@1'],
 'claims_created_or_changed':['A032-PRODUCT-BRANCH-MASS-RIGIDITY@1: A079 independent acceptance','A079-FIXED-NONFAIR-SIBLING-SEED-TRANSPORT@1'],
 'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A032.md','HANDOFF.md','CLAIMS.json','FROZEN_SPEC.json','BALANCED_SPEC.json','LEAN_SPEC.json','out/validation.json','out/balanced_validation.json','out/lean_output.txt','out/SOURCE_MANIFEST.json','out/PERSISTENCE_RECEIPT.json'],
 'next_consumers':['A032','A034','A088','A094','A096','A097','B16','B20'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['No independent review of new fixed-mask embedding recorded','Shared registry adoption and remote copies unverified','Core Lean returned RUNTIME_UNVERIFIED with no target certificate; mathematical proof is paper+exact checks'],
 'packet_ids':['A079']}
keys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==keys
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

sources=[]
def record(p,role):
 if p.is_file():sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'role':role})
record(HOME/'AGENTS.md','machine instructions')
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
 record(CAM/name,'execution source; registry/plan at relevant B16,G-PHASE-COND and obstruction locators')
record(C/'BOARD.md','stage-entry coordination snapshot; selected related rows read')
record(C/'claude/B16/STREAM_NOTES.md','lead v2 full')
for name in ['MASS_RIGIDITY.md','REPORT.md','CLAIMS.json','out/ternary_obstruction.json','out/truth_tables.json']:
 record(origin/name,'A032 exact source; independently reconstructed or fixture read')
for name in ['REPORT.md','BOUNDARY.md','CLAIMS.json']:
 record(A/'runs/20261014T060856Z-fleet05-A079-correlated-auxiliaries'/name,'own productive predecessor')
sup=HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ISOSPECTRAL_SPLICING_CURATED.md']:
 record(sup/name,'supplement background at relevant normalization/tensor/retained-entropy scope')
for p in (C/'context').glob('*.txt'):record(p,'paper text inspected at scope/entropy/composition locators; cp1252; no theorem imported')
save(R/'out/SOURCE_MANIFEST.json',{'saved_at':STAMP,'sources':sources,'priority':'Current user scope and endpoint supersede historical campaign dates; current wake warned of stale owner-model notes, not used as mathematical premises'})

rp=R/'REPORT.md';text=rp.read_text(encoding='utf-8')
text=text.replace('Actual outputs and runtime are in out/balanced_validation.json.',f'PASS:{bal["assertions"]} exact assertions in{bal["seconds"]:.4f}s. Actual outputs are in out/balanced_validation.json.')
text=text.replace('after its bounded attempt, with no compiler output or','after74.139s wall time (requested compiler timeout60s, plus wrapper/launch overhead), with no compiler output or')
rp.write_text(text,encoding='utf-8')

(A/'STATUS.md').write_text('STATE: Stage6 saved: A032 mass rigidity independently HOLDS; fixed5/8 nonfair product sibling retains arbitrary seed in3/8 complement, full-FEI strength;344 exact seed completions PASS; FEI OPEN.\nNEXT: Carry incoming reference through active physical query with both child normalizers, full seed terminal, signed Renyi gap and SAME unused seed reserve; A088/A094 review, A032/A034/A096/A097 consume.\n',encoding='utf-8')
worklog=A/'WORKLOG.md'
with worklog.open('a',encoding='utf-8') as f:f.write(f'\n{STAMP} stage6 fleet03: independently reconstructed A032 mass-rigidity@1; retired old unequal-two-product NEXT. Constructed fixed5/8 nonfair-product sibling with arbitrary3/8 complementary seed, exact H=5-9log2(3)/16+3H(h)/8,I=17/8+3I(h)/8 and signed gap3/4-2log2(3)-3R(h)/8. Checks278 seed cases/3085 assertions plus66 balanced cases/596 assertions PASS. Core Lean runtime-unverified; no formal claim. Saved protocol bundle and handoff; full FEI OPEN.\n')
learned=A/'LEARNED.md';s=learned.read_text(encoding='utf-8-sig')
old='- First unpaid step: a nonfair branch has an odd norm factor, so probability need not be1/2;'
new='- SUPERSEDED 2026-10-21 by A032-PRODUCT-BRANCH-MASS-RIGIDITY@1 (independently reconstructed here): two positive product branches MUST be fair and mass1/2; the old unequal-two-product target is impossible. The following older observation applies only to a standalone product row with a forced NONPRODUCT complement: a nonfair branch has an odd norm factor, so probability need not be1/2;'
if old in s:s=s.replace(old,new)
s+='\n2026-10-21 stage6 durable facts:\n- A032 product-branch mass rigidity@1 independently HOLDS: primitive ternary product norm reduced numerator1mod4; complementary positive such masses force1/2 and fair marginals. Do not search for unequal two-product Boolean splits.\n- Fixed a,b on four bits, a product/nonfair mass5/8, b indicator/nonproduct mass3/8, admit F_h=a+zbh for EVERY Boolean seed h. H=5-(9/16)log2(3)+(3/8)H(h), I=17/8+(3/8)I(h), I_data=7/4+(3/8)I(h). One nonfair product sibling does not exclude arbitrary seed entropy in its complement.\n- Balancing h_t=ell*f^tensor t costs3/8 in F. Its spectral address/seed mutual information is exactlyh2(3/8), and both joint and conditional/data ratios tend to H(f)/I(f). Hence this fixed-mask correlated class retains full FEI.\n- Full signed address gap is3/4-2log2(3)-(3/8)R(h), R order1/2. It cancels the full complementary seed Renyi bill; only Shannon seed debt remains. Preserve the same seed reserve across an active physical query.\n- Exact278 seed checks and66 balanced completions PASS; core Lean returned RUNTIME_UNVERIFIED and supplies no theorem certificate. New embedding paper proof awaits independent review; no full FEI resolution.\n'
learned.write_text(s,encoding='utf-8')

for heading in protocol['required_per_run']['report_fields']:
 assert '# '+heading in rp.read_text(encoding='utf-8'),heading
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
entries=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  entries.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
save(R/'out/PERSISTENCE_RECEIPT.json',{'saved_at':STAMP,'status':'LOCAL_FILES_AND_SCHEMAS_VERIFIED','assertions':val['assertions']+bal['assertions'],'Boolean_completion_cases':344,'source_review_statement_hash_preserved':True,'new_claim_independent_review':'PENDING','formal_result':'RUNTIME_UNVERIFIED','progress_delta_identical':True,'remote_mirror':'NOT_VERIFIED','files':entries})
print(json.dumps({'status':'PASS','files':len(entries),'exact_assertions':val['assertions']+bal['assertions'],'completions':344,'schema':'exact protocol fields; identical progress/delta','full_FEI':'OPEN'}))
