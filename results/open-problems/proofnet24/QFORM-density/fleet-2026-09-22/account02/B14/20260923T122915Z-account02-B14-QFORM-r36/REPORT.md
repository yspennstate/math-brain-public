SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T12:29:15Z.
attacking: full-target extreme localization and random-coefficient pair smoothing — identify the exact zero-loss localization of the entire small-ball target, and separate it from analytic certificates that are not fragment-uniform.

# account02/B14 r36 — exact full-target localization and a Fourier-tail obstruction inside the extreme class

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T122915Z-account02-B14-QFORM-r36`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM + SOURCE-VALID PROOF-INTERFACE OBSTRUCTION / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and sources actually used

The target is unchanged: for every finite `n`, independent real coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, centering, identical-law, log-concavity, diagonal-coordinate, or post-rotation independence assumption is added.

Fresh brain control was resolved on `main`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no pause on account02/B14. The live corrections excluding pointwise law-uniform quadratic-phase decay, post-rotation independence, bounded-diameter localization, fixed fragment-count localization, arbitrary-joint rank-three coarea, and worst normalized spectral fibers remain in force.

Two completed designated-partner results are used at equations below:

1. account03/B14 r34, `QFORM-SINGULAR-FUNCTIONAL-EXTREME-LOCALIZATION-v1`, canonical source
   `yspennstate/math-open-problems@5b60b66568f5be5eb2375597ae1acb866c68f5f8`, which gives exact extreme-product localization for **every nonnegative Borel functional**, including unbounded singular kernels;
2. newest compatible account03/B14 r35, `QFORM-SQRT-CRITICAL-BUDGET-MIXTURE-v1`, canonical source
   `yspennstate/math-open-problems@29096949260b7ec2e9659c1379bd0a0882a37387`, which turns conditional critical Fourier constants `K(theta)` into the optimized physical-pair bound through `E sqrt(K)`.

The required Claude source is used from
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. In particular, `COUNTEREXAMPLE_SEARCH.md` proves Theorem A: when **all** eigenvalues of an `n`-dimensional quadratic part have modulus at least `sigma`, with arbitrary linear terms,

`||p_Q||_infinity <= (n/sigma) (d/(d-1)) kappa_d^(1/d)`, `d=n-1`.

`FOURIER_ROUTE_REPORT.md` also proves the whole-law fifth-volume exit

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`

for any disjoint original-coordinate cross block `M` with positive fifth volume, with no marginal gate.

## 2. First unpaid implication, stated early

`QFORM-EXTREME-LOCALIZE-THEN-WHOLE-ACTIVE-CERTIFICATE-v1`:

> It is legitimate, with **exactly zero loss in the final universal constant**, to restrict the full QFORM small-ball supremum to product laws whose marginals are indicators of arbitrary compact finite unions of intervals of total length one. It is **not** legitimate to infer that a chosen Fourier/reciprocal certificate is then uniform over those extreme laws. After localization one still must pay a whole-active volume/ridge/random-slope/fractional-trace certificate before normalizing or charging individual active fragments.

Sections 3 and 5 prove both halves.

## 3. Exact full-target extreme localization

For fixed finite `n`, let `D_n` be all product probability laws

`dmu(x)=prod_i f_i(x_i) dx`, `0<=f_i<=1`, `int f_i=1`,

and let `F_n` be the subclass with

`f_i=1_{E_i}`,

where every `E_i` is a compact finite union of intervals and `|E_i|=1`. No common bound is imposed on the number, diameter, location, or separation of the components.

For a measurable `P:R^n->R`, define the extended small-ball density functional

`Lambda(P,mu)=sup_{t in R, h>0} h^(-1) mu{t<=P<t+h}`.            (3.1)

### Theorem 3.1 — `QFORM-FULL-SMALLBALL-EXTREME-LOCALIZATION-v1`

For every measurable `P`,

`boxed: sup_{mu in D_n} Lambda(P,mu) = sup_{nu in F_n} Lambda(P,nu).` (3.2)

Consequently, if `P_{A,b,c}(x)=x^T A x+b^T x+c`, then the exact extended universal constant

`C_* = sup_n sup_{A:s_3(A)>=1} sup_{b,c} sup_{mu in D_n} Lambda(P_{A,b,c},mu)`   (3.3)

is unchanged when `D_n` is replaced by `F_n` for every `n`.

#### Proof

Fix `t,h` and set the nonnegative bounded Borel kernel

`G_{t,h}(x)=h^(-1) 1_{[t,t+h)}(P(x))`.                           (3.4)

Partner r34 applies to every nonnegative Borel kernel and yields

`sup_{mu in D_n} int G_{t,h} dmu = sup_{nu in F_n} int G_{t,h} dnu`. (3.5)

Now commute two ordinary suprema:

`sup_{mu in D_n} Lambda(P,mu)
 = sup_mu sup_{t,h} int G_{t,h} dmu
 = sup_{t,h} sup_mu int G_{t,h} dmu
 = sup_{t,h} sup_{nu in F_n} int G_{t,h} dnu
 = sup_{nu in F_n} Lambda(P,nu).`                               (3.6)

Taking further suprema in `(n,A,b,c)` gives (3.3) with no change in constant. QED.

### Density interpretation

If the common value in (3.2) is finite, every interval `I` satisfies `mu(P in I)<=C|I|`. By countable interval covers the output measure is absolutely continuous with respect to Lebesgue measure, and Lebesgue differentiation gives an essential density bound `<=C`. Conversely a density cap `C` gives the interval inequality. Therefore the owner's **essential bounded-density target is exactly equivalent**, with the same optimal universal constant, to the same target on `F_n`.

A failure of the full theorem likewise yields a sequence of compact finite-fragment extreme laws with small-ball ratios tending to infinity. The theorem does not assert a single extremizer, a fixed fragment count, a common compact set, or attainment of the global supremum.

## 4. A useful global power form of the completed pair-log bound

An earlier source-pinned B14 pair-log compiler gives, for an actual original-coordinate invertible indefinite pair `B`,

`D=|det B|`, `kappa=sigma_min(B)`,

and a completed scalar remainder having density cap `H`, the piecewise estimate

`C_log = 6 [H/(kappa sqrt(D))]^(1/3)` below the transition,        (4.1)

and

`C_log = D^(-1/2) [3+2 log theta]`,
`theta=2 sqrt(2 D H/kappa)`,                                     (4.2)

above it.

The same cubic-root expression actually dominates both branches:

`boxed: C_log(D,kappa,H) <= 6 [H/(kappa sqrt(D))]^(1/3)` for all `H>0`. (4.3)

Indeed, only the upper branch needs checking. Put `u=theta^(2/3)>=1`. Then the right side of (4.3) equals `3u/sqrt(D)`, while (4.2) is `(3+3 log u)/sqrt(D)`, and `1+log u<=u`.

As a translation-uniform corollary, if after pair completion and conditioning on outside original coordinates

`R=rho(Z)+2(gamma Z+beta)V`,                                     (4.4)

where `Z,V` are independent cap-one original coordinates, `rho` is any measurable same-bank remainder and `gamma!=0`, then conditional on `Z=z`, except at one null fiber,

`H(z)<=1/[2|gamma z+beta|]`.                                     (4.5)

Thus

`||p_Q||_infinity
 <=6 (2 kappa sqrt(D))^(-1/3) E|gamma Z+beta|^(-1/3).`            (4.6)

The variable `gamma Z+beta` has density cap `1/|gamma|`. Symmetric decreasing rearrangement of `|x|^(-1/3)` gives

`E|gamma Z+beta|^(-1/3)
 <= (1/|gamma|) int_{-|gamma|/2}^{|gamma|/2} |u|^(-1/3) du
 =3*2^(-2/3)|gamma|^(-1/3).`                                    (4.7)

Therefore

`boxed: ||p_Q||_infinity <= 9 [kappa sqrt(D)|gamma|]^(-1/3).`     (4.8)

No support radius, moment, location, or translation parameter appears. This corollary is an independent pair-log benchmark; the previously completed physical-space random-slope compiler is numerically stronger in some zero-self cases.

## 5. Extreme localization does not uniformize critical Fourier tails

The exact theorem in Section 3 must not be confused with a uniform analytic estimate on every member of `F_n`.

For `T>=2`, take an integer `N>=T^2` and define the compact finite-fragment unit set

`E_{T,N}= union_{k=1}^N [2 pi k/T -1/(2N), 2 pi k/T +1/(2N)]`.    (5.1)

Its components are disjoint and total length is one. Let `V_T` have density `1_{E_{T,N}}`. Writing `sinc(x)=sin(x)/x`, direct integration at the resonant frequency gives

`phi_{V_T}(T)
 = N * [2 sin(T/(2N))/T]
 = sinc(T/(2N)).`                                                 (5.2)

Since `T/(2N)<=1/4`,

`|phi_{V_T}(T)| >= c_0 := sinc(1/4)>0.98`.                       (5.3)

Hence the smallest possible critical linear-Fourier constant

`K_T^* := sup_{s!=0} |s| |phi_{V_T}(s)|`                         (5.4)

satisfies

`boxed: K_T^* >= c_0 T -> infinity.`                             (5.5)

Thus compact finite-fragment extreme localization does **not** imply a law-uniform `K/|t|` characteristic-function tail.

### Target-valid stress form and the newest partner r35

Let `U_1,U_2,Z` be independent Uniform`[-1/2,1/2]`, independent of `V_T`, and consider

`Q_T=2U_1U_2+2ZV_T`.                                             (5.6)

The homogeneous matrix is the direct sum of two hyperbolic blocks `[[0,1],[1,0]]`, so its eigenvalues are `{1,-1,1,-1}`. Every law in (5.6) belongs to the compact finite-fragment extreme class from Section 3; this is inside the exact owner target.

Use `(U_1,U_2)` as the physical pair, so `D=kappa=1`, and condition on `Z=z`. The residual characteristic function is

`phi_{R_z}(t)=phi_{V_T}(2zt)`.                                   (5.7)

Consequently the **minimal** r35 critical constant is

`K(z)=K_T^*/(2|z|)`                                              (5.8)

for `z!=0`. The exceptional fiber has probability zero. Since

`E|Z|^(-1/2)=2 sqrt(2)`,

partner r35's square-root budget is exactly

`b_T=E sqrt(K(Z))=2 sqrt(K_T^*)`,                                (5.9)

so its optimized certificate is `F_{1,1}(4K_T^*)`.

This certificate necessarily diverges with `T`. Indeed for `K>=1`, in

`F_{1,1}(K)=inf_{y>0}[4 sqrt(K/y)+Omega(y)]`,                     (5.10)

if `y<=sqrt(K)` the first term is at least `4K^(1/4)`; if `y>=sqrt(K)`, then `y>=1` and

`Omega(y)=log y+2c_E >= (1/2)log K+2c_E`.                        (5.11)

Therefore

`F_{1,1}(K) >= min{4K^(1/4), (1/2)log K+2c_E} -> infinity`,       (5.12)

and by (5.5) the black-box r35 Fourier-tail route applied after extreme localization has no universal numerical constant on this family.

### Why this is only a proof-interface obstruction

The true output densities are uniformly bounded. Apply Claude's proved Theorem A from the required `COUNTEREXAMPLE_SEARCH.md` to the four-dimensional quadratic part in (5.6). All four eigenvalues have modulus one, so with `n=4`, `d=3`, `sigma=1`,

`boxed: ||p_{Q_T}||_infinity <= 6 kappa_3^(1/3)`,                 (5.13)

independently of `T`, `N`, and fragment separation. (The previously completed B14 physical-space random-slope theorem also gives a uniform constant.)

Thus (5.5)-(5.13) prove `QFORM-EXTREME-CLASS-CRITICAL-FOURIER-BARRIER-v1`: **exact target-level extreme localization is valid, but paying a critical pointwise Fourier tail separately on each localized active law is not a universal proof route.** The failure is in that analytic interface, not in QFORM and not in partner r35.

## 6. Required Claude whole-law volume result is compatible with the localization theorem

There is a positive contrast. Let `M=A_{I,J}` be any disjoint original-coordinate cross block and `Z_5=e_5(M^TM)>0`. Claude's proved `D_5` theorem gives for every admissible product law, with arbitrary self blocks and affine terms,

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10).`                    (6.1)

By Theorem 3.1 the left-hand worst-law constant is exactly the same after restricting every marginal to compact finite-fragment indicators. Therefore (6.1) transfers through the extreme localization with **zero** fragment tax. This illustrates the safe order:

`whole-active analytic certificate -> optional outside localization/mixture`,

not

`active fragmentation -> normalize/estimate each fragment -> reciprocal/Fourier payment`.

## 7. What changed and what remains

New in this run:

- the partner singular-functional theorem is promoted to an **exact full QFORM small-ball localization principle**, not merely a fixed fractional-trace corollary;
- the full universal essential density constant is proved unchanged on compact finite-fragment extreme product laws, with no fixed fragment count or bounded diameter;
- a resonant compact finite-fragment family proves that this localization does not make critical Fourier-tail constants uniform;
- newest partner r35 is applied quantitatively to show its critical-tail certificate diverges on that family, while Claude Theorem A proves the true exact-target output remains uniformly bounded;
- Claude `D_5` is identified as a compatible whole-law certificate that survives the localization exactly.

The full conjecture remains open. The first structural debt is now sharper: in each surviving no-pivot/N3 state, after reducing input laws if useful to arbitrary compact finite-fragment extremes, one must still expose **before active normalization** either a whole-law D'/D5/ridge/mixed-hub/grouped-bank certificate, a protected original-coordinate slope/Schur direction, or a fractional-trace/positive-copy estimate whose subprobability homogeneity carries a full mass power through reciprocal payment. A fixed support diameter, fixed fragment count, pointwise law-uniform Fourier decay, or post-rotation independence cannot replace this step.

## 8. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- Essential boundedness only in the supporting branches above; full-target continuity remains separate.
- All conditioning is on original coordinates; no spectral rotation is declared independent.
- No moment or support assumption is used.
- `E_{T,N}` is compact finite-fragment and has total measure exactly one; it is a legal density cap-one extreme law.
- The diverging r35 certificate is explicitly a proof-mechanism obstruction, not a lower bound on `||p_{Q_T}||_infinity`.
- Repository transport is not verified native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
- Model self-report: `GPT-5.6 Sol`; reasoning/configured effort and provider thinking telemetry: `UNKNOWN / not exposed`.
