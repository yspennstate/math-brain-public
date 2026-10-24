from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; ROOT=R.parents[1]
rid=R.name
statement="For every n>=3 and every complete adaptive physical restriction tree T of the one-point defect f_n(x)=1-2*1_{x=0} on the uniform n-cube, define bad nodes by B_i(f_v)>2*Inf_i(f_v) and Q_bad(T)=sum_{v bad} pi_v*I(g_v*h_v)/2. Then Q_bad(T)/I(f_n)=(n-1)/2-1/n. Consequently no finite Kprime bounds Q_bad(T)<=Kprime*I(f) for all Boolean f and all complete trees at badness threshold K=2. For every fixed K>2, this same family's Q_bad,K(T)/I(f_n) tends to zero. Its Shannon H/I is less than 4 for n>=2. The universal localized bridge at a sufficiently large fixed K, optimized stopping trees, C018 and FEI are not refuted."
hyp=['genuine Boolean sign function on uniform cube, represented as {0,1}^n by coordinate relabeling','entropy in bits; influence is sum of directed-edge disagreement probabilities','complete tree queries distinct remaining physical coordinates on each path until constant leaves','strict badness inequality B_i>K*Inf_i','n>=3 for divergent-ratio formula']
claim={
 'claim_id':'A025-LOCALIZED-ODDFACE-THRESHOLD2-NOGO','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A025/account05'],'proof_source':str(R/'REPORT.md'),'proof_dependencies':[],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['universal linear localized odd-face payment at badness threshold K=2 (also K<2)'],
 'first_unproved_line':None,'next_consumers':['Claude B05','A023','A028','A064','A087','A094','B20']}
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':rid,'stream':'B05','packet_id':'A025','gap_id':'G-R-MISMATCH',
 'attempt_id':'A025-localized-oddface-01','method':'Exact integer census of n<=4 adaptive trees; self-contained point-defect finite-to-infinite proof and strict threshold boundary',
 'mathematical_delta':statement,'deliverable_status':'COMPLETE_LOCAL_FILES; independent review and supervisor copy pending',
 'mathematical_status':'THRESHOLD_2_PAYMENT_REFUTED; LARGE_THRESHOLD_BRIDGE_OPEN; FULL_FEI_OPEN',
 'claim_versions_used':[],'claims_created_or_changed':['A025-LOCALIZED-ODDFACE-THRESHOLD2-NOGO v1'],
 'source_artifacts':['REPORT.md','code/exact_tree.py','out/FROZEN_SPEC.json','out/SPEC_CORRECTION.json','out/EXACT_TREE_RESULTS.json','code/verify_family.py','out/FAMILY_SPEC.json','out/FAMILY_RESULTS.json','out/SOURCES_READ.json'],
 'next_consumers':['Claude B05','A023','A028','A064','A087','A094','B20'],
 'next_action':'Independently reconstruct threshold-2 theorem (A087/A094), then test the surviving K=4 localized bridge on one overlapping-control family with actual B_i classification and terminal entropy retained.',
 'stagnant_substantive_attempts':0,'blockers':['No proof or counterfamily for a sufficiently large fixed K; no independent review yet'],
 'packet_ids':['A025']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:(R/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
sources=[]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
 p=base/n;sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'protocol/state/navigation; mathematical premises independently derived'})
for p in (base/'runs').rglob('REPORT.md'):
 sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'earlier B05/B19 full report; B09 target/background excerpt, not a premise'})
base=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ERASURE_REDUCTION.md','sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']:
 p=base/n;sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'read campaign/seed source; erasure definition at ER sections 1-2'})
for p in Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'):
 sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'introductory scope and theorem/composition locators read; no theorem used in proof; UTF-8 replacement decoding for legacy bytes'})
for p in [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B05\STREAM_NOTES.md')]:
 sources.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'role':'stage-start board and B05 v1 localized odd-face instruction'})
(R/'out'/'SOURCES_READ.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
results=json.loads((R/'out'/'EXACT_TREE_RESULTS.json').read_text())
family=json.loads((R/'out'/'FAMILY_RESULTS.json').read_text())
report=r'''# A025: strict threshold 2 fails localized odd-face payment

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. The B05 lead's v1 instruction replaces the already retired local variance-refund helper by

Q_bad,K(T) := sum_{v: B_{i_v}(f_v)>K d_v} pi_v I(g_v h_v)/2 <= Kprime I(f),

where g_v,h_v are the actual fair Boolean children, d_v=Inf_{i_v}(f_v), B_i=H(S_i|S_-i), and pi_v is the physical probability of reaching v. All entropies are in bits. This stage proves failure for K=2 (and K<2), even for every complete adaptive tree of its explicit family. It does not refute the existence of a sufficiently large K,Kprime. We use {0,1} coordinates as a relabeling of the uniform sign cube. The selected family has output rarity 2^-n and dimension n.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. Read campaign README/status, registry/obstruction and packet/next-action navigation, the plan's B05/A025 contracts, the supplemental campaign, claims, counterexamples, seed lemmas and mapping. B05's original 20261011T193057Z report sections 2-7 and B19's 20261011T195038Z audit were read to retire their accepted local no-go; it is not reproved or used as a premise. The B09 earlier report was read as background, not accepted as a dependency. Read ERASURE_REDUCTION.md sections 1-5 and BLOCK_RESTRICTION_IDENTITY sections 1-3 for notation and scope. The threshold 38pp paper introduction, composition and rare-activation theorem locators, its 29pp earlier version, and the percolation 30pp/31pp introductions and theorem locators were consulted; no result from either paper is needed here. The older PDF text exports contain legacy non-UTF8 bytes; replacement decoding was used after an initial decoding failure.

BOARD.md was read at stage start (supervisor 2026-10-11 22:57 UTC). Claude B05 STREAM_NOTES.md v1 supplies the exact localized odd-face target. No source-complete B05 lead REPORT.md existed under its run tree when checked. Therefore the face recurrence below is reconstructed, rather than relying on the lead's in-progress claim. Exact local SHA256 receipts and read scope are in out/SOURCES_READ.json. No web source or priority claim is needed for this self-contained derivation.

## complete derivation or exact first unsupported line

Let f_n(x)=1-2*1_{x=0}. This is a genuine Boolean sign, equal to -1 at one vertex only. Put q=2^-n. Its Fourier coefficients are a_empty=1-2q and a_S=-2q for every nonempty S. Each coordinate has influence d=2q, so I(f_n)=2nq.

At any split of a live m-variable point-defect node, one child is constant +1 and one is f_{m-1}, up to translation. Hence their product is f_{m-1}, and

c_m := I(g h)/2 = (m-1)2^(1-m).

The spectra show that each nonempty residual Fourier pair has equal masses 4q_m^2, where q_m=2^-m. There are 2^(m-1)-1 such pairs. Only the empty residual pair is exceptional, with masses A=(1-2q_m)^2 and D=4q_m^2. Consequently

B_i(f_m)=4q_m-8q_m^2+E(A,D),
E(A,D)=A log2(1+D/A)+D log2(1+A/D).

For m>=3, A/D=(2^(m-1)-1)^2>=9. Thus

E(A,D)>D log2(A/D)>=4q_m^2 log2(9)>8q_m^2,

so B_i(f_m)>4q_m=2d for every coordinate. At m=2 the spectrum is uniform on four sets and B_i=1=2d exactly; at m=1 the function is a character and B_i=0. Therefore the strict K=2 bad nodes are exactly the live m>=3 nodes.

Any adaptive complete physical tree has exactly one live path; every restriction along it remains a translated point defect. The probability of reaching its m-variable live node is 2^-(n-m), irrespective of coordinate order. All other reached nodes are constant and have zero charge. Thus, for every such tree and every n>=3,

Q_bad,2(T)=sum_{m=3}^n 2^-(n-m)c_m
          =2^(1-n)[n(n-1)/2-1],
Q_bad,2(T)/I(f_n)=(n-1)/2-1/n -> infinity.

For any fixed Kprime>=0, every integer n>=ceil(2Kprime+3) yields a strict violation. If K<2, the m=2 node is also bad, and Q_bad,K/I=(n-1)/2. This is a counterfamily to a threshold choice and its claimed linear global charge, not merely a finite failed coefficient.

To check the face normalization independently, define Q(f)=2^(1-n) times the number of 2-faces with corner product -1. Faces not involving the split coordinate partition into the two child cubes and contribute their average Q. A face involving that coordinate is odd exactly when its residual edge has different values of gh. The number of such edges is 2^(n-2) I(gh), so their normalized contribution is I(gh)/2. This proves Q(f)=I(gh)/2+(Q(g)+Q(h))/2. For f_n, precisely the binomial(n,2) faces containing its exceptional vertex are odd. The total Q/I=(n-1)/2 agrees with the localized formula after subtracting the single m=2 payment 1/n.

The threshold boundary is essential. Since E(A,D)<=D log2(e(A+D)/D) and A+D<=1 for m>=2,

B_i(f_m)/d <= 2+2^-m(4m-8+2log2(e)) < 2+4m2^-m.

Here the entropy estimate follows from -(1-t)ln(1-t)<=t with t=D/(A+D). For fixed K>2, let M_K be the largest integer m>=2 satisfying 4m2^-m>K-2, or take M_K=1 if that set is empty. It is finite. Only nodes with m<=M_K can be bad. Thus every complete tree of this family satisfies

Q_bad,K(T)/I(f_n) <= M_K(M_K-1)/(2n) -> 0.

This family supplies no large-K obstruction. It also satisfies H(f_n)/I(f_n)<4 for n>=2: its tail entropy is (2^n-1)4q^2(2n-2), while the empty atom entropy is <=(4q-4q^2)log2(e). After division by 2nq the sum is <4-4/n+2log2(e)/n<4. Its Shannon ratio tends to 4, consistent with the campaign's point-defect controls.

No line in the stated threshold-2 theorem remains unsupported. The first unpaid line for the intended universal route is: there exist sufficiently large fixed K,Kprime such that the localized payment holds on arbitrary Boolean functions for an appropriately quantified physical tree, with terminal entropy retained. This stage neither proves nor disproves that line. A stopping tree may terminate before all coordinates are read; the theorem does not claim that every stopping strategy fails.

## executed validation with domain, arithmetic, commands and outputs

code/exact_tree.py exhausts all Boolean functions in n=0..4 modulo output complement. It computes integer Walsh transforms and exact d, verifies Parseval and the influence identity, classifies B_i>Kd by exact integer-power comparison, and uses dynamic programming over every coordinate choice and both actual children to maximize the complete-tree localized cost. Coordinates are not discarded by a heuristic. Output complement preserves spectra and gh, so that quotient is exact.

For integer Walsh coefficients a_S and N=2^n, set A=a_T^2 and D=a_{T+i}^2. Multiplying (A+D)^(A+D)/(A^A D^D) over pairs and comparing with 2^(K sum D) exactly certifies the strict logarithmic sign. Zero entries contribute a factor one. The physical cost at a node is the directed edge-count of gh divided by N. In the DP, its integer numerator adds to both child numerators because their fair 1/2 weights cancel the halved child cube size. Therefore the DP returns exact rational cost/influence ratios.

Frozen spec: out/FROZEN_SPEC.json. Its original written count 32898 was an arithmetic typo; the immutable correction out/SPEC_CORRECTION.json records 1+2+8+128+32768=32907, with no changed domain or dimension escalation. Actual census: CASE_COUNT_PLACEHOLDER cases, ASSERTIONS_PLACEHOLDER exact assertions, SECONDS_PLACEHOLDER seconds. Maximum ratios by dimension are:

| n | K=2 | K=3 | K=4 |
|---|---:|---:|---:|
| 0,1,2 | 0 | 0 | 0 |
| 3 | 2/3 | 0 | 0 |
| 4 | 5/4 | 3/8 | 0 |

At K=2 the witnesses are single-vertex defects, up to translation. At K=3,n=4, the supplied witness has negative vertices encoded by integer 14, root coordinate 0, physical cost numerator 6 and influence numerator 16. That finite 3/8 cost is not a growing-family refutation. K=4 has no bad node through n=4; this is finite evidence only.

code/verify_family.py independently constructs the point-defect truth tables for the frozen domain n=1..10, directly enumerates odd 2-faces and physical boundaries, and rechecks the Fourier coefficients and rational inequalities in the sign proof. The first v1 checker was stopped manually: its large exact powers at n near 10 were unnecessary and threatened the pilot budget. It produced no completed certificate and no claimed assertions. Version 2 replaces those powers by the exact rational A/D>=9 comparison and the analytic log2(9)>2; out/FAMILY_SPEC.json freezes that revision. It passed FAMILY_ASSERTIONS_PLACEHOLDER assertions in FAMILY_SECONDS_PLACEHOLDER seconds. The v1 memory estimate 5 MB was too low for the unnecessarily large powers; it was not a heavy search, and no dimension escalation was used. No GPU, background job, random search, floating sign decision or cross-agent write was used.

Commands (run in this run directory):

    python -X utf8 code/exact_tree.py
    python -X utf8 code/verify_family.py

Outputs: out/EXACT_TREE_RESULTS.json and out/FAMILY_RESULTS.json. This is a second implementation by the same author, not independent human/agent acceptance.

## proof dependencies and changed downstream conclusions

The new proof has no external unreviewed mathematical dependency. It uses the conditional spectral entropy definition, elementary Walsh algebra and the displayed face-count proof. The B05 localized odd-face proposal requires a strict badness threshold greater than 2 if it is to hold uniformly on complete trees. Its K=2 specialization is refuted even under complete-tree existential coordinate ordering, since every complete tree on this family has the same divergent cost. This does not settle any existential stopping-tree theorem with terminal costs. The mismatch/KL identity is not weakened or refuted; this stage directly evaluates the proposed odd-face replacement. No actual downstream adoption is claimed. The existing local variance-refund no-go remains unchanged. Because B05 already has a pending-review queue above the protocol cap, this stage supplies a narrowed falsification of the lead's designated live replacement, not another broad positive candidate.

## one next mathematical action and independent reviewer

Have A087 reconstruct the exceptional Fourier pair and live-path sum; A094 is the alternate reviewer. Then test the surviving K=4 localized payment on one overlapping-control family, classifying actual B_i at nodes and retaining terminal entropy. Do not extend the n<=4 census mechanically or report this threshold-2 family as failure for all K.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in this authorized A025 run folder, with code and exact JSON outputs. STATUS.md, WORKLOG.md and LEARNED.md are saved only in A025. out/RECEIPTS.json records sizes and SHA256s of the completed artifacts; all are below 20 MB. Local persistence is complete. Independent review, supervisor GitHub/brain copying, mirror verification and downstream mathematical use remain pending; no shared index or brain was written.

## Universal bridge

This stage moves C019, through the B05 localized odd-face replacement, by proving that the strict badness threshold K=2 cannot have any finite global payment constant: the exact whole-tree cost/influence grows as (n-1)/2-1/n for an actual rare Boolean family. It also proves why that family stops obstructing every fixed K>2. What remains is the larger-threshold localized payment on general functions, a suitable stopping-tree quantifier and complete terminal entropy. Testing that surviving bridge on overlapping controls, after independent reconstruction of this narrow counterfamily, is the shortest next route toward full FEI because it attacks the unpaid nonreusing tree cost directly rather than closing another isolated class.
'''
report=report.replace('FAMILY_ASSERTIONS_PLACEHOLDER',str(family['assertions_passed'])).replace('FAMILY_SECONDS_PLACEHOLDER',str(round(family['seconds'],4))).replace('CASE_COUNT_PLACEHOLDER',str(results['cases'])).replace('ASSERTIONS_PLACEHOLDER',str(results['assertions_passed'])).replace('SECONDS_PLACEHOLDER',str(round(results['seconds'],4)))
report=report.replace('It produced no completed certificate and no claimed assertions.', 'It produced no completed certificate and no claimed assertions. Its cap check was between dimensions and did not interrupt a single expensive power operation; the process was manually interrupted, and actual in-process runtime was not captured. This runtime-control defect was removed with the inexpensive rational certificate.')
(R/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A025 threshold-2 localized odd-face payment refuted by exact Boolean family; n<=4 census complete; review pending; full FEI OPEN.\nNEXT: A087/A094 reconstruct; test surviving K=4 localized payment on overlapping controls with terminal entropy retained.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Read protocol, campaign, stage board and B05 direction. Exact n<=4 tree census: {results["cases"]} cases, {results["assertions_passed"]} assertions. Proved point-defect Q_bad,2/I=(n-1)/2-1/n for every complete tree; fixed K>2 ratio tends to zero. Stopped costly v1 family sign validator; rational v2 passes. Saved full source-complete narrow theorem; independent review pending.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nPoint-defect f_n=1-2*1_{x=0}: every m>=3 restriction coordinate satisfies B_i>2 Inf_i, m=2 equality. Q_bad,2/I=(n-1)/2-1/n in every complete physical tree, while Shannon H/I<4. This refutes only badness threshold <=2. For fixed K>2, B_i/Inf_i<2+4m2^-m forces bounded residual dimension at bad nodes, hence Q_bad,K/I=O_K(1/n). Exact integer-power log comparisons are effective at n<=4 but unnecessary and expensive for larger near-constant Walsh coefficients; use proved rational lower bounds. Keep all-K and stopping-tree scope open.\n')
receipt=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  receipt.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'out'/'RECEIPTS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('Saved report, claims, progress, packet delta, rolling files and',len(receipt),'artifact receipts.')
