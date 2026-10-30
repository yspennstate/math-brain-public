# QFORM-S16-MIXED-EXTERIOR-ENDPOINT-v1

Run: `20260924T134332Z-fixedmult-auto11-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **proved supporting theorem and a paid `s_16` sub-branch; NOT a universal 16-eigenvalue theorem**.

## Pinned dependencies

Baseline manuscript:

- `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Transverse `s_16` carrier theorem consumed here:

- `yspennstate/math-open-problems@15082841edd324c5a29c7fb4d9ceb2f81726f107`
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B11/20260924T131227Z-fleet03-B11-fixedmult-r57/TRANSVERSE_S16.md`
- blob `68cfb76a592b389ac5d7719e8dff0fdd65bdb127`.

That theorem supplies, in the only unpaid normalized no-pivot `s_16(A)>=1` chamber, an original-coordinate cut `[n]=I sqcup J`, cross block `M=A[I,J]`, its top-four left singular space `U`, and the same-bank zero-diagonal matrix `O=A[I,I]-diag(A[I,I])` such that

\[
Z_4(M)\ge \frac{\kappa^4}{1280},\qquad
s_4((I-P_U)O)\ge\frac{1559}{1600},
\qquad \kappa=\frac1{6400}.
\tag{0}
\]

The result below converts this transverse same-bank mass into a literal fifth physical crossing unless a precise row-overlap functional traps at least half of the mixed exterior energy.

---

## 1. General mixed four-plus-one exterior identity

Let `M` be any real `m x n` matrix with `Z_4(M)>0`. Write its squared singular values in decreasing order as

\[
x_1\ge x_2\ge\cdots\ge0,
\qquad x_j=\sigma_j(M)^2,
\]

and let `U` be the span of its first four left singular vectors. Let `P_U` denote the orthogonal projection onto `U`.

For a physical four-column set `T`, put

\[
W_T=M[:,T],\qquad
w_T=\det(W_T^TW_T).
\]

When `w_T>0`, let `P_T` be the orthogonal projection onto `ran(W_T)`; when `w_T=0`, every expression below multiplied by `w_T` is defined as zero.

For a vector `y in R^m`, define its mixed four-plus-one volume

\[
\mathcal U_M(y)
:=
\sum_{|T|=4} w_T\,\|(I-P_T)y\|_2^2.
\tag{1}
\]

### Theorem 1 — exact spectral representation and a universal `1/5` exclusion gap

One has

\[
\boxed{
\mathcal U_M(y)
=
\sum_{|R|=4} x_R\,\|(I-P_R)y\|_2^2,
}
\tag{2}
\]

where the sum on the right is over four-subsets of the left singular directions, `x_R=prod_{j in R}x_j`, and `P_R` is projection onto their span. Consequently

\[
\boxed{
\mathcal U_M(y)
\ge
\frac{Z_4(M)}5\,\|(I-P_U)y\|_2^2.
}
\tag{3}
\]

#### Proof

The left side of (1) is the squared Hilbert--Schmidt norm of the exterior map obtained by applying `wedge^4 M` and then wedging its output with `y`. Hence it is invariant under right orthogonal changes of coordinates in the domain. Apply an SVD of `M`. On the standard exterior basis, `wedge^4 M` sends a four-set `R` to

\[
\Bigl(\prod_{j\in R}\sigma_j\Bigr)u_R,
\]

where `u_R` is a unit decomposable four-vector. Wedging with `y` has squared norm

\[
\|u_R\wedge y\|^2=\|(I-P_R)y\|^2.
\]

This proves (2). Equivalently, it is a Cauchy--Binet identity for all five-by-five minors in which four columns come from `M` and the fifth is the distinguished vector `y`.

The coefficient of `|<y,u_j>|^2` in (2), divided by `Z_4=e_4(x)`, is

\[
\frac{e_4(x_{\ne j})}{e_4(x)}.
\tag{4}
\]

For every `j>=5`,

\[
x_j e_3(x_{\ne j})\le4e_4(x_{\ne j}).
\tag{5}
\]

Indeed,

\[
4e_4(x_{\ne j})
=
\sum_{|R|=3,\,j\notin R}x_R
\sum_{k\notin R,\,k\ne j}x_k.
\]

Every three-set `R` misses at least one of the indices `1,2,3,4`; that missed coordinate has `x_k>=x_j`. Thus every inner sum is at least `x_j`, proving (5). Since

\[
e_4(x)=x_j e_3(x_{\ne j})+e_4(x_{\ne j}),
\]

(5) implies

\[
\frac{e_4(x_{\ne j})}{e_4(x)}\ge\frac15
\qquad(j\ge5).
\]

All coefficients are nonnegative, so discarding the first four left singular directions gives (3). QED.

---

## 2. Exact physical-disjoint defect formula

Now let `O=O^T` be any zero-diagonal `m x m` matrix. For each physical coordinate `c`, write

\[
y_c=Oe_c,
\qquad y_c(c)=0.
\]

For `w_T>0` define

\[
r_{c,T}=(I-P_T)y_c,
\qquad
\ell_{c,T}=e_c^TP_Te_c.
\tag{6}
\]

Define the full mixed exterior energy

\[
\mathcal U(M,O)
:=
\sum_c\sum_{|T|=4}w_T\|r_{c,T}\|^2,
\tag{7}
\]

and the **physically disjoint** mixed energy

\[
\mathcal D(M,O)
:=
\sum_c\sum_{|T|=4}
\sum_{\substack{S\subset[m]\setminus\{c\}\\|S|=5}}
\det\bigl([M_{S,T}\; y_c|_S]\bigr)^2.
\tag{8}
\]

### Theorem 2 — exact overlap loss

One has

\[
\boxed{
\mathcal D(M,O)
=
\sum_{c,T}w_T
\left[
(1-\ell_{c,T})\|r_{c,T}\|^2-|r_{c,T}(c)|^2
\right].
}
\tag{9}
\]

In particular, with

\[
\mathcal F(M,O)
:=
\sum_{c,T}w_T
\left[
\ell_{c,T}\|r_{c,T}\|^2+|r_{c,T}(c)|^2
\right],
\tag{10}
\]

we have the exact decomposition

\[
\boxed{\mathcal U=\mathcal D+\mathcal F.}
\tag{11}
\]

Both `D` and `F` are nonnegative.

#### Proof

Fix `c,T` with `w_T>0`. Put `B=[W_T\;y_c]`. The Schur-complement formula for the Gram determinant gives

\[
\det(B^TB)=w_T\|r_{c,T}\|^2.
\tag{12}
\]

By Cauchy--Binet, this is the total squared mass of all five-row minors of `B`. The fraction of that row-volume mass carried by five-sets containing row `c` is the row leverage of `c` in `B`. Because `r_{c,T}` is orthogonal to `ran(W_T)`, the projection onto `ran(B)` is

\[
P_T+\frac{r_{c,T}r_{c,T}^T}{\|r_{c,T}\|^2}
\]

when `r_{c,T}\ne0`. Hence that leverage is

\[
\ell_{c,T}+rac{|r_{c,T}(c)|^2}{\|r_{c,T}\|^2}.
\]

Subtracting the row-minor mass containing `c` from (12) gives exactly (9). The zero-residual and singular-`W_T` cases follow by continuity or directly because every relevant five-minor vanishes. Nonnegativity is automatic because (8) is a sum of squares and `F=U-D` is exactly the complementary row-minor mass. QED.

---

## 3. Product-preserving random split

Split the physical row bank independently and fairly as

\[
I=R\sqcup C.
\]

The new literal original-coordinate cut is

\[
R\ \big|\ (J\cup C),
\]

whose crossing block is

\[
N_R=[\,M_{R,J}\ \ O_{R,C}\,].
\tag{13}
\]

Every summand in (8) consists of five distinct row coordinates `S` and one different coordinate `c`. It appears among the order-five minors of `N_R` whenever `S subset R` and `c in C`, an event of probability `2^{-6}`. Therefore

\[
\boxed{
\mathbb E_R Z_5(N_R)
\ge\frac1{64}\mathcal D(M,O).
}
\tag{14}
\]

(The inequality rather than equality merely ignores other order-five minors of `N_R`.) Thus some literal physical repartition satisfies

\[
\boxed{Z_5(N_R)\ge\mathcal D(M,O)/64.}
\tag{15}
\]

No spectral rotation is applied to the random variables.

---

## 4. Consequence in the terminal `s_16` chamber

Consume the fleet03/B11 transverse-carrier theorem (pinned above). Its physical `M,O,U` satisfy (0). By Theorem 1,

\[
\begin{aligned}
\mathcal U(M,O)
&\ge\frac{Z_4(M)}5\|(I-P_U)O\|_F^2\\
&\ge\frac{Z_4(M)}5\cdot4\left(\frac{1559}{1600}\right)^2\\
&=
\frac{2430481}{3200000}\,Z_4(M).
\end{aligned}
\tag{16}
\]

Thus the transverse theorem forces a **universal amount of mixed four-plus-one exterior energy**; the only issue is whether that energy is physically disjoint.

### Paid branch

If

\[
\boxed{\mathcal D(M,O)\ge\frac12\mathcal U(M,O),}
\tag{17}
\]

then (15), (16), and `Z_4(M)>=kappa^4/1280` give a physical cut with

\[
Z_5(N_R)
\ge
\frac{2430481}{524288000000}\,\kappa^4.
\tag{18}
\]

The manuscript's order-five Fourier theorem therefore applies to the **full original quadratic polynomial**, retaining all same-bank curvature and affine terms:

\[
\|p_Q\|_\infty
\le
5e\left(
\frac{2430481}{524288000000}\,\kappa^4
\right)^{-1/10}
<1546.
\tag{19}
\]

This is an actual arbitrary-law, arbitrary-dimension `L^infinity` payment of this terminal `s_16` sub-branch.

After the usual normalization, the same branch gives `<1546 K^2/s`.

### Exact remaining obstruction

If (17) fails, then

\[
\boxed{
\mathcal F(M,O)>\frac12\mathcal U(M,O),
}
\tag{20}
\]

where `F` is the explicit positive functional (10). Hence at least one of the two mechanisms carries more than one quarter of the forced mixed exterior energy:

\[
\sum_{c,T}w_T\ell_{c,T}\|r_{c,T}\|^2
>\frac14\mathcal U
\tag{21a}
\]

or

\[
\sum_{c,T}w_T|r_{c,T}(c)|^2
>\frac14\mathcal U.
\tag{21b}
\]

Equation (21a) is a **four-volume row-leverage trap**: the candidate fifth directions are preferentially attached to physical rows already heavily present in the four-dimensional crossing. Equation (21b) is a **self-coordinate residual trap**: after projecting away a physical four-column carrier, the residual fifth direction is strongly aligned with the same coordinate that labels its zero-diagonal same-bank column.

These are exact, positive, physical-coordinate obstructions. They replace the vague statement that the transverse fifth direction may be lost under repartition.

---

## 5. What has and has not been proved

Combining the baseline manuscript, the fleet03/B11 transverse-carrier theorem, and the new identities above yields the following rigorous reduction under normalized `s_16(A)>=1`:

1. Every pivot branch is already paid by the manuscript.
2. In the no-pivot branch, if `V_5>=kappa^5`, the manuscript's order-five cut pays the density.
3. In the only remaining transverse order-four chamber, the full mixed four-plus-one energy is uniformly positive by (16).
4. If at least half of that energy is physically disjoint, (19) gives the full-law density bound `<1546`.
5. Therefore every still-unpaid `s_16` survivor must satisfy the explicit trapping inequality (20), hence (21a) or (21b).

This is a strict reduction of the `17 -> 16` problem but **not** a universal 16-eigenvalue theorem. A complete `s_16` proof still needs a product-preserving receiver for the leverage trap (21a) and the self-coordinate trap (21b), or a proof that one of them forces an already-paid pivot/hub endpoint. No Gaussianity, moment assumption, bounded support, leverage hypothesis, exact-rank hypothesis, or independence after rotation has been introduced.

The unrestricted three-eigenvalue conjecture remains open.
