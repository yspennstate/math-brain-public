# C04.36 — clarification of the distributed-revisitation branch

This immutable addendum clarifies one interpretation sentence in

`runs/2026-09-20/2026-09-20T144000Z__report.md`.

Theorem C04.35 itself is unchanged. In its proof a coarse bin is declared **search-heavy** when it contains more than `A` skeleton starts before the wrong exit. That property is determined by the stopped path alone and is exactly what is required for the posterior-conditioning argument.

Therefore Branch S in Section 7 should conservatively be read as

> **distributed revisitation:** `Omega(L/N)` pairwise separated directional bins each contain more than `A` skeleton starts before the wrong exit.

The phrase “before a bad start needed by the corridor is found” was stronger than what was actually proved and should not be used downstream. A bad start may occur early and the same bin may then be revisited many times. The proved conclusion is still useful: the residual trajectory must distribute repeated skeleton occupation across linearly many separated directional bands, rather than obtaining the whole residual cost from one localized trap.

This clarification does not change any displayed inequality, the conditional-independence proof, the posterior-information branch, the actual-span erasure theorem, or the fixed status

`FULL_SOURCE_IMPLICATION: 0 -> 0`.
