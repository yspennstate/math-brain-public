---
name: frontier_route_bandit_thompson_built_needs_failure_records_2026_11_10
description: "Frontier route choice as a bandit (research statement sec 6)? Built 10 Nov: 06_math_research/frontier/route_bandit.py (order/record/report). Learns little yet: 27 of 243 live routes have any attributed outcome and failed attempts are almost never recorded, so nothing drops; agents must log `record TNNN --route R --outcome tried|useful`"
metadata:
  type: project
  created: 2026-11-10
  status: provisional
  evidence: "an agent loop tick 10 Nov 18:4x; report over 46 rows with live routes; test_route_bandit.py controls pass"
---

The research statement (section 6) asks for route choice on a frontier row as a bandit: Beta posterior per route, Thompson sampling for the order, a route dropped when P(p_r > floor) falls below a level, the record shared across agents and days. Nothing like it existed (grep for thompson/bandit over the frontier folder, complete, rc 1).

Built as a standalone module beside frontier.py, which is unchanged: `python route_bandit.py order T170 [--seed N]`, `record TNNN --route R --outcome useful|tried --by ID`, `report`. Prior = cross-row base rate of finished routes (done/settled vs dead) worth 2 pseudo-attempts, plus half-weight transfer from terminal routes on other rows whose words match (frontier.sim >= 0.34, capped at 4). Data = moves on the row: progress kinds (moved, narrowed, result, partial) are successes, kinds naming a failed attempt are failures; an untagged older move is attributed to its best word-matching route.

Measured 10 Nov: 1,031 terminal routes, base rate 0.859 - generous, because "done" means an assigned step completed, including steps that ended in negative evidence. 46 rows have 243 live routes; 27 have any attributed outcome; 0 are dropped. The bottleneck is the record, not the method: the ledger keeps progress moves but hardly ever a failed attempt on a live route. What would change this: agents logging `tried` outcomes; then rerun `report` and check whether drops agree with routes later marked dead (the validation still to do).

**Validation, same evening (an agent, 20:1x; Downloads/career/drafts_2026-11-10/rs_implement/bandit_backtest_events.py, bandit_events.json).** Pushed first: commit 391185536072 on origin main (Git Data API; blob shas of the three files checked against GitHub equal to local). Then each of the 664 live->dead / live->done transitions in the route ledgers was scored just before its resolving record, with route states, cross-row terminal routes and the row's moves all cut there (584 scorable: 50 dead, 534 done). The posterior mean does not separate them: AUC 0.50 (dead scored no lower than done); 0.61 on the 65 with word transfer (5 dead); 21 had any move data (1 dead). The drop rule flagged none of either. Why: a route's median life from live to closed is 5 min (dead) and 8 min (done) - the ledger writes a route when the attempt is already over, so there is no window in which a prediction could act. A plain date split (bandit_backtest.py, D = 16 Oct .. 1 Nov) has the same cause in another form: no route live at D was ever resolved after D (722 live at 25 Oct, all orphaned; the newest dated route record is 31 Oct). So the bandit is untestable on this record, not refuted. What would make it testable: routes opened as live when ASSIGNED (not when finished) and `tried` moves logged per attempt (rule 8); rerun bandit_backtest_events.py after a week of that.

**Fix landed 10 Nov 20:4x (an agent, brain commit d30ce37905d6):** `frontier.py check TNNN "<route>" --open --by <you>`
writes the route as live at check time when the check does not refuse it (exit 0 or 1; a refusal, exit 2, writes nothing),
and WORKER_RULES rule 2 now tells workers to run check that way. Test: test_frontier_check_open.py. So start times exist
from now on; rerun Downloads/career/drafts_2026-11-10/rs_implement/bandit_backtest_events.py about 17 Nov. If live records
still do not appear, workers are not using the flag: the next step is making --open the default.
