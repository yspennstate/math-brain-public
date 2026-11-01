# HARD10-03 — delivery / finite-state certificate addendum

This append-only addendum records delivery receipts and the finite-state sanity check for

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T04-41-30Z__report.md`.

The full `d=3` conjecture remains **OPEN / PARTIAL**. No result here is promoted to a full proof.

## 1. Main mathematical checkpoint receipt

Path:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T04-41-30Z__report.md`

Commit:

`03f8959e6c7ab8ac8a39f0f8696472d2f7c90caa`

Blob from the exact commit record:

`9dfca3ea7475425c58eb98137c3f78d59b06a799`

The file was fetched back using that exact commit ref after creation. Delivery status: **VERIFIED**.

## 2. Finite-state checker

A self-contained finite-state checker for `NEW-L56` was archived at

`proofnet24/HARD10-03/artifacts/2026-09-16T04-45-00Z__cycle_drift_check.py`

Commit:

`cd5809823a74cff7be2a62f045ebaad47adfe239`

Exact readback blob:

`4631d4ed40d5160bbf6bbdfd523e8b52a2ef60ac`

Delivery status: **VERIFIED**.

The checker enumerates all `5! = 120` permutations on the cycle graph `C5`, constructs the exact continuous-time interchange generator, and compares

\[
\frac d{dt}\frac{\mathbb E C_t}{|V|}
\]

with

\[
\frac{|E|}{|V|}\,[2\mathbb P(e\text{ has same-cycle endpoints})-1]
\]

at three times. This is only a finite-state sanity check; the report contains the analytic generator proof valid on the cubic tori.

## 3. Executed checker output

Executed JSON output is archived at

`proofnet24/HARD10-03/artifacts/2026-09-16T04-45-00Z__cycle_drift_check_output.json`

Commit:

`fb9b8b5b97d5f3cef404a686fe88a8e65e568e5e`

Exact readback blob:

`7fb668ee883041d2553316727393fe3ba6155789`

Delivery status: **VERIFIED**.

The maximum absolute discrepancy in the drift identity was

\[
3.2057689836051395\times10^{-15},
\]

and the checker returned `pass_tolerance_1e-12 = true`.

The three tested times were `0.1`, `0.7`, and `2.0`; the corresponding same-cycle edge probabilities were approximately

\[
0.09043673605,\qquad
0.36895316305,\qquad
0.48340892164.
\]

## 4. Status / failures / scope

No GitHub approval or security denial occurred in this run. No prior or peer file was modified or overwritten. No repository settings, workflows, permissions, public posting, third-party contact, Gmail, email, Google Drive, or paid compute were used.

The finite-state checker does not independently certify `NEW-L57`; that theorem rests on the exact finite-torus drift identity, fixed-`r` endpoint estimates already archived, and fixed-finite-orbit torus-to-lattice convergence. The report keeps the distinction between a diverging finite scale `M(beta)` and an actually infinite cycle explicit.
