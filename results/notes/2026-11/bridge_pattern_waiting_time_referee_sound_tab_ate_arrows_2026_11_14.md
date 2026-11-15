---
name: bridge_pattern_waiting_time_referee_sound_tab_ate_arrows_2026_11_14
description: "Posted paper PDF shows 'o' or a missing symbol? A script wrote \\t (\\to became TAB+o) - grep .tex for control chars. Bridge-pattern waiting time refereed 14 Nov: SOUND, arrows + Lemma 4.3 fixed (f3c8d2a), gamma_0 1.5439 rechecked"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T11:53:34+02:00
  status: provisional
  evidence: ""
  lesson: true
---

A posted paper can carry LaTeX commands that a script broke: in bridge-pattern-waiting-time (posted 433f9f9) three `\to` had become a backslash, a TAB character and "o", because a Python script wrote "\t" inside an ordinary string. The PDF showed "o" where the arrow should be, and nothing failed at compile time. The same happens to `\frac` (form feed), `\beta`/`\bar`/`\begin` (backspace), `\rho`/`\right` (carriage return), `\nu`/`\newline` (newline) and `\varphi`/`\vec` (vertical tab). Before posting, and when refereeing a posted paper, grep the .tex for control characters (TAB, FF, BS, VT, BEL, a CR that is not a line ending) and for a backslash at the end of a line. Write LaTeX through a file-writing tool or a raw string, never an ordinary quoted string.

The referee pass itself (14 Nov 2026, an agent): verdict SOUND. The paper proves E T_n ~ gamma_lambda n for the first time the last n steps of simple random walk form a bridge to the level nearest lambda sqrt(n), with gamma_lambda = 1 + E F_lambda for the Slepian process B(t+1)-B(t). This answers Pitman-Tang Open problem 2.3 (arXiv:1411.0041). Fixes in commit f3c8d2a: the three arrows, and `\cite[Lemma~2.3]{PTS}` changed to Lemma 4.3 (Pitman-Tang-Shepp, arXiv:1411.0040, EJP 2015, numbers it 4.3 in both versions).

Independent checks: Table 1 recomputed by first-step analysis on the last n-1 letters, every entry equal (lambda=1, n=4: 469/52). Exact E T_n/n for lambda=0 at n=10..20 by value iteration (2^19 states at n=20) is 1.53215 ... 1.53775, which extrapolates to 1.5436-1.5454 against the paper's 1.54388. A sparse direct solve at n=20 ran out of 15 minutes; value iteration took about a minute.

Not checked: Shepp 1971 equation numbers and the published Seminaire numbering (publisher pages). Report: 06_math_research/referee_reports/2026-11-14/BPWT_posted_referee/REPORT.md.


Related: [[divisible_sandpile_critical_tail_referee_sound_three_refs_added_2026_11_14]] [[a_card_that_drops_input_must_name_it_2026_11_14]] [[research_writing_human_voice_2026_06_10]]
