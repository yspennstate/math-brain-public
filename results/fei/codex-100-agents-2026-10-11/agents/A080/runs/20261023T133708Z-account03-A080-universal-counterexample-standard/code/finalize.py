"""Persist this stage's protocol package and verify exact schemas/hashes."""
import datetime
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
RUN=R.name
STAMP=datetime.datetime.now(datetime.timezone.utc).isoformat()
PROTOCOL=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
P=json.loads(PROTOCOL.read_text(encoding='utf-8'))

def read(name):
    return json.loads((R/name).read_text(encoding='utf-8'))

def write(name,value):
    (R/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

main=read('out/main_summary.json')
verify=read('out/verification_summary.json')
extraction=read('out/extraction_summary.json')
sign_check=read('out/SOURCE_SIGN_CHECK.json')
assert sign_check['status']=='PASS' and len(sign_check['nonnegative_parent_debit_witness']['all_restrictions'])==27
assert all(s['status']=='PASS' for s in (main,verify,extraction))
assert (main['tensor_rows'],main['bank_rows'],verify['lifted_dual_states'],extraction['clipped_bank_rows'])==(1536,1024,2904,1024)
base=Path('~/brain_workers/FEI100_20261011')
sourceA072=base/'agents/A072/runs/20261023T120900Z-account03-A072-exact-walsh-engine'
sourceA074=base/'agents/A074/runs/20261023T130641Z-account03-A074-independent-reproducer'
source_digest='7915dd26ad9c6b26a8980b8d2f2775a63fed7d3e8ba5fe8831ca5796f05f313c'
consumers=['A071','A072','A074','A075','A084','A089','A092','B16','B20']
claim_id='A080-EXACT-HULL-TENSOR-FAITHFUL-BANK'
statement=(
 'For every K>=0 and arbitrary finite disjoint uniform-cube Boolean factors, the full physical stopping hull R_K of (H-KI)_+ tensorizes exactly: R_K(product_i f_i)=sum_i R_K(f_i), with no root-sign hypothesis. Always 0<=H-R_K<=KI, and for 0<=K<=L, 0<=R_K-R_L<=(L-K)I; R_K is convex piecewise affine in K. For every actual disjoint-core Boolean composition F=B(g_i), pivotal probabilities q_i and signed correction C=H(F)-sum_i q_i H(g_i), the bank A=C+kappa I(F)+sum_i q_i R_K(g_i) satisfies H(F)+(kappa-K)I(F)<=A<=H(F)+kappa I(F). Any two representations of the same F at the same K,kappa differ by at most K I(F). With fixed kappa, unbounded A/I implies an actual ordinary H/I counterfamily, even with varying K; the converse holds at bounded K. The clipped bank A_plus=C_+ +kappa I+sum_i q_i R_K(g_i), even though not universally coherent, obeys A_plus/I-kappa<=max(H(F)/I(F),max_{i:q_i I(g_i)>0} H(g_i)/I(g_i)); its unbounded root ratio therefore extracts an actual whole-or-core Boolean counterfamily. Products cannot amplify a finite A/I or R_K/I at fixed K,kappa. For F_t the product of t independent two-bit functions negative only at00, H=2t,I=t,Var=1-4^-t,R_K=t(2-K)_+, providing sharp bank endpoints at0<=K<=2 and divergent variance/average-influence normalizations despite H/I=2. No universal initial bank bound, no full FEI proof, and no unbounded ordinary-ratio family is asserted.'
)
hypotheses=[
 'Finite {-1,1}-valued functions on independent uniform physical bits; H is Shannon entropy in bits of the normalized squared Fourier law, I is total physical influence.',
 'K>=0; every R_K is the true complete finite physical stopping hull, with all adaptive queries and both full outcomes retained; factors have disjoint supports.',
 'Composition cores and outer gate are actual Boolean functions, allowing constants/dummies; q_i are actual independent biased-output pivotal probabilities, not substituted formal parameters.',
 'Counterexample extraction uses fixed kappa, nonconstant actual whole functions, and actual full influence denominators; bounded K is required only in stated converse and representation-sequence comparisons.',
 'Initial-bank algebra is unconditional. Nonnegative coherent status of the signed bank at kappa=6 is the separate A072 theorem reviewed by A074; no fresh original owner credit or repeated repartition payment is inferred.'
]
claim={
 'claim_id':claim_id,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A080'],
 'proof_source':[str(R/'PROOF.md'),str(R/'out/main_certificates.json'),str(R/'out/verification_summary.json'),str(R/'out/extraction_summary.json')],
 'proof_dependencies':['Finite physical restriction DAG and stopping-policy duality, proved directly by backward induction.','Shannon chain rule, entropy concavity, character orthogonality and direct edge counting, reconstructed in PROOF.md.','Actual pivotal-influence identity and exact composition correction; no unproved FEI inequality.','A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1 is used only to identify the separately coherent kappa=6 bank; algebra, tensorization and extraction do not require its drift theorem.'],
 'review_records':[{'reviewer':'A080','verdict':'AUTHOR_PROOF_AND_EXACT_VALIDATION_ONLY','arithmetic':'Rational prime-log forms and integer-power signs; direct-character primal/dual reconstruction without producer import or Bellman maximization.','critical_scope':'Zero-payoff leaf completion and actual joint policy attain the lifted feasible dual; clipped bank chooses an actual whole/core function.','external_independent_review':'PENDING','source_repair_supplied':False}],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Tensor amplification of a finite ordinary H/I or full-hull R_K/I ratio.','Inference from variance-normalized or dimension-averaged-influence growth to an FEI counterexample.'],
 'first_unproved_line':'A dimension-independent initial price for the coherent bank, or a literal Boolean sequence with its actual root A/I (or A_plus/I with whole/core extraction) unbounded.',
 'next_consumers':consumers
}
assert set(claim)==set(P['required_per_run']['claim_fields'])
source089=base/'agents/A089/runs/20261023T130925Z-account03-A089-repair-specialist'
source089_payload=read('out/A089_SOURCE_CLAIMS.json')
source089_claims=source089_payload if isinstance(source089_payload,list) else source089_payload['claims']
reviewed=next(c for c in source089_claims if c['claim_id']=='A089-SHARPENED-SIGNED-COMPOSITION-RESERVE')
assert reviewed['statement_sha256']=='94adafb66d404d69b722a3569138674608b98775a94613fe3d4c9889ca26e633'
assert set(reviewed)==set(P['required_per_run']['claim_fields'])
reviewed['review_records'].append({'reviewer':'A080','verdict':'HOLDS_AT_SUBSTATEMENT_SCOPE','scope':'Unchanged all-partition initial-price sandwich, inner savings bounds and fixed-K existential initial-price equivalence; PROOF section5 price paragraphs.','source_statement_sha256':reviewed['statement_sha256'],'not_accepted':'Full owner/debit proof: literal S=H-KI gives negative child debit; exact parity sign receipt and proposed S=KI-H erratum. No full source-version acceptance.','repair_supplied':'None in accepted price substatement; proposed sign repair in excluded owner proof, with recusal from independent acceptance of its repaired version.','artifacts':[str(R/'SOURCE_REVIEW.md'),str(R/'out/SOURCE_SIGN_CHECK.json')],'source_owner_correction':'PENDING_A089'})
reviewed['proof_source']=[str(source089/'PROOF.md'),str(source089/'CLAIMS.json'),str(R/'SOURCE_REVIEW.md')]
reviewed['status']='SOURCE_AUTHOR_PROVED; A080_PRICE_SUBSTATEMENT_HOLDS; FULL_A080_ACCEPTANCE_WITHHELD_PENDING_OWNER_PROOF_ERRATUM'
reviewed['first_unproved_line']='Written PROOF section5 uses S=H-KI and incorrectly asserts d_b=S_b+a_b>=0; exact admissible-root witness fails. The proposed S=KI-H erratum awaits A089 source correction and independent owner-proof review. Separately the universal initial bank price remains unproved.'
claim['proof_dependencies'].append('The bank sandwich overlaps A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1, independently reconstructed here; source digest preserved in scoped review. Tensor lower bound and clipped extraction are distinct A080 additions.')
write('CLAIMS.json',{'run_id':RUN,'stream':'B16','claims':[claim,reviewed]})
progress={
 'protocol_revision':P['revision'],'run_id':RUN,'stream':'B16','packet_id':'A080',
 'gap_id':'B16-RETAINED-ARBITRARY-SEED-ENTROPY',
 'attempt_id':'A080-exact-tensor-faithful-signed-and-clipped-bank-v1',
 'method':'Consume the newly independently reviewed signed-coherence theorem; prove exact full-hull tensorization by zero-payoff completion; bound true hulls by entropy; derive representation-stable signed-bank sandwich and actual-function extraction from the clipped bank; verify primal/dual certificates with direct characters.',
 'mathematical_delta':'Universal all-dimensional exact tensorization removes the previous root-sign restriction; all-real-rate stability; bank partition distortion <=KI; fixed-kappa normalized divergence is faithful; even the incoherent clipped candidate yields an actual whole/core unbounded-ratio family if its true root ratio diverges. Explicit all-t actual family rejects variance/average-influence artifacts. The initial bank price remains unpaid.',
 'deliverable_status':'COMPLETE_LOCAL',
 'mathematical_status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1; unchanged digest '+source_digest+' (coherent bank context only)','A074 independent acceptance, immutable run20261023T130641Z (source review receipt, not review of this new theorem)','Prior A080 full-hull product upper bound; lower bound is newly proved without the old root-sign hypothesis.'],
 'claims_created_or_changed':[claim_id+'@1'],
 'source_artifacts':[str(R/x) for x in ('PROOF.md','FROZEN_SPEC.json','MAIN_SPEC_ADDENDUM.json','EXTRACTION_SPEC.json','out/main_summary.json','out/verification_summary.json','out/extraction_summary.json','out/main_certificates.json')],
 'next_consumers':consumers,
 'next_action':'A074/A092 independently reconstruct zero-payoff completion and sharp bank sandwich/extraction from PROOF.md; A072/A075/A089 then attack the initial price on genuinely indecomposable cores, using actual full I and fixed kappa, rather than tensor amplification or repeated reuse of spent influence stock.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal initial influence payment is open; no actual unbounded ordinary-ratio family found.','External independent review of this new universal lemma remains pending.','Supervisor copying, remote mirrors and downstream mathematical consumption are not verified.','Brain self-care degraded/unverified: stale personal owner/state/dream context and attachment-rendering/write-lock failure; excluded from mathematical premises.'],
 'packet_ids':['A080']
}
expected=[x.split(' (')[0] for x in P['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
progress['claim_versions_used'].append('A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1; unchanged digest94adafb66d404d69b722a3569138674608b98775a94613fe3d4c9889ca26e633; bank-price substatement independently accepted only')
progress['claims_created_or_changed'].append('A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1 scoped price review; written owner-proof sign erratum identified, not a statement refutation')
progress['source_artifacts'] += [str(R/'SOURCE_REVIEW.md'),str(R/'out/SOURCE_SIGN_CHECK.json')]
progress['blockers'].append('A089 must apply/verify the written owner-proof sign erratum S=KI-H; scoped price acceptance does not accept that repaired owner proof.')
write('PROGRESS.json',progress)
(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# A080 / B16 — stage requested 2026-10-23 13:37 UTC

## exact target, quantifiers, hypotheses and units

Prove a universal counterexample standard for the newly coherent signed-composition bank: an FEI disproof requires a sequence of actual Boolean uniform-cube functions with ordinary H/I unbounded. Entropy is in bits and I is total physical influence. K>=0, finite disjoint supports, all physical restrictions and adaptive stopping policies, constants and dummies are included. A finite high ratio only bounds the possible universal constant from below. Full FEI remains OPEN. The user's current campaign deadline,2026-10-23 14:49 UTC, supersedes the older protocol calendar.

## sources actually read, revisions and theorem locators

Read BOARD at stage start (13:38 UTC snapshot), unchanged B16 STREAM_NOTES v2, own STATUS/prior-stage results, machine rules and the entire execution protocol revision{P['revision']}. Campaign/registry/paper intake carries forward from earlier stages; no new literature assertion is used. Newly consumed immutable sources are A071113913 REPORT, A075's latest source report, A092121344 REPORT and, critically, A072120900 PROOF sections1–4 and CLAIMS plus A074130641 PROOF/CLAIMS. A072's exact source claim digest is{source_digest}; A074 accepts that unchanged claim. New source coherence supersedes the old next-step search for an unbounded nonempty correction drift. Source byte receipts are in out/SOURCE_RECEIPTS.json. No peer executable was imported or run.

Current-session brain wake completed but self-care remains degraded/unverified: personal owner/state/dream notes were100.1h/84.7h/35.4h stale and attachment rendering had a write-lock timeout. This affects personalization and memory completeness; those notes were excluded from mathematical premises. Shared governor heartbeat was stale; it was not restarted or altered. All computations stayed in the frozen100MB lightweight class.

## complete derivation or exact first unsupported line

PROOF.md gives the full argument. The new tensor lower bound completes every negative-signed-deficit, zero-credit leaf to constants before combining optimal factor policies. It yields R_K(product f_i)=sum R_K(f_i) for ALL factors, removing the prior sufficient root-sign condition. Entropy erasure gives0<=H-R_K<=KI and influence superharmonicity gives rate Lipschitz control. Substituting D_i=H_i-R_i proves H+(kappa-K)I<=A<=H+kappa I, so two representations differ by at most KI. Tensor products cannot amplify finite ratios. A growing clipped-root bank selects an actual whole function or active core with ordinary ratio at least A_plus/I-kappa, even though clipping failed coherence.

The exact all-t point-defect tensor family has H=2t,I=t,Var=1-4^-t and R=t(2-K)_+. It realizes both bank endpoints and rejects divergence obtained by dividing by variance or average influence. Units, empty-spectrum conditioning, dummy bits, rate variation and decomposition changes are handled explicitly. A one-state partition comparison is not authorization to recharge the same owner after earlier spending. The first unsupported full-FEI line is a dimension-independent initial A<=L I, or a concrete Boolean family with unbounded faithful root ratio. Neither is asserted.

## executed validation with domain, arithmetic, commands and outputs

Specifications were saved before their computations. All16 labelled two-bit functions give256 ordered tensor pairs at six fixed rates:1536 root rows. All16 two-bit outer gates and16 first two-bit cores, with the fixed second core, give256 circuits at four rates:1024 bank rows. No symmetry reduction, maximum dimension4, no automatic growth. Exact Fraction/log-prime identities are ordered by clearing denominators and comparing integers; largest comparison uses{main['max_integer_comparison_bits']} bits. No floating-point mathematical verdict is used.

Commands from A080 are `python -B -X utf8 runs/{RUN}/code/check.py --pilot`, then `.../code/check.py`, `.../code/verify.py`, and `.../code/extraction.py`. Pilot:221 predicates,4 tensor and16 bank rows, runtime0.553s. Main:{main['exact_predicates']} predicates, runtime{main['elapsed_seconds']:.3f}s. Separate direct-character certificate verification:{verify['exact_predicates']} predicates,132 factor dual states,2904 lifted dual states,96 actual physical policy trees,1536 tensor-root primal/dual equalities, runtime{verify['elapsed_seconds']:.3f}s. These are{main['exact_predicates']+verify['exact_predicates']} main/verification predicates; repeated import checks are not counted. Clipped extraction:1024 rows ({extraction['nonconstant_rows']} nonconstant,{extraction['constant_rows']} constant), all passed. Validation uses saved feasible duals and attaining policies rather than reproducing the product Bellman maximization. It is separate author implementation, not external-agent acceptance. Every job was under55s with100MB estimated memory; none crossed the300MB memok gate.

## proof dependencies and changed downstream conclusions

Only finite stopping induction, Shannon chain rule/concavity, character orthogonality and actual pivotal-influence identities enter the new lemmas. A072's separately reviewed theorem makes the kappa=6 signed bank coherent; its initial price is still missing. Universal tensor additivity closes all tensor amplification of true hull/root-bank ratios. A bounded-K change of representation cannot produce new divergent ratios. The clipped bank remains incoherent, but its genuine root ratio can still expose an actual core counterfamily. Arbitrary admission-capital overestimates do not satisfy this extraction theorem. Source claim versions were neither repaired nor overwritten.

## one next mathematical action and independent reviewer

A074/A092 should independently verify the zero-credit completion lower bound and sharp sandwich/extraction in PROOF.md. Then A072/A075/A089 should test initial payment on indecomposable actual Boolean cores with total physical influence and fixed kappa. This review is pending; naming recipients is a source-bound handoff, not evidence of their receipt or acceptance. No new schedule, worker, message or brain write was created.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, code/out, the three frozen specifications, proof, source receipts and current rolling files are saved inside A080. out/MANIFEST.json records SHA256/size receipts; out/FINAL_AUDIT.json checks exact protocol fields, source digests, compatibility-copy bytes and all file-size limits. Statement digest hashes UTF-8 exact_statement bytes. No local save blocker. Git was not run; supervisor copying and remote durability remain unverified. No process or heavy job from this stage remains running.

## Universal bridge

This stage advances B16's C019 stopping-tree/initial-bank bridge by exact all-function tensorization and a sharp representation-stable, counterexample-faithful bank comparison; it also gives a one-state C024 repartition bound, without asserting a paid history transfer. What remains is universal initial influence payment on arbitrary indecomposable Boolean cores, or an actual root-ratio divergence yielding an ordinary Boolean counterfamily. NEXT attacks that single unpaid line using A072's now-reviewed coherent signed bank; further tensor growth, local overprotection or variance normalization cannot close FEI and are ruled out here.
'''
report=report.replace('largest comparison uses','main producer\'s largest comparison uses')
report=report.replace('the three frozen specifications','the frozen specifications')
report=report.replace('No peer executable was imported or run.','No peer executable was imported or run. A later live checkpoint led to reading A089130925 PROOF/CLAIMS completely: its existing all-partition sandwich overlaps our independent derivation and is credited with a scoped unchanged-version acceptance in SOURCE_REVIEW.md. The source written owner proof has S reversed; exact two-bit parity gives child debits-1. This is a proof erratum, not a source-statement or FEI refutation. A089 source correction and A074/A092 landing review are pending.')
report=report.replace('The new tensor lower bound','The bank sandwich is an independent reconstruction of the overlapping A089 result; it is not claimed novel. The new tensor lower bound')
report=report.replace('This stage advances B16\'s C019','Source accounting caveat: A089 must correct and verify its written S convention; no source owner-proof acceptance is claimed here. This stage advances B16\'s C019')
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: COMPLETE_LOCAL '+RUN+'; exact full-hull tensorization and faithful signed/clipped-bank extraction author-checked; scoped A089 price acceptance; independent review pending; FEI OPEN.\nNEXT: A074/A092 review tensor/extraction; A089 correct written owner-proof S sign; A072/A075/A089 price initial signed bank on indecomposable cores with actual total influence/fixed kappa.\n',encoding='utf-8')
log=f'\n### {STAMP} — {RUN}\nConsumed A072120900/A074130641 universal signed-coherence source; superseded raw nonempty-drift search. Proved exact R_K tensorization without root-sign assumption, rate stability, KI partition-width bank sandwich and actual whole/core extraction for clipped roots. Main1536 tensor/1024 bank rows plus direct-character primal/dual verification passed{main["exact_predicates"]+verify["exact_predicates"]} exact predicates; clipped extraction1024 rows passed. Source-independent agent acceptance and initial bank price remain open. Saved the protocol package and current rolling files; no full FEI claim.\n'
learn=f'\n### {STAMP} — universal hull tensorization and counterfamily extraction ({RUN})\nFor every K>=0, R_K(product f_i)=sum_i R_K(f_i) for disjoint actual Boolean factors: complete every optimal zero-payoff negative-deficit leaf to constants, then combine factor policies. This removes the old root-sign condition. Always0<=H-R_K<=KI and0<=R_K-R_L<=(L-K)I forK<=L. For any actual disjoint-core representation, A=C+kappa I+sum q_i R_K satisfies H+(kappa-K)I<=A<=H+kappa I; hence any two same-K representations differ by<=KI and fixed-kappa A/I divergence gives actual H/I divergence. This one-state repricing bound does not pay repeated historical charges. Even A_plus=C_++kappa I+sum q_i R_K satisfies A_plus/I-kappa<=max(whole H/I,active-core H_i/I_i), giving an actual Boolean whole-or-core selector despite clipped coherence failing. The bound requires TRUE hulls, not arbitrary capital overestimates. Tensor two-bit defects give H=2t,I=t,Var=1-4^-t,R=t(2-K)_+; variance/average-influence divergence is fake. Proof is author-complete with two exact implementations; independent review pending. Full FEI initial payment remains open.\n'
for file,entry in [('WORKLOG.md',log),('LEARNED.md',learn)]:
    p=A/file
    old=p.read_text(encoding='utf-8') if p.exists() else ''
    if RUN not in old:
        p.write_text(old+entry,encoding='utf-8')
review_marker='A089130925-SIGNED-DEBIT-ERRATUM'
for name in ('WORKLOG.md','LEARNED.md'):
    p=A/name
    old=p.read_text(encoding='utf-8')
    if review_marker not in old:
        p.write_text(old+'\n### '+STAMP+' — '+review_marker+'\nA089 independently established the same all-partition bank sandwich; this run credits and accepts only that unchanged substatement. Literal source PROOF section5 writes S=H-KI, which gives child debits-1 on actual two-bit parity atK10,kappa9/2 with supplied bank9. Correct convention S=KI-H gives19. The source claim does not prescribe the reversed sign, so no statement refutation. Proposed owner-proof erratum supplied; A089 correction and independent A074/A092 acceptance pending; A080 recuses from full acceptance of the repaired owner proof. Exact frozen receipt and source bytes are in '+str(R/'SOURCE_REVIEW.md')+'.\n',encoding='utf-8')

sources=[PROTOCOL,base/'BOARD.md',base/'claude/B16/STREAM_NOTES.md',sourceA072/'PROOF.md',sourceA072/'CLAIMS.json',sourceA074/'PROOF.md',sourceA074/'CLAIMS.json',source089/'PROOF.md',source089/'CLAIMS.json']
receipts=[]
for p in sources:
    b=p.read_bytes()
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'scope':'read-only source; current-byte receipt, not a historical BOARD snapshot'})
write('out/SOURCE_RECEIPTS.json',{'written_at_utc':STAMP,'source_claim_id':'A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1','source_statement_sha256':source_digest,'sources':receipts})
source_payload=json.loads((sourceA072/'CLAIMS.json').read_text(encoding='utf-8'))
source_claims=source_payload if isinstance(source_payload,list) else source_payload['claims']
assert any(c['claim_id']=='A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE' and c['statement_sha256']==source_digest for c in source_claims)
for heading in P['required_per_run']['report_fields']:
    assert '\n## '+heading+'\n' in report
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
manifest=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name not in ('MANIFEST.json','FINAL_AUDIT.json'):
        b=p.read_bytes()
        assert len(b)<20*1024*1024,(p,len(b))
        manifest.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
write('out/MANIFEST.json',{'written_at_utc':STAMP,'run_id':RUN,'entries':manifest})
audit={'status':'PASS','written_at_utc':STAMP,'run_id':RUN,'claim_fields_exact':True,'progress_fields_exact':True,'all_report_fields_present':True,'compatibility_copy_byte_identical':True,'statement_sha256_verified':True,'source_claim_digest_unchanged':True,'files_manifested':len(manifest),'all_files_under_20mb':True,'rolling_status_two_lines':True,'external_independent_review':'PENDING','full_fei':'OPEN','remote_copy':'UNVERIFIED','stage_jobs_running':False}
write('out/FINAL_AUDIT.json',audit)
print(json.dumps(audit),flush=True)
