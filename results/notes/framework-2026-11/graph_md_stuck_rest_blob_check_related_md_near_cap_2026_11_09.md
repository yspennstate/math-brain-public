---
name: graph_md_stuck_rest_blob_check_related_md_near_cap_2026_11_09
description: "[VERIFIED] Yes, fixed (9 Nov): GRAPH.md past 30 MB stopped reaching GitHub because push_paths_api's existence check downloaded the whole blob by REST; now a GraphQL byteSize query, landed 79d0c40bed. RELATED.md is 80.9 MB and will pass the 95 MB cap within days"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:28:28+04:00
  status: provisional
  evidence: ""
---

Question: why did GRAPH.md stop updating online (online copy 25.4 MB from 5 Nov, local 34.5 MB on 9 Nov)?

online_memory_push.py sends a view over 30 MB by carrier: a git push of a one-file commit to a throwaway branch, then push_paths_api.py (REST) builds the commit on main. Before building it, push_paths_api checked the blob with GET /git/blobs/<sha>, which returns the whole file as base64. For the 34 MB GRAPH.md that read failed, so every run logged 'past the blob API; push its blob by git to a temp branch first' and redid the carrier upload every 5 minutes. GraphQL saw the blob all along (object(oid) byteSize 34461345).

Fix (an agent, 9 Nov 03:59 and 04:1x; backup push_paths_api.py.pre_gqlblob_20261109): blob_size_gql() asks GraphQL for byteSize only, with 4 tries; the REST read runs only when GraphQL cannot answer. Checks that could fail: real blob 34461345, made-up sha 0, wrong repo None. The 04:06 daemon run got past the check but failed 'could not land after 8 tries' while three big release uploads held the uplink (an offload hit a TLS handshake timeout at 04:03); by hand at 04:1x it landed 79d0c40bed in 12.6 s with every blob read back. Mirrors 704a614ed6 and 06d60e0258 in 12_cognitive_architecture/dreaming.

Next to break: RELATED.md is 80.9 MB locally (49,873 memories x 6 neighbor lines of about 247 chars), online 51.0 MB from 5 Nov. push_paths_api refuses over 95 MB and GitHub refuses over 100 MB; at about 1.6 KB a memory that is near 58,600 memories, a few days at the current import rate. Options for whoever owns build_brain_architecture.py: drop the description snippet from neighbor lines (about 40% smaller) or shard the file; check the readers of RELATED.md first.

Related: [[related_md_builder_killed_at_cap_now_a_sparse_product_2026_11_08]] - its 8 Nov full build wrote RELATED.md at 52 MB; [[github_api_drain_was_memory_push_stale_listing_1470_calls_2026_11_08]] - same push daemon.
