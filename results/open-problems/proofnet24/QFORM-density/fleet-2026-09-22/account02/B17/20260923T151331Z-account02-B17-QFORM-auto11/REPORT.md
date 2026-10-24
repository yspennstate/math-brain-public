SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T15:13:31Z.
attacking: unequal opposite rank-one cube banks with an arbitrary cap-one heavy coordinate; close the entire finite majority-heavy separated-bank family globally below 3sqrt(2).

# QFORM-UNEQUAL-BANK-GLOBAL-BARRIER-v1

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **SUPPORTING ANALYTIC THEOREM / SOURCE-VALID WITNESS CLASS CLOSED / FULL QFORM OPEN**.

The full owner target remains **OPEN / NOT PROVED / NOT DISPROVED**. No continuity statement for the full target is made here. All density bounds below are essential-density statements; no moment, bounded-support, log-concavity, iid, diagonal-basis reduction, or post-rotation independence is assumed for the owner target. The only log-concavity used below is a proved property of the deliberately chosen uniform-cube bank witnesses.

## 0. First unpaid implication after this run

The separated majority-heavy rank-three witness class is now paid even when the two opposite rank-one banks have unequal dimensions and completely different leverage profiles. A sharp witness above `3sqrt(2)` must leave this class. The nearest unpaid B17 target is therefore a genuinely coupled shared-coordinate family, especially the designated partner's N3 interior

`-a X^2 + 2 sqrt(1-a^2) X B + a B^2 + C^2`, `0<a<1`,

where the cross term prevents the signwise separated-bank argument below. An off-tip peak in that class above `3sqrt(2)` would refute the candidate sharp constant, but not the existence of a larger universal QFORM constant.

## 1. Exact source-valid family and theorem

Let `m,n>=1`, let `a in R^m`, `b in R^n` satisfy

`||a||_2=||b||_2=1`,

and let `alpha,lambda,mu>=1`. Put

`S_a=sum_j a_j U_j`,  `T_b=sum_k b_k V_k`,

where all `U_j,V_k` are independent `Unif[-1/2,1/2]`. Let `X` be an independent arbitrary real random variable with probability density `0<=f<=1`.

The physical matrix

`A=diag(alpha, lambda a a^T, -mu b b^T)`

has exact nonzero spectrum

`{alpha, lambda, -mu}`.

Indeed `aa^T` and `bb^T` are rank-one projections because `||a||=||b||=1`. Thus every finite member has three eigenvalues of magnitude at least one, exactly as required by the owner target. The physical coordinates are independent before applying `A`; no spectral rotation is used to assert independence.

Define

`Q=alpha X^2 + lambda S_a^2 - mu T_b^2`.

### Theorem

For every such finite source-valid witness,

`||p_Q||_infinity <= K_*`,

where

`K_* = (pi/2)(sqrt(2)+2^(1/4)) = 4.089443637123813... < 3sqrt(2)`.

Hence unequal dimensions, unequal bank leverage profiles, arbitrary translations/fragments/unbounded support of the heavy cap-one law, and arbitrary eigenvalue magnitudes `alpha,lambda,mu>=1` cannot produce the known `3sqrt(2)` obstruction in this separated majority-heavy architecture.

Multiplying the whole quadratic form by `-1` gives the corresponding sign-reversed statement. The theorem does **not** cover a cap-one heavy variable placed on the minority-sign axis with two same-sign diffuse banks; that is a complementary geometry treated separately by the partner programme.

## 2. Normalize the three scalar coordinates without rotating them

Set

`F=sqrt(alpha) X`, `H_+=sqrt(lambda) S_a`, `H_-=sqrt(mu) T_b`.

These are still independent because only coordinatewise scalar rescaling was used. Let their densities be `g,h_+,h_-`.

Because `alpha>=1`,

`0<=g<=alpha^(-1/2)<=1`.

Each unscaled bank density is an even log-concave convolution of centered interval densities, hence is even and nonincreasing on `[0,infinity)`. Scaling preserves that property. The next section proves the quantitative bank bounds

`||h_+||_infinity, ||h_-||_infinity <= sqrt(2)`,

`||h_+||_2^2, ||h_-||_2^2 <= 1`.

The scaling by `sqrt(lambda)` and `sqrt(mu)` can only improve these inequalities.

Thus it is enough to prove a purely one-dimensional analytic lemma for

`Q=F^2+H_+^2-H_-^2`

under exactly those density properties.

## 3. Ball/Rogozin currency: both Linfinity and L2

The completed pinned source at commit `e5f71d79eff325201dd0274053d20268ce65b837` uses Rogozin/Ball cube slicing as the sharp one-dimensional projection input. Applied to the actual cube bank `S_a`, it gives

`||h_a||_infinity <= sqrt(2)`.

There is a second useful consequence that is crucial here. Let `S_a'` be an independent copy and define

`Z=(S_a-S_a')/sqrt(2)`.

The `2m`-coordinate coefficient vector `(a,-a)/sqrt(2)` has Euclidean norm one, so the same cube-slicing theorem gives

`p_Z(0)<=sqrt(2)`.

But scaling and convolution give exactly

`p_Z(0)=sqrt(2) p_{S_a-S_a'}(0)=sqrt(2) int_R h_a(t)^2 dt`.

Therefore

`||h_a||_2^2<=1`.

The same argument applies to `b`. After scaling by `sqrt(lambda)` or `sqrt(mu)`,

`||h_+||_infinity <= sqrt(2)/sqrt(lambda) <= sqrt(2)`,
`||h_+||_2^2 <= 1/sqrt(lambda) <=1`,

and similarly for `h_-`.

This is an actual use of the completed source theorem on the present witness family, not a formal citation.

## 4. A common angular integral

For `0<=u<=1` define

`J(u)=int_0^infinity h_-(r) h_+(u r) dr`.

Two bounds are available simultaneously.

First, probability normalization and the Linfinity bank bound give

`J(u) <= ||h_+||_infinity int_0^infinity h_-(r)dr <= sqrt(2)/2`.

Second, Cauchy-Schwarz and evenness give, for `u>0`,

`J(u)
 <= (int_0^infinity h_-(r)^2dr)^(1/2)
    (int_0^infinity h_+(ur)^2dr)^(1/2)
 <= (1/2)^(1/2) (1/(2u))^(1/2)
 = 1/(2 sqrt(u)).`

The following elementary angular majorant will occur on both signs of the output:

`4 int_0^1 J(u)/sqrt(1-u^2) du`.

Split at `u=1/sqrt(2)`. On the first piece use `J<=sqrt(2)/2`; on the second use

`J(u)<=1/(2sqrt(u))<=2^(1/4)/2`.

Since `arcsin(1/sqrt(2))=pi/4`,

`4 int_0^1 J(u)/sqrt(1-u^2)du
 <= pi/sqrt(2) + pi 2^(1/4)/2
 = (pi/2)(sqrt(2)+2^(1/4))
 = K_*.`

The choice `1/sqrt(2)` is intentionally elementary, not optimized.

## 5. Positive output: direct polar domination

Let `s>=0`. Use polar coordinates in the two positive variables `(F,H_+)`. For each fixed `z=H_-`, the radius forced by

`F^2+H_+^2=s+z^2`

is

`R=sqrt(s+z^2)`.

The standard radial Jacobian gives the density representative

`p_Q(s)
 = (1/2) int_R h_-(z)
     int_0^{2pi} g(R cos(theta)) h_+(R sin(theta)) dtheta dz.`

No continuity is used. Since `g<=1`, and because `R>=|z|` while `h_+` is even decreasing on the positive half-line,

`h_+(R sin(theta)) <= h_+(z sin(theta))`

after taking absolute values in the even density. Hence

`p_Q(s)
 <= (1/2) int_R h_-(z) int_0^{2pi} h_+(z sin(theta)) dtheta dz`.

Evenness in `z` and fourfold angular symmetry now give exactly

`p_Q(s) <= 4 int_0^1 J(u)/sqrt(1-u^2)du <= K_*.`

Thus **every nonnegative output level** is already below `3sqrt(2)`, uniformly over the arbitrary heavy cap-one law.

This sharpens the pinned source's general rank-three one-sheet theorem on this structured family. The source theorem independently gives `p_Q(s)<=pi sqrt(2)` for `s>=0`; here the cube-bank Linfinity/L2 currency lowers the same side to `K_*`.

## 6. Negative output: exact one-dimensional bathtub reduction

Let

`W=H_+^2-H_-^2`

and denote its density by `k`. For `x>=0` define the square densities

`q_+(x)=h_+(sqrt(x))/sqrt(x)`,
`q_-(x)=h_-(sqrt(x))/sqrt(x)`.

Both are nonincreasing on `(0,infinity)` because the corresponding `h` is nonincreasing.

For `v>=0`, direct convolution of the two squares gives

`k(-v)=int_0^infinity q_+(u) q_-(u+v) du`.

Therefore `v -> k(-v)` is nonincreasing. If `s<=0`, then

`p_Q(s)=int_R g(x) k(s-x^2) dx`,

and the kernel `x -> k(s-x^2)` is even and nonincreasing in `|x|`. Under `0<=g<=1` and `int g=1`, the one-dimensional bathtub principle gives

`p_Q(s)
 <= int_{-1/2}^{1/2} k(s-x^2) dx
 <= int_{-1/2}^{1/2} k(-x^2) dx
 =: C_-`.

This step is valid for arbitrary fragmented, translated or unbounded-support heavy laws; no interval assumption is imposed on the original heavy law. The centered interval appears only as the optimizer of the cap-one linear functional.

Now expand the last integral. The square-density substitution gives

`k(-x^2)
 = int_R h_+(y) h_-(sqrt(x^2+y^2))/sqrt(x^2+y^2) dy`.

Hence

`C_-
 = int_{|x|<=1/2} int_R
   h_+(y) h_-(sqrt(x^2+y^2))/sqrt(x^2+y^2) dy dx`.

Enlarge the `x`-strip to the whole plane. In polar coordinates the radial Jacobian cancels the denominator, giving

`C_- <= 4 int_0^1 J(u)/sqrt(1-u^2)du <= K_*`.

Thus **every nonpositive output level** is also below `K_*`.

The negative side is exactly where the generic X-ray-only shortcut is known to fail without product provenance. Here the conclusion is paid by the special source-valid bank structure, the cap-one bathtub step, and the Ball/Rogozin bank norms; no generic arbitrary-joint coarea assertion is being used.

## 7. Strict comparison with the Gaussian obstruction

The comparison is analytic. Divide by `sqrt(2)`:

`K_*/sqrt(2)=(pi/2)(1+2^(-1/4)).`

Use the classical `pi<22/7` and the elementary

`2^(-1/4)<10/11`,

whose fourth-power certificate is `14641<20000`. Then

`K_*/sqrt(2)
 < (11/7)(1+10/11)
 =3`.

Therefore

`K_*<3sqrt(2)`.

Numerically only as a diagnostic,

`K_*=4.089443637123813...`,
`3sqrt(2)-K_*=0.153197049995472...`.

## 8. What the pinned source does and does not settle

For the same physical exact-spectrum family, the completed `COUNTEREXAMPLE_SEARCH` Theorem C at the pinned commit applies to the positive one-sheet side and yields

`p_Q(s)<=pi sqrt(2)=4.442882938...`, `s>=0`.

That is a real finite-source inequality but its constant lies above the candidate `3sqrt(2)`. Failure of `pi sqrt(2)` to certify sharpness is therefore a proof-constant limitation, not a QFORM counterexample. The present theorem uses extra source-valid bank structure to replace that constant by `K_*<3sqrt(2)` and separately pays the negative two-sheet side.

No conclusion here upgrades the pinned source's open arbitrary-product two-sheet problem to the full QFORM theorem.

## 9. Latest designated partner consumed

The fresh `account03/B17` handoff `20260923T150436Z-account03-B17-QFORM-auto11` proves an exact cone-tip optimizer for the genuinely coupled N3 one-heavy Gaussianized family

`Q_a=-aX^2+2sqrt(1-a^2)XB+aB^2+C^2`, `0<a<=1`,

with exact physical finite approximants having spectrum `{1,1,-1}`. Its cross term makes it genuinely outside the separated block class of the present theorem when `0<a<1`. At the minority-heavy endpoint `a=1`, it proves the strict cone-tip ceiling

`sqrt(6pi) erf(sqrt(3/2)) < 97/24 < 3sqrt(2)`

and a negative first finite-bank correction.

Taken together, the two results remove both of the easiest rank-three one-heavy escape routes:

1. arbitrary finite **majority-heavy separated** unequal rank-one banks are globally bounded by `K_*<3sqrt(2)` (this run);
2. the partner's **minority-heavy coupled N3 endpoint** is already strictly subcritical at the exact cap-one cone-tip optimum and approaches that endpoint from below.

The remaining N3 interior cross-term geometry is therefore a genuinely different unpaid mechanism, rather than a hidden unequal-bank variant of the present class.

## 10. Scope and correction discipline

This theorem is source-valid at every finite dimension. It does not assume independence after diagonalizing `A`: independence is used only in the displayed original block coordinates, where the inputs were constructed independently. It does not use any hidden moment or support bound on the arbitrary heavy law. It does not use the corrected-false arbitrary-joint coarea or X-ray-only two-sheet principles. It makes no full-target continuity claim.

A future example in another class with density peak above `3sqrt(2)` would refute the proposed sharp constant only. It would not, by itself, refute the existence of some larger universal density bound required by the owner-level QFORM question.

### Verdict

`QFORM-UNEQUAL-BANK-GLOBAL-BARRIER-v1`: **PROVED for the stated source-valid class.**

Full arbitrary-product QFORM: **OPEN / NOT PROVED / NOT DISPROVED.**
