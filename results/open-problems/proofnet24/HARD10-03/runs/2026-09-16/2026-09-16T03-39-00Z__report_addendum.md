# HARD10-03 — random-cut sharpening and delivery addendum

This is an append-only sharpening of

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T03-35-45Z__report.md`.

The full `d=3` Tóth conjecture remains open.

## 1. NEW-L53A — sharper random-cut exponent

The main report used a Paley--Zygmund lower bound for the number of bichromatic edges of the selected spanning tree. For the fair block coloring there is a sharper exact observation.

Conditional on a permutation realization in the block-visitation event, let `T` be any spanning tree of the root-cycle block support and let

\[
Z=\#\{e\in T:e\text{ has differently colored endpoints}\}.
\]

As proved in the main report,

\[
Z\sim\operatorname{Bin}(k-1,1/2).
\]

By symmetry of the fair binomial law,

\[
\boxed{
\mathbb P_\xi\left(
Z\ge\left\lceil\frac{k-1}{2}\right\rceil
\right)\ge\frac12.
}
\tag{1.1}
\]

For every binary cut, the number of root-cycle arrows from red blocks to blue blocks equals the number in the reverse direction. Therefore if `Z` tree edges are bichromatic, the full permutation crossing count

\[
N_\xi=\#\{x\in R_\xi:P(x)\in D_\xi\}
\]

satisfies

\[
N_\xi\ge Z/2.
\]

Set

\[
s_k:=\left\lceil\frac{k-1}{4}\right\rceil.
\tag{1.2}
\]

Then, pathwise on the block-visitation event,

\[
\boxed{
1
\le
2\,\mathbb E_\xi
\mathbf1_{\{N_\xi\ge s_k\}}.
}
\tag{1.3}
\]

For a fixed cut, the strong-Rayleigh / negative-association Chernoff bound from the main report remains

\[
\mathbb P(N_\xi\ge s_k)
\le
\left(\frac{e\mu_\xi}{s_k}\right)^{s_k},
\qquad
\mu_\xi=
\sum_{x\in R_\xi,y\in D_\xi}p_\beta(x,y).
\tag{1.4}
\]

Define the directed maximum cut heat

\[
\Lambda_\beta(\mathcal B)
:=
\max_{I\subseteq\{1,\dots,k\}}
\sum_{i\in I,j\notin I}
\sum_{x\in B_i,y\in B_j}p_\beta(x,y).
\tag{1.5}
\]

Then `mu_xi<=Lambda_beta(B)` for every coloring. Hence:

### NEW-L53A — PROVED

\[
\boxed{
\mathbb P\bigl(\mathcal V(\mathcal B)\bigr)
\le
\min\left\{
1,
\frac{\mathcal H_\beta(\mathcal B)}{k},
2\left(
\frac{e\Lambda_\beta(\mathcal B)}{s_k}
\right)^{s_k}
\right\},
\qquad
s_k=\left\lceil\frac{k-1}{4}\right\rceil.
}
\tag{1.6}
\]

Because the ordinary one-particle kernel is symmetric,

\[
h_{ij}
:=
\sum_{x\in B_i,y\in B_j}p_\beta(x,y)
=h_{ji}.
\]

Thus every directed cut counts each separated unordered block pair once, whereas

\[
\mathcal H_\beta(\mathcal B)
=2\sum_{i<j}h_{ij}.
\]

Consequently

\[
\boxed{
\Lambda_\beta(\mathcal B)
\le\frac12\mathcal H_\beta(\mathcal B).
}
\tag{1.7}
\]

Combining (1.6)--(1.7), if

\[
\mathcal H_\beta(\mathcal B)
\le
\frac{k-1}{4e},
\tag{1.8}
\]

then

\[
\frac{e\Lambda_\beta}{s_k}
\le\frac12,
\]

and therefore

\[
\boxed{
\mathbb P\bigl(\mathcal V(\mathcal B)\bigr)
\le
2^{1-s_k}
\le
2^{1-(k-1)/4}.
}
\tag{1.9}
\]

This improves the exponent from roughly `k/8` to `k/4` and improves the sufficient cross-heat threshold by a constant factor. No new external theorem is used.

## 2. Conditional version

For an admissible no-peeking history `F`, define

\[
\Lambda^\mathscr F(\mathcal B)
=
\max_I
\sum_{i\in I,j\notin I}
\sum_{x\in B_i,y\in B_j}
K^\mathscr F_\beta(x,y).
\tag{2.1}
\]

The conditional kernel need not be symmetric, so one should retain `Lambda^F` rather than replace it by half of the total directed cross heat. The same proof gives

\[
\boxed{
\mathbb P(\mathcal V(\mathcal B)\mid\mathscr F)
\le
\min\left\{
1,
\frac{\mathcal H^\mathscr F(\mathcal B)}{k},
2\left(
\frac{e\Lambda^\mathscr F(\mathcal B)}{s_k}
\right)^{s_k}
\right\}.
}
\tag{2.2}
\]

A sufficient condition expressed only through total conditional cross heat is

\[
\mathcal H^\mathscr F(\mathcal B)
\le\frac{k-1}{8e},
\]

which implies the same `2^{1-s_k}` exponential bound because `Lambda^F<=H^F`.

## 3. Delivery receipt for the main checkpoint

Main report path:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T03-35-45Z__report.md`

Commit:

`2a0654395faf6dad819fdbf2fcbef9a2063d2d5f`

Exact-commit readback blob:

`ab5d652a3534fdcd2acb0f30fcc454198cc4044c`

Delivery status: **VERIFIED**.

No previous file is modified by this addendum.
