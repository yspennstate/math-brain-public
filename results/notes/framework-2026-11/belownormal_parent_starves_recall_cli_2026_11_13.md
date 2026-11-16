---
name: belownormal_parent_starves_recall_cli_2026_11_13
description: "Recall CLI takes 10+ minutes but the server log says 5 s? [VERIFIED 13 Nov] A hidden BelowNormal parent on a saturated box starves the client in interpreter startup before it connects; run the caller at Normal"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T02:42:45+02:00
  status: verified
  evidence: brain_recall_server/calls.jsonl + client.jsonl 13 Nov 01:44-02:45; prf_cli.log; repro46.py
  modified: 2026-11-13T00:43:50.394Z
---

**What was seen (13 Nov 2026, an agent).** A batch test (prf_cli.py, launched hidden at BelowNormal by a VBS) calls
`brain.py recall "<q>"` once per question. With the workstation at 87 pct CPU and physical memory critical, single calls took
649.6 s, 863.8 s, 806.0 s and 486.6 s. The recall server's own row for each of those calls says about 5 s
(calls.jsonl `ms` 5301), and the client's `served` note lands only at the very end. The same question run from an
interactive shell at Normal priority: 5.7 s, served.

**Why.** The client process inherits its parent's BelowNormal class. When Normal and AboveNormal threads fill every core, a
BelowNormal process gets almost no CPU, and it is still in Python startup (site, sitecustomize, the brain.py prelude)
when it should be sending the request. The server is AboveNormal and fast; the time is all in the client before connect.
It is not the question: the slow q046 had 31 tokens.

**How to tell.** A recall that is slow at the caller but fast in calls.jsonl (same minute, same session) is the caller
starving, not recall. Compare the caller's wall time with the server row's `ms` before profiling recall.

**What to do.** Run a batch that calls recall at Normal priority (the recall itself runs in the server, so the caller costs
almost nothing), or call the server in process (brain_recall_client.run) instead of spawning a Python per question.
Raising your own test process with `(Get-Process -Id <pid>).PriorityClass='Normal'` makes later children Normal too.
Not a reason to raise other agents' renders: the 18 Sep law stands.

**What also made it worse, and was mine.** I had stacked three T104 GPU searches without sizing them (4.5-6.7 GB host RAM
each, 17.7 GB together), which put the box at physical-memory critical in the same window. See
[[never_starve_a_shared_computer_size_memory_before_you_queue_2026_09_06]] and
[[a_belownormal_render_stalls_on_ecoqos_opt_out_keeps_the_priority_2026_09_24]].

Found while measuring the served lex stage; the lex memo that landed the same hour is in brain.py (ONE SCAN PER QUERY).


Consolidated 13 Nov 2026 (SWS dream) with five sibling cases into [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]] - the one mechanism under all of them.
