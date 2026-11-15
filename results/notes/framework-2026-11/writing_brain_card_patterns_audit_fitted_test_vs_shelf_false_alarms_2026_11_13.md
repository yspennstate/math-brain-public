---
name: writing_brain_card_patterns_audit_fitted_test_vs_shelf_false_alarms_2026_11_13
description: "Writing-brain cards audited 13 Nov: 56 of 301 carry a pattern, all pass their own example (a fitted test); on 1,905 shelf passages no literature pattern fires on more than 0.6 pct; one false alarm (WB-M0006); two mechanical checks handed to agent"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T23:56:29+02:00
  status: verified
  evidence: "my own runs 13 Nov 23:48-23:55 of loops/agent_fork_1113/wb_cardtest.py, wb_cardfire.py 40 22, wb_nopattern.py and proposed_mech_checks.py --selftest (12 of 12) plus five papers under 06_math_research; outputs in session agent's transcript"
---

Audit of the writing brain's cards and page checker on 13 Nov 2026 (an agent, Fable 5.2, read-only; the cards and tools are an agent's).

What was measured
- 301 cards: 82 kind mistake, 219 kind hook. 56 carry a regex pattern (42 mistake, 14 hook). 40 mistake cards have no pattern: all 40 are process or judgment mistakes with a by-hand check (wrong file opened, a scene too thin to picture, a grant that has ended), except a few that can be made mechanical (below).
- Fitted test: every testable pattern fires on its own bad sentence and stays silent on its own better sentence (54 of 54; 2 have neither). This test cannot fail in a useful way: the pattern was written to the sentence.
- False-alarm test, the one that can fail: every 40th passage node of nodes/books (1,905 passages, 199,124 words). 30 of 56 patterns never fire. No literature-wing or all-wing pattern fires on more than 0.6 pct of passages (WB-H0001 0.6, WB-M0002 0.4, WB-H0020 0.4, WB-M0006 0.3). Script-wing patterns fire often on novels (WB-M0019 8.1 pct, WB-M0061 4.1, WB-M0025 3.9), which is no fault: after_page.py only runs cards whose wing is the page's wing or all.
- One real false alarm: WB-M0006 (the text talks about itself) fires on a physical note in dialogue (P-PG98-d00418, "show the door-keeper this note").
- after_page.py has six mechanical checks (headings, hedges, overfull hbox, funding and AI declaration, figures, abstract length). Two more written and handed over, not wired in: mech_i_and_we_both (card WB-M0057) and mech_abstract_has_citation (card WB-M0039), in loops/agent_fork_1113/proposed_mech_checks.py. Controls 12 of 12 both ways; on five real papers under 06_math_research three hits, all true (two papers mix I and we, one abstract carries an arXiv id), no false hit.

**Why:** the request behind it: AI keeps making very simple mistakes in writing, and the Fable agents audit what the other agents built.

**How to apply:** when auditing a pattern check, do not stop at the card's own example. Run every pattern over a sample of good published prose of the same wing and read the hits: the share that fires is the false-alarm rate, and each hit read by eye is either a fault in the pattern or a rule the shelf does not keep. Tools: loops/agent_fork_1113/wb_cardtest.py (fitted), wb_cardfire.py STEP TOP (false alarms), wb_nopattern.py (cards with no pattern). A threshold check with no way to calibrate it (the all-symbols card WB-M0080) was left unwritten on purpose.

