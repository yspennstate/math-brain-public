SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T13:32:04Z.
attacking: a weak-law-stable fixed-tent normal form for the exact sharp density constant, and application of account02/B15's completed ruled one-sheet bound to that fixed functional.

# QFORM account01/B15 — fixed-tent exact normal form and rough-law-safe closure

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / FIXED-TENT-EXACT-NORMAL-FORM / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Control, scope, and exact target

Fresh final control was re-resolved at `yspennstate/math-research-brain@0cdc732db5de9f7573ef7fa36d1f8c01d3184e67`. The protected `AGENTS.md` and `scheduled_tasks/README.md` blobs are unchanged from the startup read; OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and no later B15 stop was observed.

The full target remains OPEN: for independent real coordinates with probability densities `0<=f_i<=1` and symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential density height of

`Q=X^T A X`.

Write

`s(A)=s_3(A)`

for the third largest absolute eigenvalue. The target class is equivalently `s(A)>=1`. Continuity of the raw output density is kept separate from this central `L^infinity` question.

Corrections consumed and preserved: no law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea height bound; no projection/X-ray-only control of the two-sheet trace; no small-operator-norm random-quadratic perturbation shortcut for arbitrary unbounded product sources.

The newest-Claude package required by the owner was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

The completed designated-partner source actually applied below is

`yspennstate/math-open-problems@46c33d97490f78f8c3de0435f63d573958d81180`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T130525Z-account02-B15-qform-auto11/REPORT.md`.

That partner report rechecks the newest-Claude ruled one-sheet coarea constant, proves its rough-input transfer in original coordinates, and supplies the interval/tent inequalities used in Section 7.

## 2. Qualitative absolute continuity is much easier than the owner theorem

I first separate the three regularity levels cleanly.

### Proposition 2.1 — absolute continuity for every nonzero quadratic form

Let `A` be any nonzero real symmetric matrix and let the full input law on `R^n` be absolutely continuous with respect to Lebesgue measure. No independence or density cap is needed. Then the law of

`q(x)=x^T A x`

is absolutely continuous on `R`.

**Proof.** The gradient is

`grad q(x)=2Ax`.

Its critical set is `ker A`, a proper linear subspace and hence Lebesgue-null. Let `N subset R` be Lebesgue-null. For `k>=1` put

`E_k={x: |x|<=k, |grad q(x)|>=1/k}`.

By the coarea formula,

`int_(q^{-1}(N) cap E_k) |grad q(x)| dx = int_N H^{n-1}(q^{-1}(t) cap E_k) dt = 0`.

Since `|grad q|>=1/k` on `E_k`, the set `q^{-1}(N) cap E_k` has Lebesgue measure zero. The union of the `E_k` is `R^n\ker A`; adding the null critical set still gives a null preimage. An absolutely continuous input law therefore assigns `q^{-1}(N)` probability zero. QED.

So under the owner hypothesis absolute continuity is automatic. The difficult part is not existence of a density; it is one **universal quantitative height bound**.

## 3. Density height as domination of measures

For a finite Borel measure `mu` on `R`, define

`D_infinity(mu)=inf{D>=0: mu(E)<=D |E| for every Borel E}`,

allowing `+infinity`.

Then `D_infinity(mu)<infinity` iff `mu=p dx` for some `p in L^infinity`, and in that case

`D_infinity(mu)=||p||_(L^infinity,ess)`.

This formulation avoids any choice of density representative and does not assume continuity.

Let

`tau(u)=(1-|u|)_+`.

It satisfies

`tau>=0`, `int_R tau=1`, `||tau||_infinity=1`, `Lip(tau)=1`.

For a target output law `mu_Q`, define the fixed-scale tent profile

`H_Q(y)=(tau*mu_Q)(y)=E tau(Q-y)`.

## 4. Main theorem — one fixed tent has exactly the sharp universal density constant

Define extended-real sharp constants

`C_dens = sup_target s(A) D_infinity(mu_Q)`

and

`C_tent = sup_target sup_(y in R) s(A) E tau(Q-y)`.

### Theorem 4.1

`C_dens = C_tent`.

This equality is exact; there is no multiplicative loss, no continuity premise, and no assumption that the output already has a density.

### Proof: easy direction

If `mu_Q<=D dx`, then

`H_Q(y)=int tau(y-u) dmu_Q(u) <= D int tau = D`.

Hence

`s(A) sup_y H_Q(y) <= s(A)D_infinity(mu_Q)`.

Taking suprema gives `C_tent<=C_dens`.

### Proof: reverse direction by spectral homogeneity

Assume `C_tent<infinity`, and fix one target instance. Put `s=s(A)>=1` and `Q=X^TAX`.

For every `0<r<=s`, the scaled matrix

`A_r=A/r`

is still in the target class because

`s(A_r)=s/r>=1`.

Its output is `Q/r`. Therefore, for every `t in R`, the definition of `C_tent` gives

`(s/r) E tau((Q-t)/r) <= C_tent`.

Set

`tau_r(u)=r^{-1} tau(u/r)`.

Then the preceding inequality is exactly

`(tau_r*mu_Q)(t) <= C_tent/s`                                             (4.1)

for every `t` and every `0<r<=s`.

Now let `phi>=0` lie in `C_c(R)`. Since `tau_r` is an approximate identity,

`int phi dmu_Q = lim_(r downarrow 0) int phi(t)(tau_r*mu_Q)(t) dt`.

Using (4.1),

`int phi dmu_Q <= (C_tent/s) int phi(t) dt`.

By the Riesz representation/regularity characterization of measure domination,

`mu_Q <= (C_tent/s) dx`.

Thus

`s D_infinity(mu_Q) <= C_tent`.

Taking the target supremum gives `C_dens<=C_tent`, proving equality. QED.

### Consequence 4.2 — the central target can be attacked at one fixed physical scale

The entire owner theorem is equivalent to

`sup_target sup_y s(A) E (1-|Q-y|)_+ < infinity`.                         (4.2)

So there is no need to carry a shrinking window, an approximate identity, or raw density continuity through the hard product-geometry estimate. The shrinking occurs only **after** the uniform fixed-tent estimate has been proved, and spectral scaling performs that final passage exactly.

For comparison with a unit small-ball formulation,

`(1/2) P(|Q-y|<=1/2) <= E tau(Q-y) <= P(|Q-y|<1)`.

Thus the fixed tent is also quantitatively equivalent, up to constants, to a single fixed-width local probability; Theorem 4.1 gives exact equality at the sharp density-constant level.

## 5. Target-level regularity lemma for the fixed functional

The raw density may be rough, but the exact sharp functional from Theorem 4.1 is automatically regular.

### Lemma 5.1

For every probability law `mu` on `R`,

`H_mu(y)=(tau*mu)(y)`

lies in `C_0(R)`, obeys

`0<=H_mu<=1`,

and is `1`-Lipschitz:

`|H_mu(y)-H_mu(z)|<=|y-z|`.

In particular its maximum is attained.

**Proof.** The first two bounds are immediate. Since `tau` is one-Lipschitz,

`|H_mu(y)-H_mu(z)| <= int |tau(y-u)-tau(z-u)| dmu(u) <= |y-z|`.

Also

`H_mu(y)<=mu([y-1,y+1])`,

which tends to zero as `|y|->infinity` for any probability measure. QED.

Hence the sharp constant can be written

`C_dens = sup_target s(A) max_y H_Q(y)`.                                  (5.1)

This is an attained, continuous objective for every individual instance even before raw-output continuity is known.

## 6. Weak-law stability: the safe rough-input interface

Define the bounded-Lipschitz metric

`d_BL(mu,nu)=sup{|int f d(mu-nu)|: ||f||_infinity<=1, Lip(f)<=1}`.

Every translate `u -> tau(u-y)` is an admissible test, so

`sup_y |H_mu(y)-H_nu(y)| <= d_BL(mu,nu)`.                                 (6.1)

On probability measures on `R`, `d_BL` metrizes weak convergence. Therefore

`mu_m => mu  ==>  ||H_(mu_m)-H_mu||_infinity -> 0`.                       (6.2)

If also positive scales `s_m->s`, then, because all tent profiles are at most one,

`sup_y |s_m H_(mu_m)(y)-s H_mu(y)|`
`<= s_m d_BL(mu_m,mu)+|s_m-s| -> 0`.                                     (6.3)

This is the precise target-level rough-law limit theorem needed for a fixed-scale density estimate.

### Why this is nontrivial in light of the fresh partner obstruction

The latest account02/B15 report constructs target-valid smooth compact cap-one product laws for the fixed matrix `A=I_3` which converge weakly, while their output densities do **not** converge in `L^1` or `L^infinity` and their normalized shrinking-interval profiles remain separated by an explicit positive amount. In its notation,

`liminf_m sup_y | [rho_m([y-r_m,y+r_m])-rho([y-r_m,y+r_m])] /(2r_m) |`
`>=27/(9504 pi)>9.04e-4`.

Thus weak convergence cannot justify taking the source limit and the window-width limit simultaneously.

Equations (6.1)-(6.3) identify the safe order of operations:

1. keep the tent at **fixed unit scale**;
2. pass to a rough source using weak convergence;
3. only after a uniform target-class estimate is established, use the matrix scaling in Theorem 4.1 to recover the raw `L^infinity` density bound.

This order completely avoids the partner's shrinking-profile obstruction.

## 7. Exact cap-preserving smooth-core reduction

The same fixed-tent interface gives a zero-loss reduction to smooth compactly supported marginals.

### Lemma 7.1 — one-dimensional cap-preserving smoothing

If `f` is a probability density with `0<=f<=1`, then there are probability densities

`f_m in C_c^infinity(R)`, `0<=f_m<=1`,

with `||f_m-f||_1->0`.

**Construction.** Choose `R_m->infinity` so the discarded tail mass

`delta_m=int_(|x|>R_m) f(x) dx`

tends to zero. Put `g_m=f 1_[ -R_m,R_m]` and mollify with a compactly supported probability mollifier of width tending to zero:

`h_m=g_m*eta_m`.

Then `0<=h_m<=1`, `h_m` is smooth compactly supported, its mass is `1-delta_m`, and choose the mollifier scale so `||h_m-g_m||_1->0`.

Let `b>=0` be a fixed smooth compact probability bump. For a sufficiently large dilation `L_m`, the normalized dilation `b_(L_m)` satisfies

`delta_m ||b_(L_m)||_infinity <=1`.

Translate its support beyond the support of `h_m`, and put

`f_m=h_m+delta_m b_(L_m)(.-T_m)`.

The two supports are disjoint, so `f_m<=1`; it is a smooth compactly supported probability density. Finally

`||f_m-f||_1 <= ||h_m-g_m||_1+2 delta_m ->0`. QED.

For fixed dimension, if `F=prod_i f_i` and `F_m=prod_i f_(i,m)`, telescoping gives

`||F_m-F||_1 <= sum_i ||f_(i,m)-f_i||_1 ->0`.                             (7.1)

Hence, for the same matrix `A`,

`sup_y |E_m tau(Q-y)-E tau(Q-y)| <= ||F_m-F||_1 ->0`.                    (7.2)

### Corollary 7.2 — exact smooth compact core

Let the right-hand supremum below run over all target matrices but only independent marginals in `C_c^infinity` with cap one. Then

`C_dens`
`= sup_(smooth compact target sources) s(A) max_y E tau(Q-y)`.            (7.3)

There is no loss of sharp constant. This is stronger as a proof interface than attempting convergence of the raw densities: the latter is precisely what the fresh partner obstruction shows can fail under weak approximation.

A simultaneous fixed-dimensional coefficient limit is also safe at this functional: if `A_m->A`, input product laws converge weakly, and `s_3(A_m)->s_3(A)`, then the output laws converge weakly and (6.3) gives uniform convergence of the scaled fixed-tent profiles. No moment assumption is needed because coefficient convergence is locally uniform and weakly convergent probability laws are tight.

## 8. Actual application of completed account02/B15 ruled theorem

I now apply the assigned partner result directly to the exact sharp functional (4.2).

Let `S` be an original-coordinate physical triple such that

`B=A_(S,S)`

is invertible and indefinite, of signature `(2,1)` or `(1,2)`. Put

`kappa=sigma_min(B)`.

Condition on all outside **original** coordinates `W`. Completing the square in the three coordinates of `S` translates those three original independent variables; it does not rotate them. Let `G_B` denote the majority/one-sheet event relative to the resulting conditional critical value. The partner theorem proves, uniformly in the outside coordinates and affine translation, that the majority output submeasure obeys

`mu_B^+(I)<=C_B |I|`,

with

`C_B<=pi sqrt(2)/kappa`.                                                  (8.1)

Because the tent is nonnegative and has integral one, (8.1) gives for every center `y`

`E[tau(Q-y) 1_(G_B)] <= C_B <= pi sqrt(2)/kappa`.                         (8.2)

This is equivalently the partner's positive-tent inequality with epsilon one, applied conditionally at center `y-c(W)` and then averaged over `W`.

Therefore the exact sharp target functional satisfies the concrete decomposition

`boxed{`
`s(A) E tau(Q-y)`
`<= pi sqrt(2) s(A)/kappa + s(A) E[tau(Q-y) 1_(G_B^c)].`
`}`                                                                        (8.3)

If

`kappa>=c s(A)`,

then the full majority contribution costs at most

`pi sqrt(2)/c`.                                                           (8.4)

Only the minority/two-sheet fixed-tent term remains.

This application preserves arbitrary outside quadratic coefficients and cross couplings, uses only conditioning in original independent coordinates, and does not use a projection-only or rotated-independence shortcut.

## 9. Implication ledger: absolute continuity, bounded density, continuity

The logically correct hierarchy after this run is:

1. **Absolute continuity:** proved qualitatively already for every nonzero symmetric `A` and every absolutely continuous joint input law (Proposition 2.1). The target hypotheses are much stronger than needed.
2. **Instancewise bounded density:** source-reported local principal-block arguments provide matrix-dependent bounds in broad target scope, but the owner theorem asks for one constant independent of the physical conditioning. The central quantitative statement is exactly `C_dens<infinity`, equivalently the fixed-tent statement (4.2).
3. **Raw continuous density:** this is a separate stronger qualitative conclusion. It does not follow from an `L^infinity` bound alone. The shared canonical `CLAIMS.json` still records the full target continuous-representative claim as OPEN, so this run does not promote it. A sufficient Fourier condition such as `hat(mu_Q) in L^1` would imply a `C_0` density, but the live pointwise-decay correction forbids assuming a universal such envelope.
4. **Regularized continuity:** regardless of raw continuity, the exact fixed-tent profile `H_Q` is always in `C_0`, one-Lipschitz, and has an attained maximum. This is the target-level regularity lemma actually needed by the new sharp normal form.

The partner's target-valid oscillatory family further shows that raw continuity/common height plus weak convergence does not imply density convergence, so continuity cannot be used as a surrogate for the universal small-ball estimate.

## 10. First unpaid implication after this run

The global theorem is still OPEN. The fixed-tent reduction isolates the remaining quantitative task as

`boxed{ sup_target sup_y s(A) E tau(X^TAX-y) < infinity. }`              (10.1)

On any branch possessing a well-conditioned indefinite original-coordinate physical triple, (8.3) pays the entire majority/one-sheet contribution. The remaining local term is

`s(A) E[tau(Q-y) 1_(minority/two-sheet)]`.                               (10.2)

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction says this cannot be controlled from a generic projection X-ray norm alone. In the no-good-minor/high-leverage classes, the structural work is still to aggregate original-coordinate product banks/ridges/volume certificates before paying reciprocal degeneracies, or to show that the simultaneous minority regime falls into one of those already-paid branches.

The regularity/limit contribution of this run is that any such branch may now be proved first for smooth compact cap-one sources at the **fixed tent scale**, passed to rough sources with zero loss using Section 6/7, and only then desmoothed exactly by target homogeneity. This avoids both false pointwise Fourier decay and the fresh partner's normalized shrinking-window obstruction.

## 11. Status and source discipline

This is a complete supporting reduction and rough-law closure, not a proof of the full conjecture. No FEI or other research was used. No task, schedule, enablement/quiet state, notification, email, account binding, permission, paid/remote call, public release, or production state was changed.

The canonical same-hour login file already existed for the distinct account01/B15 run `20260923T130634Z-account01-B15-QFORM-auto11`; it was not overwritten. This run has its own immutable math path and remains `WITHOUT_VERIFIED_BRAIN` because repository retrieval/publication is not verified native learned-memory ingestion.
