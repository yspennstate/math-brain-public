SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B14, 2026-09-22T21:38:21Z.
attacking: translations/localization: a decoupling-ready zero-loss localization theorem for weighted Fourier and positive multi-copy functionals, with a quantitative regularity application.

# account03/B14 — weighted Fourier and multi-copy localization without fragment tax

Run: `20260922T213821Z-account03-B14-QFORM-r19`

Status: `SUPPORTING_THEOREMS_PROVED / TARGET_RELEVANT / FULL_QFORM_OPEN / CONTINUITY_NOT_FULLY_PROVED / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction-aware scope

The full target remains OPEN: for every finite `n`, independent real coordinates with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal `L^infinity` bound, or give a valid target counterexample. Continuity is a separate requested conclusion.

This run does not use law-uniform pointwise van-der-Corput decay, arbitrary-joint rank-three coarea, positive moments of conditional projection-density suprema, post-rotation independence, a bounded support radius, a bounded fragment count, or fragmentwise rescaling. The live correction state rules all of those shortcuts out in the scopes previously recorded.

The B14 question is narrower: can arbitrary shifts, remote support components and unbounded supports be removed from the *actual nonlinear Fourier/decoupling functionals* used by the current proof routes, with exactly zero loss in the desired constant? The answer below is yes for a broad class that includes weighted Fourier budgets and positive two-copy collision kernels.

## 2. Source-exact partner input

Designated partner account04/B14 proved `QFORM-LAW-LEVEL-FINITE-MIXTURE-LOCALIZATION-v1` at

`yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T201507Z-account04-B14-mixture-localization-r4/REPORT.md`.

Its theorem says that every cap-one product law on `R^n` is a total-variation limit of finite convex mixtures of product laws whose one-dimensional marginals are indicators `1_E` of compact finite unions of intervals with `|E|=1`. No support radius, number of fragments, separation, moment or centering parameter occurs.

Write `D_n` for all cap-one product probability laws and `F_n` for those finite-fragment product-indicator laws.

The results below apply this completed partner theorem to actual nonlinear inequalities rather than merely restating it.

## 3. Weighted Fourier localization

Let `P:R^n->R` be any measurable map and let `w:R->[0,infinity]` be any Borel weight. For a probability law `mu` define

`J_w(P;mu)=int_R w(t) | E_mu exp(i t P(X)) | dt`,

with values in `[0,infinity]`.

### Theorem 3.1 — `QFORM-WEIGHTED-FOURIER-EXTREME-LOCALIZATION-v1`

For every measurable `P` and every nonnegative Borel weight `w`,

`boxed( sup_{mu in D_n} J_w(P;mu) = sup_{nu in F_n} J_w(P;nu). )`       (3.1)

Thus a uniform weighted Fourier estimate may be proved only for compact finite-fragment extreme product laws and transfers to all arbitrary cap-one product laws with exactly the same constant.

#### Proof

Fix `mu in D_n`. By the partner theorem there are finite mixtures

`mu_r=sum_a theta_{r,a} nu_{r,a}`, `nu_{r,a} in F_n`,

with `||mu_r-mu||_TV ->0`.

For every `t`, the characteristic functional is linear in the law, so

`|E_{mu_r} e^{itP}| <= sum_a theta_{r,a} |E_{nu_{r,a}}e^{itP}|`.

Multiply by `w(t)>=0` and integrate:

`J_w(P;mu_r)
 <=sum_a theta_{r,a}J_w(P;nu_{r,a})
 <=sup_{nu in F_n}J_w(P;nu)`.                                    (3.2)

Total-variation convergence implies uniform convergence of expectations of bounded measurable functions, hence for each `t`,

`E_{mu_r}e^{itP} -> E_mu e^{itP}`.

Fatou applied to the nonnegative functions `w(t)|E_{mu_r}e^{itP}|` gives

`J_w(P;mu)<=liminf_r J_w(P;mu_r)<=sup_{F_n}J_w(P;nu)`.           (3.3)

Taking the supremum over `D_n` yields one inequality, while `F_n subset D_n` yields the reverse. QED.

No boundedness or integrability of `w` is assumed; the statement is an exact equality of extended-real suprema.

### Corollary 3.2 — exact target small-ball constant

For `P(x)=x^TAx+d^Tx+c`, define

`C_SB(P;C)=sup_{mu in C} sup_{I interval, |I|>0} mu(P^{-1}(I))/|I|`.

Then

`boxed( C_SB(P;D_n)=C_SB(P;F_n). )`                              (3.4)

Indeed the partner law-level theorem transfers every interval inequality simultaneously with the same constant, and the reverse inclusion is trivial. If this common number is finite, the pushforward measure is dominated by `C_SB` times Lebesgue measure and hence has a density bounded by `C_SB` almost everywhere. Therefore finite-fragment localization preserves the *exact density target constant*, not merely weak convergence or a fixed-interval estimate.

## 4. Translation quotient for every weighted Fourier budget

Now specialize to a quadratic-affine phase

`P_{A,d}(x)=x^TAx+d^Tx`,

with `A` symmetric. Decompose

`d=d_R+d_0`, `d_R in Range(A)`, `d_0=P_{ker A}d`.

Choose `h` with `2Ah=-d_R`. Writing `x=y+h`,

`P_{A,d}(y+h)=y^TAy+d_0^Ty+constant`.                            (4.1)

Physical translation preserves independence, every one-dimensional density cap, and the class `F_n` (translate each finite union of intervals). The additive constant contributes only a unimodular Fourier factor. Hence for `C=D_n` or `F_n`,

`boxed(
 sup_{mu in C}J_w(P_{A,d};mu)
 =sup_{mu in C}J_w(P_{A,d_0};mu).
)`                                                               (4.2)

The same equality holds for `C_SB`. Thus every range-compatible affine translation costs exactly zero; only the kernel component of an affine term is intrinsic. This remains true for arbitrary unbounded supports and arbitrarily distant fragments.

## 5. Weighted Fourier budget transfers quantitative regularity

Fix `0<alpha<=1`. Suppose a class of finite-fragment extreme product laws satisfies

`int_R |t|^alpha |phi_P(t)| dt <= M`                            (5.1)

uniformly. Theorem 3.1 transfers (5.1), with the *same* `M`, to every law in `D_n`.

Because `|phi_P|<=1`,

`int |phi_P(t)|dt <=2+M`: on `|t|<=1` use the trivial bound and on `|t|>1` use `|t|^alpha>=1`. Thus Fourier inversion gives a bounded continuous density and

`||p_P||_infinity <= (2+M)/(2pi)`.                              (5.2)

Moreover `|e^{-iu}-1|<=2^(1-alpha)|u|^alpha`, so

`boxed(
 |p_P(x+h)-p_P(x)|
 <= [2^(1-alpha) M/(2pi)] |h|^alpha.
)`                                                               (5.3)

This identifies the exact missing ingredient behind the partner's statement that ordinary total-variation localization does not by itself transfer continuity: a uniform weighted Fourier moment *does* transfer continuity, and even a quantitative Hölder modulus, without any support or fragment parameter.

## 6. Positive multi-copy localization: a decoupling-ready compiler

Many current QFORM routes square a characteristic function or introduce an independent copy. Ordinary one-law convexity is then not the right interface. The partner theorem nevertheless gives an exact positive-kernel multi-copy reduction.

Let `m>=1` and let `K:(R^n)^m->[0,infinity]` be measurable. For product input laws `mu_1,...,mu_m` set

`F_K(mu_1,...,mu_m)=int K(x^(1),...,x^(m)) dmu_1...dmu_m`.

### Theorem 6.1 — `QFORM-POSITIVE-MULTICOPY-LOCALIZATION-v1`

`boxed(
 sup_{mu_1,...,mu_m in D_n} F_K(mu_1,...,mu_m)
 =sup_{nu_1,...,nu_m in F_n}F_K(nu_1,...,nu_m).
)`                                                               (6.1)

#### Proof

First truncate `K_N=min(K,N)`. Approximate each `mu_j` in total variation by finite mixtures of `F_n` laws. Their tensor product is a finite convex mixture of tensors of extreme laws. Since `K_N` is bounded and nonnegative, passage to the total-variation limit is legitimate and multilinearity gives

`F_{K_N}(mu_1,...,mu_m)<=sup_{nu_1,...,nu_m in F_n}F_{K_N}(nu_1,...,nu_m)`.

Let `N->infinity` and use monotone convergence. The reverse inclusion is immediate. QED.

For an iid two-copy functional, the right side is allowed to use two different extreme laws. This distinction is essential and is not silently replaced by a same-extreme claim.

### Fejer collision corollary

For `T>0` put

`K_T(s)=int_{-T}^T (1-|t|/T)e^{its}dt
       =T [ sin(Ts/2)/(Ts/2) ]^2 >=0`.                           (6.2)

For independent copies `X,X'` with common law `mu`, and real measurable `P`,

`int_{-T}^T (1-|t|/T)|phi_P(t)|^2 dt
 =E K_T(P(X)-P(X')).`                                           (6.3)

Therefore

`boxed(
 sup_{mu in D_n} int_{-T}^T (1-|t|/T)|phi_P(t)|^2dt
 <=sup_{nu_1,nu_2 in F_n} E K_T(P(U)-P(V)).
)`                                                               (6.4)

The right side involves only compact finite-fragment product laws, with no support-radius, fragment-count or separation tax. This is directly usable before sum/difference or other copy transforms and therefore does not assume the false statement that conditioning on a conjugate sum/difference preserves density caps or independence.

This is the main new decoupling-ready localization inference of the run.

## 7. Application to a current completed Fourier branch: Hölder regularity

A compatible completed result from account03/B02 is

`yspennstate/math-open-problems@328f301cc05ac55f7dd9e3f2534890e63495470e`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T210429Z-account03-B02-qform-r15/REPORT.md`.

On its one-sided-square/rank-two-cross branch it proves

`|phi_Q(t)| <= min(1,C_0 |t|^(-1) A(t))`,                       (7.1)

where

`C_0=pi sqrt(M_R) Delta^(-1/2)`,

and

`||A||_3 <= A_0=2(2pi)^(1/3)sqrt(M_L)|d|^(-1/3)`.              (7.2)

The source used these inequalities only for an unweighted `L^1` estimate. They in fact imply a weighted moment. For every `0<alpha<1/3` and every `T>0`,

`int |t|^alpha |phi_Q(t)|dt
 <= 2 T^(alpha+1)/(alpha+1) + B_alpha T^(alpha-1/3)`,             (7.3)

where

`B_alpha=C_0 A_0 [4/(1-3alpha)]^(2/3)`.                         (7.4)

Indeed, the low-frequency term uses `|phi|<=1`. On `|t|>T`, Holder with exponents `3` and `3/2` gives

`int_{|t|>T}|t|^(alpha-1)A(t)dt
 <=||A||_3 [4/(1-3alpha)]^(2/3)T^(alpha-1/3)`.                  (7.5)

Writing `q=1/3-alpha`, optimization of (7.3) at

`T=(q B_alpha/2)^(3/4)`

gives the explicit bound

`boxed(
 int |t|^alpha |phi_Q(t)|dt
 <= [4/(3(alpha+1))]
    B_alpha^(3(1+alpha)/4)
    (q/2)^(-3q/4).
)`                                                               (7.6)

Consequently the B02 branch actually has a `C^{0,alpha}` output density for every `alpha<1/3`, with the Hölder modulus obtained from (5.3). For example at `alpha=1/6`,

`B_(1/6)=8 pi (2pi)^(1/3)(M_L M_R)^(1/2)|d|^(-1/3)Delta^(-1/2)`

and

`int |t|^(1/6)|phi_Q(t)|dt
 <=(8/7)12^(1/8) B_(1/6)^(7/8)`.                               (7.7)

This is a genuine strengthening of a live target-valid branch, not a full-target claim. The hypotheses of the B02 theorem (a nonzero physical square, one-sided isolation, and an exact rank-two physical cross block) remain essential.

## 8. What this pays and what remains unpaid

The translations/localization debt is now stronger than an interval-only reduction:

1. the exact worst-case small-ball/density constant is unchanged by reduction to compact finite-fragment extreme product laws;
2. every range-compatible affine shift is quotientable at zero cost;
3. every nonnegative weighted Fourier budget is exactly extremally localizable;
4. positive multi-copy/Fejer collision functionals used before decoupling are exactly localizable, with no fragmentwise normalization;
5. uniform weighted Fourier moments transfer quantitative continuity/Hölder regularity.

None of these facts supplies the missing universal Fourier or small-ball estimate from only `s_3(A)>=1`. Recent completed structural work leaves heavy-star/dependent-leakage branches in which a normalized linear innovation from one original-coordinate bank remains dependent on quadratic curvature carried by that same bank. The present theorems say that arbitrary support geometry is not an extra obstruction there: one may reduce the original product laws globally to finite-fragment extremes before applying a positive-copy or weighted-Fourier argument. But the dependence between the bank innovation and its same-bank quadratic leakage must still be paid honestly.

A useful next obligation is therefore:

`QFORM-STAR-DEPENDENT-LEAKAGE-POSITIVE-COPY-v1`: use the positive two-copy compiler (6.4) to prove a dimension-free Fejer/collision estimate for the remaining heavy-star configuration *before* any sum/difference conditioning, retaining the full original product provenance of the bank.

## 9. Source/status discipline


Repository retrieval was genuine, but no authenticated native brain receiver-memory use occurred, so `WITHOUT_VERIFIED_BRAIN` remains required. No scheduler mutation, new task, cross-account action, email/Drive action, notification enablement, public release, remote workflow, paid API/model/Codex call, credential use, or unrelated private transcript was used.
