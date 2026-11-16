---
name: house_rule_a_write_to_a_file_others_write_takes_a_mesh_claim_2026_11_09
description: "Writing or appending to a file other agents or jobs also write (shared STATUS.md, queue, registry JSON, board, shared log, MEMORY.md)? agent_mesh.py claim --resource file:<path> --mode write first, gate the write on its exit code (3 = held), release after; a flock is not enough"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T07:58:52+04:00
  status: house-rule
  evidence: "global CLAUDE.md mesh order; LIVE2 5/5 brain runs missed it"
---

Writing to a file other agents or jobs also write: a shared STATUS.md, a queue, a registry or index JSON, a board, a log several scripts append to, MEMORY.md, anything under brain or the shared repos. Before the write, take a mesh claim and let its exit code gate the write; release after:

    python3 agent_mesh.py claim --agent <id> --resource file:<path> --purpose "<why>" --mode write && <the write>
    python3 agent_mesh.py release --agent <id> --resource file:<path>

Exit code 3 means another agent holds it: stop, do not write around it. A script that does the write needs the claim inside the script, not only in the session that ran it. A file lock (flock, mkdir lock) guards one machine's processes; the mesh claim is how agents on this machine see each other, so use it even when a lock is also there. Run `hello` first if the agent is not live ([[a_mesh_claim_from_a_lapsed_agent_returns_rc3_like_a_conflict_2026_10_18]]).

A standing house rule (global CLAUDE.md): "Before ANY mutation of shared state (files, git, memories, deployments, external systems), acquire the narrowest write or exclusive claim." Why this card exists: in LIVE2 (9 Nov) five Codex runs with the brain were asked for a script that appends to a shared status file, searched recall for shell locking, and none took a claim ([[live2_house_facts_brain_6_bare_0_of_25_only_skip_ci_surfaced_2026_11_09]]).


The claim has to land in the store everyone else reads. A script inherits the mesh store from whoever runs it, exactly as it finds it: it does not set, change or clear AGENT_MESH_HOME and passes no --db. A sandboxed agent told to keep its work "inside this folder" tends to invent a store there (`AGENT_MESH_HOME=$PWD/.mesh`), and its claim is then invisible to every other agent. With this sentence in the rule lines, Codex trap passes went from 14 to 20 of 20 (LIVE15, 9 Nov, [[live15_codex_inherit_store_clause_20_vs_14_of_20_traps_2026_11_09]]).
