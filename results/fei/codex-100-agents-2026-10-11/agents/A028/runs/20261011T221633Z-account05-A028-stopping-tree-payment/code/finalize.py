from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

RUN = Path(__file__).resolve().parents[1]
AGENT = RUN.parents[1]
TEAM = AGENT.parents[1]
CANON = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPP = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
STAMP = datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def save(name, data):
    (RUN/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

protocol = json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
validation = json.loads((RUN/'out/validation.json').read_text(encoding='utf-8'))
assert validation['assertions_passed'] == 106858
inventory = []
def pin(path,scope):
    raw = path.read_bytes()
    inventory.append({'path':str(path),'sha256':sha(raw),'bytes':len(raw),'scope':scope})
    return sha(raw)

for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json',
             'OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json',
             'FEI_100_agent_research_plan.tex']:
    pin(CANON/name,'Protocol complete; other campaign files consulted for B06 route, contracts and relevant obstructions')
for q in (CANON/'runs').rglob('REPORT.md'):
    pin(q,'Original prior-run provenance and obstruction scope; not a positive proof dependency')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    pin(SUPP/name,'Route and scope consultation, especially C019 and terminal admission guards')
for q in (SUPP/'sources').iterdir():
    if q.is_file():
        pin(q,'Inventoried; block identity, erasure reduction, and logarithmic allocation actually inspected; other notes not proof premises')
for name in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt',
             'percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    pin(TEAM/'context'/name,'cp1252 text; threshold A/C/D, Section 8.4 and scope introductions; percolation conventions/scope only')
pin(TEAM/'BOARD.md','Stage-start board read')
for who,filename in [('A026','GOOD_COORDINATE_TARGET.tex'),('A027','ADAPTIVE_BLOCK_SELECTION.tex'),('A021','REPORT.md')]:
    q=next((TEAM/'agents'/who/'runs').rglob(filename))
    pin(q,'A026/A027 original proofs independently reconstructed; A021 balanced scope comparison')
save('out/source_inventory.json',{'at':STAMP,'sources':inventory,'missing':str(TEAM/'claude/B06/STREAM_NOTES.md')})

claims=[]
for who in ['A026','A027']:
    source=next((TEAM/'agents'/who/'runs').rglob('CLAIMS.json'))
    for original in json.loads(source.read_text(encoding='utf-8')):
        item=dict(original)
        item['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
        item['review_records']=original['review_records']+[{
            'reviewer':'A028','verdict':'ACCEPT_AT_STATED_SCOPE','review_source':str(RUN/'INDEPENDENT_REVIEW.md'),
            'original_claims_source':str(source),'original_claims_sha256':sha(source.read_bytes()),
            'method':'Separate scalar integer Walsh/prime-log/combinatorial reconstruction plus analytic hereditary/block/limit proofs',
            'validation_source':str(RUN/'out/validation.json'),'at':STAMP}]
        claims.append(item)

statement=('For every finite-dimensional uniform-cube Boolean sign g, r>=1 fresh point-controls, '
           'p=2^-r, delta=Pr(g=-1), F=1+A_r(g-1), and the control-first physical stopping tree, '
           'the actual magnitude-mismatch/KL bill obeys E sum J <= (3+log2(e)/e) Q and '
           'E sum (J+3log2(e)mu) <= kappa Q, where Q=2rp delta and '
           'kappa=3+log2(e)(3+1/e)<8. Adding any certified terminal allowance K I(g) gives '
           'complete expected path-plus-terminal payment <=max(kappa,K) I(F). '
           'Finite fresh point-activation, sign-negation and disjoint-physical-product expressions '
           'over FEI-certified terminals preserve this maximum constant independently of depth, '
           'control arity, core bias and factor count.')
new={
    'claim_id':'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT','version':1,
    'exact_statement':statement,
    'hypotheses':['Uniform physical product cube; Boolean sign outputs; bit entropy/KL',
                  'Fresh physical point-indicator controls; products on disjoint physical supports',
                  'J uses magnitude mismatch, including the last-child sign correction',
                  'Every terminal has an explicit FEI certificate; fixed overlap parameters when applicable'],
    'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A028'],
    'proof_source':str(RUN/'REPORT.md'),
    'proof_dependencies':['Recovered actual-child inequality Delta H<=J+3mu/ln2 (campaign plan sharper mismatch/KL paragraph)',
                          'Parseval and exact physical influence decomposition; disjoint Fourier tensorization',
                          'Terminal FEI certificates are hypotheses; recovered threshold Theorems A/C/D for their respective applications'],
    'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[],'first_unproved_line':None,
    'next_consumers':['A023','A029','A064','A065','A087','A094','A097','B20']}
claims.append(new)
save('CLAIMS.json',claims)

progress={
    'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B06','packet_id':'A028',
    'gap_id':'C019','attempt_id':'A028-C019-unbalanced-control-first-v1',
    'method':'Exact actual-child magnitude-mismatch packets, weighted KL bill, independent B06 reconstructions',
    'mathematical_delta':'Complete unbalanced control-first mismatch+linear payment kappa<8 with reserved terminal influence; finite fresh-activation/disjoint-product closure preserves recovered terminal constants; four B06 v1 reviews accepted locally',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
    'mathematical_status':'RESTRICTED_STOPPING_LEDGER_PROVED_FULL_FEI_OPEN',
    'claim_versions_used':['C019@conditional','recovered-mismatch-upper-bound@campaign-plan',
                           'threshold-38pp@Theorems-A-C-D-terminal-hypotheses',
                           'A026-AFFINE4-GOOD-COORDINATE@1-reviewed-here'],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
    'source_artifacts':[str(RUN/'REPORT.md'),str(RUN/'INDEPENDENT_REVIEW.md'),str(RUN/'code/check.py'),
                        str(RUN/'out/validation.json'),str(RUN/'out/source_inventory.json')],
    'next_consumers':['A029','A064','A065','A087','A094','B20'],
    'next_action':'Derive shifted-empty-row transport when a proper subset of a low-density core is revealed before its activation controls, retaining residual-core entropy and physical boundary',
    'stagnant_substantive_attempts':0,
    'blockers':['Universal terminal-admission/representation theorem remains unproved; no such claim made',
                'New lemma independent review and canonical adoption not yet observed; B06 lead notes absent'],
    'packet_ids':['A028']}
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)
expected=set(protocol['required_per_run']['claim_fields'])
for claim in claims:
    assert set(claim)==expected,(claim['claim_id'],set(claim)^expected)
assert set(progress)=={field.split(' (')[0] for field in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report,field

(AGENT/'STATUS.md').write_text('STATE: A028 saved complete C019 unbalanced control-first ledger kappa<8; four B06 v1 claims independently accepted locally; 106858 exact assertions; new lemma review pending; full FEI OPEN.\nNEXT: A087/A094 review; derive proper partial-core shifted-row transport beyond fresh-activation terminal admission, retaining all residual entropy.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{STAMP} — Read protocol/board and original B06 proofs; lead notes absent. Avoided duplicating A021 balanced ledger. Derived unbalanced actual magnitude mismatch, corrected last-node sign, proved complete KL+linear payment kappa=3+log2(e)(3+1/e)<8 and finite nested closure with terminal influence reserved. Independently reconstructed A026 two claims and A027 two claims; accepted at stated scopes, adoption pending. Final exact v2 checker: 1112 activations, 32906 global-sign census representatives, combinatorial 32-bit threshold, 106858 assertions in {validation["compute_seconds"]:.3f}s. Saved all protocol artifacts; universal admission gap remains.\n')
(AGENT/'LEARNED.md').write_text('''# A028 durable facts

For F=1+A_r(g-1), p=2^-r, delta=Pr(g=-1), the control-first queried influence is Q=2rpdelta and terminal influence is pI(g). At s>=2 active controls, u=2^-s, b0=1-4udelta>=0, mu=2udelta. At s=1, actual MAGNITUDE mismatch is min(delta,1-delta), not signed disagreement delta. Always J_s=mu-mu^2+mu^2log2(q0/mu^2), q0=(1+b0^2)/2.

Complete weighted KL/log bill J_tree<=(3+log2(e)/e)Q, and including all recovered 3mu/ln2 allowance gives kappa Q, kappa=3+log2(e)(3+1/e)<8. The scalar bound 6delta+2delta log2(1/(2delta))<=4 is the useful weighted-tail payment; do not truncate a negative log term independently.

Terminal K I(g) is paid from pI(g), yielding max(kappa,K) root influence. Finite fresh point-activations, output signs, and products with disjoint physical supports preserve this constant at any depth. Regular/fixed-overlap/threshold-formula source constants exceed 8 and are preserved. No arbitrary-root decomposition theorem is proved. Rare arbitrary cores still require pH(g) and preserve full FEI hardness.

A026 affine-dimension-four selection and symmetric-threshold amplitude obstruction v1, and A027 proper-core block and quantitative hardness v1, independently accepted locally in this run; source pins and reviewer records are saved. The small affine census is a finite exact lemma plus a hereditary physical support projection proof. No unrestricted Fourier-linear change is a physical query.

Validation uses integer Walsh, Fraction edge counts, exact prime-log equality vectors, and symmetric combinatorial coefficients. Final v2 passed 106858 assertions, 1112 activation cases and 32906 proxy representatives. Floating approximations were not sign certificates. Next universal work is partial-core shifted-row transport plus terminal admission, not more isolated activation endpoints.
''',encoding='utf-8')
receipt=[]
for q in sorted(RUN.rglob('*')):
    if q.is_file() and q.name!='persistence_receipt.json':
        raw=q.read_bytes()
        assert len(raw)<20*1024*1024
        receipt.append({'path':str(q.relative_to(RUN)),'bytes':len(raw),'sha256':sha(raw)})
save('out/persistence_receipt.json',{'at':STAMP,'protocol_field_sets_checked':True,
                                    'schema_note':'Protocol display label packet_ids (one primary ID, for compatibility) is serialized as packet_ids, as explicitly required by its compatibility rule and user instruction.',
                                    'progress_compatibility_equal':True,'artifacts':receipt,
                                    'mirror_status':'NOT_OBSERVED','new_claim_review':'PENDING'})
print(json.dumps({'files':len(receipt),'protocol_checks':'PASS','assertions':validation['assertions_passed'],
                  'run':str(RUN),'source_pins':len(inventory)},indent=2))
