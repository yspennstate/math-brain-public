from pathlib import Path
import hashlib,json,datetime
BASE=Path(__file__).resolve().parent.parent
HOME=BASE.parent.parent
ROOT=Path('~/mop_fei100/reports/fei-2026-10-11')
SUP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
CON=Path('~/brain_workers/FEI100_20261011/context')
protocol=json.loads((ROOT/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def save(name,data): (BASE/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(text): return hashlib.sha256(text.encode()).hexdigest()
consumers=['A023','A029','A039','A057','A063','A064','A097']
statements=[
 'For every finite adaptive transcript tree on a common finite joint law P(W,A,L), sum_h P(h) I(W;Y_h|A,h) + sum_l P(l) H(W|A,l) = H(W|A); every cut and subtree obey the same identity. For finite common-law divergences, K_h+j_h=d_h+E_P K_hy, hence sum_h P(h)d_h+sum_l P(l)K_l=K_root+sum_h P(h)j_h. Shared channels give zero injection; replacing a predicted child reference q by r adds E_p log2(q/r) on the resource side. All terminal terms are retained.',
 'For every Boolean function on a finite uniform cube and every finite adaptive physical block restriction tree, the function-specific kernel k_h(y|S_0)=2^(-|B_h|) (f_h|B_h=y)hat(S_0 intersect C_h)^2 / sum_U f_hhat(U union (S_0 intersect C_h))^2, on positive fibers, constructs a common root spectral/physical-transcript law with actual fair physical branches and actual child spectra. It satisfies sum_h P(h) J_h=I(S_0;L) and H(S_0|L)=sum_h P(h) H(S_h intersect B_h|S_h intersect C_h,h)+sum_l P(l)H(f_l). No universal phase-blind channel on parent squared spectra exists, as witnessed by f=[1,1,1,-1], g=[1,1,-1,1].'
]
ids=['A037-CONDITIONAL-CREDIT-CONSERVATION','A037-PHYSICAL-SPECTRAL-COMMON-LIFT']
claims=[]
for i,statement in enumerate(statements):
    claim=dict(claim_id=ids[i],version=1,exact_statement=statement,hypotheses=['Finite probability/tree spaces; bits; omit zero-probability histories','KL formulas require finite supported divergences' if i==0 else 'Boolean signs, uniform inputs, adaptive block choices measurable from physical history; no rerevealed coordinates'],statement_sha256=digest(statement),contributors=['A037'],proof_source={'run_id':BASE.name,'files':['REPORT.md','POSTERIOR_CREDIT_CHAIN.tex','NO_REUSE_CERTIFICATE.md','code/ledger_check.py','out/VALIDATION.json']},proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[] if i==0 else ['Universal physical-child spectral channel determined solely by squared parent Fourier masses'],first_unproved_line=None,next_consumers=consumers)
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    claims.append(claim)
save('CLAIMS.json',claims)
progress=dict(protocol_revision=protocol['revision'],run_id=BASE.name,stream='B08',packet_id='A037',gap_id='FEI-B08-A037-INITIAL',attempt_id='A037-conditional-ledger-01',method='Finite-tree conditional entropy/KL telescope with explicit channel/reference corrections; function-specific physical spectral lift; rational prime-log validation',mathematical_delta='Closed finite-hierarchy single-use identity and common physical lift; identified terminal posterior exactly with cumulative erasure plus terminal spectral entropy. Universal influence payment remains open.',deliverable_status='COMPLETE_LOCALLY_SAVED_REVIEW_PENDING',mathematical_status='PACKET_INTERFACE_AUTHOR_PROVED_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[c['claim_id']+'@1' for c in claims],source_artifacts=['REPORT.md','POSTERIOR_CREDIT_CHAIN.tex','NO_REUSE_CERTIFICATE.md','code/ledger_check.py','out/FROZEN_SPEC.md','out/VALIDATION.json','out/SOURCES_READ.json'],next_consumers=consumers+['A088','A094'],next_action='Compute channel injection and reference-reset corrections for a chosen parent/child witness generator on the sparse activated bent-defect physical tree; determine the exact influence-payment gap.',stagnant_substantive_attempts=0,blockers=['B08 STREAM_NOTES.md absent; not a blocker for independent packet proof','Independent A088/A094 review pending','Full-FEI payment of erased-label/witness cost and channel/reset corrections unproved'],packet_ids=['A037'])
# Protocol's last field includes an explanatory parenthesis; its wire key is
# packet_ids, explicitly required in the same protocol's compatibility section.
assert set(progress)=={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
paths=[ROOT/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
paths += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [SUP/'sources'/'BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']
paths += list(CON.glob('*.txt'))
paths += [Path('~/brain_workers/FEI100_20261011/BOARD.md')]
paths += list((ROOT/'runs').glob('B*/**/REPORT.md'))
save('out/SOURCES_READ.json',{'scope':'Sources inspected at the interfaces stated in REPORT.md; hashes pin bytes, not blanket theorem acceptance. Unrelated source files only inventoried.','sources':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],'absent':['~/brain_workers/FEI100_20261011/claude/B08/STREAM_NOTES.md']})
validation=json.loads((BASE/'out/VALIDATION.json').read_text())
assert validation['status']=='PASS'
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: A037 finite-tree entropy/KL nonreuse and physical common-lift proofs saved; 18,945 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A088/A094 review; compute parent/child witness channel/reset corrections on the activated bent-defect tree, keeping the erasure/terminal residual.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | A037 stage 1: Read protocol/board and packet interfaces; lead notes absent. Proved finite common-space entropy/KL ledgers, mismatch/reset corrections, and adaptive physical spectral lift with exact terminal erasure identification. Initial checker zero-division from retained zero-mass states repaired by filtering unreachable states. Frozen 81 rational cases + 256 three-bit Boolean lifts + 16 two-bit controls passed {validation["assertions"]} assertions in {validation["runtime_seconds"]:.3f}s. Saved source-complete claims and protocol deltas; review and universal influence payment remain open.\n')
(HOME/'LEARNED.md').write_text('''# Durable A037 facts

1. A finite common-space posterior tree releases sum p_h I(W;Y_h|A,h)=H(W|A)-E H(W|A,L). Terminal entropy remains; cut/subtree identities prevent replay credit. Keep side conditioning: W,L independent fair and A=W XOR L give I(W;L)=0 but I(W;L|A)=1.
2. Reference KL chain: K_h+j_h=d_h+E_P K_child. Shared kernels give j_h=0; mismatched kernels inject E_P D(kP||kQ). Reset reference correction is E_p log2(q_predicted/r_new), signed and indispensable.
3. Function-specific physical lift: k(y|S_0,h)=2^-|B| childhat(T)^2/q(T), T=S_0 intersect remaining-after-block. It preserves fair physical branches and actual child spectra. Its cumulative mixture information is I(S_0;L); its terminal root posterior is cumulative erased-label entropy plus expected terminal Fourier entropy.
4. Parent squared spectra alone cannot select named child spectra: f=[1,1,1,-1], g=[1,1,-1,1] have identical uniform squared spectra but bit-0=0 children constant versus bit-1 character. Retain phases and common-channel corrections.
5. Exact validation: Fraction probabilities and rational coefficients of log2(prime), 18,945 assertions. Remove zero-mass states before dividing by fiber probabilities. Finite checks support proofs but do not substitute for their all-tree quantifiers.
6. These identities do not prove FEI. The shortest remaining bridge is payment of the entire erasure/witness residual with compatible transported references, including reset/channel costs. Root normalization and distinct actual-run witness conditions stay explicit.
''',encoding='utf-8')
files=[p for p in BASE.rglob('*') if p.is_file() and p.name!='ARTIFACT_SHA256.json']
save('out/ARTIFACT_SHA256.json',{'created_at':stamp,'artifacts':[{'path':str(p.relative_to(BASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files]})
for p in files: assert p.stat().st_size<20_000_000
print(json.dumps({'status':'SAVED','claims':len(claims),'protocol_fields':'EXACT','assertions':validation['assertions'],'run':str(BASE),'artifacts':len(files)},indent=2))
