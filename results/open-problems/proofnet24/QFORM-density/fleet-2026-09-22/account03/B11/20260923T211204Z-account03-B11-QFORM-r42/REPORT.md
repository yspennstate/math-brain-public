SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T21:12:04Z.
attacking: the punctured near-coloop interpolation gap: convert the uniformly persistent internal third curvature into aggregate physical third-volume, or force it onto at most three nearly-coloop physical rows.

# account03/B11 r42 — internal curvature to aggregate E3 or a finite heavy-row collar

Status: **new exact structural identity + quantitative E3 exit + finite-row reduction / designated partner applied / full unrestricted QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Regularity: the new E3 branch below has a continuous `C_0` density by the cited physical-E3 receiver. The surviving finite-heavy-row collar is not closed here, so no unrestricted continuity conclusion is claimed.

The owner target remains unchanged: independent ORIGINAL coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moments, compact/connected support, diagonal-basis independence, law-uniform pointwise van der Corput decay, arbitrary-joint coarea, conditional-density cap, fiber-supremum, or small-random-quadratic-error assumption is used.

## 1. Mandatory rank-two control and inherited punctured-collar geometry

For independent centered unit uniforms,

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<\frac12.
\]

Thus the opposite-sign rank-two saddle is genuinely logarithmically singular. The third direction must supply a real additional smoothing currency.

Retain the exact-rank-three indefinite factorization from account03/B11 r41,

\[
A=RMR^T,\qquad R^TR=I_3,\qquad s:=\min_a|\lambda_a(M)|\ge1,
\]

with signature `(2,1)` or `(1,2)`. In the true-near-coloop hard chamber, r37--r41 provide a literal ORIGINAL-coordinate cut `H|T`, with physical crossing

\[
B:=A[H,T],
\]

whose singular values satisfy

\[
\sigma_1\ge\sigma_2\ge\sigma_3\ge0,
\qquad
\boxed{\sigma_1\sigma_2>\kappa_*s^2},
\tag{1.1}
\]

where

\[
\kappa_*:=\frac{34}{111}\left(\frac{17}{288}\right)^2
=\frac{4913}{4603392}
=0.001067256492603715\ldots .
\tag{1.2}
\]

Let `U=[u_1,u_2]` be the first two left singular vectors of `B`. Let `w` be the unit completion inside the three-dimensional space `range(R_H)`, and put

\[
E=[U,w]\in\mathbb R^{|H|\times3},\qquad E^TE=I_3.
\]

Write the `H`-side quadratic matrix in this basis as

\[
C:=E^TA[H,H]E
=\begin{pmatrix}C_0&d\\ d^T&\alpha\end{pmatrix},
\qquad
h:=\binom d\alpha\in\mathbb R^3.
\tag{1.3}
\]

The r41 internal-curvature theorem proves

\[
\boxed{\|h\|_2>\beta_0s},
\qquad
\beta_0:=\frac{34}{111}\frac{17}{288}
=\frac{289}{15984}
=0.01808058058058058\ldots .
\tag{1.4}
\]

Only the third *cross* singular value `sigma_3` may collapse. The point of the present run is to turn the noncollapsing internal vector `h` into a physical aggregate quantity before paying any reciprocal minor.

## 2. New exact identity: internal curvature equals leverage-weighted transfer energy

For each physical coordinate `i in H`, define the row of the orthonormal three-frame `E`

\[
z_i:=E^Te_i=(a_i,\omega_i)\in\mathbb R^2\times\mathbb R,
\]

and the two leverages

\[
\ell_i:=\|a_i\|_2^2,
\qquad
q_i:=\|z_i\|_2^2=\ell_i+\omega_i^2.
\tag{2.1}
\]

Thus `0<=ell_i<=q_i<=1`, `sum_i ell_i=2`, and `sum_i q_i=3`.

Let

\[
c_i:=A[H\setminus\{i\},\{i\}]
\]

be the off-diagonal physical self-column of coordinate `i` inside the `H` bank, and for `ell_i<1` set

\[
\delta_i:=\operatorname{dist}\bigl(c_i,
\operatorname{span}\{u_1|_{H\setminus\{i\}},u_2|_{H\setminus\{i\}}\}\bigr).
\tag{2.2}
\]

When `ell_i=1`, use the same zero convention as the aggregate-transfer theorem and define `(1-ell_i)delta_i^2=0`. Finally put

\[
W_H:=\sum_{i\in H}(1-\ell_i)\delta_i^2.
\tag{2.3}
\]

### Theorem `QFORM-INTERNAL-CURVATURE-TRANSFER-IDENTITY-v1`

In the exact-rank-three punctured collar above,

\[
\boxed{
(1-\ell_i)\delta_i^2
=(1-q_i)(h\cdot z_i)^2
\quad\text{for every }i\in H,
}
\tag{2.4}
\]

and therefore

\[
\boxed{
W_H=\sum_{i\in H}(1-q_i)(h\cdot z_i)^2.
}
\tag{2.5}
\]

Moreover

\[
\boxed{
\sum_{i\in H}(h\cdot z_i)^2=\|h\|_2^2.
}
\tag{2.6}
\]

#### Proof

Because `R_H` has full column rank three in the r41 chamber and `E` spans `range(R_H)`,

\[
A[H,H]=ECE^T.
\tag{2.7}
\]

The `i`th full physical self-column is

\[
ECE^Te_i=ECz_i.
\]

Writing the first two coordinates of `Cz_i` as `r_i in R^2` and its third coordinate as

\[
b_i:=e_3^TCz_i=h\cdot z_i,
\tag{2.8}
\]

and deleting physical row `i`, we obtain the exact decomposition

\[
c_i=U_{-i}r_i+b_iw_{-i}.
\tag{2.9}
\]

Thus only the second term contributes to distance from `span(U_{-i})`:

\[
\delta_i^2=b_i^2\operatorname{dist}(w_{-i},\operatorname{span}U_{-i})^2.
\tag{2.10}
\]

For `ell_i<1`, the Gram base-height formula and the fact that `E` has orthonormal columns give

\[
\operatorname{dist}(w_{-i},\operatorname{span}U_{-i})^2
=
\frac{\det(E_{-i}^TE_{-i})}{\det(U_{-i}^TU_{-i})}.
\tag{2.11}
\]

Deleting one row from an orthonormal frame gives

\[
E_{-i}^TE_{-i}=I_3-z_iz_i^T,
\qquad
U_{-i}^TU_{-i}=I_2-a_ia_i^T.
\]

The matrix determinant lemma therefore gives

\[
\det(E_{-i}^TE_{-i})=1-q_i,
\qquad
\det(U_{-i}^TU_{-i})=1-\ell_i.
\tag{2.12}
\]

Substituting (2.12) into (2.10) proves (2.4) whenever `ell_i<1`. If `ell_i=1`, then `q_i=1` because `ell_i<=q_i<=1`, so both sides of (2.4) vanish under the stated convention. Summing proves (2.5).

Finally, the scalar vector with components `h·z_i` is exactly `Eh`. Since `E^TE=I_3`,

\[
\sum_i(h\cdot z_i)^2=\|Eh\|_2^2=\|h\|_2^2,
\]

which proves (2.6). QED.

### Interpretation

This identity is the missing bridge between the SVD-basis internal curvature from r41 and the *physical original-coordinate transfer currency* used by the fleet's aggregate spectral-plane theorem. It does not select a tiny minor. Every coordinate's failure to be a coloop, measured by `1-q_i`, is multiplied by exactly the amount of third internal curvature carried by that coordinate.

## 3. Quantitative consequence: paid E3 branch or at most three heavy rows

Use the completed account01/B02 aggregate-transfer theorem `QFORM-RANK2-SPECTRALPLANE-AGGREGATE-TRANSFER-L1-v1`. For the current cut `H|T`, its squared top crossing singular values are

\[
x_1=\sigma_1^2,\qquad x_2=\sigma_2^2,
\]

and it produces a literal ORIGINAL-coordinate cut `S'|T'` satisfying

\[
E_3(A[S',T'])\ge\frac{27}{256}x_1x_2W_H.
\tag{3.1}
\]

By (1.1),

\[
x_1x_2=(\sigma_1\sigma_2)^2>\kappa_*^2s^4.
\tag{3.2}
\]

Split into two cases.

### Case A: aggregate internal curvature is not too concentrated

If

\[
W_H\ge\frac{\beta_0^2}{8}s^2,
\tag{3.3}
\]

then (3.1)--(3.2) yield

\[
\boxed{
E_3(A[S',T'])>\zeta_*s^6,
}
\tag{3.4}
\]

where

\[
\zeta_*:=\frac{27}{256}\frac{\kappa_*^2\beta_0^2}{8}
=4.909035430513786\times10^{-12}.
\tag{3.5}
\]

The completed marginal-free physical-third-volume receiver gives

\[
\|p_Q\|_\infty\le10.345084\,E_3(A[S',T'])^{-1/6},
\]

hence

\[
\boxed{
\|p_Q\|_\infty<\frac{793.539}{s}.
}
\tag{3.6}
\]

This branch has a continuous `C_0` density because the receiver proves the characteristic function is integrable.

### Case B: aggregate transfer is small

Assume instead

\[
W_H<\frac{\beta_0^2}{8}s^2.
\tag{3.7}
\]

Define the high-leverage physical set

\[
J:=\{i\in H:q_i>3/4\}.
\tag{3.8}
\]

Since `sum_i q_i=3`, necessarily

\[
\boxed{|J|\le3.}
\tag{3.9}
\]

For `i notin J`, `1-q_i>=1/4`, so (2.5) and (3.7) imply

\[
\frac14\sum_{i\notin J}(h\cdot z_i)^2
\le W_H
<\frac{\beta_0^2}{8}s^2.
\]

Thus

\[
\sum_{i\notin J}(h\cdot z_i)^2
<\frac{\beta_0^2}{2}s^2.
\tag{3.10}
\]

Using (1.4) and (2.6),

\[
\sum_{i\in J}(h\cdot z_i)^2
>\frac{\beta_0^2}{2}s^2.
\tag{3.11}
\]

Therefore some physical coordinate `i_* in J` satisfies

\[
\boxed{
q_{i_*}>\frac34,
\qquad
|h\cdot z_{i_*}|>\frac{\beta_0}{\sqrt6}s
=0.00738136611261614\ldots\,s.
}
\tag{3.12}
\]

This is a strict finite-row reduction: if the aggregate E3 exit does not fire, more than half of the paid third internal-curvature energy must live on at most three nearly-coloop physical rows of the `H`-side rank-three range.

No density theorem is claimed from (3.12) alone. The next receiver must use this finite heavy-row geometry without treating a small nonzero third cross shear as a removable perturbation.

## 4. Designated account04/B11 partner result applied to an actual inequality

Before entering the hard small-leaf chamber, use the completed designated-partner pair-area compiler from account04/B11 r5:

\[
\|p_Q\|_\infty\le\frac{128\sqrt2}{s\sqrt{g_{ij}}},
\qquad g_{ij}=\|r_i\wedge r_j\|^2.
\tag{4.1}
\]

For the true-near-coloop hub `r_0=\sqrt c\,e`, `c>63/64`, and a residual spectral row `r_j=s_je+w_j`,

\[
g_{0j}=c\|w_j\|^2.
\]

Hence if any residual row has

\[
\|w_j\|^2\ge1/36,
\]

then

\[
g_{0j}>\frac{63}{64}\frac1{36}=\frac7{256},
\]

and the designated partner theorem gives the actual target inequality

\[
\boxed{
\|p_Q\|_\infty
<\frac{2048\sqrt{2/7}}{s}
=\frac{1094.70204687329\ldots}{s}.
}
\tag{4.2}
\]

Thus r42's new transfer identity is needed only after this concrete partner exit has removed the large-leaf branch.

## 5. How the third direction removes the logarithmic singularity

The two uniformly strong crossing directions in (1.1) are exactly the two-direction saddle that by itself sits at the logarithmic endpoint. The r41 theorem proves that a third internal curvature vector `h` of size `>beta_0 s` survives even when the third cross singular value tends to zero.

The new identity (2.5) now gives a physical interpretation of that third direction:

- if its energy is spread across coordinates that are not almost coloops of the rank-three `H`-range, it necessarily creates aggregate physical third-volume; the E3 Fourier receiver turns that volume into an `L^1` characteristic-function bound and hence a continuous bounded density;
- if aggregate third-volume does not appear, the third curvature cannot disappear: it is forced onto at most three high-leverage physical rows, with one row carrying the explicit amount (3.12).

Thus the punctured collar is reduced from a diffuse analytic interpolation problem to a finite physical-heavy-row problem. This is stronger than merely observing that `(d,alpha)` is nonzero: the new formula identifies exactly where that curvature must live in ORIGINAL coordinates.

The statement is invariant under `M -> -M`, so it treats signatures `(2,1)` and `(1,2)` symmetrically.

## 6. Remaining implication

The full conjecture remains OPEN. The first unpaid B11 implication is now

`QFORM-FINITE-HEAVYROW-PUNCTURED-RECEIVER-v1`:

> In the exact-rank-three true-near-coloop chamber, assume the large-leaf account04/B11 pair-area exit fails and the aggregate E3 exit in Section 3 fails. Then there is a set of at most three physical `H`-coordinates with `q_i>3/4` carrying more than half of the internal third-curvature energy, and one satisfies (3.12). Use that finite set, together with `sigma_1 sigma_2 >= kappa_* s^2`, to obtain a density bound uniform in the vanishing third cross singular value, or route to an already-paid pivot/pair-area/overlap-one receiver.

The proof must retain the nonzero `sigma_3 zW` term exactly; no moment assumption or small-random-perturbation deletion is allowed. Arbitrary additional nonseparable spectrum remains a separate bridge from exact rank three to the full owner target. Global continuity therefore remains open.

## 7. Source pins and scope


Fresh math source before publication: `yspennstate/math-open-problems@68e6d8f52d904033878f6f55c376c38fd214684e`.

Dependencies actually used:

- account03/B11 r41, canonical path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T201243Z-account03-B11-QFORM-r41/REPORT.md`, repository state through `7120df98e7d30de603f45a8823fb02d25564f218`;
- aggregate rank-two spectral-plane transfer: account01/B02 commit `56e56e3c3af5bad72c125079b30eaa38824291de`;
- marginal-free physical-E3 receiver `||p||_infinity <=10.345084 E3^{-1/6}`: account02/B02 path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`, read at fresh math state above;
- designated partner account04/B11 disjoint-volume/pair-area compiler: commit `50b07997bec888ff7cc6820cd42be8e34d0ffc48`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T111608Z-account04-B11-disjoint-volume-compiler-r5/REPORT.md`.

The live correction inbox was refreshed at brain commit `28e3f8d2529df15e5d65e5229f7f077536122d96`; no refuted pointwise-decay, arbitrary-joint-coarea, conditional-cap, one-good-minor, mixed-slice, or perturbative-tail premise is used.
