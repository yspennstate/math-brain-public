# fleet02/B18 r27 — circular two-sheet stress family and dual compiler barrier

## Status and first unpaid implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** This report proves a new target-valid obstruction to two current proof compilers; it does not give a counterexample to the conjecture.

New claim: `QFORM-CIRCULAR-DUAL-COMPILER-BARRIER-v1` (`PROVED_IN_SOURCE_PENDING_INDEPENDENT_REVIEW`).

The first unpaid implication after this run is now concrete:

> `QFORM-CIRCULAR-TWOSHEET-ZEROPIVOT-v1`: for the circular Parseval family below, prove a universal bound on the **negative / two-sheet** density using the original-coordinate product law, without a nonzero physical Schur pivot, an exact low-dimensional coordinate bank, or one rank-three cross-volume cut.

The positive / one-sheet half-line is already paid by the pinned ruled-surface theorem with constant `pi sqrt(2)`.

Target hypotheses retained throughout: independent real inputs with one-dimensional probability densities bounded by one; no moments, support restrictions, iid assumption, log-concavity, smoothness, diagonal-basis independence, or post-rotation independence. Continuity is separate from essential boundedness.

## 1. Exact target family

For `m>=3`, let

\[
v_j=m^{-1/2}\bigl(1,\sqrt2\cos(2\pi j/m),\sqrt2\sin(2\pi j/m)\bigr),
\qquad j=0,\dots,m-1.
\]

The elementary trigonometric sums give

\[
V^TV=I_3,\qquad \|v_j\|^2=3/m.
\]

Fix `r>0`, set

\[
s=\sqrt{1+r^2},\qquad u_0=r e_1,
\]

and let `U` have rows `u_0,v_0,...,v_{m-1}`. Define

\[
D_r=
\begin{pmatrix}
0&s^{-1}&0\\
s^{-1}&0&0\\
0&0&1
\end{pmatrix},
\qquad
A_{m,r}=U D_r U^T.
\]

Then

\[
U^TU=\operatorname{diag}(s^2,1,1).
\]

The nonzero eigenvalues of `UD_rU^T` equal those of `D_rU^TU`; the latter matrix is

\[
\begin{pmatrix}0&s^{-1}&0\\s&0&0\\0&0&1\end{pmatrix},
\]

so

\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,r})=\{-1,1,1\}.}
\]

Thus every member of the family satisfies the exact QFORM spectral hypothesis, uniformly in both `m` and `r`.

Writing `Y=V^TX_R`, the quadratic form is

\[
Q_{m,r}=\frac{2}{s}(Y_1+rX_0)Y_2+Y_3^2.
\]

The hub diagonal is zero. The residual physical diagonals satisfy

\[
|A_{jj}|=|v_j^TD_rv_j|\le\|D_r\|_{op}\|v_j\|^2=3/m.
\]

Moreover the hub-residual pair determinants satisfy `|det A[{0,j}]|=A_{0j}^2<=2/m`, and the previously checked circular-frame bound gives residual pair determinants `<=18/m^2`. Hence for every fixed N3 threshold `tau>0`, the family with `m` large lies in the live no-pivot window.

## 2. Completed e5f result actually applied: the one-sheet half is already closed

Pinned source:

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C.

For a rank-three form of signature `(2+,1-)` with all three absolute eigenvalues at least one, that theorem proves on the one-sheet side

\[
p_Q(t)\le \pi\sqrt2,\qquad t\ge0.
\]

Since `A_{m,r}` has exact nonzero spectrum `{-1,1,1}`,

\[
\boxed{p_{Q_{m,r}}(t)\le\pi\sqrt2\quad\text{for a.e. }t\ge0,}
\]

for every `m,r` and every admissible product input law. Thus any unresolved behavior of this family is confined to the negative / two-sheet side. No rotated-coordinate independence is asserted in this application.

## 3. Primary-source check behind the partner compiler

The designated partner fleet03/B18 proved at

`math-open-problems@dfbc17f17b702ed7c7191ba24648a70f67dda851`

that if a nonzero original physical scalar pivot `a=A_ii` has a Schur complement admitting an original-coordinate rank-two cross block `B` with nonzero singular values `sigma_1,sigma_2`, then

\[
\boxed{
\|p_Q\|_\infty\le8|a|^{-1/2}(\sigma_1\sigma_2)^{-1/4}.
}
\tag{3.1}
\]

Its only external probabilistic input is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1. The primary statement is source-matched: for `1<=k<n`, a product probability density `f=prod f_i` with bounded nonnegative one-dimensional factors of integral one has, for every `k`-dimensional orthogonal marginal,

\[
\|\pi_E f\|_\infty
\le
\min\left\{
\left(\frac n{n-k}\right)^{(n-k)/2},2^{k/2}
\right\}
\prod_i\|f_i\|_\infty^{\gamma_i},
\quad \sum_i\gamma_i=k.
\]

Consequently cap-one product inputs give `||pi_E f||_infty<=2^{k/2}`. There is no moment, support, log-concavity, smoothness, symmetry, or iid hypothesis. The theorem bounds the **joint density of the orthogonal projection**; it does not say the projected coordinates are independent. If the source block has exactly `k` coordinates, the same cap needed by the partner follows trivially from the original product density rather than from the formal `k<n` statement.

This is exactly the source scope used in (3.1), and no stronger interpretation is used below.

## 4. New algebraic barrier for every one-pivot rank-two Schur certificate

Fix a residual physical coordinate `i` with

\[
a_i=(A_{m,r})_{ii}=v_i^TD_rv_i\ne0.
\]

Let `S=A_{m,r}/a_i` denote its scalar Schur complement. By congruence,

\[
\operatorname{rank}S=2.
\]

Partition all remaining physical coordinates as `L disjoint_union R`, and write

\[
B=S_{L,R}.
\]

Assume `B` has rank two, so that the partner theorem (3.1) is applicable. By Cauchy--Binet,

\[
(\sigma_1(B)\sigma_2(B))^2
=
\sum_{p<q\in L}\sum_{k<\ell\in R}
\det B_{\{p,q\},\{k,\ell\}}^2.
\tag{4.1}
\]

For a scalar Schur complement,

\[
\det B_{\{p,q\},\{k,\ell\}}
=
\frac1{a_i}
\det A_{\{i,p,q\},\{i,k,\ell\}}.
\tag{4.2}
\]

Because `A=UD_rU^T` has rank three,

\[
\det A_{\{i,p,q\},\{i,k,\ell\}}
=
\det(D_r)\,\det(u_i,u_p,u_q)\,\det(u_i,u_k,u_\ell).
\tag{4.3}
\]

Define

\[
\Omega_L(i)=\sum_{p<q\in L}\det(u_i,u_p,u_q)^2,
\qquad
\Omega_R(i)=\sum_{k<\ell\in R}\det(u_i,u_k,u_\ell)^2.
\]

Equations (4.1)--(4.3) give the exact factorization

\[
\sigma_1(B)\sigma_2(B)
=
\frac{|\det D_r|}{|a_i|}
\sqrt{\Omega_L(i)\Omega_R(i)}.
\tag{4.4}
\]

Let

\[
T_i=\sum_{p<q;\ p,q\ne i}\det(u_i,u_p,u_q)^2.
\]

The pair collections contributing to `Omega_L` and `Omega_R` are disjoint, hence

\[
\Omega_L+\Omega_R\le T_i,
\qquad
\sqrt{\Omega_L\Omega_R}\le T_i/2.
\]

Therefore

\[
\sigma_1(B)\sigma_2(B)
\le
\frac{|\det D_r|}{2|a_i|}T_i.
\tag{4.5}
\]

Now use the standard Cauchy--Binet leverage identity. For `G=U^TU`, the total squared three-volume through row `i` is

\[
T_i=\det(G)\,u_i^TG^{-1}u_i.
\]

Here `G=diag(s^2,1,1)` and `u_i=v_i`, so

\[
u_i^TG^{-1}u_i
=
\frac1{m(1+r^2)}+\frac2m,
\]

and hence

\[
\boxed{T_i=\frac{3+2r^2}{m}.}
\tag{4.6}
\]

Also

\[
|\det D_r|=(1+r^2)^{-1},
\qquad
|a_i|\le3/m.
\]

Thus

\[
|a_i|\,|\det D_r|\,T_i
\le
\frac3m\frac1{1+r^2}\frac{3+2r^2}{m}
\le\frac9{m^2}.
\tag{4.7}
\]

Insert (4.5) into the partner certificate (3.1):

\[
8|a_i|^{-1/2}(\sigma_1\sigma_2)^{-1/4}
\ge
8\,2^{1/4}
\bigl(|a_i|\,|\det D_r|\,T_i\bigr)^{-1/4}.
\]

Using (4.7), every applicable one-pivot rank-two certificate obeys

\[
\boxed{
8|a_i|^{-1/2}(\sigma_1\sigma_2)^{-1/4}
\ge
\frac{8\,2^{1/4}}{\sqrt3}\sqrt m
=5.4927123837\ldots\sqrt m.
}
\tag{4.8}
\]

If the chosen cross block has rank below two, the partner theorem is unavailable rather than better. The hub itself has zero pivot. Therefore **no application of the completed one-pivot rank-two Schur compiler can give a dimension-free certificate on this family**.

This is a lower bound on that theorem's numerical certificate, not a lower bound on the true density.

## 5. The latest nested partner compiler is structurally incompatible here

The newest designated-partner handoff,

`math-open-problems@2d03e0a0014e3aa8e3ecf95994501bde16093872`,

iterates nonzero scalar Schur pivots outside a terminal rank-two cross block. But every nonzero scalar Schur pivot reduces matrix rank by exactly one:

\[
\operatorname{rank}A=1+\operatorname{rank}(A/a_i).
\]

Since `rank(A_{m,r})=3`, after two successive nonzero scalar pivots the residual rank is at most one. It therefore cannot contain a rank-two cross block. Consequently the nested compiler can have at most one pivot on this exact-rank-three family; its only compatible terminal case is precisely the one-pivot certificate already ruled out quantitatively by (4.8).

This is an exact incompatibility, not a criticism of the partner theorem: the partner theorem is useful for higher-rank target matrices, but its hypotheses cannot close this rank-three stress family.

## 6. Simultaneous obstruction to the pinned single-cut Theorem-D route

The preceding B18 report at

`math-open-problems@b0fe7c60d4fb400917fb53d2435d5262fdcfea97`

proved for every exact-rank-three Schur-isotropic matrix `A=UDU^T` with normalized spectral product one that any physical rank-three cross-volume cut satisfies

\[
Z=e_3(A_{IJ}^TA_{IJ})\le(1+r^2)^{-1}
\]

when the hub is on one side, and `Z<=(1+r^2)^{-2}` when the hub is absent. The pinned e5f Theorem D certificate is

\[
6\sqrt e\,Z^{-1/6}.
\]

Hence every **applicable** single-cut Theorem-D certificate on `A_{m,r}` is at least

\[
6\sqrt e\,(1+r^2)^{1/6}.
\tag{6.1}
\]

Take the diagonal sequence `r=m`. Then the family still has exact nonzero spectrum `{-1,1,1}` and enters every fixed N3 window as `m->infinity`, while

- every applicable single-cut Theorem-D certificate is at least `6 sqrt(e) (1+m^2)^{1/6}`, i.e. order `m^{1/3}`;
- every applicable one-pivot rank-two Schur certificate is at least `(8 2^{1/4}/sqrt3) sqrt(m)`, i.e. order `m^{1/2}`;
- two-or-more-pivot nested rank-two compilation is impossible by rank.

At the same time the actual positive-half-line density remains bounded by `pi sqrt(2)` from Section 2.

Thus this target-valid sequence simultaneously defeats the two most immediate nonplanar large-shear certificates while leaving half of the density problem already solved. It is a rigorous **proof-method stress family**, not a QFORM counterexample.

## 7. What this changes

The previous debt `QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1` cannot be discharged merely by replacing the failed single rank-three cut with a nonzero physical pivot followed by the newest partner rank-two compiler. The circular family proves that route has an unavoidable `sqrt(m)` certificate loss.

The exact surviving problem is narrower:

\[
Q_{m,m}=\frac{2}{\sqrt{1+m^2}}(Y_1+mX_0)Y_2+Y_3^2,
\qquad V^TV=I_3,
\]

with the circular rows above. Its positive half-line is uniformly controlled. A successful next mechanism must exploit the zero physical hub and the **aggregate** Pluecker identity before conditioning, or introduce a genuinely different product-preserving oscillatory argument for the negative/two-sheet side. It cannot rely only on

1. one exact planar bank (none exists at dimension-free mass),
2. one rank-three physical cross cut,
3. one nonzero physical Schur pivot followed by rank-two cross smoothing, or
4. two successive nonzero pivots ending in a rank-two block.

This is the first unpaid implication for the next B18 run.

## 8. Source/correction ledger

Consumed completed sources at equations:

- e5f `COUNTEREXAMPLE_SEARCH.md`, ruled one-sheet Theorem C: actual inequality `p(t)<=pi sqrt(2)` for this family on `t>=0`.
- e5f `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`, Theorem D: actual certificate obstruction (6.1), combined with the preceding B18 exact cross-volume factorization.
- designated partner fleet03/B18 `math-open-problems@dfbc17f17b702ed7c7191ba24648a70f67dda851`: rank-two half-Riesz Schur compiler (3.1), used in the new lower bound (4.8).
- newest designated partner `math-open-problems@2d03e0a0014e3aa8e3ecf95994501bde16093872`: nested compiler, shown exactly incompatible after one pivot because the stress family has rank three.

Primary external source checked at its theorem statement: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1. Its product-density hypotheses and `2^{k/2}` cap match the partner use; no rotation-independence inference is made.

Live corrections retained: no post-rotation independence; no arbitrary-joint coarea; bounded X-ray/joint density alone does not pay the two-sheet trace; conditional density caps do not substitute for independence; no generic exact planar-bank extraction; no generic single Schur rank-two extraction; continuity remains separate.

Full-problem status change: `OPEN -> OPEN`.
Independent end-to-end review: not performed in this slot.
Execution mode: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver was used).
