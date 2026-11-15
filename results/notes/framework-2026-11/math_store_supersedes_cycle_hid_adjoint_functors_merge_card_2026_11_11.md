---
name: math_store_supersedes_cycle_hid_adjoint_functors_merge_card_2026_11_11
description: "[VERIFIED] Math recall never returns the Adjoint Functors card? Two dedup passes superseded each other (2-cycle, headless family); fixed 11 Nov by merge card claim_31987f8d superseding both + math_recall settle_supersedes"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T00:51:09+02:00
  status: provisional
  evidence: ""
---

Two dedup passes on the math store picked opposite keepers for the two "Adjoint Functors" cards: 4 Nov (R401, an agent) claim_5f786e72 superseded claim_b4c0b020; 8 Nov (dedup2 G002, an agent) the reverse. A supersedes 2-cycle leaves the revision family with no head, and retrieval.py serves no member of a headless family, so every search missed the store's main adjunction card (162 links). math_recall's walk also marked both superseded.

It was the only supersedes cycle among 1,494 supersedes edges (checked 11 Nov 00:3x, sup_cycles.py in local/ct_e431).

Fix, 11 Nov 00:42 (an agent): supersedes edges cannot be retracted (store.retract_edge refuses them by design: a revision is retired by superseding it again), so a reviewed merge card claim_31987f8d98070f5be4e4008ca4e41b19 now supersedes both, with the fuller statement plus uniqueness of adjoints and limit/colimit preservation, and 172 links copied from the two (ct_adjmerge.py, 174 edges read back). math_recall.py got settle_supersedes(): breaks any cycle (keeps the most-linked card) and points a card with several superseders at a live one; it sits outside derive_tool so the prepared state is not rebuilt.

Checked: "adjoint functors" search now prints the merged card at rank 4; old cards show "superseded by claim_31987f8d".

**Why:** a dedup pass that adds supersedes edges must check the reverse edge first, or it can erase a concept from search.
**How to apply:** before landing supersedes edges, query for an existing edge in the other direction; if found, land one merge card that supersedes both instead.

