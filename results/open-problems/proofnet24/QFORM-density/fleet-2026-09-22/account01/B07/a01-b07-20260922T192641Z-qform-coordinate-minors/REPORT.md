SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-22T19:26:41Z.
attacking: replace single-minor inversion by a projection-Plancherel payment for an entire rectangular coordinate-minor bank.

# account01/B07 — projection-Plancherel payment for rectangular coordinate-minor banks

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `a01-b07-20260922T192641Z-qform-coordinate-minors`  
**Assignment:** coordinate minor selection  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, fresh control, and corrections

The target is unchanged: for independent real `X_i` with densities `0<=f_i<=1` and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately.

The pre-publication control refresh reached `yspennstate/math-research-brain@1fbdb5a35599eecac8fca5ea351df896aad3b319`, OWNER CONTROL revision `2026-09-22.14`. QFORM remains the sole target and there is no stop. Revision `.14` promotes a joint integrated-characteristic-function route, while still forbidding the false one-coordinate pointwise van-der-Corput shortcut.

The consolidated current-research file still marks the full conjecture OPEN and keeps the following corrections live. This report does not use any of the invalid interfaces:

* law-uniform pointwise quadratic-phase decay is false;
* arbitrary-joint rank-three coarea with only a joint density cap is false;
* positive moments of conditional projection-density caps can diverge;
* post-rotation independence is false;
* a single nonsingular `2x2` cross minor is insufficient;
* one uniformly good fixed principal/cross minor is not forced by the spectral hypothesis.

The mechanism below is materially different from my preceding finite-heavy-core/DPP factorization runs: it works directly at the conditional characteristic function and uses `L^2` Plancherel plus a product-preserving projection-density theorem.

## 2. Source-pinned completed inputs actually used

### Assigned partner: account02/B07

I read the complete proof of account02/B07 `QFORM-DISJOINT-CROSS-PLANCHEREL-v1` at

`yspennstate/math-open-problems@dbf85b8f59fcbb22d4599b7cba9edd97d9ffa83f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T180412Z-b07-afd8d7/REPORT.md`.

For disjoint physical banks `I,J` with `|I|=|J|=m>=3` and invertible `C=A[I,J]`, it proves

`||p_Q||_infinity <= [m/(m-2)] |det C|^(-1/m)`

with a continuous density, while allowing arbitrary self blocks, outside couplings, affine terms, signs and additional spectrum. Its proof is a conditional `L^2` Plancherel estimate.

### Product projection input: account02/B06

I also read the complete proof of account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `R` has `k` orthonormal columns and `Y=R^T X`, then the physical product law gives

`||p_Y||_infinity <= product_i (1-ell_i)^(-(1-ell_i)/2) <= exp(k/2)`

with `ell_i` the row leverages of `R`. This is a genuine weighted fiber integral; it is not the refuted unrestricted fiber-supremum bound.

The new proof below applies the assigned partner's Plancherel mechanism with this projection result on one or both sides. The combination is the key new step.

## 3. Main theorem: arbitrary physical banks, exact cross rank

Let `I,J` be disjoint sets of original coordinates. Put

`C=A[I,J]`, `rank(C)=r>=3`.

Let `s_1,...,s_r>0` be the nonzero singular values of `C`, and define

`Delta_r(C) := product_{nu=1}^r s_nu^2 = pdet(CC^T)`.

### Theorem 3.1 — `QFORM-PROJECTION-CROSS-PLANCHEREL-v1`

For arbitrary values of every other entry of the symmetric matrix `A`, and arbitrary independent input laws with densities at most one, the full quadratic form `Q=X^TAX` has a **continuous** density satisfying

`boxed: ||p_Q||_infinity <= e * [r/(r-2)] * Delta_r(C)^(-1/(2r)).`      (3.1)

If one side has exactly `r` physical coordinates, i.e. `|I|=r` or `|J|=r`, then the factor `e` improves to `sqrt(e)`:

`boxed: ||p_Q||_infinity <= sqrt(e) * [r/(r-2)] * Delta_r(C)^(-1/(2r)).` (3.2)

If both sides have exactly `r` coordinates, then the factor improves to `1`; this exactly recovers the assigned partner theorem:

`||p_Q||_infinity <= [r/(r-2)] |det C|^(-1/r).`                       (3.3)

No moments, support, sign, definiteness, diagonal-basis assumption, or independence after rotation is used.

### Proof

Condition on all original coordinates outside `I union J`. This preserves independence inside the two selected physical banks. For fixed outside value `z`, write `x=X_I`, `y=X_J`. The conditional phase is

`q_z(x,y)=x^T P x + 2 x^T C y + y^T R y + alpha_z dot x + beta_z dot y + d_z`,

where `P,R` are arbitrary symmetric matrices.

Take the compact singular-value decomposition

`C=U Sigma V^T`,

where `U in R^(|I| x r)` and `V in R^(|J| x r)` have orthonormal columns and `Sigma=diag(s_1,...,s_r)`.

For fixed real `t`, absorb all self-quadratic and affine terms into the complex amplitudes

`h_t(x)=f_I(x) exp(i t[x^T P x+alpha_z dot x])`,
`g_t(y)=f_J(y) exp(i t[y^T R y+beta_z dot y])`.

Push the complex measures `h_t(x)dx` and `g_t(y)dy` forward under `U^T` and `V^T`, and denote the resulting complex densities by `H_t(xi)` and `G_t(eta)`. Pointwise,

`|H_t(xi)| <= rho_U(xi)`, `|G_t(eta)| <= rho_V(eta)`,                 (3.4)

where `rho_U,rho_V` are the ordinary densities of `U^T X_I`, `V^T X_J`. The account02/B06 projection theorem gives

`||rho_U||_infinity, ||rho_V||_infinity <= e^(r/2)`.                 (3.5)

Each is a probability density, so

`||H_t||_2 <= ||rho_U||_2 <= e^(r/4)`,
`||G_t||_2 <= ||rho_V||_2 <= e^(r/4)`.                               (3.6)

This is the step that replaces selecting one physical coordinate minor. It retains the whole product-law projection.

Using the Fourier convention `hat H(omega)=int exp(-i omega dot xi) H(xi) dxi`, the conditional characteristic function, up to the irrelevant factor `exp(it d_z)`, is

`phi_z(t)=int int H_t(xi) G_t(eta) exp(i 2t xi^T Sigma eta) dxi deta`

`          =int G_t(eta) hat H_t(-2t Sigma eta) deta`.                (3.7)

Cauchy--Schwarz, the invertible change of variables `omega=-2t Sigma eta`, and Plancherel yield, for `t!=0`,

`|phi_z(t)|
 <= ||G_t||_2 (2|t|)^(-r/2) (det Sigma)^(-1/2) ||hat H_t||_2`
` =  pi^(r/2) (det Sigma)^(-1/2) |t|^(-r/2) ||H_t||_2 ||G_t||_2`
` <= pi^(r/2) e^(r/2) Delta_r(C)^(-1/4) |t|^(-r/2).`                 (3.8)

The bound is uniform in the outside conditioning, hence

`|phi_Q(t)| <= min(1, a |t|^(-r/2))`,
`a=pi^(r/2)e^(r/2)Delta_r(C)^(-1/4)`.                                 (3.9)

For `r>2`,

`int_R min(1,a|t|^(-r/2)) dt
 =2 a^(2/r) r/(r-2).`                                                  (3.10)

Because `a^(2/r)=pi e Delta_r(C)^(-1/(2r))`, Fourier inversion gives (3.1).

If `|I|=r`, then `U` is a square orthogonal matrix and the pushed complex amplitude has the exact `L^2` norm

`||H_t||_2=||h_t||_2=||f_I||_2<=1`,                                  (3.11)

instead of `e^(r/4)`. Thus (3.8) loses only one factor `e^(r/4)`, which becomes `sqrt(e)` after taking the `2/r` power. This proves (3.2); the same applies if `|J|=r`. If both banks have size `r`, both projected `L^2` norms are at most one and (3.3) follows, recovering the partner theorem exactly.

Finally, the majorant (3.9) is in `L^1`. Therefore the unconditional characteristic function is integrable, and Fourier inversion gives a bounded continuous density (indeed one vanishing at infinity). QED.

## 4. Coordinate-minor corollary: a whole rectangular third-minor bank is payable

The assignment asks not to invert one tiny coordinate minor. The most useful `r=3` one-sided consequence is exact.

Fix a **physical row triple** `I`, let `J` be any disjoint physical coordinate bank, and set `C=A[I,J]`. If `C` has row rank three, then by Cauchy--Binet

`Delta_I(J):=det(CC^T)
 = sum_{K subset J, |K|=3} det A[I,K]^2`.                              (4.1)

Hence Theorem 3.1 gives

`boxed: ||p_Q||_infinity <= 3 sqrt(e) Delta_I(J)^(-1/6).`             (4.2)

Thus all column triples are aggregated **before** reciprocal payment. A single tiny `det A[I,K]` is harmless as long as the total squared determinant bank (4.1) is large.

There is a symmetric statement with one physical column triple and an arbitrary row bank.

If an arbitrary physical cut `S,S^c` has `rank A[S,S^c]=3`, then

`E_3(A[S,S^c])
 =e_3(A[S,S^c]A[S,S^c]^T)
 =Delta_3(A[S,S^c])`,                                                 (4.3)

so the fully two-sided aggregate bank satisfies

`boxed: ||p_Q||_infinity <= 3 e E_3(A[S,S^c])^(-1/6).`                (4.4)

This is the exact-rank-three aggregate-before-inversion estimate missing from my earlier regularized-determinant result: it has **no coordinate-leverage hypothesis**.

## 5. Actual application to the earlier determinant-weighted Pluecker invariant

My earlier report `QFORM-AGGREGATE-CROSSMINOR-DETERMINANT-v1`, source-pinned at

`yspennstate/math-open-problems@22acf813ef825872ffe594818d6adb27e9d4e41f`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/a01-b07-20260922T134418Z-qform-r11/REPORT.md`,

applied the designated account02/B07 disjoint-basis invariant. For an exact-rank-three matrix

`A=U Lambda U^T`, `U^T U=I_3`,

with Pluecker weights `w_K=det(U_K)^2` and

`delta=sum_{K cap L=empty} w_K w_L`,

a uniform coordinate cut obeys exactly

`E_S E_3(A[S,S^c]) = |det Lambda|^2 delta /64`.                       (5.1)

So some cut has

`E_3(A[S,S^c]) >= |det Lambda|^2 delta/64`.                            (5.2)

The previous report could use this only when the same cut passed a `q=1` leverage gate. That gate is now unnecessary: because the full matrix has exact rank three, the selected cross block has rank at most three, and (5.2)>0 forces rank exactly three. Applying (4.4) gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <= 6 e |det Lambda|^(-1/3) delta^(-1/6).`                            (5.3)

This is continuous-density control on the positive-`delta` exact-rank-three branch, and it preserves the original physical product law. It does not use the refuted arbitrary-joint coarea lemma.

At the concrete threshold `delta>=1/8` and `|det Lambda|>=1`, (5.3) is `<23.066`. The older account02/B07 entropy theorem is numerically sharper on its own separable-residual scope (`<=6e` at this threshold); the point of (5.3) is the new **arbitrary-self-block Plancherel interface** and the removal of the leverage gate from the cross-minor route.

As a stress check, the six-coordinate paired frame from my earlier report has `delta=1/8` and every rank-three split has `E_3=1/64` while all fixed-cut range leverages equal one. The old regularized `q=1` route failed on every such cut. The present rank-three cross-Plancherel theorem applies anyway; for the balanced `3x3` split it uses the stronger two-square-side constant and gives `||p_Q||_infinity<=6`. This confirms that the former leverage obstruction was an artifact of that proof interface, not of the target law.

## 6. What this does and does not close

### Newly paid

1. Any physical cross block of exact rank `r>=3` is paid by its full pseudodeterminant, with arbitrary self blocks and outside couplings.
2. A fixed physical row triple is paid by the **entire** determinant-weighted column-minor bank `sum_K det A[I,K]^2`; no column triple needs to be selected.
3. Any rank-three physical cut is paid by the full two-sided aggregate third-minor mass `E_3` with no leverage condition.
4. The previous exact-rank-three Pluecker/cut inequality (5.1) now directly gives (5.3).

### Still open

The three-large-eigenvalue hypothesis does not force a single row triple with `Delta_I(J)>=c`, nor does it force a rank-three cross cut in a general higher-rank matrix. The live singleton-plus-two-banks and diffuse examples rule out such a fixed-minor shortcut. If `rank C>3`, Theorem 3.1 pays the product of **all** nonzero singular values of `C`; that pseudodeterminant can be tiny even when the third-compound mass `E_3(C)` is large. Therefore (3.1) cannot simply replace `Delta_r` by `E_3` for arbitrary high-rank `C`.

The next precise implication is therefore

**`QFORM-ROW-PACKET-PROJECTION-PAYMENT-v1` (OPEN):** starting from the finite-heavy-core / third-compound packet already obtained in the B07 structural reductions, convert a determinant-weighted family of physical row triples into either

* one row triple `I` whose full rectangular bank `det(A[I,J]A[I,J]^T)` is dimension-free large and hence paid by (4.2), or
* a genuinely mixture-level projection/Plancherel estimate that sums the row-triple determinant weights before reciprocal inversion.

Only the **row** dispersion remains in (4.2); the entire column dispersion has been removed. In the `h=2` bordered-minor branch this still has to be combined with the division-free polynomial bank rather than a Schur denominator.

A second formulation is the high-rank gap: find a product-preserving way to extract three singular directions from a high-rank cross block while routing the remaining cross interaction, or prove an integrated determinant estimate using `E_3(C)` directly. Simply dropping the residual cross interaction is not valid because it is a two-sided nonseparable phase.

## 7. Conditional end-to-end route after this run

A compact route to the full theorem is now:

1. use the existing third-compound/finite-heavy structural reduction to obtain a constant determinant-weighted third-order physical packet;
2. whenever that packet is carried by a rank-three cut, apply (4.4) immediately;
3. whenever it pins a physical row triple, aggregate **all** column triples by (4.1) and apply (4.2);
4. pay the remaining spread-over-row-triples case by a mixture-level row mechanism (or route it into the already completed pair/rank-two branches);
5. combine O0/O1/O2/O3 packet payments. All signs, extra spectrum and arbitrary cap-one product laws remain present throughout.

The first missing implication is step 4, now strictly narrower than the prior two-sided minor-selection problem.

## 8. Status

* `QFORM-PROJECTION-CROSS-PLANCHEREL-v1`: **PROVED SUPPORTING THEOREM**.
* `QFORM-RECTANGULAR-THIRD-MINOR-BANK-v1` (equation (4.2)): **PROVED SUPPORTING COROLLARY**.
* Exact-rank-three Pluecker positive-`delta` cross-cut branch: **PAID by (5.3)**; no leverage gate.
* Full QFORM conjecture: **OPEN / neither proved nor disproved**.
* Full continuity: **OPEN**. Continuity is proved only on the scoped branches covered by Theorem 3.1.
