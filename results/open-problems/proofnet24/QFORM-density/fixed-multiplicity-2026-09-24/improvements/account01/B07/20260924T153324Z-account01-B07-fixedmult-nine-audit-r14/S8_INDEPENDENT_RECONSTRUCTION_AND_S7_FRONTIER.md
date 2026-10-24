# account01/B07 r14 — independent reconstruction of multiplicity eight; seven-direction frontier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T153324Z-account01-B07-fixedmult-nine-audit-r14`  
Status: **PASS as an independent complete mathematical reconstruction of a fixed-multiplicity-eight theorem; owner/release status unchanged. Multiplicity seven and the unrestricted three-eigenvalue conjecture remain OPEN.**

## 1. Exact theorem reconstructed

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K`, let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

\[
s_8(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density and the safe bound

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<2400\,{K^2\over s}}
\tag{1.1}
\]

holds. This reconstruction does **not** claim a globally continuous representative: the no-pivot Fourier branches are continuous, while the pivot branches are used only as essential-density domination arguments.

The proof below was reconstructed from the following source-pinned ingredients, but each transition was rederived rather than importing a peer verdict:

1. the audited standalone nine/400 source `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, in particular its marginal-free order-three receiver, five-direction full half-potential proposition, physical pivot estimates, and product-coordinate grouped Fourier compiler;
2. the eight-direction terminal-collar theorem `yspennstate/math-open-problems@5dc3b183bf69c8ab69f725c4464d5073f5c803cd`;
3. robust two-anchor extraction `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B17/20260924T141823Z-account03-B17-fixedmult-auto11/ROBUST_TWO_ANCHOR.md`;
4. the one-exception completion route in account01/B12, commit `804377122a7a321d1b65eff634066f59f45bf9a3`, which I independently checked algebraically.

A separate account03/B08 review at commit `2bf752b5944536f51357d3d3b8b17212a297c7a6` also reports an end-to-end PASS, but its verdict is not used as a premise below.

## 2. Pivot branches already close under eight directions

Normalize `K=s=1` and use the terminal-collar pivot scale

\[
\eta=10^{-2},\qquad \kappa=80^{-2}.
\]

### 2.1 Scalar pivot

If `|A_ii|>=eta`, condition on the complement and complete the square. The scalar profile gives

\[
\|p_Q\|_\infty
\le \eta^{-1/2}\sup_a \mathbb E|R-a|^{-1/2}.
\]

The Schur complement loses at most one unit spectral direction, so it has at least seven and in particular at least five. The audited five-direction full half-potential proposition in the nine/400 source gives

\[
H_5\le\max\{70,16(1/400)^{-1/4},1+(3/40)^{-1/2}(J_0+2L_0)\}<115.
\]

Since `eta^{-1/2}=10`,

\[
\boxed{\|p_Q\|_\infty<1150.}
\tag{2.1}
\]

No condition on the remaining spectrum, signs, affine terms or support is introduced.

### 2.2 Principal pair pivot

If a principal two-coordinate determinant has modulus at least `eta`, a definite pair gives

\[
\|p_Q\|_\infty\le \pi/\sqrt\eta<40.
\]

For an indefinite pair, the pair Schur complement loses at most two unit directions, hence retains at least six. Only one nonzero unit direction is needed by the audited quarter-power/logarithmic-potential receiver. Inserting `D>=eta=1/100` in the hyperbolic envelope gives the safe bound

\[
\boxed{\|p_Q\|_\infty<197.}
\tag{2.2}
\]

Thus all pivot branches are already below 2400.

## 3. Exact no-pivot eight-direction collar

Assume no `eta`-pivot and `s_8(A)>=1`. The terminal-collar theorem at commit `5dc3b183bf69c8ab69f725c4464d5073f5c803cd` proves the following dichotomy.

Either

\[
V_3(A)\ge\kappa^3,
\tag{3.1}
\]

or the order-two sampled interpolation has a quantitative two-sided collar. I checked the proof from its seed level:

- `V_1>=kappa`, otherwise `||A||<eta+sqrt(kappa)<1`;
- `V_2>=kappa V_1>=kappa^2`, because a bad `r=1` sampling ratio would yield five large diagonal defects but restricted interpolation rank one, contradicting strict diagonal dominance;
- if `V_3<kappa^3<=kappa V_2`, determinant-squared sampling at `r=2` has expected off-diagonal error `<9kappa`; Markov leaves at least half of `V_2` on seeds with `||E||_F^2<=18kappa`;
- global interpolation rank is at most six, restricted rank is at most two, so `s_8(A)>=1` forces two large diagonal defects outside the seed;
- the bordered determinant identity turns those two defects into overlap-one third minors;
- the same two coordinates form a determinant collar because the `2x2` interpolant block is diagonally dominant.

The resulting collar constant is

\[
\delta_*
={97\over100}-{297\sqrt2+3\sqrt{202}\over4000}
=0.85433514019\ldots .
\tag{3.2}
\]

No singular seed is inserted into the determinant-sampling identities.

If (3.1) holds, a fair literal coordinate cut has crossing third volume at least `4^{-3}kappa^3`. The audited marginal-free order-three receiver has `C_3<15`, so

\[
\boxed{\|p_Q\|_\infty<15(\kappa^3/64)^{-1/6}=2400.}
\tag{3.3}
\]

This branch has a continuous density.

## 4. The collar contains one robust literal physical pair

Assume the second terminal alternative. For each physical two-set `H`, define

\[
D_H=\sum_{|U|=2,\,U\cap H=\varnothing}\det A[H,U]^2
=\det(C_HC_H^T),\qquad C_H=A[H,H^c].
\tag{4.1}
\]

Cauchy–Binet gives

\[
\sum_H D_H=V_2(A).
\tag{4.2}
\]

Assign each good sampled seed to its two large-defect coordinates `H`; let `w_H` be the total determinant-squared seed mass assigned to `H`. Good seeds carry at least half of `V_2`, hence

\[
\sum_H w_H\ge\frac12\sum_HD_H.
\]

Therefore some `H` with `D_H>0` obeys `w_H>=D_H/2`. The two-sided determinant collar gives, after squaring and summing only its assigned seeds,

\[
\delta_*^2w_H\le\Xi_H\le D_H^2.
\]

Consequently

\[
\boxed{
g:=D_H=\det(CC^T)\ge{\delta_*^2\over2}=:d_0
=0.36494426588\ldots .
}
\tag{4.3}
\]

This step is dimension-free precisely because the full determinant bank `D_H` is normalized before any local minor is selected.

For exact arithmetic later, `sqrt2<3/2` and `sqrt202<15` imply

\[
\delta_*>6779/8000>4/5,
\qquad g>8/25.
\tag{4.4}
\]

## 5. At most one high-leverage coordinate

Put `L=H^c`, `G=CC^T`,

\[
Q_C=C^TG^{-1}C,\qquad P=I-Q_C,\qquad q_i=(Q_C)_{ii}.
\]

`Q_C` is a rank-two orthogonal projection, so `sum_i q_i=2`. Define the rank-two determinantal law

\[
w_{ij}={\det(C_{\{i,j\}})^2\over g},\qquad i<j.
\]

Cauchy–Binet and the determinantal inclusion identity give

\[
\sum_{i<j}w_{ij}=1,
\qquad q_i=\sum_{j\ne i}w_{ij}.
\tag{5.1}
\]

Because there is no `eta`-pivot,

\[
|A_{uv}|^2<\eta+\eta^2=101/10000\qquad(u\ne v).
\]

Every `2x2` physical cross minor of `C` therefore obeys

\[
|\det C_{\{i,j\}}|<2(101/10000)=101/5000.
\]

Together with (4.3),

\[
w_{ij}<0.00112<0.02.
\tag{5.2}
\]

If two distinct coordinates had `q_i,q_j>0.51`, inclusion–exclusion in the two-subset law would give

\[
w_{ij}\ge q_i+q_j-1>0.02,
\]

contradicting (5.2). Thus there is at most one exceptional coordinate `e` with leverage above `0.51`. Set `L'=L\setminus\{e\}` (choose an arbitrary `e` if no exception exists). Then

\[
\boxed{p_i:=P_{ii}=1-q_i\ge49/100\quad(i\in L').}
\tag{5.3}
\]

This is a physical-coordinate statement; no random coordinate system is rotated.

## 6. One-exception completion forces a macroscopic anchored third-volume packet

Let `D=A[L,L]`, write its row `i` as `d_i`, and put

\[
r_i=d_iP.
\]

For `i\in L'`, define

\[
W_i=\sum_{\substack{T\subset L\setminus\{i\}\\|T|=3}}
\det A[H\cup\{i\},T]^2.
\]

Since `r_i` is orthogonal to the two rows of `C`, Cauchy–Binet applied to the three-row frame `[C;r_i]`, with the column-`i` inclusion contribution removed, gives the exact identity

\[
\boxed{W_i=g\bigl(p_i\|r_i\|^2-r_{ii}^2\bigr).}
\tag{6.1}
\]

I checked this identity directly: the total third volume is `g||r_i||^2`, while the volume of triples containing column `i` is `g(q_i||r_i||^2+r_{ii}^2)`, because the leverage of column `i` in the orthogonal row sum `row(C)\oplus span(r_i)` equals `q_i+r_{ii}^2/||r_i||^2`.

Set `W'=sum_{i\in L'}W_i`. Define

\[
\lambda_i={r_{ii}\over p_i}\ (i\in L'),\qquad \lambda_e=0,
\]

and let `D_0=diag(lambda_i)`. Define a generally nonsymmetric outside error by

\[
e_i^TE=(d_i-\lambda_i e_i^T)P\quad(i\in L'),
\qquad e_e^TE=0,
\]

extended by zero on the anchor coordinates. Then `E_ii=0` and

\[
\|e_i^TE\|^2
=\|r_i\|^2-{r_{ii}^2\over p_i}
={W_i\over gp_i}.
\]

Hence from (5.3)

\[
\boxed{\|E\|_F^2\le {W'\over g(49/100)}.}
\tag{6.2}
\]

Put `R=A-D_0-E`. For every row except the single exceptional row `e`, the row of `R` lies in the four-dimensional deterministic space consisting of the two anchor-coordinate axes plus `row(C)`. The exceptional row contributes at most one further rank. Therefore

\[
\boxed{\operatorname{rank}R\le5.}
\tag{6.3}
\]

When both rows and columns are restricted to `L'`, the exceptional row is absent and the outside part is rowwise `(D-D_0)Q_C`; therefore

\[
\boxed{\operatorname{rank}R[L',L']\le2.}
\tag{6.4}
\]

Suppose `||E||_F<=1/4`. Then

\[
s_8(D_0+R)=s_8(A-E)\ge3/4.
\]

Using (6.3), the rank-shift inequality yields `s_3(D_0)>=3/4`. Thus three diagonal entries `lambda_i`, necessarily indexed in `L'`, have modulus at least `3/4`.

On these three physical coordinates,

\[
|R_{ii}|>|\lambda_i|-|A_{ii}|>0.74,
\]

whereas, for `i\ne j`,

\[
|R_{ij}|\le |A_{ij}|+|E_{ij}|
<\sqrt{101/10000}+1/4.
\]

The two-entry off-diagonal row sum is less than

\[
2(\sqrt{101/10000}+1/4)=0.7009975\ldots<0.74.
\]

Hence the selected `3x3` block of `R[L',L']` is strictly row-diagonally dominant and invertible, contradicting (6.4). Therefore `||E||_F>1/4`. Combining with (6.2),

\[
\boxed{W'>{49\over1600}g.}
\tag{6.5}
\]

This is the decisive rank budget: `5+3=8` globally while the physical restricted rank remains two.

## 7. Convert the packet into a product-safe density receiver

Randomly split the literal outside coordinates `L=I\sqcup J`. Every term in `W'` has one distinguished coordinate `i` and a disjoint three-set `T`; the event `i\in I`, `T\subset J` has probability `1/16`. Hence some physical cut satisfies

\[
\mathcal C
:=\sum_{\substack{i\in I\cap L'\\T\subset J,\ |T|=3}}
\det A[H\cup\{i\},T]^2
>{49g\over25600}
\ge {49d_0\over25600}.
\tag{7.1}
\]

Put `M=A[H,J]`. Positivity of `mathcal C` forces `M` to have row rank two. Project each literal row `A[i,J]`, `i\in I\cap L'`, orthogonally off `row(M)` and denote the residual by `c_i`. Gram–Schmidt and Cauchy–Binet give

\[
\boxed{\mathcal C=\det(MM^T)\sum_i\|c_i\|^2.}
\tag{7.2}
\]

Apply the audited grouped product-Fourier compiler with two literal anchor hubs and one residual volume direction, `(k,ell)=(2,1)`. If all residual first-volume marginals are at most one half, Fourier inversion gives

\[
\|p_Q\|_\infty
\le C_{21}\,\mathcal C^{-1/6},
\qquad
C_{21}=3\,2^{1/6}e^{2/3}.
\]

If one residual row has more than half the first-volume, promote that literal coordinate to a third hub; the terminal three-hub coefficient is smaller after the factor-two volume loss. Therefore the same displayed bound holds without a leverage restriction. From (7.1),

\[
\boxed{\|p_Q\|_\infty<22.02.}
\tag{7.3}
\]

The envelope is integrable, so this no-pivot terminal branch has a continuous `C_0` density. Arbitrary same-bank curvature and arbitrary affine terms remain in the phase throughout.

## 8. Full assembly and scaling

For normalized `K=s=1`, the exhaustive branch bounds are

- scalar pivot: `<1150` by (2.1);
- definite/indefinite pair pivot: `<40` / `<197` by (2.2);
- no pivot with `V_3>=kappa^3`: `<2400` by (3.3);
- no-pivot terminal collar: `<22.02` by (7.3).

Thus (1.1) holds in the normalized problem. For general `K,s`, set `Y=KX` and normalize the quadratic matrix by `s`; the output rescales by `s/K^2`, yielding exactly the factor `K^2/s`.

This proof preserves every owner quantifier.

## 9. Independent-review gate

A prior genuinely separate account03/B08 end-to-end review of the multiplicity-eight candidate is commit

`2bf752b5944536f51357d3d3b8b17212a297c7a6`.

The present B07 run independently reconstructed the terminal collar, robust-anchor averaging, determinant leverage law, one-exception nonsymmetric completion, both rank bounds, random-cut conversion, grouped `(2,1)` receiver, pivot assembly, and scaling. I obtain **PASS**.

Therefore there are now at least two separate complete mathematical review artifacts supporting the fixed-multiplicity-eight theorem. I do **not** alter an owner-level validation/release flag; reconciliation and any release decision remain separate.

## 10. Attempt below eight: multiplicity seven remains open

I checked the newest seven-direction structural router at commit

`e64de830ea3cf21eaa5c2c7b0650a4b0bb0de0e1`.

It does not claim a seven-direction theorem. Its useful exact facts are:

- deleting `q<=2` literal coordinates changes `A` by rank at most `2q`, so `s_7(A)>=1` leaves at least five unit directions after one deletion and at least three after two;
- if a parent/one-deletion/two-deletion spectral window is diffuse, an existing affine-uniform physical-window receiver pays the density;
- otherwise one gets three nested original-coordinate off-diagonal stars;
- independently, the invertible-seed overlap theorem supplies a quantitative overlap-one packet unless `V_3` is already large and paid.

The remaining unpaid state is thus an **overlap-one/shared-anchor packet coexisting with three nested physical stars**. No dependence-safe receiver converting that joint structure into a universal density bound is presently proved. The rank budget explains why the eight-direction one-exception completion does not simply descend: at seven, absorbing one exceptional physical row leaves global rank five and only two singular-value slots, not the three diagonal defects needed to contradict a restricted rank-two block.

Hence the rigorous fixed-multiplicity frontier after this run is

\[
\boxed{8\ \text{proved in the reviewed candidate chain};\quad 7\ \text{OPEN};\quad 3\ \text{OPEN}.}
\]
