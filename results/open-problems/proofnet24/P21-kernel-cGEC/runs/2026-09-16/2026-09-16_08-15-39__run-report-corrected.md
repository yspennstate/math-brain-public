# ProofNet24 P21 — restricted correlated Gaussian equivalence (cGEC)

**Run timestamp:** 2026-09-16 08:15:39 Asia/Jerusalem  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Track:** `P21-kernel-cGEC`  
**Exact target:** P04 Target 1; exactly two augmentations per original sample; fixed Delta > 0 and fixed ridge lambda > 0; smooth bounded odd activation with bounded derivatives (especially tanh); Gaussian feature entries variance 1/d; n/d -> alpha > 0; m/d -> beta > 0; initially a unit-norm linear teacher; NO number theory.  
**Runtime honesty:** the exposed runtime is GPT-5.6 Sol. The user requested GPT-6 / maximum reasoning, but no GPT-6 selector or separate reasoning-effort control is exposed. I do not claim an unavailable model switch, hidden subagent, or unperformed review.  
**Delivery:** GitHub only. No email or Gmail action was used.

## Canonical correction status

An earlier same-run immutable file, `2026-09-16_08-15-39__run-report.md`, was written at commit `69d3a9863afc3140409988a52fc2499cde1d66d6`. Exact-commit readback exposed several transport-level TeX escape defects such as a dropped `frac` prefix. The historical file is preserved unchanged. This file is the complete canonical corrected report. To prevent a second transport failure, all formulas below use plain UTF-8 / ASCII mathematical notation rather than TeX control sequences.

---

# 0. Executive verdict and theorem-sized advance

The exact restricted squared-ridge P04 Target 1 remains:

`MATHEMATICALLY PROVED / CANDIDATE COMPLETE`.

Formal ProofNet24 closure remains protocol-open by one audit. P26 has supplied one genuine OTHER-worker complete end-to-end audit, `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS`; one additional genuinely independent OTHER complete audit is still required. Repeated P21 specialist/self-audits do not count as that second audit.

The requested squared-ridge theorem is unchanged:

`| E L_A* - E L_G* | <= C d^(-1/2)`.

The bounded-C2 Taylor debt over the full training telescope is `O(d^(-1))`. Separately, the correctly matched clean prediction-risk comparison has total training replacement `O(d^(-1/2))`, plus `O(M^(-1/2))` for an independent empirical clean block of size M.

This run proves an exact convex-dual whole-block influence theorem and uses it to rederive the P04 rank-two Woodbury formula independently. It also rigorously falsifies an overly optimistic nonquadratic remainder target from the preceding P21 checkpoint and replaces it with a sharper projected-cubic program.

## New claim `P21-FENCHEL-BLOCK-44` — PROVED

Let `F_-(w)` be a proper closed lambda-strongly-convex leave-original-sample objective with unique minimizer `w_-`. Let the current two-row block be `X in R^(2 x m)` with target `t in R^2`. For a scalar convex loss ell, define

`phi(r) = ell(r_1) + ell(r_2)` and `e = t - X w_-`.

The full objective is

`F_-(w) + (1/N) phi(t - X w)`.

Define the exact nonlinear response

`K_N(s) = N [ F_-*(X^T s / N) - F_-*(0) - w_-^T X^T s / N ]`.

Then exactly

`L_i* - L_-* = (1/N) Psi_N(e)`,

where

`Psi_N(e) = sup_{s in R^2} { s^T e - phi*(s) - K_N(s) }`.

The response `K_N` is convex and nonnegative, with `K_N(0)=0` and gradient zero at 0. If `F_-` is C2 Legendre, then with

`w_s = grad F_-*(X^T s / N)`,

one has the exact 2 by 2 Hessian identity

`Hess_s K_N(s) = (1/N) X [ Hess F_-(w_s) ]^(-1) X^T`.

If `0 < mu <= ell'' <= L < infinity`, then `phi* + K_N` is `(1/L)`-strongly convex. Hence `Psi_N = (phi* + K_N)*` is C2 and satisfies the dimension-free curvature bound

`0 <= Hess_e Psi_N(e) <= L I_2`.

For squared loss and quadratic `F_-`, this exact formula collapses to the P04 Woodbury increment.

## New claim `P21-NAIVE-N2-REMAINDER-NOGO-44` — PROVED

For a generic smooth strongly convex leave objective, replacing the exact nonlinear response `K_N` by its quadratic Hessian at the leave optimizer does NOT have an `O(N^(-2))` optimized-value remainder. The first omitted term is generically `N^(-3/2)` per original-sample block, which accumulates to `N^(-1/2)` over `Theta(N)` blocks.

An explicit counterexample is

`F_-(w) = 0.5 ||w||^2 + epsilon [ sin(v^T w) - v^T w ]`, with `0 < epsilon < 1/2`,

for a unit vector v, together with two identical current rows

`x_1 = x_2 = sqrt(N) v^T`

and squared block loss with residual target `e=(1,1)`.

The leave objective is globally `(1-epsilon)`-strongly convex with bounded derivatives, but

`Delta_exact - Delta_quadratic = -(4 epsilon / 81) N^(-3/2) + O(N^(-2))`.

Thus the predecessor's hoped generic `E|R_i| <= C/N^2` after quadraticizing the optimizer response is false. The requested squared-ridge Target 1 is unaffected because its leave objective is exactly quadratic, so this cubic response vanishes identically.

## New claims `P21-CROSSHAT-L4-44` and `P21-PROJECTED-CUBIC-BASE-44` — PROVED

For a smooth strongly convex empirical leave objective, the projected cubic response at the basepoint has exactly the scale needed for a future nonquadratic extension.

Assume

`F_-(w) = (1/N) sum_{a not in current block} ell(t_a - x_a^T w) + (lambda/2)||w||^2`,

with `mu <= ell'' <= L` and bounded `ell'''`.

At the leave optimizer define

`H = Hess F_-(w_-)`, `B = H^(-1)`,

and for bounded `s in R^2`,

`q_s = X_i^T s / N`, `h_s = B q_s`, `v_a(s) = x_a^T h_s`.

Uniformly for `||s|| <= S`, along the actual/Gaussian whole-block hybrid chain,

`E sup_{||s||<=S} sum_{a not in current block} |v_a(s)|^4 <= C_S / N`.

Moreover,

`E sup_{||s||<=S} | N^(3/2) D^3 F_-*(0)[q_s,q_s,q_s] | <= C_S`.

The proof conditions on the leave environment first and uses the current two-view block as the fresh object. The dimension gain appears before the training-row sum. No factor of m, m^2, sqrt(m), or sqrt(log d) is paid.

The exact remaining nonquadratic lemma is pathwise/adaptive:

`sup_{tau in [0,1]} E sup_{||s||<=S} sum_a | x_a^T H(w_{tau,s})^(-1) X_i^T s / N |^4 <= C_S/N`,

where

`w_{tau,s} = grad F_-*( tau X_i^T s / N )`.

At tau=0 this is proved by the new basepoint result. For tau>0, the inverse Hessian depends on the fresh current block through `q_s`, so the simple conditional freshness argument no longer applies. This adaptive response, not another generic CLT, is the live extension bottleneck.

---

# 1. Canonical repository state consumed

## 1.1 Shared instructions

Read directly from master:

- `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

The active protocol requires GitHub-only archival, complete immutable UTF-8 reports, exact paths/SHAs/claim IDs, primary-source verification, theorem-sized progress or a rigorous obstruction, independent peer auditing, cumulative PROVED / CONDITIONAL / DISPROVED / OPEN bookkeeping, and exact-commit readback. It requires two OTHER complete end-to-end audits before formal closure of a candidate-complete theorem.

The original report path for this run was checked before creation and returned 404. The corrected path was also checked before creation and returned 404.

## 1.2 Latest complete P21 predecessor

Read:

`proofnet24/P21-kernel-cGEC/runs/2026-09-16/2026-09-16_07-12-18__run-report.md`

- creation commit `2648f1533c37d7f10dcd956b447a9e2a7c88c25f`;
- blob `57840c23b490db2f00094fb956a334f7383e30ac`.

Retained exact-target package:

- source normalization `N=2n` and coefficient `1/(2N)`;
- whole-original-sample two-row replacement preserving the shared latent block;
- exact rank-two Woodbury optimized-value identity;
- leave-block stability and rank-two leverage freezing;
- exact teacher Gaussian-Stein identity;
- correlated odd-Hermite/Price two-view covariance comparison;
- plus/minus parity reduction;
- total `O(d^(-1/2))` training telescope and `O(d^(-1))` bounded-C2 Taylor debt;
- logically separate clean-risk theorem with an independently matched clean block.

Its newest higher-order package was `P21-RIDGE-COLQ-43`, `P21-OFFDIAG-CONTRACT-43`, `P21-BLOCK-C2-LOGFREE-43`, and `P21-JOINT-CUM4-LOGFREE-43`.

The predecessor proposed a smooth nonquadratic influence theorem with a hoped `O(N^(-2))` remainder. The present run proves the exact Fenchel influence formula and shows that this generic remainder target is false after quadraticization.

## 1.3 Latest complete P04 report plus canonical correction

Read:

`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__run-report.md`

- creation commit `55c3c8e4e245aec6d6f0420ca27dff48e71a95ea`;
- blob `53141d29bc03899d6c7d6fb832d92c69bf0e3c46`.

Its exact readback found a display-only TeX transport defect in the Target-1 objective. The canonical correction is

`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__readback-correction.md`,

blob `d1d2ed9edf2cd16466b067520f7c4aff456c5077`.

The correction explicitly confirms

`L(w) = (1/(2N)) ||y-Xw||^2 + (lambda/2)||w||^2`, with `N=2n`,

or equivalently coefficient `1/(4n)` in the two-view double sum. It states that no Target-1 theorem, bound, status, or dependency changes.

P04 continues to classify restricted Target 1 as PROVED / candidate complete, with one additional OTHER complete end-to-end audit required for formal closure.

## 1.4 Outside complete-audit count

Repository search for `AUDIT-P04-T1-ENDTOEND` still identifies one genuine outside complete audit:

`P26-AUDIT-P04-T1-ENDTOEND-17 = PASS`.

The P26 audit-health record explicitly states that repeated P21 self/specialist audits do not count as a second OTHER audit. Exactly one further qualifying outside complete audit remains required.

## 1.5 Kernel peer

Read:

`proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_07-55-37__run-report.md`

- creation commit `8039c72c8d508acd1e67be8f67934de81fb53fdc`;
- blob `425f0dab779cbd003023fde7b48cf1c3ca236687`.

The concrete audited peer claim is `P19-RISK-TO-RELATIVE-SLL-40`.

## 1.6 Probability/RMT peer

Read:

`proofnet24/P13-fourth-moment-RMT/runs/2026-09-16/2026-09-16_07-02-52__run-report.md`

- creation commit `953a8a3a41f3b6c728a387c3f2529eff3444a243`;
- blob `99e4c0fb32b7fe711a0a480b4607f7d83b0e9800`.

Its current sparse/compressible exclusion results and all-center no-go reinforce the same discipline used below: obtain the local fresh-variable gain before paying a large family-size multiplicity. No P13 theorem is imported into the P21 proof.

---

# 2. Primary-source assumptions reverified

Primary source: Oussama Dhifallah and Yue M. Lu, *On the Inherent Regularization Effects of Noise Injection During Training*, PMLR 139 (2021), official PMLR paper.

Its equation (3) is the noisy objective

`w_hat = argmin_w [ (1/(2 n ell)) sum_i sum_j ( y_i - w^T sigma(F^T[a_i + Delta z_ij]) )^2 + (lambda/2)||w||^2 ]`.

At exactly two augmentations,

`N = 2n` and `1/(2 n ell) = 1/(4n) = 1/(2N)`.

Contribution C.1 explicitly calls the assertion a correlated Gaussian equivalence conjecture. Its matched Gaussian row has the form

`q_ij = mu_0 1 + mu_e F^T a_i + mu_b F^T z_ij + mu_2 b_i + mu_3 p_ij`.

Thus `a_i` and `b_i` are shared across both augmentations of original sample i, while `z_ij` and `p_ij` are view-private. For odd activation, `mu_0=0`.

The paper also emphasizes that the Gaussian matrices in its multivariate formulation are dependent because they share a common Gaussian block. A viewwise replacement would destroy exactly this dependence.

Public source URLs rechecked this run:

- `https://proceedings.mlr.press/v139/dhifallah21a.html`
- `https://proceedings.mlr.press/v139/dhifallah21a/dhifallah21a.pdf`

The rigorous architectural precedent remains Hong Hu and Yue M. Lu, *Universality Laws for High-Dimensional Learning with Random Features*, arXiv:2009.07669, public v3. Its abstract explicitly identifies classical Lindeberg replacement, leave-one-out optimization, and a Stein-method CLT for weakly correlated variables as major ingredients. That theorem concerns the unperturbed model; it supports the architecture, not a false splitting of the two noisy views.

---

# 3. Exact restricted Target-1 model

Let `F=[f_1,...,f_m] in R^(d x m)` with iid entries `N(0,1/d)` and ratios `n/d -> alpha > 0`, `m/d -> beta > 0`.

For original sample i,

`a_i, z_i1, z_i2 iid N(0,I_d)`,

`t_i = xi^T a_i`, with `||xi||=1`.

The actual two rows are

`x_ij^A = sigma( F^T (a_i + Delta z_ij) )`, for j=1,2.

The matched Gaussian rows preserve the shared source structure:

`x_ij^G = mu_e F^T a_i + mu_b F^T z_ij + mu_2 b_i + mu_3 p_ij`,

with `b_i` shared and `p_ij` private.

Stack the two current rows into `X_i in R^(2 x m)` and remove both rows. Define

`H_- = lambda I + (1/N) X_-^T X_-`,

`B = H_-^(-1)`,

`e_i = t_i 1_2 - X_i w_-`,

`Q_i = (1/N) X_i B X_i^T`.

The exact squared-ridge block increment is

`L_i* - L_-* = (1/(2N)) e_i^T (I_2 + Q_i)^(-1) e_i`.

Section 6 below independently rederives this identity from convex duality rather than merely citing the existing Woodbury calculation.

---

# 4. Retained block Lindeberg theorem and TOTAL error

Use the orthogonal plus/minus transform

`x_+ = (x_1+x_2)/sqrt(2)`, `x_- = (x_1-x_2)/sqrt(2)`,

`u_+ = x_+^T w_-`, `u_- = x_-^T w_-`.

View exchange fixes `(t,u_+)` and sends `u_-` to `-u_-`. Global sign symmetry for odd sigma and the linear teacher sends all three coordinates to their negatives. After freezing the 2 by 2 leverage, the squared-ridge block needs only

`E[t u_+]`, `E[u_+^2]`, and `E[u_-^2]`.

For one feature coordinate, conditional on F, exact Gaussian integration by parts gives

`E[ t sigma(f_r^T(a+Delta z_j)) | F ] = (xi^T f_r) E[ sigma'(f_r^T(a+Delta z_j)) | F ]`.

The two-view covariance calculation must retain the common a. Oddness removes all even Hermite levels. The retained dependence-safe feature averaging controls the first unmatched off-diagonal Hermite contribution and diagonal feature-norm corrections.

The resulting unscaled one-original-sample actual/Gaussian mismatch is

`O(d^(-1/2))`.

Only after this comparison is the exact optimized-value prefactor inserted. Therefore

`one original-sample replacement = O( (N sqrt(d))^(-1) )`.

There are exactly `n=N/2` original-sample blocks, so

`TOTAL first-order training error = n O((N sqrt(d))^(-1)) = O(d^(-1/2))`.

For bounded-C2 tests the block increment has fixed moments at scale `N^(-1)`, so the complete second-order Taylor debt is

`n O(N^(-2)) = O(d^(-1))`.

The invalid arithmetic is to multiply the raw `O(d^(-1/2))` covariance discrepancy by n. The `1/(2N)` optimized-value influence enters first.

---

# 5. Separate clean-test prediction-risk theorem

Optimized training value does not imply clean prediction risk.

Let an independent correctly matched clean block define

`R0_hat(w) = c_0 - 2 r_0^T w + w^T S_0 w`.

At the leave-training-block optimizer define

`v_- = B(S_0 w_- - r_0)`,

`A_i = (I_2 + Q_i)^(-1)`,

`R_i = (1/N) X_i B S_0 B X_i^T`.

The exact current-training-block clean-risk increment is

`Gamma_i = (1/N) [ 2 e_i^T A_i X_i v_- + e_i^T A_i R_i A_i e_i ]`.

The joint fixed-rank freezing estimates are

`||A(Q)-A(Q_0)|| <= ||Q-Q_0||`,

and

`|| A R A - A_0 R_0 A_0 || <= ||R-R_0|| + (||R||+||R_0||) ||A-A_0||`.

Differentiating the whole current shared block gives `O(d^(-1/2))` L2 freezing debt for these fixed-rank matrices without an ambient-coordinate penalty. Parity removes the mixed odd-minus terms. The surviving teacher-Stein, bilinear, diagonal, and trace quantities have unscaled mismatch `O(d^(-1/2))`.

Hence

`one clean training-block replacement = O((N sqrt(d))^(-1))`,

and all `n=N/2` training replacements total `O(d^(-1/2))`, with `O(d^(-1))` second-order debt.

For an independent matched empirical clean test block of size M, empirical-to-population fluctuation is `O(M^(-1/2))`. Therefore, for `M asymp d`, the complete clean-test transfer remains `O(d^(-1/2))`.

This theorem is logically separate from the optimized training-value theorem.

---

# 6. Full proof of `P21-FENCHEL-BLOCK-44`

Let `F_- : R^m -> R union {+infinity}` be proper, closed, and strongly convex. The current block contributes

`(1/N) phi(t-Xw)`, with `phi(r)=ell(r_1)+ell(r_2)`.

Fenchel duality gives

`phi(t-Xw) = sup_s { s^T(t-Xw) - phi*(s) }`.

Strong convexity gives the standard Fenchel-Rockafellar interchange. Thus

`L_i* = sup_s [ (1/N)(s^T t - phi*(s)) + min_w { F_-(w) - w^T X^T s/N } ]`.

The inner minimum is

`-F_-*(X^T s/N)`.

Also

`L_-* = -F_-*(0)` and `grad F_-*(0)=w_-`.

Subtracting and writing `e=t-Xw_-` gives exactly

`L_i* - L_-* = (1/N) sup_s { s^T e - phi*(s) - K_N(s) }`,

where

`K_N(s)=N[F_-*(X^T s/N)-F_-*(0)-w_-^T X^T s/N]`.

Convexity of the conjugate and its tangent inequality at zero imply

`K_N(s)>=0`, `K_N(0)=0`, and `grad K_N(0)=0`.

If `F_-` is smooth Legendre, put `q_s=X^T s/N` and `w_s=grad F_-*(q_s)`. Differentiation yields

`grad K_N(s)=X(w_s-w_-)`,

and

`Hess K_N(s) = (1/N) X Hess F_-*(q_s) X^T = (1/N) X [Hess F_-(w_s)]^(-1) X^T`.

If `0<mu<=ell''<=L`, then the scalar conjugate obeys

`1/L <= (ell*)'' <= 1/mu`.

Therefore `phi*+K_N` is `1/L`-strongly convex. Its conjugate `Psi_N` has Hessian bounded between zero and `L I_2`. This proves the dimension-free bounded-Hessian statement.

## 6.1 Exact recovery of the P04 Woodbury formula

For squared ridge, the leave objective is exactly quadratic around w_-:

`F_-(w) = L_-* + 0.5 (w-w_-)^T H_- (w-w_-)`.

Therefore

`F_-*(q)-F_-*(0)-w_-^T q = 0.5 q^T B q`, with `B=H_-^(-1)`.

For `q=X^T s/N`,

`K_N(s) = 0.5 s^T Q s`, with `Q=(1/N) X B X^T`.

For scalar squared loss `ell(r)=r^2/2`,

`phi*(s)=0.5 ||s||^2`.

Hence

`Psi_N(e) = sup_s { s^T e - 0.5 s^T(I_2+Q)s } = 0.5 e^T(I_2+Q)^(-1)e`.

Thus

`L_i* - L_-* = (1/(2N)) e^T(I_2+Q)^(-1)e`.

This is an independent derivation of `T1-TWO-VIEW-LOO-WOODBURY` and checks the exact normalization simultaneously.

## 6.2 Why the quadratic problem is special

In the quadratic case all current-block dependence beyond e is compressed into the fixed 2 by 2 matrix Q, which can be frozen with `O(d^(-1/2))` unscaled debt. In a nonquadratic problem `K_N(s)` samples the full conjugate response along the path

`q_s = X^T s/N`.

Even though `Psi_N` has a dimension-free Hessian in e, `K_N` itself depends on the current block X. Therefore the retained fixed-dimensional block CLT for `(t,u_+,u_-)` does not by itself compare the exact nonquadratic increment.

---

# 7. `P21-CUBIC-RESPONSE-44` — deterministic third-order expansion

This is a deterministic local theorem under explicit regularity, not a completed random-feature nonquadratic universality theorem.

Assume `F_-*` is C4 near zero. Let

`B = Hess F_-*(0) = H_-^(-1)`.

Assume `||X||_op <= C sqrt(N)` and the fourth derivative of `F_-*` is bounded on the relevant `q_s` ball. For bounded s, Taylor expansion gives

`K_N(s) = 0.5 s^T Q s + (N/6) D^3 F_-*(0)[q_s,q_s,q_s] + O(N ||q_s||^4)`.

Since `||q_s||=O(N^(-1/2))`, define

`Gamma_N(s) = N^(3/2) D^3 F_-*(0)[q_s,q_s,q_s]`.

Then

`K_N(s) = 0.5 s^T Q s + Gamma_N(s)/(6 sqrt(N)) + O(N^(-1))`.

Define

`Psi_Q(e) = sup_s { s^T e - phi*(s) - 0.5 s^T Q s }`

and let `s_0(e)` be its unique maximizer. Strong convexity of `phi*` keeps the maximizer in a fixed ball for bounded e. Strong-concavity perturbation / the envelope theorem then gives

`L_i* - L_-* = (1/N) Psi_Q(e) - Gamma_N(s_0(e))/(6 N^(3/2)) + O(N^(-2))`.

The sign is negative because `K_N` is subtracted in the dual objective.

Therefore a generic cubic optimizer-response correction is `O(N^(-3/2))` per original block. With `n=N/2` blocks it can contribute `O(N^(-1/2))`. It cannot be silently put into the ordinary `O(N^(-2))` per-block Taylor debt.

---

# 8. `P21-NAIVE-N2-REMAINDER-NOGO-44` — exact counterexample

Let v be a unit vector and choose `0<epsilon<1/2`. Set

`F_-(w)=0.5||w||^2 + epsilon[sin(v^T w)-v^T w]`.

Along `a=v^T w`,

`f(a)=0.5a^2+epsilon(sin a-a)`.

Then

`f'(a)=a+epsilon(cos a-1)`

and

`f''(a)=1-epsilon sin a >= 1-epsilon > 0`.

Thus `F_-` is globally strongly convex with bounded higher derivatives, with minimizer `w_-=0` and Hessian identity at zero.

The conjugate expansion is

`f*(q)=0.5 q^2 + (epsilon/6) q^3 + O(q^4)`.

Take two identical current rows

`x_1=x_2=sqrt(N) v^T`

and squared block loss with residual target `e=(1,1)`.

Then

`Q = [[1,1],[1,1]]`,

and

`s_0 = (I_2+Q)^(-1)e = (1/3,1/3)`.

Also

`q_s = ((s_1+s_2)/sqrt(N)) v`.

Therefore

`K_N(s)=0.5(s_1+s_2)^2 + [epsilon/(6 sqrt(N))](s_1+s_2)^3 + O(N^(-1))`.

At `s_0`, `(s_1+s_2)^3=8/27`, so

`Delta_exact - Delta_quadratic = -(4 epsilon/81) N^(-3/2) + O(N^(-2))`.

This is a rigorous counterexample to a generic `O(N^(-2))` remainder after freezing a smooth nonquadratic response at its Hessian.

There is no conflict with the requested P04 Target 1 because the squared-ridge leave objective is exactly quadratic and `D^3 F_-* = 0` identically.

---

# 9. `P21-CROSSHAT-L4-44` — basepoint projected influence delocalization

Assume the empirical leave objective

`F_-(w)=(1/N) sum_a ell(t_a-x_a^T w)+(lambda/2)||w||^2`,

with `0<mu<=ell''<=L` and `|ell'''|<=M_3`.

At w_- write

`H = lambda I + (1/N) X_-^T D X_-`,

where `D=diag(ell''(r_a)) >= mu I`, and `B=H^(-1)`.

For bounded s define

`q_s=X_i^T s/N`, `h_s=B q_s`, `v_a(s)=x_a^T h_s=(1/N)s^T X_i B x_a`.

Fix a leave row a and define `c_a=B x_a`. Conditional on the entire leave environment and on F, the current original-sample block is fresh.

For an actual row,

`c_a^T x_ij^A = c_a^T sigma(F^T(a_i+Delta z_ij))`.

It is centered because sigma is odd and the fresh Gaussian current latent is symmetric. Its gradient in that current Gaussian latent has norm at most

`C_Delta ||F||_op ||sigma'||_infinity ||c_a||`.

Gaussian concentration therefore gives the conditional fourth-moment estimate

`E_i ||X_i c_a||^4 <= C (1+||F||_op)^4 ||c_a||^4`.

For the matched Gaussian current block the same bound follows directly from its conditional Gaussian covariance, with the shared `a_i,b_i` structure intact.

For `||s||<=S`,

`|v_a(s)|^4 <= S^4 N^(-4) ||X_i c_a||^4`.

The curvature Hessian gives the exact leverage control. Since

`(mu/N) x_a x_a^T <= H`,

one has

`(mu/N) x_a^T B x_a <= 1`.

Also `B^2 <= lambda^(-1) B`, so

`||B x_a||^2 = x_a^T B^2 x_a <= lambda^(-1) x_a^T B x_a <= N/(mu lambda)`.

Therefore, over `O(N)` leave rows,

`sum_a ||B x_a||^4 <= C N^3`.

Combining these bounds and using dimension-uniform fixed moments of the Gaussian feature operator norm gives

`E sup_{||s||<=S} sum_a |v_a(s)|^4 <= C_S/N`.

This proves `P21-CROSSHAT-L4-44`.

There is also a deterministic second-energy bound:

`(mu/N) sum_a v_a(s)^2 <= h_s^T H h_s = q_s^T B q_s`.

Because `B<=lambda^(-1)I` and a two-row current block has `||X_i||_op=O_Lq(sqrt(N))`, the quantity `sum_a v_a(s)^2` has bounded fixed moments uniformly for bounded s.

---

# 10. `P21-PROJECTED-CUBIC-BASE-44` — correct cubic scale at the basepoint

The third derivative of the empirical leave objective is

`D^3 F_-(w_-)[h,h,h] = -(1/N) sum_a ell'''(r_a) (x_a^T h)^3`.

Set `h=h_s`. Cauchy-Schwarz gives

`sum_a |v_a|^3 <= (sum_a v_a^2)^(1/2) (sum_a v_a^4)^(1/2)`.

Using the second-energy bound and `P21-CROSSHAT-L4-44`,

`E sup_{||s||<=S} |D^3 F_-(w_-)[h_s,h_s,h_s]| <= C_S N^(-3/2)`.

For a Legendre conjugate,

`D^3 F_-*(0)[q,q,q] = -D^3 F_-(w_-)[Bq,Bq,Bq]`.

Hence

`E sup_{||s||<=S} | N^(3/2) D^3 F_-*(0)[q_s,q_s,q_s] | <= C_S`.

This proves `P21-PROJECTED-CUBIC-BASE-44`.

The dimension audit is explicit: the current two-row block is exposed last; its conditional fourth-moment gain is obtained before summing over leave rows; ridge/curvature provides a leverage inequality; no global ambient tensor norm is used.

## 10.1 Why the pathwise extension remains open

Taylor's theorem for K_N samples the dual response along

`q = tau X_i^T s/N`, for `0<=tau<=1`.

Equivalently, the relevant inverse Hessian is

`H(w_{tau,s})^(-1)`, with `w_{tau,s}=grad F_-*(tau q_s)`.

Although `F_-` contains only leave rows, `w_{tau,s}` depends on the current block through `q_s`. Thus `H(w_{tau,s})^(-1) x_a` is no longer fixed when conditioning on the current fresh block. The argument from Section 9 cannot be repeated verbatim.

A naive ambient operator bound on `H(w_tau)^(-1)-H(w_-)^(-1)` is too crude and can reintroduce exactly the dimension factors that the block method avoids. The next attack must preserve the current-block freshness inside a derivative or contraction.

---

# 11. Method comparison and dependence audit

## Block Lindeberg

Whole-original-sample block Lindeberg remains the sharp method for the requested squared-ridge theorem. It preserves shared `a_i`, teacher `t_i`, and shared Gaussian residual `b_i`. The exact `1/N` influence appears before summation and produces total `O(d^(-1/2))`.

## Correlated Stein / odd-Hermite

Once the rank-two leverage is frozen and plus/minus parity is used, squared ridge needs only three same-parity second moments. A strong full-vector CLT is unnecessary.

## Contracted second-order Poincare / interpolation

The retained `P21-BLOCK-C2-LOGFREE-43` is a stronger projection-level smooth comparison and is useful for extensions. It does not imply coordinatewise Gaussianization. This run shows that the missing nonquadratic object is the adaptive response path K_N, not the fixed-dimensional block CLT itself.

## Fenchel duality and local resolvents

The exact dual formula is the nonlinear convex analogue of the rank-two resolvent formula. For squared ridge, `F_-*` is quadratic, so

`K_N(s)=0.5 s^T Q_i s`,

and the local resolvent `(I_2+Q_i)^(-1)` is exact. For nonquadratic loss the two-dimensional dual remains exact, but the local inverse Hessian evolves along the dual path. That is why the quadratic theorem closes with a frozen rank-two resolvent.

## Global resolvents / nonlinear Gram universality

Not needed for Target 1. A global nonlinear-Gram theorem is stronger than the target and risks paying spurious m, m^2, or d m factors.

## Naive CLTs

Rejected for three independent reasons:

1. the two views share `a_i` and the teacher scalar;
2. actual plus/minus channels can be dependent despite zero mixed covariance;
3. a bounded tanh feature coordinate stays a positive total-variation distance from its Gaussian surrogate coordinate.

The valid theorem is a target-functional block comparison, not coordinatewise Gaussianization.

## New nonquadratic normalization warning

The generic cubic response is `N^(-3/2)` per block. With `Theta(N)` blocks it is `N^(-1/2)` total. Any proof that labels it `O(N^(-2))` without extra cancellation or explicit comparison loses the target scale.

---

# 12. Independent audit of newest P04 Target 1

## `P21-AUDIT-P04-T1-0746-44` — PASS

**Source report:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__run-report.md`  
**Creation commit:** `55c3c8e4e245aec6d6f0420ca27dff48e71a95ea`  
**Report blob:** `53141d29bc03899d6c7d6fb832d92c69bf0e3c46`  
**Canonical Target-1 rendering correction:** `2026-09-16_07-46-09__readback-correction.md`, blob `d1d2ed9edf2cd16466b067520f7c4aff456c5077`.

Audited retained claim IDs:

- `T1-EXACT-OBJECTIVE-NORMALIZATION`;
- `T1-TWO-VIEW-LOO-WOODBURY`;
- `T1-TOTAL-BLOCK-LINDEBERG`;
- `T1-SHARED-LATENT-PRESERVATION`;
- `T1-CLEAN-TEST-JOINT-MATCH`.

### Normalization check

The official PMLR equation (3) has `1/(2 n ell)`. At ell=2 and N=2n this is exactly `1/(4n)=1/(2N)`. The newest P04 historical report contains one broken transport token in this display, but its canonical readback correction explicitly restores this formula. This is a rendering defect only.

### Whole-block Woodbury check

Section 6 independently derives the exact block influence using Fenchel duality. In the squared-ridge specialization it reproduces

`(1/(2N)) e_i^T (I_2+Q_i)^(-1)e_i`,

with `Q_i=N^(-1) X_i H_-^(-1) X_i^T`.

### Total-error check

The unscaled frozen current-block mismatch is `O(d^(-1/2))`. Insert the exact optimized-value factor first. One block costs `O((N sqrt(d))^(-1))`; `n=N/2` blocks cost `O(d^(-1/2))`. The bounded-C2 second-order debt is `n O(N^(-2))=O(d^(-1))`.

### Shared-latent check

The official cGEC row contains both `F^T a_i` and a shared `b_i` term. The two views are one replacement block. Replacing them separately would destroy precisely the intended source correlation.

### Separate clean theorem check

The clean-risk proof uses the exact increment from Section 5, joint freezing of A_i and R_i, and an independently matched clean test block. It is not deduced from optimized training value.

No normalization, dependence, dimension, or circularity defect was found.

`P21-AUDIT-P04-T1-0746-44: PASS`.

---

# 13. Independent peer audit — P19 risk-to-relative-SLL transfer

## `P21-AUDIT-P19-RISK-TO-RELATIVE-SLL-44` — PASS

**Source path:** `proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_07-55-37__run-report.md`  
**Creation commit:** `8039c72c8d508acd1e67be8f67934de81fb53fdc`  
**Blob:** `425f0dab779cbd003023fde7b48cf1c3ca236687`  
**Claim:** `P19-RISK-TO-RELATIVE-SLL-40`.

Let `D=P-P_0` and `G=E[psi psi*]`. Assume every row delta of D is supported on a pruning-admissible difference support and G has simultaneous restricted floor a on every such support:

`delta G delta* >= a ||delta||^2`.

Then

`E ||D psi||^2 = tr(D G D*) = sum_rows delta G delta* >= a ||D||_F^2`.

Therefore

`||P-P_0||_op <= ||P-P_0||_F <= (E||D psi||^2)^(1/2) / sqrt(a)`.

Let `g=sigma_r(P_0)>0` and

`q=(E||D psi||^2)^(1/2)/(g sqrt(a))`.

If q<1, then `||D||_op/g <= q`. The standard pseudoinverse principal-angle argument gives left and right projector distances at most q. Optimal Procrustes alignment gives

`h(q)=sqrt(2-2 sqrt(1-q^2)) <= sqrt(2) q`.

Applying the exact asymmetric compressed-resolvent identity to the aligned frames transfers the proxy SLL as

`epsilon_actual(K) <= epsilon_0(K) + 2 R_K h(q)`.

The same-matrix empirical certificate is also sound. If `Ghat=Z*Z/M` has a simultaneous restricted floor over the whole structured class, then pathwise

`M^(-1)||Z D*||_F^2 = tr(D Ghat D*) >= ahat ||D||_F^2`.

This remains valid even when D, its selected support, P, and P_0 depend on the same realized Z, because the restricted-floor event is uniform over the class. No iid-mask independence is inserted.

The source counterexample is valid: with `G=diag(1,0)`, `P_0=(1,0)`, `P=(1,epsilon)`, and probes `(Z,0)`, prediction discrepancy is zero while the right singular direction changes. A restricted floor is structurally necessary.

`P21-AUDIT-P19-RISK-TO-RELATIVE-SLL-44: PASS`.

---

# 14. Numerical and algebraic tests

These tests are not part of the proof.

For the explicit no-go counterexample with `epsilon=0.4`, the analytic scaled coefficient is

`-4 epsilon/81 = -0.019753086419753086...`.

Direct scalar minimization of the exact full objective gives:

| N | N^(3/2) (Delta_exact - Delta_quad) |
|---:|---:|
| 100 | -0.01988147 |
| 400 | -0.01981811 |
| 1600 | -0.01978581 |
| 6400 | -0.01976950 |
| 25600 | -0.01976130 |

The values converge to the analytic coefficient, checking the sign and normalization only.

Algebraic checks:

1. The Fenchel formula reproduces the exact ridge factor `1/(2N)`, not `1/N` or `1/(4N)`.
2. In the counterexample, `D^3 F_-*(0)[v,v,v]=epsilon`, while `q_s=(s_1+s_2)v/sqrt(N)`, yielding the `N^(-1/2)` perturbation in K_N and `N^(-3/2)` in the optimized block value.
3. The leverage inequality follows from the rank-one matrix order `(mu/N)x_a x_a^T <= H`; no row independence is assumed.
4. The current-block fourth-moment gain is taken before the leave-row sum.
5. At tau>0 the inverse Hessian genuinely depends on the current block through q_s, so the pathwise freshness issue is not cosmetic.

---

# 15. Failed and rejected routes preserved

1. Replacing the two augmentations separately — INVALID; destroys shared `a_i,t_i,b_i`.
2. Multiplying raw `O(d^(-1/2))` covariance mismatch by n — INVALID; insert `1/(2N)` first.
3. Treating teacher and logits independently — INVALID; they share a_i.
4. Inferring actual plus/minus independence from zero covariance — DISPROVED in retained work.
5. Coordinatewise total-variation Gaussianization — DISPROVED for bounded tanh coordinates.
6. Demanding a strong full-vector CLT for squared ridge — UNNECESSARY.
7. Max-coordinate nonlinear-Hessian control — too crude; pays sqrt(log d).
8. Generic log-free Hessian operator norm from coordinate l4 delocalization — DISPROVED by `P21-OPNORM-ROUTE-NOGO-42`.
9. Taking an operator/Frobenius norm before fresh-variable averaging — too crude and loses dimensions.
10. Inferring clean prediction risk from optimized training value — FALSE.
11. Reusing noisy-training Gaussian coefficients at clean test — FALSE.
12. Assuming negative-real interpolation preserves convexity — FALSE in general.
13. Global nonlinear-Gram universality as prerequisite — FALSE.
14. Quadraticizing a smooth nonquadratic leave response and declaring an `O(N^(-2))` remainder — DISPROVED this run; generic cubic response is `N^(-3/2)` per block.
15. Treating the basepoint projected-cubic estimate as uniform along the dual path — UNJUSTIFIED; adaptive path dependence remains open.

---

# 16. Cumulative dependency ledger

## PROVED — exact requested squared-ridge Target 1

- exact source normalization `N=2n`, coefficient `1/(2N)`;
- source-matched shared-latent two-view Gaussian architecture;
- whole-original-sample replacement;
- exact rank-two Woodbury optimized-value identity;
- leave-block ridge stability and leverage freezing;
- exact teacher Gaussian-Stein identity;
- correlated two-view odd-Hermite/Price covariance comparison;
- plus/minus parity reduction;
- dependence-safe feature averaging and cubic/diagonal correction control;
- unscaled one-block mismatch `O(d^(-1/2))`;
- one optimized-value block error `O((N sqrt(d))^(-1))`;
- TOTAL training replacement `O(d^(-1/2))` after `n=N/2` blocks;
- bounded-C2 Taylor debt `O(d^(-1))`;
- separate clean-risk exact block identity and joint freezing;
- separate total clean training replacement `O(d^(-1/2))`;
- independent matched clean test block contribution `O(M^(-1/2))`;
- retained `P21-RIDGE-COLQ-43`, `P21-OFFDIAG-CONTRACT-43`, `P21-BLOCK-C2-LOGFREE-43`, `P21-JOINT-CUM4-LOGFREE-43`;
- new `P21-FENCHEL-BLOCK-44`;
- new deterministic `P21-CUBIC-RESPONSE-44` under its explicit local regularity assumptions;
- new `P21-NAIVE-N2-REMAINDER-NOGO-44`;
- new `P21-CROSSHAT-L4-44`;
- new `P21-PROJECTED-CUBIC-BASE-44`;
- newest P04 Target-1 audit PASS;
- newest P19 peer audit PASS.

## CONDITIONAL / PROTOCOL-OPEN

- The mathematical restricted Target-1 theorem is candidate complete, but formal closure still requires one additional OTHER complete independent end-to-end audit beyond P26's existing audit.
- Smooth strongly convex nonquadratic-loss universality is conditional on controlling the adaptive dual-response path, for example by the pathwise cross-hat bound stated above or an equivalent averaged resolvent/Stein contraction.
- ReLU/nonsmooth activation, nonlinear teacher, and vanishing ridge remain outside the exact theorem.

## DISPROVED / REJECTED

- viewwise replacement;
- raw `n d^(-1/2)` accumulation;
- teacher/logit independence;
- marginal-only view matching;
- actual plus/minus independence;
- coordinatewise total-variation Gaussianization;
- strong joint CLT as prerequisite for squared ridge;
- generic log-free Hessian-operator control from coordinate l4 delocalization;
- premature Frobenius/operator summation of off-diagonal interactions;
- objective-to-clean inference;
- reuse of noisy coefficients at clean test;
- automatic negative-real convex interpolation;
- global nonlinear-Gram universality as prerequisite;
- new: generic `O(N^(-2))` optimized-value remainder after quadraticizing a smooth nonquadratic leave objective.

## OPEN

1. One additional qualifying OTHER complete end-to-end Target-1 audit for protocol closure.
2. Pathwise adaptive cross-hat estimate along the dual response, or an equivalent contraction.
3. Smooth strongly convex nonquadratic loss extension after item 2.
4. ReLU/nonsmooth activation.
5. Nonlinear teacher.
6. Vanishing ridge.
7. Higher-order universality beyond bounded-Hessian fixed-dimensional block tests.

---

# 17. Exact next attack

The exact squared-ridge theorem needs no new lemma. Its leave objective is quadratic, so the cubic dual response is identically zero.

For the next extension, define

`q_s = X_i^T s/N`,

`w_{tau,s}=grad F_-*(tau q_s)`,

`B_{tau,s}=Hess F_-(w_{tau,s})^(-1)`.

The exact remaining lemma is

`sup_{0<=tau<=1} E sup_{||s||<=S} sum_a | (1/N) s^T X_i B_{tau,s} x_a |^4 <= C_S/N`.

A successful proof should avoid `max_a`, avoid global Hessian perturbation norms, and preserve the order of operations that succeeded at tau=0:

1. leave out the whole original-sample block;
2. expose the fresh current block only after fixing the leave environment;
3. differentiate the adaptive inverse Hessian with respect to the current shared two-view latent rather than bounding it absolutely;
4. contract before summing over rows;
5. use the curvature leverage inequality `(mu/N)x_a x_a^T <= H` and retained ridge delocalization moments;
6. only then pay the `O(N)` row multiplicity.

If this pathwise estimate and its fourth-order analogue hold, the exact Fenchel representation yields a controlled cubic `N^(-3/2)` correction rather than pretending it vanishes. The retained log-free block comparison can then be applied to the leading bounded-Hessian influence and the finite-dimensional cubic correction, giving the natural total `O(d^(-1/2))` scale for a smooth nonquadratic extension.

---

# 18. Source list

Primary/current sources checked this run:

1. Dhifallah and Lu, *On the Inherent Regularization Effects of Noise Injection During Training*, PMLR 139 (2021): `https://proceedings.mlr.press/v139/dhifallah21a.html` and `https://proceedings.mlr.press/v139/dhifallah21a/dhifallah21a.pdf`.
2. Hu and Lu, *Universality Laws for High-Dimensional Learning with Random Features*, arXiv:2009.07669: `https://arxiv.org/abs/2009.07669`.
3. P21 predecessor: `proofnet24/P21-kernel-cGEC/runs/2026-09-16/2026-09-16_07-12-18__run-report.md`, commit `2648f1533c37d7f10dcd956b447a9e2a7c88c25f`, blob `57840c23b490db2f00094fb956a334f7383e30ac`.
4. Newest P04: `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__run-report.md`, commit `55c3c8e4e245aec6d6f0420ca27dff48e71a95ea`, blob `53141d29bc03899d6c7d6fb832d92c69bf0e3c46`, plus correction blob `d1d2ed9edf2cd16466b067520f7c4aff456c5077`.
5. P19 peer: `proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_07-55-37__run-report.md`, commit `8039c72c8d508acd1e67be8f67934de81fb53fdc`, blob `425f0dab779cbd003023fde7b48cf1c3ca236687`.
6. P13 peer: `proofnet24/P13-fourth-moment-RMT/runs/2026-09-16/2026-09-16_07-02-52__run-report.md`, commit `953a8a3a41f3b6c728a387c3f2529eff3444a243`, blob `99e4c0fb32b7fe711a0a480b4607f7d83b0e9800`.

---

# 19. Delivery record

- No email was sent, drafted, forwarded, searched, or used for coordination/archive.
- No unavailable GPT-6 or reasoning-effort control is claimed.
- No hidden agent or inaccessible source is claimed.
- The same-run historical report with transport defects remains immutable.
- This corrected file is the complete canonical UTF-8 report for the run.
- The actual commit SHA and blob SHA are to be verified by exact-commit readback immediately after this write, as required by protocol.
