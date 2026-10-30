"""Write exact-schema stage artifacts and verify their landed bytes."""
from pathlib import Path
from datetime import datetime, timezone
import copy,hashlib,json

RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];TEAM=AGENT.parents[1]
BASE=Path(r'~\mop_fei100')
P=BASE/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
SOURCE=TEAM/'agents/A015/runs/20261026T235636Z-fleet04-A015-minterm-barrier-analysis'
NOW=datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,o):
    p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    assert load(p)==o
protocol=load(P);main=load(RUN/'out/checks.json');pilot=load(RUN/'out/pilot.json');roots=load(RUN/'out/root_checks.json');lean=load(RUN/'out/lean.json')
assert main['verdict']==roots['verdict']==pilot['verdict']=='PASS'
assert main['cores']==23 and main['lifts']==115 and main['scalar_pairs']==1088
assert main['helper_sha256']==pilot['helper_sha256']==sha((RUN/'code/check.py').read_bytes())
assert roots['helper_sha256']==sha((RUN/'code/root_check.py').read_bytes())
assert roots['base_helper_sha256']==main['helper_sha256']
assert main['elapsed_seconds']<55 and pilot['elapsed_seconds']<55
total=main['checks']+roots['checks']

review=copy.deepcopy(next(c for c in load(SOURCE/'CLAIMS.json') if c['claim_id']=='A015-POSITIVE-ANCHOR-MONOTONE-UNIVERSALITY'))
textbytes=review['exact_statement'].encode('utf-8')
canon=json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')
assert review['statement_sha256'] in (sha(textbytes),sha(canon))
review['proof_source']=[str(SOURCE/p) for p in review['proof_source']]+['REVIEW_A015.md','code/check.py','out/checks.json']
review['review_records'].append({'reviewer':'A007','verdict':'HOLDS_FULL_STATED_SCOPE','role':'Independent physical/Fourier/entropy reconstruction, no substantive repair','reviewed_at':NOW,'evidence':['REVIEW_A015.md','out/checks.json']})
review['status']='INDEPENDENTLY_REVIEWED_A007_FULL_STATED_SCOPE'
statement=('For every nonconstant monotone Boolean sign core g on s>=1 uniform bits and 0<delta<=1, choose h=g or h(z)=-g(-z) with false density q<=1/2, fix ANY finite positive CNF for h with nonempty anchors, and repeat each anchor with L=2s+2ceil(log2(16/delta)) distinct positive private bits to obtain A015 F_L. Every fixed subprobability nonempty reference R covering F_L and satisfying complete C(F_L;R)<=K I(F_L), K>=0, induces a normalized nonempty core reference r with C_g(r)<=(1+delta)K I(g). Specifically epsilon=2^-L, rho=2^s qepsilon<1, a=(1-rho)^2, u_S=Fhat_L(S,empty)^2>=a p_S for p_S=ghat(S)^2, E=all nonempty core sets, Z=sum_E R, D=sum_E u log2(1/R), and B=sum_E(u-ap)log2(1/R)>=0 give the EXACT C_g(r)=(D-B)/a+Var(g)log2 Z. For ANY raw successful reference Q with total mass<=theta=Pr(initial roots nonempty)>0 and R=Q/theta, the TWO normalizers cancel exactly: C_g(r)=(D_Q-B_Q)/a+Var(g)log2 Q_E, Q_E=sum_E Q>0. This retains rare-sector surprisal and surplus for all 0<Q_E<=theta<=1. It refunds one nested conditioning event, not repeated-root/label/attachment costs. No common amplitude scaling, universal source, free adaptive reset, empty/nonempty wrapper absorption or full FEI solution is asserted.')
hypotheses=['Finite uniform physical cubes, sign Boolean targets and bit-valued entropy; monotone positive anchors, distinct fresh private bits; g nonconstant.',
'All representation, orientation and reference choices fixed before the Fourier target; reference mass<=1 with complete output coverage.',
'The paid complete source C(F_L;R)<=K I(F_L) is a hypothesis; every original decoding cost is included in R.',
'For raw-source cancellation Q is the SAME generator with total successful nonempty output mass<=theta; no actual queue supplier is constructed.',
'Core-only denominator a>0 follows from the stated finite L; domination and reference mass are used before discarding B.']
claim={'claim_id':'A007-POSITIVE-CORE-DOMINATED-FINITE-EXTRACTION','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A007'],
'proof_source':['DOMINATED_EXTRACTION.md','FROZEN_SPEC.json','ROOT_SPEC.json','code/check.py','code/root_check.py','out/checks.json','out/root_checks.json'],
'proof_dependencies':[{'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256'],'acceptance':'Independent A007 reconstruction in REVIEW_A015.md'},'Direct finite cross-entropy algebra, Boolean nonzero coefficient granularity, monotone duality, Poincare, explicit scalar bounds proved in DOMINATED_EXTRACTION.md'],
'review_records':[{'reviewer':'A007','role':'Author analytic proof and exact finite checks; not independent acceptance','verdict':'PASS','evidence':['out/checks.json','out/root_checks.json']}],
'status':'AUTHOR_PROOF_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A008','A015','A086','A094','B02','B03','B20']}
claims=[review,claim]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
write(RUN/'CLAIMS.json',claims)

progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B02','packet_id':'A007','gap_id':'G-J-COST','attempt_id':'A007-stage22-positive-dominated-extraction',
'method':'Independent positive-anchor theorem review; finite Boolean coefficient domination and complete signed surplus/root-normalization accounting.',
'mathematical_delta':'A015 positive-core universality independently HOLDS. Its previously open finite arbitrary-reference transfer is supplied at(1+delta) using L=2s+2ceil(log2(16/delta)); original root and core-sector normalizers cancel exactly with surplus. Universal ORIGINAL influence-paid source remains unpaid.',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_EXACT_CHECKS; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256']}],
'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':1,'change':'Independent A007 HOLDS review, no source mutation'},{'claim_id':claim['claim_id'],'version':1,'change':'New finite conditional extraction theorem'}],
'source_artifacts':['DOMINATED_EXTRACTION.md','REVIEW_A015.md','FROZEN_SPEC.json','ROOT_SPEC.json','FORMAL_SPEC.json','out/checks.json','out/root_checks.json','out/lean.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':claim['next_consumers'],'next_action':'A008/A015/A086/A094 audit positive finite extraction, especially granularity/duality and signed surplus. Then supply ORIGINAL arbitrary-core full source, retaining actual labels/fusion/attachments and root normalization, paid by SAME unused physical influence. Do not reopen finite extraction or positivity as presumed compression.',
'stagnant_substantive_attempts':0,'blockers':['Universal original influence-paid source unresolved','New conditional extraction requires independent review','Lean RUNTIME_UNVERIFIED: compute-state access denied; no kernel or axioms certificate','Supervisor mirror/adoption not observed','Initial checklist working update returned lock-held-too-long; no lock removed'],'packet_ids':['A007']}
fields={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)

sources=[P,Path(r'~\AGENTS.md'),TEAM/'BOARD.md',TEAM/'claude/B02/STREAM_NOTES.md',SOURCE/'POSITIVE_CORE.md',SOURCE/'REPORT.md',SOURCE/'CLAIMS.json',SOURCE/'code/persist.py',AGENT/'runs/20261023T140735Z-fleet03-A007-root-normalization/REPORT.md',TEAM/'agents/A008/runs/20261023T144206Z-fleet03-A008-gate-label-compression/PROOF_AND_REVIEW.md']
for name in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:sources.append(P.parent/name)
supp=BASE/'research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:sources.append(supp/name)
sources+=list((TEAM/'context').glob('*.txt'))
write(RUN/'out/SOURCE_RECEIPTS.json',{'observed_at':NOW,'scope':'Byte pins, not assertions of complete rereading. Full mathematical sources A015 positive proof and A008 extraction read; campaign context selected passages and earlier-stage reads inherited. Board pin is final observation.','sources':[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sources]})

report=f'''# A007: finite positive-core extraction and nested root refund

## exact target, quantifiers, hypotheses and units

Every nonconstant monotone sign core g on s>=1 uniform bits, every0<delta<=1, every fixed finite positive CNF of its monotone dual h with false density q<=1/2, and ANY supplied complete nonempty subprobability reference R for its L=2s+2ceil(log2(16/delta)) private lift: prove C(F_L;R)<=K I(F_L) implies C_g(r)<=(1+delta)K I(g). Retain both original-root and core-sector conditioning and the nonnegative spectral surplus. Costs in bits; physical uniform-cube influence. Independently review A015 positive universality@1. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD (2026-10-27 06:38UTC), B02 STREAM_NOTES v2, own STATUS/LEARNED and previous signed-embedding report; A015 POSITIVE_CORE.md and whole exact claim, its REPORT and relevant persist hash recipe; A008 PROOF_AND_REVIEW.md. Protocol revision{protocol['revision']} read in full. Campaign README/CURRENT_STATUS, registries, plan endpoint J and A007 acceptance contract, supplemental campaign/claims/counterexamples/seed/mapping passages and source inventory were checked; earlier full baseline reads are inherited, not claimed repeated. Four paper text versions were searched at relevant theorem/root/normalization locators; none is a premise of the new proof. One math-recall call supplied leads, including A008's fixed-pair obstruction and finite signed extraction; no provisional memory statement is used as proof. out/SOURCE_RECEIPTS.json pins bytes and limits the read claims. No web-priority assertion or new literature import.

## complete derivation or exact first unsupported line

DOMINATED_EXTRACTION.md gives the complete proof. For p=ghat^2 and u=Fhat_core^2, Boolean coefficient granularity and |Fhat_core-ghat|<=2qepsilon give u>=a p, a=(1-2^s qepsilon)^2>0. With E=all nonempty core sets, Z=sum_E R, D=sum_E u log2(1/R), and B=sum_E(u-ap)log2(1/R)>=0, the EXACT identity is C_g(r)=(D-B)/a+Var(g)log2 Z. The extra B handles unequal scaling; AND2 rules out the old common-scaling shortcut.

For the SAME raw successful output law Q and theta=Pr(initial roots nonempty), R=Q/theta, the EXACT identity becomes C_g(r)=(D_Q-B_Q)/a+Var(g)log2 Q_E. Original-root and core-sector normalizers cancel by substitution, not by dropping a negative term. Rare-sector scaling is tested uniformly and analytically for all positive masses, not merely at the finite test exponents. These are output-law identities conditional on a supplied source, not a realization claim for a new queue. They refund one nested conditioning event and do not erase repeated-root, label or attachment costs.

Monotone duality preserves every squared coefficient and influence, allowing q<=1/2 and2q<=I(g). A015 gives I(F_L)<=I(g)+(2q)(s+L)epsilon. The explicit finite L ensures rho<=delta/1024 and d0=(s+L)epsilon<delta/16, hence (1+d0)/(1-rho)^2<=1+delta. This supplies the finite arbitrary-reference reduction left open in A015, with O(s+log(1/delta)) multiplicity, not an optimality claim or an improvement over A008's distinct signed-point scaling.

REVIEW_A015.md reconstructs the FULL unchanged positive-anchor theorem: physical nesting, both influence formulas, signed spectrum, growing-private entropy tail, finite entropy error, prime/irredundant clauses and monotone-supremum equality. Verdict HOLDS, without repair. A007's new strengthening remains author proof pending independent acceptance. First unsupported universal line: an ORIGINAL arbitrary-core complete reference with C(F_L;R)<=K I(F_L) paid from the SAME unused physical influence. No source is supplied and the empty/nonempty wrapper remains explicit.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes `python -X utf8 code/check.py --pilot` and `python -X utf8 code/check.py`. Corrected pilot: {pilot['lifts']} lifts,{pilot['checks']} assertions,{pilot['elapsed_seconds']:.4f}s. Main: {main['cores']} ALL labelled nonconstant monotone cores on s<=3, {main['lifts']} actual lifts (69 canonical L1,2,3 and46 redundant-anchor L1,2), {main['truth_inputs']} full physical inputs, max dimension{main['maximum_dimension']}; {main['scalar_pairs']} rational finite-bound pairs s1..64,delta=2^-j,j0..16; {main['checks']} exact checks in{main['elapsed_seconds']:.4f}s. Literal CNF, integer Walsh and independent physical bit flips check signed coefficients, all influence identities, primeness witnesses, entropy errors, coefficient granularity, dominance and rare-sector extraction. No symmetry reduction or dimension escalation.

ROOT_SPEC.json precedes `python -X utf8 code/root_check.py`: actual four-bit AND of two OR2 clauses;18 reference profiles with distinct theta and Z exponents1,7,128; {roots['checks']} exact checks in{roots['elapsed_seconds']:.4f}s. Synthetic references cover the actual spectrum; they are not asserted to arise from a newly constructed gate sampler. Main plus root total={total}; pilots overlap and are excluded. Fractions and exact log-prime vectors establish identities; positive24-term atanh expansions with exact tail bounds and outward ln2 division establish entropy signs. Floats record runtime only.

The first pilot FAILED due to the new checker's bit/spin private-character phase, then passed after adding(-1)^|T|; out/PILOT_FAILURE.md preserves it. Negative controls reject signed-anchor nesting, common scaling and domination-free extraction; deleting the surplus fails the exact root identity. No failed run is a certificate.

FORMAL_SPEC.json freezes a core-only signed-integer accounting implication, not the real/Fourier theorem. Its explicit source/compiler hashes and target are in out/lean.json. The45s check returned RUNTIME_UNVERIFIED after{lean['seconds']}s: compute-state access denied before a compiler result. No theorem-kind, axioms or translation certificate is available. No Lean proof is claimed. Mathlib's measured approximately4GB footprint exceeds this packet's1.5GB cap, so it was not launched. Python estimates<=100MB; core-only formal estimate200MB. No planned job exceeded300MB; no heavy search, GPU, remote job, window or detached process was launched. Latest observed governor was ok with9.9GB available memory, but C: only5.1GB free; no other work was stopped.

## proof dependencies and changed downstream conclusions

The new theorem uses independently reconstructed A015@1 plus direct finite accounting, Boolean granularity, monotone duality, Poincare and elementary scalar bounds. It does not depend on A015's acceptance of A007, on a paid arbitrary-core source, or on Lean. Claims retain exact source statement hashes. The new finite transfer is distinct from the source theorem: A007 contributes it and cannot independently accept it. A015 positive universality is reviewed unchanged. The whole signed-core source gap from the prior stage remains open, as does the monotone source gap exposed here.

## one next mathematical action and independent reviewer

{progress['next_action']} This is a source-bound handoff in A007's permitted output; no message is sent and no peer adoption is claimed.

## actual persistence receipts or precise save blocker

Four exact-schema protocol files, proofs/review, frozen specs, code, outputs and source pins are saved only in A007; code/finalize.py checks fields, source hashes, successful helper hashes, case counts and actual readback. PACKET_DELTA equals PROGRESS with packet_ids=[A007]. out/PERSISTENCE.json records landed bytes and SHA256. STATUS has exactly two lines; WORKLOG/LEARNED updated. Every file<20MB. No git, mail, brain-write, shared research-index or other-agent mutation, trading access or new worker. Supervisor mirror/adoption UNVERIFIED. Initial checklist working update failed with lock-held-too-long; no lock was removed. Brain wake flagged stale owner-model188.8h,state-of-mind173.4h,dream45.8h, reported immediately and not relied on as mathematical authority. The formal infrastructure blocker is recorded above; research artifact persistence has no blocker. All launched source checks have exited.

Universal bridge: C020 whole-set witness cost advances by independent acceptance of A015's full positive-anchor universality theorem and by closing its finite arbitrary-reference extraction gap, with explicit(1+delta) transfer and exact two-normalizer/surplus cancellation. This makes a paid positive-anchor source a quantitatively finite source for EVERY monotone core; it does not pay the source. What remains is the ORIGINAL core-sensitive complete cost bound, including labels, signed fusion, attachments and all existing bills from ONE physical influence account. NEXT targets that missing universal supplier rather than repeating positivity, limit continuity or normalization algebra as a presumed FEI proof. Full FEI remains OPEN.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
status=f'STATE: A007 stage22 saved: A015 positive universality independently HOLDS; NEW finite positive-core source extraction(1+delta) with surplus and BOTH root/sector normalizers retained;{total} exact checks PASS;Lean runtime unverified;new review pending;FEI OPEN.\nNEXT: A008/A015/A086/A094 review finite domination/duality/surplus. Fund ORIGINAL arbitrary-core complete reference from SAME unused physical influence, retaining full labels/fusion/attachments; finite positive extraction is now supplied, universal source remains unpaid.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8');assert len(status.splitlines())==2
log=f'\n## {NOW} — stage22 positive dominated finite extraction\nIndependently reconstructed A015 positive-anchor theorem unchanged. Closed its finite supplied-reference gap using Boolean coefficient granularity, monotone duality and exact surplus-aware two-normalizer cancellation. Main62997 plus root91={total} checks PASS; first pilot phase mismatch repaired and preserved. Core Lean infrastructure read denied; no formal result. Full FEI/source supplier open; independent reviewers A008/A015/A086/A094.\n'
for name,entry in [('WORKLOG.md',log),('LEARNED.md',f'\n## {NOW} — positive finite extraction and two normalizers\nFor u>=a p, fixed subprobability R and E, exact C_p(R_E/Z)=(D-B)/a+v log2 Z, B=sum_E(u-ap)log2(1/R)>=0. With raw Q and R=Q/theta, original-root normalizer cancels exactly to(D_Q-B_Q)/a+v log2 Q_E. Dropping B leaves spurious rare-root costs when scaling is unequal. This does not pay repeated roots.\nA015 positive lift: |Fhat_core-ghat|<=2qepsilon; every nonzero nonempty Boolean coefficient>=2^(1-s). Thus rho=2^s qepsilon<1 gives u>=(1-rho)^2 p. Orient via monotone dual -g(-z),q<=1/2, and L=2s+2ceil(log2(16/delta)); any supplied K-paid source transfers within(1+delta)K. No common amplitude scaling or universal supplier is needed/produced. The empty wrapper is separate. A015 whole positive-universality claim independently HOLDS.\nChecker lesson: bit1=true and Walsh(-1)^bit require private phase(-1)^|T|; do not mistake this convention error for signed-fusion failure. Lean infrastructure denial leaves formal verification UNRESOLVED.\n')]:
    with (AGENT/name).open('a',encoding='utf-8') as f:f.write(entry)

receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json' and '__pycache__' not in p.parts:
        raw=p.read_bytes();assert len(raw)<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(raw),'sha256':sha(raw)})
write(RUN/'out/PERSISTENCE.json',{'observed_at':NOW,'run':str(RUN),'files':receipts,'protocol_fields_verified':True,'rolling_status_two_lines':True,'supervisor_mirror':'UNVERIFIED'})
for item in receipts:assert sha((RUN/item['path']).read_bytes())==item['sha256']
assert load(RUN/'PROGRESS.json')==load(RUN/'PACKET_DELTA.json')
print(json.dumps({'verdict':'PERSISTED_READBACK_PASS','files':len(receipts),'exact_nonpilot_checks':total,'new_claim':claim['claim_id'],'review':review['claim_id'],'formal_status':lean['result']['status']}))
