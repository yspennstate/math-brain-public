from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';A=RUN.parent.parent;ROOT=A.parent.parent
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):
    raw=(json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode('utf-8');assert len(raw)<20_000_000;p.write_bytes(raw)
now=datetime.now(timezone.utc).isoformat();ledger=load(OUT/'THEOREM_RELEASE_LEDGER.json');check=load(OUT/'INDEPENDENT_RESET_REVIEW.json');claims=load(RUN/'CLAIMS.json')
protocol=load(ROOT.parent.parent/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
q=load(OUT/'NEXT_TEN_QUESTIONS.json');assert len(q)==10 and len({x['question_id'] for x in q})==10
assert check['status']=='PASS' and not check['pilot'] and len(check['cases'])==6
assert not load(OUT/'PARSE_FAILURES.json')
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
    assert c['first_unproved_line'] is None or isinstance(c['first_unproved_line'],str)
sources=load(OUT/'CRITICAL_SOURCE_RUNS.json')
counts=ledger['counts']
# A plain review index, with every exact statement in the companion JSON.
lines=['# Accepted theorem and proof-status index','',
       'Full FEI: OPEN. This is a finite A100 handoff snapshot, not a second canonical campaign registry. The current owner deadline is 2026-10-23 14:49 UTC. The source-complete private records remain the governing mathematical evidence.','',
       f"Recorded review groups: {counts['accepted_statement_versions']} accepted at original scope, {counts['partial_statement_versions']} partial/disputed, {counts['pending_statement_versions']} without full independent acceptance, {counts['withdrawn_statement_variants']} withdrawn false statement variant. These counts are statement/version groups, not new theorems or executed stages.",'',
       'A100 newly reconstructs only A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 in full. Its original statement and hypotheses are unchanged. The remaining accepted rows record upstream full-scope verdicts; their exact statements, complete source lists and review records are preserved in out/THEOREM_RELEASE_LEDGER.json. No full-FEI or integrated A099 acceptance follows.','',
       '| Claim and version | Exact-scope evidence |','|---|---|']
for x in ledger['accepted']:
    reviewers=', '.join(sorted({e['reviewer'] for e in x['review_evidence']}))
    lines.append(f"| {x['claim_id']}@{x['version']} | {'A100 full reconstruction; ' if x['A100_full_reconstruction_this_stage'] else 'Recorded upstream review; '}{reviewers.replace('|','/')} |")
lines += ['', 'Theorem boundaries that govern continuation:', '',
          '- C005/C006 restriction and block identities, C018 equivalence, signed Boolean convolution, normalized complete-reference/Gibbs bounds and established structured classes retain their exact original hypotheses. C018 does not supply its missing universal constant.',
          '- A097 negative-cell source floor is conditional on its supplied source price. A096 finite no-reset transport and its A099 reconstruction preserve the SAME original account and every complete terminal. No individual descendant influence bound follows.',
          '- A099 v6 NR1/NR2/RS1/RS2 have scoped reviews, including A085. Both integrated-chain independent audits and all four universal conjectures remain open.',
          '- A094 all-padding h3*h2 signed-profile application is author-proved with exact finite checks and independent review pending. Its fixed core does not bound arbitrary signed profiles.',
          '- The A085 adverse reference reset is now independently accepted locally by A100. Absolute-TV proximity fails; exact weighted likelihood admission survives.',
          '- A100 stage4 Jensen refinement is not promoted to independent acceptance by this stage. Historical A021 v1 remainder-sign acceptance stays withdrawn; A008 singleton t=1/4 correction stays active.', '',
          'Every partial, disputed, withdrawn and unreviewed statement is listed with exact text and review evidence in the companion JSON. The failed-route archive retains earlier witnesses and adds the full-support TV/reset and inherited constant-child obstructions.']
(RUN/'RELEASE_INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
question_md=['# Next ten precise research questions','']
for x in q:
    question_md += [f"{x['priority']}. **{x['question_id']} ({x['bridge']})** — {x['exact_question']} Owners: {x['research_owners']}; independent review: {x['independent_reviewer']}. {x['first_unpaid_step_or_guard']}",'']
(RUN/'CONTINUATION.md').write_text('\n'.join(question_md),encoding='utf-8')
report=f'''# A100 release and continuation ledger — stage 16

## exact target, quantifiers, hypotheses and units

Prepare the accepted-theorem/review index, failed-route archive, proof status and next ten precise questions for full uniform-cube FEI. The target remains one finite dimension-independent C for every Boolean sign f on every finite cube, H(f)<=C I(f), entropy in bits and physical influence in flip-probability units. Full FEI remains OPEN. This stage independently reviews the complete original A085 reset-obstruction theorem for every integer n>=2, with actual Boolean signs, a cheap matching complete full-support root reference and two nonconstant children. It does not authorize public release. The current user deadline 2026-10-23 14:49 UTC supersedes the old protocol endpoint; no native schedule was changed.

## sources actually read, revisions and theorem locators

Read execution-v2 protocol in full; required canonical README/status/claim/obstruction/packet/next-action files and TeX plan; supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and every sources/*.md; saved earlier B05/B09/B19 reports; current BOARD, B20 v2 STREAM_NOTES and SYNTHESIS; own prior rolling state and real stages. Byte receipts cover 601 reads with no parse errors and all four supplied paper text exports (explicit cp1252 fallback for legacy exports). Text loading and theorem locators are recorded as context, not a fresh paper-proof audit. Threshold 38pp Theorems A–D, composition/selector/activation sections and percolation 30pp Theorems1.1–1.6/3.1/3.2/4.4 remain scoped baseline context; earlier versions are not substituted for current claims. No new literature priority assertion is made.

Critical new sources: A085 20261021T174013Z PROOF sections1–5 and original claim v1; A099 20261021T155354Z STAGE6_ADDITIONS NR1–NR3 and RS1–RS2; A096 20261014T094929Z DERIVATION1–4; A097 20261014T050248Z source-floor proof; A094 20261021T155244Z AUDIT and PROFILE_CERTIFICATE; original A095/A086 histories. Exact paths and hashes are in out/SOURCE_RECEIPTS.json and out/CRITICAL_SOURCE_RUNS.json. Read-only brain recall supplied no load-bearing theorem; it reported a failed automatic refresh spawn, not a successful research write. Wake warned of two stale personal-context notes and the user was alerted.

## complete derivation or exact first unsupported line

REVIEW.md gives an independent all-n reconstruction and accepts A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 at its complete unchanged original scope. For F_n negative exactly at0,1,3 on n+1 bits, t=2^-n, directional influences are t,t,3t,...,3t, so I=(3n-1)t and queried influence=t. Direct character sums prove full spectral support; both actual children are nonconstant. With matching Q, conditional refund is exactly zero. The inherited complete child law has qa=2t² and q0=1-6t+10t². Transfer qa(1-2^-M) from atom a to empty, M=2^(2n-2), in one child only. Complete normalized references stay positive and TV<2t², while expected signed reset bill is Z=[1-(1-2t)^2 log2(1+qa(1-2^-M)/q0)]/2>3/8 for all n>=2 and tends to1/2. The n=2 endpoint uses31/16<2; n>=3 uses ln(1+x)<=x, ln2>1/2, q0>=p0/2 and4qa<=1/8. An independent entropy bound gives H<=8I. Thus this is a reference-payment obstruction on a bounded-ratio Boolean family, never an FEI counterfamily. Minimality under full support plus two nonconstant children is reconstructed and checked in dimension two.

The synthesis retains the exact account: U=A-d-T, T=b+r+T', new terminal cost T'+Z, so final balance is U+r-Z. With additional channel/label bill L, admission is exactly Z+L<=U+r. A sufficient occupied-atom relative certificate is sum_leaf w[-log2(1-eta_leaf)]+L<=U+r when Qnew>=(1-eta_leaf)Qold. This is an implication, not the missing useful-reference construction. First unsupported universal line: choose useful prescribed references/history/resets for arbitrary Boolean signs and prove their complete weighted likelihood, all prior debits, both terminal debts and other new bills fit one influence-priced original account. No-reset marginalization is already paid conditional on the root price; it supplies neither a universal cheap root nor this reset admission.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json predates the mathematical checks. Independent code/check_reset_independent.py imports no author helper. Fixed pilot n=2,3:151 exact assertions PASS. Fixed full n=2..7, all sixteen labeled two-bit signs/both queries for minimality:1255 exact assertions PASS in9.239191s; pilot not added. Integer direct character sums are cross-checked against a separate butterfly transform, and physical directional edge counts against analytic influence. Fraction arithmetic checks actual full-support spectra, both nonconstant children, complete normalizers, unchanged complementary atoms, exact TV and positive logarithm denominators. Forty-term range-reduced rational atanh sums with a proved geometric tail certify the sign intervals. The analytic derivation, not six finite cases, establishes the all-n claim. Estimated helper memory80MB, peak unmeasured, fixed55s cap, no GPU or automatic dimension escalation.

Commands: python -X utf8 code/intake.py; code/check_reset_independent.py --pilot; the same checker without --pilot; code/prepare_ledger.py; code/ledger.py; code/finalize.py, all from this run (the invoked workspace-relative forms are equivalent). Source intake observed1065 claim records and zero parse errors; local run snapshot has1069 timestamp-marker-only folders and522 folders with all four protocol files. These are presence counts, not executed/successful/failed stage counts. A100 has11 marker-only folders after its last substantive October14 stage. Forty-two files from that real stage were rehashed. No full-payload execution or remote persistence is inferred from a marker or file count.

Fresh memok passed before the bounded core-only Lean attempt (physical free15.6GB, commit free24.6GB). The endpoint statement example:31<32 by decide reached RUNTIME_UNVERIFIED after the45s timeout; target identity, theorem kind and axioms were unverified. No Lean certification is claimed. The receipt is out/LEAN_ENDPOINT_RECEIPT.json. No Mathlib build was launched. The proof rung is analytic proof plus independent exact finite certificates.

## proof dependencies and changed downstream conclusions

RELEASE_INDEX.md and out/THEOREM_RELEASE_LEDGER.json contain {counts['accepted_statement_versions']} recorded full-scope statement groups, {counts['partial_statement_versions']} partial/disputed groups, {counts['pending_statement_versions']} groups without full independent acceptance and {counts['withdrawn_statement_variants']} withdrawn variant. These are versioned review-evidence groups, not newly proved theorem counts. No exact-statement/version collision or accepted hypothesis variant was found in the grouped snapshot. Only A085 v1 receives a new full A100 reconstruction; its original exact statement, hypotheses and statement hash are unchanged in local CLAIMS.json. All other upstream acceptances keep their exact scope. Canonical adoption is pending.

out/CORRECTION_PROPAGATION.json preserves the A096 plus-M report correction, B11 proper-block FEI equivalence, bounded-H/I minimum-coordinate calibration, A021 v1 remainder-sign retraction and A008 t=1/4 singleton correction. out/FAILED_ROUTE_ARCHIVE.json preserves earlier routes and adds the independently accepted absolute-TV reset failure and independently reviewed inherited-constant-child CE obstruction. A099 scoped no-reset/reset identities survive. The new A094 all-padding fixed-core profile remains review-pending. No whole A099 manuscript or universal bridge is declared proved; two integrated independent audits remain open. The universal constant improves by zero.

## one next mathematical action and independent reviewer

First action: A097/A096 specify one useful weak non-flat active descendant reset relative to the actual incoming negative-cell reference, and prove its signed Z plus channel/label bills fits the SAME measured U+r while preserving old debit and both full terminals. A094/A092 independently reconstruct that admission. CONTINUATION.md and out/NEXT_TEN_QUESTIONS.json give exactly ten nonduplicated, source-aware followups with owners, reviewers and first-unpaid-step guards. Existing workers only; no messages, schedules or new workers are created. A085/A094 remain the proposed independent reviewers of the integrated assembly, not presumed to have completed it.

## actual persistence receipts or precise save blocker

Local four-file protocol package, complete theorem index, review, ten-question handoff, frozen spec, code, original-source hashes and exact outputs are saved inside the assigned A100 run. out/PERSISTENCE_RECEIPTS.json verifies local byte readback, exact schemas, PROGRESS/PACKET_DELTA equality, original A085 statement preservation and20MB ceilings. Rolling STATUS has exactly two lines; WORKLOG/LEARNED are appended. No intentional research brain write, git, mail, foreign-folder mutation, trading access or public upload occurred. The required administrative wake/checklist helpers are separate from research persistence. No running work was stopped, suspended or throttled; all mathematical helpers and the bounded Lean attempt have completed.

Private supervisor copying, canonical index adoption, independent mirror readback, downstream mathematical use and new public release remain UNVERIFIED. Historical threshold-paper publication receipts are retained at commit b38ba0ab49618ccbe6d1518a34c141dcec9f247c; they are not fresh public readback of this private run. Configured, executed, locally saved, reviewed, privately mirrored and publicly released work are distinguished in out/PERSISTENCE_AND_RELEASE_STATES.json. Timestamp-only folders establish none of the mathematical completion states. This release ledger is a concrete proposed delta for the existing B20 canonical workflow, not a parallel registry.

## Universal bridge

C019 stopping-tree payment and the finite-tree C024 interface advance by one independently checked obstruction to an invalid reset-admission shortcut, with exact complete-reference and original-account scope retained. A085's all-n witness rules out absolute-TV proximity as a dimension-independent payment certificate even with a cheap full-support matching root and both nonconstant children; the quantitative gap is TV<2^(1-2n) versus reset bill>3/8 and queried influence2^-n. No universal constant or new arbitrary-core reference bound is supplied. What remains is useful weighted-likelihood/relative-atom reset admission, or a universally cheap initial complete reference, with every new bill and both terminal debts paid once. NEXT is the shortest route because it addresses this unpaid existence/payment line directly, while more root censuses, no-reset telescopes or bounded-ratio calibration would repeat already completed work.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
p={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B20','packet_id':'A100','gap_id':'C019-C024-SAME-ANCESTOR-RESET-ADMISSION','attempt_id':'A100-stage16-independent-reset-review-and-release-ledger','method':'Source/version census, complete-scope independent analytic reconstruction, direct integer Fourier and Fraction sign certificates','mathematical_delta':'A085 full-support absolute-TV reset obstruction independently accepted at unchanged full scope; exact same-bank weighted likelihood admission retained. Universal FEI constant improvement0.','deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF_REMOTE_ADOPTION_UNVERIFIED','mathematical_status':'FULL_FEI_OPEN_SCOPED_OBSTRUCTION_INDEPENDENTLY_REVIEWED','claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims]+[{'claim_id':'A096-PAID-FLOOR-NO-RESET-HISTORY','version':1,'scope':'elementary transport and conditional supplied floor; no whole-assembly acceptance'},{'claim_id':'A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK','version':1,'scope':'already reviewed supplied source price; not new A100 full reconstruction'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Local A100 full original-scope review appended; exact statement/hypotheses/hash unchanged'} for c in claims],'source_artifacts':['out/SOURCE_RECEIPTS.json','out/CLAIM_CENSUS.json','out/LOCAL_RUN_CENSUS.json','REVIEW.md','out/INDEPENDENT_RESET_REVIEW.json','out/THEOREM_RELEASE_LEDGER.json','out/FAILED_ROUTE_ARCHIVE.json','out/NEXT_TEN_QUESTIONS.json','out/PERSISTENCE_AND_RELEASE_STATES.json'],'next_consumers':['B20','A096','A097','A099','A085','A094','A092'],'next_action':q[0]['exact_question'],'stagnant_substantive_attempts':0,'blockers':['Useful arbitrary-core reset/source reference at an influence price is unproved.','Integrated A099 double audit remains open.','Supervisor private copy/canonical adoption/mirror/public release unverified.','Core Lean endpoint timed out; no formal certification.'],'packet_ids':['A100']}
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(p)==set(fields)
save(RUN/'PROGRESS.json',p);save(RUN/'PACKET_DELTA.json',p)
(A/'STATUS.md').write_text('STATE: A100 stage16 complete locally: A085 full-support reset obstruction independently HOLDS;1255 exact checks;160 recorded full-scope review groups;11 A100 marker-only stages;FEI OPEN.\nNEXT: A097/A096 pay useful weak non-flat reset plus other bills from SAME U+r with old debit and both terminals;A094/A092 review;supervisor copy/adoption unverified.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Stage16 consumed current board/B20 and1065 claim records; detected11 A100/1069 fleet marker-only folders versus522 four-file runs (presence only). Rehashed42 prior real-stage files. Independently reconstructed A085 full-support all-n reset obstruction;pilot151 and full1255 exact checks PASS in9.239191s. Core Lean endpoint timed out/unverified. Saved160 recorded full-scope groups,58 partial,403 pending,1 withdrawn; no fresh blanket proof acceptance. Saved ten same-bank questions and correction/failure/release states. No remote/shared research write or work stopped.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage16: A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 independently HOLDS at original full scope: actual F_n negative at0,1,3 has full support,both nonconstant children,H<=8I,I=(3n-1)2^-n; matching root gives refund0; normalized positive reset has TV<2^(1-2n) but weighted bill>3/8. This refutes absolute-TV admission,not FEI or useful reset existence. Exact criterion including any extra channel/label bill L is Z+L<=SAME U+r. Leafwise relative lower ratios give sufficient sum w[-log2(1-eta)]+L<=U+r; proving useful ratios remains unpaid. Timestamp-only .final folders are not completed mathematical stages;11 own later nominal stages have no four-file result. Count configured/executed/saved/reviewed/mirrored/released separately.\n')
# Read back actual saved payloads; avoid a self-referential checksum.
receipt=[]
for path in sorted(RUN.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json' and '__pycache__' not in path.parts:
        raw=path.read_bytes();assert len(raw)<20_000_000
        if path.suffix=='.json':json.loads(raw.decode('utf-8-sig'))
        receipt.append({'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for name in protocol['required_per_run']['report_fields']:assert '## '+name in report
for path in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
    raw=path.read_bytes();receipt.append({'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(OUT/'PERSISTENCE_RECEIPTS.json',{'saved_utc':now,'files':receipt,'four_protocol_files_validated':True,'progress_packet_delta_identical':True,'claim_schema_exact':True,'unchanged_original_A085_statement_hypotheses_hash':True,'all_files_under20MB':True,'local_readback':'PASS','remote_copy_mirror_review_public_release':'UNVERIFIED_NOT_INFERRED','full_FEI_status':'OPEN'})
print(json.dumps({'status':'LOCAL_PACKAGE_COMPLETE','files_receipted':len(receipt),'review':claims[0]['claim_id'],'assertions':check['exact_assertions'],'recorded_review_groups':counts,'remote_save':'UNVERIFIED','full_FEI':'OPEN'},indent=2))
