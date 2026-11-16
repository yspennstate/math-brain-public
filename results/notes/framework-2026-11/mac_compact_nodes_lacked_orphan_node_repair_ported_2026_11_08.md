---
name: mac_compact_nodes_lacked_orphan_node_repair_ported_2026_11_08
description: "[VERIFIED] Yes until 8 Nov 02:01: the second machine's compact_nodes lacked origin's ensure_orphan_nodes, so a node cut off before its INDEX row stayed unseen; 0 of 991 orphaned live; fixture old fails, new repairs"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:01:26+04:00
  status: verified
  evidence: "fixture cn_fixture.py old: orphan repaired False; new: True with backfilled tag; live 991 files = 991 INDEX names; hooks 88/88; mirror 7cc3270e93"
---

Could a compaction node cut off before its INDEX row stay invisible on the second machine? Yes, until 8 Nov 02:01. Origin's ensure_orphan_nodes (3 Nov, after an agent found 3 of 1,137 nodes on the workstation orphaned by a second compaction 54-97 s after the first) never reached the second machine's compact_nodes.py. save_node writes the node, then the anchor, then the row. A hook killed between those steps leaves a node file that ensure_anchors can't see, because it walks INDEX rows only, so recall and the graph never reach that compaction.

Measured on the second machine: 991 node files and 991 INDEX names, 0 orphans, including through the 7 Nov 23:07 power loss. So nothing was lost yet.

Port (an agent): origin's function, inserted after ensure_anchors, plus its call after the PostCompact print, wrapped so a repair can never fail the hook. The rest of the second machine file is unchanged. write_anchor and ensure_anchors are byte-equal in the two copies, so the function's calls match. In a fixture in a temp COMPACT_NODES_ROOT (two nodes, one stripped to node file only and backdated 15 minutes, then a third PostCompact through main), the old file leaves the orphan, and the new one writes its row (backfilled: ensure_orphan_nodes) and its anchor. The live dry pass over two days costs 4 ms. Hooks 88/88. Backup compact_nodes.py.pre_orphans_20261108. Mirror 7cc3270e93.

How to apply: a crash-cut repair is worth porting even when the live count is 0, because the count can only show damage that has already happened. Prove it with a fixture that recreates the cut. Related: [[mac_schema_supersede_lacked_partial_guard_ported_2026_11_08]], [[mac_crash_7nov_2303_power_loss_not_panic_2026_11_08]].

