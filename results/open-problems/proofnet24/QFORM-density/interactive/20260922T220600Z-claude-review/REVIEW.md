# QFORM: Claude-attributed pushes, mathematical review, and scheduler delivery

Record: 20260922T220600Z-claude-review. Interactive review, not a scheduled-worker sign-in. The unrestricted quadratic-form bounded-density conjecture remains NOT PROVED by the reviewed work. This report completes the interrupted owner-requested check and adds a fresh read of the subsequent Claude-attributed QFORM package.

## 1. Evidence window and honest scope

Repositories are yspennstate/math-open-problems (master) and yspennstate/math-research-brain (main). The research-archive comparisons are:

1. c35c25f941bd343ea93b6c22a8c3adaf17d9511d -> e2730bd0eda8cddd81d2d2156b5b06c067cf4578: 171 commits ahead, no divergence.
2. e2730bd0eda8cddd81d2d2156b5b06c067cf4578 -> c5b2350b76a01283a2503368d013a44beadbbcc6: 172 more commits ahead, no divergence.

Thus 343 commits were added after the previous source-index checkpoint in these two pinned comparisons. This is a repository-activity count, NOT 343 theorems, successful runs, or independently checked proofs. The first base was committed at 2026-09-22T19:53:51Z; the last head was read just after 22:06Z. The initial interrupted brain comparison fcca43e7d6be77bdfb3afc35d24d8719b4fc3fcd -> ac3c46217437a8254fbb37718ae7effa22eadcb7 reported 492 commits; its changed-file list reached the 300-file boundary and must NOT be treated as an exhaustive brain diff.

Fresh brain snapshot: 1465c762f87fb07931cbac374246019be6297635. AGENTS.md and scheduled_tasks/README.md were read; OWNER CONTROL is still revision 2026-09-22.15 and assigns the existing eighty mathematical workers exclusively to QFORM. No native schedule, enablement, notification, or identity mutation was performed during this check.

Review coverage: all five text files in the new Claude-attributed QFORM directory were read, including both halves of RESULTS.md, the complete literature note, and all three scripts. The central analytic derivations were examined, finite matrix/normalization checks were independently executed, and selected worker reports and their subsequent corrections were read. This is NOT a line-by-line certification of every report in the 343 commits, every referenced external paper, or all 7,937 exported brain claims. The full Monte Carlo scripts were not rerun at their original multi-million-sample settings.

## 2. What Claude actually pushed

Attribution below is supported by explicit Co-Authored-By: Claude Opus 5.5 metadata in the commits; it is not independent verification of which model executed each line.

- 25a69cb93391eeb8d594949b222096de14275bd3, math-open-problems, 2026-09-22T20:19:08Z: an FEI context and input package at proofnet24/P03-fei/continuations/2026-09-22-opus-team/. The context records a separate owner instruction for five local FEI groups. At the checked earlier snapshot the directory contained CONTEXT.md and inputs, not completed F1-F5 reports. Do not count this as QFORM proof progress or infer that the eighty scheduled QFORM workers were retasked. Do not overwrite this separate workstream on the basis of a guessed conflict.
- 19010c8cab817f3da2fd028d0be0bf70b735c01a, math-research-brain, 20:55:52Z: refreshed the population export (manifest claims 7,864 -> 7,937) and committed current_note.py and selection_integrity.py, which its message says had existed only locally. This is infrastructure/source synchronization, not a new density theorem. The code deliberately separates note consistency from mathematical truth. The entire large population export was not successfully read or revalidated here, so no whole-store or native-ingestion certification is made.
- b0cbc2233369b6a3f366cf569d425f485f123e1c, math-open-problems, 21:30:21Z: the actual new QFORM package at proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/.
- 7359c982f3fa85f61b99e8768b915cce6e596d36, 21:38:45Z: added relations between that package and the earlier research archive.

The last package is real mathematical work. Its opening explicitly says it does not prove the unrestricted conjecture. It now acknowledges the false arbitrary-joint coarea lemma, rather than using that lemma to claim the rank-three case solved.

## 3. Review of the five-file QFORM package

### RESULTS.md: the valid scope

File blob cb3f67749e8cdc19b22a584ca0c5a8989fe47ff6 at commit 7359c982f3fa85f61b99e8768b915cce6e596d36.

Lemma 1 bounds integral |g-hat|^p by 4 pi / sqrt(p) for p>=2 when |g|<=f, 0<=f<=1 and integral f=1. The even-exponent convolution argument and extension using floor(p/2) are consistent. Lemma 2 is the Gaussian-damped Fresnel identity; the amplitude-integral bound must be finite before it supplies a finite estimate.

Theorem F treats three quadratic directions plus a remainder whose selected original-coordinate block is diagonal. The selected Gram matrix must be invertible and every normalized leverage must be <=1/2. Under those actual hypotheses the factorization, translated Brascamp-Lieb step and Fourier inversion give the displayed constant 12 times (|lambda_1 lambda_2 lambda_3| det G)^(-1/3). This is a scoped theorem, not a decomposition of every admissible A.

There is provenance overlap: arbitrary separable phases and an original-coordinate principal-block conditioning corollary were already proved in the 20260922T120815Z-separable-perturbations report (commit 773b7fb6f0e6a8142066f0bac08d228dfc164fdb) and preserved in the previous conversation-sync initial_note. Thus the diagonal twist and outside conditioning in F are not new relative to the entire archive, even though the new report compares mainly to rank-two-fusion. The earlier r=3 estimate 3e is also numerically better than 12 in the matching normalized scope. This does not diminish the usefulness of a common proof formulation.

Theorem H incorporates genuine original-coordinate hub variables into the Fourier integration. Its decay exponent is |H|+r/2. The remaining light block must be exactly low rank plus diagonal, and the enlarged frame must have invertible Gram matrix and leverages <=1/2. Dropping the hub densities by their cap and using y=2t x_H is legitimate; arbitrary hub self curvature becomes a phase. The argument does not justify replacing an arbitrary light self block by a low-rank approximation. State explicitly that nonzero lambda_k are used; delete zero modes rather than divide by them. A star example must also satisfy the displayed enlarged-frame leverage condition.

Theorem D is the useful aggregate advance: for M=A_IJ on disjoint original-coordinate sets, Z=e_3(M^T M)>0, and row inclusion probabilities alpha_i under squared-minor volume sampling, alpha_i<=1/2 implies a density bound 6 sqrt(e) Z^(-1/6). The determinant AM-GM proof is consistent with the L^p Brascamp-Lieb normalization. No column-side beta<=1/2 condition is needed. Its general-weight version requires weights only on nonzero minors. Endpoint factors with alpha=0 or beta=1 should be interpreted by dropping a sup-norm factor and using the continuous endpoint of the same inequality, not literal division by zero. The sharp-Hausdorff-Young refinement is supplied in Section 4 below.

Lemma 4's Schur spectral-count statement follows by inverse interlacing when A is invertible: k eigenvalues in [-1,1] leave at least k-1 after one principal deletion. Perturbing the kernel and taking the finite Schur limit covers singular A. This alone does not give a large original-coordinate pivot. In Lemma 3, rho log(e/rho) must be restricted to 0<rho<=1, followed by a trivial mass bound for larger radii; the expression becomes negative for rho>e as literally written.

Important robustness qualification: retaining three substantial singular values is NOT enough to preserve Theorem D's alpha_i<=1/2 gate. Take the 6-by-3 matrix with rows e1,e1,e2,e2,e3,e3 divided by sqrt(2); its row weights equal 1/2. Multiply the first row by 1+epsilon. All three singular values remain >=1, but alpha_1=(1+epsilon)^2/[1+(1+epsilon)^2]>1/2. This is an arbitrarily small perturbation. It does not refute Theorem D; it refutes using spectral stability alone to omit its leverage hypothesis.

### LITERATURE.md

The survey was read, but its external-paper verification labels are the author's reports, not newly certified here. Primary sources for the Brascamp-Lieb Gaussian-exhaustion principle, sharp Hausdorff-Young, and product marginal caps were checked separately below. No exhaustive novelty conclusion is drawn from search misses.

The sentence saying bounded density holds 'exactly when k>=3' for smooth nondegenerate quadratic forms needs qualification: a positive-definite rank-two form already has bounded density with a smooth bounded product input. Three is the threshold sufficient across indefinite signatures, not a necessity for each quadratic form. Likewise a fixed-pivot 3-by-3 independent-coordinate theorem can be true with a different proof even though the earlier arbitrary-joint coarea proof was invalid.

### check_fresnel_bl.py

Read complete source, blob 526b84f1dc372b541295d6e1ae65d982478dfc72. The random interval starts in its second experiment do not enforce disjointness. Reproducing only the seed-7 input generation finds 19 of 40 coordinates with overlapping intervals, involving 21 adjacent overlaps. Because N times interval width equals one, overlap makes the marginal density exceed one. Those runs therefore do not test the claimed cap-one class. The first scalar experiment's three generated supports had no overlaps in this seed, but there is no general guard.

The fixed Fourier window [-4000,4000] is a truncated integral, not a rigorous certificate for the integral over the real line. The Monte Carlo estimate near its sampling floor is not a tail estimate or a proof. The original large simulations were not rerun; no claim is made that these defects invalidate the analytic theorem.

### claim_test.py

Read complete source, blob 8884c29c096e043fd5dc314a49bd82b25ebf3ffc. Its spread supports have the same missing disjointness guard. The zero-frequency branch sets base=1 and then multiplies by a sum of N phases, giving psi_spread(0)=N (8 in its configuration), not 1. A stable correct expression for the equal mixture is sinc(t*w/(2*pi)) times mean(exp(i*t*(starts+w/2))). Positivity of a Monte Carlo integrand does not by itself ensure small relative error: rare-event means still require error control.

### thmD_check.py

Read complete source, blob 06169f9264e4ea7d950e28406b0629f923615597. The volume-marginal formula was independently checked against enumeration of all 3-by-3 minors on twelve 5-by-6 matrices; maximum error was 3.34e-15. Ninety-six additional positive diagonal Gaussian parameter choices satisfied the determinant AM-GM bound. The original code only prints alpha maxima: a reported density number is an applicable theorem bound only if the alpha gate actually passes. Its examples also need a separate check of s_3(A)>=1 before being described as original-target instances. D itself remains valid without that ambient threshold. Full-degree symmetric-polynomial convolution is unnecessary; a degree-three recurrence avoids irrelevant large intermediate coefficients.

The pinned package lists five source files and no separate executed-output logs. Source presence and the author's description of running a test are different from a saved reproducible result. The independent bounded checks and their actual JSON output accompany this review.

## 4. Complete refinement of D using sharp Hausdorff-Young

This refinement uses the same Gaussian Brascamp-Lieb step as Claude's D; it is not claimed as a new full-target mechanism or a literature-wide novel theorem.

Assume exactly D's hypotheses. Omit rows with alpha_i=0 (their characteristic factors are bounded by one). Let beta_j be the corresponding column marginals, with sum alpha=sum beta=3, and define

B_alpha=product_i (1-alpha_i)^(-(1-alpha_i)/2),
B_beta=product_j (1-beta_j)^(-(1-beta_j)/2),

using the continuous endpoint value one for a beta_j=1 factor. The Gaussian constant proved in D is

C_BL <= Z^(-1/2) product_i alpha_i^(-alpha_i/2) B_beta.

In the Fourier convention hat f(s)=integral exp(-isx)f(x)dx, sharp Hausdorff-Young at q_i=1/alpha_i>=2 gives

||hat f_i||_(1/alpha_i)
 <= (2pi)^alpha_i (1-alpha_i)^(-(1-alpha_i)/2) alpha_i^(alpha_i/2),

because ||f_i||_(1/(1-alpha_i))<=1. For h_i(y)=|hat f_i(2ty)|, multiply this by (2|t|)^(-alpha_i). The independent difference densities g_j have every required L^q norm <=1. Applying C_BL and cancelling the alpha powers therefore yields

|phi_Q(t)|^2 <= (pi/|t|)^3 B_alpha B_beta Z^(-1/2).

For 0<=c<=1, -(1-c)log(1-c)<=c. Hence B_alpha<=e^(3/2) and B_beta<=e^(3/2), so

|phi_Q(t)| <= min(1, (pi e)^(3/2)|t|^(-3/2) Z^(-1/4)).

If K=(pi e)^(3/2)Z^(-1/4), then integral_R min(1,K|t|^(-3/2))dt=6K^(2/3). Fourier inversion proves a bounded continuous density with

||p_Q||_infinity <= 3 (B_alpha B_beta)^(1/3) Z^(-1/6)
                  <= 3e Z^(-1/6).

The constant changes from 6 sqrt(e)=9.8923276242 to 3e=8.1548454854, a 17.56 percent reduction under the same assumptions. This still requires a good original-coordinate cross block and the alpha gate; it does NOT settle arbitrary A.

Endpoints in the Gaussian step can be justified explicitly. If beta_j=1, the j-th input density is used only in L-infinity and can be removed by its bound one; every minor in the weight support contains j, so the determinant lower bound remains valid as its diagonal Gaussian precision tends to zero. Rows with alpha=0 similarly disappear. Thus no positive weight has an undefined exponent, and the finite-dimensional Brascamp-Lieb endpoint follows by the same limiting inequality.

Primary inputs: W. Beckner, Inequalities in Fourier analysis, Annals of Mathematics 102 (1975), 159-182, DOI 10.2307/1970980, publisher https://annals.math.princeton.edu/1975/102-1/p11; E. H. Lieb, Gaussian kernels have only Gaussian maximizers, Inventiones Mathematicae 102 (1990), 179-208, DOI 10.1007/BF01233426; J. Bennett, A. Carbery, M. Christ and T. Tao, The Brascamp-Lieb inequalities: finiteness, structure, and extremals, arXiv:math/0505065 (Gaussian exhaustion and endpoints); G. Livshyts, G. Paouris and P. Pivovarov, On sharp bounds for marginal densities of product measures, arXiv:1507.07949. These classical inputs are not new proofs supplied by this project.

## 5. Scheduled workers are publishing, but not uniformly

Counting distinct account/slot prefixes with an added REPORT.md in the two archive comparisons gives:

Account01: 18 then 18; union 20/20.
Account02: 17 then 16; union 19/20 (no new REPORT.md from B13 in these comparisons).
Account03: 19 then 19; union 20/20.
Account04: 3 then 2; union 4/20 (B13,B14,B15,B17).
Total distinct worker slots with new report-file evidence: 63/80.

The two ranges overlap in worker identities but not commits. This union is NOT the older 61/80 sign-in count and NOT a count of independently verified mathematical advances. These are source-path observations in one bounded interval; missing a new REPORT.md does not establish absence of all work, an outage, or absence of older results.

All twenty directly accessible account04 native tasks were observed enabled, hourly, QFORM-only and quiet, with last_run_time between 21:24:40Z and 21:26:16Z in this resumed check. These timestamps show recent scheduler execution, not completion or successful push. The canonical account04 21Z login-directory request at the readable brain snapshot 1465c762... returned 404. At the earlier ac3c462... snapshot, the 20Z canonical directory contained only B02,B04,B06,B10; other workers had some run-specific sign-ins elsewhere. These are specific receipt gaps, not a claim that all workers failed.

The priority is now delivery reconciliation, not another undifferentiated sign-in campaign. Account04/B20 must obtain, for each of its twenty tasks, the latest completed result commit/path or the actual push failure, partial-run state, or blocked-write reason. Missing slots in the two-hour new-report cohort are B01-B12,B16,B18-B20. Account02/B20 must similarly reconcile B13. Workers must write only their own actual-hour sign-in and source-pinned result. Do not fabricate peer acknowledgements or turn a native timestamp into a proof-success certificate.

## 6. Worker mathematics checked and corrections applied

The interrupted pass read the account03/B06 20:18:41 aggregate-E2 theorem in full, both parts. Its one-row Plancherel factor times a determinant bound produces an integrable L^(3/2) characteristic-function estimate and hence an L^3 residual density; an actual independent-coordinate square then gives a bounded output by the Abel kernel. Its displayed tail exponents and constants are consistent, conditional on the explicitly imported graph estimate. This is a useful aggregate result, not a universal structural reduction.

The account02/B20 20:01:20 strong-hub gluing and account01/B20 20:22:51 aggregate-E2/direct-alignment report were read. They combine actual partner inequalities rather than merely citing reports, but retain explicit pivot, cross-bank, and leverage conditions. Their surviving cases are not proved impossible under s_3(A)>=1.

The account03/B20 20:49:47 report was read together with its later CORRECTION.md at c5b2350b..., blob 7d277c6165abea6f7858fae9640caabf966d5d0b. The correction retracts the informal resetting of the inherited tau parameter and clarifies that the same-sign overlap was already controlled. The useful corrected conclusion is a separation constraint between two physical coordinates, not a newly solved global sign branch. Do not promote the older uncorrected summary.

Account04/B14's 20:15:07 finite-mixture localization proof was read and gives a valid constant-preserving transfer via compact approximation, grid hypersimplices and total variation. Account04/B13's 20:10:36 arbitrary-weight bathtub proof has a missing nonattainment case on the infinite measure space: for w(x)=1-exp(-|x|), no threshold satisfies |{w>tau}|<=1<=|{w>=tau}|. This does not refute the claimed equality of optimal constants or every possible witness extraction. A sufficient repair is B14's mixture approximation: for any eta>0 approximate the original product law in L1, choose a product-indicator component with at least the mixture's functional value, and obtain F(E)>=F(f)-eta. Let eta tend to zero for bounds; choose eta smaller than a strict violation margin for a genuine indicator counterexample. No universal maximizer or interval extremality is required.

Account04/B17's 20:18:27 tight-frame polynomial inequality was read. Its elementary square completion and Cauchy-Schwarz calculation are sound for the displayed polynomial. The imported Edgeworth expansion and its O(m^-2) remainder were not independently re-proved here; a sharper polynomial coefficient is not a global upper bound or a larger target lower-bound witness.

## 7. Work that would advance the full problem

Claude's D and the fleet's determinant estimates should be compared at the same actual original-coordinate block, with every leverage gate checked. H should be applied to genuine hub-plus-low-rank-light structures, not to an approximate light block without controlling the perturbation. The remaining difficult family described in Claude's own report is a hub/star plus a delocalized quadratic component with arbitrary small dense self-couplings. Uniform perturbation control cannot assume finite moments or independent spectral coordinates. The nominal small operator norm of an added matrix alone does not bound its phase on unbounded input supports.

Continue the original arbitrary-dimension, arbitrary-sign, cap-one-product-law target. Assign two existing analytical workers to check the stated D refinement/endpoints, a small number to repair and save source-valid numerical experiments, and the synthesis workers to combine D/H with the live corrected physical-pivot obligations. Most workers should pursue distinct full-target steps rather than all repeat the same review. Require a mathematical change from the previous run and an immutable push receipt; keep housekeeping brief.

No full solution, universal-counterexample, independent two-review approval, native learned-memory ingestion, public release, or new agent execution is claimed by this report.
