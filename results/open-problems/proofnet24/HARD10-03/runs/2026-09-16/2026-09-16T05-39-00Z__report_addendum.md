# HARD10-03 — append-only receipt / readback correction / certificate addendum

The full `d=3` conjecture remains **OPEN / PARTIAL**. This file does not overwrite the main checkpoint; it records exact delivery receipts, a readback typo correction, one scope clarification, and the finite-state certificate for the deterministic pivotal-edge lemma used in `NEW-L58`.

## 1. Main checkpoint receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T05-23-30Z__report.md`

Create-file commit:

`e5f528d7a4c350f538e8fa8682111b2591382eed`

Exact-commit readback blob:

`029445d5c41b5c89e6d582bf40386b93284c90e6`

The report was fetched back using the exact commit ref, including the `NEW-L58`--`NEW-L60` sections. Delivery status: **VERIFIED**.

## 2. Readback correction to equation (5.2)

One LaTeX escape in the immutable main report was serialized incorrectly. In equation `(5.2)`, the fragment displayed on readback as

`- rac1{6T}`

must be read as the ordinary term

\[
-\frac{1}{6T}.
\]

Thus the intended and mathematically used equation is

\[
\boxed{
f_M(t)
\ge
\frac12-\frac1{6T}-B_Mt^{-3/2}-K_MTt^{-3/2}.
}
\tag{A.1}
\]

The subsequent choice `T=t^{3/4}` and `NEW-L60` use (A.1). This is a text-serialization correction only; it does not change the argument.

## 3. Scope clarification for the drift discussion

The sentence in Section 7 of the main report saying that the long sector “supports the drift ... at every large time” should be read in the following precise form:

* `NEW-L60` gives pointwise-in-time long-cycle mass at every sufficiently large time;
* `NEW-L56` constrains the **time average** of the same-cycle edge mass on every interval;
* because fixed short cycles have pointwise probability `O_M(t^{-3/2})`, the same-cycle edge mass required by `NEW-L56` on a large-time interval cannot be supplied by fixed-short cycles, so the required **interval-averaged** drift contribution must come from the long finite/macroscopic sector.

No pointwise lower bound on the same-cycle edge probability `a(t)` is claimed.

## 4. Exact cut-endpoint lemma behind (3.3)

For completeness, the transposition/cycle convention can be checked algebraically. Suppose a finite cycle of `sigma` is written

\[
(u,a_1,\ldots,a_p,v,b_1,\ldots,b_q).
\]

For left multiplication by `tau=(u\ v)`, only the two arrows whose images are `u` and `v` are changed, and

\[
\tau\sigma
\]

splits this cycle into

\[
(u,a_1,\ldots,a_p)
\qquad\text{and}\qquad
(v,b_1,\ldots,b_q).
\]

If the new component containing the root has size at most `M`, and the root is `sigma^k u` inside the first displayed arc, then

\[
u=\sigma^{-k}0,
\qquad
v=\sigma^{p+1-k}0,
\]

with both cyclic exponents having absolute value at most `M`. The second arc is identical after interchanging `u,v`. Thus every long-to-short pivotal edge has both endpoints in the finite orbit window used in (3.3); the main report's `M+1` padding is conservative.

The same conclusion holds under the opposite composition convention after swapping incoming/outgoing descriptions.

## 5. Finite-state pivotal checker

Checker path:

`proofnet24/HARD10-03/artifacts/2026-09-16T05-31-00Z__short_cycle_pivotal_check.py`

Commit:

`5c16880cde20619df879a9d19d483faf2eb7e542`

Exact readback blob:

`48722b41d642a6d2e5353407fba2d138ca06b867`

Delivery status: **VERIFIED**.

The checker exhaustively enumerates every permutation on `C4`, `C5`, and `C6`, all `M<=min(3,n-1)`, and every graph-edge transposition. It verifies:

1. on `L<=M`, the number of pivotal edges is at most `deg*M` (here `2M`);
2. on `L>M`, every pivotal edge has both endpoints inside the two-sided orbit window `{-M-1,...,M+1}`.

This is only a finite-state sanity check; the analytic proof is in the report and in Section 4 above.

## 6. Executed checker output

Executed output path:

`proofnet24/HARD10-03/artifacts/2026-09-16T05-31-00Z__short_cycle_pivotal_check_output.json`

Commit:

`8a40be1f36ea94dd94202dd57969c1c65a5729c1`

Exact readback blob:

`9f048bb0812a450e44ee72c7e8d981533cf3be07`

Delivery status: **VERIFIED**.

The output records `pass: true`, with no failures across

* `72` permutation/cutoff cases on `C4`,
* `360` cases on `C5`,
* `2160` cases on `C6`.

The maximum numbers of pivotal edges observed for `M=1,2,3` were respectively `(2,4,4)` on `C4`, `(2,4,5)` on `C5`, and `(2,4,6)` on `C6`.

The first attempt to create the output JSON encountered an ordinary GitHub contents-API `409` branch-head conflict because `master` advanced concurrently. In accordance with the run rule, it was retried exactly once and the retry succeeded at the commit above. No approval/security denial occurred.

## 7. Final status

The new mathematical result remains:

\[
\forall M<\infty:\qquad
\mathbb P(L_t(0)>M)
\ge
\frac12-C_Mt^{-3/4},
\]

and hence there exists a deterministic `M_*(t)->infinity` such that

\[
\mathbb P(L_t(0)>M_*(t))\ge\frac12-o(1)
\]

for **every sufficiently large prescribed time** `t`.

This does not exchange the limits `M->infinity` and `t->infinity`, so it is not a proof of an infinite cycle at any fixed finite time. No independent human or formal verification is claimed. No prior/peer file, workflow, setting, permission, email, Drive file, public resource, or third-party channel was modified.