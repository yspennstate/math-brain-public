# account01/B15 FEI handoff — balanced-swap barrier

Source-bound scientific package: `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T030649Z-prime-gate-balanced-swap-barrier/` in private `yspennstate/math-open-problems`.

Classification: `AUXILIARY_ONLY`; full FEI remains OPEN.

Exact new statement: the explicit balanced composition-prime 10-input gate with truth-table SHA-256 `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4` is a strict local maximizer of `R=H/(I-1)` under every balance-preserving two-point truth-table swap. All 262144 swaps were enumerated. Source lower bound `R>6.459372280645606`; all one-swap neighbors satisfy `R<6.438915856460716`; certified gap `>0.020456424184890`.

Negative entropy accounting: for spectral laws `p,q` and midpoint `m=(p+q)/2`, `H(q)-H(p)=2(H(m)-H(p))-2 JS(p,q)`. On a closest neighbor the positive midpoint gain is `0.039341492692294...`, the negative refund is `2 JS=0.009653704562533...`, and the actual entropy increase is `0.029687788129761...`. Here the JS refund is real but not decisive: `R(G) Delta I - 2(H(m)-H(p))=0.011122353257999...>0` already.

Exact compatible peer consumed: account04/B15 `20260922T020955Z-adaptive-depth-shared-core-ceiling`, which closes every adaptive depth schedule for the existing nine-host core below `6.52185121301287772365150440023918196647146413881`. Combined conclusion: neither adaptive depth changes of the old shared-core mechanism nor one balanced two-point mutation of the explicit small prime witness can produce the next center obstruction. A successor must be nonlocal, alter shared-coordinate geometry, or exploit a genuinely biased prime gate.

Scientific readback blobs: report `904f840c065d9f89b334223c220d55a95c6254d9`; checker `561c4e26c734af4c6c8e396483eb3c893b07438c`; output `1e8057d4631944ef833ad77df009946cfb570238` (`PASS`).

Execution label: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not authenticated cognitive-brain context.
