# B20 / A099 — tensor-prime minimal-counterexample curvature for GU

**Status:** exact reduction and gate obstruction **PROVED**, finite base **CERTIFIED**, universal good-coordinate estimate **OPEN**. Independent review pending. **Universal GU and full FEI remain OPEN.**

## Frozen candidate and exact implication

- Primary packet: **A099 (Candidate assembly)**.
- Attempt: `A099-GU-CURVATURE-PRIME-1`.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim version: `B20-A099-GU-CURVATURE-PRIME-v1`.
- Frozen pair: `(a,b)=(14,0)`.

For physical restriction averages `P_i`, put `Delta_i=1-P_i`. The candidate is

\[
\boxed{
\min_{i:\operatorname{Inf}_i(f)>0}
\frac{\Delta_iG(f)}{\operatorname{Inf}_i(f)}\le14
}
\tag{GC14}
\]

for every nonconstant tensor-prime genuine Boolean function. Proving `(GC14)` in all dimensions would imply

\[
G(f)\le14I(f),\qquad U(f)\le14I(f),\qquad H(f)\le30I(f)
\]

for every Boolean `f`. The last two implications were checked against the original `U-universal/NOTES.md` proof: GU with `(14,0)` closes the restriction induction for `U`, and the proved bridge `H<=2I+2U` gives `30`.

## Exact residual derivative

For arbitrary `a>=0`, `0<=b<1`, define

\[
\mathcal R_{a,b}=G-aI-bU.
\]

Physical restrictions commute, and the influence decrement is `Delta_i I=p_i=Inf_i(f)`. Directly expanding `G=sum_j Delta_jU` gives

\[
\boxed{
\Delta_i\mathcal R_{a,b}
=(1-b)\Delta_iU+\sum_{j\ne i}\Delta_i\Delta_jU-a p_i.}
\tag{1}
\]

This retains genuine Boolean children, signs, all normalization terms, and every mixed restriction term.

If GU fails for a fixed pair, choose a positive-residual counterexample with the smallest number of relevant coordinates. B07's proved tensor additivity makes this counterexample tensor-prime. Every child has nonpositive residual, hence for every relevant coordinate

\[
\boxed{
(1-b)\Delta_iU+\sum_{j\ne i}\Delta_i\Delta_jU>a p_i.}
\tag{2}
\]

Thus a counterexample must be simultaneously curvature-positive in every physical direction; positive GU residual alone is insufficient.

Conversely, if every tensor-prime function has one coordinate reversing (2), minimal-counterexample induction proves universal GU. Since

\[
\Delta_iG=\Delta_iU+\sum_{j\ne i}\Delta_i\Delta_jU,
\]

this criterion at `(14,0)` is exactly `(GC14)`. A stronger sufficient aggregate is

\[
G(f)+2\sum_{i<j}\Delta_i\Delta_jU(f)\le14I(f)
\]

on tensor-prime functions, but that stronger estimate is not asserted.

## Exact lower bound for this mechanism

Let `q` be the symmetric four-bit function equal to `+1` exactly on Hamming weights one and two. It has flat squared Walsh spectrum and

\[
U(q)=I(q)=2,\qquad G(q)=\frac{11}{2}.
\]

For every coordinate,

\[
p_i=\frac12,\qquad \Delta_iU=\frac{11}{8},\qquad
\Delta_iG=\frac{53}{8}.
\]

Therefore the general good-coordinate method cannot hold at this gate unless

\[
\boxed{4a+11b\ge53.}
\]

The gate is tensor-prime: any factorization across a nontrivial partition would force every mixed multiplicative rectangle to have product `+1`, whereas at the zero input and one coordinate from each side the four values have weights `0,1,1,2` and product `-1`. Tensor powers preserve all local numbers because cross-factor mixed `U` curvatures vanish. This is an all-dimensional obstruction to smaller constants for this induction, not a GU or FEI counterexample: every tensor power has `G/I=11/4` and `U/I=1`.

## Finite certification

`verify_minimal_gu_curvature.py` uses exact Walsh integer numerators, exact rational influences, and 80-digit correctly rounded decimal logarithms. It checked:

- all **65,812** Boolean truth tables through dimension four;
- **261,866** relevant-coordinate inequalities;
- `(GC14)` with minimum unnormalized margin `0.375`;
- the exact worst good-coordinate ratio `53/4`, attained by truth table `6014`; and
- exact `(U,I,G)` additivity on the tensor square of that gate.

The finite check is not a tail argument. The open step is proving `(GC14)` uniformly in dimension on tensor-prime sources.

## Before / after

- **Before:** B07 reduced GU to the signed KL aggregate on tensor-prime functions, but every positive-residual tensor-prime function remained in scope.
- **After:** it is enough to control only tensor-prime functions that are strict residual maxima under every one-coordinate physical restriction, equivalently those satisfying the reverse of `(GC14)` at every coordinate. The full second-order obstruction (2) is explicit.
- **Cost:** this induction mechanism intrinsically requires `4a+11b>=53`; pursuing constants near the observed raw GU ratio `3.09` through this curvature criterion is impossible.
- **Still unpaid:** prove one all-dimensional good-coordinate bound such as `(GC14)` using the signed convolution terms in `Delta_iU=B_i-Gamma_i+K_i`, or construct a tensor-prime Boolean family with `min_i Delta_iG/p_i` unbounded.

## Bounded reconciliation

The current alignment receipt and a fresh source search found no newer fleet01 canonical B02/B08/B13 bundles; the accessible results remain the explicitly labeled recovery leads, not reconstructed original runs. No newer B06 canonical commit than the already recorded October 12 package appeared. The newest complete B20 source inspected was the order-optimized amplification package; this run changes mechanism to GU curvature rather than repeating its posterior endpoint. A fresh private Brain search returned no new other-dot adoption receipt, so actual verified adoption remains 20 local schedules and 60 intended but unverified. No scheduler mutation or forced run was performed.

Requested independent reviewers: A090 and A094. Native Brain ingestion is not claimed.
