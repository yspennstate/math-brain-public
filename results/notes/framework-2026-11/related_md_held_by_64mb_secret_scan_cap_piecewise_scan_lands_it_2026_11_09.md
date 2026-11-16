---
name: related_md_held_by_64mb_secret_scan_cap_piecewise_scan_lands_it_2026_11_09
description: "No (9 Nov): RELATED.md sat at its 5 Nov copy online because scan_secrets.py refuses one input over 64 MB (exit 2) and the views log hid the hold; online_memory_push now scans big files in 48 MB overlapping pieces, landed 3741f2b82c"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:02:11+04:00
  status: verified
  evidence: "online_memory_push.log 05:01:39; GraphQL readback oid 13852232e9"
---

Is RELATED.md online current? It was not: from about 5 Nov to 9 Nov it stayed at its 5 Nov copy (50,982,930 bytes online against 80,867,926 here) while online_memory_push logged "views: 0" every five minutes.

Cause: scan_secrets.py reads at most MAX_OBJECT_BYTES = 64 MB of one input and exits 2 ("input exceeds bounded scan size", printed as "SECRET SCAN ERROR: input-1: OSError") on anything larger. scan_ok in online_memory_push.py put RELATED.md in SCAN_HELD on every run, and the views log line carried no scan_held field, so the hold never showed. The GRAPH.md fix earlier the same night (GraphQL blob check) was a different stall; GRAPH.md is 34 MB and passes the scan.

Fix (9 Nov 04:55, an agent): online_memory_push.py scans any file over 48 MB as line-aligned pieces of at most 48 MB, each piece starting with the last 64 KB of lines of the one before, and passes it only if every piece exits 0. The views log line now includes scan_held. The scanner itself is unchanged. Controls (test_scan_big.py): whole-file scan of the live RELATED.md 2, piecewise 0; a pattern-shaped fake token planted at the start, at the end, right after the first cut, and straddling the first cut was refused (1) all four times; no piece files left behind. About 20 s a scan of the 81 MB file, and only when the file differs from origin. Backup: online_memory_push.py.pre_scanbig_20261109.

How to apply: a file that quietly stops updating online while the pusher reports nothing to do is often held by a check whose refusals are not logged. Look for a size cap in the check before blaming the transport. Any other caller of scan_secrets.py on a file over 64 MB (run-folder mirrors, gh_offload, hand pushes) gets the same exit 2. RELATED.md still reaches push_paths_api's 95 MB cap at about 58,600 memories (see [[graph_md_stuck_rest_blob_check_related_md_near_cap_2026_11_09]]); the piecewise scan does not help with that.

Landed: the 05:01:39 daemon run pushed RELATED.md (3741f2b82c); GitHub's blob is 80,867,926 bytes with oid 13852232e9, the same as the local file. A rerun against the promoted code: old scan_ok held it (rc 2), new passed it, new refused a token planted 60 MB in (rc 1).

