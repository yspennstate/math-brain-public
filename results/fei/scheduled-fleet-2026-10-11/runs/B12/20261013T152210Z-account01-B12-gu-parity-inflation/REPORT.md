# B12 / A056 — balanced GU composition and parity inflation

Run: `20261013T152210Z-account01-B12-gu-parity-inflation`  
Attempt: `A056-GU-PARITY-INFLATION-02`  
Gap: `B12-A056-GU-COMPOSITION-v1`  
Status: **EXACT PROPER-CLASS THEOREM AND SIGNED OBSTRUCTION PROVED BY CONTRIBUTOR; REVIEW PENDING; UNIVERSAL GU AND FEI OPEN**

## Outcome

This run proves the exact upper-mass chain rule for balanced disjoint
substitution and then solves the complete GU accounting problem for a new
unbounded composition class: an arbitrary Boolean outer gate whose inputs are
encoded by disjoint parity blocks.

For balanced disjoint children,

\[
U(g(h_1,\ldots,h_m))
=U(g)+\sum_j \operatorname{Inf}_j(g)U(h_j),\qquad
I(g(h_1,\ldots,h_m))
=\sum_j \operatorname{Inf}_j(g)I(h_j).
\]

For parity blocks `P_j` of sizes `d_j>=1` and
`F=g(P_1,...,P_m)`, the sharper physical law is

\[
U(F)=U(g),\qquad
I(F)=\sum_j d_j\operatorname{Inf}_j(g),\qquad
G(F)=\sum_{j:d_j=1}\Delta_jU(g).
\]

Thus every physical coordinate in a nonterminal parity block (`d_j>=2`)
has exactly zero `U` decrement.  If all blocks are nonterminal, then
`G(F)=0`; this gives the dimension-, arity-, width-, and depth-independent
class constant `K=0` for every outer Boolean gate.

## Why the class matters

The previous B12 GU result treated arbitrary disjoint factors under the
parity/product outer gate.  This run proves the complementary axis: arbitrary
outer gates with parity inner factors.  It includes all arities and arbitrarily
large physical blocks, and nested parity realizations flatten to the same
formula.  It also tracks precisely when the deferred `U` payment reappears:
only when a block reaches physical size one.

This is not a universal GU proof.  It shows that GU mass can be deferred
through arbitrarily many parity layers; any induction must preserve terminal
reserves rather than seek a positive one-scale lower bound on `G`.

## Signed obstruction found

The exact formula exposed a false monotonicity heuristic.  Coordinate
decrements need not be nonnegative.  For the genuine three-bit Boolean truth
vector

`(+,+,-,+,+,-,-,-)`

in standard mask order,

\[
U(g)=\tfrac12,\quad
(\Delta_1U,\Delta_2U,\Delta_3U)
=(\tfrac12,-\tfrac12,-\tfrac12),\quad
G(g)=-\tfrac12,\quad I(g)=\tfrac32.
\]

Inflating coordinates two and three to width-two parity blocks deletes the
negative summands and gives `G=1/2`, `I=5/2`.  Therefore:

- `Delta_i U >= 0` is false, even for a three-bit genuine Boolean function;
- `G` is not monotone under parity inflation;
- a composition proof may not discard signed coordinate terms individually.

This is an auxiliary falsifier only.  It is not a counterexample to GU or
FEI.

## Proof mechanism

For a physical spectral set with active child set `A`, balancedness yields

\[
p_F(S)=p_g(A)\prod_{j\in A}p_{h_j}(S_j),\qquad
\pi_F(S)=\pi_g(A)\prod_{j\in A}\pi_{h_j}(S_j).
\]

The second identity uses exactly
`sum_{T nonempty} p_{h_j}(T)=1`.  Its logarithm separates, proving the
balanced chain rule.  For parity children, restriction of a coordinate in a
block of size at least two leaves a nonempty parity.  The possible sign is
only an input flip of the outer gate and does not change squared Fourier
coefficients, so both restricted children retain upper mass `U(g)`.  A
size-one block instead becomes an actual outer restriction, giving the
terminal term `Delta_j U(g)`.

The full proof is in `GU_PARITY_INFLATION.tex`.

## Verification

Command:

`python3 check_gu_parity_inflation.py`

The deterministic checker passed:

- 1,024 balanced-chain cases: all 16 two-bit outer Boolean gates and all
  ordered pairs of balanced one- or two-bit children;
- 2,120 parity-inflation cases: every Boolean outer gate through arity three
  and every width vector in `{1,2}^m`;
- 276 all-nonterminal cases with exact numerical `G=0`;
- the signed three-bit obstruction above.

Walsh coefficients and influence are exact `Fraction` values.  Logarithms use
100-digit decimal arithmetic.  There is no random seed.

## Previous and new bound

- Previous: no B12 theorem for arbitrary outer gates in the GU composition
  ledger; the prior theorem covered parity/product outer composition.
- New: `G(F)=0` exactly for every parity inflation with all block sizes at
  least two, so the covered class has sharp constant `K=0`, uniformly in all
  parameters.
- Mixed terminal/nonterminal widths satisfy the exact signed formula above,
  not a monotone closure inequality.

## Remaining universal gap

For a generic balanced child, physical restriction creates two biased child
laws rather than a signed nonempty parity.  The balanced root chain rule
therefore does not subtract cleanly at the children.  The next unpaid step is
an exact biased-child defect identity retaining signed coordinate terms, then
a payment of its complete coherent remainder from one source-influence or
terminal-reserve budget.  This is the GU version of the existing coherent
remainder obstruction.

## Review and endpoint status

- Contributor proof: complete at the stated scope.
- Deterministic self-check: passed.
- Independent end-to-end review: not observed.
- Universal GU: **OPEN**.
- Full FEI: **OPEN**.

