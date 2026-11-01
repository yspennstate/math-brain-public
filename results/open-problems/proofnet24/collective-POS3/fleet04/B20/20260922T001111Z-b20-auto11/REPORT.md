# POS3 fleet04/B20 — adjacent-swap control for exact insertion weights

**Run:** `20260922T001111Z-b20-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has a `1/3–2/3` balanced incomparable pair under the uniform law on linear extensions.  
**Parent status after this report:** **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Peer result actually consumed

This run uses the completed other-account result

`proofnet24/collective-POS3/fleet01/B19/B19-20260921T235148Z-pos3-r01/REPORT.md`

whose exact chain-deletion theorem writes, for a deleted chain `C` and `tau in L(Q)`, the number of lifts of `tau` as a corridor multiplicity `W_C(tau)`.  That report also disproves both the uniform-deletion shortcut and any universal bounded-density rescue, and isolates the next problem as a weighted balance transfer using the corridor structure itself.

The present run attacks one of the mechanisms named there: **local adjacent-swap identities for the insertion multiplicity**.  The first result below is exact, universal, and proved rather than inferred from computation.

## 2. Setup: delete one element

Let `P` be any finite poset, fix `c in P`, and put `Q=P\{c}`.  For a linear extension

`tau=(q_1,...,q_n) in L(Q)`

define

`a(tau)=max({pos_tau(q): q<c} union {0})`,

`b(tau)=min({pos_tau(q)-1: c<q} union {n})`.

Then the fleet01/B19 fiber theorem specializes to

`W(tau)=b(tau)-a(tau)+1`,

where `W(tau)` is exactly the number of legal gaps in `tau` into which `c` can be inserted.  The restriction of the uniform law on `L(P)` to `L(Q)` is proportional to `W`.

Classify each `q in Q` relative to `c` as

- `L` if `q<c`,
- `R` if `c<q`,
- `I` if `q || c`.

## 3. Adjacent-swap theorem

### Theorem 3.1 — one-boundary-gap law

Let

`tau = (...,u,v,...) in L(Q)`

with `u || v` in `Q`, and let `tau'` be obtained by swapping this adjacent incomparable pair.  Then the legal insertion-gap intervals

`I(tau)={a(tau),...,b(tau)}` and `I(tau')={a(tau'),...,b(tau')}`

are nested and differ by at most one boundary gap.  Consequently

`|W(tau')-W(tau)| <= 1`.

More precisely, if `u,v` occupy positions `r,r+1` in `tau`, then the only nonzero cases are:

1. `u<c`, `v||c`, and `a(tau)=r`: then `a(tau')=r+1` and `W(tau')=W(tau)-1`.
2. `u||c`, `v<c`, and `a(tau)=r+1`: then `a(tau')=r` and `W(tau')=W(tau)+1`.
3. `c<u`, `v||c`, and `b(tau)=r-1`: then `b(tau')=r` and `W(tau')=W(tau)+1`.
4. `u||c`, `c<v`, and `b(tau)=r`: then `b(tau')=r-1` and `W(tau')=W(tau)-1`.

In every other case `W(tau')=W(tau)`.

### Proof

Because `u` and `v` are adjacent and incomparable in `Q`, swapping them preserves the linear-extension property.  Only their two positions can affect the last predecessor of `c` or the first successor of `c`.

If both elements lie in the same class `L`, `R`, or `I`, the set of occupied predecessor positions and the set of occupied successor positions have the same extrema before and after the swap, so both `a` and `b` are unchanged.

A predecessor/successor pair cannot occur: if `u<c<v`, then transitivity gives `u<v`; if `v<c<u`, then transitivity gives `v<u`, contradicting `u||v`.

Thus the only mixed possibilities are `L/I` or `R/I`.  For `L/I`, moving the predecessor one step right changes `a` only when it is the last predecessor; it then raises `a` from `r` to `r+1`, deleting exactly the left boundary gap.  Moving it one step left has the inverse effect.  The successor boundary `b` cannot change in these cases.  The `R/I` cases are symmetric: moving the first successor one step right raises `b` by one, adding exactly the right boundary gap, and the inverse swap deletes it.  No other boundary changes.

Hence the two insertion-gap intervals are nested with symmetric difference of size at most one, proving the theorem.  `□`

## 4. Fiber-level injection, not merely a count inequality

The theorem gives a canonical lift injection across every adjacent swap.  If `I(tau)` is the smaller interval, send the lift `(tau,s)` to `(tau',s)` using the identical insertion gap `s`; feasibility is preserved because the smaller interval is contained in the larger.  If the fiber sizes differ, the larger fiber has **exactly one unmatched lift**, corresponding to the single added boundary gap.

Thus a local adjacent-swap argument in `Q` survives insertion of `c` with a completely explicit defect: zero or one full linear extension, never an uncontrolled multiplicity factor.

This is materially stronger than the false bounded-density route ruled out by fleet01/B19: globally `max W/min W` can be arbitrarily large, but **each legal adjacent swap changes the exact fiber multiplicity by at most one**.

## 5. Path and pairing consequences

Let `d(tau,sigma)` denote adjacent-incomparable-swap distance in the linear-extension graph of `Q`.  Repeated application of Theorem 3.1 gives

`|W(tau)-W(sigma)| <= d(tau,sigma)`.

Therefore, for any involutive pairing `Phi` between two extension classes (for example opposite orders of a candidate incomparable pair), if

`d(tau,Phi(tau)) <= min(W(tau),W(Phi(tau)))`

for every paired `tau`, then

`max(W(tau),W(Phi(tau))) <= 2 min(W(tau),W(Phi(tau)))`.

Summing pairwise implies that the two total weighted masses have ratio between `1/2` and `2`, hence the corresponding order probability lies in `[1/3,2/3]`.

This gives a concrete sufficient condition for a width-two reflection/exchange proof to lift through one deleted element: it is enough to construct a pairing whose swap distance is paid by the smaller insertion multiplicity.  No Radon–Nikodym bound over all extensions is required.

### Proof of the pairing criterion

The path inequality gives

`|W-W'| <= d <= min(W,W')`.

If, say, `W>=W'`, then `W-W'<=W'`, so `W<=2W'`.  The reverse case is identical.  Pairwise summation preserves the same factor-two comparison, which is equivalent to a probability in `[1/3,2/3]`.  `□`

## 6. Deterministic regression check

The companion script `verify_adjacent_swap.py` exhausts all `2^10=1024` forward-edge-generated five-point posets on labels `0,...,4`, takes `c=2`, enumerates every linear extension of `Q=P\{c}`, and checks every swappable adjacent incomparable pair.

Observed output:

`PASS checked=7506 nonzero=3804`

Across all 7,506 tested swap instances it verified the exact case formula, `|Delta W|<=1`, nested legal-gap intervals, and symmetric difference at most one.  This is regression evidence only; Theorem 3.1 is proved above.

## 7. What remains unpaid

This does **not** prove POS3, nor even the full weighted-balance transfer for a one-element third chain.  The remaining mathematical obligation is now sharper:

> Construct, for a source-valid width-two remainder and a strategically chosen candidate incomparable pair, a global reflection/injection whose aggregate path cost is controlled by the exact insertion multiplicities, or replace this route by another mechanism if such control fails.

The local multiplicity obstruction itself is no longer mysterious: each adjacent swap costs at most one lift.  The unresolved issue is whether the width-two path/reflection structure supplies enough total multiplicity to pay the cumulative swap distance while retaining a pair-order reversal.

For a deleted chain of length greater than one, an additional generalization is needed: characterize the boundary-vector defect of the full monotone corridor `W_C(tau)` under an adjacent swap.  Nothing here claims that the one-element `1`-Lipschitz bound remains true for arbitrary chain length.

## 8. Claim status

- Exact one-element adjacent-swap nested-fiber theorem: **PROVED**.
- Exact local defect `|Delta W|<=1`: **PROVED**.
- Canonical injection between neighboring lift fibers with at most one unmatched lift: **PROVED**.
- Swap-path Lipschitz inequality: **PROVED**.
- Factor-two weighted pairing criterion under the stated path-budget hypothesis: **PROVED**.
- Existence of such a global pairing for every width-three poset: **OPEN**.
- POS3 parent target: **OPEN**.
