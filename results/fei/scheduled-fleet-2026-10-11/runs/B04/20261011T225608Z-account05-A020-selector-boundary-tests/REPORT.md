# A020 — selector boundary falsifier suite

## Exact target, quantifiers, hypotheses and units

For uniform independent physical blocks x in {0,1}^a and y in {0,1}^m, let F(x,y)=g_x(y), with arbitrary Boolean branches on the same data cube. Entropy H uses log base 2 and squared normalized Fourier coefficients; influence is the uniform disagreement probability summed over coordinates. Define s=I_sel(F) and Delta=H(F)-2^-a sum_x H(g_x). Validate the B04 lead's proposed bound

    Delta <= (2/ln 2)s + a h2(s/a).

The exhaustive target is every truth table for a=1,m=0,1,2,3 and a=2,m=0,1,2. These seven labeled domains have 131,620 cases, with no symmetry quotient. A second frozen domain contains 32 named fixtures and 1,024 seeded random tables at a=2,m=4. Neither finite domain implies an all-dimensional result.

## Sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 completely, plus README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json, STREAM_NEXT_ACTIONS.json and FEI_100_agent_research_plan.tex in the canonical local report tree. Read the campaign supplement CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md. Source files were read for source inventory and relevant checks; the operative mathematical sources are BLOCK_RESTRICTION_IDENTITY_2026-09-18.md §§1–2 and ISOSPECTRAL_SPLICING_CURATED.md §§2–4. COUNTEREXAMPLES.md X004 and X005 already record support-collision and full-FEI admission obstructions: the named examples here extend their test coverage, rather than asserting novelty.

Read BOARD.md snapshot 2026-10-11 22:57 UTC and Claude B04 STREAM_NOTES.md v1 dated 22:42 UTC. Followed its specific A020 instruction to exhaust small multiplexer domains and inspect moderate-density ratios. The board identifies A018's collision identity and A019's rare-translation mechanism; this stage does not reproduce their broad claims or the addressing calibration. Relevant prior canonical B04 REPORT.md files were not found in the earlier-run traversal. Local A020 had no prior report at stage start.

Read the four context .txt manuscripts, with a decoding fallback for legacy text bytes. The current threshold paper's §8.2, Proposition 8.6, equations (75)–(79), and Corollaries 8.7–8.8 are the operative composition locators. The earlier threshold version is provenance only. The percolation manuscripts' introduction and refinement/geometry framework provide context and are not proof dependencies here. No percolation implication is claimed. out/source_receipts.json pins actual local files by SHA256; local manuscripts and notes may differ from historical publication pins.

## Complete derivation and first unsupported line

Write a_x(T)=ghat_x(T). The signed coefficient is

    Fhat(S,T)=2^-a sum_x (-1)^(S dot x) a_x(T).

Consequently sum_S Fhat(S,T)^2=R_T=2^-a sum_x a_x(T)^2. Conditional on T, the selector spectral law is nu_T(S)=Fhat(S,T)^2/R_T. The data marginal entropy gives the exact identity

    Delta = B_W + M_W,
    B_W = sum_T R_T H(nu_T),
    M_W = H(R)-2^-a sum_x H(ghat_x^2),
    s = sum_T R_T sum_S |S| nu_T(S).

These equations retain signed collisions; replacing sums of amplitudes by sums of squared amplitudes changes the problem. The entropy bound H(nu_T)<=sum_j h2(P_nu_T[j in S]) and twice-applied concavity give B_W<=a h2(s/a). Applying the cube logarithmic Sobolev inequality, in natural units Ent(v^2)<=(1/2)sum_j E(v(x)-v(x^j))^2, to |a_x(T)|/sqrt(R_T), and summing over T, gives (ln2)M_W<=2s by data Parseval and |abs(u)-abs(v)|<=|u-v|. The two-point inequality and tensorization are supplied in the source's §2; this is a reconstruction of the existing channel estimate, not a newly opened broad candidate. Adding yields the lead's inequality. This argument does not establish sharpness of the lead's asymptotic constant, which is assigned to A018.

The new finite certificate is stronger: in all seven exhaustive domains,

    Delta <= (171/200)[(2/ln2)s + a h2(s/a)],

with strict inequality whenever s>0 and equality at s=0. There are 300 zero-selector tables and 131,320 positive-selector tables. The zero case is analytic: no selector edge changes F, so all branches agree, and Delta=0. All positive cases are certified by outward rational interval comparison, not floating-point arithmetic. Every truth table is a genuine Boolean function by construction.

The first unsupported line toward a universal constant would be a nonreusing payment of the entire rare term sum_v w_v I_sel(v) log(a_v/I_sel(v)) while retaining terminal data entropy. The finite cap does not pay this term. No universal strict ratio gap at densities bounded away from zero is proved by this stage.

## Named boundary witnesses

1. Coincident support and affine parity cells. On two control bits, take complementary affine cells A0={x0+x1=0}, A1={x0+x1=1}, with leaves y and -y. The actual F=(-1)^(x0+x1)y is a character: H=0, I=3. Dropping the cross terms in the disjoint-leaf-support mixture ledger predicts H=2 and I=2. Both cells are affine and disjoint physically; the two branch Fourier supports coincide. Giving both cells the same leaf instead produces F=y, H=0, I=1, so cancellation can also erase the selector influence entirely.

2. Unequal affine cells. Use A0={x0=0}, A1={(x0,x1)=(1,0)}, A2={(1,1)}, with leaves y,-y,y. Cell probabilities are 1/2,1/4,1/4. Then F=h(x)y, where h is a two-control one-point defect. All four Fourier masses of h are 1/4, so H(F)=2 and I(F)=2. The false mixture entropy is H(1/2,1/4,1/4)+sum_l p_l H(q_l)=3, where q_l=ahat_l^2/p_l. Its influence is 1+sum_l p_l E_q_l|S|=7/4. Thus even unequal affine cells require both interference and actual selector influence. The general nested fixtures implement this same defect at a=2 and analogous partitions at higher a.

3. Nearly identical branches with coincident full Fourier support. On four data bits let g=(-1)^(y0 y1+y2 y3) and flip only y=0 to obtain g'. They disagree on 1/16 of the cube. Their Fourier coefficients are respectively sigma_T/4 and sigma_T/4-1/8, so every data Fourier label is present in both branches. Their physical splice has selector influence 1/16 and nonzero entropy increment. Branch closeness does not imply orthogonality, disjoint spectral support or zero entropy debt. The exact signed Walsh coefficients and entropy intervals are saved in fixtures.json. The higher-selector fixtures select this point flip on a singleton cell or on a parity cell; the control influence is checked directly against physical edges.

The mandatory analytic recovered bent-splice guard is reconstructed in SELECTOR_FALSIFIER_SUITE.tex. For even m, delta=2^-m and e=sqrt(delta), the parent coefficients are e sigma_T-delta and delta in its two selector sectors, while g' has e sigma_T-2delta. Expanding -t^2 ln(t^2), with a uniformly bounded Taylor remainder for m>=4, gives Delta/delta=m+3/ln2+O(delta), so no fixed selector-only increment constant survives. The full physical influence is m/2+(m+1)delta. This confirms divergent local debt while preserving the data influence available for FEI. SELECTOR_FAILURE_SCOPE.json records the exact false identities and excluded hypotheses.

The known arbitrary-signed-leaf admission X005 remains applicable: singleton affine cells with g_x(y)=h(x)y encode arbitrary h. The family is FEI-strength after tensor amplification. This stage supplies falsifier coverage, not a new universal reduction.

## Executed validation: domain, arithmetic, commands and outputs

SEARCH_SPEC.json was saved before the pilot/search; TARGETED_SPEC.json before the larger fixtures; CERTIFICATION_SPEC.json before the additional rational-cap pass. The pilot covered 512 cases and took 0.108 seconds of Python computation. The first full census took 15.528 seconds. The targeted suite took 0.284 seconds. Exact observed durations for the final cap pass and direct reconstruction are in census.json and direct_check.json. Commands run from this agent folder:

    python -X utf8 runs/20261011T225608Z-account05-A020-selector-boundary-tests/code/verify.py --pilot
    python -X utf8 runs/20261011T225608Z-account05-A020-selector-boundary-tests/code/verify.py
    python -X utf8 runs/20261011T225608Z-account05-A020-selector-boundary-tests/code/fixtures.py
    python -X utf8 runs/20261011T225608Z-account05-A020-selector-boundary-tests/code/direct_check.py

Integer Walsh numerators are squared before normalization. The script checks Parseval, each partial data-row Parseval identity, physical versus spectral selector influence, and average-child versus full data influence in every case. All logarithms use exact Fraction arithmetic for

    ln t = 2 sum_(j=0)^39 z^(2j+1)/(2j+1) + remainder,
    z=(t-1)/(t+1), 1<=t<2,
    0<=remainder<=2 z^81/[81(1-z^2)].

Range reduction expresses ln(k) through ln(t)+e ln2. Endpoints are rounded outward at integer scale 2^100. Entropy sums and averages are rounded outward, including signed subtraction. Natural units eliminate division by ln2 from the inequality: the target is 2s+a h_nat(s/a). A positive rational lower bound on target minus Delta_nat certifies the original inequality. The cap pass checks the upper interval endpoint of Delta_nat/target_nat is less than 171/200 for every positive-selector table. Source series error and all rounding are included.

The strongest discovered exhaustive witness is a=1,m=3, table mask 21 (negative values at truth-table positions 0,2,4; selector bit is least significant), branches [7,0], s=3/8. Its ratio is approximately 0.8545353225101016. Rigorous endpoints for that witness and the maximum of every outward upper endpoint are in census.json. The reported candidate ordering uses floating point; the bound 171/200 does not. At a=2,m=2 a discovered best mask is 854, ratio about 0.8187677817007175. All nontrivial maxima discovered in the exhaustive domains lie in the frozen moderate-density band [1/4,3/4]. This says nothing about global optimality in larger dimensions.

The larger 1,024 random-table sample's best moderate witness is mask 9205610344637496819, branches [50975,51227,61438,27302], a=2,m=4, s=13/16, density=13/32, with ratio about 0.6019871387555503. This is finite search evidence with a certified witness interval, not an optimality claim. direct_check.py reconstructs all 32 named fixture Fourier numerators by independent O(N^2) character sums and compares physical edge counts, using no Walsh butterfly. It is a second implementation by this agent, not an independent-agent review.

One bounded computation ran at a time. The frozen estimates are below 200 MB, so the >300 MB memory-gate condition did not apply. No dimension was raised automatically, and no GPU, window, background helper, git, external message, brain write or shared-tree mutation was used.

## Proof dependencies and changed downstream conclusions

The finite claim depends only on the saved verifier, the explicit logarithm tail derivation above and exhaustive truth-table enumeration. Standard uniform Fourier identities are derived above and independently checked on fixtures. No unreviewed agent claim is assumed by the finite certificate. The broad selector bound is a reconstructed B04 lead interface using the previously supplied log-Sobolev proof; its sharpness and eventual adoption remain separate. A090/A091 may review the finite certificate and witnesses; A018 can use the moderate-density data in its independent lead review. A019 and A027 should run future proposed collision/stopping-tree identities against the affine and nearly identical fixtures before discarding any term. The universal FEI status is unchanged: OPEN.

## One next mathematical action and independent reviewer

Next A020 action: consume A019's source-complete two-module shared-control ledger, and test the exact KL credit and ownership of physical selector influence on the saved affine and rare-point-flip fixtures, retaining terminal core entropy. Reviewers: A091 (primary), A090 (alternate), as named in the packet contract. Stop enlarging the finite census unless a new statement supplies a concrete falsification target.

## Actual persistence receipts

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, three frozen specifications, code/, out/ and the rolling STATUS.md, WORKLOG.md and LEARNED.md are saved inside A020 only. out/persistence_receipt.json records schema validation, sizes, hashes and read-back checks after final generation. No supervisor copy, Brain mirror, GitHub mirror, adoption or independent acceptance is asserted.

## Universal bridge

This stage moves the lead-designated G-LOWSEL-COLLISION interface feeding C019 stopping-tree payment by certifying its selector bound on 131,620 cases, giving a finite ratio cap 171/200, and preserving exact affine/unequal-cell collisions that invalidate unpaid ledgers. It does not lower the universal constant or amortize the rare logarithm. The remaining obligation is to assign shared-control collision costs once against actual physical influence, with terminal entropy preserved. Testing A019's next overlapping-control mechanism is the shortest useful route toward full FEI because it attacks that unpaid C019 ownership step directly; another unrestricted dimension census would provide only an isolated finite result.
