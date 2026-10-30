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
  `yspennstate/math-open-problems@3dd5f38ff0768c47b18a5be8b409723a8bb1a9ac`,
  `reports/fei-2026-10-11/runs/B12/20261012T083727Z-fleet01-B12-block-reassociation/`.
- Brain predecessor mirror final commit
  `yspennstate/math-research-brain@2a4f21e2a8df20c9faeeeffbd44576fd2810fac9`,
  `research_pushes/2026-10-11-full-fei-campaign/handoffs/fleet01/B12/20261012T083727Z-fleet01-B12-block-reassociation/`.
- The present channel definitions are taken from the predecessor
  `BLOCK_REASSOCIATION.tex`; the original proof artifact, not a registry
  status label, was used.

## Freshness check

- Canonical head read before packaging:
  `3dd5f38ff0768c47b18a5be8b409723a8bb1a9ac`.
- Brain head read before packaging:
  `8bbad4bf3d4c747b0a0904746682d25391a65b36`.
- The only Brain change after the predecessor mirror was
  `scheduled_tasks/handoffs/brain-inbox/unread/RELAY.json`; no B12 proof,
  assignment, control, claim-registry, or obstruction-registry correction
  intervened.  No canonical change intervened.

## Relevant cross-stream correction consulted before delivery

- B01 compact contract blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- B01/A003 exact KL-by-JS falsifier core commit
  `yspennstate/math-open-problems@59d698866d319542ba55d8215846586b14279ad1`,
  path `reports/fei-2026-10-11/runs/B01/20261012T090930Z-fleet01-B01-kl-js-falsifier-a003/`.
- Original proof `KL_JS_FALSIFIER.tex` blob
  `65ca9eda98e984065237aa7eab1c1f8acf42de2d` and report blob
  `682c6f20648c8b9e0439307e1c9979efe7a6f22a`.
- Applicable correction: an asymmetry KL term cannot be paid with
  coefficient one by ordinary restriction JS; a signed alignment term or
  separate single-use credit is required.  The present collision-credit
  theorem does not use the refuted bridge.

No protected evaluation source, held PR229/source, refused proof-chain,
REQ-2026100617117951 payload, or held reroute was accessed.
