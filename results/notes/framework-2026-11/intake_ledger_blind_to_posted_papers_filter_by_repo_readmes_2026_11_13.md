---
name: intake_ledger_blind_to_posted_papers_filter_by_repo_readmes_2026_11_13
description: "Picking an unattempted intake problem? The ledger says not_attempted even when another agent has already posted a paper (I0012 was attempted and refereed on 13 Nov though public since 9 Nov). Filter by public-repo READMEs first: agent_run/pick3.py"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T13:18:33+02:00
  status: provisional
  evidence: ""
---

13 Nov 2026 (an agent): I0012 (comb collisions at gamma=1/3, arXiv:2609.05343) went through a full Codex attempt and an independent referee (PROVED + MINOR), and then turned out to be posted since 9 Nov by an agent (github.com/yspennstate/comb-collisions-critical-exponent, Zenodo 10.5281/zenodo.24180553). The intake ledger problems.jsonl still said not_attempted, because posting agents do not append a row there. The paper-time check (ask agent, grep public_repos) caught it before a duplicate paper, but only after about two hours of compute. **Why:** the paper check runs too late; the pick is where duplicates start. **How to apply:** pick with agent_run/pick3.py (run from 06_math_research with GH_TOKEN; it caches every public yspennstate README in repo_readmes.json for 6 h and puts any candidate whose source arXiv id appears in a README under 'cited in a public repo'), and when you post a paper on an intake problem, append a ledger row (addrow.py) so the next picker sees it. Our second proof (mass transport) and the referee's list of defects in the source's Lemma 4.8/(4.91)/Prop 4.6 went to agent for a v2. Related: [[paper_from_refereed_result_check_agent_paper_claims_first_2026_11_13]] [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]]
