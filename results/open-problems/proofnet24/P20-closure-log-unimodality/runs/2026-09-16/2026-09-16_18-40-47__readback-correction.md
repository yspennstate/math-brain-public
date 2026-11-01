Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime/scheduler exposes no model selector or reasoning-effort selector; I do not claim otherwise.

# P20 immutable readback correction / receipt — 2026-09-16 18:40:47 run

Canonical immutable report:

`proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_18-40-47__run-report.md`

Creation commit:

`9fa714dbddadb44c6fb837688d1ce69d525fb7fe`

Verified report blob:

`f138c86333ee2b3d70bb49402bac54ab5b469bb8`.

I read the report back from that exact creation commit in contiguous ranges through the terminal status line.

One notation-only serialization defect was found in equation (3.2). The immutable report displays the first density term as

```text
rac{1}{24x}{\bf 1}_{[e^{-8},e^8]}(x)\,dx
```

where the intended LaTeX command is

```text
\frac{1}{24x}{\bf 1}_{[e^{-8},e^8]}(x)\,dx.
```

Thus the corrected equation (3.2) is

\[
\mu(dx)=
\frac{1}{24x}{\bf 1}_{[e^{-8},e^8]}(x)\,dx
+\frac{1}{36x}{\bf 1}_{[e^{-14},e^{-8})\cup(e^8,e^{14}]}(x)\,dx.
\tag{3.2 corrected}
\]

This is a notation/transport defect only. The immediately following exact normalization `16/24 + 12/36 = 1`, the archived transform code, and the interval checker all use the intended coefficient `1/24`. No mathematical claim, derivative enclosure, mode count, or status changes.

No other truncation, UTF-8 corruption, theorem-status mismatch, or proof-changing serialization defect was found in the full readback.

Artifacts independently read back:

- checker script creation commit `e75cc2f42846630e091fcf60f1d6bbd8bf695c13`, blob `34108099ad23b659bcf773a8f401af57bc8da196`;
- executed output creation commit `a173b871e6f901f9c9a8542f828e27902521b636`, blob `bf535faa733dbfe1d2d669d4f75b6ef26e67dc79`.

The executed output ends with `ALL_INTERVAL_CHECKS_PASS` and the certified sign pattern `gprime(6)>0, gprime(10)<0, gprime(20)>0, gprime(22)<0`.

Terminal readback status: **report preserved immutably; equation (3.2) corrected only by this separate receipt; P20-I0081 source statement REFUTED; tracked metric 2 -> 4; campaign closure still OPEN at 0/2 complete OTHER audits.**
