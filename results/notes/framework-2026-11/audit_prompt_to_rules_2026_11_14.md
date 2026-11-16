---
name: audit_prompt_to_rules_2026_11_14
description: "Audit 14 Nov of the agents turning the owner's prompts into rules/hooks/cards: agent briefs stored as the user's words (72 relabelled), correction flag 238->760, H20 reflexes fire on 1 in 6 tool calls, reflex pre-check 197->162 ms"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T03:11:04+02:00
  status: verified
  evidence: "REPORT.md under audits/reports/2026/11/14/prompt_to_rules_audit; commits bb02b9ef ec401ed2"
---

Audit of the agents that read the owner's prompts and turn them into rules, hooks and brain cards (13-14 Nov,
requested as a ten-day audit-and-help task).
Report: 12_cognitive_architecture/audits/reports/2026/11/14/prompt_to_rules_audit/REPORT.md (evidence/, scripts/).

What it found and what was done:
1. Agent-written briefs ("You are role N of ten...", "HOURLY FLEET CHECK") sat in PROMPTS.jsonl with origin owner, so
   rules mined from them carried an agent's words as the owner's. prompt_origin.is_agent_authored now knows worker briefs; 72
   rows relabelled to automation. Mechanism: [[agent_text_counted_as_his_words_2026_11_14]].
2. The correction flag in owner_prompt_subconscious/build.py caught under half the owner's corrections. Two passes of new
   phrase shapes: 238 -> 723 -> 760 flagged of 15,060 distinct prompts (second pass from an agent's recount;
   23 of 25 read were corrections). See [[prompt_store_correction_flag_misses_half_2026_11_14]].
3. The H20_1112 reflex batch puts a candidate on about 1 in 6 tool calls (33,582 measured); sent to its owner
   an agent.
4. Speedup landed: the reflex pre-check keeps up to three required pieces per trigger, 197 -> 162 ms of matching per
   tool call, 0 fires lost. See [[reflex_prefilter_three_pieces_edits_live_at_compile_2026_11_14]].

Still open: the store build reads the whole 262 MB ledger every time (958 s); an incremental tail read is next.
Status: findings measured on live data; fixes 1, 2 and 4 pushed (bb02b9ef, ec401ed2).

