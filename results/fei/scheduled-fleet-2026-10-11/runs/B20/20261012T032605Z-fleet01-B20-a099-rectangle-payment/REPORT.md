# B20 / A099 — universal rectangle payment and candidate assembly

**Run:** `20261012T032605Z-fleet01-B20-a099-rectangle-payment`  
**Primary packet:** A099 (Candidate assembly)  
**Attempt:** `A099-RECTANGLE-PAYMENT-1`  
**New claim:** `B20-A099-RECTANGLE-PAYMENT-v1`  
**Open leaf:** `G-CRITICAL-RECTANGLE-DECREMENT-v1`  
**Status:** three exact all-dimensional identities **PROVED pending independent
review**; candidate constant 8 **NUMERICAL only**; critical decrement inequality
and full FEI **OPEN**.

## Frozen target and prior status

The strongest current critical-source route had two relevant pieces:

1. A096 proves that a descendant-critical source of ratio `R` obeys
   `Delta_i H >= R I_i` at every essential coordinate, and that a
   minimum-dimensional counterexample is tensor-prime.
2. A054 defines the physical rectangle defect `rho_A`, extracts a genuine
   anchored Boolean product, and bounds its component excess by
   `E_{n,a}(rho)`.  Its explicit paid-cut theorem required `rho` to be much
   smaller than the block influence; universal cut admission remained open.

The exact question selected for this run was whether `rho_A` itself has a
dimension-free, nonreusing payment by physical influence.  This is a necessary
cross-route substitution before trying to remove the square-root continuity
loss in A054.

## New theorem: every rectangle interface is influence-paid

For every Boolean `f(x_A,y_B)`, define

`rho_A(f)=Pr[f(x,y)f(x',y)f(x,y')f(x',y')=-1]`.

Then, for every nontrivial physical cut,

`rho_A(f) <= min{I_A(f), I_B(f)}`.

Proof: for fixed `y,y'`, set `r(x)=f(x,y)f(x,y')`.  The conditional rectangle
probability is `Var_x(r)/2`.  Cube Poincaré bounds `Var(r)` by
`sum_{i in A} I_i(r)`.  The product `r` changes across an `i`-edge exactly when
the two corresponding `f`-edges have different pivotality; averaging two
independent `y` values bounds this by `2 I_i(f)`.  The factor `1/2` cancels the
two.  Interchanging the blocks gives the second bound.

This proof is all-dimensional and has no dependence on dimension, block size,
bias, depth, overlap, address count, or correlation gap.

## Exact singleton and nonreusing tree forms

For every coordinate `i`, with `p_i=I_i(f)`, the stronger exact identity holds:

`rho_{i}(f)=p_i(1-p_i)`.

Indeed, the sampled `i` values differ with probability `1/2`, while two
independent pivotality indicators of mean `p_i` differ with probability
`2p_i(1-p_i)`.

Consequently,

`sum_i rho_i = I(f)-sum_i I_i(f)^2 <= I(f)`.

More generally, for any physical restriction tree that queries a coordinate
at most once on each path,

`sum_v w_v rho_{i(v)}(f_v)
 <= sum_v w_v I_{i(v)}(f_v)
 = I(f)-sum_l w_l I(f_l) <= I(f)`.

The equality is the exact influence telescope.  Hence rectangle interfaces
form a globally nonreused physical budget, not merely a local diagnostic.

## Cross-route substitution and exact movement

Substituting the theorem into A054 closes the geometric-payment half of its
admission gap: every `rho_A` is already bounded by the influence on either side
of the cut.  What remains is purely analytic.  A054's current excess function

`E_{n,a}(rho)=2h2(2sqrt(rho))+(2n-a)2sqrt(rho)+6an rho`

still contains square-root and ambient-dimension losses.  For a singleton with
small `p`, `rho=p(1-p)~p` but `sqrt(rho)/p` diverges.  Thus the existing generic
continuity estimate cannot be made dimension-free merely by paying the
interface.  The paid-cut criterion in A054 is sufficient on its stated class,
but is far stronger than the newly proved universal payment.

## Smaller unpaid inequality

The assembly now isolates this exact open leaf.

> **Critical rectangle decrement (CRD-v1).** There is an absolute finite
> `C_rect` such that every nonconstant descendant-critical tensor-prime Boolean
> `f` has an essential coordinate `i` with
> `Delta_i H(f) <= C_rect rho_i(f)
> = C_rect I_i(f)(1-I_i(f))`.

This is genuinely narrower than full FEI: it is restricted to
descendant-critical tensor-prime sources and asks for one coordinate.  If true,
A096 gives

`R I_i <= Delta_i H <= C_rect I_i(1-I_i) <= C_rect I_i`,

so `R<=C_rect`.  A minimum-dimensional counterexample to a proposed constant
is descendant-critical and tensor-prime, so CRD plus the audited A096/A052
reductions would establish FEI with that constant.

No proof of CRD is claimed.  It is the first unsupported universal line in
`CANDIDATE_MANUSCRIPT.tex`.

## Mandatory counterexample controls

- **Rare restrictions / sparse defects:** `rho_i~I_i` for rare coordinates,
  so the geometric budget is correct.  The unresolved rare logarithm is in
  `Delta_i H`, not in the interface payment; no B05 rare-refund claim is
  revived.
- **Addressing / multiplexers:** the theorem charges actual physical cuts and
  never treats selector labels or reused variables as free.  Established
  fresh-selector/orthogonality endpoints are not reopened.
- **Near tensors and one-point surgery:** a small rectangle defect is paid,
  but A054's square-root continuity loss remains explicit.  Qualitative
  primitivity is not used.
- **Parity-zero erasure:** if `I_i=1`, then `rho_i=0`; for a pure parity split
  `Delta_i H=0`, so the exact identity retains the zero endpoint.
- **Prime Boolean gates:** CRD is deliberately stated on tensor-prime sources;
  the two-bit one-point gate is the observed extremal finite control.
- **Shared variables:** no product additivity across overlapping variables is
  asserted.  The block theorem uses a single physical partition.

## Exact and numerical checks

Command: `python3 verify_rectangle_payment.py`.

Using integer arithmetic only, the checker exhausts every Boolean truth table
for `1<=n<=4`, every nontrivial block cut up to complement, every singleton,
and the complete fixed-order physical restriction tree.  It passed:

- 919,072 block-payment assertions;
- 262,948 singleton-identity assertions;
- 131,624 tree-budget/telescope assertions;
- 1,313,644 assertions total over 65,812 Boolean tables.

These checks reproduce the identities; the proofs in the manuscript establish
them in all dimensions.

Command: `python3 probe_critical_rectangle.py`.

The separate floating diagnostic found 1,146 descendant-critical tensor-prime
tables through four variables.  The largest observed
`min_i Delta_i H/rho_i` was `8`, attained by the two-bit one-point gate.  The
one-point/AND family through dimension 12 decreased from 8 toward 4.  This is
**NUMERICAL**, not an interval certificate, not a proof of CRD, and not evidence
for arbitrary dimension.  The value 8 is therefore only a candidate constant.

## Source-bound coordination follow-up

The current full-FEI control manifest records 20 verified native fleet01
adoptions and an intended additional 60, but no recipient-authored peer native
adoption evidence at the checked revision.  A single bounded follow-up was
sent to the four registered dot recipients, asking for source-bound distinct
or overlapping native coverage and explicitly prohibiting duplicate migration,
new schedules, forced runs, endpoint changes, or counting transport as
adoption.

Follow-up readback:

- Brain commit `0d364f601cb420220924db9191e20c27f3ee3cd3`;
- message blob `c03c973304acd5b38cd2f7b4125d95842e54196a`;
- path
  `scheduled_tasks/handoffs/brain-inbox/messages/REQ-20261012T031958Z-FULL-FEI-OWNER--fleet01-B20--progress-20261012T033050Z.json`.

Actual coverage remains **20 verified local native adoptions; 60 intended and
unverified**.  Delivery or later adoption is not claimed in this run.

## Source pins actually used

- Full-FEI owner order baseline commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- Current manifest blob `575eff8ad97d9131bb51b895968f2025241c1e62`.
- Original owner request blob `3290aff155f63dbc1a5c58ae58c3dc3d6254b508`.
- B20 compact contract blob `d5872923b24d68dbcb93394134e3309302f5d034`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A053 near-tensor theorem blob
  `843dc932a9074272b1cf90c3ebbd9ae74ae69559` (pending review).
- A054 canonical receipt `1c1768bbb9aa1c632258326b0737c217c44d2b42`
  and Brain receipt `9ce3701e7017a67e5e4de21d91991be995efb7c4`.
- A096 tree-slack report blob `b1f1d7e4440033f59d1b047ebb10ab0f84d3a332`.
- A097 run
  `20261012T022431Z-fleet01-B20-a097-rankone-critical`.

No literature novelty claim is made.

## Review and handoff

Route Theorems 1--3 to A090 and A094 for independent reconstruction.  Route
CRD-v1 to A087 for derivation from the critical restriction identities, A092
for Boolean countersearch on larger prime gates and near tensors, and A085 for
certificate design if a finite extremal reduction appears.  B20 should next
try to prove CRD first on symmetric one-point gates and then on a class closed
under physical restriction, while retaining terminal terms.

Independent review has not occurred.  A099 is not complete under its contract,
candidate constant 8 is not established, and full FEI remains **OPEN**.
