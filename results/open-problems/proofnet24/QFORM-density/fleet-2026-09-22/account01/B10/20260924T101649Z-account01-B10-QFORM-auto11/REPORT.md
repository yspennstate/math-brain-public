# account01/B10 — diffuse residual Wiener–Fresnel compiler at leverage 1/2

## Status

**PROVED SUPPORTING THEOREM / NEW LEVERAGE-1/2 EXACT-RANK3 CHAMBER / NEW ONE-HUB CONDITIONAL BRANCH / PARTNER ENDPOINT APPLIED / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN.**

Programme: `QFORM-DENSITY-3EIG-20260922`. Source control initially resolved at `yspennstate/math-research-brain@4e31ab7d46e8d7a01a90bc1c685d1c3f6c5187df`, OWNER CONTROL revision `2026-09-22.15`. This report preserves all live corrections: no pointwise law-uniform van-der-Corput decay; no post-rotation independence; no arbitrary-joint coarea lemma; no conditional-density-moment gate; no fiber-sup dimension-free shortcut.

The main new point is that **sharp Hausdorff–Young exactly cancels the small row-leverage entropy loss in geometric Brascamp–Lieb**. This gives a dimension-free Wiener norm for every 3D orthogonal product projection whose row leverages are at most `1/2`. The resulting Fresnel compiler proves a continuous bounded density with constant `3e |det M|^{-1/3}` for an arbitrary invertible rank-three quadratic form, including arbitrary affine terms.

This is a stronger diffuse exact-rank-three chamber than the previously recorded small-leverage branches. It does not bridge the punctured near-coloop limit where one physical row has leverage tending to one.

## 1. Setup and Fourier conventions

Let `U` be an `n x 3` real matrix with orthonormal columns,

`U^T U = I_3`.

Write its physical rows as `u_i in R^3`, and put

`c_i = ||u_i||_2^2`.

Then

`sum_i c_i = 3`,

and, after omitting zero rows and defining `theta_i=u_i/sqrt(c_i)`,

`sum_i c_i theta_i theta_i^T = I_3`.                         (1)

Let the original coordinates `X_i` be independent with probability densities `f_i` satisfying `0<=f_i<=1`. Set

`Y=U^T X in R^3`.

Use the Fourier convention

`hat f(xi)=int_R exp(i xi x) f(x) dx`.

The characteristic function of `Y` is

`chi(xi)=prod_i hat f_i(u_i dot xi)`.                         (2)

We will prove that if

`max_i c_i <= 1/2`,                                           (3)

then

`||chi||_{L^1(R^3)} <= (2 pi)^3 exp(3/2)`.                    (4)

This is the key dimension-free estimate.

## 2. Geometric Brascamp–Lieb plus sharp Hausdorff–Young

For every `i` with `c_i>0`, set

`q_i=1/c_i >=2`,

`p_i=q_i/(q_i-1)=1/(1-c_i) in [1,2]`.

Define the one-dimensional nonnegative function

`F_i(t)=|hat f_i(sqrt(c_i)t)|^(1/c_i)`.

By (1), the rank-one geometric Brascamp–Lieb inequality gives

`int_{R^3} prod_i F_i(theta_i dot xi)^(c_i) dxi
 <= prod_i (int_R F_i)^(c_i)`.                                (5)

The left side is exactly `||chi||_1`, because

`F_i(theta_i dot xi)^(c_i)=|hat f_i(u_i dot xi)|`.

For the right side,

`int_R F_i(t) dt
 = c_i^(-1/2) ||hat f_i||_{q_i}^{q_i}`,

hence

`||chi||_1
 <= prod_i c_i^(-c_i/2) ||hat f_i||_{q_i}`.                 (6)

Now use the sharp Babenko–Beckner Hausdorff–Young inequality for the above unnormalised Fourier convention:

`||hat f||_q
 <= (2 pi)^(1/q) [p^(1/p)/q^(1/q)]^(1/2) ||f||_p`,         (7)

where `1<=p<=2`, `q=p/(p-1)`.

With `q=q_i=1/c_i`, `p=p_i=1/(1-c_i)`, and `||f_i||_{p_i}<=1` because `0<=f_i<=1` and `int f_i=1`, (7) becomes

`||hat f_i||_{q_i}
 <= (2 pi)^(c_i)
    c_i^(c_i/2)
    (1-c_i)^(-(1-c_i)/2)`.                                   (8)

The factor `c_i^(c_i/2)` in (8) cancels the potentially dimension-losing `c_i^(-c_i/2)` in (6). Therefore

`||chi||_1
 <= (2 pi)^(sum c_i)
    prod_i (1-c_i)^(-(1-c_i)/2)`.                             (9)

Since `sum c_i=3` and, for `0<=c<=1/2`,

`(1-c) log(1/(1-c)) <= c`                                    (10)

(the inequality follows from `-log(1-c)<=c/(1-c)`), we get

`sum_i (1-c_i) log(1/(1-c_i)) <=3`.

Thus (9) yields the promised bound

`boxed: ||chi||_1 <= (2 pi)^3 e^(3/2).`                       (11)

Consequently the law of `Y` has a bounded continuous density obtained by Fourier inversion. More importantly, (11) provides the exact Wiener currency needed for a quadratic Fresnel integral.

External analytic inputs used here are classical and source-matched: W. Beckner, *Inequalities in Fourier Analysis*, Ann. of Math. 102 (1975), 159–182, DOI 10.2307/1970980 (sharp Hausdorff–Young); and the rank-one geometric Brascamp–Lieb inequality for data satisfying (1), whose geometric constant is one (Ball/Brascamp–Lieb formulation).

## 3. Wiener–Fresnel compiler for an arbitrary invertible 3 x 3 form

Let `M` be any invertible real symmetric `3 x 3` matrix and let `beta in R^3`, `gamma in R`. Put

`R = Y^T M Y + beta^T Y + gamma`.

Write

`D=|det M|`.

### Theorem

Under (3), `R` has a continuous density and

`boxed: ||p_R||_infinity <= 3 e D^(-1/3).`                    (12)

### Proof

Let

`phi_R(t)=E exp(itR)`.

The trivial bound is `|phi_R(t)|<=1`. Since `chi in L^1`, Fourier inversion for the law of `Y`, followed by the Fresnel identity, gives for `t!=0`

`|phi_R(t)|
 <= (2 pi)^(-3) ||chi||_1 pi^(3/2) |t|^(-3/2) D^(-1/2).`     (13)

For completeness, the interchange can be justified by inserting `exp(-epsilon |y|^2)` in the `y` integral. The resulting complex Gaussian has determinant modulus at least `|t|^3 D`, so its absolute value is bounded by the right side of (13), uniformly in `epsilon`; dominated convergence against `|chi|` then removes the damping. The affine vector `beta` changes only the phase of the Gaussian integral, not its modulus.

Combining (11) and (13),

`|phi_R(t)|
 <= min(1, B |t|^(-3/2)),`

where

`B=(pi e)^(3/2) D^(-1/2)`.                                   (14)

The crossover is `t_0=B^(2/3)`. Hence

`int_R |phi_R(t)| dt
 <= 2[t_0 + B int_{t_0}^infinity t^(-3/2)dt]
 = 6 B^(2/3).`                                                (15)

Thus `phi_R in L^1`. Scalar Fourier inversion gives a continuous representative of the density and

`||p_R||_infinity
 <= (2 pi)^(-1) 6 B^(2/3)
 = 3 e D^(-1/3)`,                                             (16)

which proves (12).

No moment, support, log-concavity, connected-support, Gaussian, or post-rotation independence hypothesis is used.

## 4. Immediate exact-rank-three target branch

Take an exact-rank-three target matrix

`A=U M U^T`, `U^T U=I_3`,

whose three nonzero eigenvalues have moduli at least one. Then

`D=|det M|>=1`.

If every physical row leverage satisfies

`max_i ||u_i||^2 <=1/2`,                                     (17)

apply (12) with `beta=0` to obtain

`boxed: ||p_{X^T A X}||_infinity <=3e <8.155.`                (18)

Moreover the output density is continuous. This is a target-valid full end-to-end branch with all original inputs independent and cap one.

It is essential that the Fourier argument is applied to the ORIGINAL-product projection `U^T X`. We never diagonalize `M` and claim the resulting spectral coordinates are independent.

## 5. Conditional residual version with arbitrary frozen outside coordinates

The same theorem survives conditioning on any set of ORIGINAL coordinates and is therefore useful in the near-coloop geometry.

Let `S` be a set of physical coordinates and `R=S^c`. Write `U_R` for the remaining rows and assume

`G=U_R^T U_R` is positive definite.                                (19)

Normalize the remaining frame by

`V=U_R G^(-1/2)`, so `V^T V=I_3`.                             (20)

For `i in R`, define the normalized residual leverage

`c_i^(R)=u_i^T G^(-1)u_i`.                                   (21)

Suppose

`max_{i in R} c_i^(R) <=1/2`.                                (22)

Condition on all `X_j`, `j in S`. Because the conditioning is on ORIGINAL independent coordinates, the remaining `X_i`, `i in R`, stay independent with their original cap-one densities. If

`Y_R=V^T X_R`,

then `U_R^T X_R=G^(1/2)Y_R`, and the conditional quadratic form is

`Y_R^T [G^(1/2) M G^(1/2)] Y_R + beta(X_S)^T Y_R + gamma(X_S)`. (23)

The affine term is arbitrary but already covered by (12). Also

`|det(G^(1/2) M G^(1/2))|=D det G`.                           (24)

Therefore every conditional law satisfies

`||p_{Q|X_S}||_infinity <=3e [D det G]^(-1/3)`.               (25)

Averaging the conditional laws gives the same essential bound for `Q`. The characteristic-function envelope used in the proof of (12) is uniform in the frozen affine term, so averaging it also gives an integrable envelope; hence this branch has a continuous density as well.

Thus:

`boxed: ||p_Q||_infinity <=3e [D det G]^(-1/3)`               (26)

whenever (19),(22) hold.

## 6. One-heavy-row / near-coloop application

Let row `u_0` have leverage

`h=||u_0||^2<1`.

Condition on the ORIGINAL hub coordinate `X_0`. Then

`G=I_3-u_0u_0^T`,

so the matrix determinant lemma gives

`det G=1-h`.                                                   (27)

If every normalized remaining leverage satisfies

`u_i^T (I-u_0u_0^T)^(-1)u_i <=1/2,  i!=0`,                   (28)

then (26) gives the punctured near-coloop estimate

`boxed: ||p_Q||_infinity <=3e [D(1-h)]^(-1/3).`               (29)

This is target-valid for arbitrary affine cross terms generated by the frozen hub. In particular, for any fixed `eta>0`, the entire branch

`D(1-h)>=eta`, together with (28),

has the universal bound

`||p_Q||_infinity <=3e eta^(-1/3)`.                           (30)

For example, `D(1-h)>=1/64` gives

`||p_Q||_infinity <=12e <32.620`.                             (31)

This does not solve the limit `h up to 1`: the right side of (29) is allowed to blow up. That loss is real for this conditional residual compiler because the determinant of the normalized residual quadratic matrix is exactly `D(1-h)`.

## 7. Required partner result applied at an actual inequality

The newest completed designated partner result read in full is:

`yspennstate/math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260924T094654Z-account02-B10-QFORM-r13/REPORT.md`.

It proves, in the exact-coloop/null-hub chamber,

`Q=2 a H L + bL^2+2cLV+dV^2`,

with `H` an ORIGINAL coloop coordinate independent of the entire leaf bank and `(L,V)` retained as a possibly dependent 2D product projection, that

`||p_Q||_infinity <=6 K^(2/3)|a|^(-2/3)|d|^(-1/3)`.          (32)

For the exact target geometry the partner proves `K<=2`, `|a|>=1`, `|d|>=1`. Therefore, at the actual endpoint `h=1`,

`boxed: ||p_Q||_infinity <=6*2^(2/3)<9.525.`                  (33)

This is the actual inequality at which the designated partner result is spent. It shows that the blow-up of (29) as `h->1` is a limitation of the residual-Wiener determinant compiler, not a singularity of the exact-coloop endpoint itself.

Combining the two results yields a clean endpoint/diffuse-residual picture for the null-hub near-coloop programme:

- if `h<1`, (28) holds, and `D(1-h)>=eta`, use (30);
- if `h=1`, use the partner endpoint (33), with no independence assumed between the two leaf spectral aggregates.

The remaining punctured collar is therefore a genuine **gluing** problem, not an endpoint existence problem.

## 8. What remains open

This run does **not** prove arbitrary exact rank three. Remaining cases include:

1. a physical row leverage `>1/2` with a punctured residual determinant `D(1-h)` small;
2. normalized residual frames for which some post-hub leverage in (28) is again `>1/2`;
3. the positive-leakage shared-leaf aggregate identified by account02/B10, where coefficient-smallness cannot be treated perturbatively under arbitrary fragmented/unbounded input laws.

The first unpaid implication is now:

`QFORM-HEAVY-ROW-WIENER-TO-PARTNER-ENDPOINT-GLUING-v1`:

bridge (29) to the finite endpoint (33) without any coefficient-continuity assumption, or else recursively spend a second heavy normalized residual row before determinant inversion. Any such bridge must retain ORIGINAL-product provenance and must survive the live conditional-cap and arbitrary-joint counterexamples.

Full exact rank three: **OPEN**. Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity: **OPEN**. Continuity **is proved** for the new leverage-1/2 and conditional-residual branches above.
