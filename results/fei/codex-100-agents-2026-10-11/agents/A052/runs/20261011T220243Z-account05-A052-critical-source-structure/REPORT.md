# A052 / B11: critical-source structure

## exact target, quantifiers, hypotheses and units

For every Boolean sign f on every finite uniform cube, derive a structural restriction under either (i) R(g)<=R(f) for every proper physical restriction g, or (ii) H(f)>KI(f) and H(g)<=KI(g) for every proper physical restriction, at a fixed finite K>=0. Constants have H=I=0 and are never divided by I. A dimension-minimal K-witness satisfies (ii). Entropy is in bits except the explicitly named historical raw-indicator comparisons and natural-unit certificates. The new conclusion concerns every rank-r binary spectral syndrome VS, every physical pivot block A of size r with V_A invertible, and every syndrome word y0. It is not a connected-support theorem or a FEI solution.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY; A051--A055 PACKET_STATUS entries; STREAM_NEXT_ACTIONS B11; plan accounting/obstruction and B11 sections, especially lines 433--451 and 830--860. Earlier B05, B19 and B09 run REPORTs were inspected; the accepted B05 no-go remains in force, while B09's pending biased theorem is not a premise. BOARD.md was read at start (21:55 UTC snapshot) and again before persistence; the latter shows A051's completed stage. claude/B11/STREAM_NOTES.md was absent at both checks, so no lead instruction is asserted.

Read supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and relevant sources: BLOCK_RESTRICTION_IDENTITY sections 1--3 (full channel proof), ERASURE_REDUCTION sections 1--4, ADDENDUM_11_44, ADDENDUM_11_26, and ROUTE_MAP_CURATED's physical/component/critical scope sections. The current threshold 38-page text section 8.4, Proposition 8.9 and Corollary 8.10 was read for activation; its earlier 29-page version's composition/strong-entropy/final scope sections were inspected. Both percolation text introductions and Theorems 1.1--1.3 were inspected: their geometric criticality is unrelated to ratio criticality here, and no percolation theorem is a premise. The A051 REPORT, EXTREMALITY_DEFINITION, EXISTENCE_AND_LIMITS and CLAIMS were read and independently reconstructed in REVIEW_A051.md.

The original seven-bit component report was fetched read-only from yspennstate/math-open-problems at 31c201a0a8caef323c65abe964ff8ed4b702fc81, path proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/component-ratio-counterexample/REPORT.md, blob 978c180155e1a25d4d8f34988b5216269c7b83c3. Its complete returned text is saved in out/COMPONENT_RATIO_SOURCE.md. Source byte hashes and locators are in out/SOURCE_MANIFEST.json. Brain recall was read-only and supplied no mathematical premise. No novelty or literature-priority claim is made.

## complete derivation or exact first unsupported line

The complete statement and main derivation are CRITICAL_SOURCE_STRUCTURE.tex, equations (1)--(3). Put kappa=2/ln2. For C=A^c, let Y=VS and e0(t)=V_A^-1(y0+V_Ct). Define b=E|S_A+e0(S_C)| and epsilon=P(Y!=y0). The physical Hamming weight gives b<=r epsilon. The partial Fourier channel v_t(x)=sum_e fhat(e,t)chi_e(x) has child probabilities v_t(x)^2, whose mean is the S_C marginal. Hence

    L_A=H(S_A|S_C)+J_A=H(Y|S_C)+J_A.

For each t, multiply v_t by chi_e0(t). This leaves its square unchanged and shifts its Fourier labels by e0(t). Logarithmic Sobolev applied to the absolute value of this real function gives

    (ln2) J_A=sum_t Ent(v_t^2)
        <=2 sum_(e,t) |e+e0(t)| fhat(e,t)^2 = 2b.

Here is a self-contained justification of the analytic inequality used. For a nonnegative two-point function (u,v), homogeneity and symmetry reduce to (t,1), t>=1. Twice the difference between the desired Dirichlet bound and Ent is

    F(t)=(t^2+1)ln((t^2+1)/2)-2t^2 ln t+(t-1)^2.

F(1)=0 and F'(t)=2t ln((t^2+1)/(2t^2))+2(t-1). The difference 1-1/t-ln(2t^2/(t^2+1)) vanishes at one and has derivative (t-1)^2/[t^2(t^2+1)]>=0. Thus F'>=0. Symmetry F(t)=t^2 F(1/t) and continuity handle the remaining values. Entropy tensorization then proves Ent(w^2)<=1/2 sum_i E(|w(x)|-|w(x+e_i)|)^2<=2 sum_i ||D_i w||_2^2 for real w on a uniform product cube. Tensorization follows inductively by conditioning and convexity of Ent; no biased inequality is imported. Parseval after each fiber's character shift yields the displayed 2b. Zero marginal fibers vanish identically.

Criticality is used only in the physical-child deficit comparison:

    L_A-R(f)I_A=-E[H(f_x)-R(f)I(f_x)]>=0.

Consequently R(f)I_A<=H(Y|S_C)+kappa b. In the threshold-critical form the left side is KI_A+D_K(f). Since H(Y)<=h2(epsilon)+epsilon log2(2^r-1), the explicit concentration obstruction is

    KI_A+D_K(f) <= h2(epsilon)
        +epsilon log2(2^r-1)+kappa r epsilon.

For a nonempty flip mask u and a pivot i in its support, r=1, b=epsilon_u, where epsilon_u=(1-|E f(x)f(x+u)|)/2. Thus KI_i+D_K(f)<=h2(epsilon_u)+kappa epsilon_u. In particular a positive-entropy ratio-critical source in essential coordinates has no exact signed translation symmetry. This strengthens the exact-symmetry removal baseline quantitatively, without a uniform positive lower bound when influence vanishes.

PRUNING_SCOPE.md replays both historical failures, checks their higher-ratio physical restrictions in the inherited indicator orientation, and separately certifies that both sign lifts have actual point-defect descendants with ratio more than 1/2 larger. Components are never assumed to be descendants. Arbitrary-core activation remains FEI-hard as a class, but its amplified K-violations contain smaller K-violating physical cores and fail dimension minimality. Descendants are not assumed critical. The reviewed raw-AND-power degree-moment obstruction is retained at its distinct scope.

First unsupported line: for some absolute finite K, every prospective dimension-critical K-witness admits a proper physical pivot block with H(VS|S_C)+kappa b<=KI_A. Such a block would contradict the strictly positive deficit. The present result supplies a necessary spectral-disorder restriction and a sufficient certificate for extracting a better child; it does not prove that an affordable block exists universally or pay component excess.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications are out/FROZEN_SPEC.json and out/FROZEN_SPEC_SIGN_REPLAY.json, saved before their respective computations. No truth-table symmetry reduction, optimizer search, randomness, automatic dimension growth or GPU. The systematic form V_A=identity represents all invertible pivot submatrices by row relabelling, which preserves syndrome entropy and physical mismatch b; every tail matrix and every y0 is checked.

Executed from A052:

    python -X utf8 runs\20261011T220243Z-account05-A052-critical-source-structure\code\check_structure.py --pilot
    python -X utf8 runs\20261011T220243Z-account05-A052-critical-source-structure\code\check_structure.py
    python -X utf8 runs\20261011T220243Z-account05-A052-critical-source-structure\code\check_sign_lifts.py

Pilot: PASS, 895 assertions, 22 labelled tables through n=2, 200 syndrome cases and both fixed component witnesses, measured helper runtime 0.126 seconds (rounded). Full main check: PASS, 65,307 assertions, 278 tables through n=3, 20,680 syndrome/pivot/y0 cases, 48 positive-entropy physical-ratio-critical tables across these dimensions, two component witnesses and six activations; measured helper runtime 4.537228 seconds. Sign replay: PASS, 14 assertions, two fixed sign lifts and descendants; helper runtime 0.038350 seconds (rounded). Process startup/tool wall time is separate. Peak RAM was not measured; the frozen estimate 45 MB is below the 300 MB memok threshold, and no heavy job was needed.

Spectra and edges use independent direct Walsh/FWHT and Fraction arithmetic. Entropies are exact rational linear combinations of ln(primes). Identities compare coefficient vectors, not approximate values. Signs use rational 24-term atanh-series enclosures, with ln(p) range-reduced to k ln2+ln(p/2^k) so series parameters are <=1/3. For z>=0 the omitted tail is bounded by 2z^(2m+1)/[(2m+1)(1-z^2)]. Sign-sensitive interval linear combinations use each coefficient's sign. The decisive seven-bit signs also pass independent arbitrary-precision integer-power comparisons. No floating-point entropy sign is used; runtime measurements are floating-point metadata. Full results are the three output JSON files. These finite checks support the analytic theorem and do not infer any all-dimensional FEI bound.

## proof dependencies and changed downstream conclusions

The new affine-syndrome lemma is self-contained above and in the TeX. Its physical deficit corollary uses A051-CRITICAL-BLOCK-DEFICIT v1, independently reconstructed and accepted at its stated scope locally in REVIEW_A051.md; the existence/minimality interface A051-THRESHOLD-CRITICAL-EXISTENCE v1 is also reviewed there. No substantive repair was supplied to either source version. This responds to the stream's two-source-complete-unreviewed-candidate cap by completing review before introducing this single bundled candidate; B20 adoption and nominated A090/A094 review remain distinct. The new A052 theorem itself is pending independent review.

A054/A055 now have an explicit anti-affine-concentration test derived at the correct criticality line. A053 can use its rank-one form to quantify how a near signed symmetry obstructs criticality, while preserving activation and raw-indicator caveats. A026/A028 can use the universal channel upper bound in proper-block selection: if H(Y|S_C)+kappa b<R(f)I_A, then averaging deficits guarantees some actual child with ratio strictly larger than R(f). For constants the usual zero convention applies. This is a checkable sufficient descent condition, not a universal selection theorem. No dependent full-FEI conclusion is newly accepted.

## one next mathematical action and independent reviewer

Next: test whether the syndrome upper bound, minimized over proper physical pivot blocks and syndrome words, forces descent on every prospective high-ratio critical source; start with A053's near-tensor/sparse-defect obstructions and preserve the exact child-deficit average. Reviewer A090 should reconstruct the character-shifted channel estimate from scratch; A094 should challenge the all-descendant hypothesis, zero cases and universal gap. A054/A055 are the primary structural consumers; B20 can adopt the source reviews and index this single candidate.

## actual persistence receipts or precise save blocker

All artifacts are saved only inside A052's assigned run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, CRITICAL_SOURCE_STRUCTURE.tex, PRUNING_SCOPE.md, REVIEW_A051.md, frozen specs, scripts, output JSON, retrieved source text and source manifest. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/RECEIPTS.json records file sizes and SHA256 hashes; files remain below 20 MB. No shared index, other agent folder, read-only source tree, brain store, trading directory, git repository, scheduler or outbound message was modified. Supervisor copies, remote mirror verification, registry adoption and independent review of A052 remain pending.

## Universal bridge

This stage moves C018 erasure/block payment toward C019 stopping-tree payment: the unpaid block erasure H(S_A|S_C) is represented exactly as conditional affine-syndrome entropy, and the physical channel term has the additional bound (2/ln2)b measured in physical pivot distance. Critical witnesses must defeat every such descent certificate; exact and approximate signed symmetries now have explicit quantitative tests. What remains is a universal proper-block selection or nonreusing tree bound, including terminal entropy. The shortest next route is to try this test on the actual high-ratio critical frontier and its near-tensor defects, rather than proving another isolated class or resurrecting refuted component pruning; no universal constant or connectedness theorem has been obtained.
