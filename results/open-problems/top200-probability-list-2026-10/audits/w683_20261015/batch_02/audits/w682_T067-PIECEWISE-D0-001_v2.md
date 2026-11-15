# T067-PIECEWISE-D0-001 v2: PASS

Exact subject SHA256 `46689fc2727e31a3d52e637d9adce70e3dd3b2f981fbb8e7dc752c859cc10e3c`. Kind: narrowed; target: regular q=3 Kesten–Stigum nonreconstruction, d>=156. This is w683's independent mathematical audit of the exact v2. A distinct-account reviewer must explicitly pass this hash before admission; its earlier v1 review is not automatically a v2 receipt.

## Statement checked

For every integer d>=156 and every 0<lambda<=1/sqrt(d), the uniform-root ferromagnetic symmetric three-state Potts broadcast on the regular d-ary tree is nonreconstructible, including equality. This does not settle the smaller degrees or other models. Novelty and priority remain unverified.

## Exact-version binding

I independently checked A–D from the raw v1 proof, SHA256 `9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226`, including its entire finite certificate. I then read the full v1/v2 difference and verified exact byte equality of the entire mathematical body from Part A through its final NEXT line. The delta changes the version heading, corrects the blanket dependency-review wording and appends its amendment. Receipt checks/t067_piecewise_v2_binding_own.json binds the v2 subject to the original frozen manifest, my complete endpoint/algebra receipts and this checked delta. No numerical computation was repeated on an unchanged data set.

## A: general-L signed replacement

The root-conditional branch law is the positive tilt 1+lambda*a1. Gaussian branches with covariance C=(lambda^2 M/2)P and means C e_i have likelihood ratios exp(g_i-g_j); thus they and every hybrid are calibrated Bayesian experiments. Symmetric radial moments have equal unconditional and root-conditional expectations. The d-Gaussian sum has exactly the stated mean and covariance with s=d lambda^2 x, M=9x.

I checked the retained cubic contraction explicitly. The first and second Taylor terms cancel their p1(1-p1) pieces; the third gives the displayed ell. Calibration turns it into -E[e2(e2-9e3)]<=0 when T>=0. The sign is an expectation sign, not a pointwise comparison. The zero-sum identities and fourth-moment orbit formulas agree with the previously independently checked sharp-replacement geometry.

Each discarded term was checked against the displayed derivative norm, conditional moment and Taylor factor. The log remainder is an integral identity valid for lambda*a_i>-1, with denominator bounded below by 1-lambda. Projection contracts norm. The printed B4,B3,B1 follow using sqrt(6)<=49/20 and 1/sqrt(6)<=5/12. The mean remainder contributes 1/48+(49/160)L B4. The second raw-moment remainder has its exact U/6 density correction and M^2/6 Gaussian mean-square correction. The two cubic Gaussian terms give 5/48+L^2/36. The exact Gaussian fourth moment is 2 lambda^4 M^2+(2/3)lambda^6 M^3+lambda^8 M^4/36. Taylor order four contributes 1/40. These sum to the stated rational C_U(L),C_M(L) for every lambda<=L<=1/10; the old L=1/16 numerical inequalities are not substituted at the larger L. Global derivative bounds and finite fourth moments justify integration through the unbounded Gaussian hybrids. Detailed checked equations are saved in the progress audit.

## B: Gaussian curvature and complete integral

The heat generator is H=(9/2)D_w+(9/4)Delta_P, ||w||^2=2/3. Fourth polarization gives the mixed derivative bound 3/5 and |Delta_P^2 F|<=12/5. The three contributions to |H^2 F| are 27/10, 135/8 and 243/20, summing to 1269/40<32. Global bounded derivatives permit the two semigroup differentiations for s>0. Subtracting the endpoint chord and 16(s-a)(b-s) leaves a convex function, giving exactly the upper-interpolation direction.

The exp/cosh integrand has orthogonal Gaussian noise columns of squared norm 9s/2, hence Hessian norm at most 9s/10. Conditional-bin means cancel all integrated linear terms; the whole bin error is KPD and the full square complement contributes in [0,1-P^2]. The -1/3 is subtracted after accounting for all mass. I checked the quadrature lemma separately in its exact v1 audit.

My own evaluator reconstructs all 86 endpoints at 192-bit outward Arb precision using 192 bins of width 1/16 on [-6,6]. It computes Gaussian weights, conditional means and unnormalized variances from erf/exp with outward rounding. Symmetry groups the four sign combinations of each positive-bin pair through an exact rational identity, giving 9216 folded blocks per signal. Every computed full-integral upper bound is <= its author's final rational upper bound. The comparison uses exact dyadic rational endpoints; display floats decide nothing. Every Gaussian tail is bounded. The pilot and full run completed, with each endpoint checkpointed. No solver evaluator or source code was imported.

## C: all exact finite steps

The submission's 426 named source/data files (1,286,046 bytes) match their frozen lengths and SHA256 values. The raw endpoint-map hash matches the exact gate input. I derived the constants anew at L=16013/200000, checked 156*16013^2-200000^2=922364>0 and verified every one of the 86 rational signal points, from 1/10 to 2/3.

Independently forming C1 from its displayed formula, I computed the exact minimum of each quadratic by checking its endpoints and any interior stationary point. The moment switch 2/15 is already a signal endpoint. All 85 parent intervals have strictly positive minima; the smallest is approximately 0.0000028426327471579822, with its exact fraction in the receipt. I also recomputed every coefficient of all 87 submitted Bernstein leaves, checked equality with their rational values, verified that each exceeds 3/10^7, and checked exact gap-free leaf coverage of every parent. Removing an endpoint and raising an endpoint upper bound are both rejected by the independent checker. Thus the saved PASS fields, leaf count and source hashes alone are not the basis of this result.

## D: canonical limit and all smaller positive eigenvalues

The future sigma-fields decrease, and the tree Markov property identifies their posterior with the generation-n posterior. Bounded reverse-martingale convergence gives the calibrated symmetric limiting law. For fixed finite d, strictly positive branch likelihoods make the Bayesian fusion map continuous, hence that law is a fixed point. Cubic preservation gives T>=0. Prefix observations are garblings of the full d-branch experiment, giving M_j<=M. F2's right-branch support condition holds since eta=1/sqrt(d)<L<2887/5000. Summing the actual conditional-independent fusion inequalities gives U<=U/d+5(d-1)M^2/d, hence U<=5M^2. Pointwise A<=6 also gives U<=6M. These are exactly the two moment ceilings used in C1.

At criticality s=x. The strict C2 inequality excludes every fixed point with x>=1/10, and convergence supplies canonical finite-depth entry without a simulated rate. The audited local theorem applies for d>=156>=100 and excludes every remaining positive fixed point. The stated total-variation bound follows from calibration and Cauchy–Schwarz.

For D.4 I checked the root-independent observation kernel explicitly: retain the observation with probability c, otherwise draw independently from its unconditional marginal. Its conditional density is (1-c+3c p_i)mu(dp), its marginal is mu, and its posterior is S_c(p). Thus both experiment laws and the rescaling identity hold. Applying these independent branchwise kernels and the same edge channel preserves Blackwell order; induction from the common pure-state experiment gives the smaller-eigenvalue comparison. No pathwise ordering of posterior vectors is assumed.

## Dependencies, sources and disposition

The full RESCALE v1 file has a separate FIX for its unrestricted moment corollary. This proof uses its valid identity (R), which D.4 proves directly; the moment-corollary correction remains queued separately. GAUSSIAN-QUAD v1 has this auditor's new method PASS. Earlier exact-version audit receipts supply SOFTMAX-DERIVATIVES, CUBIC-FUSION, TERNARY-MOMENTS, UNIFORM-LOCAL and FIXEDPOINT. The v2 text correctly removes the blanket two-audit assertion.

Sly, Reconstruction for the Potts model, arXiv:0811.1208, (4.7) defines the Gaussian map and Lemma 4.3 supplies asymptotic Gaussian-approximation context. Mossel–Sly–Sohn arXiv:2212.03362v2, Appendix A, uses the Gaussian/Lindeberg comparison context. The finite general-L constants, curvature and endpoint error estimates are derived here; no numerical constant is imported from these papers. Both primary PDFs were already fetched and their relevant passages checked. Literature priority of this explicit cutoff remains unclear.

**Verdict: PASS for the stated exact-v2 nonreconstruction theorem.** Another exact-v2 distinct-account receipt is required for admission.

Evidence: checks/t067_piecewise_gaussian_own.py; checks/t067_piecewise_own.py; checks/t067_piecewise_endpoints_own.json; checks/t067_piecewise_full_own.json; checks/t067_piecewise_v1_v2.diff; checks/t067_piecewise_v2_binding_own.json; and the detailed progress audit. All owned computations completed.
