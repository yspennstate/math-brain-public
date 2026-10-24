# account01/B13 — complete multiplicity-eight replacement proof

Run: `20260924T152809Z-account01-B13-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Status

**NEW INDEPENDENT RECONSTRUCTION: PASS as a mathematical candidate.**

I independently reconstructed the newly assembled multiplicity-eight chain rather than importing its conclusion. The resulting theorem is:

### Theorem `QFORM-FIXED-MULTIPLICITY-8-B13-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K`. Let `A=A^T`, `b in R^n`, `c in R`, and suppose

\[
s_8(A)\ge s>0.
\]

Then `Q=X^TAX+b^TX+c` has an essentially bounded density and

\[
\boxed{\|p_Q\|_\infty\le 6010\,K^2/s.}
\]

The constant is deliberately conservative. The statement preserves arbitrary coordinate laws, dimension, signature, remaining spectrum, and affine terms. No Gaussianity, moments, bounded support, log-concavity, exact rank, leverage restriction, diagonal basis, or post-rotation independence is assumed. Global continuity is not claimed.

This is a **candidate pending another genuinely separate end-to-end review**. This report is not a release flag or formal verification. The unrestricted three-eigenvalue conjecture remains open.

## Source-pinned ingredients independently checked in this run

1. The complete nine/400 source `paper.tex` at commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`; especially the marginal-free order-three density receiver and order-two full half-potential receiver.
2. The preserved baseline `manuscript.tex` at `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`; especially the baseline pivot threshold `eta=1/100`, spectral-to-volume argument, Schur count, square profile and hyperbolic pair.
3. The multiplicity-eight terminal-collar derivation of account03/B04, commit `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`.
4. The robust two-anchor extraction of account03/B17, commit `0408c579bcda638e72c010ff99892a22b9049796`.
5. The disjoint incident-volume receiver of account01/B19, commit `d44d368cd18a2590fc62d0aadd2cf2b7e9d0e83f`.
6. The one-high-leverage closure of account03/B20, commit `74542593cca87e76d83b07f98e2c895f76b90796` (the report is also present on current master).
7. The elementary two-high exclusion first assembled in account03/B01 commit `50a479407cc45f4fbcc87e70ac1846c049138c9f`.

The proof below reconstructs the dependencies explicitly.

---

## 1. Normalize and define the physical pivot chamber

It suffices to prove the theorem for `K=s=1`. At the end put `Y=KX` and apply the normalized result to `A/s`; since

\[
Q=(s/K^2)\widetilde Q,
\]

density scaling gives the factor `K^2/s`.

Use the baseline thresholds

\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2}=\frac1{6400}.
\]

A physical pivot means either

\[
|A_{ii}|\ge\eta
\]

or a principal two-coordinate determinant of modulus at least `eta`.

In the no-pivot chamber,

\[
|A_{ii}|<\eta,
\qquad
|A_{ij}|^2<\eta^2+\eta=0.0101
\quad(i\ne j).
\tag{1.1}
\]

The second inequality follows from

\[
A_{ij}^2\le |A_{ii}A_{jj}|+|A_{ii}A_{jj}-A_{ij}^2|.
\]

---

## 2. All pivot branches already close under `s_8>=1`

### 2.1 Scalar pivot

Suppose `|A_ii|>=eta`. Complete the square in the **original** coordinate `X_i`. The Schur complement `S` retains at least seven unit-scale eigenvalue moduli by the audited Schur spectral-count lemma.

The scalar-square profile gives, as a domination statement,

\[
p_Q(z)\le |A_{ii}|^{-1/2}\,\mathbb E|z-R|^{-1/2},
\tag{2.1}
\]

where `R` is the Schur remainder with arbitrary affine term.

We need a full half-potential bound for `R`.

- If `S` has a baseline `eta`-pivot, the baseline pivot-half-potential argument needs only two surviving spectral directions. Since `s_7(S)>=1`, it gives truncated half potential at most `600`, and adding the outside contribution `<=1` gives full half potential `<=601`.
- If `S` has no baseline pivot, `s_5(S)>=1`. Apply the baseline order-two spectral-to-volume proposition: `V_2(S)>=kappa^2`. A fair physical cut has a crossing block with

  \[
  Z_2\ge \frac{\kappa^2}{16}.
  \]

  The audited marginal-free order-two receiver from the nine-direction source gives

  \[
  \sup_a\mathbb E|R-a|^{-1/2}
  \le C_2 Z_2^{-1/8},\qquad C_2<14,
  \]

  which is finite and below 200; the exact value is not needed.

Therefore every scalar-pivot remainder has full half potential at most `601`, and since `eta^{-1/2}=10`,

\[
\boxed{\|p_Q\|_\infty\le6010.}
\tag{2.2}
\]

No independence between the completed square and the remainder is asserted.

### 2.2 Definite pair pivot

If a physical principal pair has determinant modulus `D>=eta` and is definite, condition on all other original coordinates. The pair density is a product density bounded by one, and the exact deterministic two-dimensional Jacobian gives

\[
\|p_Q\|_\infty\le \pi D^{-1/2}\le10\pi<40.
\tag{2.3}
\]

### 2.3 Indefinite pair pivot

If the pair is indefinite with determinant modulus `D>=eta`, its two-dimensional Schur complement retains at least six unit spectral directions and therefore at least one. The full two-sign hyperbolic envelope gives conditionally

\[
p(z)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\tag{2.4}
\]

The critical value `v` is a quadratic polynomial in the remaining original coordinates. One surviving spectral direction gives the baseline quarter-power small-ball estimate and hence

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}\le4+4\log16.
\]

Averaging the positive envelope by Tonelli, including the elementary maximum

\[
\sup_{D>0}D^{-1/2}\log_+D=2/e,
\]

gives the baseline bound below `251`, hence certainly below `6010`.

Thus all physical pivot branches close already at multiplicity eight.

---

## 3. No-pivot structural dichotomy at eight directions

Assume from now on no pivot and `s_8(A)>=1`.

Define ordered disjoint minor volumes

\[
V_r(A)=\sum_{\substack{|S|=|T|=r\\S\cap T=\varnothing}}
\det A[S,T]^2.
\]

If

\[
V_3(A)\ge\kappa^3,
\tag{3.1}
\]

a fair original-coordinate cut has a literal crossing block with

\[
Z_3\ge4^{-3}\kappa^3.
\]

The marginal-free order-three physical-product receiver gives

\[
\|p_Q\|_\infty\le C_3Z_3^{-1/6}
=160C_3<2400,
\qquad C_3<15.
\tag{3.2}
\]

So only `V_3<kappa^3` remains.

### 3.1 First two volume ratios cannot be small

First `V_1>=kappa`: otherwise

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\eta+\sqrt\kappa<1,
\]

contrary to `s_8(A)>=1`.

Next `V_2>=kappa V_1>=kappa^2`. If instead `V_2<kappa V_1`, apply the sampled interpolation at `r=1`. There is a seed with

\[
A=D+R+E,\qquad
\|E\|\le\|E\|_F<2\sqrt\kappa=1/40,
\]

`rank R<=3`, `rank R[L,L]<=1`, `D` diagonal and zero on the seed, `E` zero diagonal. Then

\[
s_8(D+R)\ge39/40,
\]

so rank perturbation gives `s_5(D)>=39/40`. Hence at least two coordinates in `L` have `|D_i|>=39/40`. On those two coordinates,

\[
|R_{ii}|\ge39/40-1/100=0.965,
\]

while

\[
|R_{ij}|<\sqrt{\eta^2+\eta}+1/40<0.126.
\]

The resulting `2x2` restricted block is strictly row-diagonally dominant and has rank two, contradicting `rank R[L,L]<=1`.

Therefore

\[
V_2\ge\kappa^2,
\qquad
\frac{V_3}{V_2}<\kappa.
\tag{3.3}
\]

### 3.2 Good order-two seeds and the two-sided collar

Sample each invertible disjoint two-seed `B=A[S,T]` with probability `det(B)^2/V_2`. The interpolation theorem gives

\[
\mathbb E_B\|F_B\|_F^2\le9V_3/V_2<9\kappa.
\]

Call a seed good when

\[
\|F_B\|_F^2\le18\kappa.
\]

Good seeds carry at least half the determinant-squared mass. Put

\[
\varepsilon_*:=\sqrt{18\kappa}=\frac{3\sqrt2}{80}.
\]

For a good seed, the completion has `rank R<=6`, `rank R[L,L]<=2`, and

\[
s_8(D+R)\ge1-\varepsilon_*.
\]

Rank perturbation gives `s_2(D)>=1-\varepsilon_*`. Thus there are two coordinates `H={h_1,h_2}` in the seed complement with

\[
|D_h|\ge1-\varepsilon_*.
\tag{3.4}
\]

The exact interpolation identities imply

\[
|\det A[S,H]\det A[H,T]|
\ge\delta_*|\det A[S,T]|,
\tag{3.5}
\]

where

\[
\delta_*=(1-\varepsilon_*-\eta)^2-
(\sqrt{\eta^2+\eta}+\varepsilon_*)^2
=0.8543351401911337\ldots>0.
\tag{3.6}
\]

This follows because the diagonal entries of the interpolation block `P_B[H,H]` have modulus at least `1-epsilon_*-eta`, the off-diagonal entries have modulus at most `sqrt(eta^2+eta)+epsilon_*`, so its determinant has modulus at least `delta_*`, while

\[
P_B[H,H]=A[H,T]B^{-1}A[S,H].
\]

---

## 4. Extract one literal robust anchor pair

For every two-set `H`, let

\[
D_H:=\sum_{\substack{U\subset H^c\\|U|=2}}\det A[H,U]^2
=\det(C_HC_H^T),
\qquad C_H=A[H,H^c].
\tag{4.1}
\]

Since `V_2` is the ordered disjoint volume,

\[
\sum_H D_H=V_2.
\tag{4.2}
\]

Assign each good seed one pair `H` obtained above and let

\[
w_H:=\sum_{B\text{ good assigned to }H}\det(B)^2.
\]

Good mass is at least `V_2/2`, so some `H_*` with `D_{H_*}>0` satisfies

\[
w_{H_*}\ge\frac12D_{H_*}.
\tag{4.3}
\]

For this pair, square (3.5) and sum assigned seeds. The left side is at most `D_{H_*}^2` after dropping disjointness in the nonnegative double sum. Hence

\[
\delta_*^2w_{H_*}\le D_{H_*}^2.
\]

Using (4.3),

\[
\boxed{
g:=D_{H_*}=\det(CC^T)\ge\frac{\delta_*^2}{2}
=:d_0=0.3649442658827020\ldots,
}
\tag{4.4}
\]

where `C=A[H_*,H_*^c]` is a literal `2 x (n-2)` physical cross block.

This step is important: it spends aggregate collar mass only after normalizing by the exact identity `sum_H D_H=V_2`; it never divides by one selected tiny minor.

---

## 5. Leverage partition and the disjoint incident volume

Write `H=H_*`, `L=H^c`, and

\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
\qquad g=\det(CC^T)\ge d_0.
\]

Define the rank-two projection

\[
Q_C=C^T(CC^T)^{-1}C,
\qquad P=I-Q_C,
\]

and leverage scores

\[
q_i=(Q_C)_{ii},\qquad p_i=P_{ii}=1-q_i.
\]

Since `rank Q_C=2`,

\[
\sum_{i\in L}q_i=2.
\tag{5.1}
\]

Let

\[
J=\{i:q_i>2/3\},\qquad U=L\setminus J.
\]

Then `|J|<=2` and `p_i>=1/3` on `U`.

For row `d_i` of `D`, set

\[
r_i=d_iP.
\]

Define the product-usable incident third-minor energy

\[
W_i=\sum_{\substack{T\subset L\setminus\{i\}\\|T|=3}}
\det A[H\cup\{i\},T]^2,
\qquad
W_{\rm dis}=\sum_iW_i.
\]

A leave-one-column Gram/Cauchy–Binet identity gives exactly

\[
W_i=g\left(p_i\|r_i\|_2^2-r_{ii}^2\right).
\tag{5.2}
\]

For `i in U`, set

\[
\lambda_i=r_{ii}/p_i,
\qquad
e_i^TE=(d_i-\lambda_ie_i^T)P.
\]

For `i in J`, set `lambda_i=0` and the row of `E` to zero. Then `E_ii=0`, and from (5.2)

\[
\|e_i^TE\|_2^2
=\|r_i\|_2^2-r_{ii}^2/p_i
=\frac{W_i}{gp_i}.
\]

Therefore

\[
\boxed{
\|E\|_F^2\le\frac3gW_{\rm dis}.
}
\tag{5.3}
\]

---

## 6. Zero or one high leverage forces a paid disjoint bank

Assume `|J|=h<=1` and, for contradiction,

\[
W_{\rm dis}\le g/48.
\]

Then (5.3) gives `||E||<=1/4`.

Let `D_0` be diagonal with entries `lambda_i` on `U` and zero on `H union J`, and put

\[
R=A-D_0-(0_H\oplus E).
\]

All low rows of `R` lie in the direct sum of the two physical anchor-coordinate directions and the two-dimensional row space of `C`; each high row can add at most one extra row direction. Thus

\[
\operatorname{rank}R\le4+h.
\tag{6.1}
\]

Restricting to `U x U`, every row lies in the restricted row space of `C`, so

\[
\operatorname{rank}R[U,U]\le2.
\tag{6.2}
\]

Since `s_8(A)>=1`, Weyl/rank perturbation gives

\[
s_8(D_0+R)\ge3/4,
\qquad
s_{4-h}(D_0)\ge3/4.
\]

For `h<=1`, at least three coordinates `I subset U` satisfy `|lambda_i|>=3/4`. On this `3x3` principal block,

\[
|R_{ii}|\ge3/4-\eta=0.74,
\]

whereas for `i!=j`, using `|E_ij|<=||E||_F<=1/4` and (1.1),

\[
|R_{ij}|<\sqrt{\eta^2+\eta}+1/4
=0.3504987562\ldots.
\]

The two off-diagonal absolute values in any row therefore sum to less than

\[
0.7009975125<0.74.
\]

So `R[I,I]` is invertible and has rank three, contradicting (6.2). Hence

\[
\boxed{W_{\rm dis}>g/48.}
\tag{6.3}
\]

### Product-law receiver for (6.3)

A fair partition `L=I sqcup J'` captures at least `W_dis/16` in genuinely disjoint physical row/column banks. If residual row-volume is diffuse, the grouped physical-product compiler with two literal anchor hubs yields density

\[
\le3\,2^{1/6}e^{2/3}W(I,J')^{-1/6}.
\]

If one residual row is heavy, promote that **literal original coordinate** as a third hub and use the terminal three-hub Plancherel bound. Both routes give

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm inc}W_{\rm dis}^{-1/6},
\qquad
C_{\rm inc}=3\,2^{5/6}e^{2/3}=10.4114\ldots .
}
\tag{6.4}
\]

Together with `g>=d0`, (6.3) gives a density below `23.48`.

No same-coordinate collision is treated as independent; the random cut is applied only to terms with the distinguished row coordinate absent from the three column coordinates.

---

## 7. Two high leverages are impossible in the no-pivot chamber

It remains only to exclude `|J|=2`.

For every two-set `{a,b}` in `L`, define the normalized determinantal weights

\[
w_{ab}:=\frac{\det(C_{\{a,b\}})^2}{g}.
\]

Cauchy–Binet gives

\[
\sum_{a<b}w_{ab}=1.
\]

The one-point determinantal marginals are exactly

\[
q_i=\sum_{b\ne i}w_{ib}.
\tag{7.1}
\]

If distinct `i,j` both satisfy `q_i,q_j>2/3`, then

\[
w_{ij}\ge q_i+q_j-1>1/3,
\]

and therefore

\[
\det(C_{\{i,j\}})^2>g/3\ge d_0/3
=0.1216480886\ldots .
\tag{7.2}
\]

But all four entries of this literal `2x2` cross minor are off-diagonal entries of `A`, so the no-pivot bound (1.1) gives

\[
|\det C_{\{i,j\}}|
\le |A_{h_1i}A_{h_2j}|+|A_{h_1j}A_{h_2i}|
<2(\eta^2+\eta)=0.0202.
\]

Hence

\[
\det(C_{\{i,j\}})^2<0.00040804,
\tag{7.3}
\]

which contradicts (7.2) by more than two orders of magnitude.

Thus `|J|<=1` necessarily, and Section 6 always pays the terminal collar.

---

## 8. End-to-end normalized conclusion

Every normalized `s_8(A)>=1` state is in exactly one of the following paid branches:

1. scalar pivot: density `<=6010`;
2. definite pair pivot: density `<40`;
3. indefinite pair pivot: density `<251`;
4. no pivot with `V_3>=kappa^3`: density `<2400`;
5. no pivot with `V_3<kappa^3`: robust anchor extraction plus leverage partition forces `W_dis>g/48`, hence density `<23.48`.

Therefore

\[
\boxed{\|p_Q\|_\infty\le6010}
\]

for every normalized state. Scaling proves the theorem with `6010 K^2/s`.

The proof establishes absolute continuity and an essential density bound. Some Fourier branches are `C_0`, but no global continuity claim is made.

---

## 9. Adversarial second pass over the replacement proof

I reran the chain in reverse, looking specifically for the live forbidden shortcuts.

- **Rotations:** all probabilistic conditioning, copying and promotion is in literal original coordinates. Orthogonal projections `Q_C,P` are deterministic coefficient-space algebra only. PASS.
- **Indefinite pair:** the hyperbolic proof uses both level-set branches, both tails, and a moving critical value averaged by a positive majorant. No projected-density-only shortcut is used. PASS.
- **Small diagonal / pair curvature:** no coefficient-small term is discarded. The no-pivot chamber uses only exact entry inequalities and determinant identities. PASS.
- **Shared coordinate:** the incident-volume receiver uses only `W_dis`; collision terms are not fed into an independence argument. PASS.
- **Aggregate-to-local:** robust-anchor extraction divides only after the exact normalization `sum_H D_H=V_2`; it never selects a tiny minor and pays its reciprocal. PASS.
- **Nonsymmetric auxiliaries:** only singular values and ranks are used for the interpolation/completion matrices. PASS.
- **Affine terms:** all analytic receivers are uniform in affine terms; conditioning changes them but not the quadratic coefficient hypotheses. PASS.
- **Scaling:** `Y=KX` preserves a cap-one product law; `A/s` restores unit spectral scale; output scaling gives exactly `K^2/s`. PASS.

I found no gap in this reconstruction.

## 10. Review status and threshold frontier

This B13 reconstruction is an independent mathematical review of the newly assembled multiplicity-eight chain, but it does not by itself satisfy the owner's requirement for two genuinely separate complete reviews of the new candidate. Therefore:

- multiplicity 8: **COMPLETE CANDIDATE / PASS IN THIS REVIEW / NOT YET INDEPENDENTLY VALIDATED**;
- multiplicity 7: **OPEN**;
- unrestricted multiplicity 3: **OPEN**.

At multiplicity seven, the strongest source-pinned structural endpoint read in this run is: either the ordinary disjoint third volume already pays the density, or a fixed invertible-seed overlap-one packet survives together with three nested physical off-diagonal stars after failure of parent/one-delete/two-delete spectral-window receivers. A dependence-safe analytic receiver for that shared-anchor overlap packet is still missing. I did not find a rigorous route from that packet to an `L^infinity` bound without reusing the shared original coordinate as if independent. Accordingly I do not claim seven.
