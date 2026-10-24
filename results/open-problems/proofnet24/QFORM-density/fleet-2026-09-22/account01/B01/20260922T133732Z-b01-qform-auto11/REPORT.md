# QFORM B01 — averaged scalar gate transfer and conditional smoothing budget

Run: `20260922T133732Z-b01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Control read: `yspennstate/math-research-brain@a061e3c35962dd58137107493fe491a17a8714cb`, refreshed before publication at `ba4d529d2fc96add303b46fe7846045aef311f54`  
Status: `ESSENTIAL_STEP_APPLIED`; full conjecture remains `OPEN`; execution label `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and preserved correction

The target is the full arbitrary-product-law quadratic-form density conjecture: independent real coordinates with densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No rotation of the inputs is permitted as a way to preserve independence.

The phase-aligned fragmented-support counterexample remains in force: for any prescribed nonzero frequency `s` and any `delta>0`, the set

`{x : dist(s x^2, 2 pi Z) <= delta}`

has infinite Lebesgue measure. Choosing a measurable subset of total measure one and using its indicator as a density gives a scalar quadratic characteristic function with real part at least `cos(delta)` at that chosen frequency. Thus there is no law-uniform pointwise `|s|^{-1/2}` scalar Fresnel bound. Nothing below uses such a bound.

## 2. Partner theorem actually consumed

I use two completed results of the assigned partner `account02/B01`.

1. Run `20260922T120355Z-account02-B01-qform-r19`, canonical report `yspennstate/math-open-problems@fedbec07e3e8b2f9fcd2b1a65b0bb2a0137c212f`. For any probability density `0<=f<=1`, any `a!=0`, any `b`, and

   `F(t)=int exp(i t(a x^2+b x)) f(x) dx`, 

   every `q>2` satisfies

   `||F||_q <= S_q |a|^(-1/q)`,

   where

   `S_q=(4 pi)^(1/q) ((q-1)/(q-2))^((q-1)/q)`.

   In particular `S_3=(16 pi)^(1/3)`.

2. Run `20260922T130024Z-account02-B01-qform-r20`, canonical report `yspennstate/math-open-problems@3f6eacae4f27ffb171ba0e680f1861ae01b7246d`. For every interval `I` of length `L`, the same scalar gate obeys

   `int_I |F(t)|^2 dt <= L` if `|a|L<1`, and

   `int_I |F(t)|^2 dt <= |a|^(-1)[8+4 pi(1+log(|a|L))]` if `|a|L>=1`.

The r20 correction also shows that a direct absolute-value ambiguity/Hölder factorization can lose logarithmically even for a diagonal three-square form; that failed mechanism is not used here.

## 3. First new result: the r20 local-L2 theorem transfers to the fully coupled quadratic form

Let `Q=X^T A X` with the full target product law, and suppose one original-coordinate diagonal entry is `a=A_ii!=0`. Write `Y=X_{-i}`. Conditional on `Y=y`,

`Q = a X_i^2 + b(y) X_i + c(y)`

for some real `b(y),c(y)`. Thus

`phi_Q(t)=E_Y[ exp(i t c(Y)) F_{b(Y)}(t) ]`,

where each `F_b` is the scalar gate above with the same `a` and the original density of `X_i`.

By Jensen,

`|phi_Q(t)|^2 <= E_Y |F_{b(Y)}(t)|^2`.

Therefore, for every interval `I` of length `L`,

`int_I |phi_Q(t)|^2 dt <= B_a(L)`,

with

`B_a(L)=L` if `|a|L<1`,

and

`B_a(L)=|a|^(-1)[8+4 pi(1+log(|a|L))]` if `|a|L>=1`.

Consequently, for every `eta>0`,

`Leb{t in I : |phi_Q(t)|>eta} <= eta^(-2) B_a(L)`.

This is an averaged-in-frequency estimate for the *fully coupled* quadratic form: every off-diagonal interaction survives inside `b(Y),c(Y)`, and the bound is uniform in those random affine tilts. It is a valid replacement for the false pointwise scalar Fresnel bound, although by itself it does not imply `phi_Q in L^1`.

## 4. Conditional smoothing-budget lemma

The next result quantifies how different source-valid oscillatory mechanisms can be combined when the original-coordinate quadratic graph genuinely separates them after conditioning.

Let the independent physical coordinates be partitioned into disjoint blocks

`U_0,U_1,...,U_m,Z`.

Assume that, after fixing `Z=z`, the quadratic phase splits as

`Q = c(z) + R_z(U_0) + sum_{j=1}^m S_{j,z}(U_j)`

with no quadratic cross terms between different active blocks. The active blocks remain independent conditional on `Z` because the original law is a product law.

Assume uniformly in `z` that

`|r_z(t)| <= min(1, M |t|^(-rho))`

for the conditional characteristic function of `R_z`, and for some `q>m`,

`||s_{j,z}||_q <= K_j`, `j=1,...,m`.

Put

`delta = rho + m/q - 1`.

If `delta>0`, then

`||phi_Q||_1 <= D(rho,m,q) M^((1-m/q)/rho) prod_j K_j`,

where

`D(rho,m,q)=2^(1-m/q) [1 + 1/(1-2^(-delta))]`.

Hence `Q` has a bounded continuous density vanishing at infinity, with

`||p_Q||_infinity <= (2 pi)^(-1) D(rho,m,q) M^((1-m/q)/rho) prod_j K_j`.

### Proof

For fixed `z`, set `S_z(t)=prod_j s_{j,z}(t)`. Holder gives

`||S_z||_{q/m} <= prod_j K_j`.

Let `T_0=M^(1/rho)`. On `|t|<=T_0`, Holder gives

`int |S_z(t)| dt <= (2T_0)^(1-m/q) prod_j K_j`.

On the dyadic annulus

`A_k={2^k T_0 < |t| <= 2^(k+1)T_0}`,

we have `|r_z(t)|<=2^(-k rho)` and `|A_k|=2^(k+1)T_0`, so

`int_{A_k}|r_z S_z| <= 2^(1-m/q) T_0^(1-m/q) 2^(-k delta) prod_j K_j`.

The geometric series converges because `delta>0`. The displayed bound follows. Finally

`|phi_Q(t)| <= E_Z |r_Z(t) S_Z(t)|`,

so Fubini transfers the same `L^1` bound to the unconditional characteristic function. Fourier inversion gives the bounded continuous density and the Riemann-Lebesgue conclusion.

The requirement that the active blocks really separate is essential. Merely knowing a pointwise endpoint estimate and an unrelated scalar `L^q` bound for the same coupled characteristic function does not create this product structure.

## 5. Three concrete "three-direction" closures

I now combine the lemma with my previous source-safe random-slope Plancherel theorem, canonical handoff `account01/B01/20260922T124907Z-b01-qform-auto11.md`. For disjoint physical sets `I,J` with `|I|=|J|=k` and invertible `C=A[I,J]`, conditioning outside `I union J` gives

`|r_z(t)| <= min(1, pi^(k/2)|det C|^(-1/2)|t|^(-k/2))`

uniformly in all induced linear tilts and all self-block curvature.

### 5.1 Two cross-slope directions plus one scalar gate

Take `k=2`, so `rho=1`. Let `ell` be another physical coordinate with

`A_{ell,u}=0` for every `u in I union J`,

and let `alpha=|A_{ell ell}|>0`. The coordinate `ell` may couple arbitrarily to the conditioned remainder `Z`; this only changes its linear coefficient.

Using the partner's `q=3` scalar theorem and the smoothing lemma with `m=1` gives

`||p_Q||_infinity <= C_21 (alpha |det C|)^(-1/3)`,

where

`C_21 = 2 [1 + 1/(1-2^(-1/3))] = 11.6946442037...`.

So a rank-two physical cross packet plus one conditionally separated scalar curvature direction is enough for a continuous bounded density even though the rank-two random-slope estimate alone is only the nonintegrable endpoint `|t|^{-1}`.

### 5.2 One cross-slope direction plus two scalar gates

Take `k=1`, so `I={i}`, `J={j}`, `c=A_ij!=0`, and `rho=1/2`. Let `ell_1,ell_2` be two additional physical coordinates such that the three active blocks `{i,j}`, `{ell_1}`, `{ell_2}` have no quadratic cross terms between one another. They may each couple to the conditioned remainder `Z`. Put `alpha_r=|A_{ell_r ell_r}|>0`.

With `m=2,q=3`,

`||p_Q||_infinity <= C_12 (|c| alpha_1 alpha_2)^(-1/3)`,

where

`C_12 = 4 [1 + 1/(1-2^(-1/6))] = 40.6631805953...`.

The dyadic exponent is `1/2+2/3-1=1/6>0`.

### 5.3 Three scalar gates

If three physical coordinates `ell_1,ell_2,ell_3` are pairwise quadratically uncoupled from one another, while arbitrary couplings to the conditioned remainder are allowed, and `alpha_j=|A_{ell_j ell_j}|>0`, then conditional Holder directly gives

`||phi_Q||_1 <= prod_j ||F_j||_3 <= 16 pi (alpha_1 alpha_2 alpha_3)^(-1/3)`.

Hence

`||p_Q||_infinity <= 8 (alpha_1 alpha_2 alpha_3)^(-1/3)`.

This route is sign-independent and keeps arbitrary affine tilts coming from the rest of the matrix.

Together with the existing `k=3` random-slope theorem, these cases exhibit a precise conditional smoothing budget: cross-slope dimensions contribute `1/2` of Fourier decay each, while independent scalar quadratic gates contribute `1/3` of `L^1` integrability each at `q=3`. The threshold is exactly the one-dimensional Fourier inversion requirement.

## 6. Why this is not the full conjecture

The owner target does not guarantee that the physical coordinate graph splits into the active blocks required above. In particular, the live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` gives a spectrum-`{1,1,-1}` family for which a single scalar pivot does not expose a rank-two disjoint cross block. The live correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` shows that no uniformly conditioned fixed principal triple or rank-three physical cross cut is forced either. High-cardinality aggregation must occur before paying local reciprocal constants in the remaining branch.

The new results therefore do **not** solve the full conjecture. They identify a source-safe conditional closure mechanism and, more importantly for B01's assignment, transfer the partner's scalar averaged estimates to the fully coupled characteristic function and quantify exactly when averaged scalar gates repair a borderline cross-packet Fourier bound.

## 7. First unpaid implication

A full proof still needs a dimension-free structural/analytic bridge that, from the three-large-eigenvalue hypothesis alone, produces either

1. a source-valid high-cardinality cross packet strong enough to cross the `L^1` threshold, or
2. a conditional decomposition into smoothing blocks whose budget satisfies the inequality above,

without assuming zeros that are not forced by the matrix and without replacing product provenance by arbitrary bounded joint densities.

The most immediate B01 continuation is to seek a *coupled* analogue of the smoothing-budget lemma in which the scalar gate can interact with the rank-two packet through a low-rank linear coupling, while preserving enough displacement cancellation to avoid the r20 logarithmic ambiguity obstruction.

## 8. Verification

No Monte Carlo evidence is used. A deterministic arithmetic checker evaluates the three explicit constants and the dyadic exponents; its source and exact output are saved beside this report.

Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.
