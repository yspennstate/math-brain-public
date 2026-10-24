# P0297 referee packet (2026-10-10)

Target: [Gwynne--Miller, Problem 7.1](https://link.springer.com/article/10.1007/s00222-020-00991-6): compute the deterministic Hausdorff dimension d_gamma of (C,D_h) for each gamma in (0,2). The case gamma=sqrt(8/3) has d_gamma=4. The [2026 Rhodes--Vargas ICM survey](https://epubs.siam.org/doi/10.1137/25M1803632) still calls the general dimension an open problem.

## Saved verdicts

- w517-P0297-S0: **KEEP as dated source status only.** Reproduction: ranking CSV line 554 exactly gives tier 5, P0297, title, unsolved. Remaining gap at this checkpoint: primary statement and current openness; those are now separately sourced in SOURCE_STATUS.json.
- w516.P0297.C00: **FIX source attribution.** The dated statement is true and reproduced by ranking CSV line 554, but its row cites only the task brief and says local row verification is pending. Replace source with the CSV row and remove that pending assumption. No mathematical claim is yet audited.

These verdicts cover only the two saved source-status rows available at this point. A KEEP here is not a proof of P0297.

## Mathematical verdicts

The eleven section-level KEEP verdicts, exact scopes, independent reproductions, and open inputs are in VERDICTS.jsonl. I checked the author derivations themselves, including the finite-Gaussian differentiation, path-switching sign, mean/median passage, Stieltjes limit, weighted near-tie density, and three-route competitor factor. Independent two-edge quadrature: `python -X utf8 ~/brain_workers/w518/review_repro.py`, maximum displayed IBP discrepancy 2.22e-15 for beta=2,10,50,250 at xi=0.7; the finite-beta response approaches -1/sqrt(pi), with error 1.51511e-5 at beta=250.

The hardest open input remains H: evaluate the actual GFF LFPP optimized-crossing exponent, equivalently the limiting response-measure masses. w516 L6 and w517 NT assume weighted gap density regularity at fixed finite cutoff. w517 3R proves that an isolated pair loses a factor equal to its probability of beating the third route at the tie. No cutoff-uniform multi-route estimate is supplied. **Neither peer packet proves P0297.**

My separate snowflake covariance obstruction is in ATTEMPT.md and CLAIMS.jsonl as a proved elementary model independently KEPT by w521. It refutes an inference from constant-shift covariance alone, and is not an LQG metric because p<1 snowflakes are not length metrics. w520 produced an overlapping snowflake result, so mine remains a corroborating row rather than a second brain card.

## Prior-attempt correction (high priority for brain)

The owner-campaign row D0049-A001 in `probability_1000_intake_D_20260908/attempts.jsonl:43` says: `d_gamma = 2Q/xi with Q = 2/gamma + gamma/2`. This is algebraically false. The [primary metric introduction, equations (2.2) and (2.5)](https://arxiv.org/html/2109.01252v2) gives `xi=gamma/d_gamma` and `Q=2/gamma+gamma/2`, so `d_gamma=gamma/xi`. At gamma=sqrt(8/3), the known d=4 gives xi=1/sqrt(6) and Q=5/sqrt(6); the old `2Q/xi` evaluates to 10, a direct contradiction. CLAIMS.jsonl row w518.P0297.C2 records the exact source quote and correction. The historical attempt file is read-only; the proposed brain bundle should carry a linked correction without silently rewriting provenance.

w521 independently KEPT C2. w519 separately found the same two incorrect formula occurrences and already submitted a correction card and source-row patch. Use w519's landing, backed by C2 as an independent check; my `bundle_002.part` is held to avoid duplicating that card.

Cross-triad boundary: w516's finite response and w517's three-route factor refute the isolated-pair shortcut H0 in ATTEMPT.md. w519's correction and w520's snowflake example overlap my C2/C1, so neither of my matching cards was submitted. All eleven mathematical verdicts can be used to update the peers' submitted drafts after their stale review-state wording is fixed; BUNDLE_VERDICTS.jsonl records those file-level FIX rows.
