# account03/B06 r52 — mixed-layer localization and curved-fiber compiler

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T04:22:33Z.

attacking: `QFORM-THREEHUB-9375-LOCALIZED-CURVED-RECEIVER-v1`; convert the r51 low-disjointness three-literal-coordinate certificate into weighted Pluecker-layer currency, then isolate the exact tangential/normal residual without taking an unrestricted curved-fiber supremum.

## Status and source pins

- Owner programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.
- Fresh owner-control revision read before publication: `2026-09-22.15`.
- Final brain source refresh: `yspennstate/math-research-brain@0f17ba16607dc0f969459c7daa8cd0594a71692c`.
- Math source refresh immediately before publication: `yspennstate/math-open-problems@06f04e91cd15df1932974ca5679fd99bbae78359`.
- Predecessor: account03/B06 r51, `QFORM-RANK3-PLUCKER-DISJOINT-CROSS-v1` and `QFORM-RANK3-LOWDISJOINT-THREEHUB-CERT-v1`.
- Designated partner used below: account04/B06 r3, `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.
- Execution label: `WITHOUT_VERIFIED_BRAIN`; repository access is not native-brain ingestion.

The full QFORM conjecture remains open. Nothing below claims a universal final constant for the full theorem.

## 1. Compact conditional end-to-end argument

The r51 rank-three core has

\[
 A_0=R^TMR,
\]

where `R` is `3 x n`, has row rank three, and `M` is invertible symmetric. Put

\[
 P:=|\det M|\det(RR^T).
\]

r51 proved that if the determinant-squared Pluecker law of physical triples has disjointness probability

\[
 \Omega_3\ge 2^{-12},
\]

then the complete scalar form, including an arbitrary coordinate-separable diagonal perturbation, has a continuous `C_0` density with

\[
 \|p_Q\|_\infty\le 48P^{-1/3}.
\]

Thus this run starts only from the complementary branch `Omega_3 < 2^{-12}`. r51 then supplies a literal physical triple `H` of positive Pluecker weight such that, after using that triple as the basis,

\[
 R=R_H[I_3,Z],\qquad G:=ZZ^T,
\]

and

\[
 \frac{\det G}{\det(I+G)}<2^{-12}.
\]

The new results below show that this apparently near-singular three-hub branch is still forced to carry a fixed fraction of the complete rank-three spectral volume in one of only three finite mixed Pluecker layers, and that the near-null tail direction admits a literal-row decomposition with quantitatively small true normal innovation.

## 2. `QFORM-LOWDISJOINT-MIXED-LAYER-MASS-v1`

### Theorem

Let

\[
 R=R_H[I_3,Z],\qquad G=ZZ^T\succeq0,
\]

where `H` is a literal three-coordinate basis with `det R_H != 0`. Let

\[
 B:=R_H^TMR_H.
\]

Then

\[
 P=|\det B|\det(I+G).
\]

Define the four complete squared-Pluecker layer masses

\[
 P_0:=|\det B|,
\]
\[
 P_1:=|\det B|e_1(G),
\]
\[
 P_2:=|\det B|e_2(G),
\]
\[
 P_3:=|\det B|e_3(G)=|\det B|\det G.
\]

Here `P_k` is exactly the total spectral-volume mass of physical triples containing `k` tail coordinates and `3-k` coordinates from `H`. Therefore

\[
 \boxed{P=P_0+P_1+P_2+P_3.}
\]

If

\[
 \frac{\det G}{\det(I+G)}<2^{-12},
\]

then

\[
 \boxed{\max(P_0,P_1,P_2)>\frac5{16}P.}
\]

Thus the low-disjointness branch cannot hide essentially all of the rank-three curvature in all-tail triples: at least `31.25%` of the complete rank-three spectral volume lies in one finite layer using at least one of the three literal hub coordinates.

### Proof

The Cauchy-Binet identity gives

\[
 \det(I+ZZ^T)=1+e_1(G)+e_2(G)+e_3(G).
\]

A physical triple of `[I_3,Z]` having exactly `k` tail columns has determinant, up to sign, equal to the corresponding `k x k` minor of `Z`. Summing squared determinants over all triples in that layer gives `e_k(G)`. Multiplication by `|det B|` yields the exact layer decomposition above.

Let the eigenvalues of `G` be

\[
 s_1\ge s_2\ge s_3\ge0.
\]

The low-disjointness certificate implies

\[
 \prod_{i=1}^3\frac{s_i}{1+s_i}<2^{-12}=16^{-3}.
\]

Hence at least one factor is `<1/16`; by monotonicity and the ordering, the smallest one obeys

\[
 \frac{s_3}{1+s_3}<\frac1{16},
\]

so

\[
 \boxed{s_3<\frac1{15}.}
\]

Moreover

\[
 \det(I+G)
 =(1+s_3)(1+s_1+s_2+s_1s_2)
 <\frac{16}{15}(1+s_1+s_2+s_1s_2).
\]

Among the three nonnegative numbers `1`, `s_1+s_2`, and `s_1s_2`, one is at least one third of their sum. Therefore

\[
 \max\{1,s_1+s_2,s_1s_2\}
 >\frac5{16}\det(I+G).
\]

Since

\[
 e_1(G)\ge s_1+s_2,
 \qquad
 e_2(G)\ge s_1s_2,
\]

multiplication by `|det B|` proves the claim. QED.

### Why this is the right weighted replacement

No individual physical minor is selected before the aggregate determinant-squared mass is computed. The weights are the genuine Pluecker weights inherited from the product-coordinate geometry. This avoids the already-refuted strategy of paying a reciprocal cost on a favorable-looking single minor.

## 3. `QFORM-THREEHUB-NEARNULL-ROW-DECOMPOSITION-v1`

### Theorem

Continue in the low-disjointness branch and suppose `s_2>0`. Let `u` be a unit eigenvector of `G` for `s_3`. Choose a literal hub row index `h in {1,2,3}` with

\[
 |u_h|^2\ge\frac13,
\]

and let `J={1,2,3}\setminus{h}`. Write `z_h` for row `h` of `Z` and `Z_J` for the other two rows. Define

\[
 W_h:=\det(Z_JZ_J^T)=\det G[J,J].
\]

Then

\[
 \boxed{W_h\ge\frac13s_1s_2.}
\]

If

\[
 n_h:=P_{\ker Z_J}z_h,
\]

then

\[
 \boxed{\|n_h\|^2=\frac{\det G}{W_h}\le 3s_3<\frac15.}
\]

Hence

\[
 \boxed{\|n_h\|<5^{-1/2}.}
\]

Also, because `e_2(G)=s_1s_2+s_1s_3+s_2s_3<=3s_1s_2`,

\[
 \boxed{W_h\ge \frac19e_2(G).}
\]

If `s_2=0`, then `rank Z<=1`; the two-dimensional curved-tail debt disappears entirely and only the layer-0/layer-1 lower-rank endpoint remains.

### Proof

For `s_2>0`, the spectral formula for the adjugate is

\[
 \operatorname{adj}(G)
 =s_2s_3v_1v_1^T+s_1s_3v_2v_2^T+s_1s_2uu^T.
\]

Therefore

\[
 W_h=e_h^T\operatorname{adj}(G)e_h
 \ge s_1s_2u_h^2
 \ge \frac13s_1s_2.
\]

The Gram-Schur identity for the row split `z_h | Z_J` is

\[
 \det G
 =\det(Z_JZ_J^T)\,\|P_{\ker Z_J}z_h\|^2
 =W_h\|n_h\|^2.
\]

Thus

\[
 \|n_h\|^2
 \le\frac{s_1s_2s_3}{s_1s_2/3}
 =3s_3
 <\frac15.
\]

The `e_2` comparison follows from `s_3<=s_2<=s_1`. QED.

### Interpretation

The r51 `>15/16` three-coordinate localization is now sharpened into an actual curved-fiber normal form: two tail rows retain quantitative two-dimensional area, while the third tail row differs from their span by a vector of norm `<1/sqrt(5)`. The remaining hard variable is therefore a genuine normal innovation, not an arbitrary high-dimensional fiber.

## 4. Exact scalar-pivot cross identity on the zero-hub-diagonal-perturbation subbranch

This is a scoped payment, not a full closure.

Partition the core matrix `B` according to the literal row `h`:

\[
 B=\begin{pmatrix}a&b^T\\ b&C\end{pmatrix},
\qquad a\ne0.
\]

Suppose the coordinate-separable diagonal perturbation has zero coefficient on this one selected hub coordinate. After completing the square in the original coordinate `x_h`, the residual cross matrix from the other two hub coordinates to the complete tail bank is exactly

\[
 N_h=(C-bb^T/a)Z_J.
\]

The entire `z_h` row cancels. Therefore

\[
 \sigma_1(N_h)\sigma_2(N_h)
 =\left|\det(C-bb^T/a)\right|\sqrt{W_h}
 =\frac{|\det B|}{|a|}\sqrt{W_h}.
\]

Applying the already-completed physical scalar-pivot/rank-two-cross receiver gives

\[
 \boxed{
 \|p_Q\|_\infty
 \le
 8\,[|a|\,|\det B|\sqrt{W_h}]^{-1/4}.
 }
\]

Using the new row bound,

\[
 \boxed{
 \|p_Q\|_\infty
 \le
 8\,[|a|\,|\det B|\sqrt{s_1s_2/3}]^{-1/4}.
 }
\]

If layer 2 is the large layer, then `W_h>=e_2(G)/9`, hence

\[
 \boxed{
 \|p_Q\|_\infty
 \le
 8\,[|a|\,|\det B|\sqrt{e_2(G)}/3]^{-1/4}.
 }
\]

This branch gives absolute continuity and an essentially bounded density under its stated hypotheses. I do not claim continuity from this receiver.

## 5. Exact residual split when the selected hub does carry diagonal curvature

Let the core pivot coefficient be `a_0=B_hh` and let the diagonal perturbation at that literal coordinate be `d_h`, so the actual scalar pivot is

\[
 a=a_0+d_h.
\]

With `B` written as above but using `a_0` in its top-left entry, the exact post-pivot cross matrix is

\[
 N
 =\frac{d_h}{a}b z_h
  +\left(C-\frac{bb^T}{a}\right)Z_J.
\]

Decompose

\[
 z_h=qZ_J+n_h,
 \qquad n_h\perp\operatorname{rowspan}(Z_J).
\]

Then

\[
 \boxed{
 N=
 \left[\frac{d_h}{a}bq+C-\frac{bb^T}{a}\right]Z_J
 +\frac{d_h}{a}b n_h.
 }
\]

The first term is exactly tangential to the two-row curved plane. The second term is the true normal shared-bank leakage, and the theorem above gives

\[
 \boxed{
 \left\|\frac{d_h}{a}b n_h\right\|
 <\frac1{\sqrt5}\left|\frac{d_h}{a}\right|\|b\|.
 }
\]

This is the first essential missing implication isolated quantitatively. Smallness of this normal term alone is NOT declared sufficient: the live correction `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1` forbids that shortcut. The remaining receiver must retain the layer-0/1/2 third-curvature mass while averaging this normal statistic against the original product law.

## 6. Actual designated-partner application

The freshest completed designated partner result is account04/B06 r3,

`QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`,

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`.

Whiten the two strong rows `Z_J`:

\[
 U=(Z_JZ_J^T)^{-1/2}Z_J.
\]

The two rows of `U` are orthonormal and the column leverages satisfy

\[
 \ell_k=\|Ue_k\|^2,
 \qquad
 \sum_k\ell_k=2.
\]

If

\[
 \max_k\ell_k\le\frac12,
\]

then the tangential part `qZ_J` in the exact residual split lies precisely in the partner theorem's two-dimensional curved plane. Its fold recentering and determinant-one output shear remove that tangential shared-bank leakage exactly. At the concrete off-fold scale `r=1/64`, for curved coefficient `lambda_* != 0`, the partner estimate gives the actual inequality

\[
 \boxed{\|g_{\rm off}\|_\infty\le\frac{256}{|\lambda_*|}.}
\]

After that exact tangential removal, the only shared-bank obstruction left by the decomposition is the true normal statistic carried by `n_h`, whose coefficient has been reduced by the quantitative factor `<1/sqrt(5)` above.

If instead some `ell_k>1/2`, then a literal tail coordinate is a heavy two-frame hub. Since the leverages sum to two, there are at most three such coordinates. Thus failure of the partner diffuse gate again produces a finite physical-hub certificate rather than a dimension-dependent fiber maximum.

The partner theorem is deliberately not promoted through the remaining same-bank diagonal perturbation or through a positive normal statistic; those are outside its proved scope.

## 7. Sanity checks

A fixed-seed deterministic numerical check (`seed=20260924`) sampled 10,000 positive-semidefinite `3 x 3` Gram matrices with `s_3<1/15`. It checked:

- the mixed-layer lower bound;
- the cofactor inequality `W_h>=s_1s_2/3`;
- the Gram-Schur residual identity `||n_h||^2=det(G)/W_h`;
- the inequality `||n_h||^2<=3s_3`.

Observed:

- no layer-bound violations;
- no cofactor violations;
- maximum normalized residual-identity discrepancy about `3.92e-14`;
- maximum observed ratio `||n_h||^2/s_3` about `2.880 < 3`.

These checks are diagnostics only; the proofs above are exact.

## 8. What is and is not proved

Proved in this run:

1. exact Pluecker layer decomposition of the r51 localized rank-three core;
2. low disjointness forces `max(P0,P1,P2)>5P/16`;
3. a literal hub deletion yields a strong two-row tail area and true normal residual `<1/sqrt(5)` whenever `rank Z>=2`;
4. exact post-pivot tangential/normal decomposition;
5. a scoped scalar-pivot/rank-two-cross density payment when the chosen hub has no diagonal perturbation;
6. actual use of account04/B06 r3 to remove the full tangential shared leakage on the diffuse two-frame branch, leaving only the quantified normal term; non-diffuse failure yields at most three heavy tail coordinates.

Not proved:

- no universal full-QFORM constant follows yet from these structural inequalities;
- the layer-0/layer-1 endpoints are not fully compiled here;
- the normal term cannot be discarded merely because its coefficient is `<1/sqrt(5)`;
- continuity is not established on the scalar-pivot branch; it is available only on already-completed continuous branches such as r51's Pluecker-disjoint branch and the partner's scoped off-fold two-output branch.

## 9. Next exact debt

`QFORM-MIXED-LAYER-NORMAL-INNOVATION-RECEIVER-v1`:

Use the forced currency

\[
 \max(P_0,P_1,P_2)>5P/16
\]

jointly with the exact residual split

\[
 N=N_{\rm tangential}+\frac{d_h}{a}bn_h,
 \qquad \|n_h\|<1/\sqrt5,
\]

to prove a dimension-free original-product curved receiver. The proof must keep the third-curvature layer mass while integrating the normal statistic; if the whitened two-frame leverage gate fails, route the at-most-three heavy tail coordinates into a finite physical-hub receiver. Do not replace the normal innovation by an arbitrary bounded-density projection and do not take a curved-fiber supremum.

## Global status

**FULL QFORM: OPEN / NOT PROVED / NOT DISPROVED.**

**GLOBAL CONTINUITY: OPEN.**
