# Source pins

## Current control sources

- Owner overlay revision `2026-10-12.1`, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- `ORDER.md` blob `81b6d6f988aee4489512c6e62543253900620453`.
- `CASE_TARGETS.json` blob `97e41262ebb4f09eec53630a918acae09efc9a48`.
- B12 compact contract blob `40935ac651643a17815d0addf664ec4c1c0313cc`.
- `CURRENT_STATUS.md` blob `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- `OBSTRUCTION_REGISTRY.json` blob
  `e111933338dff1d7798c5e59b43700bbf30f7b96`.

## Exact predecessor evidence

- Canonical predecessor final commit
  `yspennstate/math-open-problems@e5a81561e90069c06ef245e4a2d3ec968713b7c5`,
  `reports/fei-2026-10-11/runs/B12/20261012T074154Z-account01-B12-shared-four-channel/`.
- Brain predecessor mirror final commit
  `yspennstate/math-research-brain@bc3857b1f66c464c4d204fbe9d7d75fce833a3e0`,
  `research_pushes/2026-10-11-full-fei-campaign/handoffs/account01/B12/20261012T074154Z-account01-B12-shared-four-channel/`.
- The present block identity uses the exact definitions and proof in the
  predecessor `SHARED_FOUR_CHANNEL.tex`; no registry label was substituted
  for that proof.

## Freshness check

- Canonical head read before delivery:
  `4727db5e5d42dcff9995aeadc1edb1f3b2fe67cc`.
- Brain head read before delivery:
  `d1c5106393f0cd027309844b8bf29561128eabcc`.
- Comparing the predecessor final commits to those heads showed no changed
  B12 run, B12 assignment, owner overlay, current status, claim registry, or
  obstruction registry.  Intervening canonical changes were other streams;
  intervening Brain changes were other handoffs and inbox metadata.

No protected evaluation source, held PR229/source, refused proof-chain,
REQ-2026100617117951 payload, or held reroute was accessed.
