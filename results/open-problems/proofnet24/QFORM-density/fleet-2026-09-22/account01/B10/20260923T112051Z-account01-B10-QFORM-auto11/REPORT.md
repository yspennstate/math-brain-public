# account01/B10 QFORM auto11 — unnormalized ridge receiver and dependent-pair hyperbolic square

**Status:** `ESSENTIAL_STEP_APPLIED / NEW_ANALYTIC_RECEIVER / CONTINUITY_UPGRADE / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`.

**Run:** `20260923T112051Z-account01-B10-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case, arbitrary orientation, independent cap-one physical coordinates.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a new dependence-tolerant analytic receiver, upgrades the exact-null-coloop endpoint from mere essential boundedness to a continuous density, preserves the useful mathematics from the preceding interrupted attempt, and applies the designated `account02/B10` collinear-bank theorem to an explicit true-collar inequality. No rotated-coordinate independence is used.

---

## 1. Compact end-to-end target and the first missing implication

Write an exact rank-three form as

\[
A=UMU^T,\qquad U^TU=I_3,
\]

where the three nonzero eigenvalues of the symmetric `M` have absolute value at least one. Thus

\[
|\det M|\ge1.
\]

The live near-coloop reduction has a physical hub row of leverage close to one. The obstruction is not the two-dimensional projected pair itself: a two-dimensional orthogonal projection of the original product law has a bounded **joint** density, although its two coordinates need not be independent. The obstruction is the extra same-bank longitudinal nuisance that can move the center of the quadratic ridge in a way which cannot be replaced by an arbitrary conditional-density estimate.

The first calculation below attacks the missing implication at exactly that interface. The key point is to keep the two-dimensional law as a joint density and never split it into fictitiously independent coordinates.

---

## 2. A sharp one-dimensional half-Riesz bathtub bound

### Lemma 2.1
Let `X` have a probability density `f` with

\[
0\le f\le K.
\]

Then for every `c\ne0` and every real `s`,

\[
\boxed{
\mathbb E|cX-s|^{-1/2}
\le 2\sqrt2\left(\frac K{|c|}\right)^{1/2}.
}
\tag{2.1}
\]

### Proof
After the affine change `u=cx-s`, the pushforward density is bounded by `K/|c|` and has total mass one. Since `|u|^{-1/2}` is symmetric decreasing, the bathtub principle places the maximizing density at height `K/|c|` on the centered interval of length `|c|/K`. Therefore

\[
\begin{aligned}
\mathbb E|cX-s|^{-1/2}
&\le \frac K{|c|}
\int_{-|c|/(2K)}^{|c|/(2K)}|u|^{-1/2}\,du\\
&=2\sqrt2\left(\frac K{|c|}\right)^{1/2}.
\end{aligned}
\]

No moment, support, smoothness, symmetry, or connected-support assumption appears. `square`

---

## 3. New receiver: an unnormalized square-root ridge is enough

### Theorem 3.1 — `QFORM-UNNORMALIZED-RIDGE-HYPERBOLIC-RECEIVER-v1`
Let `X` be independent of a pair `(Y,R)`. Assume

\[
\|p_X\|_\infty\le K
\]

and `(Y,R)` has a joint probability density `g(y,r)`. Suppose there are a measurable function `F:R->R` and a constant `H<\infty` such that

\[
\boxed{
g(y,r)\le H\,|r-F(y)|^{-1/2}
}
\tag{3.1}
\]

for almost every `(y,r)` away from the ridge. For `lambda\ne0`, set

\[
T=R+\lambda XY.
\]

Then `T` has a bounded continuous density, in fact a `C_0(R)` density, and

\[
\boxed{
\|p_T\|_\infty
\le
3\,2^{5/3}
H^{2/3}
\left(\frac K{|\lambda|}\right)^{2/3}.
}
\tag{3.2}
\]

The importance of (3.1) is that it is an **unnormalized joint-density bound**. It is not a bound on a conditional density and it does not assert any independence between `Y` and `R`.

### Proof
For almost every `t`, Fubini gives the density representation

\[
p_T(t)=\iint f_X(x)g(y,t-\lambda xy)\,dx\,dy.
\tag{3.3}
\]

Fix `delta>0` and split at `|y|=delta`.

#### Far-slope part
For `|y|>delta`, instead integrate out `x`:

\[
\begin{aligned}
p_{>\delta}(t)
&=
\iint_{|y|>\delta}
 g(y,r)
 \frac1{|\lambda y|}
 f_X\!\left(\frac{t-r}{\lambda y}\right)
 \,dr\,dy\\
&\le \frac{K}{|\lambda|\delta}
\iint g(y,r)\,dr\,dy.
\end{aligned}
\]

Hence

\[
\boxed{
p_{>\delta}(t)\le \frac{K}{|\lambda|\delta}.}
\tag{3.4}
\]

#### Near-slope part
Using the ridge envelope (3.1) and Lemma 2.1,

\[
\begin{aligned}
p_{\le\delta}(t)
&\le H\int_{|y|\le\delta}
\mathbb E
|t-F(y)-\lambda yX|^{-1/2}\,dy\\
&\le
2\sqrt2\,H
\left(\frac K{|\lambda|}\right)^{1/2}
\int_{|y|\le\delta}|y|^{-1/2}\,dy\\
&=
8\sqrt2\,H
\left(\frac K{|\lambda|}\right)^{1/2}
\sqrt\delta.
\end{aligned}
\tag{3.5}
\]

Thus

\[
p_T(t)
\le A\sqrt\delta+B\delta^{-1},
\]

with

\[
A=8\sqrt2\,H(K/|\lambda|)^{1/2},
\qquad
B=K/|\lambda|.
\]

The minimum over `delta>0` occurs at

\[
\delta^{3/2}=\frac{2B}{A}.
\]

Since

\[
\min_{x>0}(Ax+B/x^2)
=3\,2^{-2/3}A^{2/3}B^{1/3},
\]

we obtain exactly (3.2).

#### Continuity
For fixed `delta>0`, the far part is continuous. Indeed, using (3.3) and changing from `x` to the second density variable,

\[
|p_{>\delta}(t+h)-p_{>\delta}(t)|
\le
\frac K{|\lambda|\delta}
\|g(\cdot,\cdot+h)-g\|_{L^1(R^2)},
\]

which tends to zero as `h->0` by `L^1` translation continuity. It also vanishes at infinity after the standard compact-approximation argument. Equation (3.5) is uniform in `t` and tends to zero with `delta`. Hence `p_T` is a uniform limit of `C_0` functions, so `p_T in C_0(R)`. `square`

---

## 4. Main corollary: the square coordinates may be dependent

### Corollary 4.1 — `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`
Let `X` be independent of the pair `(Y,Z)`, with

\[
\|p_X\|_\infty\le K,
\qquad
\|p_{Y,Z}\|_\infty\le H.
\]

No independence between `Y` and `Z` is assumed. Let `a,b\ne0`, and let `F,theta:R->R` be arbitrary measurable functions. Then

\[
T=2aXY+F(Y)+b\bigl(Z+\theta(Y)\bigr)^2
\]

has a continuous `C_0` density satisfying

\[
\boxed{
\|p_T\|_\infty
\le
6(KH)^{2/3}|a|^{-2/3}|b|^{-1/3}.
}
\tag{4.1}
\]

### Proof
Set

\[
R=F(Y)+b(Z+\theta(Y))^2.
\]

For a fixed `y`, the map `z -> r` has the two inverse branches

\[
z+\theta(y)=\pm\sqrt{\frac{r-F(y)}b}
\]

on the appropriate half-line. The one-dimensional change of variables therefore gives the joint density of `(Y,R)` the pointwise envelope

\[
\boxed{
 g(y,r)
 \le
 \frac{H}{\sqrt{|b|}}|r-F(y)|^{-1/2}.
}
\tag{4.2}
\]

This is the crucial step: (4.2) uses only the **joint** cap for `(Y,Z)`. It never asserts that the projected coordinates are independent and never divides by the marginal density of `Y`.

Apply Theorem 3.1 with

\[
\lambda=2a,
\qquad
H_{\rm ridge}=H/\sqrt{|b|}.
\]

Then

\[
3\,2^{5/3}
(H/\sqrt{|b|})^{2/3}
(K/(2|a|))^{2/3}
=
6(KH)^{2/3}|a|^{-2/3}|b|^{-1/3},
\]

which proves (4.1), including continuity. `square`

### Why this is a genuine extension
The previously dangerous step was to infer independent projected coordinates after an orthogonal spectral rotation. Corollary 4.1 does not do that. It is designed exactly for a bounded **two-dimensional projection density**, which is what the product-marginal theorem actually supplies. Thus dependence between the two projected coordinates is now harmless whenever there is no additional moving-ridge nuisance variable.

---

## 5. QFORM application: continuous density at the exact-null coloop endpoint

This gives a clean new regularity upgrade on an already bounded endpoint.

Assume one physical spectral row has full leverage one. After an orthogonal spectral change of basis,

\[
r_0=e_1.
\]

Because the spectral rows form a Parseval frame, every other row lies in `e_1^perp`. Suppose additionally that the physical hub diagonal is zero,

\[
e_1^TMe_1=0.
\]

Choose `e_2` in the direction of `P_{e_1^perp}Me_1`. Since `M` is invertible, this direction is nonzero. In the basis `(e_1,e_2,e_3)`,

\[
M=
\begin{pmatrix}
0&s&0\\
s&d&g\\
0&g&f
\end{pmatrix},
\qquad
s\ne0,
\qquad
f\ne0,
\tag{5.1}
\]

and

\[
\boxed{\det M=-s^2f.}
\tag{5.2}
\]

Let

\[
(Y,Z)=\sum_{j\ne0}(r_{j,2},r_{j,3})X_j.
\]

The two coefficient columns are orthonormal, so the cap-one product projection theorem gives the genuine joint-density estimate

\[
\boxed{\|p_{Y,Z}\|_\infty\le2.}
\tag{5.3}
\]

The original hub variable `X_0` is genuinely independent of this pair and has density cap one. The form is

\[
Q=2sX_0Y+dY^2+2gYZ+fZ^2.
\]

Complete only the transverse square:

\[
Q
=2sX_0Y+
\left(d-\frac{g^2}{f}\right)Y^2
+f\left(Z+\frac gfY\right)^2.
\tag{5.4}
\]

Corollary 4.1 with `K=1`, `H=2`, `a=s`, `b=f` yields

\[
\begin{aligned}
\|p_Q\|_\infty
&\le6\,2^{2/3}|s|^{-2/3}|f|^{-1/3}\\
&=6\,2^{2/3}|\det M|^{-1/3}\\
&\le6\,2^{2/3}
<9.525.
\end{aligned}
\tag{5.5}
\]

Therefore:

\[
\boxed{
\text{every exact-null leverage-one coloop has a continuous }C_0\text{ density, with }\|p_Q\|_\infty<9.525.
}
\]

The earlier coloop closure established a slightly smaller essential-supremum constant by a different receiver, but did not claim continuity in full generality. Equation (5.5) supplies the missing continuity statement for this endpoint while still allowing arbitrary cap-one physical densities and dependent transverse projected coordinates.

---

## 6. Preserved calculation from the interrupted predecessor: square-fiber `L^3_t` mass

The preceding interrupted B10 attempt found a useful integrated-Fourier estimate. It is recorded here rather than discarded.

### Lemma 6.1 — `QFORM-FIBER-SQUARE-L3-MASS-v1`
Let `h(z,w)` be a nonnegative density relative to `dz dnu(w)` with

\[
0\le h\le H,
\qquad
M=\iint h(z,w)\,dz\,d\nu(w)<\infty.
\]

Let `theta(w)` be measurable and `b\ne0`. Define

\[
F(t,w)=\int_{\mathbb R}
 e^{itb(z+\theta(w))^2}h(z,w)\,dz.
\]

Then, with the Fourier convention `hat q(t)=int e^{itu}q(u)du`, one has the safe bound

\[
\boxed{
\int\!\int_{\mathbb R}|F(t,w)|^3\,dt\,d\nu(w)
\le
\frac{32\pi H^2M}{|b|}.
}
\tag{6.1}
\]

A direct proof pushes `h(.,w)` through the square map. The resulting density `q_w` has an inverse-square-root endpoint. The cap `h<=H` and mass `m(w)` give

\[
\|q_w\|_{3/2}^3\le \frac{16H^2m(w)}{|b|}
\]

(with room in the constant), while Hausdorff--Young / interpolation with the above Fourier convention gives

\[
\|\widehat q_w\|_3^3\le2\pi\|q_w\|_{3/2}^3.
\]

Integrating in `w` proves (6.1).

This estimate is valid under fragmented supports and therefore survives the live correction that kills uniform pointwise van-der-Corput decay.

### Why (6.1) alone does not finish the target
Combining one `L^3_t` square factor with only one independent scalar Fourier factor cannot force `L^1_t` integrability: the best direct Hölder bookkeeping leaves an effective time exponent at most `2/3`. Thus the interrupted mechanism hit a real integrability barrier. The present run changes mechanism: instead of seeking pointwise time decay, Theorem 3.1 uses the physical-space square-root ridge together with the hub slope and optimizes the two singular regimes directly.

---

## 7. Designated partner result applied at an actual inequality

The completed `account02/B10` theorem `QFORM-COLLINEAR-PRODUCT-BANK-COMPRESSION-v1` states that disjoint original-coordinate banks whose spectral rows are each collinear can be compressed to genuinely independent scalar variables with density cap at most `sqrt(2)`. If three aggregate bank rows have squared determinant `w>0` and the exact-rank-three spectral matrix has

\[
D=|\det M|,
\]

then the completed physical-triple theorem gives

\[
\boxed{
\|p_Q\|_\infty
\le2C_3(Dw)^{-1/3},
\qquad
C_3=16\sqrt{30}\,2^{1/4}=104.216889\ldots .
}
\tag{7.1}
\]

Here is an explicit application in the live true-collar state. Suppose the nonhub spectral rows occupy at most `N` exact projective rays. Compress each ray bank. If the hub row is `sqrt(c)e_1`, Parseval gives

\[
\sum_{p<q}
\det(r_h,\bar r_p,\bar r_q)^2
=
 c\det(I_2)=c.
\tag{7.2}
\]

There are at most `binom(N,2)` ray pairs, hence one pair obeys

\[
w\ge \frac{c}{\binom N2}.
\tag{7.3}
\]

Since `D>=1`, (7.1) gives the actual inequality

\[
\boxed{
\|p_Q\|_\infty
\le
2C_3
\left(\frac{\binom N2}{c}\right)^{1/3}.
}
\tag{7.4}
\]

In the designated partner's true collar `c>63/64`. Therefore every survivor with at most eight projective rays is uniformly paid by

\[
\boxed{
\|p_Q\|_\infty
<
2(104.216889)
\left(\frac{28}{63/64}\right)^{1/3}
<636.259.
}
\tag{7.5}
\]

No projected-coordinate independence is used: independence enters only after compression of disjoint **original-coordinate** ray banks, exactly as in the partner theorem.

This also records the useful conclusion from the interrupted predecessor: every fixed projective-ray complexity is paid, with a constant depending only on that fixed complexity. Hence a genuinely unresolved true-collar sequence must have unbounded projective complexity.

---

## 8. What is now paid, and what remains unpaid

This run changes the analytic frontier in three ways.

1. **Dependence inside the two-dimensional projected pair is no longer itself an obstruction.** A bounded joint density for `(Y,Z)` is sufficient for the hyperbolic-square receiver; no independence of `Y` and `Z` is needed.

2. **The exact-null coloop endpoint now has a continuous density.** Equation (5.5) proves `p_Q in C_0` with a universal bound `<9.525` for that endpoint.

3. **Bounded projective complexity is not the frontier.** The designated partner theorem gives (7.4), and in particular (7.5) for at most eight rays.

The genuinely unpaid object is the extra same-bank longitudinal variable in the high-complexity near-coloop state. In Witt coordinates it has the schematic form

\[
Q=
2aX_0Y
+
2aEY
+
\text{quadratic terms in the transverse variables},
\tag{8.1}
\]

where `X_0` is an original independent hub variable but `(E,Y,Z)` are linear forms of the same original product bank. The term `2aEY` moves the center of the square-root ridge. An arbitrary conditional-density cap for `E` is not enough; the live `account02/B10` correction gives an exact logarithmic-singularity construction showing why that shortcut is invalid.

Accordingly the first unpaid implication after this run is

\[
\boxed{\texttt{QFORM-MOVING-RIDGE-PRODUCT-BL-v1}.}
\]

A successful theorem should retain the **linear product provenance** of `(E,Y,Z)` and bound the moving-ridge mixture before taking any conditional supremum. A natural target formulation is a weighted affine-fiber / Brascamp--Lieb estimate for the unnormalized joint image under

\[
(E,Y,Z)\mapsto (Y,\,2aEY+bZ^2+\cdots),
\]

strong enough to feed Theorem 3.1 or a direct analogue. The theorem must remain stable as the regression residual tends to zero and must not introduce moments or support bounds.

The full arbitrary exact-rank-three QFORM theorem remains **OPEN**. The owner-level statement for all matrices with at least three eigenvalues of absolute value at least one therefore remains **OPEN** as well.

---

## 9. Correction and scope ledger

- No Gaussian, log-concave, compact-support, connected-support, moment, iid, or smoothness assumption is used.
- No orthogonal rotation of the random coordinates is made; only deterministic spectral-coordinate bookkeeping is used.
- Corollary 4.1 explicitly permits dependence between the two projected coordinates.
- The pointwise oscillatory-decay claim refuted by fragmented supports is not used.
- The bounded-projection theorem is used only to obtain a joint density cap for a true orthogonal projection, never to claim independence.
- The extra moving-ridge nuisance is **not** declared harmless; it is precisely the remaining debt.
- Continuity is proved in Theorem 3.1, Corollary 4.1, and the exact-null-coloop application (5.5). No continuity claim is made for the still-open general near-coloop branch.
- Full-solution status: `OPEN_NOT_PROVED`; no counterexample has been produced.

## 10. Source ledger

Fresh owner/control sources read from `yspennstate/math-research-brain@e2240492444afb95fb7eddb092c23d3c9d79078d`:

- `AGENTS.md`;
- `fleet.json`, `roles.json`, `PROTOCOL.md` as governed by the owner control;
- `CURRENT_RESEARCH.md`;
- `CLAIMS.json`;
- live `CORRECTION_INBOX.json`;
- `MEMORY_PROTOCOL.md`;
- `assignments/account01/B10.json`.

Designated partner consumed:

- `account02/B10` handoff `20260923T064541Z-account02-B10-QFORM-auto11.md`, especially `QFORM-COLLINEAR-PRODUCT-BANK-COMPRESSION-v1`, applied quantitatively in (7.4)--(7.5), and the live warning `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` respected in Section 8.

Preserved local predecessor mathematics:

- `account01/B10/20260923T092051Z-account01-B10-QFORM-auto11/CHECKPOINT.md`, whose `L^3` square-fiber calculation and finite-ray observation are incorporated and corrected/strengthened here.

No native authenticated brain receiver was invoked; repository use is therefore still labeled `WITHOUT_VERIFIED_BRAIN`.
