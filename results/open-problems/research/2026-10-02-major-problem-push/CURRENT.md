# Major-problem research continuation, 2026-10-02

User instruction: continue toward a bigger result on a famous open problem in probability or K-theory; push completed results and subsequent derived work to the user's GitHub. This direct instruction authorizes this separate campaign. Do not change other campaigns or automations.

## Verified completed work

`proofnet24/mmpp-counterexamples/2026-10-02/` contains a complete counterexample to Asanjarani--Nazarathy (2022), Conjecture 3.9, and a complete counterexample to the time-stationary SCV >= 1 question in He (2021), Section 4.3. The PDF, LaTeX source, two independent exact rational exponential checks and outputs are included. These are specialized published questions, not famous major conjectures. Priority is unverified; no earlier disproof was located in the search. The separate established event-stationary SCV theorem is respected.

## Current research targets

Whitt's stochastic-order assertion has now been refuted mathematically. The unrestricted FEI, forest/random-cluster, Sidorenko, and K-theory targets remain OPEN in this campaign. The deterministic-LTF subclass of FEI now has a complete internally audited proof; read the new checkpoint below before treating that subclass as an unresolved gap. Read actual reports and scripts before resuming; do not replace analysis with bookkeeping.

1. Fourier entropy--influence (FEI): `proofnet24/P03-fei/continuations/2026-10-02-selection-obstructions/` contains the exact split identity and a full monotone family proving that no uniform split-increment constant works for maximum-influence selection, even for selection within any fixed positive factor of maximum influence. The proof uses balanced majority substitution and exact entropy cancellation; root audited it and reran the check. A separate separator_obstruction.md proves that monotone ternary geometry with no direct sign-crossing edge is also insufficient, using a dimension-free conditional-entropy continuity lemma and explicit majority erosion. Root audited the proof and reran its finite construction check. These are subsidiary obstructions, not a disproof of FEI, deterministic LTF FEI, or unrestricted adaptive-coordinate existence. Further routes and their precise gaps are recorded. A new separate continuation 2026-10-02-hamming-band contains the complete independently audited restricted theorem H(f)<=[25+64(k+1)^2] I(f) for every monotone function whose potentially nonsymmetric decisions are confined to k consecutive Hamming layers; one exceptional layer has constant62. Arbitrary-bias weighted thresholds with dimension-independent sum_i |w_i/c-1| are included. Full proof, both verifiers and exhaustive exact identities for all7581 monotone five-bit functions are archived. This does not solve full FEI or all deterministic LTFs; novelty remains unverified.
2. Forest / q < 1 random-cluster negative correlation: `proofnet24/P14-probability-correlation/continuations/2026-10-02-forest-families/` contains an exact transfer and coefficient-positivity proof for homogeneous forest measures on K_(m,s), 2<=m<=8 and every s>=2, every positive common edge activity, all edge-pair types, plus an exceptional twin-matching family. Direct subset audits independently match the transfer. The derived FOUR_TWINS_ARBITRARY_CORE_H2.md gives a positive adjugate sum of squares for the first nonzero high-fugacity Rayleigh coefficient with four twin terminals over an arbitrary weighted core; the ZERO_SPOKE extension allows any common weighted neighborhood and yields an unbounded K_(m,s)+matching family. This is a genuine analytic partial result, not the full conjecture; novelty is unverified. The deletion-connectivity covariance identity overlaps arXiv:2610.00549, v1 submitted September 30, 2026 and inspected October 2, 2026, and must not be claimed as new. The further GENERAL_H2_SOS_PROOF.md is a complete independently audited general third-coefficient theorem: for any connected weighted graph, H0=H1=0 implies H2>=0, via an explicit electrical interface sum of squares. It is supported by two analytic audit routes and independent exact full-forest enumerations beyond twins, including boundary endpoint cases. Primary H0/H1 results and equality classification are credited. If H2>0 it proves high-fugacity marked-pair negative correlation; The previously unresolved H2zero higher-order cases are now covered by the all-orders high-fugacity checkpoint below; all-fugacity correlation and negative association remain unproved. General homogeneous random-cluster coefficient positivity remains unproved. arXiv:2609.26134 solves the unweighted complete-graph case only, not general finite graphs or multigraphs.
3. Sidorenko: the ten-vertex Mobius ladder (K5,5 minus a Hamiltonian C10) remains an important small unresolved case in the primary literature checked. Operator and structured graphon routes are being investigated.
4. Kaplansky / direct finiteness: current nonsofic examples change the landscape; inspect the August 2026 primary papers and already performed bounded searches before recycling old claims. No full proof or counterexample obtained.
5. Whitt (1983), Conjecture 1.1, M/G/s waiting-time stochastic comparison: `proofnet24/whitt-stochastic-comparison/2026-10-02/` contains complete counterexamples, a hand-checkable nine-state integer proof, exact QBD and independent killed-chain certificates, a strictly positive two-exponential example with delay-probability reversal >1/400 at lambda=11/10, and a general analytic light-traffic theorem. The stronger whitt_all_servers_light_traffic_proof.md proves that FOR EVERY FIXED c>=2, every nondegenerate finite hyperexponential starting law has a convex-order larger two-exponential law with strictly smaller delay probability for all sufficiently small positive lambda. The target can be chosen strictly positive with an explicit rational epsilon. Independent audits of the general finite-chain perturbation coefficient, symmetric-odds inequality, and epsilon bound pass. The nine-state witness supplies a fully explicit finite arrival rate; the general theorem does not quantify its small-rate interval. Historical priority and definitive current open status remain unverified: no earlier refutation was located, but that search is not proof of novelty. Weaker mean waiting-time statements remain unaddressed. Read whitt_README.md, the all-server extension and the full audits. Zero-service jobs can wait and must be included in the all-arrival PASTA statistic even when removed from the workload process. The general-service gap is now CLOSED by whitt_general_service_light_traffic_proof.md: every strictly positive law with finite second moment has the rigorously derived next delay coefficient, without a general analyticity assumption. The derived whitt_general_DFR_positive_comparator.md constructs an explicit strictly positive H2 comparator for every nonexponential law with finite continuous decreasing hazard bounded below; its stop-loss is strictly larger at every positive threshold, yet its delay probability is smaller at sufficiently small rates. Full independent audits pass. A further whitt_strict_mean_increase_exact.py certificate scales the explicit finite-rate positive H2 comparator by10001/10000: mean is strictly larger, stop-loss is strictly larger even at zero, but delay-probability gap exceeds12/5000 and a positive waiting-threshold gap exceeds23/10000. Its full proof and audit are archived. The old exploratory DFR file records an earlier gap and must not be read as current status.

## Previous verified checkpoint: derived-04

Read `runs/derived-04/RESULTS.md` and the actual files below. These are new extensions of the previous baseline, not recycled special-family results.

- **All deterministic LTF FEI:** `proofnet24/P03-fei/continuations/2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md` gives the complete uniform-cube theorem H(f)<=C I(f) for every linear threshold function, with arbitrary real weights and bias. Its stronger largest-defining-weight split bound closes restriction induction. Four independent internal analytic audits pass, including an alternative Gibbs-test-function KL derivation and a two-sided degree-bin entropy argument. Read all four audit files and `largest_weight_ltf_prior_art_checkpoint.md`. Both finite suites (1632 and1642 nonconstant cases) were rerun by root. The elementary relative slab-stability lemma, primary KOS biased-noise and Keller--Klein maximal-influence statements, endpoint/zero-degree handling, KL direction and interference correction are fully explicit. The original candidate is preserved. This is a complete internally verified mathematical proof, not external peer review or a novelty certificate. The primary2019 random-LTF paper described the deterministic target as unknown; the apparent2013 all-LTF claim was removed in the actual2018 ECCC revision. No earlier valid solution was located in the bounded current search, which does not prove priority. Full Boolean FEI and biased-input-product FEI remain unproved here.
- **Independent regular-weight route:** `proofnet24/P03-fei/continuations/2026-10-02-regular-bias/regular_biased_ltf_fei.md` derives H(f)<=300 p sqrt(n ln(1/p)) and arbitrary-bias regular-LTF FEI from established results, including fixed-L2-deviation weights. Full independent source/normalization audit and both verifiers are archived. This is now subsumed by the all-LTF theorem and must not be advertised as a further new full result.
- **General forest H3:** `proofnet24/P14-probability-correlation/continuations/2026-10-02-general-H3/GENERAL_H3_SOS_PROOF.md` proves H0=H1=H2=0 implies H3>=0, with an explicit shifted-response electrical sum of squares. Root read the complete final proof and independently rederived Ward signs, grounded-port normalization, coefficient powers, triple cumulants and general multiport energy completion. Three other analytic audit branches pass. Nine exact graph cases and root/weight variants pass, including two11-vertex non-M-matrix response examples checked by independent subset enumeration and frontier DP. Positive H3 proves sufficiently-large-fugacity marked-pair negative correlation; H3zero cases, later coefficients and all-fugacity conjectures remain unresolved. Read the new kernel lemma, H3zero aggregate-support separation, both failed stronger claims and exact counterexamples, and `H3_CHECKS_README.md`. Prior H0/H1 geometry and classical Grassmann/OSP tools are credited; novelty is unverified.

The response Gram need not be an ordinary positive-weight graph Laplacian, and higher local scores can involve common-mode quartics. Both shortcuts are disproved by exact certificates in the H3 continuation. They do not refute the established H2/H3 sum of squares. The new all-orders induction below explicitly controls later score terms, response-space closure, valid grounding and finite enlargement. It does not infer full correlation from a finite list of coefficients.

## Previous verified checkpoint: derived-05

Read `runs/derived-05/RESULTS.md` and `proofnet24/P14-probability-correlation/continuations/2026-10-02-all-graph-high-fugacity/ALL_GRAPH_HIGH_FUGACITY_PROOF.md` in full. The complete internally audited theorem now covers EVERY fixed finite weighted graph at sufficiently large common fugacity. It proves a nonnegative Rayleigh polynomial beyond a finite graph/weight-dependent threshold for all marked pairs, with strict negativity for pairs on a common cycle and exact independence for different graphic-matroid components. A separate audited integer-conductance corollary gives the crude explicit threshold1+2 product_(g!=e,f)(1+c_g)^2, simplifying to1+2*4^(m-2) for an unweighted m-edge graph. No practical/optimal general threshold, all-fugacity theorem, negative association, or q<1 random-cluster result is claimed. Priority and external peer review remain unverified.

The full arbitrary-order marked-score transfer is proved: scalar lower scores, intrinsic free-port Ward identities, fixed marked Schur normalization, the exact leading next response Gram, full contrast-range closure including dormant old interiors, and finite strict enlargement are preserved. At delayed level ell the even coefficient is a Green trace square and, when it vanishes, the odd coefficient is a shifted response-wedge square. Vanishing of both propagates the complete invariant; it does not merely repeat geometry or a finite coefficient list. Root, K, adversarial and independent local transfer audits pass. The earlier closure-only checkpoint retains its then-open gap honestly; the separate transfer proof closes it. Root reran five direct Fraction local-score tests and four full forest-frontier iteration cases through H4/H5/H6, including a14-vertex asymmetric three-port graph.

Read all complete proofs and audits in the new track, plus `ALL_GRAPH_HIGH_FUGACITY_SOURCE_CHECK.md` and `ALL_GRAPH_HIGH_FUGACITY_CHECKS_README.md`. Classical Grassmann/supersymmetry tools, Huang's older adjacent-edge regime, and the current arXiv:2610.00549v1 first two coefficients/equality geometry are credited. The primary abstract page checked2October2026 lists v1 submitted30September2026; a crawl date is not a new submission version. The bounded source search found no earlier complete proof of this precise all-pairs theorem, but does not certify priority.

## Previous verified checkpoint: derived-06

Read `runs/derived-06/RESULTS.md` and the full `proofnet24/P03-fei/continuations/2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md`. The complete internally audited strengthened theorem is H(f)<=C+[I(f)-Var(f)] for EVERY uniform-cube LTF. It includes the empty spectral atom and has one universal constant. The same constant covers arbitrary-depth/size/fan-in read-once LTF-gate formulas with balanced nonroot outputs and disjoint leaf blocks; the root may be biased. A new universal unate-split complement lemma gives alpha>1/2 => Delta H<=8(1-alpha). The exact variance decrement alpha² converts the earlier LTF split theorem to the stronger alpha(1-alpha) induction budget.

Root, K and adversarial full analytic audits pass. The original longer complementary-KL candidate remains preserved as an independently corroborating route. Root read and reran both scripts: author suite7778monotone functions,3488near-dictator splits,401LTFs,150composition nodes/90roots through13leaves; independent suite2977exact variance/influence recursions,281unate splits,fivecompositions through12leaves. Numerical entropy is a sanity check, not the proof. Read all audits, source/check records and the full underlying largest-weight proof.

Generic disjoint composition and the I-Var framework are prior work of O'Donnell--Tan2013, whose full primary manuscript was inspected. The new mathematical input is the uniform LTFgate bound, permitting unrestricted fan-in in this balanced subclass. Their FEI+ entropy excludes the empty spectral atom; the theorem here bounds the full ordinary uniform-input entropy. Historical priority and external peer review remain unverified. General Boolean FEI, shared-input circuits, unbalanced child outputs and uncorrected biased-input entropy remain unproved here.

## Previous verified checkpoint: derived-07

Read `runs/derived-07/RESULTS.md` and the full new bundle `proofnet24/P03-fei/continuations/2026-10-02-parallel-slabs/`. The arbitrary parallel-slab FEI theorem now has a complete internally audited proof, including every real-weight interval indicator/complement and arbitrary endpoints. A largest-weight local split bound closes restriction induction. The proof also covers at most m actual sign crossings separated STRICTLY by more than twice the largest input weight, with constant depending only on m. It does not cover arbitrary nearby crossings. Root, K and heat analytic audits pass; root reran3846slab cases through dimension12. The exact endpoint cancellation certificate explains why the earlier non-strict general separation claim was repaired. Read the final proof and all audits, not the historical candidate alone.

The complete disjoint-union entropy lemma gives H(f)<=r sum H(g_j)+log2(e)(1+1/e) sum Var(g_j). Influence adds exactly when no edge joins distinct components; the precise joining-edge failure term is preserved. Therefore finite unions of parallel intervals with strictly wide separating gaps satisfy FEI, even when their component intervals are arbitrarily narrow. Root, K, author-coordinator and independent union/chain audits pass.

The full nonmonotone layer theorem removes monotonicity and contiguity. If ell is the longest consecutive run of exceptional Hamming layers and P_sym is coordinate-permutation averaging, it proves H(f)<=24.08I(f)+32(ell+1)^2[I(f)-I(P_sym f)]. The bound depends on longest run, even if the total number of exceptional layers grows. Pairwise nonconsecutive exceptional layers have the sharper bound H(f)<=56.08 I(f), from an exact random-chain disagreement/energy identity. The count-k constant is25+32(k+1)^2. A bounded total L1 deviation A from equal weights permits m exceptional score points with arbitrary endpoint labels and k<=m(floor(A)+1), without crossing spacing or output-bias constraints. Root, heat, author-coordinator and independent union/chain full analytic audits pass, including a separate maximum-run/deficit audit. Root read and reran both independent checkers: all65812Boolean functions through dimension4,4000more in dimensions5/6,75808component assignments,16368layer subsets and3000attained-endpoint examples. Established symmetric FEI is credited.

A new exact three-crossing family has unique largest weight N+1, influencealpha=2^-N, and Delta H/alpha>=(N+3)/2-log2[N(N+1)/2] tending to infinity for oddN>=15. Root and adversarial audits pass; both exact-rational/Decimal checkers were rerun. This refutes a universal largest-weight LOCAL split criterion for three arbitrary crossings, not FEI or adaptive-coordinate existence. Both this obstruction and the exact equality-endpoint failure are preserved beside the successful results.

Read `stripe_extensions_source_check.md` and `stripe_extensions_checks_readme.md`. Primary Keller--Klein2019, KOS2004, symmetric FEI2011 and hypercontractivity inputs are credited. Recent primary arXiv2609.21563v1 (submitted18September2026, inspected2OctoberUTC) proves a distinct plateaued subclass and still states general FEI as conjectural. No earlier complete proof of the precise new statements was located in bounded searches; historical priority and outside peer review remain unverified. A generic signed-split conversion to an I-Var bound and balanced slab-gate formula consequence is a subsequent candidate being independently audited, not a completed part of this checkpoint.

## Previous verified checkpoint: derived-08

Read `runs/derived-08/RESULTS.md` and the full new bundle `proofnet24/P03-fei/continuations/2026-10-02-slab-deficit-composition/`. The complete universal signed-split lemma now gives alpha>1/2 => Delta H<=14[alpha-(EB)^2], including signed mean-zero and influence-one derivatives. If a restriction-closed class has a selected local bound Delta H<=C alpha at every restriction, exact induction gives H(f)<=max(2C,14)[I(f)-Var(f)]. The low-influence local premise is retained explicitly; ordinary global FEI alone does not suffice. Root and adversarial full analytic audits pass, including final-proof continuity. Root read and reran the standalone exhaustive checker: all65814Boolean functions through4variables,262948pivots, exact influence/variance budgets and separately identified numerical entropy checks.

The parallel-slab and strict-separated crossing classes meet the local premise, so they now have complete strong bounds and balanced read-once gate-formula extensions with the same constants and arbitrary fan-in/depth/size. Every nonroot output must be balanced, leaf blocks disjoint, and the root may be biased. Generic composition is established O'Donnell--Tan2013 prior work and is fully reproduced to verify the hypotheses.

The completed `parity_modulated_ltf_proof.md` proves ordinary FEI for arbitrary parity times an LTF, with the SAME constant as the earlier strong LTF theorem. Parity inputs may overlap every threshold input and its degree may grow with dimension. It also covers parity modulations of the balanced read-once LTF formulas. The general conditional lemma uses at most one influence above1/2; every unate function has that property by the six two-bit monotone truth tables. Entropy is unchanged by the exact character spectral shift and influence is at least the base I-Var budget. The independent heat analytic audit passes. Root's standalone exact checker verifies all7778monotone functions through5variables and all245470character modulations, with integer spectral permutation and physical-flip/budget checks. This does not prove full unate FEI or arbitrary polynomial-threshold FEI.

The elementary `disjoint_product_deficit_corollary.md` permits arbitrary child OUTPUT bias in disjoint products of strong base functions, keeping the same constant. It also permits mixed read-once trees with product nodes accepting biased children, while every other gate node retains balanced children. Its separate adversarial analytic audit passes. Tensorization and character/Chow identities are established facts, not novel claimed tools. Read the complete source/check records and all full proofs. Novelty and external peer review remain unverified, and general Boolean FEI and nonuniform-input entropy remain unresolved.

## Previous verified checkpoint: derived-09

Read `runs/derived-09/RESULTS.md` and the entire new forest bundle `proofnet24/P14-probability-correlation/continuations/2026-10-02-finite-activity-matching/`.
The strongest completed finite-activity result is now **negative association
of the entire terminal-matching indicator vector**, under every positive
matching external field and after every partial matching-bit conditioning.
The three-vertex core has arbitrary nonnegative activities; rank-one spokes
have arbitrary nonnegative row factors and three positive column factors;
terminal and matching counts are unbounded. The final full proof,
self-contained support-two NA lemma, exact forced Bernoulli-OR law and
primitive core positivity certificate are archived. Root and ant full
independent analytic audits pass. Root read and reran both exact verifiers:
author four laws/432 conditionings/10,714 inequalities; independent six-edge
law/all729 conditionings/86,634 inequalities. An exact five-edge matching
law is **not real stable**, independently checked from its raw polynomial,
so strong Rayleigh is not claimed. The earlier strict pairwise theorem and
its three predecessor derivations are retained as superseded routes. Read
the completion/source README. Arbitrary spoke/core indicators, non-rank-one
spokes, overlapping terminal edges, arbitrary cores and full forest NA or
all-fugacity pair conjectures remain unresolved. Full weighted-K4
deletion/contraction and two-port/positive-mixture failed derivations and
exact checks are also preserved; they are not conjecture counterexamples.

The new Sidorenko bundle `proofnet24/C30-sidorenko/continuations/2026-10-02-restricted-hosts/` proves the full quantitative ML10
inequality on equal-measure, equal-diagonal regular symmetric four-state
hosts: t>=s^15+5s^11 sum r_i^4+(8165/567)s^9 sum r_i^6. Three independent
exact polynomial constructions agree; the full analytic independent audit
and coefficient regeneration pass, and root reran them. Coefficient5 is
sharp infinitesimally; 8165/567 is the strongest value of this particular
coefficient certificate, not a globally optimal claim. Exact rational
weights refute coefficient15. A separate Schur-convexity certificate and
quantitative rank-one surplus are fully proved and audited. The qualitative
rank-one result is **already known** from two-spin Bethe prior work, as the
complete scope/prior-art record demonstrates. Arbitrary regular hosts,
unequal atom measures and the full ML10 problem remain open here. Read
actual proofs and all source/certificate files; numerical searches and
the historical checkpoint do not override their precise scope.

The new FEI bundle `proofnet24/P03-fei/continuations/2026-10-02-component-boundary-obstructions/` rigorously disproves a uniform comparison
between I(f) and the smaller sum of maximal same-sign component influences
already for **four genuine crossings of one linear score**. The ratio is
unbounded; the same family has fully calculated spectrum and H(f)<7I(f).
Thus this is a global proof-method obstruction, not a disproof of FEI.
Full analytic, continuity and root audits pass; root reran 415,024 exact
vertices plus symbolic cases. The five-crossing predecessor and its
43,688-vertex checker are retained and superseded. A possible three-crossing
trace inequality remains a candidate, not a completed theorem.

Historical novelty and external mathematical review remain unverified for
all new restricted statements. General Boolean FEI, full forest/random-
cluster, unrestricted Sidorenko and Kaplansky/direct finiteness remain open
in this campaign. Subsequent parity-slab, three-state and adjacent-pair
extensions require new immutable proofs/audits before completed status.

## Previous verified checkpoint: derived-10

Read `runs/derived-10/RESULTS.md` and the full new bundle `proofnet24/P03-fei/continuations/2026-10-02-parity-slabs/`.
The complete internally audited theorem is H(g)<=(C_slab+60)J(g) for
EVERY uniform-cube parallel slab, where J=sum min(I_i,1-I_i) is the
minimum influence over its character orbit. Thus every arbitrary parity
modulation satisfies ordinary FEI with that constant, including overlapping
inputs and unbounded parity degree. Root and K full independent analytic
audits pass, including the upstream ordinary slab/union inputs. The full
proof uses universal entropy gluing charged to TOTAL influence of the
centered function and at most15 original high-influence coordinates.
Neither a comparison J>=c(I-Var) nor a local bound by min(I_i,1-I_i) is
assumed; both are disproved by complete separate slab examples. Root read
and reran the checker:65,814 functions/262,948 pivots,3,951 slabs and61,396
characters; exact integer identities and numerical entropy checks are
distinguished. Root also reran the full local-obstruction checker:7 truth
realizations,33,125 Fraction assertions/250 dimensions,50 Decimal entropy
checks. The analytic divergence proof establishes the local failure.
Wide-gap unions with narrow component widths have the stated centered
constant. A generic at-most-m-unate-gate closure is conditional on ordinary
FEI and restriction closure; it is not a general halfspace-combination
or shared-input circuit theorem.

The new `proofnet24/C30-sidorenko/continuations/2026-10-02-operator-boundaries/` preserves the full classical-tool Perron trace
bound and an exact positive9x9 spectral-shortcut counterexample with
excluded fifth moment-43193/20000. Its listed positivity, exchange,
inertia, sector domination and excluded-trace properties do not imply the
required odd-moment bound. It is explicitly OUTSIDE Rossman's product
family, as proved from its diagonal and an incompatible exchange entry;
it does not disprove Rossman or Sidorenko. Root and ant full analytic
audits and independent exact ladder/matrix checks pass. All searches remain
numerical only; the audit documents an incorrect explanatory code-comment
sign while verifying the implemented objective and gradient. Classical
inequalities/transfer identities are credited, not claimed as new.

The new `proofnet24/P03-fei/continuations/2026-10-02-three-crossing-boundary-route/` records a complete exact failure of tentative
component-comparison constant2 (ratio23/11), and a complete abstract
monotone-region obstruction that is not realizable by a common linear
score. Root audited these derivations and reran the independent witness.
The exact middle-threshold trace implication is proved; its required
trace inequality and the positive three-crossing FEI theorem remain OPEN.
The307,503 finite triple-cut tests do not establish a uniform bound.

Historical priority and external peer review remain unverified. The
campaign's full famous conjectures remain unresolved; new regular-three-
state Sidorenko, adjacent-terminal forest and bounded-path FEI candidates
must be read and independently audited before completed status.

## Previous verified checkpoint: derived-11

Read `runs/derived-11/RESULTS.md` and every full proof/audit linked there.
The NEW `proofnet24/P03-fei/continuations/2026-10-02-bounded-ascending-paths/` proves H(f)<=4cot^2(pi/[2(k+1)])I(f) when either label
class has upward cube-edge paths with at most k VERTICES. Every k-Sperner
family qualifies, and the path condition is strictly weaker. Edge-free
supports have optimal constant4. Arbitrary labels inside a positive-weight
band qualify with the stated floor convention; zero-weight arbitrary
decisions are excluded. The full finite-dimensional nilpotent dilation
credits Haagerup--de la Harpe1992. Root sharpened the entropy estimate to
H<=8n*minoritydensity and supplied the cotangent dimension split. Root and
heat full audits PASS; both implementations rerun successfully on66,182
and66,060 supports. Integer identities and numerical entropy/operator
supplements are distinguished. No full FEI/I-Var/composition claim.

The NEW `proofnet24/P14-probability-correlation/continuations/2026-10-02-adjacent-terminal-background/` proves negative correlation of adjacent terminal marks
over a rank-one three-core with an arbitrary graph on OTHER terminals.
No extra terminal edge may touch the three marked endpoints. All
nonnegative primitive weights and arbitrary positive marked activities
are permitted. Strictness is outer rows positive and B>0; middle row
may be zero. The exact arbitrary-background mixture keeps its variance.
Both the11,063-term primitive certificate and the seven-polynomial
Bernstein identity are fully included. Two complete ant audits and root
audit PASS; all four implementations rerun successfully. Independent
original-graph enumeration includes cyclic backgrounds. This is a pair
theorem within the stated family, not full NA or arbitrary incidence.

The NEW `proofnet24/C30-sidorenko/continuations/2026-10-02-regular-three-state/` proves the quantitative Sidorenko ML10 bound on ALL
regular symmetric equal-three-atom hosts, with arbitrary diagonals:
s^15+5s^11 E4+(265/18)s^9 E6. Two nonnegative generator cones cover the
entire stated domain. All3^10 assignments, nine-state transfer and243
left-label integration match every density coefficient. Full root and
ant audits and root reruns PASS. Fourth coefficient5 is sharp; sixth15
has an exact positive-host counterexample. Sixth265/18 is coefficientwise-
method optimum only. INVALID old root-fixed calculations are archived
with their erratum/reproducer and explicitly excluded. Classical methods
and known proper-coloring/two-spin special cases are credited prior art.

Historical novelty and external peer review remain unverified. Full
Boolean FEI, ordinary nearby-three-crossing FEI, general forest pair/NA,
unrestricted ML10 and Kaplansky/direct finiteness remain unresolved here.
Eight-state convolution, arbitrary-backbone adjacent, arbitrary unmatched-
background matching and parity-path candidates need their own records.

## Previous verified checkpoint: derived-12

Read `runs/derived-12/RESULTS.md` and the NEW `proofnet24/C30-sidorenko/continuations/2026-10-03-eight-state-convolution/` in full.
The final proof establishes t(ML10,8p(x+y))>=(sum p)^15 for EVERY nonnegative
eight-vector on uniformly measured F2^3, allowing arbitrary signed Fourier
spectra. This is a restricted host theorem, not unrestricted Sidorenko.
All 134,217,728 rooted assignments, forward Walsh transform, and independent
fundamental-cycle / inverse-Walsh routes match every one of 89,168 host and
3,964 Fourier coefficients. Exact affine smoothing covers 29 order orbits;
the remaining 1,344-order orbit has a complete 345,312-positive-coefficient
degree-17 multiplier certificate. Both full analytic audits PASS and all
root complete-map reruns exit zero. Raw-gap and once-multiplied negativity
are preserved as failed routes; division and all boundary cases are justified.

All 53 original completed files and every coefficient are supplied in the
79,144,580-byte original-data split xz archive, with full source generators,
byte hashes and reproduction instructions. Both uploaded binary part hashes
match local Git objects. Directly readable proofs, audits, source code and
smaller reports accompany it. The original pre-audit proof is preserved;
the FINAL copy and audits supply the completed status. False stronger cycle
and individual-block assertions are exact obstructions, not counterexamples
to Sidorenko. Numerical search is explicitly separated from proof.

Primary ML10 status and newer group-host papers were checked through
3 October 2026. Historical novelty and external specialist review remain
unverified. Larger Boolean groups, arbitrary regular hosts, unequal atoms,
full FEI, full forest pair/NA and Kaplansky/direct finiteness remain open here.
The arbitrary-backbone matching, all-port adjacent forest, and logarithmic
parity FEI candidates need their own full completion checkpoints.

## Previous verified checkpoint: derived-13

Read `runs/derived-13/RESULTS.md` and NEW `proofnet24/P14-probability-correlation/continuations/2026-10-03-backbone-and-all-ports/` in full. Two restricted
forest attachment theorems are complete. First, the whole disjoint matching
vector attached by rank-one spokes to three ports of ANY weighted backbone
is CNA under the stated backbone/matching conditioning and fields. The
actual split baseline's hypothetical triangle yields M²>=2BJF, closing the
full forced-subset/OR-law gates. The degree-N strict margin M²-2BJF>=M²/N
is independently derived. All proofs, zero cases and conditioning are full.
Ant and root full audits PASS; root reran all33,864 simple+106 weighted
Hessian examples, author33,588 conditional matching laws and independent
14,310 laws. Ordered/unordered event-check totals are distinguished.

Second, adjacent path marks among three new vertices with proportional
profiles to ANY number of vertices of ANY backbone are NC for every
activity, allowing outer edge rho>=0. Strictness is exactly rho>0 or ac>0
and some positive profile. Role reversal gives the exact mixture Gamma and
actual-apex LC bound Gamma<=U/s. R/D²=rho(1+rho)+ac[(1+2rho)U+acU²-b Gamma].
K and root full audits PASS; all2,440 author conditions and11 independent
literal whole-vertex cases rerun successfully. No arbitrary marked positions,
nonproportional spokes or all-indicator NA are claimed.

All earlier new arbitrary-H matching and three-port Bernstein intermediate
proofs are preserved with full audits and data and are superseded in scope,
not recycled as independent achievements. Previously completed code/proof
dependencies are credited. Four/five-port abstract-row failures are preserved
exactly; the negative five-port row violates apex LC and is unrealizable.
Known matroid log-concavity supplies the two completed theorem inputs;
entrywise Hessian signs are never assumed. Current primary sources and the
random-cluster/arboreal activity distinction were checked. Historical novelty
and external review remain unverified. Full forest pair/NA, full FEI, general
ML10 and Kaplansky/direct finiteness remain unresolved here. New all-port
disjoint-pair and ordinary regular odd-crossing FEI candidates need separate
checkpoints before completed status.

## Previous verified checkpoint: derived-14

Read `runs/derived-14/RESULTS.md` and NEW `proofnet24/P03-fei/continuations/2026-10-03-parity-and-regular-crossings/` in full.  The strongest
ordinary result proves FEI for every fixed finite-crossing weighted score
with input regularity `max|w_i|<=B||w||_2/sqrt(n)` and both output masses at
least fixed `r0>0`.  Crossings may be even or odd, arbitrarily located and
arbitrarily close; individual weights have no positive lower bound.  Output
balance yields two protected opposite-label Gaussian-mass intervals, a local
signed-translation lower bound, and then `I>=c sqrt(n)` by regular block
resampling.  Endpoint atoms are handled by the actual half-open/closed label
sets.  The repaired proof and full independent analytic audit PASS.  Author
checks pass 440 exact translations and 35,259 balanced truth tables; the
independent attained-cut suite passes 14,386 tie families and 28,772 label
inequalities.  The constant depends on `m,B,r0`; irregular or vanishing-
balance regimes and full Boolean FEI remain open.

An incomparable complete theorem allows arbitrary output bias for odd
crossing count when all normalized crossing locations are bounded.  It also
needs only input regularity, with no minimum weight or gap.  Its two full
audits and three rerun exact suites pass.  The older bounded-ratio theorem is
retained as a credited predecessor, not counted again.

For character outputs, if `g=F(g_1,...,g_m)` is any shared-input Boolean
combination of unate gates, then `H(chi_T g)<=[log2(4m^2+2q)+3]I(chi_T g)`,
`q=n-|T|`; full parity has constant `2log2(m)+5`.  Both full audits and the
author/independent implementations pass, including 1,053,853 exact
isoperimetric checks and 4,296 direct KL identities.  The weak logarithmic
bound is prior work and credited.  The separate bounded-alternation path
theorem gives a cotangent constant under nearly full parity; full parity of
a unate function has sharp constant2.  Ordinary unmodulated shared-input
gate closure is not claimed.

Failed unrestricted-three-crossing routes are preserved: the actual middle
trace inequality remains open; a broader trace statement diverges, TP2 has
an exact negative minor, and full crossing retention does not rescue the
largest-pivot local split.  Exhaustive weights1..8/dimension8 cover
47,693,379 triple cuts with maximum observed trace ratio3/2, finite evidence
only.  These are method obstructions, not FEI counterexamples.  Current
primary sources, including distinct 2026 subclasses, were checked.
Historical novelty and external review remain unverified.  Full FEI, full
forest/random-cluster, general ML10 and Kaplansky/direct finiteness remain
open in this campaign.  The new disjoint-pair forest-backbone proof requires
its own immutable completion checkpoint.

## Previous verified checkpoint: derived-15

Read `runs/derived-15/RESULTS.md` and NEW `proofnet24/P14-probability-correlation/continuations/2026-10-03-forest-backbone-disjoint-pair/` in full.  A complete
restricted forest theorem now covers two disjoint marked edges among four
new vertices with proportional spoke rows to ANY finite weighted FOREST
backbone and any number of common neighbors.  The marked indicators are NC
at every activity.  Strictness is exactly: all four row factors positive and
at least two positive-profile backbone vertices (or conditioned contracted
components).  Positive backbone/marked fields and coordinate/cylinder
conditioning of backbone edges are included.  Arbitrary-event conditioning,
individual spoke fields and nonproportional rows are not.

A direct Gaussian tree-covariance identity gives
`D(s)/Z_H=det(I+s B^(1/2) C B^(1/2))=product_i(1+s x_i)`.  The exact
four-core transfer retains all cumulants and yields
`(EF-AC)/(D^2abcd)=2(UT-Omega)+(a+b)(c+d)(Gamma^2+U^2T-2UOmega)`.
Both brackets have explicit nonnegative Stieltjes expansions; the first is
strict exactly at profile rank at least2.  No cyclic real-rootedness or
entrywise Hessian sign is assumed.

The full independent analytic audit PASSes.  Root reran the author checker
on all324 positive-probability partial conditionings and the independent
all-vertex DP on16,608 exhaustive exact plus1,200 seeded rational cases;
zero counterexamples/strictness mismatches.  Cyclic-backbone searches are
preserved as numerical evidence only.  Primary 2003/current2026 forest,
complete-graph and negative-dependence sources were checked.  Historical
novelty and external review remain unverified.  Cyclic backbones,
nonproportional attachments, arbitrary marked positions, whole-vector NA and
the full forest pair/NA conjecture remain open.  Full FEI, unrestricted ML10
and Kaplansky/direct finiteness also remain open in this campaign.

## Previous verified checkpoint: derived-16

Read `runs/derived-16/RESULTS.md` and NEW `proofnet24/C30-sidorenko/continuations/2026-10-03-colored-coefficient-obstruction/` in full.  This
checkpoint does NOT solve ML10 Sidorenko.  It proves the four-B/eleven-A
colored square density is nonnegative for every entrywise-nonnegative
symmetric 2x2 A and arbitrary real symmetric 2x2 B.  Its exact quartic
reduces to a 2x2 PSD test; `4CD-E^2` has66 nonzero monomials, all with
positive integer coefficients.  Independent 32-left-label elimination
reconstructs all1,024 source assignments, six grouped polynomials and the
complete determinant certificate.

The stronger coefficientwise binary-averaging route is now exactly refuted
inside the actual strictly-positive host class.  A mean-one sixteen-state
Boolean convolution kernel has sixth colored coefficient
`-809116997184077332220240713482240/1524^15`.  Literal 64-even-subset full
transfers, Walsh blocks and3,932,160 direct Fourier-flow terms independently
give the same integer.  The total averaging difference is positive and the
full density is about70.6086>1, so this is a method obstruction and NOT a
Sidorenko counterexample.

The C4 transfer/reflection/Walsh identities pass exact audits, but one
nontrivial-character contribution is negative for an admissible q=4 host;
termwise character positivity is therefore also invalid.  q=32/q=64 global
C4 searches are numerical evidence only.  Root reran all five exact programs
successfully.  Primary status sources were checked through3October2026;
historical novelty and external review remain unverified.  Global C4,
total averaging monotonicity, unrestricted ML10, full FEI, full forest
negative dependence and Kaplansky/direct finiteness remain open here.

## Latest verified checkpoint: derived-17

Read `runs/derived-17/RESULTS.md` and NEW `proofnet24/P14-probability-correlation/continuations/2026-10-03-weighted-cycle-disjoint-pair/` in full.  The
derived-15 disjoint-marked-edge theorem now extends from forest backbones to
EVERY arbitrarily weighted cycle backbone with an arbitrary nonnegative
common profile.  For four proportional spoke rows and the two disjoint
marked edges, NC holds at every activity.  Strictness is exactly four
positive row factors and at least two positive profile entries.  Every
positive-probability rim cylinder conditioning is included, using positive
contracted profile blocks.

The new one-apex polynomial theorem is exact:
`D(s)=tr(product_i T_i(s))-2 product_i lambda_i`, with
`T_i=[[1+lambda_i+s beta_i,s beta_i lambda_i],[1,lambda_i]]`.
At a zero, monodromy gives a quasi-periodic tridiagonal eigenproblem.  The
weights `m_(i+1)=m_i/[lambda_i(1+lambda_i)]` make it Hermitian, including
the wraparound because `|rho|^2=product_i lambda_i(1+lambda_i)`.  Hence all
roots are negative real.  Zero activities/profiles and unequal parallel C2
are fully handled.  The audited arbitrary-backbone four-core identity then
supplies the Rayleigh inequality through its two Stieltjes sums.

The full independent analytic audit PASSes.  Its standalone checker matches
three coefficient constructions and exact root multiplicities in148 apex
cases, eight literal marked graphs, and all106 partial rim conditionings
(88 strict,18 equality), with zero failures.  The author checker adds67 apex
and five literal marked cases.  A separately audited Chebyshev proof covers
the uniform specialization.  Closest current unit-wheel prior work is
credited.  Historical novelty and external review remain unverified.  This
does not cover nonproportional rows, multicycle backbones or whole-vector NA;
the full forest conjecture, FEI, unrestricted ML10 and Kaplansky/direct
finiteness remain open.

## Previous verified checkpoint: derived-18

Read `runs/derived-18/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-cactus-backbone-disjoint-pair/`
in full.  The derived-17 disjoint-marked-edge theorem now extends from one
weighted cycle to EVERY finite weighted CACTUS backbone: every block may be
an edge or a cycle, so one connected backbone may contain arbitrarily many
cycles arranged through articulation vertices.  With arbitrary nonnegative
common profile and four proportional spoke rows, the two disjoint external
marked edges are NC at every activity.  Strictness is exactly four positive
row factors and at least two positive profile entries.  Every positive-
probability backbone cylinder conditioning is included, with strictness from
positive contracted profile blocks.

The stronger new input is a profile-uniform determinant representation
`D_G(z)=c det(K+sum_x z_x q_xq_x*)`, with `K>0`.  The cycle transfer from
derived-17 supplies the cycle block.  An exact rank-one leaf lift and a new
one-vertex-sum Schur gluing preserve the representation; induction over the
cactus block tree completes the proof.  The articulation variable is
explicitly split as `z_u^(1)+z_u^(2)=z_u`, closing the only ambiguity found
by the adversarial audit.  The full multivariate apex-spoke polynomial is
therefore real stable; its whole spoke marginal is strongly Rayleigh and
negatively associated under spoke fields/coordinate conditioning.  This does
not assert NA jointly with backbone or external marked edges.

The fresh independent analytic audit PASSes.  The author checker passes24
determinant leaf lifts,12 literal one-sums,44 unicyclic/pseudoforest/cactus
root suites,10 marked graphs and78 positive-probability conditionings, while
skipping3 zero measures.  The independent checker passes20 normalization,
12 abstract Schur,12 literal split-profile and12 genuine cactus root cases,
one figure-eight marked graph, and64 positive-probability conditionings
(32 strict,32 equality), skipping17 zero measures.  Exact Fraction,
determinant, literal-forest and Sturm/gcd arithmetic are distinguished from
proof.

Brand--Dell--Roth's apex component identity, Huang's reductions, Bado's
unit-wheel theorem, current2026 forest papers and Borcea--Branden--Liggett
strong-Rayleigh theory are credited.  Historical novelty and external review
remain unverified.  A theta or other 2-connected block with two independent
cycles, nonproportional rows, backbone/marked whole-vector NA, and the full
forest conjecture remain open.  Full FEI, unrestricted ML10 and
Kaplansky/direct finiteness also remain open in this campaign.

## Previous verified checkpoint: derived-19

Read `runs/derived-19/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-theta-side-uniform/`
in full.  The cactus boundary is now crossed for a genuine 2-connected
block with two independent cycles.  For `K_(2,3)`, give the three edges at
one degree-three-side vertex activity `p>0` and the other three activity
`q>0`.  The full five-variable apex-spoke forest polynomial is real stable
for every `p,q`.  Hence its spoke marginal is strongly Rayleigh and NA under
spoke fields and positive-probability spoke conditioning.  Every profile-ray
polynomial has only strictly negative roots.  The audited four-core transfer
then gives NC for the two disjoint external marked edges with four
proportional rows at every positive pair of marked activities; strictness is
exactly four positive row factors and at least two positive profile entries.

The proof reduces the four spoke-pair orbits to quadratic Rayleigh
differences.  Shifts by `p+q+1`, `3p+1`, and `3q+1` factor every discriminant
through four explicit positive-definite binary forms.  All degenerate
leading-coefficient boundaries are evaluated exactly.  This is global
multivariate stability, not a finite root experiment.

The independent audit PASSes.  The author checker enumerates all2,048
augmented subsets, retains712 forests and verifies18 exact symbolic
certificates.  The independent checker instead uses54 backbone forests and
their component products, rederives the18 identities, checks24 exact
rational root cases and six direct marked graphs (four strict, two equality),
with no counterexamples.  It caught only boundary/stale wording issues,
which are incorporated.

Six unrelated backbone activities, arbitrary theta subdivisions,
two-terminal/series-parallel closure, backbone conditioning, nonproportional
rows, and joint backbone/marked NA remain open.  A 36,000,000-evaluation
six-weight countersearch found no negative value and is numerical evidence
only.  Current primary sources are credited; historical novelty and external
review remain unverified.  The full forest conjecture, full FEI,
unrestricted ML10 and Kaplansky/direct finiteness remain open.

## Previous verified checkpoint: derived-20

Read `runs/derived-20/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-theta-one-arm/`
in full.  A second genuine non-cactus family is now proved.  In `K_(2,3)`,
give both edges of one length-two arm activity `rt` and the other four edges
activity `t`, for arbitrary `r,t>0`.  The full five-variable apex-spoke
forest polynomial is real stable.  This is incomparable with derived-19's
endpoint-side `p,q` family: it breaks arm symmetry instead.  The spoke
marginal is strongly Rayleigh/NA under spoke fields and positive-probability
spoke conditioning; every profile ray has strictly negative roots.  The
four-core transfer gives the same proportional-row disjoint-marked-pair NC
corollary at positive marked activities, with the exact support strictness.

The proof reduces five pair orbits to quadratic Rayleigh certificates after
shifts `2t+1`, `2rt+1`, and `t(r+2)+1`.  Five binary-form determinants factor
into manifestly positive products through one coefficientwise-positive
polynomial `S`; every degenerate boundary is evaluated exactly.

The independent audit PASSes without correction.  The author checker
enumerates all2,048 augmented subsets, retains712 forests and verifies22
symbolic identities.  The independent component-factor checker uses54
backbone forests, independently verifies the22 certificates, 24 exact
rational root cases and six direct marked graphs (four strict, two equality),
with no counterexamples.

The combined three-parameter weights `pr,p,p,qr,q,q` remain open: one
internal-pair discriminant leaves a genuine bivariate quartic, with neither
SOS nor counterexample obtained.  Two-terminal gluing, six unrelated
weights, theta subdivisions, series-parallel closure, backbone conditioning,
nonproportional rows and joint backbone/marked NA are also open.  Historical
novelty and external review remain unverified.  The full forest conjecture,
full FEI, unrestricted ML10 and Kaplansky/direct finiteness remain open.

## Previous verified checkpoint: derived-21

Read `runs/derived-21/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-theta-three-parameter/`
in full.  The two preceding theta families are now unified.  On `K_(2,3)`,
the six backbone activities may be `(pr,p,p;qr,q,q)` for arbitrary
`p,q,r>0`.  The full five-variable apex-spoke forest polynomial is real
stable.  This strictly subsumes derived-19 at `r=1` and derived-20 at
`p=q`.  Its spoke marginal is strongly Rayleigh/NA under spoke fields and
positive-probability spoke conditioning; every profile ray has strictly
negative roots.  The audited four-core transfer gives the proportional-row
disjoint-marked-pair NC corollary at positive marked activities with exact
support strictness.

Seven pair orbits reduce to quadratic Rayleigh certificates through six
positive-definite binary forms.  Their determinants factor into manifestly
positive products involving two displayed coefficientwise-positive
polynomials.  The decisive repair to the initially stalled route is to
collect the special--ordinary internal-pair difference in the unused
ordinary spoke, not an endpoint; the apparent quartic then becomes a binary
endpoint form.  Every degenerate boundary is exact.

The independent audit PASSes without correction.  The author checker
enumerates all2,048 augmented subsets, retains712 forests and verifies31
symbolic identities.  The independent component-factor checker uses54
backbone forests and independently verifies the31 certificates, 24 exact
rational root cases and six direct marked graphs (four strict, two equality),
with no counterexamples.

Three unrelated arm multipliers, six arbitrary weights, theta subdivisions,
two-terminal/series-parallel closure, backbone conditioning, nonproportional
rows and joint backbone/marked NA remain open.  The 36,000,000-evaluation
six-weight search remains evidence only.  Historical novelty and external
review are unverified.  The full forest conjecture, full FEI, unrestricted
ML10 and Kaplansky/direct finiteness remain open.

## Previous verified checkpoint: derived-22

Read `runs/derived-22/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-theta-rank-one/`
in full.  The theta result now covers the full positive rank-one `2 x 3`
edge-weight matrix.  On `K_(2,3)`, the six backbone activities may be
`(pa,pb,pc;qa,qb,qc)` for arbitrary `p,q,a,b,c>0`.  The complete
five-variable apex-spoke forest polynomial is real stable.  This strictly
subsumes derived-21 (`a=r,b=c=1`) and removes all symmetry among the three
arms.  The spoke marginal is strongly Rayleigh/NA under spoke fields and
positive-probability spoke conditioning; every nonzero profile ray has
strictly negative roots.  The audited four-core transfer gives the inherited
proportional-row disjoint-marked-pair NC corollary.

The ten spoke pairs reduce by parameter permutation to three exact quadratic
templates.  Four positive-definite binary-form certificates control all
leading coefficients and discriminants.  The hard internal-pair mixed
coefficient is not coefficientwise positive, but its determinant factors
into three positive linear factors and one displayed coefficientwise-positive
polynomial `S`.  Every degenerate boundary is evaluated exactly.

The author checker constructs the 32-term polynomial from 54 backbone forests
(712 augmented forests at unit weights), verifies thirteen exact structural
identities and four binary-form certificates, including a 411-term expanded
determinant.  The independent checker reconstructs the polynomial separately
and PASSes 18 symbolic identities, 1,200 exact rational all-pair evaluations,
24 exact profile-root cases and six direct marked graphs (four strict, two
equality), with no counterexamples.  It explicitly checks both endpoint--
internal axes and the signed-mixed-coefficient internal determinant.

Six arbitrary non-rank-one activities, theta subdivisions,
two-terminal/series-parallel closure, backbone conditioning, nonproportional
rows and joint backbone/marked NA remain open.  Current primary sources are
credited; targeted search found no exact prior theorem, but historical
novelty and external review remain unverified.  The full forest conjecture,
full FEI, unrestricted ML10 and Kaplansky/direct finiteness remain open.

## Latest verified checkpoint: derived-23

Read `runs/derived-23/RESULTS.md` and NEW
`proofnet24/P14-probability-correlation/continuations/2026-10-03-theta-six-weight/`
in full.  The rank-one restriction is now completely removed.  For arbitrary
positive activities `(a,b,c;d,e,f)` on the six edges of `K_(2,3)`, the full
five-variable apex-spoke forest polynomial is real stable.  This exhausts all
positive weightings of the unsubdivided theta backbone.  The spoke marginal
is strongly Rayleigh/NA under spoke fields and positive-probability spoke
conditioning; every nonzero profile ray has strictly negative roots.  The
audited four-core transfer gives the inherited proportional-row
disjoint-marked-pair NC corollary.

The ten spoke pairs reduce under simultaneous parameter relabeling to three
exact quadratic templates.  The hard internal discriminant is not
coefficientwise positive: each diagonal has31 negative coefficients among166
terms.  Its determinant instead factors into three strictly positive crossed
two-column AM--GM forms and a coefficient-positive54-term polynomial.  The
determinant prevents a diagonal sign change on the connected positive
orthant; its exact all-ones value is432.  Every zero-leading boundary is
evaluated exactly.

The author checker reconstructs the32-term polynomial from54 backbone
forests and verifies19 structural identities plus the4,422-term expanded
internal determinant identity.  The independent component-factor audit
PASSes17 symbolic identities,1,000 exact rational all-pair evaluations,24
exact profile-root cases and six direct marked graphs (four strict, two
equality), with no counterexamples.  It independently validates the crossed
`T` factors and the connected-domain inertia argument at exact basepoint
`108 I`.

Theta subdivisions, two-terminal/series-parallel closure, backbone
conditioning, nonproportional rows and joint backbone/marked NA remain open.
Current primary sources are credited; targeted search found no exact prior
theorem, but historical novelty and external review remain unverified.  The
full forest conjecture, full FEI, unrestricted ML10 and Kaplansky/direct
finiteness remain open.

## Next priorities

The derived M_TWINS_ARBITRARY_CORE_COROLLARY.md further allows every terminal count m>=4 over an arbitrary weighted core, by an audited Schur-complement reduction. It gives an explicit adjugate sum of squares for H2 and a high-fugacity marked-pair theorem, not the full forest conjecture.

Develop a substantial further result on FEI, the full forest/random-cluster problem, Sidorenko, or K-theory; do not spend the entire continuation rechecking already proved queueing identities. For Whitt, the all-server finite-mixture result, general finite-second-moment coefficient theorem, and strictly positive bounded continuous DFR comparison theorem are proved and audited. Investigate historical priority and genuinely new extensions; do not recycle the old DFR gap as unresolved. The finite-rate larger-mean example also defeats strict increasing-convex comparison at every nonnegative threshold. For forests, the full arbitrary-order regional-absorption induction now proves every high-fugacity marked-pair case. Pursue all-fugacity marked-pair negativity, a quantitative threshold, or a further genuinely new extension; do not recycle the old H3zero/transfer gap as unresolved. K4 chains show arbitrarily long leading zero strings, so any finite coefficient list is insufficient. For FEI, the deterministic-LTF theorem is now complete internally; pursue unrestricted Boolean FEI or a genuinely new audited extension, and do not recycle the LTF, strengthened-deficit, balanced-formula, regular-weight or fixed-band results as new achievements. The parallel-slab, strict-separated crossing, finite wide-gap union, and maximum-run exceptional-layer theorems are now complete internally; build beyond them. Three arbitrary crossings have a certified largest-weight local obstruction, and arbitrary endpoint equality has a certified cancellation gap. The generic signed-split I-Var conversion, strong balanced slab-gate formulas, arbitrary parity-modulated LTFs and disjoint-product/mixed-tree corollaries are now complete internally; build beyond them. Independent finite-fugacity forest deletion/contraction and Sidorenko operator/perturbation routes remain active. Arbitrary input-biased full entropy needs correct normalization (a rare dictator already obstructs a variance-influence-only universal bound). The prior monotone maximum-influence and separator obstructions remain valid and limit extensions beyond parallel slabs. Any new result must include a full proof or rigorously stated gap and independent verification. Preserve the full derivations of all further results in GitHub.

## Persistence protocol

Write full proofs, derivations, failed routes, code, exact certificates and independent audits to immutable `research/2026-10-02-major-problem-push/runs/<actual-run>/` folders, and to the appropriate existing problem track when appropriate. Update only this CURRENT.md in place. Read the branch before a push; preserve unrelated paths; use a fast-forward update without force. A complete proof plus independent audit and current source check is required before claiming an open target solved. Record priority as unverified unless adequately established.

The authorized continuation window ends at 2026-10-03T08:51:21+03:00 (2026-10-03T05:51:21Z). Nine hourly follow-up invocations were created; an invocation after the deadline should report final state only. The automation is separate from pre-existing schedules. It does not imply uninterrupted execution. No emails, other external publishing, or alteration of other automations is authorized.
