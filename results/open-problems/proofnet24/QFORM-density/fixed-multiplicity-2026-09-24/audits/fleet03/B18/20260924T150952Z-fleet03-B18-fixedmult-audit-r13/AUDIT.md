# fleet03/B18 r13 — independent end-to-end audit of the new multiplicity-eight candidate

Run: `20260924T150952Z-fleet03-B18-fixedmult-audit-r13`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: **WITHOUT_VERIFIED_BRAIN**.  
Role lens: primary-source prior-art verification plus complete proof audit.

## Verdict

**PASS as one independent end-to-end review of the assembled fixed-multiplicity-eight candidate.** I found no mathematical gap in the candidate proof assembled independently in fleet03/B01 and fleet03/B07 from the pinned nine-eigenvalue manuscript and the later eight-direction collar/anchor/incident-volume lemmas.

This is **not** an owner-level promotion by itself: the current control requires two genuinely separate complete reviews before independent-validation status. The unrestricted three-eigenvalue conjecture remains OPEN. Global continuity is not established by this candidate; the theorem certified here is an essential-density bound.

I additionally apply the already source-checked Livshyts--Paouris--Pivovarov projection theorem to the newly assembled `s_8` proof. This lowers the safe constant from the candidate's `2400` to

\[
\boxed{\|p_Q\|_\infty < 1745\,K^2/s\qquad(s_8(A)\ge s>0).}
\]

The numerical `1745` is a convenient integer ceiling; the largest audited branch is exactly bounded by

\[
160\,6^{4/3}=1744.43576911885\ldots.
\]

No novelty claim is made for the primary marginal theorem or for earlier fleet lemmas.

## 1. Sources pinned and checked

The current standalone paper audited end to end is:

- `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`,
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`,
- git blob `19fb119877426b640b2c0dae19ec2f78a399fe11`,
- advertised SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

The new `s_8` dependency chain independently checked in this review is:

1. fleet03/B04 terminal collar, commit `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`;
2. fleet03/B17 robust two-anchor extraction, commit `0408c579bcda638e72c010ff99892a22b9049796`;
3. fleet01/B19 disjoint incident-third-volume receiver, commit `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`;
4. fleet03/B20 zero/one-high-leverage closure, commit `74542593cca87e76d83b07f98e2c895f76b90796`;
5. fleet03/B01 closing two-high lemma/candidate assembly, commit `50a479407cc45f4fbcc87e70ac1846c049138c9f`;
6. fleet03/B07 independent duplicate assembly with exact checks, current file `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B07/20260924T150837Z-fleet03-B07-fixedmult-r2/REPORT.md` and checks at master commit `a030136f2065387d05143b844284a69cf88056c3`.

The primary-source sharpening is Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1: if a density is a product of one-dimensional probability densities bounded by one, every `d`-dimensional orthogonal marginal has density at most `2^(d/2)`. Its hypotheses are exactly compatible with arbitrary rough non-iid independent cap-one inputs. It imposes no Gaussian, moment, bounded-support, log-concavity, centering, symmetry or smoothness assumption.

Rudelson--Vershynin's projection/sum theorem is also hypothesis-compatible but has a nonsharp unspecified `C^d` in higher dimension; its one-dimensional theorem gives the sharp `sqrt(2)` constant. Herry--Malicet--Poly's quadratic-form regularity theorem is **not** a replacement here: it assumes iid inputs with a sufficiently smooth Gaussian-field representation, so I did not use it to cover the arbitrary rough/non-iid scope.

## 2. End-to-end audit of the pinned nine-eigenvalue source

I reread the complete pinned source and independently checked all proof-critical components used below.

### Fourier/rough-law layer — PASS

- Plancherel and Gaussian inversion use the stated Fourier normalization consistently.
- The negative-half-moment Fourier identity has the correct `1/sqrt(2 pi)` factor and its power-envelope integral is correct.
- The heat-flow proof of geometric rank-one Brascamp--Lieb has the correct sign: the frame relation makes the quadratic remainder nonnegative, and the large-time Gaussian limit has exactly the required mass product.
- Rough one-dimensional densities are handled by monotone truncation/approximate identities; no hidden smoothness or moment hypothesis is introduced.
- The product-projection proof is valid and only rotates deterministic integration coordinates, never the random inputs.
- The scalar Fourier-power argument correctly represents `|fhat|^(2m)` through a sum of independent differences and applies a projection-density estimate after normalization.

### Decoupling/grouped compiler — PASS

- The decoupling square introduces an independent copy only of the genuine original bank. Pure same-bank phases have modulus one after expansion.
- The regularized determinant proof uses a genuine geometric frame and correct Jacobians; the `d_i` powers cancel exactly.
- In the grouped compiler, the phase-weighted hub density has the required `L^2` cap; the light-bank image is mollified before expanding its norm, and the final estimate is uniform in the mollifier.
- Weighted Holder is applied to the finite non-probability measure with the correct exponents. The map
  `D -> (M_J D,(c_i D)_{i in T})`
  has Gram determinant `S^2 det(C_T C_T^T)`.
- The subset-entropy inequality is the entropy-subadditivity identity for a uniformly ordered random subset and has the correct sign.
- Heavy-row promotion always promotes literal original coordinates, so no projected-coordinate independence is invented.

### Pivot/spectral/sampling layer — PASS

- The singular Schur-count proof is valid, including the singular-matrix regularization: use a fixed threshold `t-delta`, then pass to the limit and finally let `delta downarrow 0`.
- The volume-sampled bordered determinant count correctly treats singular seeds as absent and therefore uses an inequality rather than a false equality.
- The nonsymmetric interpolation has global rank at most `3r` and restricted `L x L` rank at most `r`; subsequent singular-value perturbation is valid for nonsymmetric auxiliaries.
- `D` really vanishes on the seed coordinates. The forced large diagonal entries therefore lie in the complement where the restricted rank bound is available.
- The definite pair, hyperbolic pair, quarter-power concentration, full pair half-potential and scalar convolution kernel arguments have the claimed scaling and all affine terms remain arbitrary.

Thus the pinned `s_9` paper itself passes this review. Its global conclusion is essential boundedness; only selected Fourier branches explicitly prove a continuous `C_0` density.

## 3. Audit of the new eight-direction structural chain

Work normalized with cap `K=1`, spectral scale `s=1`, and the later eight-direction collar constants

\[
\eta=10^{-2},\qquad \kappa=80^{-2}=1/6400.
\]

Absence of an `eta` pivot gives, for every `i ne j`,

\[
|A_{ii}|<\eta,\qquad
|A_{ij}|^2<\eta+\eta^2=101/10000.
\tag{3.1}
\]

The second inequality follows directly from
`|A_ii A_jj-A_ij^2|<eta` and the diagonal cap.

### 3.1 Terminal collar — PASS

Assume `s_8(A)>=1`, no `eta` pivot, and the order-three disjoint volume is small, `V_3<kappa^3`.

The B04 proof first shows `V_1>=kappa`; otherwise the diagonal and off-diagonal operator norms sum to less than one. It then shows `V_2>=kappa V_1>=kappa^2`: if `V_2<kappa V_1`, the order-one interpolant has `||E||<1/40`, global rank at most three, restricted complement rank at most one, and `s_8(A)>=1` forces at least five complement diagonal entries of the diagonal part above `39/40`. Two of them make a strictly diagonally dominant `2 x 2` principal submatrix of the restricted rank-one remainder, a contradiction.

Since `V_3/V_2<kappa`, sampling order-two seeds and Markov gives good seeds carrying at least `V_2/2`, each with interpolation error

\[
\varepsilon_* = \sqrt{18\kappa}=3\sqrt2/80.
\]

Global rank six then forces two large complement diagonal defects. For their two-set `H`, the interpolation factorization gives

\[
|\det A[S,H]\det A[H,T]|\ge \delta_* |\det A[S,T]|,
\]
where

\[
\delta_*={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}
=0.854335140191\ldots>0.
\]

All index sets remain literal and pairwise disjoint. I checked the determinant lower bound even though the interpolant is nonsymmetric: both diagonal magnitudes are bounded below and both off-diagonal magnitudes above, so `|ad-bc|>=|ad|-|bc|` is exactly what is needed.

### 3.2 Robust-anchor extraction — PASS

For each literal pair `H`, set

\[
D_H=\sum_{U\subset H^c, |U|=2}\det A[H,U]^2
=\det(C_H C_H^T),\quad C_H=A[H,H^c].
\]

Cauchy--Binet gives `sum_H D_H=V_2`. Assign each good seed one of its certified pairs `H` and let `w_H` be its total seed weight. Since `sum_H w_H>=V_2/2`, there is an `H_*` with `D_H>0` and `w_H/D_H>=1/2` (zero-`D_H` terms cannot carry positive assigned weight). The two-sided determinant inequality and the nonnegative unrestricted product of the two Cauchy--Binet sums give

\[
\delta_*^2 w_{H_*}
\le \Xi_{H_*}
\le D_{H_*}^2.
\]

Therefore

\[
\boxed{g:=\det(CC^T)=D_{H_*}\ge \delta_*^2/2
=0.364944265882702\ldots.}
\tag{3.2}
\]

This aggregate-to-one-pair step is dimension free and does not choose a tiny individual minor.

### 3.3 Product-usable incident receiver — PASS

For this anchor pair `H`, B19 defines the disjoint incident third volume

\[
W_{dis}(H)=\sum_{i\in L}\sum_{T\subset L\setminus\{i\},|T|=3}
\det A[H\cup\{i\},T]^2.
\]

A fair original-coordinate cut puts the distinguished row coordinate in one bank and its three distinct column coordinates in the other with probability `1/16`. On a realized cut the exact three-row Gram identity writes the currency as `S^2 Z_1`. In the diffuse case the grouped `(k,ell)=(2,1)` compiler applies; if one residual row is heavy, that literal original coordinate is promoted to a third hub. Hence

\[
\|p_Q\|_\infty\le
C_{inc}W_{dis}^{-1/6},\qquad
C_{inc}=3\,2^{5/6}e^{2/3},
\]

with integrable characteristic function and a continuous `C_0` density. I checked that no coordinate appears in both random banks in this argument.

### 3.4 Zero/one-high leverage closure — PASS

Let

\[
Q_C=C^T(CC^T)^{-1}C,\qquad q_i=(Q_C)_{ii},\qquad
J=\{i:q_i>2/3\}.
\]

`Q_C` is a rank-two orthogonal projection, so `sum q_i=2` and `|J|<=2`.

For low-leverage coordinates B20 constructs a zero-diagonal error matrix `E` satisfying

\[
\|E\|_F^2\le 3W_{dis}/g.
\]

If `|J|<=1` and hypothetically `W_dis<=g/48`, then `||E||_F<=1/4`. The remainder has global rank at most `4+|J|` and restricted low-low rank at most two. Singular-value rank perturbation forces at least three low diagonal coefficients of modulus at least `3/4`; on those three coordinates (3.1) and `||E||_F<=1/4` make the restricted remainder strictly diagonally dominant and hence rank three, contradicting the restricted rank-two bound. Therefore

\[
\boxed{|J|\le1\implies W_{dis}>g/48.}
\tag{3.3}
\]

This yields the previously recorded `<23.48` density bound.

### 3.5 Two-high state is impossible — PASS

This is the final new implication in the B01/B07 candidate, and I independently rederived it.

For columns `c_i` of the `2 x |L|` matrix `C`, define

\[
w_{ij}={\det(c_i,c_j)^2\over g}.
\]

Cauchy--Binet gives `sum_{i<j} w_ij=1`. The rank-two projection identity is

\[
q_i=\sum_{j\ne i}w_{ij}.
\tag{3.4}
\]

A direct proof is
`sum_j det(c_i,c_j)^2=(Jc_i)^T(CC^T)(Jc_i)=det(CC^T)c_i^T(CC^T)^{-1}c_i`.

If two distinct indices `i,j` both satisfy `q>2/3`, inclusion-exclusion in the two-element determinantal weight gives

\[
w_{ij}\ge q_i+q_j-1>1/3,
\]
so by (3.2)

\[
\det(C_{\{i,j\}})^2>g/3>0.1216.
\tag{3.5}
\]

But every entry of this physical `2 x 2` cross minor is an off-diagonal entry of `A`. By (3.1),

\[
|\det(C_{\{i,j\}})|
<2(\eta+\eta^2)=101/5000,
\]
therefore

\[
\det(C_{\{i,j\}})^2<10201/25000000=0.00040804,
\tag{3.6}
\]
contradicting (3.5). Hence the robust terminal pair automatically has `|J|<=1`, and (3.3) closes the terminal collar.

This final step is elementary but decisive. It uses both currencies simultaneously: the order-one physical entry cap from the no-pivot state and the order-one anchor Gram determinant forced by `s_8`. It is not a generic rank-two-crossing density theorem.

## 4. Full multiplicity-eight proof after the audit

The normalized `s_8(A)>=1` proof is now exhaustive.

**Scalar pivot.** If `|A_ii|>=eta=1/100`, the scalar-square profile contributes `eta^(-1/2)=10`. Its Schur complement retains at least seven unit spectral directions, hence satisfies the five-direction full half-potential proposition from the pinned paper. Using the exact displayed constants there,

\[
H_5\le\max\{70,16p^{-1/4},1+d^{-1/2}(J_0+2L_0)\}
=98.8220973674\ldots<99,
\]
for `d=3/40`, `p=1/400`. Thus this branch is `<990`.

**Definite pair pivot.** If a principal pair has determinant modulus at least `eta`, direct conditioning gives `<10 pi<32`.

**Indefinite pair pivot.** Its Schur complement retains at least six unit directions, so the quarter-power logarithmic-potential lemma applies. With `D>=eta`, the hyperbolic envelope gives

\[
\|p_Q\|_\infty
\le10(6+\log16+L_0)+1/e
=192.4712831609\ldots<193.
\]

**No pivot, large `V_3`.** This is paid by a literal coordinate cut and the order-three crossing receiver.

**No pivot, small `V_3`.** Sections 3.1--3.5 produce a robust pair, exclude two high leverages, force `W_dis>g/48`, and apply the B19 product-safe incident receiver. This branch is `<23.48` with a continuous density.

Thus the candidate really covers all signs, singular/indefinite cases, dimensions, affine terms and arbitrary rough non-iid cap-one product laws.

For general `K,s`, put `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

Then the coordinates of `Y` have density cap one, `s_8(A/s)>=1`, and `Q=(s/K^2)\widetilde Q`. Hence every normalized universal bound `C` scales to `CK^2/s`.

## 5. Primary-source sharpening: safe constant 1745

My earlier B18 source transfer from Livshyts--Paouris--Pivovarov gives, for every literal crossing block `M`,

\[
\|p_Q\|_\infty\le 6^{4/3} Z_3(M)^{-1/6}.
\tag{5.1}
\]

The proof uses only Theorem 1.1 of LPP plus the same grouped original-coordinate compiler: a full-rank `d`-dimensional linear image has density cap

\[
2^{d/2}/\sqrt{\det(LL^T)},
\]

and the one-dimensional case gives

\[
\int|\widehat f(t)|^pdt\le4\pi/\sqrt p,\qquad p\ge2.
\]

No new stochastic rotation is introduced.

In the `s_8` large-third-volume branch, a fair cut has

\[
Z_3\ge \kappa^3/64,
\]
so exactly

\[
(\kappa^3/64)^{-1/6}=160.
\]

Applying (5.1),

\[
\boxed{\|p_Q\|_\infty\le160\,6^{4/3}
=1744.43576911885\ldots.}
\tag{5.2}
\]

This is larger than every other audited branch (`<990`, `<193`, `<32`, and `<23.48`), so a simple global statement is

\[
\boxed{\|p_Q\|_\infty<1745 K^2/s\quad\text{whenever }s_8(A)\ge s>0.}
\tag{5.3}
\]

The same source transfer can sharpen the B19 incident receiver: the `(2,1)` grouped coefficient becomes `3*2^(5/6)` before the random-cut loss, so after the `1/16` cut one may use `C_inc^sharp=6 sqrt(2)` instead of `3*2^(5/6)e^(2/3)`. With (3.2)--(3.3) the terminal branch becomes `<19.136`; this does not change the global `1745` ceiling.

## 6. Designated historical fleet04/B18 result applied to an actual inequality

For compatibility with the B18 partner instruction retained in the older assignment, I also applied fleet04/B18's completed bounded-window null-hub theorem (report `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T221534Z-fleet04-B18-QFORM-r5/REPORT.md`).

Take

\[
B=\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&1&0\\
0&0&0&0
\end{pmatrix},\qquad
A=B\oplus I_5.
\]

`B` has nonzero eigenvalues `1,-1,1`, so its spectral window has `s=L=1`, its null-hub physical edge has size one, and `A` has exactly eight eigenvalues of modulus at least one. Conditioning the five outside original coordinates leaves only affine/constant changes in the four-coordinate block. Applying fleet04/B18 with edge gate `a=1` gives the concrete full-law inequality

\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty\le576^{1/3}
=8.32033529221\ldots}
\]

for every admissible cap-one product law and arbitrary affine terms. This is only a concrete partner application, not an ingredient in the general `s_8` proof.

## 7. Prior-art boundary

A targeted primary-source search found no exact published theorem matching the present arbitrary-rough, non-iid product-law fixed-multiplicity statement. LPP and Rudelson--Vershynin supply the projection-density inputs; Herry--Malicet--Poly work under substantially stronger iid/smooth Gaussian-representation assumptions. This search is not exhaustive and no novelty claim is made from it.

## 8. Final review status

- pinned standalone `s_9`, constant-400 manuscript: **PASS in this B18 end-to-end review**;
- newly assembled `s_8` theorem: **PASS as one independent B18 end-to-end review**, with source-sharpened safe constant `1745 K^2/s`;
- required second genuinely independent end-to-end review for `s_8`: **STILL REQUIRED** before owner-level promotion;
- global continuity for `s_8`: **NOT PROVED**; continuity is available in the large-`V_3` Fourier branch and terminal incident-volume branch, but not established uniformly across every pivot branch;
- unrestricted three-large-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No Monte Carlo evidence enters any theorem. No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, conditional-cap-as-independence, or pointwise rough quadratic-phase hypothesis is used.
