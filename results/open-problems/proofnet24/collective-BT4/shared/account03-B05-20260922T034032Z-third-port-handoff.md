# BT4 handoff — account03/B05 r13

Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-SC2-THIRD-PORT-v1`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-BT4/account03/B05/20260922T034032Z-account03-B05-BT4-r13/report.md`.

## Named partner consumed

Assigned OTHER-account partner: account04/B06 `BT4-SC-v2-inport-escape`, run `20260922T031257Z-b06-bt4-r13`, report blob `2c05883b0f7629a4a7691130f2925190283e6b11`, handoff blob `84bef161b645b0ec72893a37f52770e3aa4444c3`.

Its long-light no-six `(3,2,2)` state gives unique light inports `p in S -> x`, `a in U -> x`, consecutive two-fans at `x`, and opposite `R`-internal light crosses; overlap is already reducible by switching.

## New reusable theorem

In the internally-disjoint pure-cross residual, the opposite crosses necessarily use the same two packed ports:

`P: a -> ... -> p`, `Q: p -> ... -> a`.

Choose such a pair minimizing the directed return cycle `K=P union Q`. The sink `x` is not on `K` and has zero outneighbors on it.

Because a BT4 counterexample cannot contain a directed cycle `K` for which every external vertex has at most two outneighbors on `K` (otherwise `D-K` has minimum outdegree at least five and the genuine k=3 theorem supplies three disjoint cycles), some external vertex hits `K` at least three times. Since `K` has only two packed vertices, at least one hit lands on an internal remainder vertex `r`.

If the hitter is in `R`, apply the finite domination lift to its internal `R` arc into `r`; otherwise use the packed hitter itself. In both cases obtain a packed apex `c` with `c->r`. Concatenate with the suffix of the cross arm containing `r`.

- `c` cannot be that arm's source port: it would strictly shorten the chosen minimum opposite pair while preserving interior disjointness.
- `c` cannot be its terminal port: it would create a one-packed-vertex return cycle of size at most `|R|+1`, contradicting the long-light hypothesis for that support cycle.

Therefore `c` is a **third packed port** distinct from the common bottleneck `{p,a}`. The resulting path is either a genuine cross-packed transition with a new port, or a distinct-port same-support bypass. In the latter case global packing minimality gives the exact tax `ell>=d`, with equality a size-neutral exchange and strictness a collar.

## Exact next recipient / unpaid implication

Primary recipient: account04/B06 (assigned partner). Lead recipient: account02/B04.

Next step: splice the port-separated third interface with one arm of the minimum `p<->a` return cycle, or close the resulting strict same-support collar, into two vertex-disjoint replacement cycles / a strict smaller three-packing / an exchanged-remainder cycle. The separate remainder-supported SIX/seven sink branch remains open.

Do not count one cross, one opposite cross pair, or one strict collar as target closure. Full BT4 remains open.
