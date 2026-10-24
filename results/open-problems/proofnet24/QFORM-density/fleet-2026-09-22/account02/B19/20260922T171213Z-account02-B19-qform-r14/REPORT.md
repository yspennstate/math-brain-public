# account02/B19 — cross-cut half-Hölder smoothing and the high-Schur-offdiagonal splice

Run: `20260922T171213Z-account02-B19-qform-r14`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed: revision `2026-09-22.8`  
Assignment: Universal proof assembly / SYNTHESIS  
Classification: `ESSENTIAL_STEP_APPLIED` plus a local `CANDIDATE_REFUTED`; full target remains OPEN.

## 1. Exact target and source pins

Target: for independent real coordinates with probability densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of Q=X^TAX, or give a target-valid counterexample. No moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption is added.

Fresh source dependencies actually read and applied:

* named partner account03/B19, run `20260922T160316Z-account03-B19-QFORM-r14`, canonical mathematics `yspennstate/math-open-problems@7291482e652c4cb47efc44c1656c0af46fa0f45e`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T160316Z-account03-B19-QFORM-r14/REPORT.md`. I use its exact opposite-sign physical-pivot quarter-kernel/Hölder splice and its fixed-first-singular-value Schur-cross-bank closure.
* account02/B06, canonical mathematics `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. I use `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`: for any k-dimensional orthogonal projection of an original product law with coordinate density caps one, the projected density is at most exp(k/2).
* account01/B19, handoff source `yspennstate/math-open-problems@46d99d0364a9bf15376b5c8875cdd321373ba75c`, which proves the target-level branch `s_2(A-diag A)<=3/10` with density <66. Thus any remaining counterexample satisfies `s_2(A-diag A)>3/10`.
* orientation-free rank-two affine half-Riesz synthesis `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, used only as part of the current conditional end-to-end map; it is not needed in the new lemma below.

Live corrections respected include the false law-uniform pointwise Fresnel bound, no independence after rotation, no unrestricted fiber supremum, no fabricated conditional cap after sum/difference rotation, no fixed-good-minor dichotomy, and the Plücker-support/two-pivot-support disjointness correction.

## 2. New theorem: arbitrary-self-term cross-cut half-Hölder smoothing

### Theorem 2.1 — `QFORM-CROSSCUT-HALF-HOLDER-v1`

Let U=(U_i)_{i in I} and V=(V_j)_{j in J} be two independent original-coordinate blocks. Every coordinate has a probability density bounded by one. Let F(U),G(V) be arbitrary measurable real functions and let C be a real |I| by |J| matrix whose first two singular values satisfy s1>=s2>0. Put

`T = F(U) + 2 U^T C V + G(V)`.

Then for every interval K of length h>0,

`P(T in K) <= e^(1/2) pi^(1/4) h^(1/2) (s1 s2)^(-1/4)`.       (2.1)

No quadratic assumption on F or G is required. In particular, arbitrary within-bank quadratic terms and arbitrary affine terms are allowed.

### Proof

For fixed V define

`a(V)=P_U(T in K | V)`.

By Cauchy-Schwarz and an independent copy U' of U,

`P(T in K)^2 <= E_V a(V)^2`
`= P(T(U,V) in K and T(U',V) in K)`.                         (2.2)

On the event in (2.2), because K has length h,

`|T(U,V)-T(U',V)| <= h`.

The whole G(V) term cancels, leaving

`T(U,V)-T(U',V)`
`= F(U)-F(U') + 2 (U-U')^T C V`.                              (2.3)

Write Z=U-U'. Its coordinates are independent and each difference density satisfies

`g_i(z)=int f_i(x)f_i(x-z) dx <= ||f_i||_infinity int f_i <=1`.       (2.4)

Condition on U,U'. Let w=C^T Z. If w is nonzero, the scalar projection `(w/||w||)^T V` has density at most `e^(1/2)` by `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` with k=1. Therefore the conditional probability in (2.2) is at most

`h e^(1/2) / (2 ||C^T Z||)`.                                  (2.5)

Let u1,u2 be the first two left singular vectors of C and set

`Y=(u1^T Z,u2^T Z)`.

Again by the weighted affine-fiber theorem, now with k=2, Y has a joint density bounded by e. Hence

`W=(s1 Y1,s2 Y2)`

has density bounded by

`L=e/(s1 s2)`.                                                    (2.6)

Since `||C^T Z|| >= ||W||`, it remains to bound the inverse radius of an arbitrary R^2 probability density bounded by L. Layer cake gives

`E ||W||^(-1)`
`= int_0^infinity P(||W|| < t^(-1)) dt`
`<= int_0^infinity min(1, pi L t^(-2)) dt`
`= 2 sqrt(pi L)`
`= 2 sqrt(pi e/(s1 s2))`.                                        (2.7)

A zero value of w occurs only on a null set once s2>0, and (2.7) supplies the integrable majorant. Averaging (2.5) and using (2.7),

`P(T in K)^2 <= h e sqrt(pi) / sqrt(s1 s2)`.                    (2.8)

Taking square roots proves (2.1). QED.

### Why this is correction-safe

The proof never conditions on a rotated sum/difference variable and never asserts that such a conditional law preserves the density cap. The only new random vector Z=U-U' still has independent original-coordinate differences, each with a genuine density cap one by convolution. The only projected densities are unconditional orthogonal projections, paid by the source-proved weighted affine-fiber Brascamp-Lieb theorem.

## 3. Quantitative random-cut certificate for a high second off-diagonal singular value

### Lemma 3.1 — `QFORM-KYFAN-CUT-TRICHOTOMY-v1`

Let H be a real symmetric zero-diagonal matrix and suppose `s2(H)>tau>0`. Then there is a nontrivial coordinate bipartition I|J, with C=H[I,J], such that

`s1(C)+s2(C) > tau/2`.                                           (3.1)

Consequently one of the following holds:

1. **two-channel cut:** `s2(C)>=tau/16` and therefore
   `s1(C)s2(C) > 7 tau^2/256`;
2. **one-side diffuse near-rank-one cut:** `s2(C)<tau/16`, `s1(C)>7tau/16`, and at least one top singular vector has maximum squared coordinate at most 1/2;
3. **localized physical coefficient:** `s2(C)<tau/16`, `s1(C)>7tau/16`, both top singular vectors have a coordinate of squared magnitude >1/2, and some physical cross coefficient obeys
   `|H_ij|>5tau/32`.

### Proof

Choose independent signs epsilon_i in {+1,-1}, D_epsilon=diag(epsilon), and

`M_epsilon=(H-D_epsilon H D_epsilon)/2`.

Because H has zero diagonal, `E D_epsilon H D_epsilon=0`, so `E M_epsilon=H/2`. For the cut I={epsilon=+1}, J={epsilon=-1}, M has block form

`[[0,C],[C^T,0]]`,

and therefore its Ky-Fan 4-norm is

`||M||_(4)=2(s1(C)+s2(C))`.

Convexity of the Ky-Fan norm yields

`(1/2)||H||_(4) <= E ||M||_(4)`,

so some cut satisfies

`s1(C)+s2(C) >= ||H||_(4)/4`.

Since s1(H)>=s2(H)>tau, `||H||_(4)>2tau`, proving (3.1).

If s2(C)>=tau/16, then (3.1) gives s1(C)>7tau/16, proving item 1. Otherwise write `C=s1 u v^T+E` with `||E||=s2(C)<tau/16`. If one of u,v has max squared coordinate <=1/2, item 2 holds. Otherwise choose i,j with `|u_i|,|v_j|>1/sqrt(2)`. Then

`|C_ij| >= s1 |u_i v_j|-||E|| > (1/2)(7tau/16)-tau/16 =5tau/32`,

which is item 3. QED.

For the live threshold `tau=3/10`, the two-channel branch has

`s1(C)s2(C) >63/25600`,

so Theorem 2.1 gives the explicit concentration estimate

`P(Q in K) < 9.856 |K|^(1/2)`                                    (3.2)

for the original quadratic form written across that cut, irrespective of both within-side quadratic forms.

## 4. Applying the named partner: high-Schur-offdiagonal opposite-pivot branch closes

Consider the exact account03/B19 opposite-sign physical pivot setting. The physical 2x2 pivot has diagonal magnitudes at least m>0 and determinant parameter Delta>0. After physical square completion, its Schur critical value is

`kappa(Z)=Z^T S Z`,

and the named partner supplies the conditional quarter-kernel

`h_z(t)<=K0 |t-kappa(z)|^(-1/4)`,
`K0=2 Delta^(-1/4)m^(-1/4)`,

together with the Hölder splice: any concentration exponent alpha>1/4 for kappa gives a bounded density for the parent Q.

Put O=S-diag(S). If `s2(O)>tau`, Lemma 3.1 gives a cut C with `s1(C)+s2(C)>tau/2`.

* In the two-channel branch, Theorem 2.1 gives alpha=1/2 directly for kappa, hence the partner splice closes the parent density. With the explicit L from (2.1), the bound is `K0(1+L)` because `4alpha-1=1`.
* In either near-rank-one branch, `s1(C)>7tau/16`. The named partner's proved Section 5 theorem `QFORM-SCHUR-CROSS-LOWRIDGE-STABILITY-v1` applies with `sigma=7tau/16`: a diffuse top singular vector is paid by q=1 ridge-Hölder, while double localization forces a physical mixed coefficient and the partner's 3/8 small-ball lemma. Both exponents exceed 1/4, so the same quarter-kernel splice closes.

Therefore:

### Corollary 4.1 — `QFORM-HIGH-SCHUR-OFFDIAG-PAID-v1`

In the account03/B19 opposite-sign physical-pivot regime, for every fixed `m,Delta,tau>0`,

`m_pivot>=m`, `Delta_pivot>=Delta`, and `s2(S-diag S)>tau`

imply a finite essential-density bound depending only on `(m,Delta,tau)`, uniformly over dimension and all independent cap-one input laws.

This is a genuine application of the named partner result: the new random-cut and half-Hölder estimates turn a global second-singular resource of the Schur critical form into one of the partner's already-paid cross-bank mechanisms.

## 5. Exact target-class adversary against a stronger two-channel selector

A tempting strengthening of Lemma 3.1 would be: `s2(H)>tau` forces a cut with `s2(C)>=c tau` for one universal c>0. This is false even inside the exact owner target.

Take

`A = [[0,1,1,1],
      [1,2,0,0],
      [1,0,2,0],
      [1,0,0,2]]`,

and H=A-diag(A). Then H is the three-leaf star

`H=[[0,v^T],[v,0_3]]`, `v=(1,1,1)`.

Its nonzero singular values are exactly `sqrt(3),sqrt(3)`, while every coordinate cut cross block has rank one: whichever side contains the center, all cross edges occupy only the center row or the center column. Hence `s2(C)=0` for every cut.

The matrix A itself is target-valid. The two-dimensional leaf-orthogonal subspace has eigenvalue 2, and the remaining center/leaf-sum block is `[[0,sqrt(3)],[sqrt(3),2]]`, whose eigenvalues are 3 and -1. Thus

`spectrum(A)={3,2,2,-1}`.

This is not a QFORM counterexample; indeed it is already easy by its same-sign physical diagonals. It is a source-valid counterexample to the stronger proposed structural implication that high `s2(H)` alone forces a rank-two cross cut. Therefore the near-rank-one diffuse/localized mechanisms in Lemma 3.1 and in the named partner theorem are genuinely necessary.

## 6. Conditional end-to-end proof and first unpaid implication

The strongest current conditional proof is now:

1. the spectral-window diffuse branch is paid by the source-complete ridge theorem;
2. the account01/B19 theorem pays every target form with `s2(A-diag A)<=3/10` (<66);
3. exact-rank-three nonzero physical-pivot residual orientation is paid by the orientation-free rank-two affine half-Riesz theorem;
4. opposite-sign quantitative physical pivots whose Schur critical form has `s2(S-diag S)>tau` are paid by Corollary 4.1;
5. the named partner already pays every fixed-first-singular Schur cross bank, including its near-rank-one diffuse/localized subcases.

Thus the first unpaid target-level implication is structural:

`QFORM-HIGH-OFFDIAG-PIVOT-OR-GROUPED-EXTRACTION-v2`.

Exact quantifiers: prove that there exist universal positive constants `m0,Delta0,tau0` and a finite list of already-paid grouped-coordinate/ridge alternatives such that every real symmetric A satisfying the owner target, failing the spectral-window diffuse branch and satisfying `s2(A-diag A)>3/10`, either

(a) has an opposite-sign original-coordinate physical 2x2 pivot with `m_pivot>=m0`, `Delta_pivot>=Delta0` whose exact Schur complement S satisfies `s2(S-diag S)>tau0`; or

(b) falls into one of the already-proved majority-pivot, same-sign definite, exact-rank-three nonzero-pivot, ridge, weighted-affine-fiber, or grouped-bank mechanisms with universal parameters.

The star example proves that (a) cannot be replaced by a universal rank-two cross-cut conclusion on the original H. Any complete structural reduction must retain the one-channel grouped-bank/localized branch and arbitrary additional spectrum.

No full-proof claim is made.