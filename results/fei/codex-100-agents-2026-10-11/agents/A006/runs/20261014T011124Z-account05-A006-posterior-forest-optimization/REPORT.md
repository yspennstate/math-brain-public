# A006 stage 4: complete rooted-star mass for unmatched coordinates

## exact target, quantifiers, hypotheses and units

A006, B02, G-J-COST / C020. For EVERY finite nonempty simple graph G on its covered physical variables, positive graph DNF f_G=OR_(edges uv)(x_u AND x_v), both globally fixed endpoint orders, pi_e=1/4, and any globally fixed strictly positive feasible incidence weights lambda_e, I construct an exact complete conditioned output lower mass on EVERY covered nonempty set. The family uses all inclusion-maximal matchings in G[A] and completes unmatched vertices by actual rooted stars. It retains posterior witness entropy, all size/subset/count/multiset/root/label factors, and distinct actual chronological events. Costs are in bits and the original gamma is 6/5. The reference is never selected as a function of sampled A.

This closes A009's matching-sector coverage defect, including all 104 positive-spectrum zero-mass cases on four labelled variables. It gives an explicit computable positive mass and lower bound for arbitrary graphs, but no dimension-independent expected influence payment. Full FEI remains OPEN. Exact rational log intervals also certify complete nonempty cost C_MS<5I for all 63 nonempty four-variable graph tables at each of two fixed weight choices; this is finite reference validation, not a new FEI class or an all-graph constant.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, snapshot 2026-10-14 01:10 UTC, the stream's full B02 STREAM_NOTES.md v2 dated 2026-10-11 23:35 UTC, own STATUS.md and the full EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Long board output required follow-up chunks and a middle-section reread. The board reports independent A007/A008/A010 reconstructions of my determinant v1; these are observed local review reports, not evidence of shared registry adoption. The stale lead's first dictionary/majority instructions were completed earlier. This stage consumes the new complete-probability interface and the precisely identified unmatched-component dependency before another cost-payment candidate.

Read A008 stage3 REPORT.md, COMPLETE_MASS.md and CLAIMS.json in runs/20261013T222820Z-account05-A008-gate-label-compression. Read A009 stage3 REPORT.md and full MATCHING_CERTIFICATE.md in runs/20261013T235139Z-account05-A009-fractional-incidence-optimization. Read A014 stage3 REPORT.md and its warning that zero conditioned remainder does not eliminate off-clause spectrum, and A010 stage3 REPORT.md plus STATUS.md describing independent-sector mass and the missing non-independent sector. Revisited the original forests.tex queue definition, original root conditioning and partition interface; prior complete baseline/campaign/paper reads are retained. No brain query, outside theorem or author checker was used. out/SOURCES.json pins actual source paths and saved bytes; mutable board hashes describe final-save bytes.

## complete derivation or exact first unsupported line

STAR_COMPLETION.md proves the exact arbitrary-graph construction. A maximal matching M in G[A] leaves an independent unmatched set U. Each unmatched u chooses any neighbor nu(u); it lies either at a matched coordinate or outside A. Matching gates own pairs. Unmatched gates own singleton u, are children of the gate owning nu(u) when that coordinate is matched, and are isolated roots otherwise. No two singleton gates can coincide, since that would require an edge within U. The entire ownership-incidence graph is exactly a disjoint union of outgoing stars and isolated roots, so every specified event obeys the original source-SCC root restriction.

For matched e={v,w}, let h_v,h_w be child counts at the two attachment coordinates and c_e=h_v+h_w; let b be the number of outside-A neighbor choices. The exact mass for M is

    Q_M(A)=D^-1 product_(e in M)(lambda_e/24)
              *sum_nu [product_(u in U)(lambda_(u,nu(u))/8) *4^-b
                         *product_(e={v,w} in M) h_v!h_w!/((c_e+1)^2(c_e+2))],
    D=product_all_edges(1+lambda_e/4)-1.

The matched root pays pi*t_pair=1/24; a singleton child pays t_singleton*Pr(c=0)=1/8; an external singleton root additionally pays pi=1/4. A parent star pays its count law and the uniform two-coordinate multiset factor, and h_v!h_w! counts only genuine chronological child-label sequences. Initial roots and different attachment coordinates stay in fixed order. Both endpoint orders make original theta identically one, so t_singleton=1/4 and t_pair=1/6 exactly.

The actual queue's pair-owned subsets recover M, singleton subset/gate IDs recover nu, and appended-child draws recover parent, attachment and chronological choices. Thus different matchings, choices and slot permutations are disjoint actual events. Summing all maximal M gives Q_MS(A)<=Q_part(A)<=Q_*(A). It is strictly positive for every covered A. At conditional posterior eta(r)=q(r)/Q_MS(A), E[-log q]-H(eta)=-log Q_MS(A); this is output aggregation rather than credit for duplicate descriptions or a physically free record.

Using (c+1)^2(c+2)<=2*6^c and discarding h!>=1 gives the explicit lower bound

    Q_M(A)>=D^-1*48^(-(|M|+|U|))*product_(e in M)lambda_e*product_(u in U)r_u,
    r_u=sum_(v neighbor u)lambda_uv.

Summing that bound over maximal matchings gives a computable positive L_MS(A), so complete cost is at most -log2 L_MS(A). It specializes on independent sets to the already-known exact mass D^-1 product_(u in A)(r_u/32). That specialization is a consistency check, not a repeated independent-sector theorem. Enumerating maximal matchings can be exponential; no polynomial-time claim is made.

REVIEW_A008.md independently reconstructs the WHOLE formal A008 complete-mass v1, unchanged statement hash, including actual event bijection, root odds, all operator factors, beta/exponential/simplex moments, coefficient bounds, final ambiguity and universal boundary. Its formal statement HOLDS without repair. The auxiliary sentence 'each t_u=1/2 (uniform singleton choice)' in the source's star example is ERROR: on width two, both orders give t_singleton=1/4, and one order gives theta/[2(1+2^-gamma)]. This sentence is not used in the formal mass identity or stripped-star coefficient. I record formal acceptance with that scoped source error, not unqualified source acceptance. A009's matching proof correctly uses 1/4 and is unaffected. Any consumer that actually substituted 1/2 for t must recompute its probabilities.

The exact first unsupported all-graph line is an influence-paid expectation of the full mass, for one globally fixed feasible vector:

    Var(f_G)log2 D - sum_(A!=empty)P_f(A)log2 [sum_M 48^(-(|M|+|U|))
                                     product_(e in M)lambda_e product_(u in U)r_u]
       <=K I(f_G)

with absolute K. Positivity and finite <5I certificates do not establish this line. A sharper posterior should preserve the exact factorial factor above instead of discarding it. Nothing in this stage replaces raw indicator-sum error by conditioned local norms, the substitution A014 has refuted. Higher-width/arbitrary Boolean prime tables still lack this maximal-matching star decomposition and universal payment.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the actual trace jobs. Pilot: every one of 7 nonempty labelled n=3 graph tables, both weight choices, 74 covered graph-set-weight cases, 102 distinct actual traces/neighbor assignments; 1,577 assertions PASS in 0.043153 seconds. Full: all 63 nonempty labelled n=4 graphs and every covered nonempty A, both weights lambda_e=1/Delta and lambda_uv=1/(deg u+deg v); 1,490 covered cases, 2,984 neighbor-assignment cases and 3,080 distinct actual traces. Full check passed 32,744 assertions in 0.641297 seconds. Exactly all 104 positive-spectrum sets with zero A009 matching mass now have positive completed mass, verified independently.

Integer FWHT, Parseval and independently counted physical pivotal edges validate each actual Boolean spectrum/influence. Each chosen matching's entire ownership-incidence graph is independently checked against the prescribed star structure. Every chronological event is executed by the queue, its probability is multiplied from the original conditioned root odds INCLUDING absent roots, original size/subset probabilities, child counts, multiset choices and lambda-weighted child draws, and traces are deduplicated across all matchings/neighbor choices for that A. Rational closed-form mass, positive lower bound and total output subprobability are checked exactly. The independent A008 operator review covers 209 exponent vectors; no author code is imported.

COST_SPEC.json preceded separate interval jobs on the same saved functions and masses. Twenty atanh terms after binary range reduction give ln y with remainder <=2*z^41/[41(1-z^2)], then outward division by certified ln2 endpoints. All operations use Fraction, and the logarithm signs are positive for inverse subprobability mass. Pilot: 14 graph-weight cost cases, 96 interval assertions, 3.190150 seconds; certified C_MS<4I at n=3. Full: 126 graph-weight cost cases, 1,526 interval assertions, 1.054275 seconds; certified C_MS<5I at n=4. The maximum displayed ratio upper is approximately 4.274746610302, at K_2,2 under the endpoint-degree weights; the rigorous signs use the stored rational endpoints, not that display. This is not an optimized weight/posterior infimum or an all-n estimate.

Total successful assertions across both pilots and full jobs: 35,943. All computations were fixed before their respective jobs, with no symmetry reduction, automatic dimension increase, heavy job, GPU, window or background process. The 100 MB estimate is below the 300 MB memok threshold. Each completed graph/cost case was checkpointed. All mathematical runtimes are measured helper times; early shell reads/startup were slow and are not counted as computation evidence.

Commands from A006:

    python -X utf8 runs/20261014T011124Z-account05-A006-posterior-forest-optimization/code/check.py --pilot
    python -X utf8 runs/20261014T011124Z-account05-A006-posterior-forest-optimization/code/check.py
    python -X utf8 runs/20261014T011124Z-account05-A006-posterior-forest-optimization/code/cost.py --pilot
    python -X utf8 runs/20261014T011124Z-account05-A006-posterior-forest-optimization/code/cost.py

out/CHECK_3.json, CHECK_4.json, A008_OPERATOR_REVIEW.json and COST_3.json/COST_4.json preserve the exact certificates. The analytic graph/weight-continuum proof, not extrapolation from finite cubes, supplies the arbitrary-graph mass formula and positivity. No failed mathematical computation was hidden.

## proof dependencies and changed downstream conclusions

The original complete queue is the baseline premise. A008's exact complete-mass formal statement is independently reconstructed before use, and the new graph formula is also derived directly from the original probabilities. My earlier determinant v1 is not assumed to be exact queue mass. A009 supplies the identified matching defect and correct two-order probability interface; its complete-graph bound/KKT is read but not adopted as a whole independent review here. A010 identifies the non-independent spectral sector; A014 rules out a conditioned-error shortcut. None of their unreviewed broader results is a proof premise.

The completed star family resolves arbitrary-graph coverage, not universal influence payment. It directly extends the existing exact independent and near-perfect-matching sectors rather than opening another known-class calibration. The separate source error affects only an auxiliary t evaluation; A008's unchanged formal mass claim and A009's correct matching ledger remain valid. Shared claim-status changes and author-file corrections are left to their owners. No broad universal payment candidate is opened.

## one next mathematical action and independent reviewer

Next: combine A010's local incidence cancellation on non-independent graph spectra with the exact maximal-matching star mass, retaining h_v!h_w! rather than the coarse 48 bound; bound the spectral expectation of the remaining matched-root label and unmatched row-mass costs under one fixed feasible vector. Produce one paid expected-cost inequality or an exact actual-Boolean obstruction. For wider tables, first identify the precise failure of the maximal-matching independence step rather than assuming the graph proof transfers. A008/A009 should independently reconstruct (1)'s root/count/multiset/chronological bijection; A086/A094 should challenge the weight-continuum lower bound, cost certificate, and auxiliary-error scope. No messages were sent.

## actual persistence receipts or precise save blocker

The requested four protocol files, STAR_COMPLETION.md, REVIEW_A008.md, two frozen specs, code and exact outputs are saved here. out/SOURCES.json pins source bytes; out/RECEIPTS.json validates exact field sets and local sizes/SHA256. STATUS.md has exactly STATE/NEXT lines, and WORKLOG.md/LEARNED.md are updated only in A006. All artifacts are below 20 MB. Other agent/shared trees, git, Brain, trading directories and external services were not modified. New graph interface independent review, supervisor adoption/copying and mirror verification remain pending; no local save blocker exists.

## Universal bridge

C020 / PI-J moves by closing the matching-sector coverage defect on every graph prime table with an exact complete actual-run mass and explicit positive lower bound; all 104 finite positive-spectrum failures are covered and n=4 complete reference costs are certified below 5I, while A008's formal arbitrary-reference mass receives a scoped independent acceptance with one auxiliary probability error isolated. The unknown universal K is unchanged: the spectral expected matched-root label and unmatched row-mass bill is still unpaid, and higher-width prime tables need a replacement for maximal-matching independence. NEXT combines the new whole-set star posterior with A010's live non-independent incidence cancellation at that exact expectation gap, so it advances the general bridge rather than repeating clique, bipartite or read-once FEI calibrations.
