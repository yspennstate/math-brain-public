"""Persist only this A076 run and A076 rolling files."""
from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
read=lambda p:Path(p).read_text(encoding='utf-8')
put=lambda p,t:Path(p).write_text(t,encoding='utf-8')
validation=json.loads(read(R/'out/VALIDATION.json')) if (R/'out/VALIDATION.json').exists() else {'status':'PENDING'}
base=Path('~/brain_workers/FEI100_20261011')
sources=[A/'runs/20261023T135923Z-account03-A076-threshold-and-tribes-controls/DISJOINT_MASK_PROOF.md',
base/'BOARD.md',base/'claude/B16/STREAM_NOTES.md',base/'context/threshold_paper_38pp.txt',
base/'context/threshold_paper_29pp_earlier_version.txt',base/'context/percolation_spectral_pivotal_entropy_30pp.txt',
base/'context/percolation_spectral_pivotal_entropy_31pp_other_version.txt']
receipts=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources]
put(R/'out/SOURCE_RECEIPTS.json',json.dumps(receipts,indent=2))
statement=('Repair of stage11 raw-mask bank: for a zero-one shared event a, independent Boolean V, '
'F=1+a(V-1), p=Ea, mu=EV,q=1-mu,D=sum |S| ahat(S)^2,J=sum phi(ahat(S)^2), '
'N=H(F)-pH(V), the exact equation (1) of ACTIVATION_PROOF.md holds and '
'0<=N<=2qJ+5pq, I_shared=2qD, I_private=pI(V). For 0<p<=1/2 and J<=KD, '
'N<=(K+5)I_shared. H(1-2a)<=C I(1-2a) implies N<=(C+13)I_shared. '
'Existence of an absolute all-event coefficient for this admission is equivalent to full FEI. '
'The specified rare-event admission need not be hereditary under shared restrictions. '
'The known bent-splice family has N/I_shared>=k-2 for even k>=4 and so obstructs '
'shared-only payment for two arbitrary nonconstant profiles; no novelty or FEI disproof is claimed.')
claim={
'claim_id':'A076-STRUCTURED-SPECTRA','version':12,'exact_statement':statement,
'hypotheses':['Uniform finite independent shared/private cubes; all entropies in bits with empty coefficient retained.',
'Root event probability p<=1/2 only where explicitly used; no automatic hereditary admission.',
'Threshold constant22 conditional on supplied threshold Theorem A equation6, with C<9.',
'Actual original unused account must pay any new admission; old source240, frozen R/K and all old debits remain unchanged.'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A076'],
'proof_source':{'path':str(R/'ACTIVATION_PROOF.md'),'locators':['sections1-3 repair','section4 known-obstruction reconstruction'],'validation':str(R/'out/VALIDATION.json')},
'proof_dependencies':['Finite Walsh tensor algebra, Parseval variance bound and Shannon chain rule','Supplied threshold Theorem A equation6 (only conditional constant22)'],
'review_records':[],'status':'AUTHOR_PROOF_REPAIR_PENDING_INDEPENDENT_REVIEW',
'supersedes':[],'refutes':['Any arbitrary-two-profile N<=K*I_shared with absolute K; known bent-splice obstruction reconstructed'],
'first_unproved_line':'An arbitrary-event original influence-priced source J(a)<=K D(a), or a necessary two-profile continuation paid jointly from unused original private/shared capacity.',
'next_consumers':['A077','A078','A092','A094']}
put(R/'CLAIMS.json',json.dumps([claim],indent=2))
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B16','packet_id':'A076',
'gap_id':'B16-ORIGINAL-ACTIVATION-AWARE-MASK-SOURCE','attempt_id':'A076-activation-repair-v12',
'method':'Exact tensor spectrum; disagreement-weighted event entropy; independent grouped-spectrum reconstruction of known obstruction.',
'mathematical_delta':'Raw mask payment replaced by 2qJ+5pq; exact actual-influence normalization; all-event admission shown FEI-equivalent; known two-profile shared-only obstruction reconstructed.',
'deliverable_status':'COMPLETE_LOCAL' if validation['status']=='PASS' else 'VALIDATION_PENDING',
'mathematical_status':'SCOPED_AUTHOR_PROOF; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
'claim_versions_used':['A076-STRUCTURED-SPECTRA@11 (prior bank and obstruction context)','threshold_paper_38pp Theorem A eq6 (conditional corollary only)',
'math-card claim_7f5f22ff912203aa5274e2ba4e216316da9392bbfda1386c6f02803c17b8e759 (known bent-splice control, reconstructed independently)'],
'claims_created_or_changed':['A076-STRUCTURED-SPECTRA@12 (scoped repair; previous controls retained)'],
'source_artifacts':[str(R/'ACTIVATION_PROOF.md'),str(R/'out/VALIDATION.json'),str(R/'out/SOURCE_RECEIPTS.json')],
'next_consumers':['A077','A078','A092','A094'],
'next_action':'Fund a necessary arbitrary-core two-profile query using BOTH actual unused original private and shared accounts; require original-source invoice, inherited U and full terminals. Do not retry shared-only normalization.',
'stagnant_substantive_attempts':0,
'blockers':['Full FEI unresolved; external reconstruction pending.','Brain wake attachment-integrity checks degraded by attachment lock timeout; owner notified; no affected attachment used.'],
'packet_ids':['A076']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:put(R/name,json.dumps(progress,indent=2))
report=f'''# A076: activation-aware repair, full FEI open

## exact target, quantifiers, hypotheses and units

Repair the prior disjoint-mask source bill for every finite uniform Boolean F=1+a(x)(V(y)-1), independent physical x,y, with the complete private entropy U=pH(V) retained. All entropy units are bits. Establish an actual-influence charge that vanishes at cancellation, then test whether it extends to arbitrary profiles. No claim of full FEI or a counterfamily is made.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json v2 in full; campaign README, status, claim/obstruction/packet/next-action indices and plan were inspected for B16/current gaps. Read supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING; inventoried its sources. Read current BOARD and B16 STREAM_NOTES v2; their old majority/tribes assignment is already closed in A076 stage2. Resume the newer stage11 raw-mask obstruction instead. Read own STATUS and LEARNED and prior DISJOINT_MASK_PROOF sections1-5. Supplied threshold 38pp Theorem A eq6 supplies only conditional C<9; percolation 30pp intro/Theorem1.1 has geometric crossing hypotheses and supplies no arbitrary-event theorem. Earlier versions are retained as source receipts, not additional proof dependencies. No new literature/priority claim is made.

Math recall identified the existing bent-splice obstruction. Read full card claim_7f5f22ff912203aa5274e2ba4e216316da9392bbfda1386c6f02803c17b8e759 and its links. Its asymptotic is not assumed: section4 independently derives the weaker sufficient bound N>=delta(k-2). Hash receipts are in out/SOURCE_RECEIPTS.json. Brain wake returned exit1 with attachment lock timeouts; owner notified before relying on affected notes. No failed attachment is used.

## complete derivation or exact first unsupported line

ACTIVATION_PROOF.md sections1-3 derive the complete joint spectrum, exact scalar bank and original physical influences. The repair is 0<=N<=2qJ(a)+5pq, I_shared=2qD(a), q=1-EV. For p<=1/2 and J<=KD, N<=(K+5)I_shared; supplied FEI for the event gives coefficient C+13 (22 for supplied thresholds). The argument retains pH(V) exactly and vanishes when V=+1. The all-event version is FEI-equivalent by setting V=-1. Thus the precise first unpaid universal line is influence-priced arbitrary-event J(a), not an omitted interference term.

Section4 independently reconstructs a known obstruction: for quadratic bent G and point-flipped V, the selector bank N is at least (k-2) times its actual shared influence, for every even k>=4. The private influence is k/2+k*2^-k and is not discarded. This defeats only a shared-only two-profile supplier. Shared restrictions may violate p<=1/2, so the rare-event admission is not a hereditary consumed-influence theorem.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: FROZEN_SPEC.json, written before search; helper activation-v1; nx=1,2,3, ny=2, all rare indicators and all16 private truth tables (2832 cases), seven fixed grouped bent dimensions and full tables at k4,6. No symmetry enumeration shortcut; no automatic dimension increase. Memory estimate90MB; under300MB, so no large-job admission required; runtime cap60s with55s pilot guard.

Command: python -X utf8 code/check_activation.py (from run directory). Validation status {validation['status']}; exact assertions {validation.get('exact_assertions','PENDING')}, elapsed {validation.get('elapsed_seconds','PENDING')} seconds. Exact Fraction Walsh coefficients and rational prime-exponent entropy identities; signs use24-term atanh enclosures with rigorous geometric tails. Output out/VALIDATION.json records counts and script hash. Floating approximations are not certificates. Lean attempt returned RUNTIME_UNVERIFIED after121 seconds, exit1, recorded in out/LEAN_RESULT.txt. No Lean-checked result is claimed and no retry was launched. The mathematical rung is author proof with exact finite checks, independently unreviewed.

## proof dependencies and changed downstream conclusions

Sections1-2 require no prior threshold FEI. The rare-event source conversion uses only D(a)>=Var(a)>=p/2 from Parseval. Only coefficient22 invokes supplied threshold Theorem A. Previous source240, frozen actual R/K and old debits are unchanged: this stage issues no fresh universal funds and does not apply old point-prefix Xi transport beyond its hypotheses. Full terminal U,N are retained. Existing threshold-class177 admission remains conditional and intact.

The all-event reduction and known bent control rule out treating a disagreement scalar as the missing universal source. A077/A078 should retain both original private/shared capacities in any continuation; the event class alone is still full FEI strength.

## one next mathematical action and independent reviewer

{progress['next_action']} A077/A078 reconstruct formulas and hereditary caveat; A092/A094 independently audit the original-account scope and known obstruction. No acceptance or downstream use is claimed.

## actual persistence receipts or precise save blocker

Saved locally under the assigned A076 run: proof, frozen specification, code, validation, CLAIMS, PROGRESS and identical PACKET_DELTA. Rolling STATUS/WORKLOG/LEARNED updated. SHA256 manifest is produced by this finalizer. No git, mail, brain write, other agent mutation, remote job or trading process is used. Repository mirror and independent review are supervisor tasks and unverified here. Administrative hooks are separate from mathematical completion.

## Universal bridge

This stage moves C019/C024 by replacing the nonvanishing raw-mask majorant with the exact activation-weighted source and proving its actual original-influence normalization; it adds no paid arbitrary-core source. The all-event admission remains FEI-equivalent, and the known bent selector proves why shared disagreement alone cannot pay arbitrary two-profile continuation. The shortest next route is a necessary selected-query invoice using unused original private as well as shared capacity, with full input and terminal entropy retained; another threshold constant or another shared-only test cannot close this gap.
'''
put(R/'REPORT.md',report)
state='STATE: A076 current stage saved: activation-aware bank N<=2qJ+5pq, exact actual influences; all-event admission FEI-equivalent; known bent shared-only obstruction reconstructed; '+validation['status']+'; review pending; FEI OPEN.\n'
put(A/'STATUS.md',state+'NEXT: Fund ONE necessary arbitrary-core two-profile query from BOTH unused ORIGINAL private/shared owners, with old debits and full terminal U/N retained; A077/A078 reconstruct, A092/A094 review; no shared-only reset.\n')
entry=f'\n{stamp}: activation repair saved; {validation["status"]}, {validation.get("exact_assertions","pending")} exact assertions. N<=2qJ+5pq cancels at q0; rare-event actual-source payment derived; hereditary premise explicitly limited. Known bent-splice shared-only failure reconstructed, not new. Full FEI and arbitrary-original source remain open.\n'
for name in ['WORKLOG.md','LEARNED.md']:
    p=A/name;old=read(p) if p.exists() else '';put(p,old+entry)
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='MANIFEST.json':manifest.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
put(R/'out/MANIFEST.json',json.dumps(manifest,indent=2))
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
print(json.dumps({'saved':str(R),'status':validation['status'],'files':len(manifest)},indent=2))
