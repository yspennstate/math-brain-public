# fleet03/B17 — the 3sqrt(2) obstruction survives the no-pivot reduction

Run: `20260923T000852Z-fleet03-B17-QFORM-r20`  
Status: `SUBSTANTIVE_SUPPORTING_THEOREM`; full QFORM conjecture OPEN; full continuity OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. Purpose and current source state

The current owner target is the unrestricted QFORM density conjecture for independent real coordinates with density caps one and a real symmetric matrix having at least three eigenvalues of absolute value at least one. No moments, support restrictions, log-concavity, Gaussianity, or independence after a spectral rotation are assumed.

This run applies the newest no-pivot reduction and the completed designated-partner witness to the same quantitative inequality. The relevant source pins are:

- newest no-pivot synthesis: `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`;
- newest Claude geometric/Fourier source: `yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`;
- designated partner `fleet04/B17`: `yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

The live corrections were respected: no pointwise law-uniform quadratic-phase decay, arbitrary-joint rank-three coarea bound, worst conditional projection cap, single uniformly good physical minor, or independence after rotation is used.

## 2. The current N3 class

Fix `tau` in `(0,1]`. Following the newest synthesis, call a symmetric matrix `M` **no-tau-pivot** when

\[
 |M_{ii}|<\tau\quad\hbox{for every }i,
 \qquad
 |\det M[\{i,j\},\{i,j\}]|<\tau\quad\hbox{for every }i\ne j.
\]

The remaining statement `N3(tau,C0)` asks for a universal density cap `C0` on this class under the original condition that at least three eigenvalues have absolute value at least one. The supplied Gaussian-padding argument shows that proving one such N3 statement is enough for the full conjecture, subject to the already supplied supporting estimates. N3 itself is still unproved.

The question here is sharpness: does moving to the strict no-pivot class eliminate the known `3sqrt(2)` obstruction? The answer is no, even for exact rank three, and still no after making the matrix invertible.

## 3. Exact partner witness and its physical pivot scale

Use the designated partner's rational orthogonal matrix

\[
O={1\over7}
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},
\qquad J=\operatorname{diag}(1,1,-1),
\]

and set

\[
B=O^TJO={1\over49}
\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix}.
\]

Let `v_j=O e_j`. For each integer `m>=3`, form the `3m x 3` matrix `R_m` by repeating the row `v_j^T/sqrt(m)` exactly `m` times for each `j=1,2,3`, and put

\[
A_m=R_m J R_m^T.
\]

Then `R_m^T R_m=I_3`, hence the nonzero spectrum of `A_m` is exactly `{1,1,-1}`. A physical coordinate is indexed by a bank label `j` and a within-bank label. For coordinates in banks `j,k`,

\[
 (A_m)_{(j,a),(k,b)}={B_{jk}\over m}.
\]

Therefore the largest diagonal pivot is exactly

\[
\eta_m:=\max_i |(A_m)_{ii}|={41\over49m}.
\tag{3.1}
\]

The three distinct-bank principal `2x2` determinants of `B` are, exactly,

\[
\det B_{12}=-{41\over49},\qquad
\det B_{13}={23\over49},\qquad
\det B_{23}=-{31\over49}.
\tag{3.2}
\]

Two coordinates from the same bank give determinant zero. Hence

\[
\max_{i<j}|\det (A_m)_{\{i,j\},\{i,j\}}|
={41\over49m^2}
={49\over41}\eta_m^2.
\tag{3.3}
\]

Consequently, for every fixed `tau in (0,1]`, every integer

\[
m\ge3,\qquad m>{41\over49\tau}
\tag{3.4}
\]

puts `A_m` strictly inside the no-tau-pivot class. This is an exact physical-coordinate statement, not a spectral-basis statement.

## 4. N3 has the same known lower-bound obstruction

Take all `3m` physical inputs iid `Unif[-1/2,1/2]`. The completed `fleet04/B17` local Edgeworth/coarea theorem proves that the density is continuous and

\[
 p_{Q_m}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right),
 \qquad Q_m=X^T A_m X.
\tag{4.1}
\]

Now fix `tau`. By (3.4), all sufficiently large members of this very sequence satisfy N3's strict no-pivot hypotheses. If `N3(tau,C_0)` were true, then for those `m`

\[
3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right)
=p_{Q_m}(0)\le C_0.
\]

Letting `m` tend to infinity gives the source-valid necessary inequality

\[
\boxed{C_0\ge3\sqrt2.}
\tag{4.2}
\]

Thus the no-pivot reduction does not buy any improvement in the known sharp lower-bound obstruction. In particular, a proof of N3 with a constant below `3sqrt(2)` is impossible.

There is an exact first-order relation to the physical pivot scale. Since `1/m=(49/41) eta_m`, (4.1) becomes

\[
\boxed{
 {p_{Q_m}(0)\over3\sqrt2}
 =1-{5295\over18368}\eta_m+O(\eta_m^2).
}
\tag{4.3}
\]

The coefficient is `5295/18368 = 0.288273083623693...`. Therefore this exact rotated product witness approaches the `3sqrt(2)` obstruction linearly as every physical scalar pivot tends to zero, while every physical `2x2` determinant tends to zero quadratically.

This is a direct application of the completed designated-partner result to the newest live proof gap.

## 5. Applying the newest determinant-only pair theorem to the same witness

The bank-1/bank-2 physical pair is indefinite, with

\[
D={41\over49m^2},\qquad s_3(A_m)=1.
\]

The newest determinant-only physical-pair theorem therefore gives the valid inequality

\[
\boxed{
\|p_{Q_m}\|_\infty
\le {7m\over\sqrt{41}}
\left[
9.2+\log_+\left({10000\sqrt{41}\over7m}\right)
\right].
}
\tag{5.1}
\]

This is useful evidence about where the remaining proof must aggregate. The right side of (5.1) grows at least linearly in `m` once the logarithm turns off, whereas the actual witness density in (4.1) tends to the finite value `3sqrt(2)`. Therefore paying the reciprocal determinant of one physical pair before exploiting the repeated product-bank structure cannot prove a dimension-free N3 estimate on this family. This does not refute the pair theorem; it identifies its quantitative loss on the exact uncovered no-pivot stress geometry.

The newer 5-volume decoupling theorem is likewise not a direct escape here: `A_m` has rank three, so every cross block has rank at most three and every fifth exterior volume is zero. A successful N3 proof must use the three-direction aggregate structure rather than require five cross directions.

## 6. Full-rank no-pivot padding preserves the obstruction

The sharp obstruction is not an artifact of exact rank deficiency. Let

\[
P_m=R_mR_m^T,
\qquad \delta_m=m^{-2},
\qquad
\widetilde A_m=A_m+\delta_m(I-P_m).
\tag{6.1}
\]

Because `P_m` is the orthogonal projection onto `range(R_m)`, the spectrum is exactly

\[
\operatorname{spec}(\widetilde A_m)
=\{1,1,-1\}\cup\{m^{-2}\}^{3m-3}.
\tag{6.2}
\]

Thus every `\widetilde A_m` is invertible and still has exactly three eigenvalues of absolute value at least one.

The entries of `P_m` equal `1/m` within a common bank and zero between different banks. Hence a diagonal entry of `\widetilde A_m` has magnitude at most

\[
{41\over49m}+{1\over m^2}< {2\over m}.
\tag{6.3}
\]

For two different coordinates in the same bank, the principal determinant has magnitude at most

\[
{1\over m^2}\left({82\over49m}+{1\over m^2}\right)<{4\over m^2}.
\tag{6.4}
\]

For coordinates in two different banks, expansion around (3.2) gives

\[
|\det \widetilde A_m[\{i,j\}]|
\le {41\over49m^2}+{72\over49m^3}+{1\over m^4}
<{4\over m^2}.
\tag{6.5}
\]

Therefore, for every fixed `tau in (0,1]`, if

\[
m\ge3,\qquad m>{2\over\tau},
\tag{6.6}
\]

then `\widetilde A_m` is invertible and strictly no-tau-pivot.

For the same centered unit-interval product input,

\[
0\le X^T(\widetilde A_m-A_m)X
=\delta_m X^T(I-P_m)X
\le \delta_m\|X\|^2
\le {3\over4m}.
\tag{6.7}
\]

Thus `\widetilde Q_m-Q_m ->0` deterministically. The partner's triangular-array limit gives

\[
Q_m\Rightarrow
S:=G_1^2+G_2^2-G_3^2,
\qquad G_j\stackrel{ind}{\sim}N(0,1/12),
\]

so also `\widetilde Q_m => S`. The limit density is continuous and

\[
p_S(0)={1\over2\sqrt2(1/12)}=3\sqrt2.
\tag{6.8}
\]

Define the interval-concentration seminorm

\[
K(Z)=\sup_{a<b}{\Pr(a<Z<b)\over b-a}.
\]

For weak convergence, Portmanteau on every open interval gives

\[
K(S)\le\liminf_m K(\widetilde Q_m).
\]

Since the continuous density of `S` has value `3sqrt(2)` at zero,

\[
\boxed{
\liminf_{m\to\infty}K(\widetilde Q_m)\ge3\sqrt2.
}
\tag{6.9}
\]

Hence even the **invertible** strict no-pivot subclass has universal concentration/density constant at least `3sqrt(2)`. This is stronger than merely observing that a singular rank-three limit is difficult.

Continuity is proved by the partner theorem for the exact rank-three witness `Q_m`. This run does not assert continuity for the padded full-rank sequence, and full-target continuity remains open.

## 7. Consequence for proof design

For every `tau in (0,1]`, the newest residual N3 class contains a completely explicit sequence of cap-one product witnesses with physical pivot scale tending to zero and density peak tending to `3sqrt(2)`. The obstruction remains after adding a nonzero spectral tail and making every matrix invertible.

Therefore a dimension-free proof of N3 cannot rely on a quantitative gain that is bounded away from zero merely because all physical scalar and pair pivots are small. On this family, the large eigenspace is genuinely diffuse, individual pair determinants cost `m^{-2}`, and the known determinant-only pair theorem pays `m`; nevertheless the aggregate three-direction product law remains at constant density scale. The missing mechanism must aggregate repeated coordinates / spectral volume before reciprocal pivot payment, or exploit a genuinely three-direction product-preserving Fourier or geometric inequality.

This result does **not** prove N3 or the full conjecture and gives no counterexample. It sharpens the necessary constant and supplies an exact stress family for the remaining proof interface.

## 8. Exact checks

Sibling `check_no_pivot_witness.py` performs the rational checks `B^2=I`, the three principal minors in (3.2), the pivot scale, the coefficient conversion in (4.3), and sample padded no-pivot bounds. `check_results.txt` records the executed output. No Monte Carlo or histogram is used.
