# account02/B11 — indefinite residual-shear collar

Status: **new scoped theorems / full QFORM OPEN**.  The statements below use arbitrary independent real inputs with densities at most one.  No moment, support, log-concavity, identical-law, post-rotation-independence, or small-random-perturbation assumption is used.  Essential boundedness is the main conclusion; continuity is asserted only in the second theorem where the source theorem supplies an L1 Fourier proof.

## 1. First unpaid implication and what is paid here

The latest completed designated partner account03/B11 r39 closes the exact-graph null-ruling endpoint by retaining an exact rank-two crossing and using the internal bilinear curvature `2 z d^T u` as a dyadic frequency sweep.  Its next gap is the punctured double-graph collar, where a tiny third cross singular direction appears and one must not divide by that singular value.

This report proves two exact collar statements.

1. A **rank-two logarithmic saddle + genuine square** remains uniformly bounded after an arbitrarily large or small coupling of that square to an independent fourth source coordinate.  At zero coupling this is an exact rank-three `(+,+,-)` or `(+,-,-)` form.  This gives an explicit sign-specific one-sheet/two-sheet splice.
2. The partner r39 internal-bilinear theorem is **exactly invariant under a residual coupling `2 kappa z W` whenever `W` comes from a source bank disjoint from both active banks**.  The bound does not depend on `kappa`, so the tiny third cross singular scale is not inverted.  The remaining obstruction is therefore sharply localized to the case in which the residual scalar is another projection of the same active bank and is dependent on the active two-plane.

## 2. Uniform independent-square collar

### Theorem `QFORM-INDEFINITE-SQUARE-INDEPENDENT-SHEAR-v1`

Let `X1,X2,Z,W` be independent with densities at most one.  For real `a,b,kappa` with

`|a| >= 1`, `|b| >= 1`,

put

`Q = 2 a X1 X2 + b Z^2 + 2 kappa Z W`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 8 * 2^(1/4) * |a|^(-3/4) * |b|^(-1/4) <= 8*2^(1/4) = 9.5136569201... .`  (2.1)

The estimate is **uniform in kappa**.

#### Proof

Condition on the original independent coordinate `W=w`.  The identity

`b Z^2 + 2 kappa w Z = b (Z + kappa w/b)^2 - kappa^2 w^2/b`  (2.2)

is exact.  Constants do not affect concentration.  For every real `s` and `rho>0`, the preimage under `z -> b(z+c)^2` of `[s-rho,s+rho]` has total Lebesgue length at most

`2 sqrt(2 rho/|b|)`.

Indeed, after dividing by `|b|`, if the squared interval meets zero its preimage length is at most `2 sqrt(2 rho/|b|)`; if it lies strictly above zero, concavity of the square root gives the same maximum at the endpoint touching zero.  Since the density of `Z` is at most one,

`sup_s P(|b(Z+c)^2-s| <= rho) <= H_b sqrt(rho),`
`H_b = 2 sqrt(2/|b|)`.  (2.3)

Now apply the **completed indefinite physical-pair theorem** recorded in the required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, Section 7.  For the physical pair `(X1,X2)` its quadratic block is

`B = [[0,a],[a,0]],`

so `|det B|=a^2` and `sigma_min(B)=|a|`.  The theorem gives, uniformly in the conditioned value `w`,

`||p_{Q | W=w}||_infinity`
` <= 4 sqrt(2 H_b) (|det B| sigma_min(B))^(-1/4)`
` = 8*2^(1/4) |a|^(-3/4)|b|^(-1/4)`.  (2.4)

A mixture of conditional densities with a common essential cap has the same cap, proving (2.1).  No conditional density of a rotated statistic is invoked: the only conditioning is on the genuinely independent original coordinate `W`.

### Target validity and exact signature endpoint

The physical coefficient matrix is block diagonal,

`A_kappa = [[0,a],[a,0]] direct_sum [[b,kappa],[kappa,0]].`

Its eigenvalues are

`+|a|, -|a|, (b+sqrt(b^2+4kappa^2))/2, (b-sqrt(b^2+4kappa^2))/2`.  (2.5)

One of the last two has sign `sign(b)` and magnitude

`(|b|+sqrt(b^2+4kappa^2))/2 >= |b| >= 1`.

Hence every `A_kappa` is in the full QFORM target: it has at least three eigenvalues of modulus at least one.  At `kappa=0` its rank is exactly three.  If `b>0` the nonzero signature is `(+,+,-)`; if `b<0` it is `(+,-,-)`.

### Sign-specific ruled splice at the exact-rank-three endpoint

At `kappa=0`, the required pinned source's proved ruled theorem (COUNTEREXAMPLE_SEARCH.md, Theorem C) applies to the exact rank-three spectral form.  It gives

`p_Q(s) <= pi sqrt(2)` whenever `b*s >= 0`.  (2.6)

For `b>0` this is the `s>=0` one-sheet side of the `(+,+,-)` form.  For `b<0`, apply Theorem C to `-Q`; this is the `s<=0` one-sheet side of the `(+,-,-)` form.  I do **not** extend (2.6) to the opposite side by X-ray control: the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids that inference.  The opposite two-sheet side is instead paid by the global physical-pair estimate (2.1).

### The logarithmic endpoint is retained, not hidden

For centered unit uniforms and `kappa=b=0`,

`p_{2a X1 X2}(t) = |a|^(-1) log(|a|/(2|t|)),`
`0<|t|<|a|/2`,  (2.7)

so the rank-two opposite-sign saddle is genuinely unbounded.  The third direction `b Z^2` removes this logarithm because its conditional small-ball law has the square-root exponent (2.3), exactly the hypothesis absorbed by the pair-log theorem.  The additional term `2 kappa ZW` does not count as a perturbation and is never deleted: exact completion (2.2) shows that, after conditioning on the independent `W`, it only translates the square.  This is why the bound remains uniform as `kappa -> 0` (and in fact for all `kappa`).

This does not conflict with `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`: here the genuine square coefficient `b` is bounded away from zero; the quantity allowed to vanish is the cross-shear `kappa`.

## 3. Partner r39 survives an independent residual cross direction

Read and apply the completed designated partner theorem

`QFORM-RANK2-CROSS-INTERNAL-BILINEAR-DYADIC-v1`

from `account03/B11` r39, canonical report commit `b53315b2f91c6a917f8c5c17f3a5dba07904374b`.

### Theorem `QFORM-R39-INDEPENDENT-RESIDUAL-SHEAR-v1`

Assume the exact hypotheses and notation of partner r39:

`Q0 = F(u) + 2 z d^T u + 2 u^T S v + G(Y)`,

where the first source bank `X` and second source bank `Y` are independent, `(u,z)` has caps `M3,M2,M1`, `v` has cap `MY`, `S=diag(sigma1,sigma2)>0`, and `D=|d|>0`.  Let `W` be **any random variable independent of both source banks** (it need not itself have a density), and let `H` be any measurable real function.  Then for every real `kappa`,

`Q = Q0 + 2 kappa z W + H(W)`  (3.1)

has a bounded continuous density with exactly the r39 bound

`||p_Q||_infinity <= M1/(pi D)`
` + sqrt(MY)/sqrt(sigma1 sigma2) * S(M2,M3)`,  (3.2)

where

`S(M2,M3)=sum_{j>=0} 2^(-j/2) sqrt(2 M2 + pi M3(1+2j log 2)).`

In particular the right side is independent of `kappa` and of the law of `W`.

#### Proof

Condition on `W=w`.  Equation (3.1) becomes the partner r39 form plus the affine `z` term `2 eta z` with `eta=kappa w`, and an irrelevant constant `H(w)`.  Partner r39 explicitly proves that its estimate permits an arbitrary affine `z` term: replacing `d^T u` by `d^T u+eta` only translates the scalar coordinate in the dyadic calculation.  Since `W` is independent of both active source banks, all r39 projection caps and the independence of `X` and `Y` are unchanged after conditioning.  Thus every conditional law obeys the same bound (3.2).

For continuity, r39's proof gives an `L1(dt)` characteristic-function estimate whose integral is uniform in `eta`.  Therefore

`int |phi_Q(t)| dt <= E_W int |phi_{Q|W}(t)| dt < infinity`

by Tonelli and the triangle inequality.  Fourier inversion gives a bounded continuous density.  No conditional cap of a dependent projection is used.

### A target-valid collar family with no tiny-singular-value loss

Take six independent original cap-one coordinates `(X1,X2,Z,Y1,Y2,W)` and

`Q_kappa = 2 Z X1 + 2 X1 Y1 + 2 X2 Y2 + 2 kappa Z W`.  (3.3)

In (3.2), `D=sigma1=sigma2=1` and all four projection caps equal one.  Hence

`||p_{Q_kappa}||_infinity <= C_*`
`:= 1/pi + sum_{j>=0} 2^(-j/2) sqrt(2 + pi(1+2j log2)) < 13`,  (3.4)

uniformly in `kappa`; the density is continuous.  A rigorous 30-term-plus-tail check is in `VERIFY.py`.

The coefficient graph splits into the pair `X2--Y2` of weight one and the weighted path `Y1--X1--Z--W` with edge weights `1,1,kappa`.  Consequently the spectrum is

`{+1,-1,+s_+(kappa),-s_+(kappa),+s_-(kappa),-s_-(kappa)}`,  (3.5)

where

`s_+^2 = (2+kappa^2 + sqrt(4+kappa^4))/2`,
`s_-^2 = (2+kappa^2 - sqrt(4+kappa^4))/2`.

Since `s_+>=sqrt(2)`, (3.3) is a genuine QFORM-target family for every `kappa`.  At `kappa=0`, `s_-=0`; as `kappa->0`, the new cross singular scale tends to zero, but (3.4) does not divide by it.  This is a concrete punctured-collar success.

## 4. Precisely what remains unpaid

The general partner r39 punctured double-graph collar is harder for one specific reason.  Its residual scalar is typically another projection `W` of the **same** second product bank that already generates the active plane `v`.  Then conditioning on `W` can make the conditional density of `v` arbitrarily large; bounded joint projection density is not a replacement for independence.  The existing `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` and related two-planar corrections are exactly relevant here.

Therefore Theorem 3 does not close the general collar.  It shows that the tiny third singular value itself is **not** the analytic enemy: it is harmless whenever its right-null scalar has genuine source-disjoint provenance.  The first unpaid implication is now

`QFORM-R39-SAMEBANK-RESIDUAL-SHEAR-v1`:

> Prove an unconditional version of the r39 dyadic estimate for
> `2 z d^T u + 2 u^T S v + 2 kappa z W`
> when `(v,W)` is one three-dimensional orthogonal projection of a single cap-one product bank, with a bound uniform as `kappa->0`; or force an original-coordinate cut that places the residual scalar on a disjoint source bank and invokes Theorem 3.

A valid proof must use the product-frame/X-ray provenance of the full `(v,W)` projection and may not condition on `W`, replace it by an arbitrary joint-density cap, or delete `kappa zW` as a small quadratic perturbation.  The fresh one-hub transverse-compression lemma has the same analytic edge: its exact-rank-three null-hub normal form leaves a transverse leakage inside the same leaf bank.  The independent-shear theorem here pays the source-disjoint version of that leakage but not the dependent one.

Arbitrary additional nonseparable spectrum remains a separate full-QFORM bridge.  Full QFORM is not proved or disproved by this report.
