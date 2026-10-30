# QFORM B17 — irrational null-cone fragmentation is asymptotically suppressed

Run: `20260923T190352Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS-EXCLUSION; FULL QFORM OPEN**  
Continuity: not claimed beyond this explicit finite-rectangle family.

## 1. Result

Let

\[
A={1\over6}\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\]

As in the completed fleet01/fleet04 B17 work, `spec(A)={1,1,-1,0,0,0}`.  Write

\[
T x=\left({x_1+x_2\over\sqrt2},{x_3+x_4\over\sqrt2},{x_5+x_6\over\sqrt2}\right),
\qquad
B=I-{2\over3}{\bf1}{\bf1}^T,
\]
so that `A=T^T B T`, `TT^T=I_3`, and `B^2=I_3`.

Set

\[
z=4+3\sqrt2,
\qquad
y_*=(1,1,z),
\qquad
c=\left({1\over\sqrt2},{1\over\sqrt2},{1\over\sqrt2},{1\over\sqrt2},{z\over\sqrt2},{z\over\sqrt2}\right).
\]
Then

\[
y_*^T B y_*=0,
\]
so the **full remote cell is centered exactly on the real null cone**, at the irrational direction `R c`.

For arbitrary `0<eta<1` and `R>=12`, give every physical coordinate the cap-one density

\[
f_{i,R}(x)=
\mathbf1_{[-(1-\eta)/2,(1-\eta)/2]}(x)
+\mathbf1_{[Rc_i-\eta/2,Rc_i+\eta/2]}(x).
\]
The two intervals are disjoint for the values of `R` used below, have total length one, and hence define probability densities bounded by one.

Let `Q_R=X^TAX`.  If `p_*` denotes the exact centered-unit-cube cone-tip value

\[
p_*=4.06307061680603726012548\ldots,
\]
then

\[
\boxed{
(1-\eta)^4p_*
\le p_{Q_R}(0)
\le (1-\eta)^4p_*+{252\sqrt6\over R}.
}
\tag{1.1}
\]

Consequently, uniformly in the fragment mass `eta`,

\[
\boxed{
\limsup_{R\to\infty}\sup_{0<\eta<1}p_{Q_R}(0)\le p_*<3\sqrt2.
}
\tag{1.2}
\]

In particular, using the certified source bound `p_*<4.064=508/125`, together with `sqrt(6)<5/2` and `sqrt(2)>140/99`, for every

\[
\boxed{R\ge3600}
\]
we have the entirely rationally certified separation

\[
p_{Q_R}(0)
< {508\over125}+{630\over3600}
={4239\over1000}
<{140\over33}
<3\sqrt2.
\tag{1.3}
\]

Thus **even exact irrational null-cone alignment of the remote cell cannot create an O(1) cone-tip enhancement** in this dense six-variable architecture.  A fixed finite remote cell centered at distance `R` contributes only `O(R^{-1})` unless its leading center lies in the kernel of `A`.

## 2. Partner result applied to an actual inequality

The designated partner `fleet04/B17` proved the fragmented-main-cell theorem at

`yspennstate/math-open-problems@8c57f6e8fd6fe7ea16e6acbe7f199be22f1daf58`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260923T171805Z-fleet04-B17-QFORM-r5/REPORT.md`.

Its homogeneous scaling calculation applies verbatim to the present central component, regardless of where the remote intervals are placed.  Therefore the all-central rectangle contributes exactly

\[
(1-\eta)^4p_*,
\]
which gives the lower inequality in (1.1).  The new work below supplies the matching upper control on all 63 other cells, including the deliberately null-aligned irrational one.

The exact value `p_*` and its certified interval evaluation come from

`yspennstate/math-open-problems@e83d0cc194d791acf31d6c86245204887cfd8171`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260923T144233Z-fleet01-B17-QFORM-auto11/REPORT.md`.

## 3. Exact null alignment

Because

\[
q(y)=y^TBy=|y|^2-{2\over3}(y_1+y_2+y_3)^2,
\]
for `y=(1,1,z)` the null equation is

\[
2+z^2-{2\over3}(2+z)^2=0
\iff z^2-8z-2=0.
\]
The positive root is `z=4+3sqrt(2)`, proving `q(y_*)=0` exactly.  Since `Tc=y_*`,

\[
(Rc)^TA(Rc)=R^2 y_*^TBy_*=0.
\]

Thus the construction targets precisely the loophole left by rational-center separation: a nonzero remote center lies exactly on the real cone.

## 4. Cell decomposition and the O(1/R) lemma

Expand the six-fold product density into its 64 rectangular cells.  Index a cell by a subset `S` of coordinates chosen from the remote intervals.  Its center is

\[
x_S=R c^S,
\]
where `c^S_i=c_i` for `i in S` and zero otherwise.  The all-central cell is `S=emptyset`.

For every nonempty `S`, each coordinate of `Tc^S` is one of

\[
0,\quad {1\over2},\quad1
\]
for the first two banks, and one of

\[
0,\quad {z\over2},\quad z
\]
for the third bank.  All entries are nonnegative and at least one is positive.  Hence

\[
\boxed{|Tc^S|\ge {1\over2}\qquad(S\ne\varnothing).}
\tag{4.1}
\]

Since `A=T^TBT`, `TT^T=I`, and `B` is orthogonal,

\[
|Ac^S|=|BTc^S|=|Tc^S|.
\tag{4.2}
\]
Choose an index `j=j(S)` with

\[
|(Ac^S)_j|\ge {|Tc^S|\over\sqrt6}.
\]
Every point of the cell can be written `x=x_S+u`, where every side length is at most one, hence

\[
|u|\le {\sqrt6\over2}.
\]
Because `||A||_op=1`,

\[
|(Au)_j|\le {\sqrt6\over2}.
\]
If `R|Tc^S|>=6`, which follows from `R>=12` and (4.1), then throughout the entire cell

\[
|(Ax)_j|
\ge {R|Tc^S|\over\sqrt6}-{\sqrt6\over2}
\ge {R|Tc^S|\over2\sqrt6}.
\]
Therefore

\[
\left|{\partial\over\partial x_j}(x^TAx)\right|
=2|(Ax)_j|
\ge {R|Tc^S|\over\sqrt6}.
\tag{4.3}
\]

Fix the other five coordinates.  As a function of `x_j`, `x^TAx` is a polynomial of degree at most two.  Thus it has at most two zeroes in the interval, and the one-dimensional delta identity plus (4.3) gives

\[
\int_{I_j}\delta(x^TAx)\,dx_j
\le {2\sqrt6\over R|Tc^S|}.
\]
The product of the other five side lengths is at most one.  Hence the entire cell contributes at most

\[
{2\sqrt6\over R|Tc^S|}
\le {4\sqrt6\over R}.
\tag{4.4}
\]

There are 63 noncentral cells, so their total contribution is at most

\[
{252\sqrt6\over R}.
\]
Together with the exact central-cell contribution this proves (1.1).

Notice that the proof does **not** require `q(Tc^S)` to be bounded away from zero.  It therefore covers cells whose leading center lies exactly on the cone.  The only dangerous case for this argument is `Tc^S=0`, equivalently `Ac^S=0`, i.e. a leading **kernel cancellation** rather than a nonzero cone alignment.  The present positive-center choice excludes such cancellations automatically.

## 5. General finite-cell suppression principle

The same argument yields the following reusable statement for this exact matrix.  Let finitely many rectangular product cells have centers `R d_alpha` and uniformly bounded side lengths.  If

\[
m=\min_{\alpha:\,Td_\alpha\ne0}|Td_\alpha|>0,
\]
then every non-kernel cell contributes at most

\[
{2\sqrt6\over Rm}
\]
up to the product of its other five side lengths, once `Rm>=6`.  Thus any fixed finite collection of non-kernel remote cells has total cone-tip contribution `O(R^{-1})`, **even when any number of their spectral centers lie exactly on the indefinite null cone**.

This isolates the genuinely unpaid remote-fragment mechanism: to retain an O(1) contribution at arbitrarily large separation one needs leading kernel cancellations, a number of fragments growing with the separation scale, or a different off-zero alignment.  A single irrational null ray is not enough.

## 6. Correction compatibility and scope

This proof stays in the original independent physical coordinates and uses only an exact finite rectangle decomposition and one-coordinate coarea on cells with a derivative bounded away from zero.  It uses none of the refuted law-uniform pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea bounds, positive conditional-density moments, bounded-fragment extremality, or Monte Carlo histogram reasoning.

The theorem is cone-tip-only and architecture-specific.  It does not rule out off-zero peaks, kernel-cancelling fragment patterns, a number of fragments growing with `R`, arbitrary extra spectrum, or the full target.  Therefore the unrestricted QFORM conjecture and full-target continuity remain **OPEN / NOT PROVED**.
