SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T05:32:40Z.
attacking: close the diffuse exact-rank-two near-null-pivot branch by combining the rank-two Fresnel/Brascamp--Lieb product integral with one literal physical diagonal square through a one-dimensional mixed Strichartz estimate.

# account03/B13 r44 — one physical square completes a diffuse rank-two carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T053240Z-account03-B13-qform-r44`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW CONTINUOUS-DENSITY THEOREM FOR DIAGONAL + DIFFUSE RANK TWO; CLOSES THE NON-RANK-ONE BRANCH OF THE PARTNER DICHOTOMY / FULL QFORM OPEN**.

All random coordinates below are the original independent physical coordinates. No random-coordinate rotation, moment assumption, compact support, connected support, log-concavity, pointwise law-uniform van der Corput estimate, fiber supremum, or deletion of a coefficient-small random quadratic term is used.

## 1. Source-pinned inputs and the exact debt


The designated partner `account04/B13` supplied two completed inputs.

1. `yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T201653Z-account04-B13-extremal-slab-dichotomy-r1/REPORT.md`:
   in the diffuse exact-rank-two chamber
   \[
   A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad \max_i c_i\le1/3,\quad c_i=\|u_i\|_2^2,\qquad s_3(A)\ge1,
   \]
   there is an original coordinate `k` with \(|d_k|\ge1\), and every slab ratio
   \[
   \rho={\Pr\{X^TAX\in J\}\over |J|}
   \]
   satisfies
   \[
   |A_{kk}\det\Lambda|\le1536e^2\rho^{-4}.
   \tag{1.1}
   \]
   With
   \[
   H:=\sqrt{1536e^2}=106.534455308869\ldots,
   \tag{1.2}
   \]
   either \(|A_{kk}|\le H\rho^{-2}\) or \(|\det\Lambda|\le H\rho^{-2}\). The latter is the near-rank-one branch.

2. `yspennstate/math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T031520Z-account04-B13-diagonal-sparsification-r2/REPORT.md`:
   \[
   d_{(5)}\le C_5\rho^{-1},\qquad C_5=2\sqrt{30\pi}=19.416259125557\ldots,
   \tag{1.3}
   \]
   and the optimizer-free cap-one-product reduction is valid as a supremum identity, with bounded finite-union unit-product epsilon witnesses and no interval/diameter/fragment-count conclusion.

The first unpaid partner branch was the near-null physical pivot when the rank-two carrier is not already near rank one. The theorem below closes that branch by retaining the physical square exactly in the oscillatory integral.

## 2. Two analytic lemmas

We use the unnormalized Fourier transform
\[
\widehat g(s)=\int_{\mathbb R}g(x)e^{isx}\,dx.
\]

### Lemma 2.1 — high-power Fourier budget

If \(|g|\le1\) and \(\|g\|_1\le1\), then for every \(p\ge2\),
\[
\int_{\mathbb R}|\widehat g(s)|^p\,ds\le2\pi\sqrt{e/p}.
\tag{2.1}
\]

This is the same Babenko--Beckner/Hausdorff--Young estimate already used in the completed diffuse-frame theorem. The crucial point is that arbitrary measurable unit-modulus phases are permitted.

### Lemma 2.2 — one-dimensional parabola mixed norms

For
\[
(T_df)(t,s)=\int_{\mathbb R} f(x)e^{i(sx+dtx^2)}\,dx,
\qquad d\ne0,
\tag{2.2}
\]
and every \(q\in[2,\infty]\), put
\[
{2\over r}+{1\over q}={1\over2},\qquad r\in[4,\infty].
\tag{2.3}
\]
There is one universal finite constant \(S_*\) such that
\[
\boxed{
\|T_df\|_{L_t^rL_s^q}\le S_*|d|^{-1/r}\|f\|_2.
}
\tag{2.4}
\]
The same estimate holds with an extra phase \(e^{itbx}\), because it only translates the `s` variable by `tb` for each `t`.

#### Proof

At \((r,q)=(\infty,2)\), (2.4) is Plancherel. At \((4,\infty)\), use the standard `TT*` proof: the kernel of `T_1T_1^*` is the one-dimensional Fresnel kernel and obeys
\[
\|K_{t-\tau}*h\|_\infty\le \sqrt\pi\,|t-\tau|^{-1/2}\|h\|_1.
\]
The one-dimensional Hardy--Littlewood--Sobolev inequality maps convolution by \(|t|^{-1/2}\) from \(L^{4/3}\) to \(L^4\), giving \(L^2\to L_t^4L_s^\infty\). Mixed-norm interpolation with Plancherel gives (2.4) for the whole line (2.3), with a constant uniformly bounded between the two endpoint constants. Finally `t -> dt` gives the factor \(|d|^{-1/r}\). QED.

For cap-one mass-one densities, \(\|f\|_2\le1\).

## 3. Main theorem: one literal physical square completes diffuse rank two

### Theorem 3.1 — `QFORM-R2-ONE-PHYSICAL-SQUARE-STRICHARTZ-v1`

Let
\[
A=D+U\Lambda U^T,
\qquad U^TU=I_2,
\qquad \max_i\|u_i\|^2\le1/3,
\tag{3.1}
\]
where \(D=\operatorname{diag}(d_i)\), and \(\Lambda\) is a real symmetric invertible `2 x 2` matrix. Assume that for at least one original coordinate `k`,
\[
|d_k|\ge1.
\tag{3.2}
\]
Then for every independent cap-one product input and every deterministic affine term \(b^TX\),
\[
Y=X^TAX+b^TX
\]
has a bounded continuous density, and there is a universal finite constant \(C_{\rm sq}\) such that
\[
\boxed{
\|p_Y\|_\infty\le C_{\rm sq}\bigl(1+|\det\Lambda|^{-6/13}\bigr).
}
\tag{3.3}
\]

No support or moment regularity is imposed on the input laws.

### Proof, case `c_k>0`

Write
\[
c_i=\|u_i\|^2,
\qquad c=c_k\in(0,1/3],
\qquad q={1\over c}\in[3,\infty),
\qquad r={4\over1-2c}\in[4,12].
\tag{3.4}
\]
For fixed `t`, set
\[
G_i(t,s)=\int f_i(x)e^{it(d_ix^2+b_ix)}e^{isx}\,dx.
\tag{3.5}
\]
The rank-two Fresnel identity gives, with \(D_\Lambda=|\det\Lambda|\),
\[
|\phi_Y(t)|
\le (4\pi|t|)^{-1}D_\Lambda^{-1/2}J(t),
\tag{3.6}
\]
where
\[
J(t)=\int_{\mathbb R^2}\prod_i|G_i(t,\langle u_i,\xi\rangle)|\,d\xi.
\tag{3.7}
\]

Apply the rank-one geometric Brascamp--Lieb inequality to the Parseval decomposition
\[
\sum_i c_i\,\widehat u_i\widehat u_i^T=I_2,
\qquad \widehat u_i=u_i/\sqrt{c_i}.
\]
For every nonspecial coordinate, spend its high-power budget (2.1). Leave coordinate `k` unspent. Exactly as in the diffuse-frame proof, the scaling factors cancel for all nonspecial rows, and one obtains
\[
\boxed{
J(t)\le (2\pi\sqrt e)^{2-c}c^{-c/2}\,\|G_k(t,\cdot)\|_{L_s^{1/c}}.
}
\tag{3.8}
\]
The prefactor in (3.6)--(3.8) is uniformly bounded for \(0<c\le1/3\); indeed \(c^{-c/2}\to1\) as \(c\downarrow0\).

Lemma 2.2, `|d_k|>=1`, and `||f_k||_2<=1` give
\[
\|G_k\|_{L_t^rL_s^q}\le S_*.
\tag{3.9}
\]
For \(T\ge1\), Holder in `t` therefore yields
\[
\int_{|t|>T}|\phi_Y(t)|\,dt
\le K_*D_\Lambda^{-1/2}T^{-1/r}
\le K_*D_\Lambda^{-1/2}T^{-1/12},
\tag{3.10}
\]
where `K_*` is universal. The first exponent is exact; the second is the uniform worst case because \(r\le12\).

On \(|t|\le T\), use only \(|\phi_Y(t)|\le1\). Thus
\[
\|\phi_Y\|_1
\le2T+K_*D_\Lambda^{-1/2}T^{-1/12}.
\tag{3.11}
\]
Taking
\[
T=\max\{1,(K_*D_\Lambda^{-1/2})^{12/13}\}
\tag{3.12}
\]
gives
\[
\|\phi_Y\|_1\le C_*(1+D_\Lambda^{-6/13}).
\tag{3.13}
\]
Fourier inversion proves a bounded continuous density and (3.3).

A sharper leverage-dependent exponent is available from the first inequality in (3.10): for `c>0`, one may replace `6/13` by
\[
{2\over5-2c}\le{6\over13}.
\tag{3.14}
\]

### Proof, case `c_k=0`

Now the carrier does not involve `X_k`, so the characteristic function factors as
\[
\phi_Y(t)=g_k(t)\phi_{-k}(t),
\tag{3.15}
\]
where
\[
g_k(t)=\mathbb E e^{it(d_kX_k^2+b_kX_k)}.
\]
The same rank-two Fresnel/Brascamp--Lieb argument using all remaining rows gives
\[
|\phi_{-k}(t)|\le \pi e\,D_\Lambda^{-1/2}|t|^{-1}.
\tag{3.16}
\]
For the special square, completing the linear phase only translates before squaring; alternatively absorb the linear term by a physical-coordinate shift. The density `h` of `d_k(X_k+const)^2` obeys the standard square envelope, and
\[
\|g_k\|_3\le (2\pi)^{1/3}5^{2/3}|d_k|^{-1/3}\le (2\pi)^{1/3}5^{2/3}.
\tag{3.17}
\]
Indeed `h(y)<=|d_k y|^{-1/2}` after scaling and
\[
\int h^{3/2}\le \mathbb E|X_k+const|^{-1/2}\le5
\]
after translating the cap-one density; the bound `5` follows by splitting at distance one from the translation.

Holder with exponents `3` and `3/2` in (3.15)--(3.17) gives
\[
\int_{|t|>T}|\phi_Y(t)|dt
\le K_0D_\Lambda^{-1/2}T^{-1/3}.
\tag{3.18}
\]
Optimizing against the near-time term `2T` gives \(O(1+D_\Lambda^{-3/8})\), which is stronger than (3.3) after adjusting the universal constant. This completes the proof. QED.

## 4. Equation-level application of the designated partner result

Return to the partner's diffuse exact-rank-two target chamber with `s_3(A)>=1`. The partner provides `k` with `|d_k|>=1`, so Theorem 3.1 applies to that **same original physical coordinate**.

Consider the complement of the partner's near-rank-one alternative:
\[
D_\Lambda=|\det\Lambda|>H\rho^{-2}.
\tag{4.1}
\]
Then every slab ratio satisfies, by Theorem 3.1,
\[
\rho\le \|p_Q\|_\infty
\le C_{\rm sq}\left(1+H^{-6/13}\rho^{12/13}\right).
\tag{4.2}
\]
This inequality forces a universal upper bound on `rho`. Explicitly, if `rho>2 C_sq`, then
\[
\rho^{1/13}\le2C_{\rm sq}H^{-6/13},
\]
so
\[
\boxed{
\rho\le R_{\rm sq}:=
\max\{2C_{\rm sq},(2C_{\rm sq})^{13}H^{-6}\}<\infty.
}
\tag{4.3}
\]

### Corollary 4.1 — `QFORM-DIFFUSE-R2-NEARNULL-BRANCH-CLOSED-v1`

The near-null-pivot/non-rank-one branch in the completed account04/B13 dichotomy cannot support unbounded slab ratios. Every diffuse exact-rank-two slab witness with `rho>R_sq` must instead satisfy
\[
\boxed{|\det\Lambda|\le H\rho^{-2}.}
\tag{4.4}
\]
Equivalently, its carrier is within
\[
\boxed{10.321552950447\,\rho^{-1}}
\tag{4.5}
\]
in operator norm of a symmetric rank-one matrix.

This is the actual partner-result application: the partner dichotomy supplied both the literal large physical square and the determinant threshold; the new theorem turns the determinant-lower branch into the sublinear self-bound `rho <= const + const rho^(12/13)`.

## 5. Combining with the partner's fifth-diagonal sparsification

For `rho>R_sq`, retain the four largest physical diagonal coefficients in `D_S`. Equations (1.3), (4.4), and the singular-value formula for a symmetric `2 x 2` carrier give
\[
A=D_S+R_1+E,
\qquad \operatorname{rank}(D_S+R_1)\le5,
\tag{5.1}
\]
with
\[
\boxed{
\|E\|_{op}
\le {C_5+\sqrt H\over\rho}
={29.737812076004\ldots\over\rho}.
}
\tag{5.2}
\]
Here `R_1` is symmetric rank at most one and `E` is the sum of the remaining diagonal tail and the second carrier eigenmode. Hence, for `rho>=2(29.737813)`,
\[
s_3(D_S+R_1)\ge1/2.
\tag{5.3}
\]

This improves the surviving diffuse exact-rank-two endpoint from a rank-at-most-six core plus diagonal tail to a **rank-at-most-five physical-center-plus-one-line core** plus an `O(rho^-1)` residual. The residual is not deleted: its rank-one nonseparable part and its diagonal part remain in the phase.

## 6. Extremal-product interpretation

The partner's optimizer-free theorem transfers any strict cap-one product-law slab witness, with arbitrarily small ratio loss and unchanged `A,J`, to bounded finite-union unit-product indicators. Theorem 3.1 is already valid directly for the original cap-one laws, so in the geometric formulation it yields the same branch closure for
\[
\left|\left\{x\in\prod_iE_i:x^TAx\in J\right\}\right|/|J|,
\qquad |E_i|=1,
\]
without interval extremality, centered uniforms, a common support diameter, or a uniform fragment count.

## 7. Exact remaining implication

**Full QFORM remains OPEN / not proved / not disproved. Global continuity remains OPEN.** Continuity is proved in Theorem 3.1's exact diffuse diagonal-plus-rank-two scope.

The surviving diffuse exact-rank-two obstruction is now only the partner's near-rank-one side together with (1.3): a rank-at-most-five physical-center-plus-one-line core with an entangled operator-norm `O(rho^-1)` residual. The next B13 implication is

`QFORM-RANK1-PLUS-4DIAG-OP1OVERrho-RECEIVER-v1`:

> retain the second carrier mode and diagonal tail inside a product-preserving receiver for the rank-one-plus-four-physical-diagonal core; do not discard the `O(rho^-1)` residual as a random perturbation on arbitrary translated/fragmented supports.

## 8. Arithmetic checks

The exact constants inherited from the partner are
\[
H=106.53445530886934\ldots,
\quad \sqrt H=10.321552950446426\ldots,
\quad C_5=19.41625912555699\ldots,
\]
so
\[
C_5+\sqrt H=29.737812076003415\ldots .
\]
The exponent algebra is
\[
q=1/c,\qquad r=4/(1-2c),\qquad 4\le r\le12,
\]
\[
T^{-1/r}\le T^{-1/12}\quad(T\ge1),
\]
and balancing `T` with `D_Lambda^(-1/2) T^(-1/12)` gives `D_Lambda^(-6/13)`. Under the partner floor `D_Lambda>H rho^(-2)`, this becomes `rho^(12/13)`, strictly sublinear in `rho`.

These are deterministic analytic checks, not Monte Carlo evidence.
