SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B01, 2026-09-22T21:06:42Z.
attacking: leakage-safe three-bank overlap synthesis; test whether a uniformly conditioned cross-bank triangle plus arbitrary within-bank phases can by itself force integrable Fourier decay.

# QFORM account01/B01 — exact rank-one completion obstruction for three-bank cross smoothing

**Run:** `20260922T210642Z-b01-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and first missing implication

The full target remains open: for independent real coordinates with densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential-supremum density bound for `Q=X^TAX`, or give a target-valid counterexample. Continuity is a separate desired conclusion.

The current B01 interface from account02/B01 r27 is the leakage-preserving three-bank identity

`|phi_Q(t)|^2 = int prod_{i=1}^3 K_{i,t}(delta_i,t(M delta)_i) d delta`,

where arbitrary within-bank phases are absorbed into complex amplitudes and each overlap kernel retains the unnormalized shear/mixed-norm budget. The first unpaid synthesis question was whether three well-conditioned cross-bank couplings can themselves force enough smoothing after arbitrary within-bank leakage.

This run shows that the answer is **no** in the strongest possible three-scalar-bank sense: every nonzero cross triangle has an exact diagonal completion of rank one. For the symmetric unit triangle the completion gives an explicit cap-one product law whose output density is unbounded and whose characteristic function has exactly the nonintegrable `|t|^{-1/2}` stationary-phase order. Thus no theorem depending only on the cross-triangle conditioning and the three marginal density caps can close the full leakage branch. The missing spectral resource must be harvested from the within-bank residuals (or recursively from additional coordinates).

## 2. Exact algebraic normal form: every nonzero cross triangle has a rank-one diagonal completion

Let

`C(a,b,c) = [[0,a,c],[a,0,b],[c,b,0]]`,

with `abc != 0`. Define

`d1*=a*c/b`,  `d2*=a*b/c`,  `d3*=b*c/a`.

Then

`M* = C(a,b,c)+diag(d1*,d2*,d3*)`

has rank exactly one. Indeed, since `d1* != 0`,

`M* = (1/d1*) (d1*,a,c)^T (d1*,a,c)`.

The identities needed for the factorization are

`a^2/d1*=d2*`, `c^2/d1*=d3*`, `a*c/d1*=b`.

Hence arbitrary one-bank quadratic phases can change a perfectly nondegenerate cross triangle into a one-dimensional square. The cross terms themselves are untouched.

This completion is unique: if a symmetric rank-one matrix has the fixed nonzero off-diagonal entries `a,b,c`, then its diagonal entries necessarily equal the three values above, by the vanishing of the `2x2` principal minors.

### Defect form

For an arbitrary diagonal completion `d_i=d_i*+delta_i`,

`M = M* + diag(delta_1,delta_2,delta_3)`.

If `sigma_min(M)>=s`, then at least two of `|delta_1|,|delta_2|,|delta_3|` are at least `s`. This follows from the rank-one perturbation inequality

`s_3(D+R) <= s_2(D)`

for `D=diag(delta_i)` and `rank(R)<=1`. Thus `s_3(M)>=s` implies `s_2(D)>=s`.

This gives a precise successor obligation for a leakage-safe proof: after removing the dangerous rank-one completion, two diagonal-defect curvatures must be paid if the **actual scalar core** is well conditioned. If those curvatures have disappeared into larger within-bank quadratic blocks, the proof must recurse into those blocks rather than charging the cross triangle again.

## 3. Exact counterexample to cross-core-only leakage closure

Take

`a=b=c=1`,

so

`C=[[0,1,1],[1,0,1],[1,1,0]]`

has eigenvalues `{2,-1,-1}` and therefore `sigma_min(C)=1`.

Let `U,V,W` be independent `Unif[-1/2,1/2]`, hence each input density is exactly one on its support. Add the legal within-bank phases

`R_1(U)=U^2`, `R_2(V)=V^2`, `R_3(W)=W^2`.

The complete three-bank quadratic form is

`Q0 = 2(UV+VW+WU)+U^2+V^2+W^2 = (U+V+W)^2`.

Thus the well-conditioned cross core has collapsed to rank one solely through one-bank quadratic phases.

Let `S=U+V+W`. Its density is the centered three-fold unit-interval convolution

`h(s)=3/4-s^2` for `|s|<=1/2`,

and `h(s)=(1/2)(3/2-|s|)^2` for `1/2<=|s|<=3/2`.

Therefore for `0<y<1/4`, the density of `Q0=S^2` is exactly

`p_Q0(y) = [h(sqrt(y))+h(-sqrt(y))]/(2sqrt(y))`
`        = (3/4-y)/sqrt(y)`.

Hence

`||p_Q0||_infinity = infinity`.

This is **not** a counterexample to the owner's three-large-eigenvalue conjecture, because the completed `3x3` matrix is `J_3`, of rank one. It is a counterexample to the stronger intermediate statement:

> a uniformly conditioned three-bank off-diagonal core, together with arbitrary within-bank phases and cap-one scalar aggregate densities, already forces a bounded output density.

That intermediate statement is false even at `sigma_min(C)=1`.

## 4. Fourier sharpness and direct application of account02/B01 r27

The same example gives an exact sharpness test for the leakage-safe cross-edge estimate from the designated partner account02/B01 r27.

Since `h(0)=3/4` and `h` is piecewise `C^1`, one-dimensional stationary phase at the nondegenerate critical point `s=0` gives

`phi_Q0(t)=int h(s) exp(i t s^2) ds`
`         = (3/4) exp(i pi/4) sqrt(pi/t) + O(t^-1)`

as `t->+infinity`.

Consequently

`lim_{t->infinity} sqrt(t)|phi_Q0(t)| = (3/4)sqrt(pi)`.

The partner theorem `QFORM-CROSS-EDGE-POINTWISE-v1` applies to any of the three physical cross coefficients, all equal to one, and gives the actual inequality

`|phi_Q0(t)| <= min(1,sqrt(pi/|t|))`.

Thus the partner exponent `1/2` is sharp up to the factor `4/3` on this leakage example. Having **three** nonzero safe cross edges does not improve the universal leakage-safe pointwise exponent: the one-bank diagonal phases can rank-one-complete all three simultaneously.

This directly applies the named partner result rather than merely citing it, and it shows why its three separate cross-edge budgets cannot simply be multiplied to obtain an `L^1_t` estimate.

Partner source actually used:

`yspennstate/math-open-problems@b3f18a11f29e878b69278f6487fe50b4e3380d99:proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T200159Z-account02-B01-qform-r27/REPORT.md`.

## 5. Target-valid embedding: the conjecture survives because the missing curvature is elsewhere

The obstruction above identifies a proof-interface failure, not a target failure. Embed it into the exact target by adding two independent physical square directions:

`A_target = J_3 direct_sum I_2`.

Its eigenvalues are exactly `{3,1,1,0,0}`, so it has three eigenvalues of modulus at least one. For five independent `Unif[-1/2,1/2]` inputs,

`Q_target = (U+V+W)^2 + Y_1^2 + Y_2^2`.

The variable `S=U+V+W` is independent of `Y_1,Y_2`, and `||p_S||_infinity=3/4<=1`. Hence the already-proved diagonal same-sign theorem applied to the independent triple `(S,Y_1,Y_2)` gives

`||p_Qtarget||_infinity <= pi`.

At the Fourier level the three independent square factors each contribute the scalar `L^3`/stationary-phase currency; in fact

`phi_Qtarget(t) = phi_{S^2}(t) phi_{Y_1^2}(t) phi_{Y_2^2}(t)`

has asymptotic order `|t|^{-3/2}`. The two residual physical squares provide exactly the two half-powers missing from the cross-triangle-only `|t|^{-1/2}` behavior.

This target-valid embedding isolates the correct next task: **residual curvature is not optional bookkeeping; it is the smoothing resource that repairs the rank-one completion.**

## 6. Relation to the current three-bank core theorem

Account02/B05 proved that for three independent scalar aggregates and an actual scalar quadratic core `M` with `sigma_min(M)>=s`, the scalar quadratic-plus-affine law has density `<36/s`. That result is not contradicted here. In the present obstruction the actual scalar core after adding the within-bank phases is `J_3`, which is singular. What fails is the attempt to apply the theorem to the off-diagonal matrix `C` while treating the same-variable quadratic terms `U_i^2` as harmless residual leakage.

B05 source used for the scope comparison:

`yspennstate/math-open-problems@a31006ef311ca9e937f37c62d602d21ada3b1139:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T202100Z-b05-qform-47d9c1a2/REPORT.md`.

## 7. Compact conditional end-to-end consequence

A viable three-bank proof can now be organized as follows.

1. Extract three disjoint original-coordinate banks and the exact cross-bank scalar aggregate coefficients.
2. Form the unique dangerous rank-one diagonal completion `d_i*` above for every nonzero triangle.
3. Charge the **defects** from that completion, not the cross triangle itself, to actual residual spectral curvature.
4. If the actual scalar aggregate core is uniformly nonsingular, the defect lemma forces two defect curvatures of size at least its smallest singular value and the completed scalar-core theorem applies.
5. If those defect curvatures leak into higher-dimensional within-bank blocks, recurse into those blocks using the ridge/pair/random-slope mechanisms before taking conditional suprema.
6. Only after those residual currencies are retained can the three overlap budgets be combined toward a global `L^1_t` or small-ball bound.

The first unpaid implication is therefore sharpened to:

`QFORM-TRIBANK-RANKONE-COMPLETION-DEFECT-RECURSION-v1` — show that the two defect curvatures forced by the global three-large-eigenvalue resource can be harvested inside the original product banks (or routed to an already-paid ridge/pair branch) without worst-fiber normalization.

## 8. Status and regularity

- Full QFORM: **OPEN**.
- Intermediate claim "conditioned cross triangle + arbitrary within-bank phases suffices": **REFUTED**.
- Rank-one completion normal form and defect lemma: **PROVED**.
- Target-valid embedding: **PROVED** and remains bounded (`<=pi`).
- General essential boundedness: not proved by this run.
- General continuity: not proved by this run.

No Gaussianity, moments, compact support beyond the explicit test example, spectral-coordinate independence, or pointwise scalar Fresnel premise is introduced into the target argument.
