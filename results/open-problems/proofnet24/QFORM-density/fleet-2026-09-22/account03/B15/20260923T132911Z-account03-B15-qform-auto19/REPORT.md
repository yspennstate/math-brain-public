SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T13:29:11Z.
attacking: lock every exact one-scale height/window formulation to an actual output-density maximizer, using the completed target-wide fixed-instance C0 theorem and the account04/B15 heat-height identity.

# account03/B15 auto19 — peak-locked one-scale normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account03/B15`  
**Run:** `20260923T132911Z-account03-B15-qform-auto19`  
**Status:** `ESSENTIAL_STEP_APPLIED / PEAK_LOCKED_ONE_SCALE_NORMAL_FORM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and dependencies

The owner target remains the universal estimate for `Q=X^T A X` under independent cap-one marginals and at least three eigenvalues of `A` of modulus at least one. No universal bound is proved in this report.

Two completed fixed-instance regularity inputs are used at their exact scopes.

1. `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`, proves that for every fixed symmetric `A` with `rank(A)>=3` and every cap-one product input law, the output has an instance-dependent bounded density `p_Q in C_0(R)`. Its zero-diagonal proof is combined there with the completed nonzero-physical-diagonal theorem from this slot at `d73760eb784a86c356c64f05dd92f84655618f02`.

2. The designated partner `account04/B15`, `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`, proves for every probability law `mu`

   `sup_(epsilon>0,y) (mu*gamma_epsilon)(y)=||p_mu||_infinity`,

   with `+infinity` when no bounded density exists; if `p_mu in C_0`, Gaussian smoothing converges uniformly to `p_mu`.

No uniform modulus of continuity is assumed. Earlier source-valid phase-aligned examples show that no such target-uniform modulus exists even for fixed `A=I_3` and smooth cap-one inputs.

## 2. Homogeneous optimal constant

For a rank-at-least-three symmetric matrix let `s_3(A)>0` be its third singular value and write

`M(A,f):=||p_(X^T A X)||_infinity`.

Define the homogeneous constant

`C_* := sup_(rank(A)>=3, cap-one product f) s_3(A) M(A,f)`.

Let

`C_tar := sup_(s_3(A)>=1, cap-one product f) M(A,f)`

be the optimal constant in the owner's normalized class. Then

`C_*=C_tar`

in the extended sense.

Indeed, if `s=s_3(A)>0`, put `B=A/s`. Since `Q_B=Q_A/s`,

`M(B,f)=s M(A,f)`

and `s_3(B)=1`. Thus `s M(A,f)<=C_tar`, proving `C_*<=C_tar`. Conversely if `s_3(A)>=1`, then `M(A,f)<=s_3(A)M(A,f)<=C_*`, so `C_tar<=C_*`.

This scalar normalization changes only the quadratic matrix and never rotates the independent input coordinates.

## 3. Peak-locked fixed-kernel theorem

Because the completed fixed-instance theorem gives `p_Q in C_0(R)`, every target instance has at least one global maximizer. Fix **any**

`y_*=y_*(A,f) in argmax_y p_Q(y)`

and let `M=p_Q(y_*)`.

### Theorem

For every bounded nonnegative probability density `K` on `R`,

`boxed[ C_* = sup_(rank(A)>=3,f) s_3(A) E K(Q-y_*) ].`

The choice of maximizer may be arbitrary for each instance.

### Proof: upper bound

Since `K>=0` and `int K=1`,

`E K(Q-y_*) = int K(z-y_*) p_Q(z) dz <= M int K = M`.

Hence

`s_3(A) E K(Q-y_*) <= s_3(A) M <= C_*`.

Taking the supremum proves the `<=` direction.

### Proof: lower bound

Fix one instance `(A,f)`, let `s=s_3(A)`, and fix a global maximizer `y_*`. For `lambda>0`, set

`A_lambda=lambda A`, `Q_lambda=lambda Q`, `s_3(A_lambda)=lambda s`, `y_lambda=lambda y_*`.

The scaled density is

`p_lambda(u)=lambda^(-1) p_Q(u/lambda)`,

so `y_lambda` is again a global maximizer. Therefore

`lambda s E K(Q_lambda-y_lambda)
 = s int lambda K(lambda(z-y_*)) p_Q(z) dz`.

Put `epsilon=1/lambda` and `K_epsilon(u)=epsilon^(-1)K(u/epsilon)`. Then the right-hand side is

`s int K_epsilon(z-y_*)p_Q(z)dz`.

The family `K_epsilon` is an approximate identity. Since `p_Q` is continuous at the chosen maximizer,

`int K_epsilon(z-y_*)p_Q(z)dz -> p_Q(y_*)=M`

as `epsilon downarrow0`. Hence the supremum over scaled target instances is at least `sM`. Taking the supremum over the original instance gives the reverse inequality and proves the theorem.

The argument uses only pointwise continuity at the selected peak. It does not require a law-uniform continuity, Holder, Sobolev, BV, or translation modulus.

## 4. Designated partner applied to an actual equality: Gaussian mode form

Take `K=gamma_1`. The completed account04/B15 theorem gives for each fixed instance

`E gamma_1(Q-y_*) <= sup_(epsilon,y) E gamma_epsilon(Q-y)=M`.

More importantly, because `p_Q in C_0`, the partner's uniform Gaussian approximation gives

`E gamma_epsilon(Q-y_*) -> M` as `epsilon downarrow0`.

Under the scalar matrix scaling `A_lambda=lambda A`,

`lambda E gamma_1(lambda(Q-y_*)) = E gamma_(1/lambda)(Q-y_*)`.

Therefore the partner theorem is applied directly to yield the exact peak-locked Gaussian identity

`boxed[ C_* = sup_(rank(A)>=3,f) s_3(A) E gamma_1(Q-y_*) ].`

Thus the free center in the exact fixed-Gaussian normal form can be restricted, with zero constant loss, to a **true global mode of the unsmoothed output density**.

## 5. Peak-locked interval, tent, annulus and punctured forms

The theorem immediately gives several exact formulations that are stronger proof interfaces than an arbitrary-center one-scale test.

### Unit interval centered at a true density peak

For

`K_box(u)=1_{|u|<=1/2}`

(up to irrelevant endpoint convention),

`boxed[ C_* = sup_(A,f) s_3(A) P(|Q-y_*|<=1/2). ]`

Hence the full conjecture is equivalent to one fixed-radius small-ball estimate, but only at actual density maximizers. No arbitrary output center has to be paid.

### Positive tent centered at a true density peak

For `K_tent(u)=(1-|u|)_+`, which has integral one,

`boxed[ C_* = sup_(A,f) s_3(A) E(1-|Q-y_*|)_+. ]`

This retains the absolutely integrable sinc-squared Fourier multiplier while deleting the arbitrary-center supremum.

### Annular shell centered at a true density peak

For

`K_ann(u)=(1/2) 1_{1<|u|<2}`,

`boxed[ C_* = sup_(A,f) (s_3(A)/2) P(1<|Q-y_*|<2). ]`

This is a zero-loss **punctured** formulation: the tested shell excludes the entire unit neighborhood of the actual maximum point of the density. Earlier free-center obstructions showed that a puncture by itself is useless if the center may be translated arbitrarily. The present theorem removes that particular freedom. It does not yet prove the shell probability bound.

### Arbitrarily high-order positive puncture

For each integer `m>=1`, let

`kappa_m(u)=u^(2m) gamma_1(u)/(2m-1)!!`.

This is a nonnegative probability density vanishing to order `2m` at zero, so

`boxed[ C_* = sup_(A,f) s_3(A) E kappa_m(Q-y_*). ]`

Thus one may demand arbitrary physical-space cancellation exactly at a true density maximum while preserving positivity and the exact optimal universal constant.

## 6. What this does and does not pay

This result uses qualitative regularity to strengthen the proof interface, but it does **not** infer continuity from boundedness and does **not** infer the missing universal height from continuity. The implications remain separate:

- absolute continuity is qualitatively much weaker than bounded density;
- target-wide fixed-instance `C_0 cap L^infinity` is already source-proved with matrix-dependent constants;
- no target-uniform continuity/Besov/Sobolev/BV modulus is available;
- the universal quantifier reversal `sup_(A,f) s_3(A)||p_Q||_infinity<infinity` remains open.

The concrete new unpaid implication can now be stated without a free center. For example, it suffices and is necessary to prove

`sup_(A,f) s_3(A) P(|Q-y_*(A,f)|<=1/2) < infinity`,

or equivalently the annular shell estimate

`sup_(A,f) s_3(A) P(1<|Q-y_*|<2) < infinity`.

A promising next use is to insert the condition `y_* in argmax p_Q` into the minority/two-sheet or grouped-bank geometry before taking any fiber supremum or paying reciprocal tiny-minor costs. The prior heat-mode posterior constraint and this true-density-mode restriction are distinct: the present center is a mode of the unsmoothed `p_Q` itself.

## 7. Integrity ledger

- Full universal QFORM constant: **OPEN / NOT PROVED / NOT DISPROVED**.
- Target-wide absolute continuity: qualitatively proved by existing coarea arguments.
- Target-wide fixed-instance bounded `C_0` density: completed source `9b8bb7e...`, using `d73760e...` in the nonzero-diagonal branch.
- New contribution: exact peak-locked one-scale normal form for every bounded positive probability kernel, with no constant loss.
- Designated partner actually applied: account04/B15 heat-height theorem `ad7e5daa...` to the Gaussian equality above.
- No Gaussian-input, log-concavity, moment, compact-support, connected-support, post-rotation independence, pointwise van-der-Corput, arbitrary-joint coarea, conditional-density-moment, or naive fiber-sup premise is used.
- No public release or scheduler/task mutation is part of this mathematics.

**Next step:** exploit the actual-mode restriction in an original-coordinate product-preserving two-sheet/grouped-bank inequality; do not attempt to manufacture a uniform regularity modulus, which is already refuted.
