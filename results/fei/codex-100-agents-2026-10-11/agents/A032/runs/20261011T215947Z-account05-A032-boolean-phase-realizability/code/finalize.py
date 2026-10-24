import json, hashlib, datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
RUN=ROOT.name
def dump(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2),encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
report_root=Path(r'~\mop_fei100\reports\fei-2026-10-11')
campaign_root=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
sources=[]
paths=[report_root/name for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
paths += [campaign_root/name for name in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
paths += list((campaign_root/'sources').glob('*.md'))+list((report_root/'runs').rglob('REPORT.md'))+list(context.glob('*.txt'))
for path in paths:
    data=path.read_bytes()
    sources.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'reading_scope':'paper introductions and relevant Fourier/composition locators; text scanned' if path.parent==context else 'campaign context or mathematical source read; not a proof dependency'})
dump('out/SOURCE_MANIFEST.json',sources)
summaries=[json.loads((ROOT/'out'/f'summary_n{n}.json').read_text()) for n in range(5)]
dump('BOOLEAN_REALIZABILITY.json',{'schema':'A032-uniform-realizability/1','ambient_convention':'physical and spectral masks in least significant bit order; chi_s(x)=(-1)^(s dot x)','exact_interface':'code/phase_exact.py:admit and affine_admit','classification':summaries,'coupled_obstruction':'out/coupled_phase_certificate.json','lifting_checks':'out/lift_checks.json','independent_review':'PENDING A088/A094','full_FEI':'OPEN'})
statement=('For every uniform Boolean cube, a spectral probability law supported on at most four labels is realizable iff it is a singleton of mass1 or the uniform law on an affine plane. A uniform affine-subspace law of dimension r is realizable iff r is even, and then H=r<=2D<=2I. For arbitrary supported laws, phase realizability is equivalent to phase realizability on the support affine-span quotient. The labelled four-variable law with Walsh magnitudes (8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) and denominator256 passes all15 separate XOR pair partitions but has no realizing phase (all512 phases certified). Complete exact enumeration on n=4 yields2261 distinct Boolean spectral laws among975621 magnitude laws satisfying square norm and necessary even/common-mod4 arithmetic.')
claim={'claim_id':'A032-EXACT-PHASE-ADMISSION','version':1,'exact_statement':statement,'hypotheses':['Finite uniform cube; real Boolean outputs +/-1','Labelled full spectral law, not an unlabelled mass histogram','D=sum_i min(Inf_i,1-Inf_i); H in bits','Finite enumeration fixes n<=4; all-dimensional claims proved analytically'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A032'],'proof_source':['REALIZABILITY_METHOD.md','out/coupled_phase_certificate.json','code/enumerate_exact.py','out/summary_n4.json','code/verify_direct.py'],'proof_dependencies':[],'review_records':[{'reviewer':'A032 author','method':'separate direct character-sum reconstruction of all2299 law witnesses and direct signed-convolution rejection of all512 candidate phases','verdict':'PASS; NOT INDEPENDENT REVIEW'}],'status':'PROVED_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Separate exact XOR pair partitions are sufficient for one common Boolean phase'],'first_unproved_line':None,'next_consumers':['A031','A033','A034','A045','A078','A079','A088','A094']}
dump('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B07','packet_id':'A032','gap_id':'G-BOOLEANITY','attempt_id':'A032-PHASE-ADMISSION-01','method':'Exact integer Walsh admission; full finite truth catalogue; affine-rank reduction; coupled-sign rejection certificates','mathematical_delta':'Complete n<=4 phase-law admission baseline, support<=4 all-dimensional characterization, even-rank affine-flat realizations, and a ten-atom certificate separating independent XOR partitions from simultaneous phase consistency. No universal entropy payment proved.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'PACKET_INTERFACE_AND_STATED_CASES_CLOSED; UNIVERSAL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':[],'claims_created_or_changed':['A032-EXACT-PHASE-ADMISSION@1'],'source_artifacts':['REPORT.md','CLAIMS.json','BOOLEAN_REALIZABILITY.json','REALIZABILITY_METHOD.md','SEARCH_SPEC.json','VERIFY_SPEC.json','code/phase_exact.py','code/enumerate_exact.py','code/verify_direct.py','code/check_lifts.py','out/summary_n4.json','out/coupled_phase_certificate.json','out/direct_verification.json','out/lift_checks.json','out/SOURCE_MANIFEST.json'],'next_consumers':['A031','A033','A034','A045','A078','A079','A088','A094'],'next_action':'A033/A031 test the512-phase coupled obstruction against the proposed signed payment and identify an algebraic phase-consistency inequality that bounds unpaid conditional entropy; A088/A094 independently reconstruct certificates.','stagnant_substantive_attempts':0,'blockers':['B07 STREAM_NOTES.md absent at supplied path; board and authoritative B07 contract used instead. No mathematical computation blocker.'],'packet_ids':['A032']}
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)
report='''# A032 Boolean phase realizability

## exact target, quantifiers, hypotheses and units

Determine exact phase realizability of labelled spectral laws on every uniform cube, with finite exact admission through n=4 and analytic certificates for support<=4 and uniform affine-subspace laws in every dimension. All outputs are +/-1; H is in bits, I is expected spectral Hamming weight, and D=sum_i min(Inf_i,1-Inf_i). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol fei-execution-protocol/2, revision2026-10-11-execution-v2, all rules read. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS B07, plan Boolean phase subsection and A032 acceptance contract, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and curated sources, and earlier B05/B09/B19 reports supplied context. BOARD snapshot2026-10-11 21:55UTC was read at stage start. B07 lead notes do not exist at the supplied path. Source hashes and reading scopes are in out/SOURCE_MANIFEST.json. The four supplied paper text versions were scanned; introductions and relevant Fourier definitions and threshold Proposition7.1 composition identities were read. These class-specific papers supply no premise for this proof. ERASURE_RIGIDITY.md Section1 already proves coordinate-product spectral rigidity; its Section2 explicitly prevents a naive approximate-independence payment. No novelty is claimed for bent functions, arithmetic granularity, or the finite checking strategy.

## complete derivation or exact first unsupported line

REALIZABILITY_METHOD.md gives complete all-dimensional proofs, general integer-square and modulo4 admission conditions, XOR pair-partition certificates, complete sign enumeration, the four-atom classification, affine-flat characterization and affine quotient equivalence. The four-atom class is exactly characters or uniform affine planes. Uniform rank-r affine support is realizable exactly for even r, with an explicit quadratic truth-table formula and H<=2D<=2I.

The ten-atom law p=a^2/256 with a=(8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) passes every separate nonzero-XOR pair partition. Nevertheless every one of its512 phase vectors, modulo global negation, has a nonzero signed convolution coefficient. out/coupled_phase_certificate.json lists each first violating XOR and integer coefficient, and all15 individually possible partitions. This is an exact obstruction to replacing coupled Boolean signs by independent equation-wise cancellations, not an FEI counterexample.

First unsupported universal line: no result here proves a dimension-independent entropy/influence payment from the simultaneous phase identities for general nonflat, growing-affine-rank spectra. The finite catalogue is not extrapolated to that claim.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede searches in SEARCH_SPEC.json and VERIFY_SPEC.json. Commands, from this run directory:

    python -X utf8 code/enumerate_exact.py --n 0 1 2 3
    python -X utf8 code/enumerate_exact.py --n 4
    python -X utf8 code/verify_direct.py
    python -X utf8 code/check_lifts.py

All admission arithmetic is integers/Fraction. The pilot found a mistaken common-mod4 filter at n=1; it was corrected to n>=2 and the pilot reran successfully. Both the endpoint correction and frozen-domain correction are recorded, with no dimension escalation. One computation job ran at a time. Estimated memory stayed below100MB; no job expected to exceed300MB. The full n=4 arithmetic run took51.018seconds, including candidate enumeration and certificate checks, below its180-second cap. n=4 enumerated32768 truth tables after fixing f(0)=+1, exactly representing all65536 tables modulo global output negation. No input or spectral-label symmetry was quotiented.

| n | truth representatives | distinct laws | arithmetic candidate laws |
|---|---:|---:|---:|
|0|1|1|1|
|1|2|2|2|
|2|8|5|5|
|3|128|30|86|
|4|32768|2261|975621|

Candidate laws exhaust nonnegative integer magnitudes of norm2^n satisfying evenness and common-mod4 where applicable; they stream through all labelled placements of every sum-of-squares multiset. Complete Boolean truth enumeration decides each candidate. n=4 has973360 impossible candidate laws. Saved catalogues provide a concrete truth mask for every realizable law and its phase multiplicity modulo global sign. A distinct direct-character implementation reconstructed all2299 saved law witnesses, checked multiset placement counts via factorials, and verified the512 coupled-phase rejections via signed convolution. Six affine examples test ranks2,3,4 and ambient n up to30, including lifted truth tables and direct transforms for n<=5. Larger ambient examples carry an exact reduced truth table and the proved lifting formula. This is author reproduction in a different representation, not independent agent acceptance.

## proof dependencies and changed downstream conclusions

No unreviewed campaign claim is a proof dependency. The new admission interface can be reused by A031/A033/A034/A078/A079. A045 receives only the explicit warning that uniform Walsh arithmetic does not apply to a biased basis. Independent XOR cancellation is now concretely refuted as a sufficient admission relaxation, even after norm, dyadic-square, modulo4 and every individual XOR partition test. The independent-product endpoint remains prior work and is not republished as a new claim. Conditional auxiliary entropy remains unpaid.

## one next mathematical action and independent reviewer

Use the explicit ten-atom coupled obstruction to isolate the first additional common-phase constraint required by A031/A033's signed entropy payment, and derive a conditional entropy consequence from that constraint rather than escalating a fixed convolution prefix. Independent reviewers: A088 and A094. Source-bound handoffs are recorded locally for supervisor collection; no messages were sent.

## actual persistence receipts or precise save blocker

All required files, exact catalogues, certificates and reproducible scripts are written inside A032's designated run; rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/ARTIFACT_RECEIPTS.json lists local file byte counts and SHA256 values. No file exceeds20MB. Shared source trees and other agents were read only; no git, brain mutation, upload, mirror verification or independent review is claimed. No save blocker remains.

## Universal bridge

This stage moves B07's G-BOOLEANITY/G-PHASE-COND admission bridge: complete certificates now distinguish globally realizable phases from independent XOR cancellations, with an ambient-independent affine quotient and closed sparse/affine-flat cases. It does not advance a numerical universal C018/C019/C020/C024 payment. What remains is to convert common-phase consistency into a paid entropy remainder for nonflat spectra of growing affine rank, while retaining arbitrary tensor conditional entropy. Applying the ten-atom obstruction to the live signed-payment derivation is the shortest next route: it identifies information discarded by the relaxation and tests the needed universal mechanism, whereas merely enumerating another dimension would only extend the finite census.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A032 phase-admission packet complete locally: n<=4 exact census, sparse/affine-flat proofs, and512-phase coupled obstruction; review pending; full FEI OPEN.\nNEXT: A088/A094 reconstruct certificates; A031/A033 derive a conditional-entropy payment from simultaneous phase consistency using the ten-atom obstruction.\n',encoding='utf-8')
(AGENT/'LEARNED.md').write_text('''# A032 durable lessons

- Uniform Walsh square arithmetic: N^2 p_s must be an integer square; Walsh integers are even for n>=1 and share residue modulo4 for n>=2. The n=1 exception matters.
- Support<=4: exactly singleton spectra and uniform affine planes are Boolean-realizable. Four phase signs must have product-1. Non-affine four-point support has a unique XOR pair and cannot cancel.
- Uniform affine rank-r spectrum is realizable exactly when r is even. Quadratic pair factors construct its actual truth table. H=r<=2D<=2I. Coordinate-product rigidity was already proved in ERASURE_RIGIDITY.md; no novelty claim.
- Arbitrary support on t+V reduces phase admission to rank(V) physical bits; influence is not invariant under arbitrary linear relabelling.
- Separate XOR pair partitions are insufficient. Candidate Walsh magnitudes(8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) pass all15 partitions but all512 common phases fail signed convolution. The run contains an independently encoded rejection for each phase.
- n=4 exact catalogue:2261 Boolean spectral laws among975621 arithmetic-compatible laws. Global output negation is the only removed truth-table symmetry. Full finite census does not supply a universal entropy bound.
- Conditional auxiliary entropy and arbitrary-tensor embedding remain obligations; flat cases and integer granularity cannot be substituted for that payment.
''',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{datetime.datetime.now(datetime.timezone.utc).isoformat()}: Complete n=4 run passed in51.018s; 975621 candidates,2261 realizable. Different direct-character checker reconstructed2299 law witnesses and512 simultaneous phase rejections; six affine lift checks passed. Saved required report/claims/progress/delta plus interface and all certificates. Universal FEI and independent review remain open.\n')
receipts=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name!='ARTIFACT_RECEIPTS.json':
        receipts.append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':sha(path)})
assert all(row['bytes']<20_000_000 for row in receipts)
dump('out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED','files':len(receipts),'max_file_bytes':max(row['bytes'] for row in receipts),'run_directory':str(ROOT)}))
