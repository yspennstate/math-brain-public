# B12 / A057 — changing-witness product-potential telescope

Run ID: `20261012T042255Z-account01-B12-changing-witness-potential`  
Primary packet: `A057` (Coherent restriction remainder)  
Attempt: `B12-A057-ATTEMPT-04`  
Claim: `B12-A057-CHANGING-WITNESS-POTENTIAL-v1`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v4`  
Full FEI: **OPEN**

## Bounded objective and prior status

The preceding B12 theorem proved, for one fixed outer Boolean pair
`a±b`, the all-depth bound

`sum_v w_v R_{mu_v}(alpha_v) <= [M(a,b)+(4+2ln2+2/e)q] I(h)`.

B19/A094 has now independently reconstructed and accepted that theorem at
exactly this fixed-source scope.  Its review identifies the first unsupported
universal quantity as

`sum_v w_v alpha_v^2 M(a_v,b_v)`

when the outer witness changes coherently.  The bounded objective of this run
was to freeze an actual parent--child coherence law and determine whether the
reserve telescopes once or must be repaired.

## New theorem — PROVED, independent review pending

Let `W` and `X` be disjoint physical blocks, let `g_+,g_-` be arbitrary
Boolean signs on `W`, put `a=(g_++g_-)/2`, `b=(g_+-g_-)/2`, and let `h` be
an arbitrary Boolean sign on `X`.  Run any finite adaptive physical
restriction tree on `W union X`, without coordinate reuse on a path.  Source
queries may be chosen after observing child answers and conversely.  Thus the
current pair `(a_v,b_v)`, its energy `q_v`, and its collision reserve can vary
and correlate with the current child `h_v`.

In natural-log units define

`Z_v=E_raw(b_v)`, `V_v=Var(h_v)`, `J_v=I(h_v)`, and
`C_*=4+2ln2+2/e=6.122053243462775...`.

At every node put

`P_v=C_* q_v J_v+V_v Z_v`.

If an `X`-coordinate is queried, let `R_v` be the exact biased coherent
remainder.  Then for every such adaptive tree,

`sum_{v: X-query} w_v R_v + sum_{leaf l} w_l P_l <= P_root`.       (1)

Consequently,

`sum_{v: X-query} w_v R_v`

`<= C_* q I(h)+Var(h) E_raw(b)`.                                   (2)

This is the first B12 theorem that allows the witness itself to change along
the tree.  It removes the fixed-source hypothesis for actual coherent
restrictions of one root splice and permits arbitrary adaptive interleaving,
unbounded dimension, unbounded depth, arbitrary bias/collision ratios, and
arbitrary correlation caused by the query strategy.

## Proof and the one-use reserve identity

At a child-coordinate query, `q_v,Z_v` stay fixed and the exact restriction
identities are

`J_v-(J_++J_-)/2=Inf_i(h_v)`,

`V_v-(V_++V_-)/2=alpha_v^2`.

The accepted one-node envelope is

`R_v <= q_v psi(alpha_v)+(4+2ln2)q_v alpha_v^2`

`       +M(a_v,b_v)alpha_v^2`.

Here `M(a_v,b_v)<=Z_v`, `psi(alpha)<= (2/e)|alpha|`, and
`alpha^2<=|alpha|<=Inf_i(h_v)`.  Therefore

`R_v <= P_v-(P_++P_-)/2`.

At a source-coordinate query, `h_v` is unchanged.  Parseval gives
`q_v=(q_++q_-)/2`, while nonnegativity of the scalar kernel gives
`Z_v>=(Z_++Z_-)/2`.  Hence `P_v>=(P_++P_-)/2`.  Summing these local Bellman
inequalities over the tree proves (1).

The reserve component has the sharper exact identity

`sum_{X-query v} w_v alpha_v^2 Z_v`

`+ sum_{W-query v} w_v V_v [Z_v-(Z_++Z_-)/2]`

`+ sum_leaf w_l V_l Z_l = Var(h) E_raw(b)`.                         (3)

Since `M_v<=Z_v`, (3) pays the changing ledger once.  The second term is
source restriction dissipation; the last is the unspent terminal reserve.
This is precisely the nonreusing accounting that the fixed-source theorem
lacked.

The full analytic proof, including endpoints, is in
`CHANGING_WITNESS_TELESCOPE.tex`.

## Exact scope and remaining universal obstruction

The newly covered class is every adaptive **interleaved restriction** of one
disjoint Boolean splice.  It is strictly larger than child-only restriction:
the outer source can be physically restricted at arbitrary branch-dependent
times, so all witness data can change.

It is not an overlapping-input theorem.  If one physical coordinate changes
both the source pair and the child at the same step, the two one-factor
potential drops no longer separate; covariance terms remain.  Nor does (2)
prove full FEI: the initial terminal budget `E_raw(b)` is not universally
bounded by source influence here.  The live next obligations are therefore:

1. pay `Var(h) E_raw(b)` by a nonreused source-influence or global terminal
   ledger already present in the full entropy decomposition; or
2. derive a signed covariance bound for a genuine shared-coordinate query.

This is mathematical movement rather than a relabeling of the old gap: the
entire node-dependent reserve is now telescoped for coherent restrictions of
one root source, and the first unsupported line has moved to the root terminal
derivative entropy/shared-coordinate covariance.

## Mandatory controls

- **Rare restrictions and sparse defects:** the full `q psi(alpha)` term is
  retained and paid by `psi(alpha)<=(2/e)Inf_i`; it is not replaced by
  `O(alpha^2)`.
- **Parity-zero erasure:** `alpha=0` gives zero remainder and zero variance
  drop exactly.
- **Whole-set addressing/adaptive order:** arbitrary branch-dependent
  interleavings are allowed; no depth sum or predetermined query order occurs.
- **Changing activation weights:** `q_v` may vary and correlate with child
  states; its source-query martingale law is used rather than a supremum.
- **Collision ratios and bias:** the previously accepted uniform kernel
  envelope is used with no separation or bias floor.
- **Actual prime Boolean gates:** `g_+,g_-` are arbitrary genuine Boolean
  branches; no spectral realizability relaxation is used.
- **Near tensors/overlap:** the theorem explicitly requires disjoint root
  blocks and does not claim a raw convolution or shared-variable product law.
- **Terminals:** the complete leaf potential remains visible in (1); it is not
  silently discarded from the exact ledger.

## Deterministic verification

Command:

`python3 check_changing_witness.py`

Result: **PASS**.

The independent checker performed:

- 197,136 local source transitions for every ordered pair of Boolean branches
  through three source bits;
- 221,904 local child transitions for every source pair through two bits and
  every Boolean child through three bits;
- 65,536 full dynamic-program roots, maximizing the exact signed coherent
  remainder over all adaptive, branch-dependent, nonreusing interleavings and
  optional stopping for every two-bit source pair and every three-bit child.

All Parseval and child-telescope errors were zero in dyadic floating
arithmetic; `max(M-E_raw)=0`; the minimum local and global potential slacks
were zero because of exact endpoint/equality cases.  The largest observed
optimized-remainder/potential ratio was `0.379330711761409`.  These checks
support the proof but do not replace its all-dimensional analytic argument.
No random seed was used.

## Status, review, and next handoff

- Prior claim `B12-A057-UNIFORM-COHERENT-KERNEL-ENVELOPE-v1`:
  **INDEPENDENTLY_ACCEPTED_AT_DECLARED_SCOPE** by B19/A094.
- New claim `B12-A057-CHANGING-WITNESS-POTENTIAL-v1`:
  **PROVED_BY_CONTRIBUTOR_PENDING_INDEPENDENT_REVIEW**.
- A057-D1: **SUBSTANTIALLY ADVANCED**, not complete universally.
- A057-D2: mandatory balance/collision/rare-event controls remain met.
- A057: **OPEN**.
- Full FEI: **OPEN**.

Requested independent reviewers remain A091/A090.  Consumers are A058
(overlap boundary), A059 (depth-uniform decomposition), A097, and B20.
The next concrete calculation should write the simultaneous shared-coordinate
potential drop in terms of `Delta q Delta J` and `Delta V Delta Z`, then test
whether the signed near-collision refund controls those covariance terms on
genuine Boolean two-block overlaps.

## Configuration and delivery facts

The runtime identifies the assistant as Codex based on GPT-5; no exact model
version or reasoning-effort selector is exposed.  No subagent was used.  No
schedule, graph, merge, deployment, email, public release, paid resource,
protected evaluation source, held reroute, or native Brain ingestion was used
or claimed.

