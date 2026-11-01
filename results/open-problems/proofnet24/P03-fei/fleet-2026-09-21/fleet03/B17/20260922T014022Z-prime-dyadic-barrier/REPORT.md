# fleet03/B17 — a prime FEI gate whose entire dyadic physical-descendant spine is safe

**Outcome:** `AUXILIARY_ONLY / REPAIR_CLASS_REFUTED`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source-exact mathematical artifacts were consumed directly; no authenticated native brain retrieval or receiver-context result entered the mathematics.

## 0. Version/change summary and exact live obligation

The later owner control revision `2026-09-22.2` supersedes the older interface-A adversary wording and converges the FEI fleet on the all-gate inequality. The original read-once potential at center cap

\[
C_0=\Gamma_{RO}(1/2)=6.4548
\]

is already refuted as a universal potential by the balanced Numaro-derived gates. Therefore this run does **not** repeat the already-settled AND-extremality falsification.

The current source-valid replacement I bind to is the **PRIME-GATE-LIFT** obligation from

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`:
for the quadratic lift

\[
\Gamma_a(p)=\Gamma_{RO}(p)+a p(1-p),
\]

prove the gate inequality for every composition-prime Boolean gate and every interior product bias, with a finite dimension-independent `a` (the currently forced lower lift is about `0.2682003346`). That statement remains **OPEN** and is **not refuted here**.

The old missing implication is therefore no longer "AND is extremal." It is:

> control the normalized gate margin on genuinely composition-prime gates without assuming that a bad prime gate exposes a bad smaller physical descendant.

This run attacks precisely that possible restriction repair on the explicit source-bound arity-10 prime falsifier.

## 1. Named peer results consumed and actually applied

### 1.1 fleet02/B16: exact restriction-margin martingale

I consume

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`.

For a base potential `Gamma_0`, let

\[
D_0(G)=\text{gate slack},\qquad
P(G)=I(G)/4-p_{out}(1-p_{out}),\qquad
c_G=-D_0(G)/P(G).
\]

For an adaptive physical restriction path with local Poincare currency `Q_r` and local restriction margin `c_r`, stopped at `sigma`, that peer proves the exact signed identity

\[
P(G)c_G
=\mathbb E\left[\sum_{r<\sigma}Q_r c_r+P(G_\sigma)c_{G_\sigma}\right].
\tag{1.1}
\]

No positive-part estimate is used. I apply (1.1) below to the explicit ten-input witness after determining the sign of **every** proper dyadic-output continuation.

### 1.2 fleet02/B16 and fleet04/B14: the ten-input witness is already prime and balanced descendants are safe

I also consume the completed source-bound arity-10 primality theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T011313Z-arity10-composition-prime/REPORT.md`,

which proves that the ten-input gate reconstructed from fleet03/B12 is composition-prime. Thus primality is an inherited input here, not a novelty claim of this run.

The witness has truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

is balanced and monotone,

\[
I(G)=\frac{257}{128},
\qquad
6.509836127588151479<H(G)<6.509836127588151480,
\]

and therefore at uniform bias

\[
\boxed{c_G>0.018289126551422926.}
\tag{1.2}
\]

I further consume fleet04/B14's exact theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260922T012003Z-gate-witness-balance-primitive/REPORT.md`,

which proves that every proper **balanced** physical restriction of this gate with positive Poincare denominator has strictly negative old-base margin. The new work below extends that conclusion from the balanced slice to the full exact **dyadic output spine**, including asymmetric output masses `1/4,3/4,1/8,7/8,...`.

## 2. Exact dyadic-spine theorem

For a proper coordinate restriction `g` of the ten-input witness, feed every remaining free input uniformly and write

\[
q=\Pr[g=-1],\qquad r=\min(q,1-q).
\]

Call the restriction **dyadic-spine** when

\[
r=2^{-k}
\]

for an integer `k>=1` and when its Poincare denominator is positive:

\[
P(g)=\frac{I(g)-V_q}{4}>0.
\]

### Theorem 2.1 — every proper dyadic-spine descendant is paid by the old read-once potential

For every proper dyadic-spine restriction `g` of the explicit ten-input prime gate,

\[
\boxed{D_{RO}(g)\ge0,\qquad c_g\le0.}
\tag{2.1}
\]

Moreover equality in (2.1) occurs **if and only if** the rarer output-sign set is a literal coordinate subcube of codimension `k`; equivalently the essential part of `g` is an AND/OR chain, with arbitrary dummy coordinates. Every non-chain dyadic descendant obeys the strict certified gap

\[
\boxed{D_{RO}(g)>\frac1{30}.}
\tag{2.2}
\]

### Proof/certificate reduction

The read-once fixed point is exact on the dyadic AND chain. If `A_k` is the `k`-input AND gate, then at uniform bias

\[
\Gamma_{RO}(2^{-k})=C_0 I(A_k)-H(A_k),
\qquad
I(A_k)=\frac{k}{2^{k-1}}.
\tag{2.3}
\]

By symmetry the same value applies at `1-2^{-k}`. Hence for any dyadic-spine descendant

\[
D_{RO}(g)
=C_0\bigl(I(g)-I(A_k)\bigr)+H(A_k)-H(g).
\tag{2.4}
\]

The checker reconstructs the source-exact witness, enumerates all `3^10-1=59048` proper physical restrictions, retains exactly those satisfying the dyadic-output and positive-denominator hypotheses, and evaluates (2.4) with exact rational Walsh data plus rational atanh-series logarithm enclosures. No floating-point inequality decides (2.1) or (2.2).

There are exactly

\[
\boxed{13648}
\]

positive-denominator dyadic-spine restrictions, collapsing to only 51 exact `(arity,output-count,I,Walsh-magnitude-histogram)` signatures. Their complete classification is

\[
\begin{array}{c|r|r}
k&\text{strict }D_{RO}>0&\text{equality }D_{RO}=0\\\hline
1&460&0\\
2&264&9888\\
3&0&2928\\
4&0&102\\
5&0&6.
\end{array}
\tag{2.5}
\]

Every equality case passes an exact rare-sign-subcube test of codimension `k`; conversely those literal AND/OR descendants have equality by (2.3). The minimum certified strict defect is larger than `1/30`.

Thus the positive root obstruction (1.2) is not inherited by **any** proper balanced or asymmetric dyadic-output physical descendant.

## 3. Independent structural sanity check

Although composition-primality is already a consumed peer theorem, the checker independently reproduces it before applying the restriction classification. If a proper block `B` of at least two variables could be summarized by one Boolean inner gate in a nontrivial disjoint composition, then as the assignment on `B` varies the complete outside cofactor row can assume at most two values.

For the ten-input witness, the minimum number of distinct row states over all blocks of each size is

\[
\boxed{
|B|=2,3,4,5,6,7,8,9:\quad 3,5,8,9,7,6,4,3.
}
\tag{3.1}
\]

Hence no such block exists, matching the inherited fleet02/B16 primality theorem.

## 4. Applied consequence of the peer restriction martingale

Now apply the exact stopping identity (1.1), rather than merely citing it.

Consider **any** adaptive physical-restriction policy on this ten-input witness whose stopping descendants satisfy one of the following:

1. `P(G_sigma)=0` (affine/terminal), or
2. `G_sigma` is a proper dyadic-spine descendant.

Theorem 2.1 gives `c_{G_sigma}<=0` whenever the continuation currency is positive. Therefore (1.1) yields

\[
Q_\sigma c_\sigma
:=\mathbb E\sum_{r<\sigma}Q_r c_r
\ge P(G)c_G,
\tag{4.1}
\]

where

\[
Q_\sigma=\mathbb E\sum_{r<\sigma}Q_r\le P(G).
\]

Consequently every such stopped block policy satisfies

\[
\boxed{c_\sigma\ge c_G>0.018289126551422926.}
\tag{4.2}
\]

In particular, **no adaptive restriction proof that stops only on the exact balanced/dyadic AND-chain spine can repair the old read-once potential at its certified quadratic payment `c=0.01`**. The root defect cannot be exported to bad dyadic children, because there are none; the signed restriction increments before stopping must carry it themselves.

Numerically only for scale, not as a proof primitive,

\[
P(G)=\frac{I(G)-1}{4}=\frac{129}{512},
\]

so (1.2) forces more than `0.004608` units of signed `P*c` defect into those pre-stopping increments.

This is the promised actual application of a completed other-account theorem to the adversarial construction.

## 5. What is refuted, what survives, and the replacement obligation

### REFUTED repair class

The following stronger repair of the failed AND-extremality programme is false:

> a prime gate that violates the old read-once potential can always expose its violation by physically restricting until a balanced or dyadic AND-chain output measure is reached, with the block restriction margin no larger than the old certified payment.

The explicit ten-input gate has root `c_G>0.0182891`, while every positive-currency proper dyadic continuation has `c<=0`; by the exact martingale, every adaptive dyadic-stopping block must instead have signed block margin at least the root value, hence greater than `0.01`.

### NOT refuted

This does **not** refute FEI, the gate reformulation, the restriction-margin martingale, or `PRIME-GATE-LIFT`. The currently forced lift `a_*≈0.2682003346` is far larger than the ten-input root margin, so this witness is paid by that lifted candidate at uniform bias.

### Replacement obligation

A surviving proof must do at least one of the following:

* prove the lifted inequality directly on genuinely prime root interactions;
* exploit **non-dyadic** biased descendants together with their exact child slack;
* or prove a signed all-depth restriction estimate in the `Q_r c_r` currency that does not demand a locally paid dyadic stopping block.

The natural next adversarial test is therefore not another balanced or dyadic restriction sweep. It is to evaluate the lifted prime-gate candidate on source-exact **nonuniform, non-dyadic bias deformations** of a known prime obstruction and try to exceed the current forced lift; failing that, derive a curvature/monotonicity bound around the obstruction that genuinely constrains all such deformations.

**Next recipients:** `fleet02/B17` for the PRIME-GATE-LIFT adversary/reduction, `fleet02/B16` for the restriction-margin martingale, and `fleet03/B18` for integration into the common all-gate target.

## 6. Exact computation and limitations

`check_prime_dyadic.py` is standard-library Python. It reconstructs the inherited parent and child truth tables by their source hashes, recomputes exact influence and Walsh data, independently checks block primality, exhausts the 59048 proper physical restrictions, and certifies all logarithmic comparisons with rational interval arithmetic.

Executed checker SHA-256:

`719ae763268d3f5d80eae133b532d246347b7e60b81ca37d4771f563f0c8e340`.

Captured output SHA-256:

`2599a2adc65b80bfbf5a28d341e4d8d4fc6f5f06d7f536c048556c4cf754ca52`.

The finite certificate proves only the explicit witness theorem above. It is not a finite-dimensional extrapolation to all gates. No novelty or publication-priority claim is made. **Full FEI remains OPEN / NOT PROVED.**
