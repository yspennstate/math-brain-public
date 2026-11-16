---
name: writing_sessions_never_run_the_page_check_2026_11_14
description: "Why do simple writing mistakes still reach the author? Of five sessions told about the writing brain that then edited papers (36 h to 14 Nov), none ran after_page.py or writing_recall.py; whole-file checks never ran; the after-write check built for it went live 14 Nov 01:14 (hook writing_brain_page_check.py)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T00:42:27+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-13T23:18:31.750Z
---

Why do simple writing mistakes still reach the author when the author's rules are on cards? Because the sessions that write do not run the check (14 Nov 2026, an agent).

- Measured on the Claude transcripts of the 36 hours to 14 Nov 00:20 (wb_usage_audit.py, last 300 MB of each; Codex and subagent transcripts not read): 13 sessions were told about the writing brain by its hook. Five then edited prose (main.tex 130, 92, 44, 25 edits, and one draft 3). Calls from those five to after_page.py: 0. To writing_recall.py: 0. The only sessions that ran the tools were the three that build the writing brain.
- What reached those edits anyway: the hook runs the pattern cards on the text of each Write or Edit. What never ran: every whole-file check (I and we both, a citation in the abstract, funding and declaration lines, heading templates, hedge counts) and every by-hand card.
- The cards themselves are sound ([[writing_brain_card_patterns_audit_fitted_test_vs_shelf_false_alarms_2026_11_13]]) and hold the author's corrections ([[prompt_store_correction_flag_misses_half_2026_11_14]]). The gap is delivery.
- Proposed and tested (11 of 11), sent to an agent, not wired by me: proposed_page_check_after_write.py in 12_cognitive_architecture/loops/agent_fork_1113/ runs the whole-file checks after a Write or Edit of a prose page, at most three cards, once per session and file until the count changes.
- Two false alarms found on real papers: WB-M0016 counts headings opening with A or The; WB-M0024 (wing all) fires on a paper's pdfauthor line.
- THE FIX LANDED (14 Nov 01:14, an agent, commit 1f1a176c464d): the check is writing_brain/tools/page_check_after_write.py, live copy ~/.claude/dreaming/writing_brain_page_check.py, listed under PostToolUse Write|Edit in hook_dispatch_list.json. Their test at the receiver: an Edit of one clean line of a test paper brought back WB-M0057 and WB-M0039; 0.3 s an event. Both false alarms are fixed (the heading check skips A, An, The, Proof; WB-M0024 moved to wing script). Not yet measured: whether the sessions that write papers now act on what it shows. Re-run wb_usage_audit.py on or after 15 Nov and count the check's lines in their transcripts.

**Why:** the author's 13 Nov 23:33 word: AI keeps making very simple mistakes in writing and the author is trying to solve that.

**How to apply:** a tool an agent is invited to run is not a check. When a rule matters, measure whether the sessions it is for call the tool (count the calls in their transcripts), and if they do not, make the check run on the event itself. Before blaming missing rules, count the uses of the rules that exist. My selftest for the proposal failed first on its own clock: it started at t = 1000 s, inside the 1200 s cooldown of an empty state; give a cooldown test a start time larger than the cooldown.

