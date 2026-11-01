"""Persist protocol-exact records and verify local receipts (no external writes)."""
from pathlib import Path
import hashlib, json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
REPORT_ROOT=Path('~/mop_fei100/reports/fei-2026-10-11')
SUPP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
CONTEXT=Path('~/brain_workers/FEI100_20261011/context')
def write(p,obj):
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

protocol=json.loads((REPORT_ROOT/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
primary=json.loads((RUN/'out/validation.json').read_text())
pairs=json.loads((RUN/'out/pairs_validation.json').read_text())
assert primary['result']==pairs['result']=='PASS'
assert primary['cases']==2040 and pairs['cases']==8128
assert primary['seconds']<60 and pairs['seconds']<60

statement=(
    'For each rooted singleton-leaf partition tree T of [N] with 2 or 3 children per internal vertex, '
    'L_T(S)=1+sum_v b_v*1{S intersects C_v} is the length of an all-subset prefix code, '
    'max L_T<=3N-2, and H(f)<=Gamma_T(f)=sum_S fhat(S)^2 L_T(S). '
    'If Boolean f,g differ on input fraction rho, sqrt(Gamma_T(f))<=sqrt(Gamma_T(g))+'
    '2 sqrt(rho max L_T), and |I(f)-I(g)|<=2N rho. '
    'For complete depth-d ternary recursive majority g_d, d>=1, padded to N>=3^d bits, '
    'the explicit main/padding tree satisfies Gamma_T(g_d)<=6I(g_d)-3. '
    'Every truth-table edit f of this g_d satisfies Gamma_T(f)<=12I(f)-6+48N rho-16rho; '
    'in particular H(f)<=Gamma_T(f)<=12I(f) if N rho<=1/8. '
    'Every one-point edit satisfies H(f)<=Gamma_T(f)<=25I(f), and <=12I(f) for N>=6. '
    'For fixed d the code-cost difference under padding and one-point editing tends to zero.'
)
hypotheses=[
    'Uniform finite sign cube; actual Boolean f,g.',
    'Entropy and code lengths in bits; I=sum_S |S| fhat(S)^2.',
    'Tree and ordered child cells fixed for the source, not chosen after observing S.',
    'Singleton leaves, no unary vertices, internal arity 2 or 3.',
    'Family conclusions require d>=1, N>=3^d, complete ternary recursive majority base and Boolean flips on D.',
    'No arbitrary unpaid Boolean terminal is included in the family.'
]
canonical=json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':'))
claim={
    'claim_id':'A069-STABLE-HIERARCHY-EDIT-PAYMENT',
    'version':1,
    'exact_statement':statement,
    'hypotheses':hypotheses,
    'statement_sha256':hashlib.sha256(canonical.encode('utf-8')).hexdigest(),
    'contributors':['fleet05/A069'],
    'proof_source':{'path':str(RUN/'REPORT.md'),'locators':'equations (1)-(12)','sha256':sha(RUN/'REPORT.md')},
    'proof_dependencies':[],
    'review_records':[],
    'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],
    'refutes':[],
    'first_unproved_line':None,
    'next_consumers':['A070','A088','A094','A008','A011','B20']
}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
write(RUN/'CLAIMS.json',[claim])

progress={
    'protocol_revision':protocol['revision'],
    'run_id':RUN.name,
    'stream':'B14',
    'packet_id':'A069',
    'gap_id':'G-A069-STABLE-ENCODING',
    'attempt_id':'A069-geometric-transfer-1',
    'method':'all-subset hierarchy prefix decoder; weighted Parseval stability; direct Maj3 occupancy branching; exact integer-Walsh validation',
    'mathematical_delta':'C020 scoped payment for arbitrary sparse truth-table edits of padded recursive majority: code<=12I when N*rho<=1/8 and <=25I for any one-point edit; generic cost-stability interface; universal tree/reference payment remains open.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; INDEPENDENT_REVIEW_AND_MIRROR_PENDING',
    'mathematical_status':'RESTRICTED_THEOREM_AUTHOR_PROVED; FULL_FEI_OPEN',
    'claim_versions_used':[],
    'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','ABSTRACT_GEOMETRIC_ENCODING.tex','NONSPATIAL_FAMILY_PROOF.md','FROZEN_SPEC.json','FROZEN_PAIRS_SPEC.json','code/validate.py','code/validate_pairs.py','out/validation.json','out/pairs_validation.json','out/source_manifest.json'],
    'next_consumers':claim['next_consumers'],
    'next_action':'Replace rho*N by exact weighted edit-spectrum energy and pay it by edit boundary on disjoint subcube edits, retaining restricted-core entropy; A088/A094 independently reconstruct.',
    'stagnant_substantive_attempts':0,
    'blockers':[],
    'packet_ids':['A069']
}
# Protocol lists an explanatory parenthetical after packet_ids; the compatibility
# section and user contract specify the actual JSON key as packet_ids.
progress_keys={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_keys
write(RUN/'PROGRESS.json',progress)
write(RUN/'PACKET_DELTA.json',progress)

paths=[REPORT_ROOT/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [SUPP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list(CONTEXT.glob('*.txt'))
paths += [Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md')]
paths += [SUPP/'sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']
paths += sorted((REPORT_ROOT/'runs').rglob('REPORT.md'))
write(RUN/'out/source_manifest.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths])

(AGENT/'STATUS.md').write_text('STATE: A069 stable hierarchy encoding and sparse-edit recursive-majority payment proved locally; 10,168 cases / 2,509,978 exact checks PASS; independent review pending; full FEI OPEN.\nNEXT: A088/A094 review; pay exact edit-spectrum cost by boundary on disjoint subcube edits, retaining restricted-core entropy to advance C020.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as h:
    h.write('2026-10-12: Completed all-set Kraft decoder, weighted-L2 perturbation transfer, 12I sparse-edit and 25I one-point family proofs. Exact one-point pilot: 2,040 cases, 1,437,082 assertions, 3.958 seconds. Exact two-point pilot: 8,128 cases, 1,072,896 assertions, 3.006 seconds. Source/required-schema receipts saved locally; independent review, supervisor copy and mirrors pending. Full FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as h:
    h.write('For depth-d ternary recursive majority, every depth-j cell has spectral occupation probability 2^{-j}; the level expectation is (3/2)^j, I=(3/2)^d, and internal occupancy sum=2(I-1).\n')
    h.write('An all-set code (root bit, arity-many bits per occupied mask) with a binary padding join has base expected length <=6I-3 and maximum length <=3N-2. If a Boolean edit set has fraction rho, code cost <=12I(edited)-6+48N*rho-16rho; N*rho<=1/8 gives 12I. Every one-point edit for d>=1 gives 25I, and 12I for N>=6.\n')
    h.write('Do not use the exact 2-bit/four-mask base code after editing: it omits newly created Fourier sets. Uniform singleton non-Boolean spectra have tree cost 1+3d with I=1, locating the missing Boolean occupancy payment. Universal tree/reference selection remains open.\n')

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves C020')
assert json.loads((RUN/'PACKET_DELTA.json').read_text())==json.loads((RUN/'PROGRESS.json').read_text())
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='receipts.json' and '__pycache__' not in p.parts)
files += [AGENT/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for p in files:
    assert p.stat().st_size < 20_000_000
receipts={'scope':'LOCAL_ONLY; independent review and supervisor mirrors pending','required_schemas':'exact protocol field sets verified','validation_cases':primary['cases']+pairs['cases'],'exact_assertions':primary['assertions']+pairs['assertions'],'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
write(RUN/'out/receipts.json',receipts)
print(json.dumps({'schema_checks':'PASS','cases':receipts['validation_cases'],'exact_assertions':receipts['exact_assertions'],'receipt_files':len(files),'receipts_sha256':sha(RUN/'out/receipts.json')},indent=2))
