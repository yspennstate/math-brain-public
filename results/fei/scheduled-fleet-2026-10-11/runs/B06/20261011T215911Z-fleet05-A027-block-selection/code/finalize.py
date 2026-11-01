import json, hashlib
from datetime import datetime, timezone
from pathlib import Path

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('~/brain_workers/FEI100_20261011/context')
now=datetime.now(timezone.utc).isoformat()

def dump(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

sources=[]
def pin(path,scope):
    data=path.read_bytes()
    sources.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'read_scope':scope})

for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex'):
    pin(campaign/name,'Campaign instructions/index; A027 and B06 contract, G-R-SELECT and baseline scope prioritized')
for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'):
    pin(supp/name,'Supplement baseline, mandatory falsifiers and B06 crosswalk')
for name in ('BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','LOG_ALLOCATION_CURATED.md'):
    pin(supp/'sources'/name,'Complete mathematical source read; block identity sections 1-3; sparse marker and stopping obligation sections 4-5')
for stream,folder in [('B05','20261011T193057Z-fleet01-B05-rare-restrictions'),('B19','20261011T195038Z-fleet01-B19-independent-review')]:
    pin(campaign/'runs'/stream/folder/'REPORT.md','Original no-go construction and independent analytic reconstruction')
for name,scope in [
    ('threshold_paper_38pp.txt','Introduction, entropy preliminaries and Sections 8.2/8.4; Proposition 8.6, Proposition 8.9 and Corollary 8.10 used'),
    ('threshold_paper_29pp_earlier_version.txt','Introduction and convention comparison; not a proof dependency'),
    ('percolation_spectral_pivotal_entropy_30pp.txt','Introduction and Theorems 1.1-1.2; geometric hypotheses retained; not a proof dependency'),
    ('percolation_spectral_pivotal_entropy_31pp_other_version.txt','Introduction/version scope comparison; not a proof dependency')]:
    pin(context/name,scope)
pin(agent.parents[1]/'BOARD.md','Stage opening team scan; A021 control-first assignment avoided')
dump('SOURCE_READS.json',{'observed_at':now,'sources':sources,'missing_source':'~/brain_workers/FEI100_20261011/claude/B06/STREAM_NOTES.md','missing_source_action':'Followed explicit packet and STREAM_NEXT_ACTIONS; did not claim lead directions were available','read_limit':'Large context manuscripts were read at the stated sections, not independently audited cover to cover.'})

proofdeps=['C006@recovered-BLOCK_RESTRICTION_IDENTITY-sections-1-3','threshold-paper@context-38pp-Proposition-8.6']
statements=[
 ('A027-DATA-FIRST-PROPER-BLOCK', 'For every Boolean u on m>=1 uniform core bits, r>=1 fresh control bits, p=2^(-r), d=1-Eu, and F=1+A_r(u-1), the proper core block W satisfies B_W(F)<=p(2dm+2)<=6pm. I_W(F)=pI(u), expected terminal influence=rpd, and all leaves are constants or point defects satisfying H<=4I. For each fixed eta>0, I(u)>=eta*m implies H(F)<=max(6/eta+2/ln(2),4)*I(F) by a single-use physical stopping ledger.', ['Uniform normalized Boolean Fourier spectrum; entropy in bits','Explicit core/control activation representation','For the constant bound only: fixed eta>0 and I(u)>=eta*m']),
 ('A027-CORE-BLOCK-HARDNESS', 'For every Boolean core u with Eu>=0, delta=(1-Eu)/2, v=1-(Eu)^2, p=2^(-r), R0=1-4p*delta+4p^2*delta, and L the entropy of the nonempty conditional core spectrum, B_W(1+A_r(u-1))/p=v*L+4*delta*(1-p)*h2(delta)+(R0/p)*h2(p^2*v/R0). Continuous zero-mass conventions apply. A uniform core-block bound B_W<=K*p*I(u) for all such cores and r>=1 implies full FEI with constant K+2. Conversely FEI with constant C implies this block bound with constant C+5.', ['Uniform normalized Boolean Fourier spectrum; entropy in bits','Core mean nonnegative for the quantitative equivalence','Fresh point-indicator controls; W consists of all core coordinates but is proper in the full cube'])
]
claims=[]
for cid,statement,hypotheses in statements:
    claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A027'],'proof_source':str(run/'ADAPTIVE_BLOCK_SELECTION.tex'),'proof_dependencies':proofdeps,'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':None,'refutes':[],'first_unproved_line':None,'next_consumers':['A028','A029','A065','A087','A094','A097']})
dump('CLAIMS.json',claims)
validation=json.loads((run/'out'/'validation.json').read_text(encoding='utf-8'))
progress={
 'protocol_revision':'2026-10-11-execution-v2',
 'run_id':run.name,'stream':'B06','packet_id':'A027','gap_id':'G-R-SELECT','attempt_id':'A027-G-R-SELECT-001',
 'method':'Data-first physical core block; exact control-fiber entropy calculation; terminal point-defect certification; rarity-limit hardness guard',
 'mathematical_delta':'B_W<=p(2dm+2) for arbitrary activations; density-controlled proper-block stopping theorem covers coded parity plateaux and the B05 bent-marker family. Exact B_W/p formula proves the density-free full-core rule is FEI-equivalent in finiteness, with explicit K+2/C+5 bridges.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING',
 'mathematical_status':'PROVED_RESTRICTED_SELECTION_AND_SCOPE_BRIDGE; UNIVERSAL_G-R-SELECT_OPEN; FULL_FEI_OPEN',
 'claim_versions_used':proofdeps,
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['ADAPTIVE_BLOCK_SELECTION.tex','BLOCK_CONTROLS.md','SOURCE_READS.json','SEARCH_SPEC.json','VALIDATION_EXTENSION.json','code/check.py','out/validation.json'],
 'next_consumers':['A028','A029','A065','A087','A094','A097'],
 'next_action':'Derive the activation transport identity for a proper SUBSET of low-density core coordinates, retaining the remaining-core Fourier fibers; isolate the shifted empty-core row payment instead of demanding a universal full-core bound.',
 'stagnant_substantive_attempts':0,
 'blockers':['B06 STREAM_NOTES.md absent at supplied path','Independent review and supervisor mirror adoption not yet observed','Universal selection remains unpaid; I(u)/m can tend to zero'],
 'packet_ids':['A027']
}
dump('PROGRESS.json',progress)
dump('PACKET_DELTA.json',progress)

report=f'''# A027 — Data-first proper-block selection

Full FEI remains OPEN. Two local proof-complete claims are saved for independent review; no independent acceptance or novelty clearance is claimed.

## exact target, quantifiers, hypotheses and units

All cubes are uniform, outputs are Boolean signs, Fourier coefficients are normalized, and H is in bits. For every m,r>=1 and Boolean core u, put p=2^(-r), d=1-Eu and F=1+A_r(u-1). The frozen rule queries all m physical core coordinates, leaving the r fresh activation controls unqueried, and stops at the resulting leaves. This is a proper block of the full cube, with no spectral-sample-dependent choice. The structural class for a dimension-independent payment is I(u)>=eta*m for fixed eta>0. No core FEI bound is assumed.

The proved conditional payment is B_W<=p(2dm+2)<=6pm, hence B_W<=(6/eta)I_W on this class. The channel contribution is paid using M_W<=(2/ln2)I_W. Every terminal function is constant or a point defect with H<=4I. Thus the complete constant is max(6/eta+2/ln2,4), uniformly in m, r and core bias. Artifact resolution and this restricted theorem do not resolve universal G-R-SELECT.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full. The campaign README/status, claim and obstruction indices, packet matrix and plan were consulted, with the exact A027 contract and G-R-SELECT prioritized. BOARD.md was read at the stage opening. The B06 lead file was absent; no direction from it is invented. A021's control-first work was avoided by choosing a data-first rule.

Supplement CLAIMS C005/C006/C018/C019 and COUNTEREXAMPLES X001/X003/X009/X011 supplied the baseline and scope guards. BLOCK_RESTRICTION_IDENTITY sections 1-3 supplies the exact block identity and log-Sobolev channel bound; LOG_ALLOCATION sections 4-5 and the original B05/B19 reports supply the marker no-go, which is retained. The 38-page threshold paper Proposition 8.6 and Section 8.4 (Proposition 8.9, Corollary 8.10) were read at their actual scope. Earlier threshold and both percolation versions were consulted for their introductions/conventions; their geometric or composition theorems are not silently imported. SOURCE_READS.json records local observed SHA256 pins and exact read scopes. This stage does not claim a cover-to-cover independent audit of either large manuscript. No external literature novelty claim is made.

## complete derivation or exact first unsupported line

ADAPTIVE_BLOCK_SELECTION.tex contains complete proofs. For nonempty control Fourier sets the core fiber is the normalized squared spectrum of u-1, with mass 2p^2d. The empty control fiber has mass R0=1-2pd+2p^2d and nonempty-core mass q=p^2*(1-(Eu)^2). Its exceptional binary-entropy charge is bounded explicitly by 2p, including an exact rational verification of the elementary constants. Summing all fibers gives the conditional entropy bound without dropping any row.

Physical edge counting gives I_W=pI(u) and reserved terminal influence rpd. Each negative core assignment has probability d/2 and gives the point defect D_r, with influence 2rp. Its exact spectrum proves H(D_r)<=4I(D_r); no ancestral influence is reused.

An additional exact identity is B_W/p=vL+4delta(1-p)h2(delta)+(R0/p)h2(p^2v/R0), where delta=(1-Eu)/2, v=4delta(1-delta), and L is the conditional nonempty-core spectral entropy. In the fixed-core p->0 limit this retains H(u)-h2(v)+4delta*h2(delta). A universal bound on this full-core proper-block rule implies FEI with constant K+2; FEI implies that block bound with constant C+5. The proof includes the elementary edge-isoperimetric induction used to control h2(v), so this scope bridge does not rest on an unproved inequality.

The first unsupported line for UNIVERSAL selection is replacing m<=I(u)/eta, or paying the corresponding normalized defect-spectrum entropy for arbitrary low-density cores. Simply removing that hypothesis from the same full-core rule is FEI-equivalent and is not claimed as progress toward an easier endpoint.

## executed validation with domain, arithmetic, commands and outputs

The pre-search frozen specification is SEARCH_SPEC.json: every core truth table for m=1,2,3, with r=1,2,3; 828 activation cases, no symmetry reduction, no randomness, under 50 MB estimated RAM and a 60-second cap. VALIDATION_EXTENSION.json freezes the later transport-identity checks on the same domain. The fixed k=2,4,6 coded-plateau/bent fixtures are deterministic validations, not a search escalation.

Command: `python -X utf8 runs\\{run.name}\\code\\check.py` from the A027 folder. Final execution passed {validation['assertions']:,} assertions in {validation['elapsed_seconds']:.3f} seconds. Full integer Walsh spectra are compared to independently counted physical influences, actual leaf channel laws and exact fiber formulas. Entropy signs use Fraction enclosures from 22-term rational atanh series, with a proved geometric remainder and sign-correct division by the enclosure for ln2. The decisive conditional bound and terminal bounds are certified on every case. Exact identity checks use overlapping independently bounded entropy expressions; those checks are consistency validation, while the analytic proof establishes exact equality. Output is out/validation.json. No independent reviewer or Lean check is claimed.

## proof dependencies and changed downstream conclusions

The positive proof depends on the recovered exact block identity/channel payment and elementary entropy/Parseval facts. Original B05/B19 no-go is used only as a stress-family comparison, not as a premise of the positive theorem. Threshold activation formulas are baseline calibration; the new output is a block-specific conditional charge and stopping ledger, not a claim to have rediscovered the already known full-activation FEI equivalence.

For the quadratic parity-lift coded core on k+1 bits, H=k, aggregate singleton erasure=0, and I=(k+1)/2. The data-first block has B_W<=12I_W and complete constant 12+2/ln2 for every rarity. For the B05 bent-marker core on k+1 bits, I=k/2+(k+1)2^(-k)>=m/3, yielding B_W<=18I_W and complete constant 18+2/ln2. The bad marker singleton still has logarithmically unbounded erasure/influence ratio. BLOCK_CONTROLS.md gives the all-parameter calculations and distinguishes the substantial core block budget from the bad marker's tiny budget.

This can be consumed by A028/A029/A065/A097 as a concrete proper-block example and by A087/A094 for reconstruction. It does not certify arbitrary parity lifts, hidden arbitrary low-influence tensor cores or general selector trees.

## one next mathematical action and independent reviewer

Derive activation transport for a proper subset of low-density CORE coordinates, retaining the remaining-core Fourier fibers, and identify the shifted empty-core row payment. This changes the selection mechanism instead of repeating the now quantified full-core FEI-strength endpoint. A087 is the nominated independent reviewer; A094 is the alternate. Neither has reviewed this run yet. No messages are sent to them; the saved handoff names the consumers for supervisor copying.

## actual persistence receipts or precise save blocker

All required protocol files, both packet deliverables, frozen specs, proof, source pins, code and exact outputs are saved under this run directory inside A027. STATUS.md has exactly two lines, and WORKLOG.md and LEARNED.md are updated locally. out/PERSISTENCE_RECEIPT.json gives observed file hashes and byte sizes; code/finalize.py checks protocol claim/progress key equality and compatibility-copy equality. No source tree, shared registry or another worker folder was modified. GitHub/Brain copy and independent review are pending the supervisor; local persistence is not reported as mirror verification.

## Universal bridge

This stage moves C019 stopping-tree payment and G-R-SELECT by proving a complete, nonreusing proper-block ledger on an unbounded rare-activation class, including the B05 obstruction and a coded erasure plateau. It also pins the remaining universal payment to an exact defect-spectrum limit, with K+2/C+5 implications, rather than presenting the full-core choice as a universal reduction. What remains is a physically selectable smaller core block or a stopping tree that pays low-density core fibers and all leaves without assuming FEI for them. NEXT targets that exact unpaid row and residual core; it is the shortest continuation of the universal selection route because the current full-core rule's density-free extension is already FEI-strength, so further isolated dense-core classes would not remove the gap.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A027 local proper-block theorem and exact FEI-strength guard complete; 828 cases / 44,782 exact assertions passed; independent review pending; full FEI OPEN.\nNEXT: Derive transport for a proper subset of low-density core bits; retain the shifted empty-core row and terminal costs; A087/A094 review the saved proof.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — {run.name}: Read protocol, board and source-bound baseline; B06 lead file absent. Selected data-first activation block to avoid duplicating A021 control-first work. Proved B_W<=p(2dm+2), terminal point-defect payment and density-controlled proper selection. Derived exact B_W/p cost and universal full-core K+2/C+5 hardness bridge. Frozen 828-case pilot and subsequent same-domain transport validation passed 44,782 exact assertions; 1.355s final mathematical runtime. Two local claims saved for A087/A094; full FEI and low-density core selection remain open. No shared writes or external messages.\n')
(agent/'LEARNED.md').write_text('''# A027 durable mathematical facts

For F=1+A_r(u-1), p=2^-r, m core bits, d=1-Eu, querying the complete CORE is a proper full-function block when r>=1. Nonempty control Fourier fibers have mass 2p^2d and normalized spectrum of u-1. The empty-control fiber has mass R0=1-2pd+2p^2d and nonempty-core mass p^2v. Keeping its exceptional entropy gives B_W<=p(2dm+2)<=6pm.

I_W=pI(u); leaf influence is exactly rpd. Leaves are constants or r-bit point defects with H<=4I. Fixed I(u)>=eta*m therefore gives a complete stopping constant max(6/eta+2/ln2,4). This is a local proof-complete theorem pending independent review, not universal FEI.

For delta=(1-Eu)/2 and conditional nonempty-core entropy L, the exact identity is B_W/p=vL+4delta(1-p)h2(delta)+(R0/p)h2(p^2v/R0). For Eu>=0, a universal block bound KpI(u) implies full FEI with K+2; FEI C implies this block bound C+5. The full-core rule cannot be extended by silently dropping density: the unpaid normalized defect-spectrum entropy has full-FEI strength.

Quadratic bent parity-lift core: dimension k+1, H=k, zero singleton erasure, I=(k+1)/2; rare activation data-first constant 12+2/ln2. Bent-marker splice core: I=k/2+(k+1)2^-k >=(k+1)/3; its activation includes the B05 no-go and has data-first constant 18+2/ln2. The bad marker singleton remains logarithmically expensive; nonlocal block influence supplies a different budget.

Validation: all 828 actual activations for m=1,2,3 and r=1,2,3; final 44,782 assertions with integer Walsh/Fraction spectra, independent physical edge counts, rational atanh log enclosures, plus fixed k=2,4,6 code fixtures. Finite tests validate the proof formulas, not a universal extension. Independent review and mirror adoption were not observed.

Next mechanism: select a proper subset inside low-density cores and retain remaining-core fibers and the shifted empty-core row. A parity-coded spectrum or zero aggregate erasure is not a terminal certificate. Core density is not restriction hereditary.
''',encoding='utf-8')

protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claimkeys=set(protocol['required_per_run']['claim_fields'])
progresskeys={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==claimkeys for c in claims)
assert set(progress)==progresskeys
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
files=[]
for path in sorted(run.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPT.json':
        data=path.read_bytes()
        assert len(data)<20*1024*1024
        files.append({'path':str(path.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
for path in (agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md'):
    data=path.read_bytes()
    files.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
dump('out/PERSISTENCE_RECEIPT.json',{'observed_at':now,'local_save':'VERIFIED','protocol_schema':'PASS','compatibility_copy':'IDENTICAL','files':files,'independent_review':'PENDING','supervisor_mirror':'NOT_OBSERVED'})
print(json.dumps({'saved_files':len(files),'claims':len(claims),'protocol_schema':'PASS','compatibility_copy':'IDENTICAL','full_fei':'OPEN'},indent=2))
