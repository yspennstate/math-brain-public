# fleet01/B09 — rank-two cross block plus transverse curvature

Run: `20260922T124649Z-fleet01-B09-qform-transverse-r11`  
Assignment: `Bilinear block mechanism`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and live corrections

The sole target is the full arbitrary-law statement: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove

\[
\Pr\{X^TAX\in I\}\le C|I|
\]

with one universal finite constant, or give a genuine counterexample. A continuous density is a separate stronger conclusion.

This run used fresh `math-research-brain/main` at source commit `921cd237e6a85b633fa86ada50a830f59f1696c4` and consumed the live correction inbox before publication. In particular:

- law-uniform pointwise one-variable quadratic-phase decay is false;
- rotation to the eigenbasis does not preserve coordinate independence;
- unrestricted spectral-fiber suprema can lose dimension;
- a rank-two cross minor alone does not force bounded density;
- generic X-ray control alone does not control the two-sheet branch;
- the newest partner correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` says the three-large-eigenvalue hypothesis does not force one useful original-coordinate scalar pivot with rank-two Schur cross block.

No refuted premise is used below.

## 2. Partner theorem actually consumed and applied

The assigned partner `fleet02/B09` has a newer completed report:

- repository `yspennstate/math-open-problems`;
- commit `17dec75dc10459933f8bfde30daa86d1c6d90a6a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T124417Z-fleet02-B09-QFORM-r2/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-LP-v1` says that for an original-coordinate split with arbitrary quadratic-affine terms on both sides and rank-two cross block having nonzero singular values `s1,s2`, with `D=s1 s2`, the output has, for every finite `p>=2`,

\[
\|p_Q\|_p\le (2p)^{1-1/p}D^{-(p-1)/(2p)}.
\]

In particular,

\[
\|p_Q\|_3\le 6^{2/3}D^{-1/3}.
\tag{2.1}
\]

The same report records the source-valid correction that extracting one physical Schur pivot is not universally possible. The new theorem below therefore does **not** ask for an original-coordinate scalar pivot. Instead it spends quadratic curvature in the one-dimensional **left kernel of the rank-two cross block inside a three-coordinate product packet**. Rotating inside that three-coordinate packet is used only analytically: the joint packet density is still bounded by one after an orthogonal change of variables, while independence is never claimed for the rotated coordinates.

Equation (2.1) is also applied quantitatively in Section 7 to obtain an interpolation ladder with the new endpoint.

## 3. New theorem

### Theorem 3.1 — `QFORM-RANK2-CROSS-TRANSVERSE-CURVATURE-v1`

Let the original independent coordinates be partitioned into disjoint sets `S,T,R`, with `|S|=3`. Condition on `R`. Write the remaining quadratic-affine polynomial as

\[
q(s,t)=s^T B s+2s^TMt+t^TCt+\ell_S^Ts+\ell_T^Tt+c,
\]

where `B` and `C` are symmetric and `M` is `3 x |T|`. Assume

1. `rank(M)=2`;
2. its two nonzero singular values are `s_1,s_2>0`, and `D=s_1s_2`;
3. `e` is a unit vector spanning `ker(M^T)`;
4. the transverse kernel curvature
   \[
   \kappa=e^TBe
   \]
   is nonzero.

Then, uniformly over the outside conditioning and hence unconditionally, `Q=X^TAX` has a bounded **continuous** density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm tc}\,D^{-3/7}|\kappa|^{-1/7},
\qquad
C_{\rm tc}=7\pi^{-1/7}\Gamma(1/3)^{3/7}<9.068.
}
\tag{3.1}
\]

Consequently every interval `I` satisfies

\[
\boxed{
\Pr\{Q\in I\}
\le C_{\rm tc}D^{-3/7}|\kappa|^{-1/7}|I|.
}
\tag{3.2}
\]

The theorem allows arbitrary same-side curvature `B,C`, arbitrary affine terms, arbitrary outside couplings, arbitrary support geometry, and arbitrary admissible input densities. It uses no moment, log-concavity, continuity, compact-support, or eigenbasis-independence assumption.

The resource in (3.1) is naturally

\[
\Theta:=D^3|\kappa|.
\]

Indeed `\|p_Q\|_\infty<=C_tc Theta^{-1/7}`. Under scalar rescaling `A -> lambda A`, `D -> |lambda|^2D` and `|kappa| -> |lambda||kappa|`, so `Theta -> |lambda|^7 Theta` and the bound scales exactly as `|lambda|^{-1}`, as a one-dimensional density bound should.

## 4. Weighted quadratic-energy lemma

The missing ingredient at rank two is not another pointwise Fresnel estimate. It is an **integrated weighted energy** in the transverse curvature variable.

### Lemma 4.1 — one-dimensional `1/3` quadratic potential

If `h` is measurable, `0<=h<=1`, and `m=int h<=1`, then for every real `tau`,

\[
\int_\mathbb R h(x)|x^2-\tau|^{-1/3}\,dx
\le 3\,2^{2/3}m^{1/3}.
\tag{4.1}
\]

#### Proof

First let `p` be a probability density bounded by `L`. For every `r`, symmetric decreasing rearrangement of the kernel gives

\[
\int p(x)|x-r|^{-2/3}dx
\le L\int_{-1/(2L)}^{1/(2L)}|u|^{-2/3}du
=3\,2^{2/3}L^{2/3}.
\tag{4.2}
\]

If `tau<=0`, then `|x^2-tau|^{-1/3}<=|x|^{-2/3}`, so (4.2) applies. If `tau=r^2>0`, then

\[
|x^2-r^2|^{-1/3}
=\bigl(|x-r|^{-2/3}|x+r|^{-2/3}\bigr)^{1/2}
\le { |x-r|^{-2/3}+|x+r|^{-2/3}\over2},
\]

and (4.2) applies to both translates. For nonzero `m`, apply the probability statement to `p=h/m`, whose density cap is `1/m`; multiplying by `m` gives (4.1). The case `m=0` is trivial. QED.

### Lemma 4.2 — transverse weighted Fresnel energy

After a thin SVD of `M`, choose an orthogonal coordinate system on the three-dimensional `S` packet whose first coordinate `z` is the kernel direction `e` and whose remaining coordinates are `y in R^2`. Let `F(z,y)` be the transformed joint density of `X_S`. Since the original three coordinates are independent with scalar density caps one,

\[
0\le F\le1,\qquad \int F=1.
\]

For fixed outside variables and fixed `y`, the quadratic phase in `z` has the form

\[
\kappa z^2+L(y)z+G(y).
\]

Set

\[
a_t(y)=\int_\mathbb R F(z,y)
  e^{it(\kappa z^2+L(y)z+G(y))}\,dz.
\]

Then

\[
\boxed{
\int_0^\infty t^{-2/3}\|a_t\|_2^2dt
\le 6\Gamma(1/3)|\kappa|^{-1/3}.
}
\tag{4.3}
\]

#### Proof

Let

\[
m(y)=\int F(z,y)dz.
\]

This is the density of a two-dimensional orthogonal projection of the three-coordinate product law. By the Livshyts--Paouris--Pivovarov product-marginal theorem,

\[
\|m\|_\infty\le2,\qquad \int m=1.
\tag{4.4}
\]

Fix `y` and complete the square in `z`; write the shifted variable as `x`. For `epsilon>0`, Fubini is justified after inserting `e^{-epsilon t}` and

\[
\int_0^\infty t^{-2/3}e^{-\epsilon t}e^{itu}dt
=\Gamma(1/3)(\epsilon-iu)^{-1/3}.
\]

Its absolute value is at most `Gamma(1/3)|u|^{-1/3}` for `u!=0`. The zero set of the quadratic difference has two one-dimensional components in the `(x,x')` plane and therefore zero two-dimensional Lebesgue measure. Hence Lemma 4.1, applied first in `x` with `tau=(x')^2`, gives

\[
\int_0^\infty t^{-2/3}e^{-\epsilon t}|a_t(y)|^2dt
\le
3\,2^{2/3}\Gamma(1/3)|\kappa|^{-1/3}m(y)^{4/3}.
\]

Letting `epsilon downarrow0` by monotone convergence on the left and then integrating in `y`,

\[
\int m(y)^{4/3}dy
\le \|m\|_\infty^{1/3}\int m
\le2^{1/3}.
\]

The powers of two combine to `2`, proving (4.3). QED.

The point is that (4.3) survives the live correction refuting uniform pointwise van der Corput. It is an averaged `t`-energy statement derived directly from the density cap and a singular-potential estimate.

## 5. Bilinear Plancherel plus the weighted energy

Use the same thin SVD of `M` on the `T` side. Let `v in R^2` be the two active right-singular coordinates and integrate all orthogonal `T` coordinates into the complex amplitude `b_t(v)`. Its modulus is bounded by the genuine two-dimensional orthogonal marginal density `rho_T(v)`. Again by the product-marginal theorem,

\[
\|\rho_T\|_\infty\le2,\qquad \int\rho_T=1,
\]

so

\[
\|b_t\|_2\le\sqrt2.
\tag{5.1}
\]

With `Sigma=diag(s_1,s_2)`, the conditional characteristic function is

\[
\phi(t)=e^{itc}\int_{\mathbb R^2}\int_{\mathbb R^2}
 a_t(y)b_t(v)e^{2it y^T\Sigma v}\,dy\,dv.
\]

Two-dimensional Plancherel therefore gives

\[
|\phi(t)|
\le \pi |t|^{-1}D^{-1/2}\|a_t\|_2\|b_t\|_2
\le \pi\sqrt2\,D^{-1/2}|t|^{-1}\|a_t\|_2.
\tag{5.2}
\]

For any `T_0>0`, Cauchy--Schwarz with the weight from (4.3) yields

\[
\begin{aligned}
\int_{T_0}^\infty|\phi(t)|dt
&\le \pi\sqrt2 D^{-1/2}
 \left(\int_{T_0}^\infty t^{-2/3}\|a_t\|_2^2dt\right)^{1/2}
 \left(\int_{T_0}^\infty t^{-4/3}dt\right)^{1/2}\\
&\le 6\pi\sqrt{\Gamma(1/3)}
 D^{-1/2}|\kappa|^{-1/6}T_0^{-1/6}.
\end{aligned}
\tag{5.3}
\]

The same estimate holds on the negative half-line. Together with `|phi(t)|<=1`,

\[
\int_\mathbb R|\phi(t)|dt
\le2T_0+12\pi\sqrt{\Gamma(1/3)}
D^{-1/2}|\kappa|^{-1/6}T_0^{-1/6}.
\tag{5.4}
\]

The right side is minimized at

\[
T_*=[\pi\sqrt{\Gamma(1/3)}]^{6/7}
D^{-3/7}|\kappa|^{-1/7}.
\]

At the minimizer, the tail term equals `12T_*`, so

\[
\int_\mathbb R|\phi(t)|dt\le14T_*.
\]

Fourier inversion now gives

\[
\|p_Q\|_\infty
\le {14T_*\over2\pi}
=7\pi^{-1/7}\Gamma(1/3)^{3/7}
D^{-3/7}|\kappa|^{-1/7},
\]

which is (3.1). The `L^1` characteristic-function bound also gives a continuous density representative.

All constants are uniform in the coordinates conditioned outside `S union T`. Equivalently, the unconditional characteristic function is an average of the conditional characteristic functions and has the same `L^1` bound by Tonelli; hence the unconditional law also has the same bounded continuous density. QED.

## 6. Exact stress test: repair of the partner's rank-two obstruction

The previous partner report exhibited the sharp obstruction

\[
Q_0=(X_1+Y_1)^2-(X_2+Y_2)^2,
\]

whose cross block is `diag(1,-1)` but whose density can be logarithmically unbounded for admissible uniform inputs. Thus `D=1` alone is insufficient.

Now add one independent original coordinate with genuine transverse curvature:

\[
Q_c=(X_1+Y_1)^2-(X_2+Y_2)^2+cZ^2,
\qquad c\ne0.
\tag{6.1}
\]

Use

`S={X1,X2,Z}`, `T={Y1,Y2}`.

Then the cross block has singular values `1,1`, so `D=1`; its left kernel is exactly the `Z` direction; and

\[
\kappa=c.
\]

Theorem 3.1 therefore gives the genuinely endpoint-linear estimate

\[
\boxed{
\|p_{Q_c}\|_\infty\le C_{\rm tc}|c|^{-1/7}.
}
\tag{6.2}
\]

For `|c|>=1`, the full matrix has spectrum

\[
\{2,-2,c,0,0\},
\]

so (6.1) lies in the owner's three-large-eigenvalue target class. In particular, at `c=1`,

\[
\|p_{Q_1}\|_\infty<9.068.
\]

This directly identifies what repairs the partner's obstruction: a rank-two bilinear channel plus nonzero quadratic curvature **transverse to that channel**. No original-coordinate scalar Schur pivot is required.

The partner's newer correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` remains fully respected: Theorem 3.1 is a local implication conditional on a three-coordinate packet, not a claim that every target matrix has such a packet.

## 7. Partner-applied interpolation ladder

The partner's finite-`p` theorem (2.1) applies to the exact same rank-two cross setting before the new curvature endpoint is used. Combining its `L^3` bound

\[
\|p_Q\|_3\le6^{2/3}D^{-1/3}
\]

with (3.1), ordinary `L^p` interpolation gives, for every `3<=p<=infinity`,

\[
\boxed{
\|p_Q\|_p
\le
6^{2/p}C_{\rm tc}^{1-3/p}
D^{-(3p-2)/(7p)}
|\kappa|^{-(p-3)/(7p)}.
}
\tag{7.1}
\]

Thus the named partner result is used quantitatively, not merely cited. At `p=3`, (7.1) is exactly the partner bound; at `p=infinity`, it is the new transverse-curvature theorem.

## 8. Compact conditional end-to-end route and first unpaid implication

The bilinear branch now has three rigorously distinct levels:

1. **rank at least three cross block:** the prior `QFORM-RANKR-BILINEAR-PLANCHEREL-v1` gives a continuous bounded density under arbitrary same-side curvature;
2. **rank exactly two cross block:** the partner `QFORM-RANK2-CROSS-LP-v1` gives every finite `L^p` norm but cannot give `L^infinity` in general;
3. **rank exactly two plus transverse kernel curvature in a three-coordinate packet:** Theorem 3.1 upgrades the borderline rank-two channel to a continuous `L^infinity` density without requiring an independent physical scalar pivot.

The first missing target-level implication is therefore a product-preserving **aggregation/extraction trichotomy**:

> From `s_3(A)>=1`, prove with universal quantitative constants that one of the following occurs before paying reciprocal local-minor costs: (i) a disjoint coordinate cut with a controlled rank-three cross singular product; (ii) a three-original-coordinate packet `S` and disjoint `T` with rank-two cross block satisfying `D^3|kappa|>=c_0`; or (iii) one of the already proved diffuse/high-cardinality/square-smoothing branches applies. Extra spectral components must be included rather than discarded.

The latest partner falsifier shows that option (ii) cannot be replaced by the stronger but false assertion that a useful **single physical Schur pivot** always exists. The new theorem enlarges the local resource from a coordinate pivot to a rotated transverse direction inside a bounded three-coordinate product packet, while keeping the original product density through the valid joint `L^infinity` and projection bounds.

## 9. Status

Outcome: `ESSENTIAL_STEP_APPLIED`.

Proved in this run:

- `QFORM-RANK2-CROSS-TRANSVERSE-CURVATURE-v1`, equations (3.1)-(3.2);
- the weighted quadratic-energy estimate (4.3), which survives the pointwise-oscillatory-decay correction;
- the exact target-family repair (6.2) of the partner's rank-two logarithmic obstruction;
- the partner-applied interpolation ladder (7.1).

Not proved:

- the global aggregation/extraction trichotomy above;
- control of arbitrary extra spectral components in full generality;
- the full QFORM conjecture.

No numerical experiment is used as proof. The constant `C_tc` is the exact closed form displayed above; the decimal `<9.068` is only its evaluation.
