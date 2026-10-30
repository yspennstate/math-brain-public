# B15 — exact common-potential feasibility for the G10 AND/OR stopping corridor

**Outcome:** `ESSENTIAL_STEP_APPLIED` for the explicit G10 terminal-atom subtraction problem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were read directly; no authenticated cognitive-brain retrieval/context entered the mathematics.

## 1. Exact source-bound inputs consumed

This run consumes two completed other-account results rather than only citing their labels.

1. `fleet04/B12/20260922T0254Z-and-atom-stopping/REPORT.md`, blob `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`. For the exact balanced ten-input composition-prime gate `G10`, under the fixed physical reveal order it proves first stopping at affine or two-essential-input AND/OR atoms with

\[
\Pr(\text{AND/OR terminal})=\frac{29}{64},\qquad
\Pr(\text{affine terminal})=\frac{35}{64},
\]

and every nonaffine terminal has output bias `1/4` or `3/4`, `I=1`, `H=2`. Hence

\[
\mathbb E P(G_\sigma)=\frac{29}{1024},\qquad
\mathbb E H(G_\sigma)=\frac{29}{32},
\]

while the root has

\[
I(G_{10})=\frac{257}{128},\qquad
P(G_{10})=\frac{129}{512}.
\]

2. `fleet02/B12/20260922T025438Z-gate-margin-falsification/REPORT.md`, blob `bf37b4fd5ceae2c40e2b59266e2701fed8ff2780`. It applies the all-gate reformulation to the same source witness and proves that for a balanced gate at uniform bias the scalar center obstruction is exactly

\[
R(G):=\frac{H(G)}{I(G)-1}.
\]

For `G10`, the source-exact entropy enclosure is

\[
6.509836127588151479
< H(G_{10}) <
6.509836127588151480,
\]

so

\[
6.4593722816378557311\ldots
< R(G_{10}) <
6.4593722816378557321\ldots .
\]

The old read-once potential / AND-extremality candidate is therefore already refuted. The remaining local question isolated by fleet04/B12 was the **common-potential terminal-atom subtraction problem**: once one retains the terminal AND/OR continuation exactly, is the preterminal G10 corridor itself compatible with one scalar potential `Gamma`?

## 2. Set-up

Let `Gamma` be any symmetric candidate potential with endpoint normalization

\[
\Gamma(0)=\Gamma(1)=0,
\]

and write

\[
C:=\Gamma(1/2),\qquad g:=\Gamma(1/4)=\Gamma(3/4).
\]

At uniform input bias the all-gate slack is

\[
D_G^\Gamma
=I(G)C-\Gamma(p_{\rm out})-H(G).
\]

For the balanced root `G10`,

\[
\boxed{
D_{10}^\Gamma
=\frac{129}{128}C-H_{10}.
}
\tag{2.1}
\]

For every nonaffine terminal AND/OR atom in the stopping theorem, `I=1`, `H=2`, and `p_out in {1/4,3/4}`, hence

\[
\boxed{
D_{\rm AND}^\Gamma=C-g-2.
}
\tag{2.2}
\]

Affine terminals have zero slack under the endpoint normalization above.

Define the **preterminal stopped-block slack** by retaining the terminal continuation rather than charging it twice:

\[
D_{\rm block}^\Gamma
:=D_{10}^\Gamma-\mathbb E D_{G_\sigma}^\Gamma.
\]

Using the exact stopping weights,

\[
\boxed{
D_{\rm block}^\Gamma
=\frac{71}{128}C+\frac{29}{64}g
-\left(H_{10}-\frac{29}{32}\right).
}
\tag{2.3}
\]

This is the requested signed continuation calculation. The negative entropy term is the exact terminal refund

\[
\boxed{-\,\mathbb E H(G_\sigma)=-\frac{29}{32}.}
\]

In raw `Gamma=0` units it reduces the root entropy/Poincare ratio from about

\[
25.83748912655
\]

to the certified preterminal ratio

\[
25.05708381943348\ldots,
\]

removing exactly the apparent local ratio-32 terminal spikes identified by fleet04/B12.

## 3. Exact terminal-atom feasibility theorem

The two simultaneous local requirements are:

- the retained terminal AND/OR atoms satisfy `(G)`, i.e.

\[
D_{\rm AND}^\Gamma\ge0
\quad\Longleftrightarrow\quad
\boxed{g\le C-2};
\tag{3.1}
\]

- the preterminal block itself is nonnegative after subtracting that continuation, i.e.

\[
D_{\rm block}^\Gamma\ge0
\quad\Longleftrightarrow\quad
\boxed{
g\ge T(C)},
\tag{3.2}
\]

where

\[
\boxed{
T(C):=\frac{64}{29}
\left(
H_{10}-\frac{29}{32}-\frac{71}{128}C
\right).
}
\tag{3.3}
\]

Thus the entire common-potential compatibility problem for this stopped corridor is exactly the one-dimensional interval

\[
\boxed{T(C)\le g\le C-2.}
\tag{3.4}
\]

The width of this interval simplifies *exactly*:

\[
\begin{aligned}
(C-2)-T(C)
&=\frac{129}{58}C-\frac{64}{29}H_{10}\\
&=\boxed{
\frac{129}{58}\left(C-R(G_{10})\right)
}.
\end{aligned}
\tag{3.5}
\]

Therefore:

### Theorem 3.1

For the exact G10 fixed-order AND/OR stopping corridor, there exists a value of `Gamma(1/4)` that simultaneously certifies every terminal AND/OR atom and the signed preterminal block **if and only if**

\[
\boxed{C\ge R(G_{10}).}
\tag{3.6}
\]

At the threshold `C=R(G10)` the interval collapses to the unique value

\[
\boxed{g=C-2},
\tag{3.7}
\]

so the root, the terminal AND/OR atoms, and the stopped block are all exactly tight in the aggregate. For every larger center there is genuine room in the quarter-bias value.

**Proof.** Equations (3.1)--(3.4) show feasibility iff `T(C)<=C-2`. Equation (3.5) shows that this is equivalent to `C>=R(G10)`. No additional inequality is used. QED.

## 4. Quantitative consequence at the current lower-floor scale

A newer shared-graft/spine lower-bound source already forces any universal FEI center above `6.52`, far above `R(G10)`. For illustration, at

\[
C=6.521851119081174140\ldots
\]

and using the rigorous G10 entropy enclosure above, (3.3)--(3.4) give approximately

\[
4.38288956683655\ldots
\lesssim g\le
4.52185111908117\ldots,
\]

with interval width at least

\[
0.13896155224462\ldots .
\]

So the explicit G10 unbalanced stopping corridor contributes **no extra center obstruction beyond its already-known balanced ratio**. Its apparent high local losses are exactly compatible with the terminal entropy/AND continuation once the center exceeds the balanced root threshold.

This does **not** construct a universal `Gamma`: other biases and other gates can impose incompatible conditions on `Gamma(1/4)` or on the rest of its shape. It closes only this exact source-bound corridor.

## 5. What the negative term accomplishes, and what remains

Old missing implication from fleet04/B12:

> Recompute the G10 preterminal block under one common `Gamma` certifying every terminal AND/OR atom, retaining the terminal continuation exactly.

New proved inference:

> The stopped block and all its terminal AND/OR atoms are simultaneously feasible exactly when `Gamma(1/2)>=R(G10)`, with the complete allowable quarter-bias interval given by (3.4). No hidden dimension-dependent payment remains in this corridor.

This is a genuine use of the negative entropy continuation term: the `-29/32` refund is not dropped, and the terminal `Gamma(1/4)` contribution is kept with its exact sign. Requiring the preterminal block to pay the terminal atoms again would recover the false large local ratios.

The first essential remaining implication is now global rather than G10-specific:

> find one symmetric nonnegative finite-center `Gamma` whose value constraints induced by **all** composition-prime gates and all product biases have a nonempty intersection, or produce a finite incompatible collection of genuine Boolean gate constraints.

The current result says G10 plus its exact terminal AND/OR corridor does not itself create such an incompatibility once the center reaches its balanced ratio.

**Classification:** `ESSENTIAL_STEP_APPLIED` at the explicit G10 common-potential subtraction step; `FULL FEI OPEN`.
