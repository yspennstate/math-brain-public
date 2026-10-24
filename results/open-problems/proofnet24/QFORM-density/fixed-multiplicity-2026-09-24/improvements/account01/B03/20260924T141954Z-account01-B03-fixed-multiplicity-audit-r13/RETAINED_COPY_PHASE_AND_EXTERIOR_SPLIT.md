# B03 improvement: retained copy-sum phase and exact exterior row splitting

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141954Z-account01-B03-fixed-multiplicity-audit-r13`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved new dependence-safe analytic/structural identities; no unconditional multiplicity reduction below 17 is claimed.**

The baseline proof deliberately throws away the phase of the quadratic polynomial on the bank where Cauchy–Schwarz is applied. At the critical order-four endpoint this loses potentially useful curvature. The first result below keeps that phase exactly while retaining the true dependence between the copy difference and copy sum. The second result shows that aggregate crossing volume can always be split between literal physical row packets without dimension loss, but that such a split cannot by itself increase the total Fourier order beyond four.

## 1. Exact retained-copy-phase identity

Let `I,J` be disjoint original-coordinate banks. Their coordinates are independent and have probability densities bounded by one. Let

\[
 Z=F(X_I)+2X_I^T M X_J+G(X_J),
\tag{1}
\]

where `G` is arbitrary measurable and finite almost surely, and now take the same-bank term to be the actual quadratic-affine polynomial

\[
 F(x)=x^T Bx+\ell^Tx+c,
 \qquad B=B^T.
\tag{2}
\]

For an independent copy `X'_I`, put coordinatewise

\[
 D=X_I-X'_I,\qquad S=X_I+X'_I.
\tag{3}
\]

For coordinate `i`, if its original density is `f_i`, the pair `(D_i,S_i)` has the joint density

\[
 h_i(d,s)=\frac12
 f_i\!\left(\frac{s+d}{2}\right)
 f_i\!\left(\frac{s-d}{2}\right).
\tag{4}
\]

The pairs `(D_i,S_i)` are independent across `i`, but **within each pair `D_i` and `S_i` are generally dependent**. Define the partial Fourier transform in the sum coordinate

\[
 H_i(d,\xi)=\int_{\mathbb R}e^{i\xi s}h_i(d,s)\,ds.
\tag{5}
\]

### Theorem 1 — retained phase after one copy

For every real `t`,

\[
\boxed{
 |\phi_Z(t)|^2\le R_t,
}
\tag{6}
\]

where `R_t` is the nonnegative real number

\[
\boxed{
 R_t=
 \int_{\mathbb R^{|I|}}
 e^{it\ell^Td}
 \prod_{i\in I}H_i\bigl(d_i,t(Bd)_i\bigr)
 \prod_{j\in J}\widehat f_j\bigl(2t(M^Td)_j\bigr)
 \,dd.
}
\tag{7}
\]

Although the integrand in (7) need not be pointwise nonnegative, its integral is nonnegative because it is exactly the Cauchy–Schwarz square on the right side of the proof below.

#### Proof

Write

\[
 \phi_Z(t)=
 \mathbb E_{X_J}
 e^{itG(X_J)}
 \mathbb E_{X_I}
 e^{itF(X_I)+2itX_I^TMX_J}.
\]

Cauchy–Schwarz in the **original product law of `X_J`** gives

\[
 |\phi_Z(t)|^2
 \le
 \mathbb E_{X_J}
 \left|\mathbb E_{X_I}
 e^{itF(X_I)+2itX_I^TMX_J}\right|^2.
\tag{8}
\]

Expand the square with one independent copy `X'_I`. Since `B` is symmetric,

\[
 F(X_I)-F(X'_I)=D^TBS+\ell^TD.
\tag{9}
\]

Integration over the independent `X_j`, `j in J`, produces

\[
 \prod_{j\in J}\widehat f_j\bigl(2t(M^TD)_j\bigr).
\]

Now change variables separately in every copied coordinate pair from `(X_i,X'_i)` to `(D_i,S_i)`. The Jacobian is `1/2`, giving exactly (4). Because the coordinate pairs are independent, integration in all sum variables factorizes and (5) yields (7). All original integrands have modulus one, so Fubini needs no moment or support assumption. This proves (6)–(7).

The theorem is the same independent-copy device as the baseline manuscript, but it does **not** discard the same-bank quadratic phase and it does not replace the true `(D_i,S_i)` law by a product of its marginals.

## 2. Exact ambiguity-energy bounds for one coordinate pair

Let

\[
 g_i(d)=\int h_i(d,s)\,ds
\tag{10}
\]

be the density of `D_i`. Then `g_i=f_i*\widetilde f_i` is a probability density with `0<=g_i<=1`. Moreover `0<=h_i<=1/2`. Plancherel in the `s` variable therefore gives, for almost every `d`,

\[
\boxed{
 \int_{\mathbb R}|H_i(d,\xi)|^2\,d\xi
 =2\pi\int h_i(d,s)^2\,ds
 \le \pi g_i(d).
}
\tag{11}
\]

After integrating in `d`,

\[
\boxed{
 \iint_{\mathbb R^2}|H_i(d,\xi)|^2\,dd\,d\xi\le\pi.
}
\tag{12}
\]

These are unconditional statements about the **joint** difference/sum law. No conditional density of `S_i` given `D_i` is bounded or even introduced.

A useful shifted-frequency consequence is the following. Let `U` be independent of the copied pair and have a density `p_U<=K_U`. For any measurable shift `a` independent of `U`, any `beta!=0`, and `t!=0`,

\[
\boxed{
 \int p_U(u)
 |H_i(d,t(a+\beta u))|^2\,du
 \le
 \frac{\pi K_U}{|t\beta|}\,g_i(d).
}
\tag{13}
\]

Indeed, discard `p_U` in favor of its cap and use the change of variables `xi=t(a+beta u)` followed by (11).

More generally, if `(Omega,nu)` is a probability space, `A(d,omega)` is independent of `U`,

\[
 a_2(d)=\left(\int|A(d,\omega)|^2d\nu(\omega)\right)^{1/2}
 \in L^2(dd),
\]

and `alpha(d,omega)` is arbitrary measurable, then

\[
\boxed{
 \left|
 \int dd\,d\nu(\omega)\,p_U(u)du\,
 A(d,\omega)
 H_i(d,t(\alpha(d,\omega)+\beta u))
 \right|
 \le
 \left(\frac{\pi K_U}{|t\beta|}\right)^{1/2}
 \|a_2\|_{L^2(dd)}.
}
\tag{14}
\]

For fixed `d`, apply Cauchy–Schwarz in `(omega,u)`, use (13), and then integrate `a_2(d)sqrt(g_i(d))` in `d`; the last integral is at most `||a_2||_2` because `int g_i=1`.

Equation (14) is a dependence-safe way to gain a half power of `|t|` **at the copied-square level** when another independent physical variable enters the retained sum-frequency. It is specifically designed to avoid the invalid shortcut “condition on the difference and recap the sum”.

## 3. A universal two-source pointwise consequence

The retained identity already gives a clean pointwise theorem whenever the physical same-bank Hessian has one literal off-diagonal coefficient.

Suppose `B_{ik}=B_{ki}=beta!=0` for two distinct original coordinates `i,k in I`. Then

\[
\boxed{
 |\phi_Z(t)|^2\le\min\left\{1,\frac{\pi}{|\beta t|}\right\},
 \qquad
 |\phi_Z(t)|\le
 \min\left\{1,\sqrt{\frac\pi{|\beta t|}}\right\}.
}
\tag{15}
\]

#### Proof

Take absolute values in (7), discard all Fourier factors from the `J` bank, and use `|H_l(d_l,xi)|<=g_l(d_l)` for `l notin {i,k}`. Fix all other differences. They only create additive shifts in the two frequencies. It remains to bound

\[
 I=\iint
 |H_i(d_i,t(B_{ii}d_i+\beta d_k+c_i))|
 |H_k(d_k,t(\beta d_i+B_{kk}d_k+c_k))|
 \,dd_i\,dd_k.
\]

Cauchy–Schwarz gives `I^2<=I_i I_k`. For `I_i`, fix `d_i` and change `d_k` to the first frequency. Since its derivative is `t beta`, (12) gives

\[
 I_i\le\frac\pi{|t\beta|}.
\]

The symmetric argument gives the same bound for `I_k`, hence `I<=pi/(|t beta|)`. The remaining difference densities integrate to one. This proves (15).

This does not contradict the known failure of a uniform one-variable rough quadratic-phase van-der-Corput bound: the gain here comes from two genuinely independent original sources linked by a bilinear coefficient.

The decay in (15) alone is not integrable and therefore does not lower the fixed-multiplicity theorem. Its value is that it identifies an exact same-bank resource which can, in principle, be combined *before* absolute values with the critical order-four crossing endpoint.

## 4. Exact dimension-free splitting of crossing volume between physical row packets

The previous B03 split-row determinant theorem shows how two disjoint physical row packets can contribute separate Fourier determinants while sharing the same difference environment. What aggregate crossing volume itself guarantees about such packets can be stated exactly.

Let `M` be an `m x n` real matrix and let `a,b>=0`, `a+b=k`. For a row partition `[m]=I_1 disjoint_union I_2`, define the mixed row volume

\[
 W_{a,b}(I_1,I_2)
 =\sum_{\substack{S_1\subset I_1, |S_1|=a\\
                    S_2\subset I_2, |S_2|=b}}
   \sum_{|T|=k}
   \det(M_{S_1\cup S_2,T})^2.
\tag{16}
\]

### Theorem 2 — exterior row split

For every fixed partition,

\[
\boxed{
 W_{a,b}(I_1,I_2)
 \le Z_a(M_{I_1,:})Z_b(M_{I_2,:}).
}
\tag{17}
\]

For a fair independent random row partition,

\[
\boxed{
 \mathbb E W_{a,b}
 =\binom{k}{a}2^{-k}Z_k(M).
}
\tag{18}
\]

Consequently some literal physical partition satisfies

\[
\boxed{
 Z_a(M_{I_1,:})Z_b(M_{I_2,:})
 \ge\binom{k}{a}2^{-k}Z_k(M).
}
\tag{19}
\]

#### Proof

For fixed disjoint row sets `S_1,S_2`, write the corresponding exterior row vectors as `u=\wedge_{i in S_1}r_i` and `v=\wedge_{i in S_2}r_i`. Cauchy–Binet gives

\[
 \sum_{|T|=k}\det(M_{S_1\cup S_2,T})^2
 =\|u\wedge v\|^2
 \le\|u\|^2\|v\|^2.
\]

A second use of Cauchy–Binet identifies `||u||^2` and `||v||^2` with the sums of squared `a`- and `b`-column minors of the two row packets. Summing in `S_1,S_2` proves (17).

For (18), each fixed `k`-row minor has exactly `binom(k,a)` assignments with `a` of its rows in the first packet and `b` in the second, among `2^k` equally likely assignments. Linearity of expectation proves (18), and (19) follows from (17) for a realization no smaller than the expectation.

For `k=4`, two useful specializations are

\[
\boxed{Z_2(M_{I_1,:})Z_2(M_{I_2,:})\ge\frac38 Z_4(M)}
\tag{20}
\]

for some partition, and

\[
\boxed{Z_1(M_{I_1,:})Z_3(M_{I_2,:})\ge\frac14 Z_4(M)}.
\tag{21}
\]

Thus there is no dimension-loss obstruction to splitting **the same total order four** across physical row packets.

## 5. Actual order-four application

Apply (20) to any cross form (1) with `Z_4(M)>0`, and then apply the completed B03 split-row shared-environment determinant theorem from the preceding run. Retaining the order-two term in each of the two packet determinants gives

\[
\boxed{
 |\phi_Z(t)|
 \le
 \min\left\{1,
 \frac{\pi e}{|t|}
 \left(\frac{8}{3Z_4(M)}\right)^{1/8}
 \right\}.
}
\tag{22}
\]

The two packet estimates use the **same** independent-copy difference vector; no independence between the packets is asserted.

Under the normalized no-pivot `s_13(A)>=1` structural conclusion of the baseline manuscript, there is a physical cut with `Z_4(M)^(-1/8)<=160`. Hence a further literal row split has

\[
 |\phi_Q(t)|
 \le
 \min\{1,1544.581/|t|\}.
\tag{23}
\]

The exact coefficient in (23) is

`160*pi*e*(8/3)^(1/8)=1544.5800772...`.

This remains the critical `1/|t|` endpoint. It is therefore an absolute-continuity/all-finite-`L^r` statement after Hausdorff–Young, not an `L^infinity` density theorem. The unsplit order-four envelope has a slightly better constant; the point of (22) is structural provenance, not constant optimization.

## 6. Why aggregate order four cannot by itself produce the `1+4` integrable split

The previous B03 run observed that a `1+4` packet would have total crossing order five and would immediately be integrable. Theorem 2 shows what can be extracted from `Z_4`, but it also makes the missing unit of order explicit.

Take `M=I_4` (or append any number of zero rows). Then `Z_4(M)=1`. Any row packet with positive `Z_4` must contain all four nonzero rows. Its disjoint complementary packet has `Z_1=0`. Thus there is **no** disjoint physical `1+4` row split with both factors positive, despite a perfectly nonzero order-four volume.

Consequently an unconditional `17 -> 13` proof cannot obtain the needed fifth unit of Fourier order from `Z_4` alone. It must spend an additional same-bank/exterior resource, leverage information, or a genuinely stronger endpoint theorem. The retained-copy-phase identity (7) records one such resource without violating the sum/difference dependence.

## 7. Precise next obligation

At multiplicity thirteen the structural argument already supplies an order-four crossing endpoint. Equations (7), (11)–(14) show how same-bank quadratic curvature can be kept at the **same copied-square stage** instead of being discarded. To turn this into a lower-threshold theorem one still needs a product-preserving structural statement that forces enough of that retained phase to interact with the order-four packet so that the squared characteristic function gains a genuine extra power beyond `|t|^-2` (equivalently `|phi(t)|=O(|t|^{-1-epsilon})`), or a direct linear small-ball argument of comparable strength.

Separate pointwise bounds such as (15) and (22) do not add their exponents; merely taking their minimum cannot remove the logarithmic endpoint. Any successful replacement proof must combine the resources before the final absolute-value/Hölder step.

Thus the unconditional bounded-density threshold remains **17** after this run. The new identities are intended as the next dependence-safe analytic interface; they require separate review before being used in a validated lower-threshold candidate.
