SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T20:44:37Z.
attacking: a one-sided overlap-one receiver combining one physical scalar quadratic pivot with an invertible physical 2x2 cross block, without square-root decoupling.

# fleet03/B09 r41 — scalar Fresnel pivot + rank-two bilinear crossing

## Status

This run proves, pending independent review, the supporting theorem

**QFORM-ONE-SIDED-PIVOT-RANK2-CROSS-SMOOTHING-v1.**

It is an original-coordinate five-variable receiver for a configuration not covered by a literal disjoint 3x3 cross minor. It supplies one smoothing resource from a nonzero physical scalar quadratic pivot and two from an invertible physical 2x2 cross block. The proof uses only a translation-uniform L^3-in-time estimate for a scalar square phase and source-coordinate L^2 Plancherel for the bilinear block. It never asserts pointwise law-uniform van der Corput decay.

The full three-large-eigenvalue QFORM conjecture remains **OPEN**. The full-target continuity question remains **OPEN**. Continuity is proved for the branch below.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact theorem

Let `h,i1,i2,j1,j2` be five distinct original coordinates. Condition on every other original coordinate. Write

\[
Y=(X_{i_1},X_{i_2})\in\mathbb R^2,
\qquad Z=(X_{j_1},X_{j_2})\in\mathbb R^2,
\qquad X=X_h.
\]

Because conditioning is on disjoint original coordinates, `X,Y,Z` remain independent, and their one- or two-dimensional product densities satisfy

\[
0\le f_X\le1,
\qquad 0\le \rho_Y\le1,
\qquad 0\le\rho_Z\le1.
\]

Assume that the conditional polynomial has the form

\[
Q=aX^2+2X(u^TY+\beta)+F(Y)+2Y^TCZ+G(Z),
\tag{1.1}
\]

where

- `a != 0`;
- `u in R^2` and `beta in R` are arbitrary;
- `C` is an invertible real `2x2` matrix;
- `F,G` are arbitrary real quadratic-affine functions (indeed their exact form is irrelevant below, because they only enter through unit-modulus phases).

The essential structural condition is that the selected hub coordinate `h` has **no direct coupling to the selected `Z` pair**. Coupling from `h` to the selected `Y` pair is completely arbitrary. All same-side curvature on `Y` and `Z`, all coefficients involving conditioned coordinates, and all induced affine terms are retained.

Then the law of `Q` has a continuous density and

\[
\boxed{
\|p_Q\|_\infty
\le 72^{1/3}|a\det C|^{-1/3}
}
\tag{1.2}
\]

with

\[
72^{1/3}=4.160167646103808\ldots.
\]

Equivalently, for every interval `L`,

\[
\boxed{
\Pr\{Q\in L\}
\le72^{1/3}|a\det C|^{-1/3}|L|.
}
\tag{1.3}
\]

Since the bound is uniform in every conditioned outside coordinate, averaging the conditional laws proves the same estimate for the full ambient quadratic form.

### Original-coordinate overlap-one determinant form

Put

\[
R=\{h,i_1,i_2\},\qquad T=\{h,j_1,j_2\}.
\]

These triples overlap in exactly the physical coordinate `h`. Under the one-sided zero condition

\[
A_{h,j_1}=A_{h,j_2}=0,
\]

the mixed physical minor is block lower triangular:

\[
A[R,T]=
\begin{pmatrix}
 a&0&0\\
 *&&\\
 *&C&
\end{pmatrix},
\]

so

\[
\det A[R,T]=a\det C.
\tag{1.4}
\]

Thus (1.2) can be written

\[
\boxed{
\|p_Q\|_\infty
\le72^{1/3}|\det A[R,T]|^{-1/3}
}
\tag{1.5}
\]

for this one-sided overlap-one geometry. This is the first point of the run: an overlap-one `3x3` determinant can be paid directly without first converting it to a disjoint `3x3` physical cross minor.

## 2. Scalar ingredient: a translation-uniform L^3 Fresnel estimate

We need no pointwise decay. The needed scalar statement is integrated in time.

### Lemma 2.1

Let `W` be any real random variable with probability density `f` satisfying `0<=f<=1`. For every `m in R` and every `a != 0`, define

\[
H_m(t)=\mathbb E\,e^{ita(W-m)^2}.
\]

Then

\[
\boxed{
\|H_m\|_{L^3(\mathbb R_t)}
\le2(2\pi)^{1/3}|a|^{-1/3},
}
\tag{2.1}
\]

uniformly in the translation `m` and in the law of `W`.

#### Proof

Let `R=(W-m)^2`. Its density on `(0,infinity)` is

\[
h_m(r)=\frac{f(m+\sqrt r)+f(m-\sqrt r)}{2\sqrt r}.
\tag{2.2}
\]

Since the numerator is between zero and two, `s^{3/2} <= sqrt(2) s` for `0<=s<=2` gives

\[
\begin{aligned}
\int_0^\infty h_m(r)^{3/2}\,dr
&\le\int_0^\infty
 \frac{f(m+\sqrt r)+f(m-\sqrt r)}{2r^{3/4}}\,dr\\
&=\int_{\mathbb R}f(x)|x-m|^{-1/2}\,dx.
\end{aligned}
\tag{2.3}
\]

Among all probability densities bounded by one, the last integral is maximized by placing unit mass on the length-one interval closest to `m`. Therefore

\[
\int_{\mathbb R}f(x)|x-m|^{-1/2}\,dx
\le\int_{-1/2}^{1/2}|s|^{-1/2}\,ds
=2\sqrt2.
\tag{2.4}
\]

Consequently

\[
\|h_m\|_{3/2}\le(2\sqrt2)^{2/3}=2.
\tag{2.5}
\]

With Fourier convention

\[
\widehat h(t)=\int e^{itr}h(r)\,dr,
\]

Hausdorff--Young, interpolating `L^1 -> L^infinity` with Plancherel, gives

\[
\|\widehat h_m\|_3
\le(2\pi)^{1/3}\|h_m\|_{3/2}
\le2(2\pi)^{1/3}.
\tag{2.6}
\]

Finally `H_m(t)=\widehat h_m(at)`, so scaling yields (2.1). QED.

### Why this does not violate the live phase-alignment correction

The correction says that no uniform pointwise estimate of the form

\[
|\mathbb E e^{itW^2}|\lesssim |t|^{-1/2}
\]

holds over all cap-one densities. Lemma 2.1 asserts only an `L^3(dt)` norm bound. Phase-aligned fragmented supports may create isolated large-frequency peaks; they cannot make this `L^3` norm exceed the stated constant. No pointwise van der Corput premise appears below.

## 3. Two-dimensional bilinear ingredient

For an invertible real `2x2` matrix `C` and `t != 0`, define

\[
(T_tg)(y)=\int_{\mathbb R^2}e^{i2t y^TCz}g(z)\,dz.
\tag{3.1}
\]

Plancherel and the linear change of Fourier variables give the exact operator norm

\[
\boxed{
\|T_tg\|_2
=\frac{\pi}{|t|\sqrt{|\det C|}}\|g\|_2.
}
\tag{3.2}
\]

Indeed the frequency is `2t C^T y`, whose Jacobian is `4t^2|det C|`, while `||hat g||_2^2=(2pi)^2||g||_2^2`.

This is the same source-coordinate Plancherel mechanism underlying the completed fleet04/B09 dense-self-cross theorem, but here only two cross directions are present; the third smoothing direction is supplied by Lemma 2.1.

## 4. Proof of the theorem

For each fixed `y`, integrate only the physical hub variable:

\[
H_y(t)=\int_{\mathbb R}f_X(x)
 e^{it(a x^2+2x(u^Ty+\beta))}\,dx.
\tag{4.1}
\]

Completing the square gives

\[
a x^2+2x(u^Ty+\beta)
=a\left(x+\frac{u^Ty+\beta}{a}\right)^2
-\frac{(u^Ty+\beta)^2}{a}.
\tag{4.2}
\]

The final term is a unit-modulus phase. The first term is a translated scalar square. Hence Lemma 2.1 gives, uniformly in `y`,

\[
\|H_y\|_3\le B_a,
\qquad
B_a:=2(2\pi)^{1/3}|a|^{-1/3}.
\tag{4.3}
\]

Define

\[
h(t)=\left(\int \rho_Y(y)|H_y(t)|^2\,dy\right)^{1/2}.
\tag{4.4}
\]

Minkowski in `L^{3/2}` yields

\[
\begin{aligned}
\|h\|_3^2
&=\left\|\int \rho_Y(y)|H_y(\cdot)|^2dy\right\|_{3/2}\\
&\le\int\rho_Y(y)\|H_y\|_3^2dy
\le B_a^2.
\end{aligned}
\tag{4.5}
\]

Thus

\[
\boxed{\|h\|_3\le B_a.}
\tag{4.6}
\]

Now the characteristic function of (1.1) is

\[
\phi(t)=\iint \rho_Y(y)\rho_Z(z)H_y(t)
 e^{it(F(y)+2y^TCz+G(z))}\,dy\,dz.
\tag{4.7}
\]

There are two simultaneous pointwise estimates.

First, by Cauchy--Schwarz under the probability measure `rho_Y(y)dy`,

\[
|\phi(t)|
\le\int\rho_Y(y)|H_y(t)|dy
\le h(t).
\tag{4.8}
\]

Second, let

\[
a_t(y)=\rho_Y(y)H_y(t)e^{itF(y)},
\qquad
b_t(z)=\rho_Z(z)e^{itG(z)}.
\]

Because `rho_Y<=1`,

\[
\|a_t\|_2^2
=\int\rho_Y(y)^2|H_y(t)|^2dy
\le h(t)^2.
\tag{4.9}
\]

Because `rho_Z<=1` and has total mass one,

\[
\|b_t\|_2^2\le1.
\tag{4.10}
\]

Cauchy--Schwarz followed by (3.2) gives

\[
|\phi(t)|
\le\frac{\pi}{|t|\sqrt{|\det C|}}h(t).
\tag{4.11}
\]

Combining (4.8) and (4.11),

\[
|\phi(t)|
\le h(t)w_K(t),
\qquad
w_K(t)=\min\left(1,\frac K{|t|}\right),
\qquad
K=\pi|\det C|^{-1/2}.
\tag{4.12}
\]

The crucial point is that the rank-two bilinear block contributes exactly the integrable fractional weight needed to pair with the hub's `L^3` control:

\[
\int_{\mathbb R}w_K(t)^{3/2}dt
=2K+2\int_K^\infty(K/t)^{3/2}dt
=6K.
\tag{4.13}
\]

Hence

\[
\|w_K\|_{3/2}=(6K)^{2/3}.
\tag{4.14}
\]

Hölder with exponents `3` and `3/2`, followed by (4.6), gives

\[
\begin{aligned}
\|\phi\|_1
&\le\|h\|_3\|w_K\|_{3/2}\\
&\le2(2\pi)^{1/3}|a|^{-1/3}
 (6\pi|\det C|^{-1/2})^{2/3}.
\end{aligned}
\tag{4.15}
\]

Fourier inversion therefore gives

\[
\begin{aligned}
\|p_Q\|_\infty
&\le\frac1{2\pi}\|\phi\|_1\\
&\le 2^{1/3}6^{2/3}|a\det C|^{-1/3}\\
&=72^{1/3}|a\det C|^{-1/3},
\end{aligned}
\tag{4.16}
\]

which is (1.2). Moreover `phi in L^1`; Fourier inversion gives a bounded continuous representative of the density. Integrating that density over an interval proves (1.3). QED.

## 5. Ambient conditioning and all signs

Nothing in the proof assumes signs of `a`, `det C`, or of the remaining quadratic coefficients. Only their absolute magnitudes enter the norm estimates. Conditioning every outside original coordinate leaves the five selected physical coordinates independent with their original cap-one densities. Every cross term from a selected coordinate to a conditioned coordinate becomes an arbitrary affine term; these are already absorbed into `beta,F,G`. The estimate is independent of their values. Therefore averaging conditional densities preserves (1.2).

No moment, compact-support, connected-support, Gaussian, log-concavity, centering, identical-law, or diagonal-basis assumption is introduced.

## 6. Target-valid regression where no disjoint physical 3x3 receiver exists

Consider the `5x5` symmetric matrix with

\[
A_{00}=1,\qquad A_{13}=A_{31}=1,\qquad A_{24}=A_{42}=1,
\]

and all other entries zero. Its spectrum is exactly

\[
\{-1,-1,1,1,1\}.
\]

Thus it satisfies the exact target spectral hypothesis. Choose

\[
h=0,\quad Y=(X_1,X_2),\quad Z=(X_3,X_4).
\]

Then `a=1`, `C=I_2`, and the one-sided zero gate holds. The theorem gives

\[
\boxed{\|p_Q\|_\infty\le72^{1/3}<4.161.}
\tag{6.1}
\]

This example has only five coordinates, so two disjoint triples do not exist at all. Thus a theorem requiring a literal disjoint `3x3` physical cross minor cannot even be formulated on this matrix. The overlap-one receiver is genuinely different rather than a weaker restatement of a disjoint-minor theorem.

## 7. Required fleet04/B09 partner application

The completed designated partner theorem is:

> If disjoint original-coordinate banks `S,T` have equal size `r>2` and the actual physical cross block `K=A[S,T]` is invertible, arbitrary dense same-side curvature and arbitrary affine terms are allowed and
> \[
> \|p_Q\|_\infty\le\frac r{r-2}|\det K|^{-1/r}.
> \]
> In particular, for a literal physical `3x3` block,
> \[
> \|p_Q\|_\infty\le3|\det K|^{-1/3},
> \]
> with a continuous density.

Source: `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

Apply it to the target-valid `6x6` symmetric matrix

\[
A_{00}=1,
\qquad
A_{05}=A_{50}=1,
\qquad
A_{13}=A_{31}=1,
\qquad
A_{24}=A_{42}=1,
\]

all other entries zero. Its spectrum is

\[
\{-1,-1,(1-\sqrt5)/2,1,1,(1+\sqrt5)/2\},
\]

so at least five eigenvalues have modulus at least one. For

\[
S=\{0,1,2\},\qquad T=\{3,4,5\},
\]

the physical cross block is

\[
K=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad |\det K|=1.
\]

Therefore the partner theorem gives the actual inequality

\[
\boxed{\|p_Q\|_\infty\le3.}
\tag{7.1}
\]

The new theorem also applies after conditioning `X_5`: use `h=0`, `Y=(X_1,X_2)`, `Z=(X_3,X_4)`, so `a=1,C=I_2`; it gives `72^(1/3)`. Thus the partner endpoint is stronger on this six-coordinate matrix, while the five-coordinate matrix in Section 6 shows why the overlap-one receiver is independently needed.

## 8. Structural reduction: disjoint versus overlapping third-minor energy

The following algebra is useful for placing the new receiver in the full proof graph.

For symmetric `A`, define the total squared third-minor energy

\[
\mathcal E_3(A)
:=e_3(A^2)
=\sum_{R,C\in{[n]\choose3}}\det A[R,C]^2.
\tag{8.1}
\]

The equality is Cauchy--Binet. If `A` has at least three eigenvalues of absolute value at least one, then

\[
\mathcal E_3(A)\ge1.
\tag{8.2}
\]

Define the disjoint part

\[
\mathcal D_3(A)
:=\sum_{R\cap C=\varnothing}\det A[R,C]^2.
\tag{8.3}
\]

For a uniformly random Bernoulli physical partition `[n]=I sqcup J`, let `B=A[I,J]`. Cauchy--Binet gives

\[
Z_3(B):=e_3(BB^T)
=\sum_{R\subset I,\ C\subset J\atop |R|=|C|=3}\det A[R,C]^2.
\]

Each ordered disjoint pair `(R,C)` lands in the prescribed sides with probability `2^{-6}`, hence

\[
\boxed{
\mathbb E_{I|J}Z_3(A[I,J])=\mathcal D_3(A)/64.
}
\tag{8.4}
\]

Therefore some literal physical partition satisfies

\[
Z_3(A[I,J])\ge\mathcal D_3(A)/64.
\tag{8.5}
\]

The preceding fleet03/B09 r40 report proved, pending independent review, that any fixed cut with `Z_3>0` satisfies

\[
\|p_Q\|_\infty
\le C_3 Z_3^{-1/6},
\qquad
C_3=3\,2^{4/3}e^{1/3}<10.551.
\tag{8.6}
\]

Combining (8.5) and (8.6) gives the conditional structural consequence

\[
\|p_Q\|_\infty
\le2C_3\mathcal D_3(A)^{-1/6}.
\tag{8.7}
\]

In particular, if `mathcal D_3(A)>=1/2`, then

\[
\|p_Q\|_\infty<23.685.
\tag{8.8}
\]

Thus, **conditional on the pending independent review of r40**, the hard branch may be restricted to

\[
\mathcal D_3(A)<1/2,
\qquad
\sum_{R\cap C\ne\varnothing}\det A[R,C]^2>1/2.
\tag{8.9}
\]

That is exactly an overlapping-minor regime. The theorem of this run pays a nontrivial overlap-one subbranch.

## 9. Exact Schur identities for the remaining overlap classes

These identities are purely algebraic and indicate the next analytic receivers.

### 9.1 Fixed scalar pivot, overlap one

Fix `h` with `a=A_hh != 0`, and let

\[
S_h=A_{\hat h,\hat h}
-a^{-1}A_{\hat h,h}A_{h,\hat h}
\]

be the physical scalar Schur complement. For disjoint physical pairs `P,Q` not containing `h`,

\[
\boxed{
\det A[\{h\}\cup P,\{h\}\cup Q]
=a\det S_h[P,Q].
}
\tag{9.1}
\]

Thus fixed-pivot overlap-one energy equals `a^2` times disjoint `2x2` minor energy in the Schur complement. The theorem of this run handles the source-coordinate case in which the selected hub has no direct coupling to `Q`, so the Schur correction does not destroy the physical `2x2` crossing.

### 9.2 Fixed physical pair, overlap two

If `H` is a physical pair with invertible core `E=A[H,H]`, let

\[
S_H=A_{H^c,H^c}-A_{H^c,H}E^{-1}A_{H,H^c}.
\]

For distinct `i,j` outside `H`,

\[
\boxed{
\det A[H\cup\{i\},H\cup\{j\}]
=\det(E)(S_H)_{ij}.
}
\tag{9.2}
\]

So fixed-pair overlap-two third-minor energy is a pair-core determinant squared times off-diagonal Frobenius energy of the physical Schur complement.

The full overlap energy therefore naturally asks for a hierarchy:

- overlap zero: rank-three disjoint crossing, paid by r40 pending review;
- overlap one: scalar Fresnel pivot + rank-two crossing, partially paid here;
- overlap two: two-dimensional physical core + one crossing direction;
- overlap three: a physical principal `3x3` core.

The analytic difficulty is not the determinant identities; it is retaining the cap-one product provenance when the Schur correction couples the same physical variables used by the smoothing receiver.

## 10. Precise remaining gap

The theorem requires the one-sided zero gate

\[
A_{h,j_1}=A_{h,j_2}=0.
\tag{10.1}
\]

For a general overlap-one mixed minor, the hub also couples to the `Z` pair:

\[
Q=aX^2+2X(u^TY+v^TZ+\beta)
+F(Y)+2Y^TCZ+G(Z).
\tag{10.2}
\]

Completing the square changes the formal bilinear block to

\[
C-a^{-1}uv^T,
\]

and indeed

\[
\det
\begin{pmatrix}a&v^T\\u&C\end{pmatrix}
=a\det(C-a^{-1}uv^T).
\tag{10.3}
\]

But the translation of the hub density then depends simultaneously on both `Y` and `Z`. One cannot rotate it away or treat the small extra coupling as a small random error: supports may be unbounded and fragmented, and the live corrections forbid such a step. The scalar `L^3(dt)` estimate remains uniform under translations, but the translated amplitude now sits *inside* the bilinear `Y-Z` kernel and the simple Plancherel factorization (4.9)-(4.11) no longer applies.

Accordingly the next B09 debt is

**`QFORM-OVERLAP1-TWOSIDED-VECTORVALUED-FRESNEL-v1`**:

prove a vector-valued/bilinear estimate for (10.2) that pays the full determinant in (10.3), or produce a valid obstruction to that analytic interface. A successful estimate of the same determinant homogeneity would cover every overlap-one third minor and would combine naturally with the disjoint-energy reduction (8.9).

This is a different mechanism from the previous near-coloop work and therefore satisfies the instruction to change mechanism after repeated runs on the same target while preserving all prior work.

## 11. Deterministic checks

`CHECK.py` verifies:

1. `72^(1/3)=4.160167646103808...`;
2. the five-coordinate regression has spectrum `{-1,-1,1,1,1}`;
3. the six-coordinate partner regression is target-valid and has selected `3x3` determinant one;
4. the scalar-pivot determinant identity (9.1) on 100 seeded random symmetric matrices;
5. the pair-pivot determinant identity (9.2) on 100 seeded random symmetric matrices;
6. the global Cauchy--Binet identity (8.1);
7. the exact Bernoulli-partition expectation (8.4) by enumerating every partition of a seeded `7x7` symmetric matrix.

All checks pass to floating-point relative error below `6e-16` except the partition identity, whose relative discrepancy is below `9e-17`. These checks validate algebra and arithmetic only; they are not an independent analytic review.

## 12. Source integrity and scope


Consumed corrections include law-uniform pointwise quadratic-phase decay being false, no independence after rotation, naive fiber-sup dimension loss, and the fresh fleet03/B15 correction that a nonzero square plus a large affine slope does not give the claimed slope-rescue bound. None is used as a premise here.

The designated partner result was read from its completed current-QFORM source and applied in Section 7. The previous r40 theorem is used only in the explicitly conditional structural consequence of Section 8 and retains its `pending independent review` status.

Changed-file allowlist for this run consists only of this run's canonical report/check files in the authorized fleet03/B09 path and the prescribed fleet03/B09 brain handoff/run/memory records. Manual content review found only mathematical statements, public-style repository paths and commit hashes; no credentials, signed download URLs, personal material, account secrets or unrelated data are included. No installation, permission, visibility, scheduler, notification, email, cross-account authentication, paid model/API/Codex or remote-workflow action was performed.

Full QFORM status: **OPEN**.
Full-target continuity status: **OPEN**.
Branch continuity status: **PROVED** for Theorem (1.2), pending independent review of the theorem itself.
