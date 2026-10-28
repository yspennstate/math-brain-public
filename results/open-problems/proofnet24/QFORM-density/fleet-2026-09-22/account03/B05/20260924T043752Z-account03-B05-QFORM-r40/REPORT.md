SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T04:37:52Z.
attacking: QFORM-WITT-CROSSSTAR-AGGREGATE-COAREA-v1 — aggregate the pairwise Pluecker tube before reciprocal minor selection, and pay a nontrivial grouped-bank endpoint.

# account03/B05 r40 — cross-star currency decomposition and grouped-bank coarea endpoint

**Programme:** QFORM-DENSITY-3EIG-20260922.  
**Role:** quadratic coarea / equivalent interval bounds, preserving arbitrary product densities.  
**Status:** supporting theorem only; full QFORM OPEN / NOT PROVED / NOT DISPROVED.  
**Regularity:** the new grouped endpoint proves absolute continuity and an essential L-infinity bound; continuity is not claimed.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Exact live Witt packet

Use the current account01/B05 near-coloop Witt form

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,
\tag{1.1}
\]

where `H` is a literal original coordinate independent of the residual product bank, `U,V,W` are coefficient projections of that bank, `a delta !=0`, and the determinant-star currency is

\[
S_i=a^2|\delta|.
\tag{1.2}
\]

In the target-normalized survivor of that reduction, `S_i>=1/2`. Completing the transverse square, set

\[
W^\sharp=W+\frac{\gamma}{\delta}V,
\qquad
A=\alpha-\frac{\gamma^2}{\delta},
\tag{1.3}
\]

so

\[
Q=2aVH+2a\kappa UV+AV^2+\delta (W^\sharp)^2.
\tag{1.4}
\]

Let `v,u,z` denote the coefficient vectors of `V,U,W^sharp`. Since `z=w+(gamma/delta)v`, all Pluecker coefficients in the `(V,W)` plane are unchanged:

\[
v_jz_k-v_kz_j=v_jw_k-v_kw_j.
\tag{1.5}
\]

The preceding account01/B05 run proved a pairwise Borel tube with a reciprocal individual Pluecker coefficient, and exhibited a target-valid Walsh family where every individual coefficient is tiny although their aggregate square mass is one. Thus pair-first inversion cannot be the final interface.

## 2. Exact cross-star decomposition before pair selection

Fix any partition of the residual original coordinates into two disjoint banks `J sqcup K`. Put

\[
s=\|v_J\|_2^2,
\qquad
t=\|z_J\|_2^2,
\qquad c=\langle v_J,z_J\rangle.
\tag{2.1}
\]

Because replacing `w` by `z=w+(gamma/delta)v` does not change the wedge but does change norms, it is cleaner for the Pluecker identity to use the original orthonormal pair `(v,w)`. Thus in (2.1)-(2.8) below temporarily read `z=w`, so `||v||=||w||=1` and `<v,w>=0`. Then

\[
\|v_K\|^2=1-s,
\quad
\|w_K\|^2=1-t,
\quad
\langle v_K,w_K\rangle=-c.
\tag{2.2}
\]

Define the cross-star mass

\[
M_{J,K}:=\sum_{j\in J,k\in K}(v_jw_k-v_kw_j)^2.
\tag{2.3}
\]

A direct expansion gives the first exact identity

\[
\boxed{M_{J,K}=s(1-t)+(1-s)t+2c^2.}
\tag{2.4}
\]

Assume `0<s<1` and define the within-bank regression residual energies

\[
d_J=t-\frac{c^2}{s},
\qquad
d_K=(1-t)-\frac{c^2}{1-s},
\tag{2.5}
\]

and the two bank slopes

\[
\alpha_J=\frac{c}{s},
\qquad
\alpha_K=-\frac{c}{1-s}.
\tag{2.6}
\]

Cauchy-Schwarz gives `d_J,d_K>=0`. Substitution into (2.4) yields the exact three-currency decomposition

\[
\boxed{
M_{J,K}
=(1-s)d_J+s d_K+s(1-s)(\alpha_J-\alpha_K)^2.
}
\tag{2.7}
\]

Equivalently, with `G_J,G_K` the two Gram matrices of `(v,w)` restricted to each bank,

\[
M_{J,K}
=\frac{1-s}{s}\det G_J
+\frac{s}{1-s}\det G_K
+\frac{c^2}{s(1-s)}.
\tag{2.8}
\]

This decomposition is useful because the completed account02/B05 max-cut theorem gives a partition with `M_{J,K}>=1/2`. Therefore, for such a cut, at least one of the three nonnegative terms in (2.7) is at least `1/6`.

The boundary cases are explicit: if `s=0`, then `c=0` and `M_{J,K}=t`; if `s=1`, then `c=0` and `M_{J,K}=1-t`. Thus no hidden division by zero is needed.

### Interpretation

The first two currencies are genuine within-bank transverse curvature. The third currency is different: each bank may be exactly rank one in the `(v,w)` plane, but with different slopes. In the Walsh stress geometry `w_J=v_J`, `w_K=-v_K`, and `||v_J||^2=||v_K||^2=1/2`; then

\[
d_J=d_K=0,
\qquad
\alpha_J=1,
\quad\alpha_K=-1,
\qquad
M_{J,K}=s(1-s)(\alpha_J-\alpha_K)^2=1.
\tag{2.9}
\]

Thus the entire dimension-free Pluecker mass can live in a **bank regression-gap** rather than in any large physical edge.

## 3. New theorem: the bank-regression-gap endpoint is uniformly paid when the shared shear is bank-collinear

The next theorem is deliberately scoped: it closes a genuine hard aggregate endpoint without pretending to close the full Witt packet.

### Theorem 3.1 — QFORM-WITT-BANK-GAP-COAREA-v1

Retain (1.4). Let `J sqcup K` be a partition with `0<s=||v_J||^2<1`. Assume that, on each bank, both the completed transverse coefficient vector `z` and the shared-shear coefficient vector `u` are collinear with `v`:

\[
z_J=\alpha_J v_J,
\quad z_K=\alpha_K v_K,
\qquad
u_J=\beta_J v_J,
\quad u_K=\beta_K v_K.
\tag{3.1}
\]

(The notation `nu_J` in the first shared-shear slot is `u_J`; no new random variable is introduced.) Define the two disjoint-bank linear forms

\[
Y=\langle v_J,X_J\rangle,
\qquad
Z=\langle v_K,X_K\rangle.
\tag{3.2}
\]

Then `H,Y,Z` are genuinely independent. If `alpha_J != alpha_K`, the law of `Q` is absolutely continuous and

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
C_\star\,2^{2/3}
\bigl[S_i\,s(1-s)(\alpha_J-\alpha_K)^2\bigr]^{-1/3},
}
\tag{3.3}
\]

where

\[
C_\star=24(3+\sqrt2)10^{2/3}=491.735145127\ldots
\tag{3.4}
\]

is the constant from account03/B05 r39's rank-three determinant-star theorem.

In particular, if the regression-gap currency satisfies

\[
s(1-s)(\alpha_J-\alpha_K)^2\ge\frac16
\tag{3.5}
\]

and `S_i>=1/2`, then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}<1787.085.
}
\tag{3.6}
\]

For the exact Walsh bank geometry in (2.9), the stronger currency value one gives

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}<983.471
}
\tag{3.7}
\]

whenever the shared shear `u` is also bank-collinear.

#### Proof

Under (3.1),

\[
V=Y+Z,
\qquad
U=\beta_JY+\beta_KZ,
\qquad
W^\sharp=\alpha_JY+\alpha_KZ.
\tag{3.8}
\]

Therefore the whole form is a quadratic form of the **three independent scalar variables** `(H,Y,Z)`:

\[
Q
=2a(Y+Z)H
+2a\kappa(Y+Z)(\beta_JY+\beta_KZ)
+A(Y+Z)^2
+\delta(\alpha_JY+\alpha_KZ)^2.
\tag{3.9}
\]

Its symmetric coefficient matrix is

\[
M=
\begin{pmatrix}
0&a&a\\
a&A+2a\kappa\beta_J+\delta\alpha_J^2&A+a\kappa(\beta_J+\beta_K)+\delta\alpha_J\alpha_K\\
a&A+a\kappa(\beta_J+\beta_K)+\delta\alpha_J\alpha_K&A+2a\kappa\beta_K+\delta\alpha_K^2
\end{pmatrix}.
\tag{3.10}
\]

Exact expansion gives the cancellation

\[
\boxed{
\det M=-a^2\delta(\alpha_J-\alpha_K)^2.
}
\tag{3.11}
\]

Notably, `A`, `kappa`, and both shared-shear slopes `beta_J,beta_K` disappear from the determinant. Thus the grouped-bank curvature is exactly the regression-gap currency and cannot be canceled by the shared shear.

For the two linear forms, use the sharp product-marginal theorem of Livshyts--Paouris--Pivovarov (arXiv:1507.07949): every one-dimensional marginal of a product density with one-dimensional density caps one is bounded by `sqrt(2)` after unit Euclidean normalization. Hence

\[
\|p_Y\|_\infty\le\sqrt{\frac2s},
\qquad
\|p_Z\|_\infty\le\sqrt{\frac2{1-s}}.
\tag{3.12}
\]

Let `L_Y,L_Z` denote these two upper bounds and rescale

\[
\widetilde Y=L_YY,
\qquad
\widetilde Z=L_ZZ.
\tag{3.13}
\]

Then `H, Ytilde, Ztilde` are independent with density caps at most one. The determinant of the rescaled three-variable quadratic matrix is

\[
\frac{|\det M|}{L_Y^2L_Z^2}.
\tag{3.14}
\]

Applying the r39 determinant-star theorem in dimension three gives

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_\star(L_YL_Z)^{2/3}|\det M|^{-1/3}.
\tag{3.15}
\]

Since

\[
L_YL_Z\le\frac2{\sqrt{s(1-s)}},
\tag{3.16}
\]

and `|det M|=S_i(\alpha_J-\alpha_K)^2`, (3.3) follows. The numerical statements (3.6)-(3.7) are immediate. QED.

### What this theorem does and does not use

No rotation of the original random vector is declared independent. Independence of `Y` and `Z` is genuine because they are functions of **disjoint original-coordinate banks**. The marginal-density theorem is used only to bound each bank sum. No moment, support, log-concavity, connected-support, or conditional-density hypothesis is introduced. The theorem does **not** cover a residual component of `u` or `z` transverse to `v` inside a bank; those are the remaining terms identified by (2.7).

## 4. Designated partner account04/B05 applied to an actual inequality

The completed partner theorem

`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,  
`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`,

proves for two genuinely independent scalar inputs of density caps `m_1,m_2` and a definite quadratic pair block `C` that arbitrary extensions satisfy

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le \pi m_1m_2|\det C|^{-1/2}.
\tag{4.1}
\]

Apply it to the genuinely independent **disjoint-bank variables** `(Y,Z)` in Theorem 3.1. Their quadratic block is

\[
C_{YZ}=
\begin{pmatrix}
A+2a\kappa\beta_J+\delta\alpha_J^2& A+a\kappa(\beta_J+\beta_K)+\delta\alpha_J\alpha_K\\
A+a\kappa(\beta_J+\beta_K)+\delta\alpha_J\alpha_K& A+2a\kappa\beta_K+\delta\alpha_K^2
\end{pmatrix}.
\tag{4.2}
\]

Whenever this literal grouped pair is definite, (3.12) and (4.1) give the actual inequality

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
\frac{2\pi}{\sqrt{s(1-s)|\det C_{YZ}|}}.
}
\tag{4.3}
\]

Thus, for example,

\[
s(1-s)|\det C_{YZ}|\ge1
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le2\pi<6.284.}
\tag{4.4}
\]

This is an actual application of the designated partner theorem, not a claim of independence after spectral rotation. `Y` and `Z` are independent because the cut is in original coordinates.

## 5. Exact remaining factor after this run

The account02/B05 max-cut theorem supplies `M_{J,K}>=1/2`. The decomposition (2.7) shows that one of three mechanisms has currency at least `1/6`:

1. `(1-s)d_J >=1/6`: transverse Pluecker energy survives inside bank `J`;
2. `s d_K >=1/6`: transverse Pluecker energy survives inside bank `K`;
3. `s(1-s)(alpha_J-alpha_K)^2>=1/6`: a bank regression gap survives.

Theorem 3.1 pays mechanism 3 when the shared-shear and completed-square directions are exactly bank-collinear with `v`; (4.3) may pay an even stronger definite grouped-pair subbranch.

The precise next debt is therefore

`QFORM-WITT-AGGREGATE-RESIDUAL-RECEIVER-v1`:

- in mechanisms 1 or 2, exploit the **within-bank aggregate** `det G_J=s d_J` or `det G_K=(1-s)d_K` before selecting a physical edge;
- in mechanism 3 with a nonzero `u`-residual, retain that residual inside the original product integral while preserving the determinant identity (3.11), rather than conditioning on a projected residual and paying an uncontrolled conditional density.

The exact missing factor is no longer “find one large Pluecker edge.” It is a dependence-safe product-fiber inequality that converts an aggregate bank Gram determinant or regression-gap into the Borel half-profile **before reciprocal minor selection**.

## 6. Checks and integrity

Symbolic algebra verifies (2.7) identically and verifies

`det(M)+a^2*delta*(alpha_J-alpha_K)^2 == 0`.

A 1000-sample floating regression over random orthonormal `(v,w)` and random cuts gave maximum residual `1.05e-15` for (2.4)/(2.7). A 1000-sample floating regression for (3.11) gave maximum residual `4.27e-14`. These finite checks are diagnostics only; the proofs above are exact algebra.

The full conjecture and the full continuity conclusion remain open. This report uses no refuted arbitrary-joint coarea lemma, no positive conditional projection moment, no pointwise van-der-Corput bound, no curved-fiber supremum, and no independence-after-rotation premise.
