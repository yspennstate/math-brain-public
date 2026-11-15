---
name: signed_cache_hook_spent_18_ms_re_dumping_2mb_per_call_2026_11_11
description: "project_memory_hot_hook 81 ms per tool call? 18.5 ms was re-dumping the 2 MB signed body to recheck its HMAC each call; since 11 Nov 07:35 a keyed MAC of the raw bytes stands in until they change"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:36:11+02:00
  status: verified
  evidence: "hot hook 50/50 guards old+new; 90 replayed calls equal; tamper/key/sidecar controls; live sidecar 07:35:40"
---

project_memory_hot_hook.py runs on every tool call in every Claude and Codex session. Of its ~31 ms of own work, 18.5 ms
went to one line: re-serializing the 2 MB signed body (json.dumps with sort_keys) only to recompute its HMAC, on every
call, although the cache file changes about once an hour. Reading took 4.5 ms, parsing 6.5, the HMAC itself 1.1.

Since 11 Nov 07:35 (an agent) the hook keeps a sidecar, hot-contract-cache.verified, holding
HMAC(key, domain + the file's exact bytes) once a full check has passed. While the bytes are the same, that MAC stands
in for the re-dump; any change to the bytes, a missing or wrong sidecar, or a different key falls back to the full
check. Only a holder of the same key can write a matching sidecar, so the trust model does not change. Backup
project_memory_hot_hook.py.bak_rawmac_20261111.

Checked before landing, on a copy with copied state: the hook's own 50 guards pass on old and new; 90 replayed calls
(2 sessions x 5 working folders x 9 tools, 6 with output) give the same output; a tampered body with the old sidecar
is refused; a garbage sidecar falls back to the full check and is repaired; a wrong key is refused.

The general move: when a hook verifies a signature over a canonical re-serialization, the re-serialization is the
cost, not the HMAC. Key the result to the raw bytes once and reuse it until they change.

