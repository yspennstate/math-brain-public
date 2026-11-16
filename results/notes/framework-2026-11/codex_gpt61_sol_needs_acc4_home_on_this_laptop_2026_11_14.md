---
name: codex_gpt61_sol_needs_acc4_home_on_this_laptop_2026_11_14
description: "[VERIFIED] Codex exec says gpt-6.1-sol 'not supported with a ChatGPT account'? On this workstation the default ~/.codex and acc2/3/5 homes lack it; set CODEX_HOME=~\\.codex-img-acc4 (acc6 has it but is OFF)"
metadata:
  type: reference
  created: 2026-11-15
  created_at: 2026-11-15T00:09:55+02:00
  status: provisional
  evidence: ""
---

14 Nov 2026. codex exec -m gpt-6.1-sol on the default home failed model_not_found. The models_cache.json of .codex-img-acc4 lists gpt-6.1-sol; with $env:CODEX_HOME set to it, -c service_tier="default" and fast_mode false, the audit ran to exit 0 (about 2 h, high effort). features.ultrafast_mode is reported as an unknown key there and ignored. acc6 also lists it but stays off by the author's order. Check models_cache.json of a home before launching a model that a home may not serve.
