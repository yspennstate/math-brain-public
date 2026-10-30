SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T03:22:40Z.
attacking: QFORM-SMALLPAIR-SHEARVOLUME-HEAVYCORE-COMPILER-v1 by spending the complete rank-three Pluecker law before selecting a physical split, then compiling low disjointness into a three-hub near-span certificate.

# fleet03/B06 r51 — rank-three Pluecker disjointness compiler for the singular-T shear-volume branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: curved fiber integration / quantitative inequalities and rigorous computations  
Startup control commit: `yspennstate/math-research-brain@d5fea91584899bb4ce292dfcc49410064c552ac9`  
Publication control refresh observed: `yspennstate/math-research-brain@5eae7feafe693618083d0e2342554d2c4af06ee4`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW WEIGHTED RANK-THREE CROSSING THEOREM + LOW-DISJOINTNESS THREE-HUB CERTIFICATE + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is added. The proof below uses only literal original-coordinate bank splits. It does not use a fiber supremum, an arbitrary-joint coarea bound, a law-uniform pointwise quadratic-phase decay estimate, or the refuted critical rank-one same-bank half-Riesz interface.

## 1. Immediate predecessor and exact debt

The immediate predecessor is

`yspennstate/math-open-problems@8bef4dcb05d0c755e9c8df8f01e72c225dee2614`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T021836Z-fleet03-B06-qform-auto11-r50/REPORT.md`.

Its singular-T shear-flat normal form is

\[
A=\begin{pmatrix}H&E\\E^T&C\end{pmatrix},\qquad
C-E^TH^{-1}E=D+E^TTE,
\tag{1.1}
\]

with `H` a literal invertible physical `2 x 2` block, `D` diagonal on the remaining ORIGINAL coordinates, `E` a real `2 x m` row-rank-two matrix, and

\[
T=\lambda vv^T,\qquad \lambda\ne0,\qquad \|v\|_2=1.
\tag{1.2}
\]

Put

\[
G=EE^T,\qquad W=\det G>0,
\qquad U=H^{-1}+\lambda vv^T.
\tag{1.3}
\]

Removing only the coordinate-separable diagonal phase gives the exact rank-three core

\[
A_0:=A-\operatorname{diag}(0,0,D)=R^TM_3R,
\tag{1.4}
\]

where

\[
R=\begin{pmatrix}I_2&H^{-1}E\\0&v^TE\end{pmatrix},
\qquad
M_3=\operatorname{diag}(H,\lambda).
\tag{1.5}
\]

The predecessor proved the exact nonzero-eigenvalue product

\[
P:=|\operatorname{pdet}_*(A_0)|
=|\lambda|\left[
|\det H|\,v^TGv+
\frac{W}{|\det H|}\|Hv\|_2^2
\right].
\tag{1.6}
\]

Write the two positive currencies in (1.6) as

\[
P_{\rm tan}=|\det H|\,|\lambda|v^TGv,
\qquad
P_{\rm sh}=\frac{|\lambda|W}{|\det H|}\|Hv\|_2^2,
\qquad P=P_{\rm tan}+P_{\rm sh}.
\tag{1.7}
\]

The r50 debt was to consume the shear-volume alternative `P_sh` without selecting a dimension-dependent largest fiber, while keeping the whole diagonal phase `D`. This run does that whenever the complete rank-three Pluecker law has quantitative disjointness, and turns failure into an explicit three-physical-coordinate near-span certificate.

## 2. General rank-three Pluecker law

The useful statement is slightly more general than (1.4). Let

\[
A=A_0+D,\qquad A_0=R^TMR,
\tag{2.1}
\]

where `R` is a real `3 x n` matrix of row rank three, `M` is an invertible real symmetric `3 x 3` matrix, and `D` is any real diagonal matrix. Linear terms are also allowed. Define

\[
T_R:=\det(RR^T)>0,
\qquad
P:=|\det M|T_R.
\tag{2.2}
\]

Because `M` is invertible, `P` is exactly the absolute product of the three nonzero eigenvalues of `A_0`.

For every unordered physical triple `I subset {1,...,n}`, define

\[
w_I:=\det(R_I)^2,
\qquad
\mu(I):=\frac{w_I}{T_R}.
\tag{2.3}
\]

Cauchy--Binet gives

\[
\sum_{|I|=3}w_I=T_R,
\tag{2.4}
\]

so `mu` is a probability law on literal physical triples. Let `I,J` be iid with law `mu` and define

\[
\Omega_3:=\Pr\{I\cap J=\varnothing\}.
\tag{2.5}
\]

This is the complete determinant-squared rank-three disjointness currency. No physical minor is selected before `Omega_3` is spent.

## 3. Exact random-cut identity

For a physical coordinate subset `S`, put

\[
V_S:=\det(R_SR_S^T)
=\sum_{I\subset S,\ |I|=3}w_I.
\tag{3.1}
\]

Choose `S` by putting each literal coordinate independently into `S` with probability `1/2`, and let `T=S^c`.

### Lemma 3.1 — complete triple-law cut identity

\[
\boxed{
\mathbb E[V_SV_T]
=\frac{T_R^2}{64}\,\Omega_3.
}
\tag{3.2}
\]

#### Proof

Expand the product using (3.1):

\[
V_SV_T
=\sum_{I,J}w_Iw_J\mathbf1_{\{I\subset S\}}\mathbf1_{\{J\subset T\}}.
\]

If `I cap J` is nonempty, the indicator is identically zero. If `I` and `J` are disjoint triples, all six specified coordinates must receive prescribed independent Bernoulli labels, which has probability `2^{-6}=1/64`. Therefore

\[
\mathbb E[V_SV_T]
=\frac1{64}\sum_{I\cap J=\varnothing}w_Iw_J
=\frac{T_R^2}{64}\Omega_3.
\]
QED.

Consequently some deterministic original-coordinate cut `S|T` satisfies

\[
\boxed{
\sqrt{V_SV_T}
\ge \frac{T_R}{8}\sqrt{\Omega_3}.
}
\tag{3.3}
\]

This is the desired weighted replacement for a curved-fiber maximum: the whole physical triple-volume law is averaged before any reciprocal crossing quantity appears.

## 4. Exact singular product of the resulting cross block

For the cut from (3.3), the diagonal perturbation `D` contributes no cross term, and the complete cross block is

\[
N=A[S,T]=R_S^TMR_T.
\tag{4.1}
\]

If `Omega_3>0`, then (3.3) gives `V_S,V_T>0`, hence both `R_S` and `R_T` have row rank three and `N` has rank three.

### Lemma 4.1 — cross singular-volume identity

If `Delta_3(N)=sigma_1(N)sigma_2(N)sigma_3(N)` is the product of the three nonzero singular values, then

\[
\boxed{
\Delta_3(N)
=|\det M|\sqrt{V_SV_T}.
}
\tag{4.2}
\]

#### Proof

Let

\[
A_S=R_SR_S^T,\qquad A_T=R_TR_T^T,
\]

which are positive definite. The matrices

\[
U_S=R_S^TA_S^{-1/2},\qquad U_T=R_T^TA_T^{-1/2}
\]

have orthonormal columns, and

\[
N=U_S\,[A_S^{1/2}MA_T^{1/2}]\,U_T^T.
\]

Therefore the three nonzero singular values of `N` are those of the central `3 x 3` matrix. Their product is the absolute determinant,

\[
|\det(A_S^{1/2}MA_T^{1/2})|
=|\det M|\sqrt{\det A_S\det A_T},
\]

which is (4.2). QED.

Combining (3.3), (4.2), and (2.2) gives the central inequality

\[
\boxed{
\Delta_3(N)
\ge \frac{P}{8}\sqrt{\Omega_3}.
}
\tag{4.3}
\]

## 5. Full scalar density payment

Use the completed exact-rank crossing theorem

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For an exact rank-three physical cross block with singular product `Delta`, arbitrary measurable within-bank functions are permitted. The three-dimensional orthogonal projection of each cap-one original product bank has density cap at most `2^{3/2}`. Hence the theorem gives a continuous `C_0` density satisfying

\[
\|p_Q\|_\infty\le6\Delta^{-1/3}.
\tag{5.1}
\]

Apply (5.1) to (4.3).

### Theorem 5.1 — `QFORM-RANK3-PLUCKER-DISJOINT-CROSS-v1`

Under (2.1), if `Omega_3>0`, the complete scalar quadratic form, including the full diagonal coordinate-separable phase `D`, all linear terms, and all within-bank curvature, has a bounded continuous density and

\[
\boxed{
\|p_Q\|_\infty
\le
12\,P^{-1/3}\Omega_3^{-1/6}.
}
\tag{5.2}
\]

At the fixed quantitative gate

\[
\Omega_3\ge2^{-12},
\tag{5.3}
\]

this becomes

\[
\boxed{
\|p_Q\|_\infty\le48\,P^{-1/3}.
}
\tag{5.4}
\]

No fiberwise supremum appears. The dimension enters only through a probability law whose total mass is one, and the physical split is chosen only after the entire determinant-squared law is averaged.

## 6. Apply the theorem to the r50 singular-T core

In (1.4)-(1.5), take `M=M_3`. Then `P` in Theorem 5.1 is exactly the r50 quantity (1.6), while `D` is exactly the complete diagonal same-bank environment phase that previous curved two-output arguments were not allowed to discard.

Therefore, if the rank-three Pluecker disjointness of the frame `R` satisfies (5.3), the full scalar form has a continuous density with

\[
\boxed{
\|p_Q\|_\infty\le48\,P^{-1/3}.
}
\tag{6.1}
\]

Because `P>=P_sh`, the same branch also has the explicit shear-volume estimate

\[
\boxed{
\|p_Q\|_\infty
\le48\left[
\frac{|\lambda|W}{|\det H|}\|Hv\|_2^2
\right]^{-1/3}.
}
\tag{6.2}
\]

Thus the r50 shear-volume alternative is now a genuine full-scalar payment whenever the complete rank-three product geometry is not almost intersecting.

## 7. Low disjointness forces a three-hub near-span certificate

The complementary branch is not left as an amorphous `heavy core` statement.

For a physical triple `H` with `mu(H)>0`, define

\[
\delta(H):=
\frac{\det(R_{H^c}R_{H^c}^T)}{T_R}.
\tag{7.1}
\]

Cauchy--Binet gives

\[
\delta(H)
=\sum_{J\subset H^c,\ |J|=3}\mu(J).
\tag{7.2}
\]

Hence, for `H` sampled from `mu`,

\[
\boxed{
\mathbb E_{H\sim\mu}\delta(H)=\Omega_3.
}
\tag{7.3}
\]

So there exists a literal physical triple `H` of positive Pluecker weight with

\[
\boxed{\delta(H)\le\Omega_3.}
\tag{7.4}
\]

Because `R_H` is invertible, write

\[
R=R_H[I_3,Z],
\qquad Z=R_H^{-1}R_{H^c}.
\tag{7.5}
\]

Then

\[
RR^T=R_H(I+ZZ^T)R_H^T,
\qquad
R_{H^c}R_{H^c}^T=R_HZZ^TR_H^T,
\]

and therefore

\[
\boxed{
\delta(H)
=\frac{\det(ZZ^T)}{\det(I+ZZ^T)}
=\prod_{k=1}^3\frac{s_k}{1+s_k},
}
\tag{7.6}
\]

where `s_k` are the eigenvalues of `ZZ^T`.

If

\[
\Omega_3<2^{-12}=\frac1{4096},
\tag{7.7}
\]

then (7.4)-(7.6) force at least one factor `s/(1+s)<1/16`, hence

\[
\boxed{s_{\min}(ZZ^T)<\frac1{15}.}
\tag{7.8}
\]

Let `u` be a unit eigenvector for `s_min`. The physical coefficient vector

\[
c=u^T[I_3,Z]
\tag{7.9}
\]

lies in `row(R)=range(A_0)` and satisfies

\[
\|c_H\|_2^2=1,
\qquad
\|c_{H^c}\|_2^2=s_{\min}<\frac1{15}.
\tag{7.10}
\]

After normalization, more than `15/16` of this genuine rank-three core direction lies on the three literal physical coordinates `H`:

\[
\boxed{
\frac{\|c_H\|_2^2}{\|c\|_2^2}>\frac{15}{16}=0.9375.
}
\tag{7.11}
\]

### Corollary 7.1 — `QFORM-RANK3-LOWDISJOINT-THREEHUB-CERT-v1`

At the fixed gate `2^{-12}`, every rank-three core (2.1) obeys the dichotomy:

1. `Omega_3>=2^{-12}` and the full scalar form is paid by (5.4); or
2. there is a literal physical triple carrying more than `93.75%` of the squared mass of some unit direction in the core range.

This is stronger and more actionable than merely saying the rank-three range projection has a coordinate of leverage `>1/2`. It is still a structural certificate, not by itself a universal density bound.

## 8. Designated fleet04/B06 theorem applied at an actual inequality

The freshest completed designated-partner result at publication refresh remains

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260924T001014Z-fleet04-B06-QFORM-r3/REPORT.md`,

`QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.

Whiten the actual environment frame as in r50,

\[
F=G^{-1/2}E,
\qquad
\alpha_j=e_j^TG^{-1}e_j.
\tag{8.1}
\]

On the actual diffuse inequality

\[
\max_j\alpha_j\le\frac12,
\tag{8.2}
\]

put

\[
\rho=\lambda v^TGv.
\tag{8.3}
\]

At the partner's actual off-fold scale `r=1/64`, its theorem gives the continuous two-output subdensity estimate

\[
\boxed{\|g_{\rm off}\|_\infty\le\frac{256}{|\rho|}.}
\tag{8.4}
\]

The first term in (1.6) is `P_tan=|det H||rho|`. Therefore the actual inequality

\[
P_{\rm tan}\ge P/2
\tag{8.5}
\]

implies

\[
\boxed{
\|g_{\rm off}\|_\infty
\le512\,\frac{|\det H|}{P}.
}
\tag{8.6}
\]

If (8.5) fails, then

\[
P_{\rm sh}>P/2.
\tag{8.7}
\]

On the additional genuine product-geometric gate `Omega_3>=2^{-12}`, Theorem 5.1 pays the **full scalar** form by (6.1), while retaining `D`. Thus the partner result and the new rank-three Pluecker compiler split the two terms of the exact core volume without conflating a two-output off-fold estimate with a scalar theorem.

I do not promote (8.4) through the same-bank diagonal phase `D`; that would exceed the designated partner theorem's proved scope.

## 9. Finite checks

`check_r51.py` performs fixed-seed finite sanity checks only. It verifies on random full-row-rank `3 x n` frames and invertible symmetric `3 x 3` coefficients that:

- the Pluecker weights sum to `det(RR^T)`;
- the exact disjoint-pair expectation is bounded by the best physical cut as in (3.2)-(3.3);
- the cross singular product agrees with (4.2) to numerical precision;
- the `mu`-average of `delta(H)` agrees with `Omega_3` as in (7.3).

Representative normalized cross-volume discrepancies were below `1.3e-15`. These computations are not used as proof.

## 10. Scope, integrity, and next exact debt

New proved supporting statements in this run:

1. **`QFORM-RANK3-PLUCKER-DISJOINT-CROSS-v1`** — a product-weighted rank-three crossing theorem: `||p_Q||_infinity <=12 P^(-1/3) Omega_3^(-1/6)`, with continuous `C_0` density, retaining any diagonal coordinate-separable phase and arbitrary within-bank functions.
2. **`QFORM-RANK3-LOWDISJOINT-THREEHUB-CERT-v1`** — if `Omega_3<2^-12`, three literal coordinates carry more than `15/16` of some genuine core-range direction.
3. Applied to the singular-T packet, `Omega_3>=2^-12` yields the full scalar continuous-density payment `<=48 P^(-1/3)`, and in particular the shear-volume estimate (6.2).
4. The actual designated fleet04/B06 theorem is applied at (8.4)-(8.6), without exceeding its two-output off-fold scope.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN. Continuity is proved here on the rank-three Pluecker-disjoint paid branch only.

The next precise B06 debt is

**`QFORM-THREEHUB-9375-LOCALIZED-CURVED-RECEIVER-v1`**:

> starting from the low-disjointness certificate (7.11), use the literal three-coordinate hub `H` and the residual at-most-`1/15` transverse range energy to obtain a dependence-safe scalar density payment that remains uniform as the selected principal `3 x 3` coefficient block becomes nearly singular. The receiver must retain the whole diagonal phase `D`, the nonzero residual core directions and every target-valid tail; it may route a quantitatively nonsingular physical triple to the existing determinant receiver and must treat the near-singular triple by weighted curved integration rather than a fiber supremum.

Repository transport was used, but no authenticated native brain retrieval/receiver was available; execution remains `WITHOUT_VERIFIED_BRAIN`.

Privacy/write review: the changed-file allowlist for this repository is only this run directory. The report contains mathematical formulas, source commit/path identifiers and nonsecret run metadata only; no credentials, signed URLs, scheduler IDs, unrelated personal/company/client material or public-release action is present. No installation or remote workflow was used.
