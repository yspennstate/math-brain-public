# B17 FEI — arity-5 asymmetric adversary: exact quarter-output exclusion

**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** **ESSENTIAL_STEP_APPLIED** at one new arity-5 slice; full FEI remains **OPEN / NOT PROVED**.  
**Live target:** the 2026-09-22 owner gate reformulation, not the superseded interface-C / restriction assignment.

## 1. Exact candidate and peer result consumed

The live owner target is the gate inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i I^t_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p),
\tag{1.1}
\]

with required margin

\[
c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})},
\tag{1.2}
\]

where `D_G` is RHS minus LHS.  The current read-once fixed-point candidate has
`C_0=Gamma(1/2)=6.4548`; the source report's current two-input AND floor is
`c_AND^max = 4.3974201e-3`.

I consumed the completed cross-account result

`account04/B17/20260922T001445Z-gate5-balanced-central/REPORT.md`,
commit `2312eae492a94dd9d4aaa80f0a6d2cf3dcefd930`, report blob
`86d88a95c22db2fc847839c69c0f9a3e6f2173cd`.

That report proves for **every balanced five-input gate at uniform input bias**

\[
H(G)\le 6(I(G)-1),\qquad c_G(1/2,\ldots,1/2)\le-1.8192
\tag{1.3}
\]

outside dictators, by an analytic Gibbs envelope plus an exact low-boundary certificate.  I applied it adversarially: the balanced central slice is therefore not where an arity-5 falsifier can hide, so this run moved to the first asymmetric dyadic output slice

\[
p_1=\cdots=p_5=\frac12,\qquad p_{\rm out}=\frac14.
\tag{1.4}
\]

This is not a repeat of the peer calculation: it covers all `C(32,8)=10,518,300` quarter-output truth tables, whereas the peer theorem covered the balanced `|A|=16` slice.

## 2. New theorem

Let `G:{0,1}^5->{-1,1}` be uniform-input Boolean with
`Pr[G=-1]=1/4`.  Then

\[
\boxed{H(G)\le 6I(G)-4.}
\tag{2.1}
\]

The current read-once fixed point is exact on dyadic AND-chain points, so

\[
\Gamma(1/4)=C_0-2.
\tag{2.2}
\]

Consequently

\[
D_G=C_0I-H-(C_0-2)
\ge (C_0-6)(I-1)\ge0,
\tag{2.3}
\]

because the edge-isoperimetric minimum on an eight-point subset of `Q_5` is
`I>=1`.  Thus

\[
\boxed{c_G(1/2,\ldots,1/2)\le0}
\tag{2.4}
\]

throughout this entire asymmetric arity-5 slice.  Equality `c_G=0` occurs at the 40 codimension-two coordinate subcubes (`I=1,H=2`), i.e. gates with dummy inputs, not genuinely five-input adversaries.

If all five input coordinates are essential, the exact enumeration below shows `I>=5/4`.  Combining this with (2.1) gives the stronger sharp bound

\[
\boxed{c_G\le-0.9096.}
\tag{2.5}
\]

It is attained.  One equality truth set is

\[
A=\{0,1,2,3,4,5,8,10\},\qquad G=1-2\mathbf1_A,
\tag{2.6}
\]

whose coordinate influences are `(1/8,1/8,1/4,1/4,1/2)`, so all five coordinates are genuinely active, and

\[
I=5/4,\qquad H=7/2,\qquad c_G=-0.9096.
\tag{2.7}
\]

Hence this slice is separated from the positive AND margin by more than `0.91`.

## 3. Analytic high-boundary proof

Write `A={x:G(x)=-1}`, so `|A|=8`, and let `B` be its undirected edge boundary in `Q_5`.  Then

\[
I(G)=B/16.
\tag{3.1}
\]

The empty-set spectral mass is fixed:

\[
q_\varnothing=(1-2p_{\rm out})^2=1/4,
\tag{3.2}
\]

so the nonempty spectral mass is `V=3/4`.  Normalize the nonempty law by
`q'_S=q_S/V`.  Compare it with

\[
r_S=\frac{3^{-|S|}}{Z},\qquad
Z=\sum_{S\ne\varnothing}3^{-|S|}
=(4/3)^5-1=781/243.
\tag{3.3}
\]

From `D(q'||r)>=0`,

\[
H(G)
\le h_2(1/4)+\frac34\log_2 Z+I(G)\log_2 3.
\tag{3.4}
\]

At `I=3/2` the RHS becomes

\[
2+\frac34\log_2(781/81)<5=6(3/2)-4,
\tag{3.5}
\]

and the strict comparison is elementary because

\[
781/81<16\iff781<1296.
\tag{3.6}
\]

The Gibbs envelope has slope `log_2 3<6`, whereas the target `6I-4` has slope 6.  Therefore (2.1) holds strictly for every `I>=3/2`, equivalently every `B>=24`.

Only `B<=22` remains.

## 4. Exact low-boundary certificate

The adjacent checker enumerates every eight-point subset of `Q_5`.  The total is exactly

\[
\binom{32}{8}=10,518,300.
\tag{4.1}
\]

Only the following low boundaries occur:

\[
\begin{array}{c|r}
B&\#A\\\hline
16&40\\
20&7680\\
22&45440.
\end{array}
\tag{4.2}
\]

There is no `B=18` case.

For unnormalised Walsh integers

\[
W_S=\sum_xG(x)(-1)^{S\cdot x},
\tag{4.3}
\]

Parseval and influence give

\[
\sum_SW_S^2=1024,
\qquad
L:=\sum_S|S|W_S^2=64B,
\tag{4.4}
\]

while

\[
H=10-\frac1{1024}\sum_{W_S\ne0}W_S^2\log_2W_S^2.
\tag{4.5}
\]

Thus (2.1) is **exactly** equivalent to the integer inequality

\[
\boxed{
\prod_{W_S\ne0}(W_S^2)^{W_S^2}
\ge 2^{14336-6L}.
}
\tag{4.6}
\]

For `|A|=8`, every nonzero `|W_S|` is one of `4,8,12,16`.  The exhaustive low-boundary enumeration collapses all 53,160 cases to only nine signatures `(n_4,n_8,n_12,n_16)`:

- `B=16`: `(0,0,0,4)` — equality;
- `B=20`: `(16,4,0,2)` — equality; `(0,8,0,2)` and `(14,0,2,2)` — strict;
- `B=22`: `(0,12,0,1)`, `(15,6,1,1)`, `(14,4,2,1)`, `(16,4,0,2)`, `(14,0,2,2)` — all strict.

The checker evaluates (4.6) by arbitrary-precision integer comparison for each signature; no floating-point sign decision is used for the theorem.  There are 40 equality cases at `B=16` and 1,920 equality cases at `B=20`.  All 1,920 `B=20` equality cases have every coordinate essential.

This completes the proof of (2.1).

## 5. Boundary and sparse adversarial checks

The computation also records all boundary strata:

`B=16,20,22,24,26,28,30,32,34,36,38,40`

with counts summing to `10,518,300`.  The strongest genuinely five-input quarter-slice margin is exactly the `B=20`, `H=3.5`, `I=1.25` row above, namely `-0.9096`.

As smaller companion checks at uniform input bias:

- output mass `1/32`: every gate is a one-point minterm, NPN-equivalent to `AND_5`, so the dyadic fixed-point constraint is equality;
- output mass `1/16`: all 496 two-point truth sets were checked; adjacent pairs are lower-dimensional subcubes with `c_G=0`, while every nonadjacent pair has `c_G=-8.262144`;
- output mass `1/8`: all 35,960 four-point truth sets were checked; the maximum is again `c_G=0` on coordinate subcubes, while the best all-five-coordinates-essential row observed has `c_G=-2.8054857142857` (`H=2.716917186688699`, `I=0.875`).  This last decimal is a finite diagnostic, not promoted here to an independent exact theorem.

Output negation preserves the gate inequality because `Gamma` is symmetric, so the corresponding masses `31/32,15/16,7/8,3/4` are covered as well.

Combining the **consumed account04 central theorem** with the new quarter theorem therefore eliminates two large and qualitatively different exact arity-5 uniform-bias slices: balanced output and quarter/three-quarter output.  It does not cover nonuniform input biases or the remaining output weights.

## 6. What was refuted, what remains

**Refutation attempt:** the natural asymmetric candidate was a sparse/unbalanced five-input gate at the uniform input point, because account04 had already removed the central balanced slice.  No falsifier exists at output mass `1/4`; theorem (2.1) proves this for all 10,518,300 such gates.  The genuinely active extremizer is still strongly negative in `c_G`.

**Dead subroute:** continuing a uniform-input search only on the dyadic output masses already handled above is low value.  It cannot beat the current AND margin.

**Replacement obligation:** move the adversarial search off the uniform-input hyperplane.  The next exact attack should start from the closest essential quarter-slice equality family (2.6), perturb one or two input biases away from `1/2`, and evaluate **the actual margin `c_G`**.  The arity-3/4 source data says near-binding behavior approaches a lower-arity AND face, so the critical question is whether a genuinely active perturbation can increase from `-0.9096` past `+0.0043974201` before an influence dies.  If it cannot, derive a local curvature/monotonicity theorem around that family rather than another broad sweep.

**Old missing implication:** does any genuinely higher-arity Boolean gate require more read-once potential margin than the two-input AND constraint?

**New proved inference:** no five-input gate at uniform biases with output mass `1/4` or `3/4` does; indeed all essential gates there satisfy `c_G<=-0.9096`.  Together with account04/B17, balanced five-input gates at uniform biases satisfy an even stronger negative margin.

**Remaining implication to full FEI:** prove `c_G(p)<=c_AND^max` for every gate, every arity and every bias vector (or find a genuine counterexample).  The present result addresses only exact arity-5 slices and is not full FEI.

**Consumed peer artifact:** account04/B17 `20260922T001445Z-gate5-balanced-central/REPORT.md`, commit `2312eae492a94dd9d4aaa80f0a6d2cf3dcefd930`, blob `86d88a95c22db2fc847839c69c0f9a3e6f2173cd`.

**Applied to claim:** peer central exclusion forced this adversary into the asymmetric unbalanced quarter-output region instead of duplicating a balanced sweep.

**Next recipient:** all FEI gate-reformulation workers; in particular a proof-side worker should use (2.1) as an exact anchor for bias perturbations off `p_i=1/2`, and adversarial workers should skip the now-closed quarter/three-quarter uniform-input slice.

**Full FEI status:** **OPEN / NOT PROVED**.
