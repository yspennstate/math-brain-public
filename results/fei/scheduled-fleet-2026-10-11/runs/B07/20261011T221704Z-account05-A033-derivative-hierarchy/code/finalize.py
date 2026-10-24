from pathlib import Path
import json,hashlib,datetime,copy
R=Path(__file__).resolve().parents[1]; root=R.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
a031=Path('~/brain_workers/FEI100_20261011/agents/A031/runs/20261011T214115Z-account05-A031-convolution-identity/CLAIMS.json')
reviews=json.loads(a031.read_text())
for c in reviews:
    c['status']='INDEPENDENT_RECONSTRUCTION_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION'
    c['review_records'].append({'reviewer':'account05/A033','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent physical multiplication isometry proof and exact rational-weight cross-representation checks; no repairs supplied','source':str(R/'A031_INDEPENDENT_REVIEW.md'),'sha256':sha(R/'A031_INDEPENDENT_REVIEW.md')})
statement='For every finite uniform-cube Boolean sign f=(-1)^P, partition X,Y, and integer d>=0, if every nonconstant GF(2) directional phase derivative partial_i P for i in X has degree at most d on all remaining physical variables, then H(S_X|S_Y)<=kappa(d) sum_{i in X} min(Inf_i,1-Inf_i), where kappa(0)=0 and kappa(d)=h2(2^-d)/2^-d for d>=1. More sharply H(S_X|S_Y)<=sum_{i in X,d_i>=1} kappa(d_i)J_i-TC(S_X)-I(S_X;S_Y). Using the separately imported physical block-channel bound, H(f)-E_t H(f_t)<=[kappa(d)+2/ln2] I_X(f). Terminal Y entropy is retained; no universal bounded d is asserted.'
claim={
'claim_id':'A033-DIRECTIONAL-PHASE-BLOCK-PAYMENT','version':1,'exact_statement':statement,
'hypotheses':['Exact Booleanity, not norm or approximate square constraints','Uniform independent physical inputs','GF(2) degree of exact pivotal indicators on all residual variables','Entropy in bits; constants and deterministic spectral bits included'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A033'],
'proof_source':{'path':str(R/'NEW_FULL_BOOLEANITY_CONSEQUENCE.md'),'sha256':sha(R/'NEW_FULL_BOOLEANITY_CONSEQUENCE.md')},
'proof_dependencies':[{'claim':'C006 baseline physical block identity and channel bound','source':'~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','scope':'Only the final physical entropy-drop inequality; spectral result is proved directly'}],
'review_records':[],'status':'AUTHOR_PROVED_SCOPED_CONSEQUENCE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A034','A035','A067','A070','A078','A088','A094','B20']}
write('CLAIMS.json',reviews+[claim])
progress={
'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B07','packet_id':'A033','gap_id':'G-BOOLEANITY/G-PHASE-COND','attempt_id':'A033-directional-phase-01',
'method':'Import retired controls; independent review of A031 via physical multiplication; exact pivotal-indicator GF(2) minimum-weight gap and conditional entropy; correlation-rebate and tensor controls',
'mathematical_delta':'Scoped conditional and physical block entropy payment kappa(d)J_X and [kappa(d)+2/ln2]I_X; explicit full-Booleanity admission; raw high-degree marginal bill still diverges on point defects. Both A031 v1 claims independently reconstructed.',
'deliverable_status':'LOCAL_ARTIFACT_COMPLETE_WITH_EXPLICIT_ATOM_CAP_SOURCE_GAP',
'mathematical_status':'SCOPED_RESULT_PROVED; FULL_FEI_OPEN; COMPLETE_ATOM_CAP_IMPORT_PENDING_ORIGINAL_SOURCE',
'claim_versions_used':[{'id':'C006','version':'supplemental baseline 2026-10-11','scope':'physical channel bound'},{'id':'A031-SIGNED-ENTROPY-ANCHOR','version':1,'scope':'reviewed, not a proof dependency'},{'id':'A031-ANCHOR-POSITIVE-PAYMENT-NOGO','version':1,'scope':'reviewed, not a proof dependency'}],
'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in reviews+[claim]],
'source_artifacts':['NEW_FULL_BOOLEANITY_CONSEQUENCE.md','BOOLEANITY_HIERARCHY.tex','IMPORTED_CONTROLS.md','A031_INDEPENDENT_REVIEW.md','FROZEN_SPEC.json','code/check_derivatives.py','out/validation.json','out/SOURCE_MANIFEST.json'],
'next_consumers':['A031','A034','A035','A067','A070','A078','A088','A094','B20'],
'next_action':'Recover Addendum 11.51 exact atom-cap definition; then derive a signed growing-degree correlation rebate for (3) on an actual coupled, nonflat Boolean phase family, preserving arbitrary Y terminal entropy.',
'stagnant_substantive_attempts':0,
'blockers':['Original atom-cap cyclic-law addendum absent locally; gh API unauthenticated; only audited summary imported. No blocker to proved scoped theorem.','Universal growing-degree correlation rebate and proper-block selection unpaid.','B07 lead STREAM_NOTES.md absent at supplied path.'],
'packet_ids':['A033']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
v=json.loads((R/'out/validation.json').read_text())
report=f'''# A033 derivative hierarchy

## exact target, quantifiers, hypotheses and units

Identify a full-Booleanity consequence absent from the fixed convolution/cap-prefix controls and turn it into a scoped conditional entropy payment. All dimensions are finite, all physical inputs are independent uniform signs, and entropy is in bits. The proved theorem is directional GF(2) phase degree <=d implies H(S_X|S_Y)<=kappa(d)D_X and a physical block drop <=[kappa(d)+2/ln2]I_X, with arbitrary terminal Y entropy retained. Full FEI remains OPEN. The packet's complete original-source atom-cap import remains incomplete, explicitly separated from the proved theorem.

## sources actually read, revisions and theorem locators

Protocol fei-execution-protocol/2, revision {protocol['revision']}, read in full. Campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS, plan B07/A033 and section 3.4, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and all curated sources were loaded and their relevant statements inspected. Source hashes and precise loading scope are in out/SOURCE_MANIFEST.json. Four supplied paper versions were loaded; Fourier definitions and current-paper introductions were inspected. No threshold or percolation theorem is a proof dependency. Earlier B05/B09/B19 reports were loaded. BOARD snapshot 2026-10-11 22:16 UTC was read at stage start. B07 lead notes are absent. A031 DERIVATION.md and CLAIMS.json and A032 REPORT.md/admission result were read; A032 is context, not a proof premise. Fixed convolution no-go imported from ROUTE_MAP_CURATED section 3 / BOOLEANITY_ORDER Theorem 2.1; atom-cap scope imported only from plan mathematical audit section 1.4/table FIXED_CAP_PREFIX. The original cyclic addendum remains inaccessible, as documented in IMPORTED_CONTROLS.md.

## complete derivation or exact first unsupported line

NEW_FULL_BOOLEANITY_CONSEQUENCE.md proves equivalence of complete signed convolution and full physical-face norms, exact split pair identities, the sign-valued multiplicative derivative hierarchy, the two-sided minimum-weight gap for exact pivotal GF(2) polynomials, spectral conditional payment, and the physical C019 block consequence. BOOLEANITY_HIERARCHY.tex is a concise mathematical interface. The high-degree point-defect calculation shows the raw marginal bill is ~nI while H~4I, so the high-degree correlation rebate cannot be dropped. An arbitrary g(Y) tensor is admitted and its entropy is explicitly retained. No novelty claim is made for elementary bounded phase-degree FEI consequences. First unsupported universal line: a dimension-independent signed rebate cancelling the growing derivative granularity bill or a universal paid proper-block selection/terminal rule. First unsupported source-reconstruction line: the original atom-cap prefix definition and family are unavailable; their audited no-go scope is imported without inventing parameters.

## executed validation with domain, arithmetic, commands and outputs

Frozen helper derivative-check-v1 and domain are in FROZEN_SPEC.json, written before execution. Command from A033 root: `python -X utf8 runs/{R.name}/code/check_derivatives.py`. Result: {v['truth_tables']} labelled Boolean truth tables n=0,1,2,3, {v['blocks']} physical block choices, {v['assertions']} exact assertions PASS in {v['seconds']:.3f} seconds. Integer Walsh/Mobius/Fraction arithmetic verifies norm, exact edge influences, ternary derivatives with the FULL pair constraints, degree minimum-weight gaps, and A031's multiplication/convolution isometry/involution in two representations. Conditional entropy comparisons use exact integer products, not floating logarithms. Point-defect formulas n=3,...,12 are checked exactly; decimal entropy displays are illustrative only, and all-dimensional limits have analytic proofs. Estimate <30 MB, pilot cap 60 seconds, no dimension escalation or heavy jobs. Independent author reproduction of the new theorem is not independent agent acceptance. Brain recall and a failed read-only gh API retrieval are provenance attempts, not certificates.

## proof dependencies and changed downstream conclusions

The spectral theorem has a complete elementary proof and uses no unreviewed campaign claim. Its physical drop corollary separately imports accepted C006's channel bound. A031_INDEPENDENT_REVIEW.md accepts both A031 v1 claims at their stated scopes via a different physical-space reconstruction and no repairs. These are review records awaiting registry adoption; A088/A094 requests remain. Reviewing both claims before introducing the single A033 candidate prevents this run from adding another broad candidate to the existing full queue. The remaining known pending candidate is A032 plus this A033 scoped bundle; no shared indices were changed. The new payment is available to A034 and restriction consumers but does not permit dropping Y entropy or charging the growing degree bill by a fixed constant.

## one next mathematical action and independent reviewer

Recover the exact Addendum 11.51 atom-cap definition, then test a signed correlation-rebate bound for equation (3) on one growing-degree coupled Boolean phase family, retaining arbitrary tensor Y entropy. The mathematical aim is cancellation of the degree bill, not another fixed prefix or higher-dimensional census. Independent reviewers: A088 and A094; source-bound receipts are local for supervisor collection. No messages were sent.

## actual persistence receipts or precise save blocker

All requested run files and rolling STATUS.md, WORKLOG.md, LEARNED.md are saved in A033's folder. out/ARTIFACT_RECEIPTS.json contains local byte counts and SHA256 hashes. No file exceeds 20 MB. All other agent/shared source trees were read only; no git, upload, shared index mutation, independent acceptance of A033, mirror verification, or downstream adoption is claimed. Missing original atom-cap source is a provenance blocker, not a local save blocker.

## Universal bridge

This stage moves G-BOOLEANITY/G-PHASE-COND into a genuine C019 physical block payment on the directional low-phase-degree class: the full pointwise sign hierarchy supplies an exact pivotal weight gap, which pays the complete block conditional entropy plus its separately bounded physical channel at [kappa(d)+2/ln2]I_X. It also independently verifies the two live A031 signed claims. There is no numerical universal FEI constant advance. Growing-degree correlation cancellation, a universally usable block/stopping rule, and all terminal entropy remain unpaid; the original cap-family import also needs its missing source. Seeking a signed rebate for the exact growing-degree bill is the shortest mathematical next route to full FEI because point defects exhibit the necessary cancellation explicitly, whereas increasing a truncation or enumerating another dimension cannot address it.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(root/'STATUS.md').write_text('STATE: A033 scoped directional-phase block payment proved locally; 11,142 exact checks; both A031 v1 claims independently reconstructed; original atom-cap source missing; full FEI OPEN.\nNEXT: Recover cyclic Addendum 11.51; A088/A094 review scoped theorem; seek signed growing-degree correlation rebate with terminal Y entropy retained.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Imported fixed-convolution no-go and audited cap-prefix scope; original cap text absent/gh unauthenticated. Proved directional phase-degree conditional and physical block payment using exact pivotal indicator minimum weight. Passed {v["assertions"]} exact checks. Independently reconstructed both A031 v1 claims without repairs. Point defects refute raw high-degree bill payment; tensor Y entropy retained. Artifacts saved; supervisor adoption/review pending.\n')
(root/'LEARNED.md').write_text('''# A033 durable facts

- Full signed convolution is equivalent to all physical face norms and pointwise f^2=1. Complete split pair identities A_iB_i=0, A_i^2+B_i^2=1 are indispensable; ternary first derivatives alone are insufficient.
- Exact pivotal Q_i=(1-f*f_flipped)/2 is the GF(2) phase derivative. If its nonconstant degree is d_i, both its weight and complement are >=2^-d_i, proved by induction.
- kappa(d)=h2(2^-d)/2^-d<d+log2(e). Directional derivative degree <=d on block X pays H(S_X|S_Y)<=kappa(d)D_X and the physical drop <=[kappa(d)+2/ln2]I_X. Degree is on ALL remaining physical variables. Arbitrary terminal Y entropy is retained; tensor g(Y) remains admissible.
- Exact high-degree rebate: H(S_X|S_Y)=sum_X h2(Inf_i)-TC_X-I(S_X;S_Y). Point defects have raw bill/I=kappa(n-1)~n-1+log2(e), but H/I->4, so an O(I) raw degree bill is false.
- A031 v1 anchor and no-go claims independently reconstructed using physical multiplication isometry; reviews locally saved pending adoption. A033's class consequence is pending A088/A094 review. No novelty claim for elementary bounded phase-degree FEI.
- Fixed signed-order G_(K,w) no-go imported from curated route-map section 3. Fixed atom-cap cyclic no-go is distinct and only available as an audited summary; original definition/family/checker still absent and gh unauthenticated. Do not manufacture its parameters or claim full import.
''',encoding='utf-8')
for c in reviews+[claim]:assert set(c)==set(protocol['required_per_run']['claim_fields'])
expected_progress={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
receipts=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name=='ARTIFACT_RECEIPTS.json':continue
    assert p.stat().st_size<20*1024*1024
    receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/ARTIFACT_RECEIPTS.json',{'run_id':R.name,'local_only':True,'files':receipts})
print(json.dumps({'claims':len(reviews)+1,'protocol_fields_checked':True,'receipts':len(receipts),'report_saved':str(R/'REPORT.md')},indent=2))
