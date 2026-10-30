from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
old=R.parent/'20261022T220953Z-fleet03-A014-overlap-beyond-worst-case-read'
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
full=json.loads(read(R/'out/check.json'));ext=json.loads(read(R/'out/extension.json'));pilot=json.loads(read(R/'out/pilot.json'))
assert full['graphs']==249 and full['graph_queries']==1233 and ext['mass_pairs']==2077 and ext['adaptive_stopping_policies']==244
assert full['elapsed_seconds']<300 and ext['elapsed_seconds']<300 and pilot['elapsed_seconds']<60
prior=json.loads(read(old/'CLAIMS.json'))[0]
statement=prior['exact_statement']+' ADDITION AT VERSION 6: '+(
'For any finite uniform Boolean f and fixed reference q strictly positive on every nonempty Fourier set, set Q(empty)=fhat(empty)^2 and Q(S)=Var(f)q(S) otherwise. '
'For any queried coordinate i, both children inherit the SAME reference qbar(T)=[q(T)+q(T+i)]/[1-q({i})] on nonempty T outside i; only their actual empty/nonempty masses differ. '
'Their average FULL cross-entropy never exceeds CE(f,Q). Constants and one-bit cubes use the stated zero-sector conventions. '
'At every node delta=parent FULL CE-average child FULL CE is nonnegative. For EVERY finite adaptive restriction tree and stopping cut, sum reach*delta plus the full terminal CE expectation equals the ORIGINAL root CE. '
'References along histories are the original q projected off queried coordinates and conditioned nonempty, without fresh prime tables. '
'The exact excess-KL identity retains singleton debt, conditional phase cost, both child debts and the JS credit; original-reference phase asymmetry is explicit, not removed for free. '
'For every n>=3, let f_n=1-2 1_{independent sets of K_n}, lambda_e=1/(n-1), and q_n the normalized ORIGINAL complete edge-occupation mass from stage5. '
'With r=floor(k/2), F_(2r)=(2r)!/(2^r r!)*(lambda/48)^r and F_(2r+1)=(2r+1)!/(2^r r!)*(lambda/48)^r*lambda*(3n-2r-3)/96, '
'the original normalization is q_n(S)=F_|S|/sum_k binom(n,k)F_k; no normalizer is dropped. '
'The complete reference cross-entropy satisfies CE(f_n,Q_n)<=32 I(f_n), and consequently ALL adaptive histories/stopping cuts retain their full terminal costs and all delta bookings in the SAME ORIGINAL 32 I(f_n) account. '
'The positive edge DNF has unavoidable positive-DNF read n-1, hence overlap is unbounded. This is an original-reference coding result on an already known FEI threshold family, with no novelty claim for that FEI class. '
'The phase term alone cannot be bounded by constant times queried influence: on majority_(2k+1), its ratio equals 1/a_k-a_k, a_k=binom(2k,k)/4^k<=1/sqrt(k+1), so diverges. '
'The universal first unpaid line is the ORIGINAL normalized occupation cost on arbitrary overlapping graphs/linear hypergraphs; full FEI remains OPEN.')
claim=dict(prior);claim.update(version=6,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 hypotheses=prior['hypotheses']+['New full-CE transport: finite uniform Boolean cube; fixed complete positive nonempty reference; both terminal references projected from that SAME q.','Clique cost: n>=3, ORIGINAL fixed lambda=1/(n-1) complete edge-occupation factors; all empty/nonempty and full normalization costs retained.','Tree bookings are actual FULL-CE decreases, not claimed equal to true entropy decrements.'],
 proof_source={'prior_version_source':str(old/'CLAIMS.json'),'new_proof':str(R/'DERIVATION.md'),'locators':['equations (9)-(11): paid projection/calibration full-reference supermartingale','equations (12)-(14): full original clique payment','phase-to-local-influence obstruction'],'certificates':[str(R/'out/check.json'),str(R/'out/extension.json')]},
 proof_dependencies=[{'claim_id':prior['claim_id'],'version':5,'scope_used':'Earlier bundled results retained; stage5 complete occupation definition is independently reduced to clique closed masses here.'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':prior['claim_id'],'version':5}],
 refutes=prior['refutes']+[{'statement':'conditional phase cost Phi_i <= K Inf_i with universal K, even selecting a relevant coordinate','witness':'Every coordinate of majority_(2k+1): Phi_i/Inf_i=1/a_k-a_k tends to infinity','scope':'local phase payment only; not the full-CE original-account identity or FEI'}],
 first_unproved_line='Bound the ORIGINAL normalized complete occupation expectation by dimension-independent influence on arbitrary overlapping graphs/linear hypergraphs; clique matching multiplicities cannot be assumed for arbitrary induced subgraphs.',
 next_consumers=['A008','A009','A015','A086','A094','B03'])
dump(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A014','gap_id':'A014-ARBITRARY-OVERLAPPING-BLOCKER-REFERENCE-COST','attempt_id':'A014-stage18-original-reference-projection-and-clique-payment',
'method':'Exact paired Fourier marginal, full-reference CE supermartingale, complete matching occupation sum, rational log/sign certificates and ALL triangle stopping policies',
'mathematical_delta':'General SAME original-reference full child-CE transport with no renewal; K_n complete original occupation cost<=32I for all n>=3 and all histories/cuts. Local phase-to-query-influence bound refuted by odd majority. Full FEI OPEN.',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATES; REVIEW_PENDING; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':prior['claim_id'],'version':5}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':6}],
'source_artifacts':[str(old/'DERIVATION.md'),str(R/'DERIVATION.md'),str(R/'FROZEN_SPEC.json'),str(R/'FROZEN_EXTENSION.json'),str(R/'out/check.json'),str(R/'out/extension.json')],
'next_consumers':['A008','A009','A015','A086','A094','B03'],
'next_action':'Independently reconstruct clique matching/full-normalizer payment and universal paid projection/calibration CE projection; extend original occupation mass lower bound to a nonexchangeable linear-hypergraph family without replacing inherited terminal references.',
'stagnant_substantive_attempts':0,'blockers':['Universal original occupation expectation unpaid','Independent review and supervisor copying unverified','Lean compute admission held; no compiler launched'],'packet_ids':['A014']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# A014 stage18: complete original-reference payment with unbounded overlap

## exact target, quantifiers, hypotheses and units

For EVERY n>=3, pay the entire ORIGINAL fixed edge-occupation reference for f_n=1-2 1_{{independent sets of K_n}}, lambda_e=1/(n-1), including the complete normalizer and empty branch: CE(f_n,Q_n)<=32 I(f_n). Every variable has necessary positive-DNF read n-1. For ANY finite Boolean cube and positive complete nonempty reference, prove full child-reference CE transport using the SAME projected original reference for both children. On the clique family, ALL adaptive histories and stopping cuts, full terminal costs and actual CE-decrease bookings fit in the SAME original32I account. Bits; ideal probability cross-entropy. This is a coding payment for an already known threshold FEI class, not a new claim of full FEI.

## sources actually read, revisions and theorem locators

BOARD.md dated 2026-10-23 03:14 UTC, B02/B03 sections; B03 STREAM_NOTES v2; own STATUS/LEARNED and stage17 interface; stage5 exact occupation helper. Read A008 20261023T024024 REPORT: central thresholds on two disjoint blocks, all-prime reference lambda=1/N,251I/5; read A015 20261022T231544 REPORT: rare high-threshold products,96I. Those are distinct from the complete-graph edge table and scalar matching multiplicities used here. No theorem of theirs is assumed in the proof. Execution protocol revision2026-10-11-execution-v2 and initial campaign/paper reads remain inherited from this session. No external priority or novelty claim is made. The clique mass definition is independently reconstructed from the saved stage5 helper's exact factors.

## complete derivation or exact first unsupported line

DERIVATION.md equations(1)-(8) retain root debt, proper-pair child KL, phase cost and JS credit. Equations(9)-(11) give a stronger paid projection/calibration result for FULL CE: parent cost minus average complete child cost is nonnegative. Iterating only projects the SAME original q off queried coordinates and conditions it on a nonempty image; it does not replace it with a child spectrum or retuned table. Every stopping cut telescopes exactly with old delta bookings retained.

Equations(12)-(14) prove the all-n complete clique payment. Maximal matchings give closed F_k=D M_k, sum of all even/odd matching events bounds the FULL normalizer, and factorial/log inequalities give log(1/q(A))<=41n/6. The actual physical influence pays the full entropy wrapper plus all nonempty reference costs, yielding32I. No entropy bound is borrowed to pay the reference. Previous9I/2 was an ADDITIVE CONVERSION-EXCESS bound with unpaid row debt;32I here bounds the ENTIRE original reference cost on the clique family. They concern different quantities and scopes.

The candidate local phase payment fails: for odd majority every relevant coordinate has phase/Inf=1/a_k-a_k ->infinity, a_k=binom(2k,k)/4^k. The central-binomial estimate is proved by an exact induction. This does not refute the global account or FEI.

First unsupported universal line: lower-bound the ORIGINAL complete occupation mass sufficiently on arbitrary overlapping graphs/linear hypergraphs. The clique induced-subgraph matching multiplicity used in(12)-(13) is unavailable there. Delta here is a FULL reference-CE decrease; it is not claimed to equal true entropy decrement or arbitrary application-specific witness debt.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the pilot. Pilot:256 Boolean truth tables on3 bits, every queried coordinate, plus the earlier triangle epsilon=2^-64 reference: {pilot['assertions']} assertions in {pilot['elapsed_seconds']:.6f} seconds. The first strict full attempt found interval dependency at exact gap=w=0 when subtracting two separately enclosed identical CEs. The repaired checker evaluates the signed pair-log formula directly and cross-checks the CE subtraction; no graph cases ran in that failed attempt. Final sign tests have NO tolerance guards. Details are preserved in out/ATTEMPTS.txt.

Final full checker: same768 Boolean queries and one triangle reference; all1096 candidate labelled graphs n=3,4,5, selecting249 connected cut-free graphs and ALL1233 queried vertices. {full['assertions']} exact assertions PASS in {full['elapsed_seconds']:.6f} seconds. Constants, zero/constant child branches, identical and nonnested rows, both complete terminals, full normalizers, singleton debt, signed reference change, child KL and JS are retained. Code checks the FULL CE inequality as well as the excess identities. Integer FWHT, exact Fraction masses, rational outward log intervals with analytic atanh remainder; no floating-point sign evidence is promoted.

FROZEN_EXTENSION.json precedes the analytic-extension job. Closed-form masses checked for2077 fixed(n,k) pairs n=3..64; no truth-table dimension is increased. Direct occupation enumeration agrees with the closed formula on all53 nonempty clique sets n=3,4,5. Spectral mass, influence and integer-power scalar inequalities are exact. Fourteen complete scalar CE certificates cover n=3..16. ALL244 adaptive stopping/query policies on the triangle telescope the ORIGINAL account; their probabilities use independent direct character sums rather than FWHT. Extension: {ext['assertions']} assertions PASS in {ext['elapsed_seconds']:.6f} seconds. Finite checks support the separately supplied all-n proof; they do not establish universal FEI.

Commands from A014: `python -X utf8 runs/{R.name}/code/check.py --pilot`; same without `--pilot`; `python -X utf8 runs/{R.name}/code/extension.py`. Outputs out/pilot.json, out/check.json, out/extension.json and checkpoint. Estimated memory100MB; jobs sequential and each under300seconds; no >300MB job, GPU or automatic dimension escalation. Lean scalar Walsh-square identity was attempted; admission returned SETUP_UNVERIFIED before any compiler launch. No retry. Rung: proof with exact certificates, NOT Lean-checked; independent peer review pending.

## proof dependencies and changed downstream conclusions

A014 bundled claim advances5->6, without opening another broad candidate. The new projection identity and clique all-n bound are self-contained from the explicit occupation factors. Normalization uses a direct matching-polynomial sum; it does not assume the queue subprobability theorem or discard its normalizer. The source's full raw queue interpretation and physical prefix rounding retain their prior status; the new theorem concerns the exact normalized ideal reference CE. A014's original arbitrary-row coefficient-one EXCESS obstruction is not contradicted: full CE is transported with the singleton and original phase costs explicit.

## one next mathematical action and independent reviewer

A086/A094 should reconstruct the full-original-reference monotonicity and both normalizer inequalities independently. A008/A009/A015 should inspect the clique occupation formula and use the projection invariant with their paid original references. NEXT: obtain a comparable original-mass lower bound on a nonsymmetric linear-hypergraph family; retain both complete terminal references and the old delta bookings. No review message or acceptance is asserted. The new graph calculation does not duplicate B02's deleted bipartite graphs or A008/A015's threshold-product prime tables.

## actual persistence receipts or precise save blocker

The four protocol files, complete derivation, two frozen specifications, checker, extension and exact outputs are saved locally. out/RECEIPTS.json checks exact protocol field sets, identical progress/delta copies, statement hash, file sizes and SHA256, including the inherited helper dependency. Rolling STATUS has two lines; WORKLOG and LEARNED are current. Independent review, supervisor copying, remote/mirror persistence and downstream adoption remain unverified. No git, messages, outside research writes, trading process, background service or deletion. Brain self-care remains degraded: stale personal-model/state-of-mind notes were not used for mathematics.

## Universal bridge

C020 advances from unpaid row-reference conversion to a COMPLETE original edge-occupation payment<=32I on the unbounded-read clique family, and C019 gains an exact paid projection/calibration FULL-reference projection account covering every adaptive history/stopping cut on that family with both terminals and old delta bookings retained. This is not universal FEI and does not identify delta with true entropy decrement. The first unpaid step is the original occupation-mass bound beyond clique matching multiplicities. NEXT attacks that same full-cost bottleneck on nonsymmetric overlap, using a transport invariant that now works on every Boolean cube, so it can feed a universal witness proof instead of only another entropy calculation for a known class.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md',f'STATE: A014 stage18 saved: ORIGINAL K_n occupation CE<=32I, ALL adaptive histories paid SAME root; universal full-CE projection proved; {full["assertions"]}+{ext["assertions"]} exact checks PASS; review pending; FEI OPEN.\nNEXT: A086/A094 review paid projection/calibration projection/matching normalizer; extend original-mass payment to nonsymmetric overlap with both full terminals and old delta bookings.\n')
now=datetime.now(timezone.utc).isoformat()
write(A/'WORKLOG.md',read(A/'WORKLOG.md')+f'\n{now} Stage18: exact FULL-CE projection removes prior row-debt amplification at full reference level while retaining root/phase costs. Original edge-occupation K_n cost<=32I all n>=3; ALL adaptive/stopping histories funded once by root CE. {full["assertions"]}+{ext["assertions"]} exact final checks; 244 policies; strict interval-zero issue repaired by direct pair-log sum; Lean held before compiler. Full FEI OPEN; general original occupation expectation remains unpaid.\n')
write(A/'LEARNED.md',read(A/'LEARNED.md')+'\nStage18: FULL CE, unlike excess KL alone, is nonincreasing in expectation under a query if both child references inherit qbar(T)=[q(T)+q(T+i)]/[1-q({i})] and actual child empty masses. Parent CE=three-sector root CE+w CEproper+original conditional phase CE. Root CE>=h(w)>=avg h(vb); phase CE>=0. Thus delta=parentCE-avg childCE>=0; every finite adaptive stopping tree telescopes delta bookings plus full terminals to ONE original CE. This does not say delta=true entropy decrement. K_n original edge occupation lambda1/(n-1): F2r=(2r)!/(2^r r!)(lambda/48)^r; F2r+1=(2r+1)!/(2^r r!)(lambda/48)^r lambda(3n-2r-3)/96; q=Fk/sum binom(n,k)Fk. Matching polynomial gives log Z_F<=n/12, log1/Fk<=27n/4, so log1/q<=41n/6. With v/I<=4/n and h(v)<=7nv/6, full originalCE<=32I for all n>=3 and all histories retain old delta debits. This is original-reference payment for a known threshold FEI family, no new universal FEI claim. Odd majority: phase/Inf=1/a_k-a_k unbounded, so local phase charge cannot be renewed per query. General nonsymmetric original occupation cost remains the unpaid line.\n')
protocol=json.loads(read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len(read(A/'STATUS.md').splitlines())==2
assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
receipts={'saved_at_utc':now,'protocol_fields':'PASS','progress_delta_equal':True,'statement_sha256':'PASS','peer_review':'pending','remote_persistence':'unverified','lean':'SETUP_UNVERIFIED; no compiler started','source_dependencies':[],'files':[]}
helper=R.parent/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
receipts['source_dependencies'].append({'path':str(helper),'sha256':hashlib.sha256(helper.read_bytes()).hexdigest()})
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts['files'].append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(R/'out/RECEIPTS.json',receipts)
for item in receipts['files']:assert hashlib.sha256((R/item['path']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'protocol_fields':'PASS','graphs':249,'main_assertions':full['assertions'],'extension_assertions':ext['assertions'],'policies':244,'files':len(receipts['files']),'full_fei':'OPEN'}))
