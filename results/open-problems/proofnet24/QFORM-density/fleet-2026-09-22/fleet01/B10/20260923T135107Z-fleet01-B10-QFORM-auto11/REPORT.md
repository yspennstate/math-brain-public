# fleet01/B10 — punctured near-null hub: pivot–Schur Fresnel cancellation

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW_ANALYTIC_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Run:** `20260923T135107Z-fleet01-B10-QFORM-auto11`  
**Assignment:** arbitrary exact-rank-three symmetric forms, arbitrary orientation, independent cap-one original coordinates.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full rank-three target and the owner-level three-large-eigenvalue conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a new nonzero-pivot Fresnel interpolation theorem which is uniform in the near-null Rayleigh coefficient. It also gives a reciprocal determinant identity tying the newest fleet02/B10 compression to the scalar Schur complement. The remaining debt is sharply localized to an ultra-coloop/high-leverage corner.

---

## 1. Setup and the first missing implication

Write the exact-rank-three form as

\[
A=UMU^T,\qquad U^TU=I_3,
\]

where `M` is real symmetric and all three eigenvalues have absolute value at least one. Put

\[
D:=|\det M|\ge1.
\]

Choose an **original physical coordinate** `0` whose spectral row is

\[
u_0=\sqrt h\,r,\qquad \|r\|=1,
\]

with `0<h<1`. The current near-coloop reduction has `h` close to one. Let the remaining spectral rows be `u_i`, `i\ne0`; then

\[
G_L:=\sum_{i\ne0}u_i u_i^T=I-hrr^T,
\qquad
\det G_L=1-h.
\tag{1.1}
\]

Set

\[
a:=r^TMr,\qquad m:=Mr,
\qquad s:=\|m\|.
\tag{1.2}
\]

The exact-null endpoint `a=0` is already paid by existing work. The present theorem treats `a\ne0` and, unlike the ordinary scalar-pivot estimate, does **not** lose a factor `|a|^{-1/4}`.

The only extra hypothesis in the new theorem is a precisely stated diffuse-leaf Brascamp–Lieb gate:

\[
\boxed{
\ell_i:=u_i^TG_L^{-1}u_i\le\frac12
\quad(i\ne0).
}
\tag{1.3}
\]

No rotated random coordinates are declared independent. The rows `u_i` are deterministic coefficient vectors; all probabilistic factorisation below remains in the original independent coordinates `X_i`.

---

## 2. Exact pivot–Schur rank-two factorization

Assume `a\ne0`. Define

\[
S:=M-\frac{mm^T}{a}.
\tag{2.1}
\]

Then

\[
Sr=Mr-\frac{m(m^Tr)}a=m-m=0,
\]

so `S` has rank two and acts on `r^\perp`. If `v_1,v_2` is an orthonormal eigenbasis of `S|_{r^\perp}` with nonzero eigenvalues `\theta_1,\theta_2`, then the block determinant formula in the decomposition `\mathbb Rr\oplus r^\perp` gives

\[
\boxed{
\theta_1\theta_2
=\det(S|_{r^\perp})
=\frac{\det M}{a}.
}
\tag{2.2}
\]

Thus a small physical Rayleigh quotient creates a *large* rank-two Schur determinant. This observation by itself does not pay the density, because a naive square peel loses `|a|^{-1/2}`. The point of the next argument is that the Fresnel transform of the hub square cancels the apparent singularity exactly.

Let

\[
z:=\sum_{i\ne0}u_iX_i
\]

be the leaf spectral aggregate and

\[
L:=m^Tz,\qquad Y_k:=v_k^Tz.
\]

Since

\[
z^TMz=\frac{L^2}{a}+z^TSz
=\frac{L^2}{a}+\theta_1Y_1^2+\theta_2Y_2^2,
\]

the full quadratic form is exactly

\[
Q
=haX_0^2+2\sqrt h\,X_0L
+\frac{L^2}{a}
+\theta_1Y_1^2+\theta_2Y_2^2.
\tag{2.3}
\]

This identity is the key structural point: the potentially dangerous longitudinal leaf square is **the same linear form `L` that couples to the hub**.

---

## 3. Exact Fourier transform of the hub-plus-longitudinal packet

Let `f_0` be the density of `X_0`. For `t\ne0` define

\[
H_t(y)
:=e^{ity^2/a}
\int_{\mathbb R}f_0(x)
 e^{it ha x^2+i2t\sqrt h\,yx}\,dx.
\tag{3.1}
\]

The exponent completes **exactly**:

\[
\frac{y^2}{a}+ha x^2+2\sqrt h\,yx
=\frac{(y+a\sqrt h\,x)^2}{a}.
\tag{3.2}
\]

Using the Fourier convention

\[
\widehat F(\xi)=\int_{\mathbb R}e^{i\xi y}F(y)\,dy,
\]

the one-dimensional Fresnel integral therefore gives, after the standard Gaussian regularisation and removal of the damping,

\[
\widehat H_t(\xi)
=\mathfrak c(t,a)
 e^{-ia\xi^2/(4t)}
 \widehat f_0(-a\sqrt h\,\xi),
\]

where

\[
|\mathfrak c(t,a)|
=\sqrt{\frac{\pi|a|}{|t|}}.
\]

Consequently

\[
\boxed{
\|\widehat H_t\|_\infty
\le
\sqrt{\frac{\pi|a|}{|t|}}.
}
\tag{3.3}
\]

No regularity, support, moment, log-concavity or pointwise oscillatory-decay hypothesis on `f_0` is used. Only `\|\widehat f_0\|_\infty\le1`, i.e. probability normalisation, enters (3.3). In particular this step is compatible with the live correction that refutes uniform pointwise van-der-Corput decay for fragmented supports.

---

## 4. New theorem: a diffuse punctured hub has a continuous density

### Theorem — `QFORM-PUNCTURED-HUB-SCHUR-FRESNEL-v1`

Under the setup of Sections 1–3, assume `a\ne0` and the leaf leverage gate (1.3). Then `Q` has a continuous density in `C_0(\mathbb R)` and

\[
\boxed{
\|p_Q\|_\infty
\le
12\,[D(1-h)]^{-1/3}.
}
\tag{4.1}
\]

In particular the bound is **independent of the near-null coefficient `a`**.

### Proof

From (2.3), first keep the hub-plus-longitudinal packet as `H_t(L)` and Fresnel-linearise only the two rank-one squares `\theta_kY_k^2`. With Gaussian damping inserted temporarily, Fourier inversion for `H_t` and the two Fresnel formulas give

\[
|\phi_Q(t)|
\le
\frac1{2\pi}
(4\pi|t|)^{-1}
|\theta_1\theta_2|^{-1/2}
\iiint
|\widehat H_t(\xi)|
\prod_{i\ne0}
\left|
\psi_i\!\left(
 u_i^T(-\xi m+u_1v_1+u_2v_2)
\right)
\right|
\,d\xi\,du_1\,du_2,
\tag{4.2}
\]

where `\psi_i` is the characteristic function of the original independent coordinate `X_i`. The leaf expectation factorises here because all nonlinear phases have already been linearised; no projected-coordinate independence is asserted.

The linear map

\[
(\xi,u_1,u_2)
\longmapsto
\eta=-\xi m+u_1v_1+u_2v_2
\]

has Jacobian

\[
|\det(m,v_1,v_2)|=|m^Tr|=|a|,
\]

because `v_1,v_2` form an oriented orthonormal basis of `r^\perp`. Hence

\[
d\xi\,du_1\,du_2=|a|^{-1}d\eta.
\tag{4.3}
\]

By (3.3),

\[
|\widehat H_t(\xi)|
\le \sqrt{\pi|a|/|t|}.
\]

The leaf rows have Gram `G_L` from (1.1). Under (1.3), the same geometric Brascamp–Lieb plus one-dimensional Fourier `L^p` estimate used in the completed source Fresnel–Brascamp–Lieb theorem gives

\[
\boxed{
\int_{\mathbb R^3}
\prod_{i\ne0}|\psi_i(u_i^T\eta)|\,d\eta
\le
(4\pi)^3(1-h)^{-1/2}.
}
\tag{4.4}
\]

Insert (2.2)–(4.4) into (4.2). The apparent powers of `a` cancel *exactly*:

\[
|\theta_1\theta_2|^{-1/2}
|a|^{-1}
|a|^{1/2}
=
\left(\frac{|a|}{D}\right)^{1/2}
|a|^{-1}|a|^{1/2}
=D^{-1/2}.
\]

The constants reduce to

\[
\boxed{
|\phi_Q(t)|
\le
8\pi^{3/2}
[D(1-h)]^{-1/2}
|t|^{-3/2}.
}
\tag{4.5}
\]

Together with `|\phi_Q(t)|\le1`, this is integrable. Writing

\[
K=8\pi^{3/2}[D(1-h)]^{-1/2},
\]

we use

\[
\int_{\mathbb R}\min(1,K|t|^{-3/2})\,dt=6K^{2/3}
\]

and Fourier inversion to get

\[
\|p_Q\|_\infty
\le
\frac{6}{2\pi}K^{2/3}
=12[D(1-h)]^{-1/3}.
\]

Since `\phi_Q\in L^1`, the density is continuous and vanishes at infinity. Removing the Gaussian regularisation by dominated convergence completes the proof. `square`

### Quantitative corollary

Whenever

\[
D(1-h)\ge2^{-9}=\frac1{512},
\]

the theorem gives the clean universal payment

\[
\boxed{\|p_Q\|_\infty\le96}
\tag{4.6}
\]

with a continuous density.

---

## 5. Applying the newest fleet02/B10 result

The newest completed designated-partner report is

`yspennstate/math-open-problems@f81263344356dd37ef7f6323f863ba48b49f1a34`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T132259Z-fleet02-B10-QFORM-5d7c/REPORT.md`.

It proves for the near-null physical hub that if

\[
v=\frac{Mr}{\|Mr\|},
\qquad
C_m=M|_{v^\perp}
\]

is the two-dimensional compression, then

\[
\boxed{
\det C_m=\frac{a\det M}{s^2}.
}
\tag{5.1}
\]

The scalar Schur complement used in Section 2 satisfies

\[
\boxed{
\det(S|_{r^\perp})=\frac{\det M}{a}.
}
\tag{5.2}
\]

Multiplying (5.1) and (5.2) gives a new reciprocal-curvature identity

\[
\boxed{
|\det C_m|\,
|\det(S|_{r^\perp})|
=
\frac{D^2}{s^2}.
}
\tag{5.3}
\]

Since all singular values of `M` are at least one, if

\[
\sigma_1\ge\sigma_2\ge\sigma_3\ge1
\]

are its singular values, then

\[
s=\|Mr\|\le\sigma_1,
\qquad
D=\sigma_1\sigma_2\sigma_3,
\]

and therefore

\[
\boxed{
\frac{D^2}{s^2}
\ge(\sigma_2\sigma_3)^2
\ge1.
}
\tag{5.4}
\]

Thus the partner's weak compression and the scalar Schur plane can **never both lose determinant**. In the near-null limit the determinant currency is transferred, rather than destroyed. This is an inequality-level application of the designated partner identity.

The same partner report records the reviewed nonzero-pivot density payment

\[
\|p_Q\|_\infty
\le
128[h^2|a|D]^{-1/4}.
\tag{5.5}
\]

In the current true-collar range `h>63/64`, (5.5) gives the actual numerical branch

\[
|a|D\ge2^{-12}
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty<1033.}
\tag{5.6}
\]

This is the required application of a completed partner payment to an actual density inequality. No continuity upgrade is asserted from (5.5) alone.

---

## 6. The surviving chamber is now much smaller

On the diffuse-leaf subbranch (1.3), combine the new theorem with the partner nonzero-pivot payment. Any still-unpaid nonzero near-null state must satisfy **both**

\[
\boxed{
D(1-h)<2^{-9}
}
\tag{6.1}
\]

and

\[
\boxed{
|a|D<2^{-12}.
}
\tag{6.2}
\]

Hence

\[
1-h<\frac1{512D},
\qquad
|a|<\frac1{4096D}.
\tag{6.3}
\]

Moreover the partner compression and the Schur plane obey

\[
|\det C_m|
=\frac{|a|D}{s^2}
<2^{-12},
\tag{6.4}
\]

while

\[
|\det(S|_{r^\perp})|
=\frac D{|a|}
>2^{12}D^2
\ge4096.
\tag{6.5}
\]

So the remaining punctured collar is not a generic weak-curvature state. It is an **ultra-coloop** state in which

1. the leaf Gram loses longitudinal volume at scale below `1/(512D)`;
2. the physical Rayleigh quotient is below `1/(4096D)`;
3. the partner `(Mr)^\perp` compression is weak;
4. the scalar Schur rank-two determinant is simultaneously enormous.

The exact-null point `a=0` itself remains already paid by the completed exact-null theorem. The missing implication is therefore an interpolation across this ultra-corner, not a general rank-three estimate.

---

## 7. What the theorem does *not* assume or prove

- No Gaussian, log-concave, moment, compact-support, connected-support, iid or smoothness assumption is used.
- No spectral rotation of the random vector is treated as preserving independence.
- The Brascamp–Lieb step acts on characteristic functions of the **original independent leaf coordinates**.
- No false uniform pointwise quadratic-phase decay is used. The hub calculation is an exact Fresnel transform identity.
- No arbitrary-joint coarea lemma or positive conditional-density-moment bound is used.
- The leverage gate (1.3) is explicit. A state with a high whitened leaf leverage is **not** claimed paid by Theorem 4.1.
- The theorem proves a continuous density in its scope because its characteristic function is `L^1`.
- The full exact-rank-three theorem remains open, as does the full QFORM conjecture.

The first unpaid implication after this run is

\[
\boxed{
\texttt{QFORM-ULTRACOOLOP-HIGHLEVERAGE-INTERPOLATION-v1}.
}
\]

A next proof should use either (i) a second-hub peel when the leaf leverage gate fails, or (ii) in the diffuse ultra-corner, the reciprocal determinant currency (5.3) together with the already finite exact-null endpoint. A perturbative deletion of the small `a` term is invalid under the source class.

---

## 8. Source ledger


Mathematical source used for the Brascamp–Lieb integral:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, especially Lemma 1 and Theorem F.

Designated partner consumed and applied:

- `fleet02/B10`, canonical mathematics `yspennstate/math-open-problems@f81263344356dd37ef7f6323f863ba48b49f1a34`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T132259Z-fleet02-B10-QFORM-5d7c/REPORT.md`;
- source-pinned brain handoff commit `c8d0f23bf96f6f967109eafbc5cda7eda766a302`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and writes are not evidence of native authenticated brain ingestion.
