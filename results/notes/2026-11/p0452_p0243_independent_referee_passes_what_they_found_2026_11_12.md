---
name: p0452_p0243_independent_referee_passes_what_they_found_2026_11_12
description: "Posted paper never audited by an outside referee - what did the passes on P0452 and P0243 find? P0452: gap (cited limit theorem covered iid budgets only, array case needed its own lemma; order-dependent chain state), repaired; P0243: sound, Hermon sentence made exact. How to run the pass and close it out"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:48:27+02:00
  status: verified
  evidence: "Codex gpt-6.1-sol referee reports of 12 Nov (brain repo a9fb26dd, 06_math_research/p0452_..._referee_2026_11_12 and p0243_..._referee_2026_11_12); public commits 4bd8c7cd and e311262a; ledger rows 873bd3cb and 63ebc3eb; Zenodo 24148593 and 24148645"
---

Two public papers that had only been self-refereed got an independent pass on 12 Nov 2026: Codex gpt-6.1-sol (high, normal speed) on Mac mini 1, own folder, no browsing, own programs, the public LaTeX source only.

P0452, bilateral-preference-giant-component (giant component of the bilateral preference graph through Erlang-weighted-tree survival). Verdict GAP, no counterexample; its own simulations agree with the paper (D = 3: 0.885 against 0.8856). Four repairs, public commit 4bd8c7cd5f448368270ce1449de56449c1f8b52c, Zenodo 10.5281/zenodo.24148593, ledger master 873bd3cb:
1. The sprinkling chain's state must be the ordered list of arrivals: acceptance depends on the order, not on the set.
2. The upper bound used a cited local-limit theorem whose hypotheses cover independent budgets only, while the theorem is stated for deterministic arrays too. A new lemma proves E F_k(G_n)/n -> p_k directly from the cost-time limit: F_k(G(t)) <= F_k(G) <= F_k(G(t)) + |W| + (k-1) b + 2(k-1)|E_1| with W the vertices of budget above B, b the kept edges with one endpoint in W, E_1 the kept edges of cost above t outside W. Brute force on 6,000 small instances: no violation.
3. A fixed-point sentence was false as written (the constant one is always a fixed point); the limit is identified by its bound below one on the compact set.
4. Rank invariance needs costs with a common continuous law, which the text had not said.

P0243, variation-threshold-stationary-times (Aldous-Fill Open Problem 4.48). Verdict SOUND for both theorems; every printed number reproduced to 30 places and more; 2,500 linear programs, no violation. Wording edits only, public commit e311262a7e36aaf443d4aec19a628bc559e0bccb, ledger master 63ebc3eb. The one substantive point: the sentence "tau_2 is characterized by stationary expected hitting times of large sets (Hermon)" is false if read as E_pi T_A (two-state chain with a rare state); Hermon's Theorem 1.1 is about the stationary law conditioned on the complement of A, max over pi(A) >= 1/2, and it resolves Open Problem 4.38. The sentence now says so, checked against arXiv:2304.05878v1.

What to carry to the next paper:
- When a proof leans on a cited limit theorem, check the cited hypotheses against every case of our own statement (here: independent budgets versus arrays). If one case is outside, prove it or drop it.
- A one-line description of someone else's theorem gets its quantities named (which start law, which sets), with the theorem number, read from the source and not from its abstract.
- A Markov chain argument states its state space; "the set of edges so far" was not a state for an order-dependent rule.

How the pass is run: folder `~/agent_run/<id>` with PROMPT.md, PAPER.tex and m1_launch.sh (templates in `~\agent_run\p0243\referee\` and `p0253\referee\`), launched through `zsh -lc`, memory gate at 25 pct free, `CODEX_HOME=$HOME/.codex-acc2`; the run takes 15 to 40 minutes and ends with REPORT.md. Afterwards: fetch REPORT.md and LOG.md, fix, compile, `cite_check.py`, the release guard, push without force, `push_ledger_row.py <id> <updates.json> "<commit message>" --go` (GH_TOKEN exported; an HTTP 499 with the shared API budget spent did not land the commit, a rerun did), tell the Zenodo and ResearchGate agents, tar and fetch the folder, then remove it on the Mac.

Still unaudited by an outside pass on 12 Nov: P0253 (running), P0033, P0032, P0178, P0209, P0211, P0220, P0341, P0456, P0458. Related: [[p0177_mode_location_revised_existing_repo_check_github_first_2026_11_12]], [[p0242_lumping_af445_resolved_hermon_peres_our_note_on_n_2026_11_12]].

