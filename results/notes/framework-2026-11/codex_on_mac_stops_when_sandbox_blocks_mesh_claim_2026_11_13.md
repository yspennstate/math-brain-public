---
name: codex_on_mac_stops_when_sandbox_blocks_mesh_claim_2026_11_13
description: "[VERIFIED] Codex exec on a Mac quit after 10 min writing nothing ('AGENTS.md requires a mesh claim ... sandbox rejected shared database writes'): the parent must hold the claim and say so in the prompt"
status: verified
metadata:
  type: feedback
---
13 Nov 2026, Mac mini 1, STRAT17 (codex exec -s workspace-write, ~/agent_run/STRAT17): after 75k tokens of read-only work it
stopped with "OPEN: STRAT17 remains incomplete because your supplied AGENTS.md requires a mesh claim before writing, and the sandbox
rejected the shared database writes as read-only". No LOG.md, no proof files. STRAT7-16 in the same setup had not hit this.
**Why:** the machine-wide AGENTS.md mesh rule reaches the Codex worker, but workspace-write blocks agent_mesh.py's database outside -C.
**How to apply:** before launching a sandboxed Codex worker, take the mesh claim yourself (e.g. topic:<run>-workspace) and write in its
PROMPT: "parent <id> holds claim <clm-...> for every write in this folder; you need not run agent_mesh.py; the sandbox refusing it is
expected". A stopped run can be resumed in the same session: codex exec ... resume <session id> - < RESUME.md (session id is in the
log head). Check a worker by its final message, not by log bytes. Related: [[t104_split25_34_lowers_proved_strat16_2026_11_13]].
