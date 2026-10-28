from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
run=Path(__file__).resolve().parents[1];agent=run.parents[1]
protocol=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
p=json.loads(protocol.read_text(encoding='utf-8-sig'))
def read(name):return json.loads((run/'out'/name).read_text(encoding='utf-8'))
v=read('VALIDATION.json');pilot=read('PILOT.json')
mixed=read('MIXED_VALIDATION.json') if (run/'out/MIXED_VALIDATION.json').exists() else None
poly=read('POLYNOMIAL_CERTIFICATES.json') if (run/'out/POLYNOMIAL_CERTIFICATES.json').exists() else None
complete=mixed is not None and poly is not None
assert v['status']=='PASS'
if complete:assert mixed['status']==poly['status']=='PASS'
now=datetime.now(timezone.utc).isoformat()
def write(path,s):path.write_text(s,encoding='utf-8',newline='\n')
def js(path,obj):write(path,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
statement=('Retains A024-MIXED-FACE-ORDER-OBSTRUCTION@2 and extends it as follows. For every pair of disjoint Boolean uniform-cube functions w,h, binary activation F=1-(1-w)(1-h)/2, and every fair physical core query, the exact lifted controller-prefix update is average C_child=C_parent-d_core*P_oldbad/2+signed migration, retaining original reaches and both full terminal spectra. Its complete signed scalar erasure remainder satisfies R_r(a,beta)<=9*r*Inf_x(w), including deterministic r=0,1. For any two prescribed complete component trees and K0, put Phi=r*Qw+t*Qh+(Ih*Pw+Iw*Ph-Pw*Ph)/2, where Q and P are own-K0-bad odd-face and pivot subtree accounts. Every respecting adaptive interleaving and stopping cut obeys actual-(K0+9)-bad bill+E Phi_terminal+D_unused=Phi_root, with D_unused>=0 as in DERIVATION.md. A root-only price Phi<=C I(F) for EVERY prescribed component-tree pair with individually paid own-bad Q is false on the inherited tensor seeds: Phi/I=4/37+73L/1184. This does not rule out selecting other component trees. A universal net price after unused releases and full FEI remain open.')
claim={
 'claim_id':'A024-MIXED-FACE-ORDER-OBSTRUCTION','version':3,'exact_statement':statement,
 'hypotheses':['Disjoint finite Boolean physical blocks; uniform untouched coordinates; entropy in bits','F is precisely the binary activation gate stated, not an arbitrary outer gate','Component trees fixed before interleaving; next component coordinate follows its prescribed subtree; block choice may depend on all actual revealed history','Both terminal spectra retained; deterministic output cases contracted without variance division','For the entropy corollary K0>=log2(e); algebraic potential identity valid for all real K0'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A024'], 'proof_source':str(run/'DERIVATION.md'),
 'proof_dependencies':['A024-MIXED-FACE-ORDER-OBSTRUCTION@2 (inherited tensor witness and reconstructed local face/erasure identities)','A024-BIASED-CHILD-TRANSPORT@1 (empty-sector convention, reconstructed here)','B05-ODDFACE-LOCALIZED-REDUCTION@1 only for the explicitly conditional entropy corollary'],
 'review_records':[{'kind':'author exact verification','status':'PASS','source':'out/VALIDATION.json','scope':'3072 actual Boolean first-core queries; 242376 exact assertions; no nonzero actual mask migration in this family'},{'kind':'Lean attempt','status':'SETUP_UNVERIFIED','scope':'No compiler started; admission held for hung-window/under-5500-MB condition; no formal certification claimed'}],
 'status':'AUTHOR_PROOF_COMPLETE_REVIEW_PENDING' if complete else 'AUTHOR_DERIVATION_VALIDATION_IN_PROGRESS',
 'supersedes':['A024-MIXED-FACE-ORDER-OBSTRUCTION@2 (extension; original results preserved)'],
 'refutes':['Universal root-only Phi<=C I(F), even when both component own bad-Q/I ratios are 4/37'],
 'first_unproved_line':'Choose useful component trees and a respecting adaptive interleaving whose net Phi_root-D_unused is O(I(F)), with full terminals, and supply a universal decomposition/transfer beyond this binary disjoint interface.',
 'next_consumers':['A021','A023','A025','A028','A029','A087','A094','B05','B20']}
if complete:
 claim['review_records'].append({'kind':'author mixed-history verification','status':'PASS','source':'out/MIXED_VALIDATION.json','scope':f"{mixed['local_steps']} local steps and {mixed['memoized_bellman_states']} Bellman states; implementation reproduction, not independent review"})
 claim['review_records'].append({'kind':'rational polynomial certificate','status':'PASS','source':'out/POLYNOMIAL_CERTIFICATES.json','scope':'Three universal polynomial normal forms vanish; logarithm estimate remains analytical'})
eqfields=set(p['required_per_run']['claim_fields']);assert set(claim)==eqfields
js(run/'CLAIMS.json',[claim])
nextaction='Select a block policy to redeem the SAME unused releases D_T against mixed bad-pivot exposure on a growing-module pair; retain both complete terminal spectra and original component subtrees; A087/A094 independently review v3.'
progress={
 'protocol_revision':p['revision'],'run_id':run.name,'stream':'B05','packet_id':'A024',
 'gap_id':'G-R-SELECT','attempt_id':'A024-stage17-first-core-query-overlap-rebate',
 'method':'Analytic scalar log bound; exact signed child-mask update; single-use two-tree potential with overlap subtraction; exact physical Walsh replay and polynomial normalization',
 'mathematical_delta':'R<=9*r*d pays complete binary-activation mean remainder; exact first-core migration/release; all-interleaving account badbill+terminal Phi+unused releases=original Phi; root-only price obstructed, net-price selection open.',
 'deliverable_status':'COMPLETE_LOCAL' if complete else 'IN_PROGRESS',
 'mathematical_status':'AUTHOR_PROOF_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A024-MIXED-FACE-ORDER-OBSTRUCTION@2','A024-BIASED-CHILD-TRANSPORT@1','B05-ODDFACE-LOCALIZED-REDUCTION@1'],
 'claims_created_or_changed':['A024-MIXED-FACE-ORDER-OBSTRUCTION@3'],
 'source_artifacts':['DERIVATION.md','out/SOURCE_RECEIPTS.json','out/VALIDATION.json','out/MIXED_VALIDATION.json','out/POLYNOMIAL_CERTIFICATES.json'],
 'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['Universal net mixed-pivot payment and useful decomposition remain open','Independent A087/A094 review pending','Lean compute admission held; no formal certificate','Supervisor remote copy/mirror unverified'],
 'packet_ids':['A024']}
fields={s.split(' (')[0] for s in p['required_per_run']['progress_fields']};assert set(progress)==fields
js(run/'PROGRESS.json',progress);js(run/'PACKET_DELTA.json',progress)
mixedtext=(f"Mixed-history replay PASS: {mixed['local_steps']} local steps, {mixed['active_bad_steps']} active bad costs, {mixed['exact_assertions']} exact assertions, {mixed['memoized_bellman_states']} memoized Bellman states in {mixed['runtime_seconds']:.4f}s. K0=-5 exercises actual K4 costs; K0=4 checks the two nonzero designated component accounts at actual K13. The negative threshold is an algebra stress test, not a claimed FEI constant." if mixed else 'Mixed-history replay remains pending.')
polytext='Three rational-polynomial normal forms vanish exactly (potential debit, first-core frozen-mask release, union overlap rebate).' if poly else 'Polynomial replay pending.'
js(run/'out/EXECUTION_NOTES.json',{'brain_wake':'WARN: owner model/state-of-mind stale; current task and source files used instead','lean_attempt':{'status':'SETUP_UNVERIFIED','output':'Compute admission held (hung window or under 5500 MB free); no new compiler process','compiler_started':False},'corrected_infrastructure_failures':['Discovery FileNotFoundError before out existed; added mkdir and reran same domain','Source intake UnicodeDecodeError on legacy source; explicit cp1252 fallback with per-file encoding receipt, reran','Polynomial checker shadowed class P with a symbolic variable; renamed variable, reran same three identities'],'mathematical_assertion_failures':0,'stopped_processes':[]})
report=f'''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage extends the existing A024 interface through the first actual core query and then through every respecting adaptive interleaving of two prescribed component trees. Physical untouched inputs are uniform; only actual independent child outputs bias the binary outer gate. All entropy is in bits. The complete signed binary-activation mean remainder has the universal local upper price R<=9r*d. A single original two-tree account, including its negative overlap term, survives arbitrary mixed histories without renewal. The net mixed-face payment remains open.

# sources actually read, revisions and theorem locators

Read machine AGENTS.md, full EXECUTION_PROTOCOL.json revision {p['revision']}, BOARD.md snapshot 2026-10-22 22:17 UTC, own STATUS/WORKLOG/LEARNED, and unchanged B05 STREAM_NOTES v2. Read B05 lead run 20261011T225000Z REPORT.md, Lemmas1-2 and Theorem4; own productive 20261014T025222Z and 20261014T055140Z reports and latest full DERIVATION.md. Read canonical README/CURRENT_STATUS/claim-obstruction-packet registries/next actions/plan, supplement campaign/claims/counterexamples/seeds/mapping and packaged sources. Source intake records byte hashes and explicit legacy decoding where UTF-8 is rejected. The four supplied manuscript texts are loaded and their relevant composition/restriction context inspected; no new theorem from their unrelated percolation sections is used. Threshold corrected FEI+ has no output-variance numerator; physical H=Eplus+e(mean^2). Source intake and focused excerpts, not an independent complete re-audit of all manuscript proofs, are the scope of this reading. The live board shows A023/A028/A029 already carrying inherited banks; their newer theorems are not assumed from status snippets. Math recall returned general route guards, not a proof of this new lemma.

# complete derivation or exact first unsupported line

DERIVATION.md gives equations(A)-(G) with proofs. The first core query changes r,J to two actual r_b,J_b; averages are r and J-d. Its exact controller-prefix bill is C-d P_oldbad/2+M, where M is the SIGNED child-mask migration and preserves original reaches p_v/2. Both active terminals are h_0,h_1 with weights t/2, including their full H,I,Q.

The scalar inequality ln(1+s^2)<=s follows because the derivative of s-ln(1+s^2) is (s-1)^2/(1+s^2). Thus L(u,b)<=2|ub|/ln2, and the exact signed R is at most (6/ln2)r|b|<=9r*d. This keeps the negative empty-sector subtraction in the identity and drops it only in a stated upper bound. No variance or mean is divided out. Every lifted (K0+9)-bad controller node must already be own-K0-bad.

Write Q_w,P_w and Q_h,P_h for the original prescribed subtree own-bad odd-face and pivot accounts. The nonnegative potential is Phi=r Q_w+t Q_h+(I_h P_w+I_w P_h-P_w P_h)/2. At a w query its exact debit is e_w(r q_w+I_h d_w/2)+(1-e_w)P_h d_w/2; the h formula is symmetric. Therefore actualbadbill+E Phi_terminal+D_unused=Phi_root for every respecting adaptive interleaving/stopping cut. The overlap subtraction prevents double charging a pair designated bad in both blocks. D_unused includes good-query releases and own-bad queries that become good after lifting. All are debits of the same source account.

On the inherited tensor seeds, Phi/I=4/37+73L/1184, so a universal root-only price is false even though the component own-bad Q/I is 4/37. Actual controller-first K13 trees are good on this fixed-module family, and their unused releases redeem the oversized account. This is not an FEI counterfamily. First unsupported line: choose trees and a policy with NET Phi_root-D_unused=O(I(F)), retaining both full terminals; full FEI also needs a universal useful decomposition or transfer beyond disjoint binary activation.

# executed validation with domain, arithmetic, commands and outputs

Frozen discovery/validation/mixed specifications precede their jobs. `python -X utf8 .../code/check.py --pilot` PASS: {pilot['cases']} queries, {pilot['exact_assertions']} exact assertions in {pilot['runtime_seconds']:.4f}s. Full `python -X utf8 .../code/check.py` PASS: {v['cases']} actual first-core queries (four signed five-bit selector modules, every three-bit core, all three core coordinates), {v['exact_assertions']} exact assertions, {v['distinct_sign_certificates']} distinct rigorous signs, {v['runtime_seconds']:.4f}s. Integer Walsh, Fraction influence/face/reach accounts and rational prime-log vectors are exact; signs use rational atanh tails, including correct negative interval endpoints. Full physical spectra/derivative products independently check both root-block transport identities. All child masks are recomputed. This seed domain has ZERO nonzero mask migrations; the general migration formula is an algebraic proof, not an observed crossing. No claim of a realized threshold-crossing witness is made.

`python -X utf8 .../code/mixed.py`: {mixedtext} `python -X utf8 .../code/polynomial.py`: {polytext} These are separate mathematical representations by A024, not independent-agent acceptance.

Discovery-only float scan found no K4 crossing among the 32 signed bent/one-flip modules and 32 r values. It proves no impossibility beyond that domain. The first discovery write failed because out/ did not yet exist; the first intake hit an explicitly non-UTF-8 legacy text; the first polynomial run shadowed its polynomial class with a symbolic variable. These infrastructure errors were fixed and rerun on unchanged mathematical domains. out/EXECUTION_NOTES.json records them; none is a mathematical counterexample or successful check. No failed mathematical assertion occurred.

The required lean_check.py attempt returned SETUP_UNVERIFIED: compute admission held (hung window or under 5500 MB free), and no compiler started. Rung: analytical AUTHOR PROOF plus exact finite/polynomial certificates; NOT Lean-checked or independently accepted. The proposed Lean statement only encodes the frozen-mask averaging identity, so even a pass would not certify the log bound or theorem scope. Estimates are <=100 MB per math job, below the 300 MB gate; no measured peak memory claimed. Pilot under60s, full cap300s, mixed cap60s; fixed domains, no escalation/GPU/detached work. Main and mixed jobs run sequentially.

# proof dependencies and changed downstream conclusions

This is v3 of the existing candidate, not a new broad unreviewed candidate. Earlier K4 lift obstructions and K7 fixed-module repair survive. Local erasure and odd-face identities are reconstructed directly, and only the conditional entropy corollary uses the B05 localized reduction. No new manuscript theorem or unreviewed board assertion is imported. Changed conclusion: for binary activation, the complete scalar mean remainder itself has a uniform influence price. What needs additional credit is net mixed bad-pivot exposure after actual unused releases. Fixed-mask propagation with overlap rebate works through all respecting interleavings, but demanding its raw root bank be O(I) is demonstrably too strong. No arbitrary outer-gate or full-FEI payment follows.

# one next mathematical action and independent reviewer

{nextaction} In particular, use a selected early GOOD query to collect P_other*d/2 from the original bank and retain its complementary terminal. Price only the residual actual lifted-bad exposure; do not reintroduce the refuted raw-root price. A087/A094 should reconstruct the scalar estimate, overlap sign, branch weights, deterministic endpoints and all-interleaving telescope.

# actual persistence receipts or precise save blocker

The four protocol files, full derivation, fixed specs, code and exact outputs are local in the assigned A024 run. PROGRESS and PACKET_DELTA have identical fields and packet_ids=[A024]; CLAIMS has exactly protocol claim keys. out/PERSISTENCE_RECEIPTS.json records file hashes and sizes after writing; every file is below20MB. Rolling STATUS stays two lines, WORKLOG is dated, LEARNED retains precise conclusions. Local deliverable is {'complete' if complete else 'in progress'}. Supervisor copy, remote mirror, downstream adoption and independent acceptance remain unverified. No git/mail/brain writes or another agent's files are part of this mathematical stage.

# Universal bridge

This stage moves C024 history transfer into C019/B05 localized odd-face payment: the exact first-core signed mask update and one nonrenewing two-tree potential retain both full terminals through arbitrary respecting interleavings, while R<=9r*d pays the complete binary-activation mean-log remainder. The remaining universal credit is NET mixed bad-pivot exposure after unused good-query releases; a raw root-only bank is refuted by the same inherited tensor family. NEXT is the shortest route because it targets that precise unpaid policy-dependent debit with one original influence owner, rather than expanding a finite class or renaming FEI as an unpriced potential.
'''
write(run/'REPORT.md',report)
if complete:
 write(agent/'STATUS.md',f'STATE: A024 v3 saved: R<=9r*d; exact first-core migration and all-interleaving overlap-rebate bank; {v["exact_assertions"]}+{mixed["exact_assertions"]} exact assertions PASS; review pending, Lean held, FEI OPEN.\nNEXT: Redeem SAME unused good-query releases against net mixed bad-pivot exposure with both terminals; raw root Phi/I grows 73L/1184; A087/A094 review v3.\n')
 with (agent/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as fh:fh.write(f'\n{now} — Stage17: exact first-core migration/release, complete binary R<=9r*d, original two-tree union bank with -Pw*Ph/2 and signed unused releases. Full {v["cases"]}/{v["exact_assertions"]} PASS {v["runtime_seconds"]:.3f}s; mixed {mixed["local_steps"]}/{mixed["exact_assertions"]} PASS; 3 polynomial identities PASS. Lean admission held, no compiler. No actual mask migration in frozen domain. Net mixed credit and FEI remain open; v3 review A087/A094 pending.\n')
 with (agent/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as fh:fh.write('\n2026-10-23 stage17: For binary activation only, full signed erasure remainder R_r(a,b)<=9*r*d follows from ln(1+s^2)<=s and |b|<=d, with deterministic endpoints. Arbitrary outer gates are not covered. One actual core query gives avg controller bad bill=C-d*P_old/2+signed mask migration; retain original reaches and both t/2 terminals. For fixed component trees, Phi=rQw+tQh+(Ih*Pw+Iw*Ph-Pw*Ph)/2 obeys exact actual-(K0+9)-bad bill+terminal Phi+unused releases=original Phi for ALL respecting adaptive interleavings. The overlap subtraction is necessary. On old tensor seeds Phi/I=4/37+73L/1184, so price NET Phi minus unused releases, not the refuted raw root bank. Full FEI and useful general decomposition remain open.\n')
receipts=[]
for f in sorted(run.rglob('*')):
 if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json':
  data=f.read_bytes();assert len(data)<20_000_000
  receipts.append({'path':str(f.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
js(run/'out/PERSISTENCE_RECEIPTS.json',{'at':now,'files':receipts,'remote_copy':'UNVERIFIED'})
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print(json.dumps({'complete_local':complete,'protocol_keys':'PASS','files_hashed':len(receipts),'run':str(run)}))
