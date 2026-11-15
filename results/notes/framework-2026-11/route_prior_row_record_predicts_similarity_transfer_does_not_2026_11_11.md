---
name: route_prior_row_record_predicts_similarity_transfer_does_not_2026_11_11
description: "Frontier route chooser prior (statement sec 6): does similarity transfer from other rows help, and should a live route's prior use its own row's finished routes? Transfer: no (log-loss 0.4064 vs 0.4071 base, CI spans 0). Row record: yes, leave-one-out 0.3488 and forward in time 0.3610 vs 0.4006 (CI -0.065..-0.015); done 92.7 pct after all-done siblings vs 82.7 pct after a dead one. Suggested prior (row done + 4 p0)/(row finished + 4); route_bandit.py not edited, sent to its owner."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:32:40+02:00
  status: verified
  evidence: "prior_components.json (leave-one-out, 1,031 routes, row bootstrap 2,000) and prior_forward.json (earlier-stamped routes only) under brain_improvement/rs_implement_21ba_2026_11_10"
---

Statement section 6 says the route chooser "learns each route's success rate". The deployed prior for a live route (route_bandit.py) is the cross-row base rate with mass 2 plus up to 4 pseudo-attempts from similar finished routes on OTHER rows; the same row's finished routes are not used. Checked 11 Nov 03:2x on the 1,031 finished routes of 66 rows (886 done or settled, 145 dead; a "success" here is a route that ended done, not a solved problem).

**Similarity transfer adds nothing measurable.** Leave-one-out log-loss 0.4064 against 0.4071 for the base rate alone; difference -0.0007, interval over rows [-0.0034, +0.0019]. Only 207 of 1,031 routes have any similar finished route elsewhere and 2 reach the cap.

**The row's own finished routes do predict.** Leave-one-out, shrunk to the base rate with mass 4: log-loss 0.3488, difference -0.058 [-0.095, -0.026]; Brier 0.105 against 0.121. Rows differ more than chance allows (chi-square 225 on 62 degrees of freedom; 25 of 63 rows with two or more routes have no dead route).

**It holds forward in time.** Leave-one-out lets a route be predicted from siblings that ended after it. Ordering the routes by their stamp (as instants; the stamps carry mixed UTC offsets) and predicting each from earlier-stamped routes only, ties unused: base 0.4006, row prior with mass 4 0.3610, difference -0.040 [-0.065, -0.015] on 1,000 scored routes. In counts: a route ends done 92.7 pct of the time when every earlier route on its row did (341 routes) and 82.7 pct when one had died (562).

**Size of the doubt.** The record carries one stamp a route ("at"); if it is the registration time, an earlier-stamped sibling may have ended later. 289 routes share a stamp with a sibling (bulk filing), and those are predicted without each other. All stamps fall between 14 and 31 October. The gain is about a tenth of the log-loss: a better prior, not a different chooser.

**What follows.** A live route's prior should start from its row's record, (row successes + 4 p0) / (row finished + 4), in place of p0; the similarity transfer can stay or go, it does not move the score. I did not edit route_bandit.py (not mine without a claim); the result went to the frontier owner. What would change this: an end-time stamp on routes (rerun prior_forward.py), or a backtest of the chooser's picks with the row prior in place.

Files: brain_improvement/rs_implement_21ba_2026_11_10/prior_components.py and .json (leave-one-out), prior_forward.py and .json (forward). Related: [[frontier_route_drop_rule_never_fires_and_has_no_long_run_guarantee_2026_11_11]], [[record_vs_no_record_frontier_test_kit_ready_no_runs_yet_2026_11_11]].


**Addendum, 11 Nov 04:16: on resolve times, and what it changes in the chooser.** Replaying the dated route records (chooser_row_prior_events.py: 584 routes scored one second before their resolving record, from earlier records only; 50 dead, 534 done, 59 rows) gives the same forecast result: base 0.3401, deployed prior 0.3377 (difference -0.0025, interval over rows [-0.0065, +0.0016]), row prior with mass 4 0.2958 (-0.044, [-0.077, -0.009]). A route ends done 95.2 pct of the time after an all-done row record (250 routes) and 87.8 pct after a death on the row (286). That removes the one-stamp doubt above. The gain is all between rows: the row prior puts a done route above a dead route of another row 70 pct of the time (deployed 50 pct) and says nothing within a row, where it is one number for every live route (the same-row figure, 0.33 on 683 pairs, is below one half because a death lowers the score of the routes after it and not its own; my reading, not a measured within-row effect). The chooser only orders the live routes of one row, so swapping the prior changes none of its picks: 496 of the 584 routes had live siblings, and in 67 could the deployed posterior differ from a sibling's at all. The drop rule flags no route under either prior. So "what follows" above is narrower than written: the row prior corrects the printed mean; it does not change route choice. A row-level rate would matter only for which row gets worker time, which no code decides today, and a low done rate can mark a hard problem or careful bookkeeping, so it is no case for moving hours. Sent to the frontier owner. Files: chooser_row_prior_events.py, .json, .txt in the same folder.
