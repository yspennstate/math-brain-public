# QFORM-PACKETWISE-HOLDER-BL-v1

Run: `20260924T144124Z-account01-B04-fixedmult-audit-r12`

Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`

This is a supporting theorem for the fixed-multiplicity program. It does not by itself lower the unconditional 17-eigenvalue threshold.

## 1. Setup

Let

\[
Z=F(X_I)+2X_I^T M X_J+G(X_J),
\]

where the coordinates in the disjoint physical banks `I,J` are independent and have densities bounded by one. No assumptions are made on the measurable same-bank terms `F,G` beyond being finite almost surely.

Partition the row bank into disjoint packets

\[
I=I_1\sqcup\cdots\sqcup I_s,
\]

and write `M_g=M[I_g,J]`. For each nonzero packet let

\[
h_g=\max_{i\in I_g}m_i^T(M_g^TM_g)^\dagger m_i
\]

be its maximum physical row leverage. Always `0<h_g<=1`.

Choose finite Hölder exponents `q_g>=1` satisfying

\[
\sum_g q_g^{-1}=1,
\qquad h_g\le q_g/2.
\]

Packets with `q_g=+infinity` may be included by the evident limiting convention and contribute no determinant factor.

## 2. Packetwise determinant theorem

**Theorem.** Under the setup above,

\[
\boxed{
|\phi_Z(t)|
\le
\prod_g
\det\!\left(
I+\frac{q_g t^2}{2\pi^2e^2}M_g^TM_g
\right)^{-1/(4q_g)}.
}
\]

### Proof

The manuscript's first decoupling inequality gives, with `D=X_J-X'_J`,

\[
|\phi_Z(t)|^2
\le
\mathbb E_D\prod_g A_g(D),
\qquad
A_g(D)=\prod_{i\in I_g}|\widehat f_i(2t(MD)_i)|.
\]

Hölder in the single product probability space of `D` yields

\[
|\phi_Z(t)|^2
\le
\prod_g\left(\mathbb E_D A_g(D)^{q_g}\right)^{1/q_g}.
\]

Fix a packet `g`, abbreviate `q=q_g`, `M=M_g`, and set

\[
a=2t,
\qquad
\alpha=(2\pi e)^2\frac{2}{q},
\qquad
H=\alpha I+a^2M^TM.
\]

As in the manuscript's regularized graph-BL proof, define

\[
c_j=\alpha e_j^TH^{-1}e_j,
\qquad
d_i=a^2m_i^TH^{-1}m_i.
\]

The regularized frame identity is unchanged. Moreover

\[
d_i\le m_i^T(M^TM)^\dagger m_i\le h_g\le q/2.
\]

Apply geometric BL to the coordinate densities of `D` and to

\[
h_i(u)=|\widehat f_i(u)|^q.
\]

The required one-dimensional norm is

\[
\|h_i\|_{1/d_i}
=
\left(\int|\widehat f_i(u)|^{q/d_i}\,du\right)^{d_i}.
\]

Since `q/d_i>=2`, the manuscript's integrated scalar Fourier-power lemma gives

\[
\|h_i\|_{1/d_i}
\le
\left(2\pi\sqrt{\frac{2e d_i}{q}}\right)^{d_i}.
\]

The BL Jacobian contributes `d_i^{-d_i/2}`, so the powers of `d_i` cancel. The coordinate side gives

\[
\prod_j c_j^{-c_j/2}\le e^{\theta/2},
\qquad
\theta=\sum_i d_i=\sum_j(1-c_j).
\]

Thus the row Fourier factors and coordinate entropy factor contribute

\[
\left(2\pi e\sqrt{\frac2q}\right)^\theta
=\alpha^{\theta/2},
\]

which cancels the regularizer exactly. Therefore

\[
\mathbb E_D A_g(D)^q
\le
\det\!\left(
I+\frac{q t^2}{2\pi^2e^2}M_g^TM_g
\right)^{-1/2}.
\]

Insert this into Hölder and take the square root. This proves the theorem. No rotated coordinates are declared independent; all independence remains on the original product coordinates.

## 3. Volume consequence

For each packet choose an integer `k_g>=1` with

\[
Z_{k_g}(M_g)=e_{k_g}(M_g^TM_g)>0.
\]

Define

\[
P=\sum_g\frac{k_g}{2q_g}.
\]

From

\[
\det(I+c t^2M_g^TM_g)
\ge
c^{k_g}|t|^{2k_g}Z_{k_g}(M_g)
\]

we obtain

\[
|\phi_Z(t)|\le\min\{1,(a/|t|)^P\},
\]

where

\[
\boxed{
a^P=
\prod_g
\left(\pi e\sqrt{\frac2{q_g}}\right)^{k_g/(2q_g)}
Z_{k_g}(M_g)^{-1/(4q_g)}.
}
\]

If `P>1`, Fourier inversion is absolutely integrable and gives a continuous density with

\[
\boxed{
\|p_Z\|_\infty
\le
\frac{aP}{\pi(P-1)}.
}
\]

Indeed

\[
\frac1{2\pi}\int_\mathbb R\min\{1,(a/|t|)^P\}\,dt
=
\frac{aP}{\pi(P-1)}.
\]

## 4. Explicit `1+3` packet splice

Let the row bank be split into two packets with

\[
Z_1(M_1)>0,
\qquad
Z_3(M_2)>0.
\]

Choose `1<q<2`,

\[
q_2=q,
\qquad
q_1=\frac{q}{q-1}.
\]

The first packet automatically passes the leverage gate because `q_1>2`. The second packet requires only

\[
h_2\le q/2<1.
\]

Then

\[
P=\frac{1}{2q_1}+\frac{3}{2q}
=\frac{q+2}{2q}>1.
\]

The preceding formula simplifies exactly to

\[
\boxed{
\|p_Z\|_\infty
\le
e\frac{q+2}{2-q}
\left[
\frac{
(2(q-1)/q)^{q-1}(2/q)^3
}{
Z_1(M_1)^{q-1}Z_3(M_2)
}
\right]^{1/[2(q+2)]}.
}
\]

The density is continuous. The limiting case `q=1` ignores packet 1 and recovers

\[
\|p_Z\|_\infty
\le3\sqrt2\,e\,Z_3(M_2)^{-1/6}
\]

under the familiar half-leverage gate `h_2<=1/2`.

The new content is the whole interval `1/2<h_2<1`: choose any

\[
q\in[2h_2,2).
\]

Thus an order-three packet need only have leverage strictly below one if a complementary order-one packet is retained in the Hölder budget.

## 5. Exact order-four packet-split lemma

**Lemma.** For every real matrix `M`, there is a physical row partition `I=I_1 sqcup I_2` such that

\[
\boxed{
Z_1(M_1)Z_3(M_2)\ge\frac{27}{64}Z_4(M).
}
\]

### Proof

Write the physical rows as `m_i` and put `a_i=||m_i||_2^2`. For a four-row set `U`, let `G_U` be its Gram matrix. If `G_U` is positive definite, then for each `i in U`,

\[
a_i\det G_{U\setminus\{i\}}
=
det(G_U)\, (G_U)_{ii}(G_U^{-1})_{ii}
\ge\det(G_U),
\]

because the Schur complement identity gives
`(G_U)_{ii}(G_U^{-1})_{ii}>=1`. The same inequality follows by continuity when `G_U` is singular. Hence

\[
\sum_i a_i Z_3(M_{[m]\setminus\{i\}})
=
\sum_{|U|=4}\sum_{i\in U}
a_i\det G_{U\setminus\{i\}}
\ge4Z_4(M).
\]

Now independently put each physical row into `I_1` with probability `p` and into `I_2` otherwise. Expanding the two elementary symmetric volumes gives

\[
\mathbb E[Z_1(M_1)Z_3(M_2)]
=
p(1-p)^3
\sum_i a_iZ_3(M_{[m]\setminus\{i\}})
\ge4p(1-p)^3Z_4(M).
\]

The right side is maximized at `p=1/4`, where `4p(1-p)^3=27/64`. Therefore at least one deterministic physical partition satisfies the claim.

## 6. Consequence for the `s_13` no-pivot chamber and exact remaining obstruction

The audited manuscript's no-pivot spectral-to-volume proposition with `k=4`, followed by its random coordinate cut lemma, gives under

\[
s_{13}(A)\ge1
\]

and no `eta`-pivot a physical crossing `M` with

\[
Z_4(M)\ge4^{-4}\kappa^4,
\qquad
Z_4(M)^{-1/8}\le160.
\]

The order-four split lemma then produces `M_1,M_2` with

\[
Z_1(M_1)Z_3(M_2)\ge\frac{27}{64}Z_4(M).
\]

If this split also has a dimension-free leverage gap

\[
h_2\le1-\delta
\]

then taking, for example, `q=2-\delta` enters the Fourier-integrable packet theorem. More generally, if `T=Z_1(M)` then

\[
Z_1(M_1)^{q-1}Z_3(M_2)
\ge
\frac{27}{64}Z_4(M)\,T^{-(2-q)},
\]

because `Z_1(M_1)<=T`. This gives an explicit conditional `s_13` density bound.

What is **not proved** is a universal bound independent of `T` and a universal leverage gap for a volume-good split. Therefore this result does not establish the 13-eigenvalue theorem. It converts the order-four endpoint obstruction into the sharper structural problem:

> either find a volume-good `1+3` physical split whose rank-three packet is quantitatively non-coloop (`h_2<=1-delta`) with controlled weighted currency `Z_1^{q-1}Z_3`, or route the near-coloop alternative into an already controlled pivot/random-slope/grouped receiver.

This is the precise remaining debt from this mechanism. The unconditional multiplicity threshold remains 17.
