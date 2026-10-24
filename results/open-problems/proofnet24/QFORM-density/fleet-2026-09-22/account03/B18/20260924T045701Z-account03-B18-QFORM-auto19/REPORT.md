# account03/B18 auto19 — uniform-center bilinear extremality and HS half-Riesz transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T045701Z-account03-B18-QFORM-auto19`  
**Role:** literature-to-proof transfer  
**Status:** `PROVED SUPPORTING LITERATURE-TO-PROOF TRANSFER / FULL QFORM OPEN`  
**Continuity:** the new transfer proves an essentially bounded density in the stated cross-plus-private-square scope. Continuity for the same scope is available independently from account03/B18 `QFORM-CROSS-SQUARE-LORENTZ-ENDPOINT-v1` at commit `3d3c43d327b37347cc67c937d4daae8d28bf433f`; it is not inferred from the new small-ball argument alone.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-24T04:57:01Z.  
attacking: replace another Rudelson--Vershynin negative-moment iteration by a different mechanism: exact concentration-function rearrangement (Juškevičius--Lee) plus Hu--Paouris tensor stochastic dominance, then transfer the resulting Hilbert--Schmidt-scale bilinear small ball estimate into a half-Riesz bound and a private-square density bound.

## 1. Scope and correction discipline

The owner target remains OPEN / NOT PROVED / NOT DISPROVED. Inputs are independent original coordinates with one-dimensional densities bounded by one; no moment, iid, centering, support, log-concavity, smoothness, or post-rotation independence is used. This report does not use the refuted arbitrary-joint coarea lemma, conditional-density-cap-as-independence, law-uniform pointwise quadratic van der Corput, fixed-good-minor inference, or deletion of a small nonzero quadratic tail.

The mechanism is deliberately different from this slot's preceding Rudelson--Vershynin stable-rank/spectral-tail runs. It uses concentration rearrangement in one factor followed by stochastic dominance of a simple tensor.

## 2. Primary-source inputs and exact hypothesis match

### 2.1 Juškevičius--Lee: concentration of sums is maximized by centered uniforms

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1. In dimension one: if independent summands `Z_j` have densities bounded by `K_j`, then for every measurable set `S`, the probability that their sum lies in `S` is at most the probability that independent centered uniforms with density `K_j` lie in the centered interval having the same Lebesgue measure as `S`.

For fixed coefficients `a_j`, `Z_j=a_jY_j` has density cap `1/|a_j|` (zero coefficients are omitted), so the extremal comparison is exactly with `a_j V_j`, where `V_j~Unif[-1/2,1/2]` are independent. No moment or regularity assumption is present.

### 2.2 Hu--Paouris: stochastic dominance and tensor small balls

X. Hu and G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192, Theorems 1.1 and 1.3 (published later in JFA 290 (2026), 111309).

Theorem 1.3: for independent random vectors whose coordinates are independent and have densities bounded by one, the simple tensor is less peaked on every symmetric convex body than the simple tensor of independent centered cube uniforms. This exactly matches the rough non-iid product inputs here.

Theorem 1.1: with their universal constants `c,C,C',C''`, for order `ell`, coordinate density cap `M0`, an `m`-dimensional tensor subspace `F`, and `0<eps<exp(-c ell)`,

`P( ||Pi_F tensor_j (X^(j)-z_j)||_2 <= (C M0)^(-ell) eps/sqrt(m) )`

is at most

`min{m, C' ell log(1/eps)} * eps/(ell-1)! * (C'' log(1/eps))^(ell-1)`.

Only the specialization `ell=2, m=1, M0=1` is used below.

## 3. Main transfer I — exact uniform-center extremality for scalar bilinear forms

### `QFORM-BILINEAR-CUBE-CONCENTRATION-DOMINANCE-v1`

Let `X in R^m` and `Y in R^n` be disjoint ORIGINAL-coordinate product banks, each coordinate having a probability density bounded by one. Let `M` be any real `m x n` matrix. Let `U,V` be independent centered cube uniforms on `[-1/2,1/2]^m` and `[-1/2,1/2]^n`. Then for every `u>=0`,

`boxed: sup_t P(|X^T M Y-t|<=u) <= P(|U^T M V|<=u).`            (3.1)

This is a genuine **uniform-in-output-center** statement, stronger than merely controlling the centered event for the original law.

### Proof

Fix `x` and put `a=M^T x`. By Juškevičius--Lee Theorem 1 applied to the independent scalar summands `a_jY_j`, for every `t`,

`P(|a^T Y-t|<=u | X=x) <= P(|a^T V|<=u).`                         (3.2)

Integrating in `x`,

`P(|X^T M Y-t|<=u) <= P(|X^T M V|<=u).`                           (3.3)

Now identify `X^T M V=<M,X tensor V>_F`. The slab

`K_u={T: |<M,T>_F|<=u}`

is symmetric and convex. Hu--Paouris Theorem 1.3 is stated for symmetric convex bodies; apply it to `K_u intersect R B_2` and let `R->infinity` by monotone convergence. It gives

`P(|X^T M V|<=u) <= P(|U^T M V'|<=u)`,                            (3.4)

where `V'` is an independent centered cube uniform. This has the same law as the right side of (3.1). No projected coordinate is ever declared independent. QED.

This also gives a narrow, source-backed interval-extremality result: **centered cube factors are extremal for the entire concentration function of a scalar bilinear form**, not merely for the event centered at zero. It must not be generalized to arbitrary quadratic forms without proof.

## 4. Main transfer II — Hilbert--Schmidt-scale uniform small ball and half-Riesz bound

Assume `M!=0` and write

`H=||M||_HS`.

Let `F=span{M/H}` in the tensor ambient space. For the centered cubes,

`||Pi_F(U tensor V)||_2=|U^T M V|/H`.

Apply Hu--Paouris Theorem 1.1 with `ell=2`, `m=1`, `M0=1`, and zero factor shifts. Since the leading minimum is at most one, for `0<eps<e^(-2c)`,

`P(|U^T M V| <= H eps/C^2) <= C'' eps log(1/eps).`                 (4.1)

Combining (3.1) and (4.1), set

`rho=e^(-2c)/C^2`, `A=C'' C^2`.

Then for every `0<u<rho H`,

`boxed: sup_t P(|X^T M Y-t|<=u)
        <= A (u/H) log(H/(C^2 u)).`                                (4.2)

For larger `u` use the trivial bound one.

Now let `B=X^T M Y`. For every `t`, layer cake gives

`E|B-t|^(-1/2)
 = (1/2) int_0^infty s^(-3/2) P(|B-t|<s) ds.`                     (4.3)

Split at `s0=rho H`. On `(0,s0)`, insert (4.2). Since

`int_0^1 y^(-1/2) dy=2`,
`int_0^1 y^(-1/2) log(1/y) dy=4`,

and `log(H/(C^2 s0))=2c`, the small-scale contribution is at most

`2 A(c+1) sqrt(rho) H^(-1/2)`.

The tail `s>=s0` contributes `rho^(-1/2) H^(-1/2)`. Therefore

`boxed: sup_t E|X^T M Y-t|^(-1/2)
        <= K_HP ||M||_HS^(-1/2),`                                  (4.4)

where the explicit source-constant combination is

`K_HP = C[ e^c + 2 C''(c+1)e^(-c) ].`                             (4.5)

This constant is universal. Hu--Paouris explicitly do not optimize their universal constants, so no unsupported numerical value is assigned to `K_HP`.

## 5. Main transfer III — private-square density bound with aggregate cross energy

### `QFORM-BILINEAR-PRIVATE-SQUARE-HS-v1`

Let `W` be another ORIGINAL coordinate, independent of the `X` and `Y` banks, with density bounded by one. For `a!=0` and arbitrary `d,c0 in R`, put

`T=X^T M Y + a W^2+dW+c0`.

Then `T` has a density and

`boxed: ||p_T||_infinity <= K_HP / sqrt(|a| ||M||_HS).`             (5.1)

### Proof

Complete the square:

`aW^2+dW = z0 + a(W+h)^2`.

The square pushforward has a density `g` satisfying, on its supported half-line,

`g(z) <= 1/sqrt(|a| |z-z0|)`.                                     (5.2)

Indeed each nonzero level has at most two preimages and the Jacobian is `2 sqrt(|a||z-z0|)`; the two input density values are each at most one.

Independence gives a density of `T` by averaging this square density against the law of `B=X^T M Y`:

`p_T(t)=E g(t-c0-B)`.

Using (5.2) and (4.4),

`p_T(t) <= |a|^(-1/2) E|t-c0-z0-B|^(-1/2)
         <= K_HP / sqrt(|a| ||M||_HS).`

Take the essential supremum. QED.

For a physical quadratic form

`Q=2 X^T C Y + aW^2`,

this becomes

`boxed: ||p_Q||_infinity <= K_HP / sqrt(2 |a| ||C||_HS).`          (5.3)

The new proof establishes essential boundedness. Continuity for this same cross-plus-private-square scope is already supplied independently by account03/B18 `QFORM-CROSS-SQUARE-LORENTZ-ENDPOINT-v1`, which gives a continuous `C_0` density with bound `16/sqrt(|a| ||2C||_op)`; hence continuity holds in this scope, but it is logically separate from the Hu--Paouris/Juškevičius--Lee transfer.

## 6. Actual application of designated partner account04/B18

The latest designated partner result read in this run is account04/B18

`QFORM-TWOSIDED-ANCHOR-PAY-OR-RANK2-COLLAR-v1`,

scientific commit `48c914d1bd070cad090d6d5deac743bd8465bc15`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.

For the packet

`A_S=[[0,C,r],[C^T,B,h],[r^T,h^T,a]]`,

with singular values `c1>=c2` of `P_r C`, it proves the actual inequality

`||p_Q||_infinity <= 2 sqrt(2 pi)/sqrt(c1 c2)`                     (6.1)

whenever `c1 c2>0`, and at the fleet gate `c1c2>=2^-12` it gives `<320.849`.

Apply both results to the literal target family

`C_N=diag(1,1/2,...,1/2)` with `N` copies of `1/2`,

`A_N=[[0,C_N,0],[C_N,0,0],[0,0,1]].`                               (6.2)

Its spectrum is

`{+1,-1,+1}` together with `N` copies each of `+1/2,-1/2`.

Hence it has **exactly three** eigenvalues of absolute value at least one. It is in the partner packet with `r=h=0`, `B=0`, `a=1`. There `c1=1`, `c2=1/2`, so (6.1) gives

`boxed: ||p_QN||_infinity <= 4 sqrt(pi)
        = 7.0898154036220635... .`                                 (6.3)

The new theorem sees

`||C_N||_HS=sqrt(1+N/4)`

and gives

`boxed: ||p_QN||_infinity
        <= K_HP/[sqrt(2) (1+N/4)^(1/4)].`                          (6.4)

Thus the actual combined inequality is

`boxed: ||p_QN||_infinity <= min{4 sqrt(pi),
        K_HP/[sqrt(2)(1+N/4)^(1/4)]}.`                             (6.5)

This is an equation-level application of the designated partner, not merely a citation. The partner controls the transverse two-anchor geometry by its two largest cross singular values; the new source transfer exposes a complementary aggregate Hilbert--Schmidt currency when a genuinely private square is available.

## 7. What this does and does not close

The full QFORM conjecture remains OPEN. The new result is not a claim that arbitrary QFORM small-ball probabilities are maximized by centered intervals/cubes. The exact extremality statement (3.1) is only for a **scalar bilinear form on two disjoint original product banks**. The private-square theorem additionally needs a genuinely disjoint original coordinate `W`.

The new mechanism does close a concrete implication needed by several local compilers: whenever a surviving packet can be represented as a bilinear cross bank plus a disjoint physical square, aggregate cross energy `||M||_HS` supplies a dimension-free half-Riesz smoother without any stable-rank assumption. It also gives a uniform-output-center bilinear small-ball theorem, avoiding the usual defect that tensor small-ball theorems are naturally centered at zero.

The remaining global implication is structural: bare `s_3(A)>=1` need not furnish a disjoint private square plus a clean bilinear bank. In the latest account04/B18 funnel, the genuinely unpaid geometry is still a near-rank-two cross carrier with arbitrary same-side curvature, or an exact rank-one carrier whose complement-active dimension is at least three. The tensor/Rogozin transfer may be useful there only if that curvature can be source-separated without violating the live conditional-dependence corrections.

## 8. Source pins

Primary sources:

- T. Juškevičius, J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1.
- X. Hu, G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192, Theorems 1.1 and 1.3; J. Funct. Anal. 290 (2026), 111309.

Fleet sources actually used:

- designated partner account04/B18: `yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`;
- continuity supplement account03/B18: `yspennstate/math-open-problems@3d3c43d327b37347cc67c937d4daae8d28bf433f`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T030202Z-account03-B18-QFORM-auto17/CHECK.json` and sibling report.

Fresh prepublication brain control commit: `293626f938153424f19b485e0dfa58228a0193e7`; OWNER CONTROL revision `2026-09-22.15`. Full conjecture status remains OPEN.