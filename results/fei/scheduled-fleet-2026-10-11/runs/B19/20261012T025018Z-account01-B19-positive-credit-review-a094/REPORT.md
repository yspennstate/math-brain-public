# B19 / A094 independent review of the A023 positive-credit theorem

**Run:** `20261012T025018Z-account01-B19-positive-credit-review-a094`  
**Primary packet:** A094, proof-chain challenger  
**Reviewed target:** A023, `B05-A023-POINT-DEFECT-POSITIVE-CREDIT-BOUND-v1`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** **ACCEPTED at the declared finite, disjoint point-defect, deterministic factor-first, complete `L+Q` packet scope.** Full FEI remains **OPEN**.

## 1. Immutable target and independence

The reviewed B05 bundle is pinned at open-problems commit
`9ddbf20daf52b3939ef6cd277677ee380ba993da`, path
`reports/fei-2026-10-11/runs/B05/20261012T023149Z-account01-B05-positive-credit-a023/`.
Its report blob is `35833556475a97809b52b357097848d6600ab488`
and its report SHA256 is
`e1d9dd932be11c5ec820c4e6c7b73d033e559bc0f99a7e8238eaf8da50ae4c25`.
The analytic proof blob is `251d3d10b58e7847f56bf94c83eca4e7c9e41168`.

This reviewer did not contribute the reviewed theorem. The submitted checker
was inspected but was not imported by the independent checker. The needed
multifactor ownership dependency was separately reconstructed and accepted by
B19 in run `20261012T015630Z-account01-B19-multifactor-review-a094`, final
canonical commit `dd6f45aa1c65ed29a0e388b232dd6fa982a40aef`.

## 2. Claim frozen before review

For every finite list of point defects `q_(n_j)` on pairwise disjoint uniform
Boolean blocks, and every deterministic order that exhausts one factor before
moving to the next, let `P_j` be the complete reach-weighted positive `L+Q`
credit of stage `j`. The submitted claim is

\[
 P_j<48\,2^{-n_j}\le 24 I(q_{n_j}),\qquad
 \sum_jP_j<24I\!\left(\prod_jq_{n_j}\right).
\]

Together with the independently accepted exact identity
`R(A)+sum_j N_j=sum_j P_j`, this is a complete single-use payment on this
restricted family. No claim is made for addressing, shared variables,
unrelated Boolean leaves, or arbitrary stopping trees.

## 3. Independent analytic reconstruction

Write

\[
F(p)=4p(1-p)-2(1-p)^2\log_2(1-p)-2p^2\log_2p
 +(1-2p)^2\log_2(1-2p),\quad 0\le p\le\tfrac12.
\]

For a current factor `q_a`, put `delta=2^-a`. If the unrevealed remaining
product disagrees with its constant reference with probability `y`, define

\[
\phi_y(x)=F(y+(1-2y)x),\qquad
s_y(x)=\frac{\phi_y(x)-\phi_y(0)}x.
\]

At residual dimension `m>=2`, `x=2^-m`, direct substitution in the physical
parent-minus-average-children credit gives

\[
\Gamma_m(y)=x[s_y(x)-s_y(2x)].
\]

The unique continuing node has reach probability `2^(m-a)=delta/x`.
Therefore its reached positive contribution is exactly

\[
\delta[s_y(x)-s_y(2x)]_+ . \tag{3.1}
\]

The submitted derivative identities recheck exactly:

\[
F''(p)=-8+\frac4{\ln2}\ln\frac{(1-2p)^2}{p(1-p)},\qquad
F'''(p)=-\frac4{(\ln2)p(1-p)(1-2p)}<0. \tag{3.2}
\]

For `y<1/2`, `phi_y''` is decreasing. Moreover

\[
s_y'(x)=x^{-2}A_y(x),\qquad
A_y(x)=\int_0^x t\phi_y''(t)\,dt. \tag{3.3}
\]

Because `A_y'(x)=x phi_y''(x)` and `phi_y''` is decreasing, `A_y` first
increases and then decreases. It starts at zero, so it can cross zero at most
once. Thus `s_y` is first nondecreasing and then nonincreasing. Reversing the
argument direction does not create a second rise: the sampled sequence
`s_y(2^-m)`, as `m` increases, is also one-rise/one-fall. Hence the sum of the
positive increments in (3.1) is at most the full range of `s_y`.

The exact derivative

\[
F'(p)=4-8p+\frac4{\ln2}\big[(1-p)\ln(1-p)-p\ln p
 -(1-2p)\ln(1-2p)\big]
\]

and `|t ln t|<=1`, `ln 2>2/3` imply `|F'|<22`. Every secant `s_y`
is an average of `phi_y'`, and `|phi_y'|<=|F'|`; therefore `|s_y|<22`.
All `m>=2` levels contribute less than `44 delta`.

At `m=1`, the parent parameter is exactly `1/2`, both child packets equal
`F(y)` by complete-packet sign symmetry, and the reach probability is
`2 delta`. Since `F(1/2)=2` and `F(y)>=0`, this level contributes at most
`4 delta`. Consequently

\[
P(a\mid y)<48\delta. \tag{3.4}
\]

Finally `I(q_a)=2a delta>=2 delta`, and influence is exactly additive under
products on disjoint blocks. Summing (3.4) over the chosen factor order proves
the submitted constant 24.

## 4. Endpoint and normalization challenge

- `y=1/2`: `phi_y` is constant, so every `m>=2` credit vanishes.
- `y=0`: `F''` has only a logarithmic endpoint singularity; `t phi_0''(t)`
  is integrable in (3.3), and `F'(0)=4` by continuity.
- `a=1`: there is no secant tail. The sole stage has positive credit 2 and
  influence 1, giving ratio 2, safely below 24.
- Unequal dimensions: `y` is the exact parity-disagreement probability of
  the remaining factors and always lies in `[0,1/2]`; no equal-dimension
  assumption occurs.
- Order: the stage estimate is uniform in `y`, so it applies to every
  deterministic factor-first order without optimization.
- Physical units: `delta/x` is the reach probability, not a Fourier weight;
  multiplying it by the local credit cancels the local `x` exactly once.

## 5. Independent computation

`verify_a023_positive_credit.py` imports none of the submitted code. It uses
exact `Fraction` probabilities and independently implemented rational
atanh-series enclosures for every logarithm.

Command:

`python3 verify_a023_positive_credit.py`

Observed result: **13,715 checks passed, zero failures, no randomness**. The
test covers 913 complete ledgers and 2,802 factor stages: every order for all
dimension tuples in `{1,...,5}^r`, `1<=r<=3`; every order for selected
four-factor endpoint and unequal cases; and ordered/reversed/permuted
five- and six-factor cases through dimension 63. It also checks the exact
common numerator `-1` behind (3.2) at 9,999 rational points. The largest
rigorously enclosed ratio was 2, at the one-bit factor.

This computation checks normalization, signs, all-order behavior, and hard
finite regimes. The analytic argument supplies the all-dimensional result.

## 6. Controls and exact accepted scope

Accepted:

1. every finite disjoint product of genuine Boolean one-point defects;
2. every deterministic factor-first exhaustive order;
3. the complete conditional-label plus phase packet;
4. the stage bound `P_j<48*2^-n_j` and total bound `sum P_j<24 I(f)`;
5. in combination with the separately accepted ownership identity, a finite
   physical single-use payment for this family.

Not accepted or implied:

- addressing or multiplexers with unrelated leaves;
- products with shared physical variables;
- arbitrary Boolean prime gates beyond point defects;
- arbitrary adaptive or interleaved stopping trees;
- an optimal constant;
- a Boolean counterfamily with unbounded `H/I`;
- full FEI.

Sparse defects are the theorem family, and unequal disjoint products test the
near-tensor regime. The proof retains the rare logarithms inside `F`; it does
not replace them by a pointwise `O(I)` charge. Bent selectors and parity-zero
erasure are not invoked. Fresh rare activation would add its own control
packet and is not silently covered by this estimate.

## 7. Mathematical movement and remaining leaf

**Prior status:** exact single-use ownership had been independently accepted,
but the positive side had no dimension-independent influence bound.

**New reviewed status:** the submitted uniform bound is independently
accepted for the full declared unbounded point-defect product family:

\[
\frac{\sum_jP_j}{I(f)}<24.
\]

The first unsupported universal step is now distribution-valued rather than
scalar: find an analogue of the secant slope for unrelated Boolean branches
or shared variables whose positive variation has a nonreused physical
influence/KL budget and survives whole-set addressing.

No external novelty or priority claim is made. This is a source-bound review
of a campaign theorem.

## 8. Disposition

`B05-A023-POINT-DEFECT-POSITIVE-CREDIT-BOUND-v1` is
`INDEPENDENTLY_ACCEPTED_AT_DECLARED_SCOPE`. The result is reusable as a
restricted nonlocal rarity-payment theorem. Full FEI remains **OPEN**.

- Model: Codex; runtime version and reasoning-effort metadata were not exposed.
- Subagents: none.
- Scheduler, shared registry, and graph mutation: none.
- Native Brain ingestion: not claimed.

