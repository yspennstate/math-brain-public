# HARD10-03 delivery receipt and post-write scope check

Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum. The scheduler exposes no model selector or reasoning-effort selector, so the requested GPT-6 / maximum setting cannot be claimed.

This receipt is append-only. It does not modify the mathematical report, shared ledgers, or peer/history files.

## Main report

Path:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T15-21-39Z__report.md`

Creation commit:

`11c04fa9c12e68725a530dd854f8fdaed4872d41`

Exact-create-commit readback blob:

`0872666ffe27a9fd824cea5e5b572dd502fc8c25`

Delivery status: **VERIFIED**.

### Immutable typo correction

In the first metric display of the immutable main report, the optimizer symbol was serialized once as `\nu_*`. The proof and every subsequent optimizer equation use `u_*`; the intended symbol is

\[
u_*=(\sqrt{1+16e}-1)/2.
\]

No mathematical formula or value changes. The original report is not overwritten.

## Exact checker

Path:

`proofnet24/HARD10-03/artifacts/2026-09-16T15-21-39Z__mgf_cut_check.py`

Creation commit:

`e4016308bc1fa93133207dc6fd42c8336f75e55e`

Exact-create-commit readback blob:

`abe9cb781750a07aef37cb40f9d98982e3fe9b7a`

Delivery status: **VERIFIED**.

The checker was executed before upload. It uses exact rational/integer arithmetic to certify the literal exponent and the finite tree identity checks; its finite enumeration is a self-check, not the theorem proof.

## Executed checker output

Path:

`proofnet24/HARD10-03/artifacts/2026-09-16T15-21-39Z__mgf_cut_check.out`

Creation commit:

`348054f8edccf225950f46fe9571235e2594b10c`

Exact-create-commit readback blob:

`49f84acce69c780927b528b2839fc4fa2e0e4e0e`

Delivery status: **VERIFIED**.

The output ends with the certified facts:

- `epsilon_cert = 590451719447/1250000000000`;
- `epsilon_cert_decimal = 0.4723613755576`;
- rigorous log gap positive;
- optimizer bracket `[2.8351352, 2.8351353]`;
- `1441` labelled-tree identity cases passed for `2<=k<=6`;
- `epsilon_cert > 59/125`;
- the conditional `L=10^214` Peierls-scale arithmetic check passed.

## Task-local ledger delta

Path:

`proofnet24/HARD10-03/artifacts/2026-09-16T15-21-39Z__ledger_delta.yaml`

Creation commit:

`3356deddbe32acda9298a407154e451e40ac10fc`

Exact-create-commit readback blob:

`a97d4a7a14925e818ab6a19e70f8132551c2fd16`

Delivery status: **VERIFIED**.

## Post-write mathematical scope check

1. The source Tóth/Ioffe–Tóth `d=3` conjecture is still **OPEN**. The run is **PARTIAL**.
2. The fixed fleet metric moved from `203/500=0.406` to the exact optimized fair-cut MGF exponent
   \[
   \epsilon_{\rm MGF}
   =\frac{\log((1+u_*)/2)-(u_*-1)/(2u_*)}{\log2}
   =0.4723613755576205\ldots,
   \]
   with literal exact-rational certificate `590451719447/1250000000000`.
3. The new exponent applies only to the frozen deterministic connected-block visitation/leakage event under the same cross-heat condition `H_beta <= (k-1)/(4e)`. It is not a physical cube orbit-propagation theorem; that physical exponent remains `UNMEASURED`.
4. `NEW-L98` stays inside the valid one-color symmetric-exclusion/negative-association observable. It does not use the label-specific total-order observable that C27 refuted on `P3`.
5. The archived `q0=5408^-27` Peierls criterion remains a conditional gate. The new arithmetic statement `L=10^214` assumes a future genuinely local 2-dependent physical bad-block event with constant `C=1` dominated by the certified polynomial exponent; that domination has **not** been proved.
6. No chronological tagged-particle path is identified with a permutation cycle, and no monotonicity in `beta` is assumed.
7. Hammond and Björnberg–Ueltschi tree methods are used only as methodological references. Their unique-path/descendant-subtree/root-recursion hypotheses are not imported to `Z^3`.
8. The source-matching finite-box macroscopic-cycle theorem and the fully justified infinite-volume passage remain outstanding. C27's fixed-`K` torus theorem is still mesoscopic rather than macroscopic.
9. Closure audits are absent: P26 full-proof audit **MISSING**; second distinct qualified-task full-proof audit **MISSING**.

No transient write retry was required. No permission, approval, security, or usage denial occurred; approval requirement: **NOT EXPOSED**. No Gmail/email, Google Drive, public posting, paid compute, extra schedule creation, force-push, access/settings/workflow changes, credential inspection, shared-ledger edit, or peer/history-file edit was performed.
