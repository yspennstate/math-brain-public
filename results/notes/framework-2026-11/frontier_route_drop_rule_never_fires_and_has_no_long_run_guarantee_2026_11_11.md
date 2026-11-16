---
name: frontier_route_drop_rule_never_fires_and_has_no_long_run_guarantee_2026_11_11
description: "Frontier route drop rule (P(p>0.10)<0.05 in route_bandit.py): does it fire, and can it wrongly drop a good route? It never fires today: 40 straight failures needed, no live route has more than 4 attempts (243 live, 27 with any). Over a long run the fixed level wrongly drops a route at the floor 5 pct by 100 attempts, 24 pct by 2,000; an e-value rule holds 5 pct forever for 43 failures instead of 40"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:38:25+02:00
  status: verified
  evidence: "drop_rule_anytime.json (exact DP) and a 40,000-path simulation agree: wrong drop at the floor 0.053 by 100 attempts, 0.095 by 200; record count 243 live routes, max 4 own attempts, 0 drops"
---

Statement section 6 asks for the route choice to be "a decision rule whose regret I can bound" and says "a route is dropped when the posterior probability that p_r exceeds a floor falls below a fixed level". route_bandit.py does that with FLOOR 0.10, LEVEL 0.05, prior mass 2 at the cross-row base rate. Checked 11 Nov 02:3x (drop_rule_anytime.py, exact dynamic programming over successes and failures; a 40,000-path simulation agrees to the third decimal).

**What the rule does today: nothing.** The base rate is 0.859 (886 of 1,031 terminal routes ended as successes), so the prior is Beta(1.72, 0.28) and a route needs 40 straight failures of its own to be dropped (36 with the full 4 transferred failures; 28 under a flat prior). On the record: 422 rows, 243 live routes, 27 with any attempt of their own, the most attempts on one route is 4. Neither the deployed rule nor any rule at level 0.05 drops a single route. Routes leave the live set because a worker marks them dead with a reason, not because of the posterior. The Thompson order is the part of the chooser that acts.

**Straight failures needed, by floor** (deployed prior / flat prior / anytime rule): 0.1: 40 / 28 / 43; 0.2: 19 / 13 / 20; 0.3: 12 / 8 / 13; 0.5: 6 / 4 / 7; 0.7: 3 / 2 / 4. With at most 4 attempts a route, a statistical drop at 5 pct needs a floor near 0.5 or above, which would be a different claim about what a route is worth.

**The fixed level has no guarantee over a long run.** The rule is looked at after every attempt and a drop is final. For a route whose true rate sits at the floor the chance of a wrong drop is 1.5 pct by 50 attempts, 5.3 by 100, 9.5 by 200, 15.5 by 500, 24.4 by 2,000, and it keeps rising. At rate 0.11: 7.7 pct by 2,000. At 0.125: 2.0 pct. At 0.15: 0.4 pct. So the damage is confined to routes within about a quarter of the floor.

**A rule with a guarantee costs little.** Drop when E_n = (1/q) int_0^q p^s (1-p)^f dp / (q^s (1-q)^f) >= 1/LEVEL, q the floor. For every true rate at or above q, E_n is a nonnegative supermartingale started at 1 (each term has one-step mean 1 + (p-q)(p1/q - (1-p1)/(1-q)) <= 1 for p1 < q), so by Ville the chance of ever dropping such a route is at most LEVEL. Computed: 4.05 pct by 2,000 attempts at the floor, 1.5 pct at 0.11. Cost on bad routes: rate 0: 43 attempts against 40; rate 0.02: mean 72 against 57; rate 0.05: 209 against 123; rate 0.08: 1,272 against 558 (capped at 2,000).

**Regret.** On the event that no route at or above the floor is ever dropped, Thompson's bound applies unchanged; the wrong-drop event adds at most LEVEL x T x the largest gap, which is linear in T with a 5 pct constant. A sublinear bound needs the level to shrink like 1/T, which adds about ln(T/20)/0.105 failures to the 43.

**What would change this:** routes that collect tens of attempts (a route defined as a method family across rows, or transfer uncapped), or a floor near 0.5. Until then the drop rule is a sentence in the statement, not a mechanism, and the statement should say the order is what is tested.

Files: brain_improvement/rs_implement_21ba_2026_11_10/drop_rule_anytime.py, .json. route_bandit.py was not edited.

