SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T02:03:19Z.

attacking: exact regularity separation for the rank-three indefinite two-sheet branch; seek a product-preserving target-level trace estimate and apply account02/B15's completed one-sheet theorem to the tent inequality.

# account01/B15 — exact critical-gap fixed-window normal form

Run: `20260923T020319Z-account01-B15-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / EXACT_CRITICAL_GAP_FIXED_WINDOW_NORMAL_FORM`  
Full unrestricted QFORM: **OPEN / NOT PROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid premises

The owner target is the universal bounded-density estimate for `Q=X^T A X` under independent scalar densities `<=1` and at least three eigenvalues of `A` of modulus at least one. This report treats the exact-rank-three indefinite branch and gives a sharper equivalent formulation of its still-unpaid minority side.

Two completed `account02/B15` results are used, at their immutable sources.

1. **One-sheet theorem.** `yspennstate/math-open-problems@113aff6eea39e748c1bb6685c7656add2487c03e`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T000548Z-account02-B15-QFORM/REPORT.md`. For an exact rank-three signature `(+,+,-)` form with nonzero eigenvalue magnitudes `lambda_1,lambda_2,mu`, if `s=min(lambda_1,lambda_2,mu)`, the majority-sign submeasure on `[0,infinity)` has density at most `pi sqrt(2)/s`. The theorem is valid for rough cap-one product inputs and uses physical translation for its affine-in-range extension, not independence after spectral rotation.
2. **Fixed-instance regularity theorem.** `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`. For every fixed real symmetric `A` of rank at least three and every cap-one product input, `X^T A X` has a bounded density with a representative in `C_0(R)`. Its bound is matrix-dependent.

I also retain the correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, whose complete source is `yspennstate/math-open-problems@cfb4137e221cd87aeb4f669389d14fa65e3251e7`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T120617Z-a01-b06-qform-r11/REPORT.md`. Importantly, that counterexample is concentrated near the already separated two-sheet level `q=-1`; the critical-gap normalization below therefore does **not** make an X-ray-only argument valid.

No pointwise law-uniform quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea bound, positive conditional-projection moment, or projection-only shortcut is used.

## 2. Setup and exact scaling symmetry

Consider the exact-rank-three signature `(+,+,-)` class

`Q=X^T A X`,

where the three nonzero eigenvalue magnitudes are `lambda_1,lambda_2,mu>0`. Put

`s=s_3(A)=min(lambda_1,lambda_2,mu)`.

By the fixed-instance partner theorem, write `p_Q in C_0(R)` for the canonical continuous density. For `a>0`, replace `A` by `aA`. Then

`Q_a=aQ`, `s_3(aA)=a s`, and `p_{Q_a}(u)=a^{-1} p_Q(u/a)`.

Hence the scaled height is exactly invariant:

`(a s) p_{Q_a}(a t)=s p_Q(t)`.

This elementary symmetry is the engine of the new reduction.

Define the sharp scaled minority height

`C_- := sup_{instances} s sup_{t<0} p_Q(t)`.

For signature `(-,-,+)`, negate the form; all statements below are identical with signs reversed.

## 3. Critical-gap normalization: the cone vertex can be removed from the remaining sharp problem

Define

`C_-^{gap} := sup_{instances} s sup_{t<=-1} p_Q(t)`.

Then

`boxed: C_-^{gap}=C_-`.

### Proof

The inequality `C_-^{gap}<=C_-` is immediate. For the reverse inequality, fix any admissible instance and any `t<0`. Choose `a>=1/|t|`. For the scaled instance `Q_a=aQ`, the point `at<=-1`, and therefore

`(a s) p_{Q_a}(a t)=s p_Q(t)<=C_-^{gap}`.

Take the supremum over the original instance and `t<0`. `QED`

Thus a putative bad exact-rank-three indefinite sequence may be replaced, without changing its scaled density height, by another bad sequence whose offending points lie at distance at least one from the critical value. This is a normalization **across scaled instances**; it does not assert that a maximizer of a fixed `s=1` instance has a uniform distance from zero.

In the hyperbolic coordinates of the preceding B15 report, this says equivalently that the remaining two-sheet trace need only be controlled at levels `alpha>=1`. The difficult branch is therefore not a singularity at the cone vertex. It is global product-provenance concentration along separated two-sheet hyperboloids.

## 4. Exact fixed-unit-window representation of the minority sharp constant

Define the fixed-window functional

`W_- := sup_{instances, y<=-1} (s/2) P(|Q-y|<=1)`.

Then

`boxed: W_-=C_-`.

### Upper bound

If `y<=-1`, then `[y-1,y+1] subset (-infinity,0]`. Since `Q` has a density,

`P(|Q-y|<=1) <= 2 sup_{t<0} p_Q(t)`.

Multiplying by `s/2` and taking the supremum gives `W_-<=C_-`.

### Reverse bound

Fix an admissible instance and `t<0`. For every sufficiently large `a`, `at<=-1`, so the scaled instance is admissible in the definition of `W_-`. Therefore

`W_- >= (a s/2) P(|aQ-at|<=1)`
`      = (a s/2) int_{t-1/a}^{t+1/a} p_Q(u) du`.

The partner fixed-instance theorem gives continuity of `p_Q` at `t`; hence

`lim_{a->infinity} (a/2) int_{t-1/a}^{t+1/a} p_Q(u) du = p_Q(t)`.

Consequently `W_- >= s p_Q(t)`. Taking the supremum proves `W_- >= C_-`. `QED`

This removes both the shrinking-window parameter and the near-critical region. The exact-rank-three minority problem is equivalent to one positive full-dimensional estimate at one physical scale:

`boxed: s P(Q in [y-1,y+1]) <= 2 C,   y<=-1.`

There is no codimension-one density trace in this formulation; the probability is taken directly under the original product measure.

## 5. Exact fixed-tent representation

Let

`T(u)=(1-|u|)_+`,

so `int_R T(u) du=1`. Define

`K_- := sup_{instances, y<=-1} s E T(Q-y)`.

Then

`boxed: K_-=C_-`.

Indeed, for `y<=-1`, the support of `T(Q-y)` lies in `Q<=0`, and therefore

`s E T(Q-y)
 = s int T(u-y) p_Q(u) du
 <= s sup_{u<0}p_Q(u) int T
 <= C_-`.

Conversely, for any fixed `t<0` and scaled instance `Q_a=aQ`, `at<=-1` for large `a`, and

`(a s) E T(Q_a-at)`
`=a s int T(a(u-t)) p_Q(u)du`
`=s int_{-1}^1 T(v) p_Q(t+v/a)dv`
`->s p_Q(t)`

by continuity and dominated convergence. Hence `K_- >= C_-`.

The window and tent forms are therefore not merely sufficient approximations: each recovers the **sharp scaled minority density constant exactly** when the class is closed under positive scalar multiplication.

## 6. Actual application of the completed partner one-sheet result

Let

`C_{3,ind}:=sup_{instances} s ||p_Q||_infinity`

for the exact-rank-three indefinite class. The completed `account02/B15` one-sheet theorem gives, after scaling its displayed eigenvalue-`>=1` estimate,

`p_Q(t)<=pi sqrt(2)/s` for a.e. `t>=0`.

The completed fixed-instance `C_0` theorem upgrades this to every `t>=0`. Therefore

`boxed: C_- <= C_{3,ind} <= max{pi sqrt(2), C_-}`.

Combining with Sections 4 and 5 gives the new exact reduction

`boxed: C_- = W_- = K_-`,

and hence

`boxed: C_{3,ind}<infinity iff W_-<infinity iff K_-<infinity.`

The partner theorem also applies directly to the actual tent inequality, for arbitrary center `y`:

`s E T(Q-y)`
`=s E[T(Q-y) 1_{Q>=0}] + s E[T(Q-y)1_{Q<0}]`
`<=pi sqrt(2) + s E[T(Q-y)1_{Q<0}]`.

Thus the majority-sign contribution is completely paid by a universal constant; the fixed-gap minority functional above is the only exact-rank-three indefinite density-height debt.

## 7. Relation to the previous hyperbolic-trace normal form

The preceding account01/B15 report wrote the minority density as the exact full-dimensional hyperbolic-ray trace

`H_rho(alpha)=(1/2) sum_{sigma=+/-1} int_0^{2pi} int_{sqrt(alpha)}^infinity rho(F_sigma(alpha,theta,w)) dw dtheta`,

with `p_Q(-alpha)=H_rho(alpha)` almost everywhere after the normalized spectral change of variables. The present scaling lemma implies that, for the sharp scaled constant, `alpha in (0,1)` may be discarded: every such density height is reproduced by scaling at some `alpha>=1`.

More importantly, the fixed-window identity replaces the trace problem by the source-level positive-volume statement

`P(Q in [y-1,y+1])
 = int 1_{y-1 <= x^T A x <= y+1} prod_i f_i(x_i) dx`,

with `y<=-1`.

That formulation retains the original-coordinate product law all the way to the final inequality, exactly as required by the correction ledger.

## 8. Why the live X-ray correction still bites

One might hope that putting the target level a unit away from the critical cone makes the generic two-dimensional projection/X-ray estimate sufficient. It does not. The source-valid B06 counterexample constructs a density with bounded X-ray norm whose `q=x_1^2+x_2^2-x_3^2` pushforward is of size `1/(10 delta)` throughout `[-1-delta,-1+delta]`. Its bad level is already centered at `-1`.

Therefore the present reduction removes an irrelevant near-vertex complication but does not remove the real information bottleneck. A successful proof of `W_-<infinity` must use product-projection provenance (or return all the way to the original product coordinates) beyond generic line-marginal control.

## 9. Logical regularity ledger

The implications are now especially clean.

- **Absolute continuity:** already holds for every nonzero quadratic under any absolutely continuous joint input; no three-eigenvalue hypothesis is needed.
- **Fixed-instance boundedness and continuity:** for rank at least three and cap-one product inputs, the completed partner theorem gives `p_Q in C_0 cap L^infinity`, but with a matrix-dependent height.
- **Universal height:** remains the open owner conjecture. In exact-rank-three signature `(2,1)`, the majority side is paid by `pi sqrt(2)/s`, and the remaining universal statement is exactly the fixed-gap fixed-window (or fixed-tent) minority estimate above.
- **Continuity is not being used to manufacture a universal height.** It is used only to identify the sharp density value with the limit of fixed-scale windows after scaling an individual instance. If one preferred, Lebesgue differentiation at approximate maximizers would give the same equality at the essential-supremum level without continuity.

## 10. First unpaid implication

For exact-rank-three signature `(2,1)`, prove one universal finite `C` such that

`boxed: s P(|X^T A X-y|<=1) <= C`

for every independent cap-one product source, every exact-rank-three `A` with `s=s_3(A)>0`, and every `y<=-1` after orienting the minority sign to be negative.

This one-scale, one-side, unit-gap statement is equivalent to finiteness of the entire exact-rank-three indefinite density constant. It should be attacked directly with product-preserving bank/cross-block/BL structure. Generic X-ray bounds alone are insufficient even at `y=-1`.

Closing this branch still does **not** close the unrestricted higher-rank owner target; the N3/hybrid structural step remains separate.
