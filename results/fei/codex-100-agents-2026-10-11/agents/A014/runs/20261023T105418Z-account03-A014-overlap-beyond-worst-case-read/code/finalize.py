from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
old=R.parent/'20261023T032009Z-account03-A014-overlap-beyond-worst-case-read'
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
full=json.loads(read(R/'out/check.json'));scalar=json.loads(read(R/'out/scalar.json'))
ind=json.loads(read(R/'out/independent.json'));obs=json.loads(read(R/'out/obstruction.json'));pilot=json.loads(read(R/'out/pilot.json'))
assert full['candidates']==1059 and full['selected_graphs']==803 and full['sets']==26589
assert full['theorem_graphs']==5 and full['full_child_queries']==35 and full['elapsed_seconds']<300
assert scalar['scalar_n_d_k_cases']==173728 and scalar['elapsed_seconds']<300
assert ind['graphs']==5 and ind['nonempty_sets']==859 and ind['elapsed_seconds']<300
assert obs['actual_Boolean_inputs']==65792 and obs['elapsed_seconds']<60 and pilot['elapsed_seconds']<60
prior=json.loads(read(old/'CLAIMS.json'))[0]
statement=prior['exact_statement']+' ADDITION AT VERSION 7: '+(
'For EVERY simple graph G on n>=4 vertices with complement maximum degree d and n>=4(d+1), let f=1-2 times its independent-set indicator, '
'v=Var(f), and keep the ORIGINAL complete edge-occupation reference with fixed lambda_e=1/(n-1), original J(a,b)=a!b!/[(a+b+1)^2(a+b+2)], and FULL normalization. '
'Define kappa_def=(d+1)(log2(n)+20)/(I(f)/v), where I/v is the mean nonempty Fourier-set size. Then the ENTIRE ideal reference cross-entropy satisfies CE(f,Q)<=(24+kappa_def)I(f). '
'If (d+1)(log2(n)+20)<=n, then kappa_def<=4 and CE<=28I. The missing graph is otherwise arbitrary; no clique symmetry is assumed. '
'For every integer m>=6, n=2^m and d=floor(n/(m+20))-1, the complement star K_(1,d) plus isolated vertices gives an explicit nonsymmetric family with d tending to infinity, necessary positive-DNF maximum read n-1, and complete ORIGINAL CE<=28I. '
'All adaptive restriction trees and stopping cuts retain BOTH complete projected/calibrated terminal references and ALL previous actual full-CE-decrease bookings in this SAME original root account, by the version6 identity; no child density assumption or bank renewal is used. '
'The proof establishes F(A)>=r0! [lambda/48]^(r0+d+1) [lambda*delta/48]^(2d+2), r0=max(0,floor((|A|-2d-1)/2)), '
'and independently bounds the ENTIRE Z_F=sum F by exp(n/8). This raw-mass upper bound actually holds for every simple graph n>=2 at FIXED lambda=1/(n-1), allowing zero atoms; no density hypothesis is used in that lemma. The original D cancels algebraically in q=F/Z_F; no normalizer is dropped. '
'Uniform density alone does NOT bound every supported original-reference atom by log2(1/q(A))<=Cn: join r disjoint edges on A to K_(6r), n=8r, d=2r-2, min degree6r+1. '
'There F(A)=[48(n-1)]^(-r), Z_F>=1 for r>=8, so log2(1/q(A))/n>=log2(n)/8 tends to infinity, while Chat(A)=[6r+(-1)^r]/2^(8r) is nonzero. '
'This refutes the density-only POINTWISE reference-atom shortcut, not a spectral expectation bound or FEI. '
'The universal remaining line is a SAME-original-reference spectral expectation payment beyond the defect reserve, including large missing degree/arbitrary linear hypergraphs. Full FEI remains OPEN. '
'These are ideal-reference coding results on a width-two monotone class whose FEI status is not asserted new.')
claim=dict(prior)
claim.update(version=7,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 hypotheses=prior['hypotheses']+['Version7 dense-graph theorem: n>=4, complement max degree d, n>=4(d+1); ORIGINAL uniform feasible lambda=1/(n-1); full occupation table/normalizer and actual variance wrapper.','kappa_def is a structural-spectral sufficient criterion, not a universal replacement of all read-k terms.','Inherited history bookings are actual full-CE decreases; arbitrary witness/query fees are not identified with them.'],
 proof_source={'prior_version_source':str(old/'CLAIMS.json'),'new_proof':str(R/'DERIVATION.md'),'locators':['sections1-4: all-graph dense-defect full reference payment','section5: explicit growing missing degree and unavoidable read','section6: all histories from same original root','section7: exact density-only supported-atom obstruction'],'certificates':[str(R/'out'/x) for x in ['check.json','scalar.json','independent.json','obstruction.json']]},
 proof_dependencies=[{'claim_id':prior['claim_id'],'version':6,'scope_used':'General full-CE paid projection/calibration and all-history telescoping only; the new mass and full normalizer bounds are derived directly.'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':prior['claim_id'],'version':6}],
 refutes=prior['refutes']+[{'statement':'Every nonzero Fourier atom in every graph of minimum degree at least3n/4 has original normalized occupation code length<=Cn with universal C','witness':'Join r disjoint edges on A to K_(6r): nonzero Chat(A), code length/n>=log2(n)/8 for r>=8','scope':'Pointwise original-reference shortcut; no weighted-cost or FEI refutation'}],
 first_unproved_line='Pay the ORIGINAL spectral expectation beyond the (d+1)log n defect reserve. First concrete target: join r disjoint edges to K_(6r), retaining original weights, full normalizer, both projected/calibrated terminals and all old delta bookings.',
 next_consumers=['A008','A009','A010','A015','A086','A094','B03'])
assert set(claim)==set(prior);dump(R/'CLAIMS.json',[claim])
next_action='A086/A094 independently reconstruct v7 prefix multiplicity, ordered-list normalizer and source projection. Pay ORIGINAL reference on join(r disjoint edges,K_(6r)) by spectral-sector weighting rather than pointwise atom bounds; retain all terminal costs/old delta bookings.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A014','gap_id':'A014-ARBITRARY-OVERLAPPING-BLOCKER-REFERENCE-COST','attempt_id':'A014-stage19-spectral-defect-original-reference',
 'method':'Greedy-prefix matching multiplicity, exact occupation factorial bounds, full normalizer via ordered endpoint lists, downset boundary influence, independent unmatched-set reconstruction',
 'mathematical_delta':'Nonsymmetric dense G: entire ORIGINAL reference CE<=(24+kappa_def)I, kappa_def=(d+1)(log n+20)v/I; explicit growing-d growing-read family<=28I and same all-history account. Density-only supported-atom shortcut exactly refuted. Full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATES; REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':prior['claim_id'],'version':6}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':7}],
 'source_artifacts':[str(old/'DERIVATION.md'),str(R/'DERIVATION.md')]+[str(R/x) for x in ['FROZEN_SPEC.json','FROZEN_INDEPENDENT.json','FROZEN_OBSTRUCTION.json','out/check.json','out/scalar.json','out/independent.json','out/obstruction.json']],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal original-reference spectral expectation unpaid beyond defect reserve','Independent peer review and supervisor mirror verification pending','Brain self-care degraded: stale personal context/dream; recurrence watch unresolved; not used as mathematical evidence'],'packet_ids':['A014']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# A014 stage19: spectral defect pays nonsymmetric original overlap

## exact target, quantifiers, hypotheses and units

For EVERY simple G on n>=4 vertices, complement maximum degree d, n>=4(d+1), set f=1-2 times the independent-set indicator. Keep the ORIGINAL complete edge-occupation table, fixed feasible lambda_e=1/(n-1), every attachment and full normalizer. With kappa_def=(d+1)(log2 n+20)/(I/Var), the ENTIRE ideal reference CE<=(24+kappa_def)I. Thus (d+1)(log2 n+20)<=n implies CE<=28I. No symmetry of the missing graph is required. Bits; actual Boolean squared Fourier spectrum. This is a sufficient structural-spectral criterion, not a universal replacement theorem for read k. No novelty claim is made for FEI on width-two monotone DNFs themselves.

An explicit unbounded-overlap example has n=2^m, m>=6, and missing graph a star of degree floor(n/(m+20))-1 plus isolated vertices. That degree tends to infinity; necessary positive-DNF maximum read is n-1; the complete original reference costs<=28I. ALL finite adaptive restriction histories and stopping cuts keep both full terminal references and old actual CE-decrease bookings within this SAME original root account.

## sources actually read, revisions and theorem locators

Current BOARD dated2026-10-23 10:53 UTC and refreshed11:14 UTC, particularly B02/B03 and review-agent status; B03 STREAM_NOTES v2; own STATUS; stage18 DERIVATION equations(9)-(14), claims/progress/finalizer; original stage5 exact occupation helper (SHA256 {full['source_helper_sha256']}). Protocol2026-10-11-execution-v2 governs the files. Earlier campaign plan, registries and context-paper reads are inherited from the prior stages and are not represented as new independent reviews. A few read-only math-brain searches returned bounded-width FEI and congestion leads; no retrieved claim is a proof dependency. No external priority assertion or publication action.

## complete derivation or exact first unsupported line

DERIVATION sections1-4 give a direct all-n proof. The exact J ratio gives J(a,b)>=6^(-a-b)/2; a least-vertex greedy matching prefix gives factorially many distinct maximal completions until at most2d+2 vertices remain. The retained defect costs at most(d+1)(log n+20) per nonempty event. The complete normalizer is independently bounded by ordered lists on root endpoints: factorial attachment weights are counted before applying the geometric series. This proves Z_F<=exp(n/8); no queue subprobability theorem or omitted D is used. Downset boundary counting gives I=2s[n-2 E|X|]>=sn and Var/I<=4/n. Together with the FULL binary wrapper these prove CE<=(24+kappa_def)I.

Section6 applies stage18's paid projection/calibration identity. The original nonempty table is projected and conditioned on a nonempty image. The full child references calibrate their actual empty masses, and that calibration is explicitly funded by the parent categorical cost. Restrictions need not satisfy this stage's density hypothesis. No new reference table, influence bank or child bound is invoked. Booked deltas are actual full-CE decreases; they are not asserted to equal arbitrary witness fees or true entropy decrements.

Section7 supplies an actual Boolean supported-atom obstruction to a stronger proposed shortcut. Join r disjoint edges on A to a6r-clique, n=8r. Despite minimum degree>=3n/4, its original q(A) has log(1/q(A))/n>=log n/8 for r>=8. Chat(A)=[6r+(-1)^r]/2^(8r) is nonzero. This disproves a uniform POINTWISE dense-graph reference bound. Its tiny spectral weight leaves a weighted expectation bound open; this is neither an FEI refutation nor a failure of the new theorem.

First unsupported line: pay the ORIGINAL weighted spectral expectation beyond the defect reserve, rather than requiring pointwise atom bounds. General overlap/linear hypergraphs remain open. A complete original root payment on the join family above is the next sharp test.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes computation. Pilot: all64 labelled graphs on4 vertices,41 without isolates,615 nonempty sets, {pilot['assertions']} exact assertions in {pilot['elapsed_seconds']:.6f}s. The final checker additionally checks the direct rational normalizer majorant. Full:1059 fixed labelled candidates (all1024 graphs n=5;32 complement subgraphs of a fixed5-edge path n=6; three n=8 graphs deleting1,2,4 fixed disjoint edges). Excluding256 graphs with isolated vertices leaves803 graphs and26589 nonempty sets. Every complete occupation mass is checked by polynomial and direct neighbor-choice sums; recursive matching enumeration independently replaces the old edge-subset generator. Full result: {full['assertions']} exact assertions PASS in {full['elapsed_seconds']:.6f}s. Five theorem-domain graphs retain every original normalized mass; ALL35 one-coordinate child comparisons retain full projected/calibrated terminal CEs.

Scalar domain was fixed n=4..128, d=0..floor(n/4)-1, k=1..n:173728 cases. The all-n mass inequality is checked by rational integer powers, not floating logs. The explicit family has123 fixed scalar m=6..128 checks. Scalar result: {scalar['assertions']} assertions PASS in {scalar['elapsed_seconds']:.6f}s. These finite checks supplement the analytic all-dimensional proof rather than replacing it.

FROZEN_INDEPENDENT precedes a second implementation: independent-unmatched-set/perfect-matching partition, direct Fourier character sums, direct cube-boundary influences. ALL859 nonempty original masses on the five theorem-domain graphs agree exactly, including full Z_F and q: {ind['assertions']} assertions PASS in {ind['elapsed_seconds']:.6f}s. This is implementation independence by the same author; independent peer acceptance is pending.

FROZEN_OBSTRUCTION precedes128 scalar obstruction cases and the COMPLETE65792 actual Boolean inputs at n=8,16. Direct edge tests agree with the independent-sector formula, the nonzero Fourier atom and the physical boundary influence: {obs['assertions']} exact assertions PASS in {obs['elapsed_seconds']:.6f}s. No truth-table dimensions are enlarged automatically. Rational outward log intervals use an analytic atanh remainder; no floating-point sign is promoted to proof.

Commands from A014: python -X utf8 runs/{R.name}/code/check.py --pilot; check.py without --pilot; scalar.py; independent.py; obstruction.py. Every command is sequential. Estimated memory<=120MB, hence no >300MB admission required; each search under its frozen60/300s bound. No GPU, remote compute, git, other-agent mutation or messaging. Not Lean-checked. All assertions/checks must exit successfully before finalization. Output files are below20MB.

## proof dependencies and changed downstream conclusions

The single bundled A014 claim advances6->7; no new broad review candidate is opened. The new root mass/normalizer payment is derived from the exact stage5 factors and elementary inequalities. Version6 is used ONLY for the already supplied full-CE paid projection/calibration and all-history telescoping identity. Review records remain empty. Prior arbitrary-row amplification and local-phase obstructions remain scoped and unchanged. B02's biclique deletion/connector tables and A008/A015's threshold-product references are different from this arbitrary complement-degree edge occupation table.

## one next mathematical action and independent reviewer

{next_action} This targets the exact failure of the pointwise proof, rather than another symmetric example. A008/A009/A010/A015 may consume the direct full-normalizer upper bound and inherited-account invariant; no communication or acceptance is asserted.

## actual persistence receipts or precise save blocker

All requested protocol files, derivation, frozen specs, code and exact outputs are saved under THIS A014 run; STATUS, WORKLOG and LEARNED are updated in A014 only. out/RECEIPTS.json records local SHA256 and sizes; code/review_artifacts.py checks schemas, statement hash, receipt hashes, finite counts and report content. Local persistence is verified separately from independent review, supervisor copying, GitHub mirroring and downstream mathematical use, all of which remain unverified here. Brain wake reports stale personal model/state/dream and unresolved recurrence watch; those personal notes are not mathematical evidence. The session checklist working-state attempt failed because its shared lock was held; no shared file was repaired or overwritten.

## Universal bridge

This stage moves C020 whole-set witness/reference payment from the clique to arbitrary missing-edge patterns with bounded spectral defect congestion, including growing d up to about n/log n, and carries that root payment through C019-style stopping cuts with full inherited terminals and all old actual CE bookings retained. It does not resolve universal cover existence or identify every application fee with those deltas. The exact dense supported-atom obstruction shows why pointwise matching bounds alone cannot finish the universal bridge. NEXT is the SAME original reference on join(r disjoint edges,K_(6r)), paid by spectral-sector weighting with the full normalizer and old bookings: it directly removes the defect mechanism isolated here, and is a shorter route toward arbitrary overlap than another class with already factorially abundant matchings. Full FEI remains OPEN.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A014 stage19 saved: nonsymmetric ORIGINAL CE<=(24+kappa_def)I, explicit growing-d/read family<=28I; full terminals/old bookings SAME root; exact checks PASS; review pending; FEI OPEN.\nNEXT: A086/A094 review v7; pay ORIGINAL join(r disjoint edges,K6r) by spectral-sector weighting beyond dense supported-atom obstruction, retaining full normalizer/terminals/old delta bookings.\n')
stamp=datetime.now(timezone.utc).isoformat()
entry=f'\n{stamp} stage19 {R.name}: proved arbitrary missing-graph defect criterion CE<=(24+kappa_def)I, explicit nonsymmetric growing-d/read family<=28I; full original normalizer via endpoint lists; all histories use same root. Checks main={full["assertions"]}, scalar={scalar["assertions"]}, independent={ind["assertions"]}, obstruction={obs["assertions"]}, all PASS. Density-only supported-atom pointwise bound refuted; spectral expectation open. Peer review/mirror pending; no work left running after validation.\n'
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as handle:handle.write(entry)
lesson='''\nStage19 (2026-10-23): For n>=4(d+1), d=complement maximum degree, original lambda=1/(n-1) complete occupation CE<=(24+kappa_def)I with kappa_def=(d+1)(log2 n+20)v/I. All arbitrary missing patterns allowed. Root lower bound: F(A)>=r0!a^(r0+d+1)b^(2d+2), a=lambda/48,b=lambda*delta/48,r0=max(0,floor((|A|-2d-1)/2)). Distinct least-vertex prefixes survive deterministic maximal completion. J>=6^(-a-b)/2; upper J<=a!b! permits complete normalizer counting by endpoint ordered lists, yielding Z_F<=exp(n/8). Downset I=2s(n-2mu)>=sn. If (d+1)(log n+20)<=n, entire CE<=28I. Explicit complement star at n=2^m,d=floor(n/(m+20))-1 has growing d and unavoidable read n-1. Same root funds all actual CE-decrease bookings/full projected-calibrated terminals; no child density hypothesis. Pointwise shortcut fails even delta>=3n/4: join r disjoint edges to K6r has nonzero Chat(A)=(6r+(-1)^r)/2^(8r), F(A)=[48(n-1)]^-r, q(A)<=n^-r for r>=8. Thus future progress must use weighted spectral sectors, not demand all atoms be exp(-O(n)). No new FEI claim for width2 itself; peer review pending; full FEI OPEN.\n'''
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as handle:handle.write(lesson)
files=sorted(x for x in R.rglob('*') if x.is_file() and x.name!='RECEIPTS.json')
receipts=[{'path':str(x.relative_to(R)).replace('\\','/'),'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),'bytes':x.stat().st_size} for x in files]
assert all(x['bytes']<20_000_000 for x in receipts)
dump(R/'out/RECEIPTS.json',{'run_id':R.name,'created_utc':stamp,'files':receipts,'rolling_files':[{'path':str(x),'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),'bytes':x.stat().st_size} for x in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],'mirror_status':'UNVERIFIED; supervisor owns copying'})
print(json.dumps({'saved':R.name,'claim_version':7,'receipt_files':len(receipts),'main_assertions':full['assertions'],'other_assertions':scalar['assertions']+ind['assertions']+obs['assertions']}))
